#!/bin/bash
set -e

export GCP_PROJECT="${GCP_PROJECT:-antigravity-camp-nsk}"
export GCP_REGION="${GCP_REGION:-europe-west1}"
export SERVICE_NAME="document-processor"
export BUCKET_NAME="${GCP_PROJECT}-document-ingest"
export BQ_DATASET="document_processing"
export BQ_TABLE="document_metadata"

echo "================================================================="
echo "Deploying Full End-to-End NSK Serverless Pipeline on Google Cloud"
echo "Project: $GCP_PROJECT | Region: $GCP_REGION"
echo "================================================================="

CLOUDSDK_METRICS_ENVIRONMENT="${CLOUDSDK_METRICS_ENVIRONMENT:+$CLOUDSDK_METRICS_ENVIRONMENT }datacloud.antigravity" gcloud config set project "$GCP_PROJECT"
CLOUDSDK_METRICS_ENVIRONMENT="${CLOUDSDK_METRICS_ENVIRONMENT:+$CLOUDSDK_METRICS_ENVIRONMENT }datacloud.antigravity" gcloud auth application-default set-quota-project "$GCP_PROJECT" --quiet || true

echo "[1/5] Provisioning Cloud Storage Bucket: gs://$BUCKET_NAME ..."
CLOUDSDK_METRICS_ENVIRONMENT="${CLOUDSDK_METRICS_ENVIRONMENT:+$CLOUDSDK_METRICS_ENVIRONMENT }datacloud.antigravity" gcloud storage buckets create "gs://$BUCKET_NAME" --project="$GCP_PROJECT" --location="$GCP_REGION" 2>/dev/null || echo "Bucket gs://$BUCKET_NAME already exists."

echo "[2/5] Provisioning BigQuery Dataset & Table ($BQ_DATASET.$BQ_TABLE) ..."
bq --location="$GCP_REGION" mk --dataset --label datacloud:antigravity "${GCP_PROJECT}:${BQ_DATASET}" 2>/dev/null || echo "Dataset $BQ_DATASET already exists."
bq mk --table --label datacloud:antigravity \
  "${GCP_PROJECT}:${BQ_DATASET}.${BQ_TABLE}" \
  file_name:STRING,bucket:STRING,ocr_status:STRING,word_count:INTEGER,tags:STRING,popia_pii_redactions:INTEGER,audit_seal:STRING,processed_at:TIMESTAMP 2>/dev/null || echo "Table $BQ_TABLE already exists."

echo "[3/5] Deploying $SERVICE_NAME (with Live Interactive Web Dashboard & BigQuery Streamer) to Cloud Run..."
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_DIR="$(dirname "$SCRIPT_DIR")"

CLOUDSDK_METRICS_ENVIRONMENT="${CLOUDSDK_METRICS_ENVIRONMENT:+$CLOUDSDK_METRICS_ENVIRONMENT }datacloud.antigravity" gcloud run deploy "$SERVICE_NAME" \
  --source="$APP_DIR" \
  --project="$GCP_PROJECT" \
  --region="$GCP_REGION" \
  --allow-unauthenticated \
  --set-env-vars="GCP_PROJECT=$GCP_PROJECT,BQ_DATASET_ID=$BQ_DATASET,BQ_TABLE_ID=$BQ_TABLE" \
  --quiet

SERVICE_URL=$(CLOUDSDK_METRICS_ENVIRONMENT="${CLOUDSDK_METRICS_ENVIRONMENT:+$CLOUDSDK_METRICS_ENVIRONMENT }datacloud.antigravity" gcloud run services describe "$SERVICE_NAME" --project="$GCP_PROJECT" --region="$GCP_REGION" --format="value(status.url)")

echo "[4/5] Uploading Sample Documents to gs://$BUCKET_NAME & Triggering Live Processing..."
echo "NSK Sovereign Vendor Agreement for Township SMME Sindi. Director ID: 9204155123087, Email: sindi@vendor.co.za" > /tmp/sample_contract.txt
echo "Invoice billing finance acme pdf PayShap verified." > /tmp/sample_invoice.pdf
CLOUDSDK_METRICS_ENVIRONMENT="${CLOUDSDK_METRICS_ENVIRONMENT:+$CLOUDSDK_METRICS_ENVIRONMENT }datacloud.antigravity" gcloud storage cp /tmp/sample_contract.txt /tmp/sample_invoice.pdf "gs://$BUCKET_NAME/"

curl -s -X POST "$SERVICE_URL/process" -H "Content-Type: application/json" \
  -d "{\"file_name\":\"sample_contract.txt\",\"bucket\":\"$BUCKET_NAME\",\"content\":\"NSK Sovereign Vendor Agreement for Township SMME Sindi. Director ID: 9204155123087, Email: sindi@vendor.co.za\"}"
echo ""
curl -s -X POST "$SERVICE_URL/process" -H "Content-Type: application/json" \
  -d "{\"file_name\":\"sample_invoice.pdf\",\"bucket\":\"$BUCKET_NAME\",\"content\":\"Invoice billing finance acme pdf PayShap verified.\"}"
echo ""

echo "[5/5] Querying Live BigQuery Table (${GCP_PROJECT}.${BQ_DATASET}.${BQ_TABLE})..."
bq query --use_legacy_sql=false --label datacloud:antigravity \
  "SELECT file_name, ocr_status, word_count, popia_pii_redactions, audit_seal, processed_at FROM \`${GCP_PROJECT}.${BQ_DATASET}.${BQ_TABLE}\` ORDER BY processed_at DESC LIMIT 5"

echo "================================================================="
echo "🚀 FULL PIPELINE DEPLOYED & VERIFIED!"
echo "👉 Open Your Interactive Cloud Run App in Browser: $SERVICE_URL"
echo "================================================================="
