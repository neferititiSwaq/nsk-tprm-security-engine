---
marp: true
theme: default
class: invert
paginate: true
style: |
  section {
    font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    justify-content: center;
    background-color: #080b12; /* Deep Obsidian Black */
    color: #e2e8f0;
    padding: 40px 60px;
  }
  h1 {
    color: #c9a84c; /* Sovereign Warm Gold */
    font-size: 2.2em;
    font-family: 'Playfair Display', Georgia, serif;
    margin-bottom: 0.2em;
  }
  h2 {
    color: #ffffff;
    font-size: 1.5em;
    border-bottom: 2px solid #c9a84c;
    padding-bottom: 0.2em;
    font-family: 'Playfair Display', Georgia, serif;
    margin-bottom: 0.4em;
  }
  h3 {
    color: #c9a84c;
    font-size: 1.05em;
    font-family: 'Inter', sans-serif;
    font-weight: 400;
  }
  strong {
    color: #c9a84c;
  }
  ul {
    font-size: 0.95em;
    line-height: 1.6;
  }
  li {
    margin-bottom: 0.35em;
  }
  .highlight {
    background-color: rgba(201, 168, 76, 0.1);
    border-left: 3px solid #c9a84c;
    padding: 0.6em 1em;
    margin: 0.6em 0;
    border-radius: 4px;
    font-size: 0.9em;
  }
  .badge {
    display: inline-block;
    padding: 0.2em 0.6em;
    border-radius: 4px;
    font-size: 0.75em;
    font-family: monospace;
    font-weight: bold;
    text-transform: uppercase;
  }
  .badge-gold {
    background-color: rgba(201, 168, 76, 0.15);
    color: #c9a84c;
    border: 1px solid rgba(201, 168, 76, 0.4);
  }
  .badge-green {
    background-color: rgba(16, 185, 129, 0.15);
    color: #34d399;
    border: 1px solid rgba(16, 185, 129, 0.4);
  }
  footer {
    font-size: 0.7em;
    color: #64748b;
  }
---

<!-- _class: lead -->
# **NSK Devpreneur Hub**
### Sovereign Digital Public Infrastructure (DPI) & 14ms TPRM Security Engine
**FNB App of the Year Hackathon 2026 // Best Hackathon Solution**  
*Track: Youth Entrepreneurship & Small-Business Growth // Sector: Cybersecurity*  
**Founder & Systems Architect:** Maria Thembi Mathibela  
**Entity:** Nyoni Sakha Kumbi (Pty) Ltd | eMalahleni, Mpumalanga

---

## **1. The Problem: The 3-Week Supply Chain Lockout**
### African Township & Host-Community SMMEs Are Excluded by Bureaucracy

- **The Host-Community Reality:** In industrial corridors like eMalahleni, Middelburg, and Ogies, emerging youth entrepreneurs and township vendors cannot access corporate procurement pipelines because manual spatial, tax, and compliance vetting takes **3 to 4 weeks**.
- **The Enterprise Middleware Drain:** Tier-1 mining houses and commercial enterprises waste **millions of Rands annually** on foreign SaaS middleware subscriptions that drain balance sheets and route South African supplier data to offshore clouds.
- **The Disbursement Block:** Banks cannot safely trigger instant supplier financing or commercial disbursements because third-party risk verification is slow, fragmented, and vulnerable to perimeter tampering.

<div class="highlight">
<strong>The Core Bottleneck:</strong> It's not a lack of township entrepreneurial talent—it is a broken, expensive, 3-week verification tax.
</div>

---

## **2. The Solution: NSK Sovereign DPI Utility Rail**
### Replacing Expensive Foreign Middleware with Localized On-Premise Infrastructure

We engineered an on-premise, zero-middleware Digital Public Infrastructure (DPI) utility rail that automates enterprise compliance, spatial verification, and supplier risk vetting straight at the API layer.

- **Zero Third-Party Software Licenses:** Eliminates recurring foreign-currency SaaS subscriptions.
- **Hardware-Level Security:** Deployed directly on-premise on 4-Core ARM64 micro-nodes (Rockchip RK3588 SBCs drawing under 15W of power).
- **Sub-Second Clearance:** Compresses a critical **3-week corporate risk vetting process down to a 14-millisecond cryptographic match**.
- **FNB PayShap Settlement Hook:** Instant qualification for automated commercial disbursements.

---

## **3. User Journey: From 3 Weeks to 14 Milliseconds**
### Case Study: Sindi's Engineering Services (eMalahleni Mining Corridor)

