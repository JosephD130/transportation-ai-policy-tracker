# State DOT AI Policy Corpus — Master File

**Compiled:** 2026-04-29
**Purpose:** Source data for IC Issue 11 (working title TBD).
**Audience:** Working civil PEs / PMs on federal-aid and state-funded transportation projects.
**Component files:**
- [`state-dot-corpus-west.md`](./state-dot-corpus-west.md) — 13 Western entities
- [`state-dot-corpus-midwest.md`](./state-dot-corpus-midwest.md) — 12 Midwestern entities
- [`state-dot-corpus-south.md`](./state-dot-corpus-south.md) — 14 Southern entities
- [`state-dot-corpus-northeast.md`](./state-dot-corpus-northeast.md) — 13 Northeastern entities + DC + PR

Total: **52 entities** (50 states + DC + PR).

---

## Grand totals

| Bucket | Count | % | Verbatim definition |
|---|---|---|---|
| **FORBID** | 10 | 19% | Explicitly prohibits non-public agency data into commercial GenAI tools. Hard ban or termination-grade language. |
| **ENCOURAGE (with guardrails)** | 28 | 54% | Permits AI use under stated conditions: training, supervisor approval, human-in-the-loop, data classification, named tools only. |
| **PARTIAL / hybrid / restricted** | 5 | 10% | Mix of forbid + encourage signals. Or guideline-flavored, no enforcement. |
| **SILENT (no operative policy at any level)** | 9 | 17% | No published AI-specific policy at the DOT or parent state level as of April 2026. |
| **Total** | **52** | **100%** | *Idaho reclassified ENCOURAGE on 2026-05-11 (was SILENT); see [CORRECTIONS.md](./CORRECTIONS.md).* |

---

## Regional split

| Region | FORBID | ENCOURAGE | PARTIAL | SILENT | Total |
|---|---|---|---|---|---|
| Midwest | 8 | 0 | 3 | 1 | 12 |
| West | 0 | 8 | 0 | 5 | 13 |
| South | 2 | 9 | 0 | 3 | 14 |
| Northeast (+ DC + PR) | 0 | 11 | 0 | 2 | 13 |
| **Total** | **10** | **28** | **3** | **11** | **52** |

*Hybrid/partial counts vary slightly by interpretation across regions; see component files for the exact bucket reasoning per state.*

**The clearest regional pattern:** Midwest forbids. West permits. Northeast permits with the most published guardrails. South splits between two operational leaders (FDOT, TxDOT) and several silent states.

---

## The 4 DOTs that publish their OWN standalone AI policy

48 of 52 DOTs (92%) inherit AI policy from the parent state CIO / OIT / OCTO / Governor EO. **Only four have published their own:**

| DOT | Policy name | Date | Bucket | Notable feature |
|---|---|---|---|---|
| **MnDOT** | GenAI Standard IT-003 | Jul 14, 2025 | FORBID | Discharge + Minn. Stat. § 13.09 criminal liability for violations |
| **MoDOT** | Employee Conduct AI guidance | 2024-2025 | FORBID | Names tools by brand ("ChatGPT, Bing Chat, and other publicly available AI systems") |
| **FDOT** | AI Policy | May 2024 | ENCOURAGE | "Pilots over giant leaps." Procuring AI to interpret Standard Specs for Road and Bridge Construction (RFP DOT-RFP-25-9078-SJ) |
| **TxDOT** | AI Strategic Plan FY2025-2027 | Jan 2025; updated Jan 21, 2026 | ENCOURAGE | 22,000 staff hours saved on invoice automation. M365 Copilot to 940+ staff. NIST AI RMF governance |

**Implication:** if you are a PE on a federal-aid contract anywhere outside MN, MO, FL, TX, the rule that governs your AI use is set by the state CIO / OIT / OCTO, not by the DOT. The DOT website probably doesn't tell you. The state IT website does.

---

## Operational leaders (where AI is already deployed at scale)

