# Federal Transportation Agencies AI Policy Corpus

Compiled for the Transportation AI Policy Tracker, Installment 2.
Audience: working civil engineers, PEs, and PMs on federal-aid and state-funded transportation projects who need to know which federal rules govern their AI use.

Scope: 9 federal transportation agencies. For each, the operative AI policy posture was classified as FORBID / ENCOURAGE / PARTIAL / SILENT and contractor-binding status was flagged, per [methodology.md](../methodology.md).

## Federal agency AI posture — summary table

| Agency | Bucket | Contractor-binding | Key source |
|---|---|---|---|
| USDOT (OST) | ENCOURAGE | No | DOT Order 1351.41 (2026-08-26) |
| FHWA | SILENT | No | Inherits USDOT 1351.41; no agency-specific use policy |
| FAA | ENCOURAGE | Yes | FAA Notice 1370.52 (2025-03-23) |
| FTA | SILENT | No | Inherits USDOT 1351.41; no agency-specific use policy |
| FRA | SILENT | No | Inherits USDOT 1351.41; no agency-specific use policy |
| NHTSA | SILENT | No | Inherits USDOT 1351.41; no agency-specific use policy |
| FMCSA | SILENT | No | Inherits USDOT 1351.41; no agency-specific use policy |
| MARAD | SILENT | No | Inherits USDOT 1351.41; no agency-specific use policy |
| USACE Civil Works | ENCOURAGE | No | CECW-P AI Ethics Memo (2026-04-03) |

## Reading notes by agency

---

### USDOT — Office of the Secretary (OST)

**Bucket:** ENCOURAGE | **Contractor-binding:** No