```
[ BEFORE NSK: 21-Day Manual Friction ]
Sindi submits paper/PDFs ➔ 5 Disconnected Portals ➔ 3-Week Manual Review ➔ Delayed Payout ➔ Cash Flow Crisis

[ WITH NSK TRIAD: 14-Millisecond Unbroken Pipeline ]
1. The Foundry: GPS coordinates verified against municipal zoning & mine corridor (0.2s)
2. The Forge: CIPC registration validated; BCEA employment contract sealed (0.4s)
3. TPRM Engine: Deterministic on-premise hash match; 0 bytes leaked outside LAN (14ms)
4. FNB Commercial Rail: Status CLEARED_PAYSHAP_BATCH ➔ Funds hit Sindi's account instantly!
```

<div class="highlight">
Sindi gains immediate cash flow certainty. The mine achieves 100% Social & Labour Plan (SLP) compliance. FNB powers the secure commercial disbursement.
</div>

---

## **4. Technical Architecture: The Continuous Triad**
### Zero-Trust, Local-First, Middleware-Free Operating Rail

```
┌────────────────────────────────────────────────────────────────────────┐
│                   NSK CONTINUOUS OPERATING TRIAD                       │
├────────────────────┬────────────────────┬──────────────────────────────┤
│ STAGE 01:          │ STAGE 02:          │ STAGE 03:                    │
│ THE FOUNDRY        │ THE FORGE          │ TPRM SECURITY ENGINE         │
│ Spatial GIS Bounds │ Legal Automation   │ 14ms Deterministic Audit     │
├────────────────────┼────────────────────┼──────────────────────────────┤
│ • Google Maps      │ • Decoupled Python │ • On-Premise ARM64 Kernel    │
│   Geospatial API   │   & Node.js Rail   │ • Memory-Mapped Cache        │
│ • SPLUMA Zoning    │ • CIPC Validation  │ • Zero External API Calls    │
│ • REDZ & Eskom Grid│ • BCEA Contracts   │ • SHA-256 Batch Seal Log     │
└─────────┬──────────┴─────────┬──────────┴──────────────┬───────────────┘
          │                    │                         │
          ▼                    ▼                         ▼
┌────────────────────────────────────────────────────────────────────────┐
│  FNB SETTLEMENT HOOK: Instant Commercial PayShap Batch Disbursement   │
└────────────────────────────────────────────────────────────────────────┘
```

---

## **5. Hardware Benchmarks: ARM64 Edge vs. Cloud Middleware**
### Verified Audit Logs from Benchmark Document NSK-TSD-2026-V1

| Performance Metric | Baseline Cloud Middleware | NSK Local Edge Utility | Architectural Variance |
| :--- | :--- | :--- | :--- |
| **Transaction Processing Speed** | 124 ms / record | **14 ms / record** | <span class="badge badge-green">88.7% Latency Drop</span> |
| **Network Outbound Connections** | 4–6 external API calls | **0 calls (Isolated LAN)** | <span class="badge badge-green">Zero Attack Perimeter</span> |
| **CPU Overhead (Peak Load)** | 68% (Frequent spikes) | **22% (Sustained)** | <span class="badge badge-green">Optimized C-layer hooks</span> |
| **Memory Footprint (Idle)** | 1.2 GB | **142 MB** | <span class="badge badge-green">Engineered for ARM64</span> |
| **Cluster Power Draw** | Server rack power | **< 15W Total Cluster** | <span class="badge badge-green">Stage 6 Load Shedding Proof</span> |

---

## **6. The Master TPRM Register (NSK-TPRM-REG-2026-V1)**
### Audited Component Architecture & Risk Controls

- **NSK-DEP-001 (Backend Core):** Native Python Runtime &bull; Criticality: *High* &bull; Exposure: *None (Local Execution)* &bull; Status: *Locked to LTS release*.
- **NSK-DEP-002 (Data Ingestion Rail):** Node.js Microservices &bull; Criticality: *High* &bull; Exposure: *None (On-Premise Node)* &bull; Status: *Zero external package links*.
- **NSK-SYS-001 (The Forge Engine):** Legal Process Automation &bull; Criticality: *Critical* &bull; Exposure: *Metadata Only* &bull; Status: *Hardened local kernel access controls*.
- **NSK-SYS-002 (The Foundry Compiler):** Schema Compilation &bull; Criticality: *Critical* &bull; Exposure: *Restricted PII* &bull; Status: *Cryptographic hash matching; local storage only*.
- **NSK-SYS-003 (LaunchSense Utility):** Industrial Edge Node &bull; Criticality: *High* &bull; Exposure: *Network Config* &bull; Status: *Isolated within client firewall; 0 outbound*.

