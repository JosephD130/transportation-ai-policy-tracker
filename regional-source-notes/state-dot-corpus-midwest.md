# State DOT AI Policy Corpus — Midwest (12 states)

**Audience:** Working civil engineers, PEs, and PMs on federal-aid and state-funded transportation projects.
**Scope:** What every Midwestern state DOT — or its parent state — formally says about AI use on agency / contract work.
**Pulled:** April 2026. Treat dated docs as snapshots; verify with the agency before relying for compliance.

---

## Master table

| # | State (DOT) | AI-specific DOT policy? | Policy URL | Date issued / updated | Bucket | General IT / acceptable-use posture | Statewide / Governor reference | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | Illinois (IDOT) | No standalone DOT policy located. Bound by statewide DoIT policy. | DoIT: https://doit.illinois.gov/content/dam/soi/en/web/doit/documents/support/policies/2021/20250401-DoIT-AI%20Policy-v2-%20A11Y.pdf | DoIT v2 effective Apr 1, 2025 | FORBID (via DoIT) | DoIT "Policy on the Acceptable and Responsible Use of AI" applies to all agencies as AI Consumers/Creators; agencies must designate AI-policy lead within 30 days. | HB 3773 (employment AI, eff. Jan 1 2026); Generative AI & NLP Task Force (20 ILCS 1370/1-80). | No agency-specific DOT AI directive published; binding state policy is DoIT umbrella. |
| 2 | Indiana (INDOT) | No standalone INDOT policy located. Bound by State Agency AI Systems Policy. | https://www.in.gov/mph/AI/ ; State Agency AI Systems Policy PDF: https://www.in.gov/mph/cdo/files/State-of-Indiana-State-Agency-AI-Systems-Policy.pdf | Policy released 2024; document metadata Dec 13, 2024 | FORBID (via OCDO) | Office of Chief Data Officer requires every AI use case to pass an AI Readiness Questionnaire and obtain an AI Policy Exception before deployment, based on NIST AI RMF (72 sub-categories). Use of unapproved AI systems "expressly prohibited." Carve-out: employees may use web-based generative AI like ChatGPT for general productivity. | "Ask Indiana" GenAI chatbot launched May 2025; Indiana Fair Information Practices Act requires "just-in-time" notice to users interacting with AI. | INDOT does not publish a public AI directive; subject to OCDO. |
| 3 | Iowa (Iowa DOT) | No standalone DOT policy located. Bound by State of Iowa Generative AI Policy (PY-AI). | https://dom.iowa.gov/media/785/download?inline= ; https://dxsandbox.iowa.gov/state-iowa-generative-artificial-intelligence-ai-policy | Effective Mar 31, 2025 | FORBID | Statewide Department of Management policy: "The use of freely available AI tools by state entities is expressly prohibited without prior written approval from the Department of Management." Sensitive/protected data prohibited as AI input. Mandatory human evaluation of all AI output. Contractors/3rd parties bound. | Technology Association of Iowa AI Policy Subcommittee. | One of the more restrictive state postures: requires explicit DOM approval for every free AI tool. |
| 4 | Kansas (KDOT) | No standalone KDOT policy located. Bound by statewide policy P8200.00. | https://www.governor.ks.gov/wp-content/uploads/2023/08/P8200.00-Generative-Artificial-Intelligence-Signed.pdf | Signed Aug 2023; effective late Jul 2023 | FORBID (data) / ENCOURAGE (use) | Office of IT Services policy: restricted-use information cannot be entered into generative AI; everything entered into ChatGPT-style tools is treated as part of the public record. Output must be reviewed by knowledgeable human operators before action/dissemination. Contractors must disclose any generative AI use in contracts and may not use confidential/restricted data in queries or model training. | Gov. Laura Kelly directive, Aug 18, 2023. | Strong contractor disclosure language — relevant for state-funded design/CE&I contracts. |
| 5 | Michigan (MDOT) | No standalone MDOT policy located. Bound by DTMB AI Guidelines. | https://www.michigan.gov/dtmb/-/media/Project/Websites/dtmb/Law-and-Policies/Governance/State-of-MichiganDTMBAdoption-and-Usage-of-Artificial-IntelligenceGuidelines-and-Responsibilities--P.pdf | DTMB guidelines current 2024–2025 | PARTIAL → FORBID (via DTMB) | DTMB "Adoption and Usage of AI Guidelines and Responsibilities": any external tool storing/processing State of Michigan proprietary data must obtain Authority to Operate (ATO) via the Michigan Security Accreditation Process (MiSAP). Human-in-the-loop required. End users accountable for outputs. | Michigan AI Strategy (NASCIO 2025); MI Senate has separately limited lawmaker access to ChatGPT. | MiSAP/ATO is the operative gate — not a blanket ban, but a procurement chokepoint. |
| 6 | Minnesota (MnDOT) | YES — MnDOT-specific GenAI Standard IT-003. | https://www.dot.state.mn.us/policy/it-data/it-003.html | Effective Jul 14, 2025 | FORBID | DOT-specific. "Data that is private, confidential, protected, or otherwise not public must not be entered into any publicly available GenAI tool." Only Microsoft Copilot Chat (green-shield) approved for sensitive data. Third parties working on behalf of MnDOT must work with MnDOT staff to ensure tools are pre-approved. Discharge + criminal liability under Minn. Stat. § 13.09 for violations. | MN IT Services (MNIT) Public AI Services Security Standard; "AI Unleashed" governance program. | Strongest DOT-direct policy in the corpus. Cleanest contractor language. |
| 7 | Missouri (MoDOT) | YES — MoDOT-specific Employee Conduct chapter prohibition. | https://www.modot.org/media/36548 (MoDOT Employee Conduct policy) | Current 2024–2025 (cross-referenced from MoDOT Policy Manual) | FORBID | MoDOT-specific. Per agency guidance circulated to staff: prohibits use of "unapproved, open AI systems (such as ChatGPT, Bing Chat, and other publicly available AI systems) for work-related purposes" because open systems capture inputs and use them to train models, which is "equivalent to publishing information onto a public website and violates MoDOT Policy." Employees prohibited from disclosing confidential MoDOT or partner data into any AI tool. | HB 1462 "AI Non-Sentience and Responsibility Act" — places legal responsibility on humans, eff. Aug 28, 2025. | Rare among the 12: an explicit named-tool prohibition (ChatGPT, Bing Chat) at the DOT level. |
| 8 | Nebraska (NDOT) | No standalone NDOT policy located. Bound by NITC Policy 8-609. | https://nitc.nebraska.gov/docs/8-609.pdf | NITC 8-609 (current 2024–2025) | FORBID (data) / ENCOURAGE (governed use) | Nebraska Information Technology Commission Policy 8-609: AI systems owned/used/managed by the state must be coordinated through the Office of the CIO Security Risk Mitigation and Compliance team; agencies must perform privacy impact assessments and security reviews before AI use. Definition explicitly captures ChatGPT, DALL-E, Bing/Gemini, Copilot, Adobe AI. | LB 642 (AI Consumer Protection Act for high-risk systems); LB 939 (Saving Human Connection Act); LB 1185 (Conversational AI Safety Act). | DOT-specific AI policy not published; NITC governs. |
| 9 | North Dakota (NDDOT) | No standalone NDDOT policy located. Bound by NDIT AI Guidelines. | https://www.ndit.nd.gov/artificial-intelligence-guidelines | Current 2024–2025 | PARTIAL | NDIT guidelines: state-issued email NOT recommended for creating accounts on public AI services like ChatGPT (permitted with unique password). Personal accounts recommended for exploratory use. Approved vendor or internal AI/ML services require periodic QA checks; users must verify accuracy and exclude moderate-/high-risk data per NDIT Data Classification Policy. References NIST SP 1270 and NIST AI 100-1 RMF. | None DOT-specific. | Softest posture in the corpus — guideline, not prohibition. No standalone DOT directive. |
| 10 | Ohio (ODOT) | No standalone ODOT policy located. Bound by DAS IT-17. | https://digitalgovernmenthub.org/examples/it-17-use-of-artificial-intelligence-in-state-of-ohio-solutions/ ; FAQ: https://dam.assets.ohio.gov/image/upload/das.ohio.gov/technology-strategy/policy/Use_of_AI_FAQs.pdf | DAS IT-17 passed late 2023 | FORBID (data) / ENCOURAGE (use) | Department of Administrative Services Policy IT-17 "Use of Artificial Intelligence in State of Ohio Solutions": only public-record data may be entered by state employees, contractors, or temporary personnel into generative AI tools. AI must be fair, accountable, secure, explainable, transparent. Multi-agency AI Council established. | Gov. Husted policy directive establishing AI Council; Ohio HB 96 (K-12 AI policies due Jul 1, 2026). | Contractor language explicitly includes "contractors or temporary personnel" — relevant for design consultants. |
| 11 | South Dakota (SDDOT) | No standalone SDDOT policy located. Bound by BIT GenAI guidance. | https://www.sd.gov/bit?id=bit_standards_ai_guidance | BIT guidance current 2024 | PARTIAL | Bureau of Information & Telecommunications guidance: AI-generated content treated as a "starting point, not the finished product." Mandatory proofing, editing, fact-checking. Recognizes AI bias, privacy, cybersecurity risks. Tone is best-practice/guideline rather than prohibition. | None DOT-specific. SDDOT is bound by the broader BIT framework. | Softer posture; no contractor language at the DOT level. |
| 12 | Wisconsin (WisDOT) | NO formal DOT AI use policy located. WisDOT instead funded a research program. | Research report: https://wisconsindot.gov/documents2/research/0092-24-14-final-report.pdf | Research report 2024 | SILENT (DOT) / PARTIAL (state) | WisDOT has not published a public-facing GenAI use policy. Department of Workforce Development AI Task Force published the statewide Advisory Action Plan (Jul 2024). | Gov. Evers Executive Order #211 (Aug 23, 2023) creating Workforce & AI Task Force; 2023 Wisconsin Act 123 (synthetic media in political comms, Mar 2024). | Research-leaning posture — six AI domains studied (asset mgmt, safety, ops, digital twin, AVs, GenAI). Implementation roadmap, not a use policy. |