| DOT | Concrete deployment |
|---|---|
| **Caltrans** | Microsoft Copilot to **18,000 of 23,000 employees** (April 2025). Named CDAO (Vidhu Shekhar). First DOT to award GenAI vendor contracts (2024). |
| **TxDOT** | M365 Copilot to **940+ staff**. Estimated **22,000 staff hours saved annually** on invoice automation. AI Risk Management Workgroup applying NIST AI RMF. |
| **MassDOT** | First state to deploy **ChatGPT enterprise across ~40K executive staff** (Feb 2026). Custom **HEKA GenAI assistant for engineers**. Walled-off architecture is the policy. |
| **NCDOT** | **Largest live statewide AI traffic-signal deployment in the U.S.** — 2,500+ intersections via Flow Labs. AI for transit/airport language access. |
| **VDOT** | AI cost-estimation + pavement-management pilot with Deloitte (March 2025). Direct response to 68% nationwide highway construction cost surge since 2020. |
| **FDOT** | RFP procuring AI to interpret Standard Specifications for Road and Bridge Construction. |
| **UDOT** | In-road tire-anomaly AI named "innovation of the year" (2025). |
| **PennDOT** | ChatGPT Enterprise pilot (Mar 2024 – Mar 2025). Commonwealth ranked top-3 for gov AI readiness. |

---

## Laggard / contrarian standouts

| DOT | What stands out |
|---|---|
| **NYSDOT** | NY Comptroller audit (April 3, 2025) called out NYSDOT explicitly: "AI working group first met June 2024 and has not yet issued any formal policies." DOT had not provided staff training on AI risks. **NYSDOT is piloting three AI systems with no in-house policy.** Largest federal-aid pipeline in the country. |
| **Wisconsin (WisDOT)** | No DOT-direct AI use policy located. Funded a research program instead — implementation roadmap, not a use rule. |
| **West Virginia (WVDOT)** | WVOT AUP and Ethical Guidance both listed "coming soon" on the state IT site as of April 2026. |
| **Wyoming (WYDOT)** | Posture: "leave it to the districts/agencies." No DOT-level AI policy. No state EO. |
| **Puerto Rico (DTOP)** | No published AI policy. Pending PR Senate bill ("Government of Puerto Rico Artificial Intelligence Act") would establish AI Officer + advisory council. Not yet enacted. |

---

## The strongest verbatim quotes for the writeup

### Termination-grade language
**Oklahoma OMES Standard:**
> "Any state employee who inputs, uploads, transmits or otherwise discloses any federally protected data into a public AI system…shall be terminated."

### Strictest practical posture
**Louisiana OTS AI AUP (effective Sept 29, 2025):**
> "State-approved systems, accounts, and equipment are the only authorized means for using AI when conducting state business."

### DOT-direct, brand-named prohibition
**MoDOT Employee Conduct:**
> "MoDOT prohibits the use of unapproved, open AI systems (such as ChatGPT, Bing Chat, and other publicly available AI systems) for work-related purposes."

### Cleanest contractor-binding language
**MnDOT IT-003:**
> "Third parties working on behalf of MnDOT must work with MnDOT staff to ensure that any tools they use are approved by MnDOT before submitting private, confidential, protected, or otherwise not public data."

### Discharge consequence at the DOT level
**MnDOT IT-003:**
> "Employees who violate this standard or the Minnesota Government Data Practices Act are subject to discipline, up to and including discharge."

### Audit-flagged gap
**NY Office of the State Comptroller, April 3, 2025:**
> "DOT has an AI working group that first met in June 2024, but it has not yet issued any formal policies."
> "DOT has not provided training to staff on the general risks of AI."
> "DOT is piloting three AI systems."

### Most concrete saved-hours number
**TxDOT AI Strategic Plan (updated Jan 21, 2026):**
> "The Professional Engineering Procurement Services Division has saved an estimated 22,000 staff hours annually by automating invoice workflows."

### Floor clause (unique)
**Nevada Statewide AI Policy (Dec 2024):**
Prohibits agency-level AI policies from being more lenient than the statewide policy.

### Allow-list / block-list (unique)
**Delaware DTI:**
> Approved: ChatGPT, Gemini, Microsoft Copilot, Amazon Bedrock. Blocked: DeepSeek, RedNote.

---

## Contractor-binding language inventory

For consulting PMs, this is the single most important dimension. States that explicitly extend AI rules to contractors / third-parties / consultants:

| State | Mechanism |
|---|---|
| **Iowa** | "Any contracted third-party performing work on behalf of the Agency must comply." |
| **Kansas** | Contractors "must disclose any use of generative AI or integrations with such platforms in their contracts." |
| **Ohio** | DAS IT-17 explicitly applies to "state employees, contractors or temporary personnel." |
| **Minnesota (MnDOT)** | "Third parties working on behalf of MnDOT must work with MnDOT staff to ensure that any tools they use are approved by MnDOT." |
| **Louisiana** | "Agencies shall submit all software, applications, tools, and services utilizing AI for business operations to OTS for review prior to procurement and implementation." (Procurement gate effectively binds vendors and consultants.) |
| **DC** | First major US city to mandate Responsible AI training for **all gov employees + contractors**. |
| **NJ** | Mandatory "Responsible AI for Public Professionals" course for state employees; flow-down to consultants likely. |
| **Idaho** | AI-PSG §1.3 and §2.1 explicitly bind "all State of Idaho employees, contractors, sub-contractors, and their respective facilities supporting official State business operations." (Added 2026-05-11; see [CORRECTIONS.md](./CORRECTIONS.md).) |

Almost every other state's policy applies to "state employees" only and is silent on contractors. **For a consulting PM, the practical answer to "can I use AI on this project" depends on (1) the contract's specific AI clauses, (2) whether the state extends its policy to consultants, and (3) the federal funding layer.**

---

## Topic and angle candidates for Issue 11

The data supports several distinct article angles. Joseph picks one (or combines).

### Angle A — The inheritance pattern (cleanest single chart)
**Headline candidates:**
- "Your state DOT almost certainly has an AI rule. It's almost certainly not at your DOT."
- "48 of 52 state DOTs inherit their AI policy from someone else."
- "The AI policy on your federal-aid contract isn't where you think it is."

**Lead chart:** 52-entity stacked bar — origin of policy (DOT direct / state CIO / Governor EO / silent).

### Angle B — The regional disparity (richer narrative)
**Headline candidates:**
- "Where you do federal-aid work changes whether you can use AI on it."
- "Eight Midwestern DOTs forbid cloud AI. Zero Western DOTs do. The contracts look identical."
- "The same federal-aid project, four different AI rules."

**Lead chart:** US heatmap by bucket, region overlay.

### Angle C — The leaders vs. the laggards (most viscerally engaging)
**Headline candidates:**
- "Caltrans deployed Copilot to 18,000 employees. NYSDOT was audited for having no AI policy at all."
- "The four state DOTs that wrote their own AI rules — and the 48 that didn't."
- "TxDOT saved 22,000 staff hours on invoice automation. Most state DOTs haven't started."

**Lead chart:** scatter plot of operational deployment vs. policy maturity.

### Angle D — The contractor-binding gap (strongest for the consulting-PM audience)
**Headline candidates:**
- "The seven states that extend their AI rules to consultants. And the 45 that don't, yet."
- "If you are a consulting PE, only seven state DOT policies actually bind you."
- "Your contract's AI clause matters more than your firm's AI policy."

**Lead chart:** 52-entity table with contractor-binding column highlighted.

### Angle E — The 22,000-hour number (the TxDOT specific story)
**Headline candidates:**
- "TxDOT saved 22,000 staff hours on invoice automation. Here's what other DOTs could copy."
- "What 22,000 staff hours of automated invoicing actually looks like."

**Lead chart:** TxDOT before/after timing comparison (3 weeks → 27 seconds), plus per-DOT staffing.

### Angle F — The NYSDOT story (the audit + pilot tension)
**Headline candidates:**
- "NYSDOT is piloting three AI systems with no published policy. The Comptroller noticed."
- "When the auditor finds your AI program before your policy does."

**Lead chart:** AI deployment vs. published policy date — NYSDOT as outlier.

---

## Recommended next step

Joseph reviews the data above and the angle candidates. Picks ONE angle. The Issue 11 outline file gets rewritten against that angle. The body draft (already in chat) gets reshaped around the chosen narrative.

My read of strongest fits, given the audience (boss + colleagues at consulting firms + slowly-growing edge of strangers) and the publication's still-forming identity:

- **Angle A** (inheritance pattern) — most universally useful, cleanest single takeaway, least controversial. Best inaugural-issue choice.
- **Angle B** (regional disparity) — richer narrative, more shareable, slightly more reportorial.
- **Angle D** (contractor-binding gap) — most directly useful to the consulting-PM segment of the audience. Best for ARA-colleague reads.

A and D could combine into one piece: "Your state DOT almost certainly has an AI rule. It's almost certainly not at your DOT. And only 7 states extend it to consultants like you."

Angles C, E, F are spicier but pick a fight with specific agencies — defensible since the data is public, but worth a thought before the inaugural issue.
