# Northeast State DOT AI Policy Corpus

Comparison of published AI / generative-AI policy posture across 13 Northeastern transportation entities, as of April 2026.

**Critical caveat up front:** none of the 13 transportation departments in scope have published a transportation-specific AI policy as a standalone document. In every case the operative policy is set by the state CIO / Office of Information Technology / state-level executive order, and the DOT inherits that policy. The "FORBID / ENCOURAGE / SILENT" bucket below therefore reflects the *applicable* statewide policy that governs DOT staff, not a DOT-issued document.

---

## Master Table

| # | Entity | AI policy? | Policy URL (governing) | Date | Bucket | General IT / parent posture | EO / statewide ref | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | **Connecticut (CTDOT)** | Partial — statewide, not DOT-specific | [CT Responsible AI Policy AI-01 / Framework](https://portal.ct.gov/-/media/OPM/Fin-General/Policies/CT-Responsible-AI-Policy-Framework-Final-02012024.pdf) | Feb 1, 2024 (Framework); subsequent Policy AI-01 | ENCOURAGE (with guardrails) | Statewide CT Responsible AI Policy AI-01 governs all executive-branch agencies including CTDOT | CT PA 23-16 (AI in state government, 2023); legislative AI cluster pending 2026 | LLM use requires supervisor approval per use case; no input of non-public info; CT was an early-mover on a written framework |
| 2 | **Delaware (DelDOT)** | Partial — statewide DTI policy, not DelDOT-specific | [DE Generative AI Policy (DTI)](https://webfiles.dti.delaware.gov/pdfs/pp/Generative%20Artificial%20Intelligence%20Policy.pdf) | Adopted July 2025 | ENCOURAGE (allow-list + block-list) | DTI Enterprise Policy applies to all state employees; DelDOT inherits | Delaware AI Commission (HB 333, 2024); statewide AI training launched March 2026 | Notable: explicit allow-list (ChatGPT, Gemini, Copilot, Bedrock) and explicit block (DeepSeek, RedNote — non-US tools); DelDOT runs an AI-enhanced ITMS funded by FHWA ATCMTD grant |
| 3 | **Maine (MaineDOT)** | Partial — statewide OIT policy, not MaineDOT-specific | [Maine GenAI Policy (OIT)](https://www.maine.gov/oit/sites/maine.gov.oit/files/inline-files/GenAIPolicy.pdf) | Supersedes June 21, 2023 moratorium; current policy late 2023 / 2024 | FORBID-leaning ENCOURAGE (heavily restricted) | OIT Cybersecurity Directive 23-03 + GenAI Policy govern all executive-branch | Gov. Mills EO Dec 20, 2024 (AI Task Force); Maine consumer AI transparency law signed June 12, 2025 | Maine had the longest formal moratorium of any state (≥6 months starting June 21, 2023); current policy still requires waivers/approvals and human review |
| 4 | **Maryland (MDOT)** | Partial — statewide DoIT Responsible AI Policy | [MD Responsible AI Policy](https://doit.maryland.gov/policies/ai/Pages/maryland-responsible-ai-policy.aspx) | v1.0 effective May 23, 2025 | ENCOURAGE (with risk classification) | DoIT policy governs MDOT; AI Subcabinet coordinates across | Gov. Moore EO 01.01.2024.02 (Jan 2024); AI Strategy & Roadmap submitted Jan 14, 2025 | Each agency must appoint an AI lead; Level 3/4 confidential data use is "high-risk"; MD has the most formal AI governance stack of any in scope |
| 5 | **Massachusetts (MassDOT)** | Partial — EOTSS GenAI Policy + MassDOT pilot | [EOTSS Enterprise GenAI Policy](https://www.mass.gov/policy-advisory/enterprise-use-and-development-of-generative-ai-policy) | EOTSS policy 2023; MA ChatGPT enterprise rollout Feb 2026 | ENCOURAGE (active deployment) | EOTSS policy governs all executive agencies including MassDOT | Healey administration ChatGPT-for-state-employees deal announced Feb 17, 2026 | Most aggressive deployer in scope: MA is first state to deploy ChatGPT across all ~40K executive-branch staff in walled-off env; MassDOT runs HEKA AI assistant for engineers |
| 6 | **New Hampshire (NHDOT)** | Partial — statewide DoIT policy, not NHDOT-specific | [SoNH Use of AI Technologies Policy](https://mm.nh.gov/files/uploads/doit/documents/sonh-use-of-artificial-intelligence-technologies-policy.pdf) + [NH AI Code of Ethics](https://www.doit.nh.gov/sites/g/files/ehbemt506/files/documents/2023-07/nh-code-of-ethics-for-ai-systems.pdf) | Code of Ethics June 20, 2023; HB 1688 effective July 1, 2024 | ENCOURAGE (with disclosure mandate) | DoIT AI policy + Code of Ethics governs all NH state agencies | HB 1688 signed by Gov. Sununu July 12, 2024 — prohibits AI used to manipulate, discriminate, or surveil the public | Mandatory disclosure if AI-generated content is published without human edit; user must be informed when interacting with AI |
| 7 | **New Jersey (NJDOT)** | Partial — statewide circular 25-OIT-001 | [NJ Guidance on Responsible Use of Generative AI](https://nj.gov/it/docs/ps/25-OIT-001-State-of-New-Jersey-Guidance-on-Responsible-Use-of-Generative-AI.pdf) | Circular 25-OIT-001 (2025); supersedes 23-OIT-007 | ENCOURAGE (training-gated) | NJ OIT joint circular governs all state employees; NJDOT inherits | NJ AI Task Force Report; NJ Innovation Authority + NJEDA Next NJ AI program | Mandatory "Responsible AI for Public Professionals" course before access; sensitive PII prohibited in non-state-approved tools |
| 8 | **New York (NYSDOT)** | NO DOT-specific policy — statewide ITS policy applies; **DOT explicitly flagged in audit** | [NY ITS Acceptable Use of AI Technologies](https://its.ny.gov/acceptable-use-artificial-intelligence-technologies) | ITS policy issued January 2024 | ENCOURAGE (formally) but **EFFECTIVELY SILENT at NYSDOT level** | ITS AI policy governs all state entities | Gov. Hochul: ITS issued AI policy at her direction (Jan 2024); RAISE Act signed Dec 19, 2025 (effective Jan 1, 2027) — but applies to AI developers, not state agencies | **OSC audit (April 3, 2025) found NYSDOT AI working group first met June 2024 and "has not yet issued any formal policies"; DOT had not trained staff on AI risk; piloting 3 AI systems** |
| 9 | **Pennsylvania (PennDOT)** | Partial — statewide policy + 4 Pa. Code Subch. KKK | [PA Generative AI page (OA)](https://www.pa.gov/agencies/oa/programs/information-technology2/gen-ai) + [4 Pa. Code Subch. KKK](https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/004/chapter7/subchapKKKtoc.html&d=reduce) | Gov. Shapiro EO Sept 2023; Subch. KKK promulgated thereafter | ENCOURAGE (post-pilot expansion) | OA Commonwealth policy governs all agencies including PennDOT | Gov. Shapiro EO Sept 2023 created **Generative AI Governing Board** | ChatGPT Enterprise pilot Mar 2024–Mar 2025 (~175 employees across agencies); commonwealth ranked top-3 for gov AI readiness; PA prohibits private data input + AI-only decisions about employees |
| 10 | **Rhode Island (RIDOT)** | NO — statewide AI Action Plan released, no employee-use policy yet | [RI AI Task Force / ETSS](https://etss.ri.gov/data-and-ai/rhode-island-ai-task-force) | EO 24-06 (2024); AI Action Plan Jan 2026 | SILENT (roadmap stage) | No published acceptable-use policy for state employees yet | Gov. McKee EO 24-06 "Artificial Intelligence and Data Centers of Excellence" | Roadmap stage; RI has explicitly chosen "embrace, not regulate"; sector-specific guidance issued only for insurance (DBR Bulletin 2024-03) |
| 11 | **Vermont (VTrans)** | Partial — statewide ADS policy, not VTrans-specific | [Vermont Agency of Digital Services AI](https://digitalservices.vermont.gov/ai) | 2022 Act 132 created governance bodies; policy iterative since | ENCOURAGE (center-for-enablement model) | ADS Division of AI provides "Center for Enablement" + templates to all agencies | 2022 Act 132 (Council on AI + Division of AI within ADS) | VTrans publicly uses AI for sign detection/geo-localization (research project) and pavement-condition prediction; no published VTrans-specific employee AI use policy |
| 12 | **District of Columbia (DDOT)** | Partial — citywide OCTO AI/ML Governance Policy | [DC OCTO AI/ML Governance Policy](https://octo.dc.gov/page/aiml-governance-policy) + [AI Procurement Handbook](https://techplan.dc.gov/sites/default/files/u23/1E.%20AI%20Procurement%20Handbook%20-FINAL.pdf) | Mayor's Order 2024-028 issued Feb 2024; Governance Policy effective date listed as TBD | ENCOURAGE (mandatory training + procurement handbook) | OCTO is the citywide policy authority; DDOT inherits | Bowser Mayor's Order 2024-028 — DC AI Values + 18-month strategic plan + AIVA advisory group | DC was first major US city to **mandate Responsible AI training** for all gov employees + contractors; OCTO operates DC Compass GenAI tool; DDOT separately published an AV (automated vehicle) Policy Report |
| 13 | **Puerto Rico (DTOP)** | NO published AI policy; pending legislation | (no published policy) — see [PRITS](https://www.pr.gov/) and [Puerto Rico AI Act bill](https://www.mzls.com/insights/puerto-rico-senate-introduces-significant-artificial-intelligence) | Government of PR AI Act introduced 2024–2025 (not yet enacted as of April 2026 research) | SILENT | No published acceptable-use policy at DTOP or PRITS for employees as of this research | Pending: "Government of Puerto Rico Artificial Intelligence Act" — would create AI Officer under PRITS, AI Advisory Council, biennial agency review | DTOP / Autoridad de Carreteras y Transportación (ACT) have no surfaced AI guidance; PR Senate bill would mandate it once enacted |

---

## Verbatim Excerpts

Where official policy PDFs were available in HTML form or quoted in reliable secondary sources. Several primary PDFs (CT Framework, NJ Circular, MD EO, NH policy PDF, Maine cybersecurity directive) returned binary content that could not be cleanly extracted via WebFetch — those are flagged as "PDF — extract via direct read."

### Connecticut — Responsible AI Policy AI-01 / Framework (Feb 1, 2024)
> "Employees must secure supervisory approval before using LLMs for each use case. Employees shall not input non-public information into LLMs. Additionally, employees using an LLM must review all information obtained from the LLM for accuracy, veracity and completeness."
*(As summarized from the CT Responsible AI Policy framework. Original PDF at portal.ct.gov — verbatim retrieval blocked at the WebFetch layer; the above is the canonical paraphrase widely cited.)*

### Delaware — DTI Generative AI Policy (adopted July 2025)
> "Use of GenAI on State devices must be limited to State purposes, and State users should act responsibly when using GenAI."
> "Employees are approved to use public versions of AI tools like ChatGPT and Gemini, and enterprise versions such as Microsoft Copilot and Amazon Bedrock."
> The policy "permits them to use many public and enterprise AI models, but not ones considered to be potentially malicious, like DeepSeek."
*(Sources: StateScoop and GovTech reporting on the published policy; original PDF at webfiles.dti.delaware.gov.)*

### Maine — Cybersecurity Directive 23-03 (June 21, 2023, moratorium) and current OIT GenAI Policy
> "Effective immediately, Wednesday, June 21, 2023, the adoption or use of Generative AI technology is prohibited for at least six months for all State of Maine business and on any device connected to the State of Maine network."
> The current GenAI Policy "supersedes the Chief Information Officer's GenAI Moratorium" and requires "human review and approval ... before using AI-generated content."
*(Original directive at maine.gov/oit; current GenAI Policy at the same domain.)*

### Maryland — Responsible AI Policy v1.0 (effective May 23, 2025)
> "Appointing an AI lead for their agency who is responsible for ensuring that the relevant DoIT and agency policies, guidance, and best practices ... are followed."
> Six guiding principles: "Human-Centered Design, Security & Safety, Privacy, Transparency, Equity, and Accountability."
> Systems processing "Level 3 (Confidential) or Level 4 (Restricted) data are classified as high-risk and require comprehensive risk assessments before deployment."

### Massachusetts — EOTSS Enterprise Generative AI Policy
> "Public models, such as public versions of ChatGPT, Gemini and Claude, are prohibited on state-issued devices, as is providing non-public state data to those platforms."
> The 2026 ChatGPT enterprise rollout is "within a walled-off, secure environment that protects state data and ensures that employee chat inputs do not train public AI models."
*(Sources: mass.gov enterprise policy advisory; Gov. Healey announcement Feb 17, 2026.)*

### New Hampshire — HB 1688 (signed July 12, 2024; effective July 1, 2024) and NH DoIT AI Code of Ethics (June 20, 2023)
> "Any material produced by generative AI that has not been reviewed and possibly edited by a human in an appropriate responsible position must be accompanied by disclosure that the content was generated by AI."
> "In all circumstances in which a human user is interacting with an AI system, either directly or indirectly, the user must be informed that they are interacting with an AI system."
> "All state agencies must review the use of AI in their computer systems to verify compliance ... with any prohibited AI systems to be removed."

### New Jersey — Joint Circular 25-OIT-001 (Guidance on Responsible Use of Generative AI)
> "Before accessing or using generative AI in their official capacity, all state employees should take the 'Responsible AI for Public Professionals' course."
> "When prompting any public AI assistant, tool, or anything that is not listed as a State-Approved AI Tool, employees should not disclose Sensitive Personally Identifiable Information."
*(Original circular PDF at nj.gov/it/docs/ps/25-OIT-001 — verbatim PDF extraction blocked; quotes above are from the NJCCIC summary on cyber.nj.gov and the NJIA portal.)*

### New York — ITS Acceptable Use of AI Technologies Policy (January 2024) + OSC Audit (April 3, 2025)
NYSDOT-specific finding from OSC audit:
> "DOT has an AI working group that first met in June 2024, but it has not yet issued any formal policies."
> NYSOFA, DOCCS, and DOT "do not have in-house policies or specific procedures to govern how AI is authorized, developed or used, for ensuring the data is unbiased and reliable, or have formal requirements of human oversight."
> "DOT has not provided training to staff on the general risks of AI."
> "DOT is piloting three AI systems."

### Pennsylvania — Commonwealth Generative AI Policy + Gov. Shapiro EO (Sept 2023)
> The Generative AI Governing Board "provide[s] employee-centered direction on all aspects of the design, development, procurement, and deployment of generative AI in Commonwealth agencies."
> The policy "prohibits using generative AI to make decisions for employees and requires the user to review and verify anything created by generative AI. Additionally, it prohibits putting any private data or information into generative AI tools."

### Rhode Island — Gov. McKee EO 24-06 + AI Action Plan (Jan 2026)
No employee acceptable-use policy yet. Posture statement from the Task Force lead (RIC Prof. Tim Henry): *"We're not looking to have the government in this area lay out strict regulations about AI."* RIDOT inherits no specific AI use policy as of April 2026.

### Vermont — Agency of Digital Services AI guidance (under 2022 Act 132)
ADS operates a "Center for Enablement" model — drafts policy, offers agencies templates. Vermont's posture: "always labeling documents with a human owner to preserve accountability." No VTrans-specific AI use policy located; VTrans research projects use ML for traffic-sign detection and pavement-patch prediction.

### District of Columbia — OCTO AI/ML Governance Policy + Mayor's Order 2024-028 (Feb 2024)
> "The usage of non-enterprise or free AI and ML platforms is discouraged, as they may pose potential risks to data security and privacy." (Section 4.3.1)
> "Anonymized or de-identified data should be used for AI and ML purposes if utilizing production data on commercial platforms or vendor proof of concepts." (Section 4.2.4)
> "Users, developers, and administrators should only use AI and ML technologies and/or platforms approved by OCTO or Agency Information technology division." (Section 4.1.2)
> "No AI tool shall be deployed unless the deploying agency has verified that the deployment will benefit District residents."

### Puerto Rico — DTOP / PRITS
No published acceptable-use policy. Pending bill ("Government of Puerto Rico Artificial Intelligence Act") would establish an AI Officer under PRITS, an AI Advisory Council, and biennial agency reviews. Status as of April 2026: introduced, not enacted.

---

## Quick Read

**Bucket counts (n=13):**
- **ENCOURAGE (with guardrails):** 9 — CT, DE, MD, MA, NH, NJ, PA, VT, DC
- **FORBID-leaning ENCOURAGE (heavily restricted):** 1 — ME (history of formal moratorium, current policy still tight)
- **EFFECTIVELY SILENT at DOT level:** 3 — NY (statewide policy exists but OSC found NYSDOT had no in-house policy as of April 2025), RI (state still in roadmap stage), PR (bill pending)
- **Pure FORBID (no AI on agency data, full stop):** 0

**Surprising findings:**
1. **Zero standalone DOT AI policies.** Every transportation department in scope inherits from the state CIO / OIT / OCTO. No DOT in the Northeast has published its own AI acceptable-use document.
2. **NYSDOT is the laggard among large DOTs.** The NY State Comptroller's April 2025 audit explicitly named DOT as having no in-house AI policy, no staff training on AI risks, while already piloting three AI systems. This is a real story for the newsletter — biggest population, biggest federal-aid pipeline, weakest internal AI governance.
3. **Massachusetts is the outlier in the other direction.** Healey administration is the first state to deploy ChatGPT enterprise across all ~40K executive-branch employees (Feb 2026), and MassDOT already runs HEKA, a custom GenAI assistant for engineers. The walled-garden architecture is the policy.
4. **DC has the most prescriptive non-enterprise rule** ("non-enterprise or free AI ... is discouraged") plus a published AI Procurement Handbook — useful concrete model.
5. **Delaware is the only one publishing an explicit allow-list / block-list** (DeepSeek, RedNote out; ChatGPT, Gemini, Copilot, Bedrock in).

**Gaps to flag for IC readers:**
- Federal-aid project teams and consulting PMs should assume **the state CIO policy is the operative rule**, not anything from the DOT itself, in 12 of 13 cases.
- For NYSDOT, RIDOT, and DTOP staff/consultants: there is **no published rulebook** specific to your agency. Treat any cloud AI use of project data as an unsettled risk and escalate.
- For procurement language on AI in contracts: only DC has published a formal AI Procurement Handbook; PA's Subch. KKK is the closest peer in code.
- "Responsible AI training" is now a published prerequisite in NJ (mandatory), DC (mandatory), and DE (strongly encouraged). Watch for that to become contract-flow-down language for engineering consultants.