---

## Verbatim excerpts

> Quotes are pulled from the source documents and supporting reporting. Where the source PDF was not machine-readable in this pass, the quote is drawn from a credible secondary source (StateScoop, GovTech, NASCIO) and so noted.

### Minnesota — MnDOT GenAI Standard IT-003 (Jul 14, 2025) — primary source

> "Data that is private, confidential, protected, or otherwise not public must not be entered into any publicly available GenAI tool built on or continuing to train a Large Language Model."

> "All GenAI output used for decision making must be verified to ensure accuracy, relevance, and factuality and to mitigate risks such as AI hallucinations, bias, discrimination, misinformation, and negative impacts to people."

> "Employees who violate this standard or the Minnesota Government Data Practices Act are subject to discipline, up to and including discharge."

Contractor clause: "Third parties working on behalf of MnDOT must work with MnDOT staff to ensure that any tools they use are approved by MnDOT before submitting private, confidential, protected, or otherwise not public data."

### Missouri — MoDOT Employee Conduct guidance (current) — DOT-direct

> "MoDOT prohibits the use of unapproved, open AI systems (such as ChatGPT, Bing Chat, and other publicly available AI systems) for work-related purposes."

> "Open AI systems capture data entered into them and use that data to train their systems to respond to all users. This is equivalent to publishing information onto a public website and violates MoDOT Policy."

