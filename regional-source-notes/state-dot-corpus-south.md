# Southern State DOT AI Policy Corpus (14 States)

**Compiled:** 2026-04-29
**Audience:** Working civil engineers, PEs, and PMs on federal-aid and state-funded transportation projects
**Question being answered:** What does each Southern state DOT publicly say about AI use on transportation projects?

**Important methodology note:** Almost no state DOT in the South has issued its *own standalone* AI policy. The operative governance for nearly every state in this list is the **statewide AI policy / executive order** that flows through the state CIO or Office of Information Technology and binds all executive-branch agencies, *including the DOT*. The "Bucket" column reflects the policy that actually governs DOT staff conduct, even when issued at the state level.

---

## Master Table

| # | State (DOT) | AI-specific policy? | Policy URL | Date issued / updated | Bucket | General IT / parent posture | Statewide EO or CIO reference | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | **Alabama (ALDOT)** | Partial — bound by statewide EO 738 + OIT AI Governance Policy; no ALDOT-specific policy located | [oit.alabama.gov AI Governance Policy](https://oit.alabama.gov/wp-content/uploads/2025/01/Artificial-Intelligence-Governance-Policy.pdf); [EO 738](https://governor.alabama.gov/assets/2024/02/EO-738-Artificial-Intelligence.pdf) | EO 738: Feb 8, 2024; GenAI Task Force Final Report: Mar 2025; OIT AI Governance Policy: Jan 2025 | ENCOURAGE (with guardrails) | OIT AI Governance Policy is the binding posture. ALDOT already uses AI/IoT for ASAP roadside-assistance video analytics. | Gov. Ivey EO 738 created the GenAI Task Force; final report published Mar 2025. ~25% of state agencies already using GenAI. | No standalone ALDOT AI policy located. ALDOT operates AI/IoT incident-detection (ASAP program) but governance flows from OIT. |
| 2 | **Arkansas (ARDOT)** | No DOT-specific policy — state-level AI CoE just stood up (subcommittee of Data and Transparency Panel) | [ARDOT IT division](https://ardot.gov/divisions/information-technology/) (no AI policy posted) | AI CoE launched 2025; Act 927 (AI content/likeness) signed 2025 | SILENT | No published ARDOT acceptable-use policy on AI located. Default state IT acceptable-use governs. | Gov. Sanders has been vocal on AI federalism but has not issued a state employee AI EO. AI and Analytics Center of Excellence (AI CoE) is the working group. | ARDOT is **deploying** AI for enforcement (work-zone speed/phone-detection cameras Jan 2026; $2.7M Quarterhill mainline-sorter on I-40/I-55) but has not published staff use guidance. |
| 3 | **Florida (FDOT)** | **YES** — FDOT-specific AI policy, one of the earliest among state DOTs | [HNTB summary](https://www.hntb.com/think/think-innovation-in-motion-fdots-approach-for-artificial-intelligence-success/); [FDOT AI symposium deck (PDF)](https://fdotwww.blob.core.windows.net/sitefinity/docs/default-source/design/training/transportationsymposium/2024-june/2024nov-thu01-floridaemergingtechaiuaspolicies.pdf); [Florida CIO AI guidance](https://www.flgov.com/eog/news/press/2025/governor-ron-desantis-announces-proposal-citizen-bill-rights-artificial) | FDOT AI Policy: **May 2024** | ENCOURAGE (with guardrails) | "Pilots over giant leaps" — guardrails first, then scale. Keep humans in the loop for all AI-influenced activities. | Gov. DeSantis "Citizen Bill of Rights for AI" proposal (2025); Florida State CIO AI guidance referenced separately. | RFP #DOT-RFP-25-9078-SJ ($100K, 2025) procuring an AI system to interpret FDOT *Standard Specifications for Road and Bridge Construction*. Statute also requires FDOT's Next-generation Traffic Signal Modernization Grant Program. |
| 4 | **Georgia (GDOT)** | Partial — bound by GTA SS-23-002 (Responsible Use Standard) and GS-23-001 (Guidelines); no GDOT-specific policy located | [GTA SS-23-002](https://gta-psg.georgia.gov/psg/artificial-intelligence-responsible-use-ss-23-002); [GTA GS-23-001](https://gta-psg.georgia.gov/psg/artificial-intelligence-responsible-use-guidelines-gs-23-001); [GA Office of AI](https://ai.georgia.gov/) | SS-23-002 effective **Dec 1, 2024**; "Red Light, Green Light" GenAI guidelines updated Aug 1, 2025 | ENCOURAGE (heavily gated) | Pre-vetted-tools-only model. Prior GTA authorization required for any GenAI tool used regularly. | SB37 (2025) establishes GA Board for AI; mandates AI usage plans for every agency by Dec 31, 2026. | GDOT will be required to publish its own AI usage plan by end of 2026 under SB37. |
| 5 | **Kentucky (KYTC)** | Partial — bound by COT CIO-126 AI Policy + 2025 SB4 (AI Governance Framework) | [COT CIO-126 AI Policy (PDF)](https://technology.ky.gov/policies-and-procedures/PoliciesProcedures/CIO-126%20Artificial%20Intelligence%20Policy.pdf); [KY SB4 summary](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/kentucky-passes-bill-to-regulate-ai-in-government) | SB4 signed Mar 24, 2025 | ENCOURAGE (with mandatory human review) | "An AI tool may be used to generate information that will be an input to an overall process, but no consequential decision shall be rendered without human review." | SB4 gives Commonwealth Office of Technology (COT) authority over GenAI policy/procedures. Each cabinet must submit annual AI usage report to COT by Dec 1. | KYTC has shipped a notable application: a custom-trained chatbot assistant for the *Complete Streets, Roads, and Highways Manual* (built with Gresham Smith). |
| 6 | **Louisiana (LaDOTD)** | Partial — bound by OTS AI Acceptable Use Policy + EO JML 25-103 / 25-109 | [OTS AI Acceptable Use Policy](https://www.doa.la.gov/doa/ots/policies-and-forms/artificial-intelligence-acceptable-use-policy/); [EO JML 25-109 (amended)](https://www.doa.la.gov/media/tzqptbak/jml-25-109-amended-state-government-s-use-of-ai.pdf) | OTS AUP effective **Sept 29, 2025**; EO JML 25-103 (Aug 2025); EO JML 25-109 (amended) | **FORBID** (for confidential/restricted data into commercial AI) | Strictest acceptable-use posture in the South, paired with explicit procurement gate. | Gov. Landry EO JML 25-103 paused state AI procurement until Dec 15, 2025. Separate EO bans Chinese-government AI tools (DeepSeek, etc.) on state systems. | "State-approved systems, accounts, and equipment are the only authorized means for using AI when conducting state business." All AI software must be submitted to OTS for review *prior to procurement*. |
| 7 | **Mississippi (MDOT)** | Partial — bound by ITS AI Acceptable Use Policy (EO 1584) | [ITS AI-AUP](https://www.its.ms.gov/services/innovating/AI-AUP); [EO 1584 coverage](https://statescoop.com/mississippi-governor-tate-reeves-ai-executive-order/) | ITS AI-AUP approved **Nov 25, 2025**; EO 1584 (Mississippi's first AI EO) | ENCOURAGE (with hard data + foreign-AI prohibitions) | "Sensitive, confidential, or personally identifiable information (PII) may not be entered into unapproved AI tools." | Gov. Reeves EO 1584 directed ITS to inventory all AI in state agencies and develop fairness/privacy/transparency policies. | Banned uses include foreign-adversary-operated AI, deepfakes, AI-only final decisions, and entering confidential data into unapproved tools. No standalone MDOT policy located. |
| 8 | **North Carolina (NCDOT)** | Partial — bound by Gov. Stein EO 24 + NCDIT AI Governance Framework | [NCDIT AI Resources](https://it.nc.gov/resources/artificial-intelligence); [EO 24](https://governor.nc.gov/executive-order-no-24-advancing-trustworthy-artificial-intelligence-benefits-all-north-carolinians) | EO 24: 2025 (Gov. Stein) | ENCOURAGE | Statewide AI Governance Framework: fairness, accountability, transparency, security, privacy, civil liberties. | EO 24 creates AI Leadership Council, AI Accelerator at NCDIT, and oversight teams in each agency. | NCDOT shipped the **largest live statewide AI traffic-signal deployment in the U.S.** — 2,500+ intersections via Flow Labs. Also using AI for language access on transit/airports. |
| 9 | **Oklahoma (ODOT)** | Partial — bound by OMES "Use of AI in Oklahoma State Government Standard" | [OMES AI policy page](https://oklahoma.gov/ai/policy.html); [Use of AI Standard (PDF)](https://oklahoma.gov/content/dam/ok/en/omes/documents/use-of-ai-in-oklahoma-standard.pdf) | EO establishing Task Force: 2023; current Standard: undated, "shall take effect upon publication" | **FORBID** (for federally-protected data — termination consequence) | Most explicit personal-consequence language found in any state in this set. | Gov. Stitt 2023 EO; Task Force on Emerging Technologies. CIO has "sole and exclusive authority over all information technology acquisitions, including AI systems" under ITCCA. | "Any state employee who inputs, uploads, transmits or otherwise discloses any federally protected data into a public AI system…shall be terminated." All AI procurement requires CIO signature. |
| 10 | **South Carolina (SCDOT)** | Partial — bound by SC Department of Administration State AI Strategy | [SCAIStrategy page](https://admin.sc.gov/SCAIStrategy); [SC Judicial Interim AI Policy](https://www.sccourts.org/about/court-news/2025-08-15/interim-policy-on-the-use-of-generative-artificial-intelligence/) | SC State AI Strategy: **June 19, 2024** | ENCOURAGE (strategy-level, not yet rule-level) | "Three Ps: Protect, Promote, Pursue." Strategy is a vision document; binding agency-level rules are limited. | No statewide GenAI executive order located for executive-branch employees. SC Supreme Court has separate interim policy for judiciary (Mar 25, 2025). | No standalone SCDOT AI policy located. Of the SREB Southern states, SC's executive-branch posture is the lightest-touch in this set. |
| 11 | **Tennessee (TDOT)** | Partial — bound by Enterprise AI Policy 200-POL-007 + Enterprise GenAI Policy + ISC Policy 3.00 | [Enterprise GenAI Policy (PDF)](https://www.tn.gov/content/dam/tn/finance/aicouncil/documents/TN%20Enterprise%20Generative%20AI%20Policy.pdf); [200-POL-007 (PDF)](https://www.tn.gov/content/dam/tn/finance/artificial-intelligence/200-POL-007%20Enterprise%20Artificial%20Intelligence%20Policy.pdf); [TN AI Council Action Plan (Nov 2025)](https://www.tn.gov/content/dam/tn/finance/aicouncil/documents/TN%20AI%20Advisory%20Council%20Action%20Plan%20-%20November%202025.pdf) | Enterprise GenAI Policy & 200-POL-007: 2024-2025 (versioned); AI Advisory Council Action Plan: Nov 2025 | ENCOURAGE (data-class gated) | "Ensures that State personnel have access to Generative AI technologies in a way that safeguards State data and limits the possibility of State data being actively used in consumption or training of public Generative AI solutions." | Gov. Lee EO No. 2 and EO No. 3. Tenn. Code § 49-7-185 requires AI policy adoption + posting. Gov. Lee FY26 amended budget proposes $50M for AI infrastructure. | Policy applies to all branches/agencies/boards/commissions — TDOT inherited. Tennessee has clearly distinguished GenAI from broader AI in its policy stack (rare). |
| 12 | **Texas (TxDOT)** | **YES** — TxDOT-specific AI Strategic Plan (FY 2025-2027) | [TxDOT AI Strategic Plan page](https://www.txdot.gov/about/leadership/strategic-plans/txdot-artificial-intelligence-strategic-plan-update.html); [GovTech update coverage](https://www.govtech.com/artificial-intelligence/texas-department-of-transportation-updates-ai-strategic-plan) | Original Strategic Plan: **Jan 2025**; update: **Jan 21, 2026** | ENCOURAGE (most fully developed in the South) | TxDOT runs an AI Risk Management Workgroup applying the **NIST AI Risk Management Framework**. | **Texas Responsible Artificial Intelligence Governance Act (TRAIGA)** signed by Gov. Abbott **June 22, 2025** — sets statutory requirements for TxDOT AI use. | 70-page plan, 230 use cases, 22 active deployments. **Microsoft 365 Copilot deployed to 940+ staff.** **Professional Engineering Procurement Services Division saved an estimated 22,000 staff hours annually by automating invoice workflows.** Manual invoice processing went from 3 weeks → 27 seconds in some cases. |
| 13 | **Virginia (VDOT)** | Partial — bound by VITA "Utilization of AI by COV" Standard + EO 30 + EO 46 | [VITA AI page](https://www.vita.virginia.gov/policy--governance/governance/artificial-intelligence/); [VITA AI Standard (PDF)](https://www.vita.virginia.gov/media/vitavirginiagov/it-governance/ea/pdf/Utilization-of-Artificial-Intelligence-by-COV-Policy-Standard.pdf) | VITA AI Standard: **June 27, 2024**; EO 30 (Gov. Youngkin); EO 46 (DeepSeek prohibition) | ENCOURAGE (with required compliance for all stand-alone, embedded, and GenAI) | Standard "applies to both existing and new uses of AI, including stand-alone, AI embedded, and generative AI within other systems or applications." | Gov. Youngkin EO 30 established the AI standards/guidelines and AI task force. EO 46 prohibits DeepSeek on state systems. | VDOT publicly piloting AI for cost estimation + pavement management with Deloitte (March 2025) — direct response to 68% nationwide highway construction cost surge since 2020. |
| 14 | **West Virginia (WVDOT)** | No — WVOT Acceptable Use Policy and Ethical Guidance both listed "coming soon" | [WVOT AI page](https://technology.wv.gov/policy-governance/artificial-intelligence); [WV Code §5A-6-9](https://code.wvlegislature.gov/5A-6-9/) | WV Task Force on AI: organized in Office of the Governor; AI AUP: **not yet published** | SILENT (interim approved-tool list only) | "The use of AI within your agency is ultimately subject to your internal policies." Bans tools that transmit data outside the U.S. and FCC Secure Networks Act-listed tools. | WV Task Force on AI has reported but no signed enterprise EO with operational rules located. AI Task Force agenda Jan 23, 2026. | Approved tool list (active): Google Gemini for Workspace, Microsoft Copilot Chat, Microsoft Copilot Studio (CIO review required), Grammarly, Gemini Apps. WV is **already applying AI to road maintenance** (pilot bill passed 2023). |

---

## Verbatim Excerpts (Operative Clauses)

### Florida (FDOT) — May 2024 AI Policy

> "Keeping humans in the loop for all AI-influenced activities."
>
> Organizations must "protect people's privacy and comply with all applicable data protection regulations, ensure human validation of the AI data and output, and protect information that is exempt from public disclosure per Florida's public records laws."

(Source: HNTB summary of FDOT's May 2024 AI Policy. Full policy referenced in FDOT 2024 Transportation Symposium deck "Emerging Technology Program Artificial Intelligent in FDOT" by Jeremy Dilmore, PE.)

### Georgia (GTA SS-23-002, effective Dec 1, 2024)

> "Use AI tools only for their intended purpose and in accordance with any applicable laws and regulations."
>
> "Exercise due diligence and critical thinking when using AI-generated outputs and guard against intentional and unintentional misuse of AI."
>
> "All confidential information or sensitive and personal data must be authorized by appropriate agency authority for use in the manner proposed and, when used, is anonymized, encrypted, or otherwise protected when used with AI tools."

> *Procurement gate:* "Agencies must submit a Business Solutions Review request to GTA before acquiring new AI tools. GTA will assess the tool for safety, privacy, and compliance before approval."

### Kentucky (CIO-126; codified by SB4, signed Mar 24, 2025)

> "An AI tool may be used to generate information that will be an input to an overall process, but no consequential decision shall be rendered without human review."

> "COT shall mandate a minimum level of AI training for users and agencies responsible for the business processes that are incorporating generative AI."

### Louisiana (OTS AI Acceptable Use Policy, effective Sept 29, 2025)

> "State-approved systems, accounts, and equipment are the only authorized means for using AI when conducting state business."

> *Prohibited:* "Entering confidential, proprietary, and restricted state data (e.g., passwords, credit card numbers, health records) into commercially available AI systems."

> *Procurement gate:* "Agencies shall submit all software, applications, tools, and services utilizing AI for business operations to OTS for review prior to procurement and implementation."

### Mississippi (ITS AI-AUP, approved Nov 25, 2025)

> "Sensitive, confidential, or personally identifiable information (PII) may not be entered into unapproved AI tools. Any AI system using PII requires additional safeguards and approval."

> *Prohibited uses:*
> - "Using AI to generate deepfakes, impersonations, or misleading content"
> - "Relying on AI to make final or sensitive decisions (e.g., legal, personnel, compliance)"
> - "Using AI systems owned or operated by foreign adversaries"
> - "Entering confidential or personal data into unapproved AI tools"
> - "Treating AI output as accurate without human verification"

### Oklahoma (OMES "Use of AI in Oklahoma State Government Standard")

> "Do not use sensitive topics or sensitive state data within the tool such as personal identifiable information ('PII'), financial information, health data, authentication data or any other sensitive information."

> "Any state employee who inputs, uploads, transmits or otherwise discloses any federally protected data into a public AI system…shall be terminated."

> "The CIO holds sole and exclusive authority over all information technology acquisitions, including AI systems… The CIO shall be a required signatory on every acquisition involving AI."

### Tennessee (Enterprise GenAI Policy)

> "Ensures that State personnel have access to Generative AI technologies in a way that safeguards State data and limits the possibility of State data being actively used in consumption or training of public Generative AI solutions."

> Policy "applies to all branches, agencies, departments, boards, and commissions of State government."

### Texas (TxDOT AI Strategic Plan FY2025-2027; updated Jan 21, 2026)

> "The Professional Engineering Procurement Services Division has saved an estimated 22,000 staff hours annually by automating invoice workflows."
> *(Source: TxDOT AI Strategic Plan update, reported via Government Technology, Jan 21, 2026.)*

> "Generative AI (GenAI) tools such as Microsoft 365 Copilot have been deployed to more than 940 staff members for use in administrative tasks, document generation and meeting summaries."

> Statutory backbone: **Texas Responsible Artificial Intelligence Governance Act (TRAIGA)**, signed by Gov. Abbott June 22, 2025. TxDOT operates an AI Risk Management Workgroup applying the **NIST AI Risk Management Framework**.

### Virginia (VITA "Utilization of AI by COV" Policy Standard, June 27, 2024)

> Standard "applies to both existing and new uses of AI, including stand-alone, AI embedded, and generative AI within other systems or applications."
>
> (Operative companion EOs: Gov. Youngkin EO 30 establishing AI standards/task force; EO 46 prohibiting DeepSeek on state systems.)

### West Virginia (WVOT Interim Guidance)

> "The use of AI within your agency is ultimately subject to your internal policies."
>
> Prohibits "any AI model that transmits data outside of the United States" and tools "listed under the FCC Secure Networks Act."
>
> Approved tools list (active): Google Gemini for Workspace, Microsoft Copilot Chat, Microsoft Copilot Studio (CIO review required), Grammarly, Gemini Apps.
>
> WVOT Acceptable Use Policy and Ethical Guidance: "coming soon."

### Alabama (OIT AI Governance Policy, Jan 2025; EO 738, Feb 8, 2024)

EO 738 established the Generative AI Task Force chaired by OIT Secretary Daniel Urquhart. The OIT AI Governance Policy is the binding agency-level posture; ALDOT inherits. Final task force report (Mar 2025) found ~25% of state agencies were already using GenAI.

### North Carolina (Gov. Stein EO 24, 2025)

EO 24 creates an AI Leadership Council, an AI Accelerator at NCDIT, and oversight teams in each state agency. Statewide framework principles: fairness, accountability, transparency, security, privacy, protection of civil liberties. NCDOT inherits.

### Arkansas (no published DOT AI policy)

State-level AI and Analytics Center of Excellence (AI CoE) — subcommittee of the Data and Transparency Panel — is the working group setting forthcoming guidelines. Act 927 (2025) addresses AI-generated content/likeness rights. No verbatim DOT AI use clause located.

### South Carolina (SC AI Strategy, June 19, 2024)

> Strategy "is steadfastly rooted in the three Ps: Protect, Promote and Pursue" and "outlines the state's AI vision, guiding principles, goals and actions necessary for the productive and responsible use of AI for state agencies."

(Vision-level only. SCDOT-specific operational rules not located.)

---

## Quick Read (Synthesis)

**Bucket counts (n=14):**
- **FORBID** (explicit prohibitions on uploading agency/contract data to commercial AI): **2** — Louisiana, Oklahoma
- **ENCOURAGE** (explicitly permits AI with stated guardrails — training, citation, human review, approved tools): **9** — Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, Tennessee, Texas, Virginia
- **SILENT** (no operational AI policy currently published): **3** — Arkansas, South Carolina (strategy only, no rules), West Virginia (AUP listed "coming soon")

**Surprising finding:** Only **two** of the 14 Southern DOTs have published their *own* DOT-specific AI policy — **FDOT** (May 2024) and **TxDOT** (Strategic Plan FY2025-2027, updated Jan 2026). Every other DOT in the South operates under the parent state CIO/OIT/ITS policy. For the working PE/PM, this means the operative rule on whether you can paste a project memo into ChatGPT is set by the state IT agency, not the DOT — and varies materially. Oklahoma is the only state with explicit *termination* consequence language for federally-protected data uploads. Louisiana's "state-approved systems are the only authorized means" is the strictest practical posture. Texas is by far the most operationally mature, with 22,000 staff hours saved on invoice automation and Copilot deployed to 940+ staff under TRAIGA + NIST AI RMF governance.

**Gaps to flag:**
- ALDOT, ARDOT, MDOT, SCDOT, WVDOT, KYTC, NCDOT, GDOT, VDOT, LaDOTD, ODOT, TDOT — none have a public DOT-specific AI policy. Federal-aid PMs working in these states should reference the parent state policy, not the DOT site, when answering "can I use AI on this contract?"
- Procurement language is the most uneven dimension: GA, LA, OK have explicit pre-acquisition gates; most others are silent on whether a consultant can use AI in delivering a contract product.
- FDOT's RFP #DOT-RFP-25-9078-SJ (procuring an AI to interpret its own *Standard Specifications for Road and Bridge Construction*) is the most concrete signal in the South that DOTs are starting to bake AI into design/spec workflows, not just operations/ITS.
- Georgia SB37 (Dec 31, 2026 deadline for every agency to publish an AI usage plan) is the deadline most likely to trigger a wave of new GDOT-specific guidance worth tracking.

---

## Sources

- [TxDOT AI Strategic Plan (page)](https://www.txdot.gov/about/leadership/strategic-plans/txdot-artificial-intelligence-strategic-plan-update.html)
- [GovTech: TxDOT Updates AI Strategic Plan (Jan 2026)](https://www.govtech.com/artificial-intelligence/texas-department-of-transportation-updates-ai-strategic-plan)
- [TxDOT launches AI Strategic Plan (newsroom)](https://www.txdot.gov/about/newsroom/statewide/txdot-launches-ai-strategic-plan.html)
- [FDOT 2024 Symposium AI/UAS Policies deck (PDF)](https://fdotwww.blob.core.windows.net/sitefinity/docs/default-source/design/training/transportationsymposium/2024-june/2024nov-thu01-floridaemergingtechaiuaspolicies.pdf)
- [HNTB: FDOT's Approach for AI Success](https://www.hntb.com/think/think-innovation-in-motion-fdots-approach-for-artificial-intelligence-success/)
- [FDOT $100K AI Procurement (RFP DOT-RFP-25-9078-SJ)](https://floridaprocurements.com/florida-dot-ai-procurement-glimpse-into-future/)
- [VITA Artificial Intelligence Standard (PDF, 6/27/2024)](https://www.vita.virginia.gov/media/vitavirginiagov/it-governance/ea/pdf/Utilization-of-Artificial-Intelligence-by-COV-Policy-Standard.pdf)
- [VITA Artificial Intelligence policy hub](https://www.vita.virginia.gov/policy--governance/governance/artificial-intelligence/)
- [NCDIT Artificial Intelligence](https://it.nc.gov/resources/artificial-intelligence)
- [NC Gov. Stein Executive Order No. 24](https://governor.nc.gov/executive-order-no-24-advancing-trustworthy-artificial-intelligence-benefits-all-north-carolinians)
- [Tennessee Enterprise Generative AI Policy (PDF)](https://www.tn.gov/content/dam/tn/finance/aicouncil/documents/TN%20Enterprise%20Generative%20AI%20Policy.pdf)
- [Tennessee Enterprise AI Policy 200-POL-007 (PDF)](https://www.tn.gov/content/dam/tn/finance/artificial-intelligence/200-POL-007%20Enterprise%20Artificial%20Intelligence%20Policy.pdf)
- [Tennessee AI Advisory Council Action Plan Nov 2025 (PDF)](https://www.tn.gov/content/dam/tn/finance/aicouncil/documents/TN%20AI%20Advisory%20Council%20Action%20Plan%20-%20November%202025.pdf)
- [GA Office of Artificial Intelligence](https://ai.georgia.gov/)
- [GTA SS-23-002 Responsible Use Standard](https://gta-psg.georgia.gov/psg/artificial-intelligence-responsible-use-ss-23-002)
- [GTA GS-23-001 Responsible Use Guidelines](https://gta-psg.georgia.gov/psg/artificial-intelligence-responsible-use-guidelines-gs-23-001)
- [Alabama EO 738 (PDF)](https://governor.alabama.gov/assets/2024/02/EO-738-Artificial-Intelligence.pdf)
- [Alabama OIT AI Governance Policy (PDF, Jan 2025)](https://oit.alabama.gov/wp-content/uploads/2025/01/Artificial-Intelligence-Governance-Policy.pdf)
- [Alabama GenAI Task Force Final Report (Mar 2025)](https://governor.alabama.gov/newsroom/2025/03/governor-ivey-releases-genai-task-force-final-report/)
- [Arkansas DOT IT Division](https://ardot.gov/divisions/information-technology/)
- [Arkansas AI Working Group (Government Technology)](https://www.govtech.com/artificial-intelligence/new-arkansas-ai-working-group-will-guide-implementation)
- [Kentucky COT CIO-126 AI Policy (PDF)](https://technology.ky.gov/policies-and-procedures/PoliciesProcedures/CIO-126%20Artificial%20Intelligence%20Policy.pdf)
- [Kentucky SB4 summary (Akin)](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/kentucky-passes-bill-to-regulate-ai-in-government)
- [KYTC Complete Streets Manual + Chatbot (Gresham Smith)](https://www.greshamsmith.com/projects/kentucky-transportation-cabinets-complete-streets-roads-and-highways-manual/)
- [Louisiana OTS AI Acceptable Use Policy](https://www.doa.la.gov/doa/ots/policies-and-forms/artificial-intelligence-acceptable-use-policy/)
- [Louisiana EO JML 25-109 amended (PDF)](https://www.doa.la.gov/media/tzqptbak/jml-25-109-amended-state-government-s-use-of-ai.pdf)
- [Louisiana EO JML 25-103 (PDF)](https://gov.louisiana.gov/assets/ExecutiveOrders/2025/JML-Exective-Order-25-103.pdf)
- [Mississippi ITS AI Acceptable Use Policy](https://www.its.ms.gov/services/innovating/AI-AUP)
- [Mississippi EO 1584 coverage (StateScoop)](https://statescoop.com/mississippi-governor-tate-reeves-ai-executive-order/)
- [Oklahoma AI Policy](https://oklahoma.gov/ai/policy.html)
- [Oklahoma "Use of AI in Oklahoma State Government Standard" (PDF)](https://oklahoma.gov/content/dam/ok/en/omes/documents/use-of-ai-in-oklahoma-standard.pdf)
- [South Carolina State AI Strategy](https://admin.sc.gov/SCAIStrategy)
- [West Virginia Office of Technology AI page](https://technology.wv.gov/policy-governance/artificial-intelligence)
- [West Virginia Code §5A-6-9](https://code.wvlegislature.gov/5A-6-9/)
- [NCDOT AI traffic signal deployment (StateScoop)](https://statescoop.com/north-carolina-ai-traffic-signal-management-software-2025/)
- [VDOT AI cost estimation pilot (Virginia Mercury)](https://virginiamercury.com/2025/03/07/vdot-bets-on-ai-to-cut-costs-and-keep-virginia-roads-smooth/)
- [TxDOT AI overview (ASCE Source)](https://www.asce.org/publications-and-news/civil-engineering-source/article/2025/09/18/texas-dot-works-to-leverage-power-of-ai)
- [Eno: AI Transforming Transportation Agencies — Texas](https://enotrans.org/article/ai-is-transforming-transportation-agencies-starting-in-texas/)
- [ARDOT AI workzone cameras (Tech.co)](https://tech.co/news/arkansas-interstates-deploy-ai-tech)
- [ARDOT-Quarterhill mainline sorter (Trucking Dive)](https://www.truckingdive.com/news/arkansas-dot-plans-efficient-freight-management-ai-driven-project-quarterhill/802658/)