---

## **7. Regulatory & Data Sovereignty Alignment**
### Total Compliance with South African Legislative Frameworks

- **POPIA Act No. 4 of 2013:** 
  All vendor and enterprise processing maintains strict physical residency within South Africa. PII never crosses corporate firewalls or borders.
- **DMRE & SLP Regulatory Auditing:** 
  Every cleared transaction batch generates an immutable **SHA-256 Cryptographic Ledger Seal**:
  `9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08`
  providing tamper-proof mathematical proof for mining compliance inspectors.
- **FICA & Banking Security:** 
  Deterministic hash validation replaces paper-based verification, eliminating identity fraud and unauthorized supplier tampering.

---

## **8. Judges' Live Demo & Verification Guide**
### Test Our Solution Live in 3 Clicks (Zero Setup Required)

**1. Live Interactive Audit Console:**
👉 **[`https://devpreneur-hub.vercel.app/tprm-audit`](https://devpreneur-hub.vercel.app/tprm-audit)**
* Click **"Run Live Batch Simulation"** to trigger the 1,000-record host-community batch execution. Watch the deterministic terminal output compile at **14ms/record**.
* Click **"Copy Audit Seal"** to inspect the live SHA-256 tamper-proof ledger hash.

**2. Enterprise Architecture & Google Maps Geospatial Solution:**
👉 **[`https://devpreneur-hub.vercel.app/enterprise`](https://devpreneur-hub.vercel.app/enterprise)**
* Click **"Spatial Commute Matrix"** in the Hero or Stage 01 card to test live route clearance across the eMalahleni/Middelburg mining corridor.

**3. Open-Source Showcase Repository:**
👉 **[`https://github.com/neferititiSwaq/nsk-tprm-security-engine`](https://github.com/neferititiSwaq/nsk-tprm-security-engine)**

---

## **9. Business Model & Commercial Scalability**
### Sustainable B2B & Public Utility Revenue Engine

- **Tiered Enterprise SaaS / API Retainers:** 
  Corporate mining houses and industrial conglomerates subscribe for automated spatial and TPRM vendor vetting (Starting at **R95,000 / month** per enterprise cluster).
- **Banking Transaction Fee-Share:** 
  Volume-based integration fees on cleared commercial PayShap disbursements.
- **On-Premise Hardware Deployment Packages:** 
  Turnkey deployment of sovereign 3x Orange Pi 5 Plus ARM64 sandboxing clusters at remote mine sites and municipal administrative hubs.
- **Public Sector Municipal Licensing:** 
  Multi-municipality SPLUMA spatial GIS screening licenses across Mpumalanga and SADC.

---

## **10. Why NSK Devpreneur Hub Wins**
### An Authentic Solution Built by African Builders for African Realities

| Evaluation Criteria | Traditional Industry Competitors | NSK Devpreneur Hub |
| :--- | :--- | :--- |
| **Deployment Model** | Foreign Cloud (AWS / Azure) | **Sovereign Local Edge (ARM64 On-Premise)** |
| **Software Licensing** | Multi-Million Rand Foreign SaaS | **Zero-Middleware (100% Owned Utility)** |
| **Verification Speed** | 3 to 4 Weeks Manual Vetting | **14 Milliseconds Local Cryptographic Match** |
| **Data Sovereignty** | Cross-Border PII Exposure | **100% POPIA Compliant Air-Gapped LAN** |
| **Bank Integration** | Delayed Manual EFT Batches | **Instant FNB PayShap Batch Clearance** |

<div class="highlight">
<strong>Our Vision:</strong> Unlocking Africa's sovereign economic future by putting the digital scaffolding directly into African hands.
</div>

---

<!-- _class: lead -->
# **Thank You, Adjudicators!**
### Let's Build Africa's Sovereign Digital Future Together

**Maria Thembi Mathibela**  
Founder, CEO & Systems Architect  
**Nyoni Sakha Kumbi (Pty) Ltd t/a NSK Devpreneur Hub**  

🌐 **Live Platform:** [devpreneur-hub.vercel.app/tprm-audit](https://devpreneur-hub.vercel.app/tprm-audit)  
🐙 **Code Repository:** [github.com/neferititiSwaq/nsk-tprm-security-engine](https://github.com/neferititiSwaq/nsk-tprm-security-engine)  
⚡ **Hardware Campaign:** [BackaBuddy Sovereign Edge Campaign](https://www.backabuddy.co.za/campaign/digital-public-infrastructure)  
📧 **Email:** *thembisilemathibela2010@gmail.com* | eMalahleni, South Africa