> "Employees inputting data and information into an AI tool are prohibited from disclosing confidential data or information belonging to MoDOT or MoDOT's partners."

### Iowa — State of Iowa Generative AI Policy PY-AI (Mar 31, 2025) — statewide; binds Iowa DOT

> "The use of freely available AI tools by state entities is expressly prohibited without prior written approval from the Department of Management."

> "Prior to finalizing any output generated by AI technologies, workforce members must subject such output to thorough human evaluation and iteration that focuses on checking if the AI-generated content is accurate, relevant, and suitable."

> "All Support Entity workforce members (employees and contractors) and any contracted third-party performing work on behalf of the Agency must comply with this Policy."

### Kansas — Statewide P8200.00 (Jul–Aug 2023) — binds KDOT

> "Restricted-use information cannot be provided when interacting with generative AI." (Kansas treats anything entered into tools like ChatGPT as part of the public record.)

> "Responses generated by an AI must be reviewed by knowledgeable human operators for accuracy, appropriateness, privacy and security before being acted upon or disseminated."

> Contractors "must disclose any use of generative AI or integrations with such platforms in their contracts" and are "prohibited from using any confidential or restricted data in queries with generative AI tools, as well as in the building up or training of generative AI programs." (Source: StateScoop summary of P8200.00.)