**Source:** [DOT Order 1351.41 — U.S. Department of Transportation Artificial Intelligence (AI) Policy](https://www.transportation.gov/orders/ai-policy) — Effective 08/26/2026. Originating office OST-S80. Last updated 2026-09-02.

**Verbatim operative clause:**
> "The Department fully embraces the memorandum's pro-innovation, America-first approach to Artificial Intelligence (AI) as a critical enabler of its mission to advance safety, rebuild our national infrastructure, and usher in a new era of American leadership... The Department's core philosophy is one of responsible acceleration to aggressively remove bureaucratic barriers to empower our Nation's transportation innovators while maintaining the streamlined, effective governance necessary to ensure AI is deployed safely, fosters public trust, and maximizes taxpayer value."
> — DOT AI Strategy Part III: Compliance Plan for OMB M-25-21 (September 2025), p.1

**What the policy does:**
- Establishes the NETT Council as the DOT AI Governance Board (chaired by the Deputy Secretary, with the CDAIO as vice-chair).
- Creates the CDAIO (Chief Data and AI Officer) role.
- Mandates an AI Use Case Inventory (TrUCKR system) and SR2 Committee review of safety-impacting / rights-impacting AI.
- Establishes the AI Accelerator Roadmap (OPSLAB, ART Network, TrAIN) to provide secure AI development environments.
- References forthcoming Generative AI Use Guidance (in final stages of development per Part III).
- Updates existing AI minimum risk management guidance.

**Contractor status:** The department-level policy governs DOT Operating Administrations and Secretarial Offices. No explicit contractor-binding language found in DOT 1351.41. The applicability clause is limited to OAs and Secretarial Offices "only to the extent that it is consistent with the expressed language contained in 49 U.S.C. 106 and 40110 as applicable to the Federal Aviation Administration and Office of Inspector General."

**Note:** DOT 1351.41 is a governance and innovation policy, not an employee-facing acceptable-use policy in the mold of state CIO policies. It directs *how* AI governance works across the department but does not itself set employee rules for tool use — that is delegated to OA-level policies (e.g., FAA Notice 1370.52). For this reason, USDOT is classified ENCOURAGE (explicit pro-innovation posture with governance guardrails), but the operative employee-use rules live at the OA level.

---

### FHWA — Federal Highway Administration

**Bucket:** SILENT | **Contractor-binding:** No

**Sources searched:**
- fhwa.dot.gov — Publications, research (EAR Program, FHWA-HRT-25-020, FHWA-HRT-22-026)
- highways.dot.gov — AI Deployment Center of Excellence (AI-COE), Policy & Guidance Center
- its-dr.fhwa.dot.gov — AI Implementation Guide, ITS JPO AI research
- search terms: "artificial intelligence," "AI policy," "generative AI," "AI use," "acceptable use policy AI"

**What was found (and why it does not count as a policy):**
- FHWA operates an **AI Deployment Center of Excellence** (highways.dot.gov/ai-coe) — described as a "national resource to guide AI adoption across surface transportation." This is an external-facing resource/best-practices body, not an internal employee-use policy.
- FHWA sponsors extensive AI R&D through the **Exploratory Advanced Research (EAR) Program** (FHWA-HRT-25-020 "The Role of AI and ML in Federally Supported Surface Transportation: 2024 Updates"). This is a research program, not a use policy.
- The **ITS JPO AI Implementation Guide** (its-dr.fhwa.dot.gov) provides readiness/implementation frameworks for transportation professionals — again, external-facing guidance, not an employee policy.
- No FHWA-specific AI acceptable-use policy, generative AI policy, or employee-facing AI tool-use rules were located.

**Contractor status:** No FHWA-specific AI policy means no contractor-binding. Contractors performing FHWA work are subject to generic federal procurement rules (FAR/DFARS) and may inherit USDOT-level governance but are not bound by any FHWA-specific AI use rule.

---

### FAA — Federal Aviation Administration

**Bucket:** ENCOURAGE | **Contractor-binding:** Yes

**Source:** [FAA Notice 1370.52 — Use of Generative AI Tools and Services](https://www.faa.gov/documentLibrary/media/Notice/N_1370.52_Generative_AI_Tools_and_Services.pdf) — Effective 03/23/2025, Cancellation Date 03/23/2026. Initiated by ADO-210 (Analytics Enablement).

**Verbatim operative clauses:**
> "This Notice establishes the interim policy on the use of Generative Artificial Intelligence (GAI) in the Federal Aviation Administration (FAA)."
> — §1

> "This Notice applies to all employees and contractors within the FAA."
> — §2

> "FAA organizations, managers and employees must not use GAI to: (a) Perform or facilitate illegal or malicious activities; (b) Be cited as direct evidence or authority for a determination/decision; (c) Be used to contravene or circumvent any requirement, guidance, order, policy, notice, or standard operating procedure..."
> — §6.a.1

> "FAA employees and contractors must never input [Sensitive Unclassified Information (SUI), Classified National Security Information (CNSI)] into GAI tools that are outside the government secured cloud or data center environments."
> — §6.c

> "Government Contractor Responsibility: FAA contractors who use GAI are responsible for their actions and the content generated using GAI. Use of GAI by FAA contractors must not result in any action or output inconsistent with their federal contractual requirements. (1) Contractors must discuss with their FAA Contracting Officer (CO) and/or Contracting Officer Representative (COR) ... their use of GAI in the performance of their duties. (2) Contractors must adhere to the restrictions of use of GAI addressed in 5.a.1 above."
> — §6.b

**What the policy does:**
- Permits GAI use with stated guardrails (supervisor approval required before use; only ESB-approved software on the Technology Product Roadmap; no SUI/CNSI into external GAI tools; all outputs reviewed for accuracy before publishing; misuse must be reported).
- Establishes the Enterprise Software Board (ESB) as the approval body for GAI-capable software.
- Tracks all AI use-cases via the FAA Chief Data Office.
- References an "FAA AI Strategy" for broader (non-GAI) AI use.
- Distribution: Electronic. Cancels FAA Notice 1370.51.

**Contractor status:** Explicitly contractor-binding. The Notice names contractors as covered parties (§2, §6.b) and imposes the same use restrictions on them.

**Note:** This Notice carries a cancellation date of 03/23/2026 and is listed as "Cancelled" on the FAA Orders and Notices webpage. No replacement GAI use policy was located during this research window. FAA inherits USDOT 1351.41 as a DOT OA. The FAA also publishes the "FAA Roadmap for AI Safety Assurance" (August 2024) addressing AI safety in aviation systems — a safety-regulation document, not an employee-use policy.

---

### FTA — Federal Transit Administration

**Bucket:** SILENT | **Contractor-binding:** No

**Sources searched:**
- transit.dot.gov — Research & Innovation (STAR Plan 2.0, Transit Bus Automation FAQs, AI-based trespass monitoring Report 0256, micro-transit AI dispatch Report 0269)
- FTA Master Agreement v34 (November 2025) — standard grant/contract terms
- search terms: "artificial intelligence," "AI policy," "generative AI," "AI use," "acceptable use policy"

**What was found (and why it does not count):**
- **Strategic Transit Automation Research (STAR) Plan 2.0: 2023-2028** (FTA Report 0264) — a research planning document for transit bus automation. Not an employee AI use policy.
- **Transit Bus Automation Policy FAQs** (updated March 2026) — guidance for transit agencies on automated bus requirements. Not an FAA/FTA employee AI use policy.
- **FTA Report 0256** "Utilizing AI with Vision-based Systems for Monitoring Trespassing" — research report.
- **FTA Report 0269** "Providing a Dynamic, Data-Driven Micro-Transit Service with Smart Dispatch Using AI" — research report.
- No FTA-specific AI acceptable-use policy, generative AI policy, or employee-facing AI tool-use rules were located.

**Contractor status:** No FTA-specific AI policy means no contractor-binding. FTA grantees/contractors are subject to the FTA Master Agreement and generic FAR requirements.

---

### FRA — Federal Railroad Administration

**Bucket:** SILENT | **Contractor-binding:** No

**Sources searched:**
- railroads.fra.dot.gov — elibrary (trespassing database using AI, automated train operations sensor platform)
- trespasstoolkit.fra.dot.gov — CCTV and AI-based trespass detection resources
- gradecrossingtoolkit.fra.dot.gov — AI for grade crossing safety
- search terms: "artificial intelligence," "AI policy," "generative AI," "AI use," "acceptable use policy"

**What was found (and why it does not count):**
- **Grade Crossing Trespass Detection (GTCD) software** — developed by Volpe Center under FRA direction; AI for processing video to detect trespass events. A research product, not a use policy.
- **"Development of Railroad Trespassing Database Using AI"** (DOT/FRA/ORD-24/09) — research report on AI analysis of 27,000+ hours of video. Not a use policy.
- **Automated Train Operations (ATO) Sensor Platform Data Analysis** — research project.
- **Report to Congress on Automated Track Inspection Technologies** — policy/administrative document, not an AI use policy.
- No FRA-specific AI acceptable-use policy, generative AI policy, or employee-facing AI tool-use rules were located.

**Contractor status:** No FRA-specific AI policy means no contractor-binding.

---

### NHTSA — National Highway Traffic Safety Administration

**Bucket:** SILENT | **Contractor-binding:** No

**Sources searched:**
- nhtsa.gov — Automated Vehicle Safety, AV 4.0, Federal Automated Vehicles Policy
- Report to Congress July 2025 (NHTSA Research and Rulemaking Activities on ADS-equipped vehicles)
- Federal Register (2026-07-31) — "Updating and Expanding Guidance on Safe Development and Deployment of Automated Driving Systems" (NHTSA-2026-1520)
- search terms: "artificial intelligence," "AI policy," "generative AI," "AI use," "acceptable use policy"

**What was found (and why it does not count):**
- **Automated Vehicle Safety** program and **AV 4.0** (Ensuring American Leadership in Automated Vehicle Technologies) — voluntary guidance for manufacturers on automated driving systems. Not an employee AI use policy.
- **Federal Automated Vehicles Policy** (2016) and **Automated Driving Systems: A Vision for Safety** (2017) — vehicle safety guidance. Not employee-use.
- **Report to Congress July 2025** — documents NHTSA investigating "broader artificial intelligence (AI) applications within ADS technologies and assessing AI training and validation strategies." Research posture document, not a use policy.
- **July 2026 Federal Register notice** — announces intent to update ADS guidance. Not an employee-use policy.
- No NHTSA-specific AI acceptable-use policy, generative AI policy, or employee-facing AI tool-use rules were located.

**Contractor status:** No NHTSA-specific AI policy means no contractor-binding.

---

### FMCSA — Federal Motor Carrier Safety Administration

**Bucket:** SILENT | **Contractor-binding:** No

**Sources searched:**
- fmcsa.dot.gov — newsroom, guidance, programs
- ai.fmcsa.dot.gov — A&I Online portal (Analysis and Information Resources, NOT an AI policy)
- ask.fmcsa.dot.gov — FAQ/knowledge base
- search terms: "artificial intelligence," "AI policy," "generative AI," "AI use," "acceptable use policy"

**What was found (and why it does not count):**
- **A&I Online** (ai.fmcsa.dot.gov) — Motor Carrier Analysis and Information Resources Online data portal. Despite the `ai.` subdomain, this is a safety data system (SMS, crash numbers, investigations), not an artificial-intelligence use policy.
- **Regulatory Guidance** mailbox (FMCSAguidance@dot.gov) — FMCSA publishes regulatory guidance on safety topics; none on AI use.
- **Vinn White** (former FMCSA Deputy Administrator) served as USDOT Acting Chief AI Officer — indicates FMCSA involvement in departmental AI governance but no standalone FMCSA AI policy.
- No FMCSA-specific AI acceptable-use policy, generative AI policy, or employee-facing AI tool-use rules were located.

**Contractor status:** No FMCSA-specific AI policy means no contractor-binding.

---

### MARAD — Maritime Administration

**Bucket:** SILENT | **Contractor-binding:** No

**Sources searched:**
- marad.dot.gov — Maritime Security Compliance System, vessel history, MSCI advisories
- mscs.marad.dot.gov — Maritime Service Compliance System
- vesselhistory.marad.dot.gov — Vessel History Database
- search terms: "artificial intelligence," "AI policy," "generative AI," "AI use," "acceptable use policy"

**What was found (and why it does not count):**
- **MSCI 2025-006** "Worldwide Foreign Adversarial Technological, Physical, and Cyber Influence" — maritime security advisory on port equipment/network vulnerabilities. Not an AI use policy.
- **MSCI 2023-009** — similar advisory.
- **Vessel History Database** — historical fleet data.
- **Maritime Service Compliance System (MSCS)** — compliance tracking for maritime academy graduates.
- No MARAD-specific AI acceptable-use policy, generative AI policy, or employee-facing AI tool-use rules were located.

**Contractor status:** No MARAD-specific AI policy means no contractor-binding.

---

### USACE Civil Works — U.S. Army Corps of Engineers

**Bucket:** ENCOURAGE | **Contractor-binding:** No

**Source:** [Ethical and Responsible Use of Artificial Intelligence in Planning Programs and Studies](https://planning.erdc.dren.mil/toolbox/library.cfm?Option=Listing&Search=&Type=EGM) — CECW-P Memorandum, 3 April 2026, signed by Eric L. Bush, SES, Chief, Civil Works Planning and Policy, USACE. Distribution: USACE Civil Works planners.

**Verbatim operative clauses:**
> "This memorandum provides guidance regarding the ethical and responsible use of Artificial Intelligence (AI) in Civil Works planning programs and studies. It translates federal policy and Department of War (DOW) guidance on AI into practical expectations for U.S. Army Corps of Engineers (USACE) Civil Works planners, with emphasis on transparency, ethical behaviors, fairness, efficiency, and cost-effectiveness."
> — §1 Purpose

> "AI shall be used as a decision support tool only. It does not replace professional judgment, technical review, or approval/decision-making authority."
> — §3 Background

> "Human planners remain responsible for study design, interpretation of results, and recommendations. AI output is advisory and must never be treated as a binding decision."
> — §4.b Human Responsibility and Control

> "PII and sensitive data must not be entered into external AI services unless explicitly authorized."
> — §4.f Data Stewardship

> "AI must not be used to make final determinations regarding statutory compliance, selection of plans, or commitments to non-federal sponsors."
> — §5.b.1 Prohibited Uses

> "AI must not be used to bypass existing model certification or approval processes."
> — §5.b.2

> "AI must not be used to fabricate data or create records that do not reflect actual study conditions or legally accurate information."
> — §5.b.3

**What the policy does:**
- Establishes eight guiding principles: Mission-Driven, Human Control, Transparency, Reliability & QA, Bias Avoidance, Data Stewardship, Cybersecurity, Accountability.
- Permits AI as a decision-support tool only (appropriate uses: dataset exploration, drafting report sections with human review, scenario analysis with approved models, public comment summarization with human verification).
- Prohibits AI for final statutory compliance determinations, bypassing model certification, or fabricating data.
- Approved tools include: CoPilot, Army Vantage, AskSage, uPoP chatbot (DOW GenAI at genai.mil approved for CUI).
- Establishes governance: HQ Civil Works oversight, MSC AI Planning Coordinator (GS-13+), District Study Teams responsible for compliance, PCoP maintains tool inventory.
- References: EO 13960, EO 14110, EO 14179, DOW Responsible AI Strategy, DOW Data/AI Adoption Strategy, DOW AI Strategy (Jan 2026).

**Contractor status:** The memo applies to "USACE Civil Works planners" and "District Study Teams." Contractors are not explicitly named as covered parties. Non-federal sponsors are mentioned only in the context of AI not replacing commitments to them (§5.b.1). The memo does not contain flow-down language binding contractors or consultants. Classified as NOT contractor-binding per methodology.md (must explicitly name contractors/third parties/consultants/vendors).

**Note:** USACE Civil Works is a DOW agency, not a DOT Operating Administration. It does not inherit USDOT 1351.41. Its AI governance flows from DOW/DA policy and EOs, not from DOT. This is a separate policy stream from the DOT agencies above.

---

## Cross-cutting observations

1. **USDOT 1351.41 is the umbrella; OA-level policies are sparse.** DOT Order 1351.41 (August 2026) establishes department-wide AI governance, but only the FAA has published an OA-level employee-facing AI use policy (Notice 1370.52). FHWA, FTA, FRA, NHTSA, FMCSA, and MARAD are all SILENT at the OA level — they inherit the department-level governance framework but have not translated it into employee-facing use rules.

2. **FAA is the only DOT OA that binds contractors.** FAA Notice 1370.52 explicitly names contractors as covered parties and imposes the same use restrictions. No other DOT OA has a contractor-binding AI use policy.

3. **USACE Civil Works operates under a separate (DOW) policy stream.** The USACE Civil Works AI Ethics Memo (April 2026) is the most detailed employee-facing AI use policy among the 9 agencies studied — it has explicit guiding principles, approved/prohibited uses, and governance roles. It does NOT bind contractors.

4. **The FAA Notice is time-limited.** FAA Notice 1370.52 carries a cancellation date of 03/23/2026 and is already listed as "Cancelled" on the FAA Orders webpage. No replacement was located. The FAA's AI posture should be re-verified in the next refresh.

5. **Research programs are not use policies.** All 9 agencies sponsor AI research (FHWA EAR, FTA STAR, FRA GTCD, NHTSA ADS, etc.), but research activity does not constitute an employee AI use policy. The Tracker scores what governs employee/contractor behavior, not what the agency funds.

6. **Contractor-binding count:** 1 of 9 (FAA). This contrasts sharply with Installment 1 (state DOTs), where 7 of 52 entities were contractor-binding. The federal layer is more permissive toward contractors on AI use — or more accurately, has not yet addressed the question.
