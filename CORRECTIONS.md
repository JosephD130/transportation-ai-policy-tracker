# Issue 11 Corrections

Issue 11 ("State DOT AI policies — the inheritance pattern + contractor-binding gap") shipped in May 2026. This file logs every correction to the underlying Tracker corpus after publication. Issue 11's published body, social copy, and substack HTML are **not modified** — they remain the record of what was sent. Corrections flow to the corpus, the CSV, the GitHub repo, and (eventually) the Issue 11 reference page.

---

## 2026-05-11 — Idaho reclassified from SILENT to ENCOURAGE (binds contractors)

### What Issue 11 originally said

> Idaho — ITD. No DOT-specific; statewide guidance in draft. Status: **SILENT**. Office of Information Technology Services (ITS) is drafting statewide AI guidance; presented to legislature Jul 2025.

### What's actually true

Idaho Office of Information Technology Services (ITS) published a binding *Artificial Intelligence Governance Policy, Standard, and Guideline* (P.ITS-01 / S.ITS-01 / G.ITS-01), Version 1.0, in **August 2025** — nine months before Issue 11 shipped.

**Document URL:** https://its.idaho.gov/wp-content/uploads/2024/09/AI-PSG_FINALAug2025.pdf
**Companion strategic doc:** *Idaho's AI Advantage: A Framework for Responsible Innovation*, August 2025 — https://its.idaho.gov/wp-content/uploads/2025/08/Idaho-AI-Advantage-Framework.pdf

### What the AI-PSG does

- Combined Policy + Standard + Guideline (three instruments in one document).
- **Scope (§1.3 and §2.1):** binds all State of Idaho employees, contractors, sub-contractors, agents, and business partners conducting state business.
- **Mandatory human review** of GenAI outputs used for official purposes.
- **AI-use disclosure required** on public-facing content with a standardized disclaimer.
- **Four-tier data classification.** Critical data prohibited from GenAI without AI Executive Committee approval.
- **NIST AI RMF aligned** (GOVERN, MAP, MEASURE, MANAGE).
- **Procurement requirements:** AI vendor contracts must include security, privacy, audit rights, transparency, and incident-reporting clauses.

ITD has no transportation-specific AI document, so it inherits the statewide AI-PSG by scope. The inheritance is binding on contractors, not advisory.

### Effect on Tracker classifications

| Field | Before | After |
|---|---|---|
| Bucket | SILENT | ENCOURAGE (with guardrails) |
| Contractor-binding | No | **Yes** |
| Policy origin | None active | Office of Information Technology Services (ITS) |
| Policy URL | https://its.idaho.gov/ai/ | https://its.idaho.gov/wp-content/uploads/2024/09/AI-PSG_FINALAug2025.pdf |
| Date | 2025 (draft) | 2025-08 (v1.0 final) |

### Effect on Tracker grand totals

| Metric | Before | After |
|---|---|---|
| Bucket: ENCOURAGE | 27 (52%) | **28 (54%)** |
| Bucket: SILENT | 10 (19%) | **9 (17%)** |
| Region West: ENCOURAGE | 7 | **8** |
| Region West: SILENT | 6 | **5** |
| Contractor-binding states | 7 | **8** |
| "48 of 52 inherit" | 48 | **48** (unchanged — Idaho was always counted as inheriting; the policy it inherits just now has a name) |
| "4 publish their own" | 4 (MnDOT, MoDOT, FDOT, TxDOT) | **4** (unchanged) |

### Why it got missed

Three structural reasons that the methodology should be updated to avoid:

1. **PDF URL path lies about the date.** Document is dated August 2025 but lives at `/wp-content/uploads/2024/09/AI-PSG_FINALAug2025.pdf`. A date-filter scrape that excluded "2024" URL paths would skip it.
2. **Document lives on the state IT portal (its.idaho.gov), not on the DOT website (itd.idaho.gov).** The original Tracker pull was DOT-anchored. It did not systematically cross-check the state CIO / Office of Information Technology site for each state.
3. **The PDF binary is compressed and image-laden.** Standard WebFetch returned garbage; only `pdftotext -layout` extracted clean text. Any methodology relying on LLM-summarized PDF fetches without an OCR/pdftotext fallback will silently miss content like this.

### Methodology fix going forward

For each state's Tracker entry, the methodology now requires checking, in addition to the DOT website:
- `[state-abbreviation].gov` root
- `its.[state].gov` or equivalent state IT services site
- The state CIO / Office of Information Technology office
- The Governor's executive orders index
- Validation that PDF text extraction returned >500 characters of readable text. If not, fall back to `pdftotext -layout` or manual download.

### Credit

Brought to attention by **Mike Copeland** on LinkedIn, 2026-05-10.

### Files updated for this correction

- [transportation-ai-policy-tracker.csv](./transportation-ai-policy-tracker.csv) — Idaho row reclassified.
- [regional-source-notes/state-dot-corpus-west.md](./regional-source-notes/state-dot-corpus-west.md) — Idaho row + Western region summary + sources updated.
- [master-corpus.md](./master-corpus.md) — grand totals, regional split, contractor-binding inventory updated.
- [README.md](./README.md) — headline findings updated.
- [methodology.md](./methodology.md) — new source-search step + PDF text-extraction guard added.
- [issue-11-chart.png](./issue-11-chart.png) — regenerated from the corrected bucket counts.
- This file ([CORRECTIONS.md](./CORRECTIONS.md)) — created.

### Files NOT modified (intentionally)

The Issue 11 newsletter body, the Substack mirror, the social posts as published on May 2026, and the issue-specific build files remain the historical record of what subscribers received. Any future reference to Idaho's classification should point at this file rather than the published Issue 11 body.