### Ohio — DAS IT-17 (late 2023) — binds ODOT

> "Only data that is public record should be entered by state employees, contractors or temporary personnel into generative AI tools."

> Agency use cases must "align with core AI principles to be fair, accountable, secure and safe, explainable and transparent." (Source: Center for Community Solutions summary of IT-17.)

### Indiana — State Agency AI Systems Policy (2024) — binds INDOT

> "The use of any AI system(s) not approved pursuant to the AI policy is expressly prohibited."

> Carve-out: the policy "applies to a majority of AI initiatives, with the exception of employees using web-based generative AI applications such as ChatGPT as needed." (Source: GovTech summary.)

> AI Readiness Questionnaire is mandatory; the assessment is "based on the National Institute of Standards and Technology's Artificial Intelligence Risk Management Framework and includes 72 subcategories."

### Michigan — DTMB AI Guidelines (current) — binds MDOT

> "The use of generative-AI tools, such as ChatGPT, Microsoft CoPilot, Gemini, and Bedrock, are already governed by existing State of Michigan (SOM) policies, standards, and procedures."

> "Any external tool used for storing, analyzing, or processing SOM proprietary data must receive an Authority to Operate (ATO) via the Michigan Security Accreditation Process (MiSAP)."

### Nebraska — NITC Policy 8-609 (current) — binds NDOT

Nebraska's policy defines AI broadly to capture "standalone systems like OpenAI's ChatGPT and DALL-E, integrated features within search engines like Microsoft Bing and Google Gemini, and embedded tools like Adobe AI Assistant and Microsoft Copilot." Agencies "utilizing AI must consult with the Office of the CIO's Security Risk Mitigation and Compliance team regarding system development and operations, and must conduct privacy impact assessments and security reviews."

### North Dakota — NDIT AI Guidelines (current) — binds NDDOT

> "Use of state-issued email addresses for creating accounts on public AI resources like ChatGPT is not recommended, though it is permitted if you use a unique password."

> Users should "verify for accuracy prior to use and exclude moderate-risk and high-risk data following the Data Classification Policy."

### South Dakota — BIT Generative AI Guidance (current) — binds SDDOT

Guidance frames AI-generated content as "a starting point, not the finished product," requiring proofing, editing, fact-checking, and recognizing risks of AI bias, privacy, and cybersecurity. Tone: best-practice guidance rather than prohibition.

### Illinois — DoIT AI Policy v2 (Apr 1, 2025) — binds IDOT

> "The Policy applies to Agencies in their roles as AI Consumers or AI Creators, addressing any AI Systems that may be developed, deployed, or used by an Agency."

> "Within 30 days of the effective date of this Policy, Utilizing Agencies must designate an employee to perform the functions required by the AI Policy."

### Wisconsin — Could not locate a published WisDOT AI use policy.

WisDOT has commissioned and published a research report ("Artificial Intelligence in Transportation Final Report," WisDOT 0092-24-14, 2024) covering asset management, safety, operations, digital twin, AVs, and GenAI. That report includes a phased implementation roadmap but is research output, not a binding employee/contractor use policy. Statewide framework: Gov. Tony Evers' Executive Order #211 (Aug 23, 2023) created the Governor's Task Force on Workforce and Artificial Intelligence; the Task Force published its Advisory Action Plan in July 2024.

---

## Quick read (synthesis, ~150 words)

Of the 12 Midwestern DOTs surveyed, only **2 publish a DOT-direct AI use policy**: **MnDOT** (IT-003, Jul 2025) and **MoDOT** (Employee Conduct guidance — explicit ChatGPT/Bing Chat prohibition). The remaining 10 are governed by statewide CIO/IT or executive policy. By bucket: **FORBID** dominates — 8 states explicitly prohibit entering non-public agency data into commercial GenAI tools (IL, IN, IA, KS, MI, MN, MO, OH); **2 are PARTIAL** (ND, SD) — guidance-flavored, no hard ban; **1 is FORBID/ENCOURAGE hybrid** (NE) — broad authorization with mandatory privacy/security review; **1 is SILENT** at the DOT level (WI — research roadmap exists, no use policy). Surprising findings: (1) MoDOT names tools by brand — rare among DOTs; (2) Kansas, Ohio, and Iowa explicitly bind contractors in addition to employees, which matters for design and CE&I consultants on federal-aid contracts. Gaps to flag: no Midwestern DOT publicly addresses AI use in design submittals, RFIs, or constructability reviews — that procurement guidance is a hole worth tracking.

