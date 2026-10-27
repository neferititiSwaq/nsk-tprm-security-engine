import os
import json
import base64
import hashlib
import hmac
import re
import logging
from datetime import datetime, timezone
from flask import Flask, request, jsonify, render_template_string
from google.cloud import bigquery

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

PROJECT_ID = os.environ.get("GCP_PROJECT", "antigravity-camp-nsk")
BQ_DATASET = os.environ.get("BQ_DATASET_ID", "document_processing")
BQ_TABLE = os.environ.get("BQ_TABLE_ID", "document_metadata")

# POPIA Section 19 PII Sanitization Regex Patterns
SA_ID_PATTERN = re.compile(r"\b\d{13}\b")
EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

STOPWORDS = {"the", "and", "for", "with", "this", "that", "from", "into", "shall", "are"}


def sanitize_popia_pii(text: str) -> tuple[str, int]:
    """Masks South African 13-digit IDs and emails before cloud processing."""
    redactions = len(SA_ID_PATTERN.findall(text)) + len(EMAIL_PATTERN.findall(text))
    sanitized = SA_ID_PATTERN.sub("[REDACTED_SA_ID]", text)
    sanitized = EMAIL_PATTERN.sub("[REDACTED_EMAIL]", sanitized)
    return sanitized, redactions


def extract_tags(text: str, top_n: int = 5) -> list[str]:
    words = [w.lower() for w in re.findall(r"[a-zA-Z]{4,}", text) if w.lower() not in STOPWORDS]
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    sorted_words = sorted(counts.keys(), key=lambda k: (-counts[k], k))
    return sorted_words[:top_n] if sorted_words else ["compliance", "document", "sovereign", "audit"]


def generate_hmac_seal(payload_str: str) -> str:
    secret = os.environ.get("NSK_SEAL_SECRET", "nsk-sovereign-tprm-camp-2026").encode("utf-8")
    digest = hmac.new(secret, payload_str.encode("utf-8"), hashlib.sha256).hexdigest()
    return f"NSK-SEAL-2026-{digest[:16].upper()}"


def stream_to_bigquery(record: dict) -> str:
    """Streams extracted document metadata directly into BigQuery."""
    try:
        client = bigquery.Client(project=PROJECT_ID)
        table_id = f"{PROJECT_ID}.{BQ_DATASET}.{BQ_TABLE}"
        row = {
            "file_name": record["file_name"],
            "bucket": record["bucket"],
            "ocr_status": record["ocr_status"],
            "word_count": record["word_count"],
            "tags": json.dumps(record["tags"]),
            "popia_pii_redactions": record["popia_pii_redactions"],
            "audit_seal": record["audit_seal"],
            "processed_at": record["processed_at"],
        }
        errors = client.insert_rows_json(table_id, [row])
        if errors:
            logging.warning(f"BigQuery streaming warnings: {errors}")
            return "BQ_WARNING"
        logging.info(f"Successfully streamed metadata for {record['file_name']} to BigQuery {table_id}")
        return "STREAMED_TO_BIGQUERY"
    except Exception as exc:
        logging.warning(f"BigQuery stream skipped/fallback: {exc}")
        return "LOCAL_FALLBACK"


DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>NSK Sovereign Cloud Run Document & TPRM Pipeline</title>
  <style>
    body { background: #0a0e17; color: #f8fafc; font-family: system-ui, -apple-system, sans-serif; margin: 0; padding: 32px; }
    .container { max-width: 860px; margin: 0 auto; background: #111827; border: 1px solid #d4af37; border-radius: 12px; padding: 28px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    h1 { color: #d4af37; margin-top: 0; font-size: 1.6rem; }
    .badge { display: inline-block; background: #065f46; color: #34d399; padding: 4px 12px; border-radius: 999px; font-size: 0.82rem; font-weight: 600; margin-bottom: 16px; }
    label { display: block; margin-top: 14px; font-weight: 600; color: #cbd5e1; font-size: 0.9rem; }
    input, textarea { width: 100%; box-sizing: border-box; margin-top: 6px; padding: 10px; border-radius: 8px; border: 1px solid #334155; background: #1e293b; color: #fff; font-family: monospace; }
    button { margin-top: 18px; background: #d4af37; color: #0a0e17; border: none; padding: 12px 22px; border-radius: 8px; font-weight: 700; cursor: pointer; font-size: 0.95rem; }
    button:hover { background: #eab308; }
    pre { background: #020617; border: 1px solid #1e293b; padding: 16px; border-radius: 8px; overflow-x: auto; color: #38bdf8; margin-top: 20px; }
  </style>
</head>
<body>
  <div class="container">
    <span class="badge">● LIVE ON GOOGLE CLOUD RUN ({{ project }})</span>
    <h1>NSK Sovereign Serverless Document & TPRM Pipeline</h1>
    <p style="color:#94a3b8;">Ingests vendor compliance documents, enforces POPIA Section 19 PII sanitization, extracts metadata, generates an HMAC-SHA256 Cryptographic Seal, and streams to BigQuery.</p>

    <label>Document Filename (GCS Object):</label>
    <input id="file_name" value="sindi_cipc_vendor_contract.txt" />

    <label>Document Content (Includes Simulated SA ID & Email to Test POPIA Redaction):</label>
    <textarea id="content" rows="4">NSK Sovereign Vendor Agreement for Township SMME Sindi. Director SA ID: 9204155123087, Contact: sindi@township-tech.co.za. Verified for PayShap enterprise settlement and cloud security compliance.</textarea>

    <button onclick="runPipeline()">⚡ Trigger Cloud Run Document Audit & Stream to BigQuery</button>

    <pre id="output">// Click the button above to trigger your live Cloud Run microservice...</pre>
  </div>

  <script>
    async function runPipeline() {
      const out = document.getElementById('output');
      out.textContent = 'Processing on Google Cloud Run & streaming to BigQuery...';
      const res = await fetch('/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          file_name: document.getElementById('file_name').value,
          bucket: '{{ project }}-document-ingest',
          content: document.getElementById('content').value
        })
      });
      const data = await res.json();
      out.textContent = JSON.stringify(data, null, 2);
    }
  </script>
</body>
</html>
"""


@app.route("/", methods=["GET"])
def index():
    if "text/html" in request.headers.get("Accept", ""):
        return render_template_string(DASHBOARD_HTML, project=PROJECT_ID)
    return health_check()


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "service": "document-processor",
        "engine": "NSK Sovereign Serverless Document & TPRM Pipeline",
        "project": PROJECT_ID,
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


@app.route("/", methods=["POST"])
@app.route("/process", methods=["POST"])
def process_document_event():
    """Handles Pub/Sub push envelopes or direct JSON document audit payloads."""
    envelope = request.get_json(silent=True) or {}

    if "message" in envelope and "data" in envelope["message"]:
        try:
            decoded = base64.b64decode(envelope["message"]["data"]).decode("utf-8")
            event_data = json.loads(decoded)
        except Exception:
            return jsonify({"error": "Invalid Pub/Sub message payload"}), 204
    else:
        event_data = envelope

    event_type = envelope.get("message", {}).get("attributes", {}).get("eventType", "OBJECT_FINALIZE")
    if event_type == "OBJECT_DELETE":
        return jsonify({"status": "ignored", "reason": "OBJECT_DELETE"}), 200

    file_name = event_data.get("name") or event_data.get("file_name") or "sample_contract.txt"
    bucket_name = event_data.get("bucket") or f"{PROJECT_ID}-document-ingest"
    raw_content = event_data.get(
        "content",
        f"NSK Sovereign Cloud Run Vendor Document ({file_name}) from gs://{bucket_name}. Director ID: 9204155123087."
    )

    logging.info(f"Processing document: gs://{bucket_name}/{file_name}")

    # Stage 1: POPIA Section 19 Sanitization
    sanitized_text, pii_redactions = sanitize_popia_pii(raw_content)

    # Stage 2: Document Analysis & Tag Extraction
    words = sanitized_text.split()
    word_count = len(words)
    ocr_status = "SIMULATED_OCR" if file_name.lower().endswith(".pdf") else "EXTRACTED_TEXT"
    tags = extract_tags(sanitized_text)

    # Stage 3: Cryptographic Audit Seal
    processed_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    seal = generate_hmac_seal(f"{bucket_name}/{file_name}:{word_count}:{processed_at}")

    record = {
        "status": "success",
        "bucket": bucket_name,
        "file_name": file_name,
        "ocr_status": ocr_status,
        "word_count": word_count,
        "tags": tags,
        "popia_pii_redactions": pii_redactions,
        "audit_seal": seal,
        "processed_at": processed_at
    }

    # Stage 4: Stream to BigQuery
    record["bigquery_status"] = stream_to_bigquery(record)
    return jsonify(record), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
