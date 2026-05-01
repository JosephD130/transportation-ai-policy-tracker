# Transportation AI Policy Tracker

A maintained scoring of every major transportation agency's published AI policy posture.

Maintained by [Joseph Dib, P.E., PMP](https://www.linkedin.com/in/josephdib) and published as part of [Infrastructure Catalyst](https://infrastructurecatalyst.com).

---

## What this is

For a working civil PE on a federal-aid transportation project, the answer to "can I use AI on this contract?" lives across at least three layers:

1. The contract itself
2. The state DOT's policy as of the contract date
3. The federal preemption layer (OMB M-25-22 and downstream agency guidance)

Most working PMs only know one of those layers exists. This Tracker scores every layer, with verbatim source clauses and an open dataset, so anyone can verify before they touch AI on a deliverable.

The Tracker is published in installments:

- **Installment 1 (April 2026):** State DOT layer. 52 entities (50 states + DC + Puerto Rico). *In this repo as of launch.*
- **Installment 2 (~June 2026):** Federal transportation agencies. ~9 entities (USDOT, FHWA, FAA, FTA, FRA, NHTSA, FMCSA, MARAD, USACE Civil Works).
- **Installment 3 (~August 2026):** Major transit authorities. ~8 entities (MTA, WMATA, LA Metro, BART, MBTA, CTA, SEPTA, Sound Transit).
- **Installment 4 (~October 2026):** Multi-state, port, toll, and MPO authorities. ~15 entities.
- **Quarterly refresh starting Q1 2027:** scan what changed across all layers; publish updates.

---

## What's in this repo

| File | What it is |
|---|---|
| `transportation-ai-policy-tracker.csv` | The 52-entity dataset — one row per state-level entity, with bucket, policy URL, date, and contractor-binding flag. |
| `methodology.md` | How entities are scored, what counts as FORBID / ENCOURAGE / PARTIAL / SILENT, what counts as contractor-binding. |
| `regional-source-notes/` | The full reading notes for each region (West, Midwest, South, Northeast). Includes verbatim operative clauses and source URLs. |
| `master-corpus.md` | The consolidated synthesis across all 52 entities. |
| `issue-11-chart.png` | The launch chart showing regional bucket distribution + headline numbers. |
| `build_chart.py` | Script that regenerates the chart from the CSV. Pure matplotlib. |

---

## Headline findings (state DOT layer)

- **52 entities surveyed.**
- **10 FORBID** putting non-public agency data into commercial GenAI.
- **27 ENCOURAGE** with stated guardrails.
- **3 PARTIAL** (hybrid / guideline-only postures).
- **12 SILENT** (no AI-specific policy at any level).
- **Only 4 DOTs publish their own AI policy:** MnDOT (IT-003), MoDOT (Employee Conduct), FDOT (May 2024), TxDOT (Strategic Plan FY 2025-2027).
- **48 of 52 inherit** their AI policy from the state CIO, OIT, OCTO, or a Governor's executive order.
- **Only 7 states extend AI rules to contractors:** Iowa, Kansas, Ohio, Minnesota, Louisiana, DC, New Jersey.

Strong regional split: Midwest forbids most (8 of 12). West permits most (0 of 13 forbid). Northeast publishes the most formal frameworks (10 of 13 ENCOURAGE). South splits between two operational leaders (FDOT, TxDOT) and a few silent states.

---

## How to use this

**If you are a working PE/PM on a federal-aid project:**
1. Find your contract's AI clause. Silence is not permission.
2. Look up your state in `transportation-ai-policy-tracker.csv` to see where the operative rule actually lives.
3. Read the verbatim operative clause for your state in the regional notes.
4. If the consultant question is unanswered (and 45 of 52 are silent on it), default to no-cloud-uploads. Use on-prem or local models, redact agency-identifying data, or get written permission from the contracting officer.

**If you are auditing your firm's AI use:**
1. Pull every active contract.
2. Cross-reference against the Tracker.
3. Flag any contract where your firm is using cloud AI on agency data in a state that forbids it (Midwest is the highest-risk bucket).

**If you want to contribute:**
1. Spot a stale or wrong entry? Open a PR with the corrected verbatim clause and a public source URL.
2. Want a non-state agency added (transit, toll, port, MPO)? Open an issue. Installments 2-4 expand the scope.

---

## Methodology in one sentence

I read every state DOT's website plus the parent state CIO / OIT / OCTO / Governor EO, captured verbatim operative clauses, classified each entity into one of four buckets, and flagged whether the policy explicitly extends to contractors and consultants. Full methodology in `methodology.md`.

---

## License

Data and source notes are released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Cite as: *Joseph Dib, Transportation AI Policy Tracker, Infrastructure Catalyst, 2026.*

The chart-building script (`build_chart.py`) is released under MIT.

---

## Contact

Questions, corrections, or agencies to add: reply on the [Infrastructure Catalyst newsletter](https://infrastructurecatalyst.com) or open a GitHub issue.

The Tracker refreshes every quarter once the launch arc closes (Q1 2027).