---

## Sources

- [MnDOT GenAI Standard IT-003](https://www.dot.state.mn.us/policy/it-data/it-003.html)
- [MoDOT Employee Conduct policy chapter](https://www.modot.org/media/36548)
- [State of Iowa Generative AI Policy PY-AI (PDF)](https://dom.iowa.gov/media/785/download?inline=)
- [Iowa Agencies Sandbox — GenAI policy hub](https://dxsandbox.iowa.gov/state-iowa-generative-artificial-intelligence-ai-policy)
- [Kansas P8200.00 Generative AI Policy (PDF)](https://www.governor.ks.gov/wp-content/uploads/2023/08/P8200.00-Generative-Artificial-Intelligence-Signed.pdf)
- [StateScoop — Kansas generative AI policy](https://statescoop.com/kansas-generative-artificial-intelligence-policy/)
- [Michigan DTMB AI Guidelines (PDF)](https://www.michigan.gov/dtmb/-/media/Project/Websites/dtmb/Law-and-Policies/Governance/State-of-MichiganDTMBAdoption-and-Usage-of-Artificial-IntelligenceGuidelines-and-Responsibilities--P.pdf)
- [Nebraska NITC Policy 8-609 (PDF)](https://nitc.nebraska.gov/docs/8-609.pdf)
- [North Dakota IT Artificial Intelligence Guidelines](https://www.ndit.nd.gov/artificial-intelligence-guidelines)
- [Ohio IT-17 entry — Digital Government Hub](https://digitalgovernmenthub.org/examples/it-17-use-of-artificial-intelligence-in-state-of-ohio-solutions/)
- [Ohio DAS — Use of AI FAQs (PDF)](https://dam.assets.ohio.gov/image/upload/das.ohio.gov/technology-strategy/policy/Use_of_AI_FAQs.pdf)
- [South Dakota BIT — AI Standards & Guidance](https://www.sd.gov/bit?id=bit_standards_ai_guidance)
- [Indiana State Agency AI Systems Policy hub](https://www.in.gov/mph/AI/)
- [Illinois DoIT — Acceptable & Responsible Use of AI (PDF)](https://doit.illinois.gov/content/dam/soi/en/web/doit/documents/support/policies/2021/20250401-DoIT-AI%20Policy-v2-%20A11Y.pdf)
- [Illinois Generative AI & NLP Task Force 2024 Report (PDF)](https://doit.illinois.gov/content/dam/soi/en/web/doit/meetings/ai-taskforce/reports/2024-gen-ai-task-force-report.pdf)
- [Wisconsin Gov. Evers — Executive Order #211 announcement](https://content.govdelivery.com/accounts/WIGOV/bulletins/36b5a34)
- [Wisconsin Workforce & AI Task Force Advisory Action Plan (PDF)](https://dwd.wisconsin.gov/ai-taskforce/pdf/ai-advisory-action-plan.pdf)
- [WisDOT Research 0092-24-14 — AI in Transportation Final Report (PDF)](https://wisconsindot.gov/documents2/research/0092-24-14-final-report.pdf)
- [GovTech — Indiana's New AI Policy Calls for Pre-Deployment Assessments](https://www.govtech.com/biz/data/indianas-new-ai-policy-calls-for-pre-deployment-assessments)
- [GovTech — Ohio Creates Policy and Council to Govern Statewide AI Use](https://www.govtech.com/artificial-intelligence/ohio-creates-policy-and-council-to-govern-statewide-ai-use)
- [Center for Community Solutions — Ohio DAS AI policy summary](https://www.communitysolutions.com/resources/ohio-department-of-administrative-services-releases-policy-governing-use-of-ai)

---

*Compiled April 2026 for Infrastructure Catalyst newsletter. Not legal advice — verify each policy with the issuing agency before relying on it for compliance.*
