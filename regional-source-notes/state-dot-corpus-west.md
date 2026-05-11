# State DOT AI Policy Corpus — 13 Western States

Compiled for Infrastructure Catalyst, April 2026. Audience: working civil engineers, PEs, and PMs on federal-aid and state-funded transportation projects. Researched via web search and primary-source review of state CIO / Governor / DOT publications.

Scope note: very few state DOTs publish standalone AI policies. The dominant pattern is a **statewide CIO or Governor-level policy** that binds the DOT, plus **agency-level pilots** (Caltrans Copilot rollout, ADOT translation pilots, UDOT tire-anomaly AI, ITD DMV AI). The "Bucket" column reflects the operative posture **as it applies to the DOT** — i.e., FORBID = the DOT is bound by an explicit prohibition on cloud AI uploads of agency data; ENCOURAGE = the DOT is bound by (or has) an explicit permission with guardrails; SILENT = no AI-specific policy located.

---

## Master Table

| # | State / DOT | Has AI policy? | Policy URL | Date issued / updated | Bucket | General IT / acceptable-use posture | Statewide AI EO / law reference | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | **Alaska — AKDOT&PF** | Partial (statewide AOs, no DOT-specific) | [Admin Order 359](https://gov.alaska.gov/admin-orders/administrative-order-no-359/), [Admin Order 360](https://gov.alaska.gov/admin-orders/administrative-order-no-360/) | AO 359 / AO 360 (2025) | **ENCOURAGE** | Statewide acceptable-use governed by Office of Information Technology (OIT); no published AI-specific AUP located | Dunleavy AO 359 (efficiency, AI-assisted spend review) and AO 360 (permitting digitization via AI) | No standalone AI strategic plan; no named CDAO; ITIF testified before legislature on SB 2 (deepfakes) Apr 2025; orders are pro-AI directives, not guardrail policies |
| 2 | **Arizona — ADOT** | Yes (statewide P2000 binds ADOT) | [P2000 Generative AI Policy](https://aset.az.gov/sites/default/files/2024-03/P2000%20-%20Generative%20AI%20Policy.pdf) | Mar 2024 (ASET); refreshed in 2024-25 implementation | **ENCOURAGE** (with guardrails) | Statewide P2000 + ASET acceptable-use baseline; mandates training, AI tool inventory, risk assessment | ASET Statewide Policy P2000 (Generative AI); state did not pass a separate AI EO | ADOT ran Spring 2025 pilots: multilingual translation, plain-language rewrites, doc summarization; ADOT also using Azure AI Vision for asset inspection |
| 3 | **California — Caltrans** | Yes (DOT-level CDAO authority) | [EO N-12-23](https://www.gov.ca.gov/wp-content/uploads/2023/09/AI-EO-No.12-_-GGN-Signed.pdf), [EO N-5-26](https://www.gov.ca.gov/wp-content/uploads/2026/03/3.30-FINAL-Trusted-AI-Procurement-EO-N-5-26.pdf), [State GenAI Guidelines](https://www.govops.ca.gov/wp-content/uploads/sites/11/2024/03/3.a-GenAI-Guidelines.pdf) | EO N-12-23: Sep 6, 2023; State GenAI Guidelines: Mar 2024; EO N-5-26: Mar 30, 2026 | **ENCOURAGE** (most mature) | CalSTA + Caltrans CDAO sets ethical AI policy; statewide GenAI procurement guidelines (SAM/SIMM) | EO N-12-23 (2023), EO N-5-26 (2026), SB 896 GenAI Accountability Act, AB 2013 training-data transparency | **Named CDAO: Vidhu Shekhar** (formalized Feb 2025 via CalSTA memo). 18,000 of 23,000 Caltrans employees got Microsoft Copilot access (April 2025). First DOT in nation to award GenAI vendor contracts (2024) |
| 4 | **Colorado — CDOT** | No DOT-specific; broad state law in flight | [SB24-205](https://leg.colorado.gov/bills/sb24-205) | Signed May 17, 2024; effective delayed to Jun 30, 2026 (SB 25B-004) | **SILENT** at DOT level | CDOT has Chief Data Office; no published AI AUP located on codot.gov | Colorado AI Act (SB24-205) — consumer protection / high-risk AI deployers, attorney general enforcement | CDOT focus is on connected/autonomous vehicles, traffic ops dashboards, geospatial. No CDAO. SB 24-205 will reach CDOT only if it deploys "high-risk" AI making consequential decisions |
| 5 | **Hawaii — HDOT** | Partial (statewide framework via ETS) | [HB2152 (2024)](https://www.capitol.hawaii.gov/sessions/session2024/bills/HB2152_.HTM), [ETS Policies](https://ets.hawaii.gov/policies/) | HB2152 enacted 2024; ETS guidelines under development | **SILENT → emerging ENCOURAGE** | Statewide ETS policies/standards apply; AUP via ETS; no HDOT-specific AI AUP located | HB2152 directs ETS + state CIO + cybersecurity coordinator to risk-assess GenAI; no Governor Green AI EO located | Hawaii is in build-the-framework phase. Risk assessment + workforce-impact reports were due to legislature 20 days before 2025 session |
| 6 | **Idaho — ITD** | No DOT-specific; ITD inherits binding statewide AI-PSG (P.ITS-01 / S.ITS-01 / G.ITS-01) | [AI Governance Policy/Standard/Guideline (Aug 2025 PDF)](https://its.idaho.gov/wp-content/uploads/2024/09/AI-PSG_FINALAug2025.pdf), [Idaho's AI Advantage Framework](https://its.idaho.gov/wp-content/uploads/2025/08/Idaho-AI-Advantage-Framework.pdf), [ITS AI Help Center](https://its.idaho.gov/ai/) | v1.0 — August 2025 | **ENCOURAGE (binds contractors)** | Idaho Office of Information Technology Services (ITS) published a combined Policy + Standard + Guideline binding all state employees, contractors, sub-contractors, agents, and business partners. Mandatory human review of GenAI outputs; AI-use disclosure on public-facing content; 4-tier data classification (Critical data prohibited from GenAI without AI Executive Committee approval); NIST AI RMF aligned (GOVERN, MAP, MEASURE, MANAGE) | No AI EO at governor level; ITS Executive Committee governs | ITD inherits AI-PSG; ITD DMV named one of four AI leaders by ITS; ITD presented "GenAI Challenge to Highway QA Integrity" at TRB. **Correction (2026-05-11):** Issue 11 originally classified Idaho as SILENT (draft pending). The AI-PSG was published nine months before Issue 11 shipped; we missed it because the document lives on its.idaho.gov rather than itd.idaho.gov, the PDF URL path is `/wp-content/uploads/2024/09/...` despite the Aug 2025 date, and the PDF binary required `pdftotext -layout` to extract cleanly. Brought to attention by Mike Copeland. |
| 7 | **Montana — MDT** | No DOT-specific; workforce-focused EO | [EO 5-2025 (406 JOBS)](https://news.mt.gov/Governors-Office/Governor_Gianforte_Announces_New_Initiative_to_Bolster_Workforce_Development_in_Skilled_Trades_and_AI) | Aug 11, 2025 | **SILENT** at DOT level | SITSD (CIO Kevin Gilbertson) sets statewide IT standards | EO 5-2025 (workforce/AI training, not guardrails); 2025 session passed Right to Compute Act (SB 212), HB 556 (insurer AI), HB 514 (NIL) | EO 5-2025 directs Dept of Labor to integrate AI tools and train workforce. Montana's posture is permissive ("right to compute"). MDT itself has no public AI policy |
| 8 | **Nevada — NDOT** | Yes (statewide CIO policy binds NDOT) | [Nevada AI Policy (CIO-signed)](https://www.it.nv.gov/siteassets/itnew.nv.gov/content/governance/Policy_on_the_Responsible_and_Ethical_Use_of_Artificial_Intelligence_in_Nevada_-_CIO_Signed.pdf) | Dec 2024 | **ENCOURAGE** (with explicit floor) | Statewide policy on responsible/ethical AI, signed by CIO Tim Galluzi under Gov. Lombardo | Lombardo policy (Dec 2024); 2025 session: AB 406 (mental health AI restriction), SB 213/263 (AI synthetic intimate images) | Policy explicitly **prohibits agency-level AI policies from being more lenient than the statewide one** — that's load-bearing for NDOT |
| 9 | **New Mexico — NMDOT** | No DOT-specific; statewide transparency law | [HB0184 (2024)](https://www.nmlegis.gov/Sessions/24%20Regular/bills/house/HB0184.HTML) | 2024 session; first inventories due Oct 1, 2024 | **SILENT** at DOT level | Statewide General Services Department implementing the AI Transparency Act ($500K appropriation) | Government Use of AI Transparency Act (HB0184) — agencies must inventory AI systems, identify whether they make/inform "consequential decisions" | NMDOT must report its AI inventory to the state. No AI EO. AG Torrez has proposed deepfake legislation separately |
| 10 | **Oregon — ODOT** | Partial (statewide interim guidelines) | [Interim AI Guidelines V1.5](https://www.oregon.gov/eis/cyber-security-services/Documents/Interim_AI_Guidelines_V1.5%201.pdf), [State Gov AI Council Action Plan](https://www.oregon.gov/eis/Documents/SG%20AI%20Final%20Recommended%20Action%20Plan%2020250211.pdf) | EIS Interim Guidelines V1.5 (2024); Action Plan Feb 11, 2025 | **ENCOURAGE** (with guardrails) | Enterprise Information Services (EIS) AUP + interim AI guidelines apply to ODOT | No Governor EO located; State Government AI Advisory Council recommendations Feb 2025 | ODOT publishes a public "AI Research Tools Guide" listing approved GenAI tools. Oregon DOJ has its own AI guidance (Dec 24, 2024) |
| 11 | **Utah — UDOT** | Partial (statewide UAIPA + DTS guidance) | [Utah AI Policy Act (SB149/2024)](https://le.utah.gov/~2024/bills/static/SB0149.html), [DTS AI Initiatives](https://dts.utah.gov/what-we-are-doing/our-initiatives/artificial-intelligence/) | UAIPA effective May 1, 2024; expanded 2025 session | **ENCOURAGE** (consumer-facing transparency required) | Division of Technology Services (DTS) sets statewide acceptable-use; UAIPA imposes transparency duty on **public-facing** GenAI | UAIPA (SB 149) — requires disclosure when consumers interact with GenAI; created Office of AI Policy in Dept of Commerce | UDOT publicly highlighted its in-road tire-anomaly AI as "innovation of the year" (2025). UAIPA disclosure obligations would apply to any UDOT public-facing chatbot |
| 12 | **Washington — WSDOT** | Yes (statewide IT policy binds WSDOT) | [WaTech Interim Guidelines](https://watech.wa.gov/policies/interim-guidelines-purposeful-and-responsible-use-generative-artificial-intelligence-ai-washington), [EO 24-01](https://governor.wa.gov/sites/default/files/exe_order/24-01%20-%20Artificial%20Intelligence%20(tmp).pdf) | EO 24-01: Jan 30, 2024; Interim Guidelines adopted as statewide IT policy Dec 11, 2025 | **ENCOURAGE** (with guardrails) | WaTech sets enterprise IT/AUP for executive-branch agencies including WSDOT | Inslee EO 24-01 (Jan 30, 2024). Adopted as statewide policy Dec 11, 2025 | WaTech also published "Equity Analysis Guidelines for Deployment of GenAI" (Dec 2024). WSDOT has no separate AI AUP located |
| 13 | **Wyoming — WYDOT** | No (district-led approach) | [WY A&I AI page](https://ai.wyo.gov/) | n/a | **SILENT** | Administration & Information / state CIO governs IT acceptable-use; no AI-specific AUP located | No AI EO; legislature reviewed SF 51 (synthetic media) 2024 session; WDE issued K-12 guidance Jul 2024 | Wyoming's posture is "leave it to the districts/agencies." Gov. Gordon spoke at NGA 2024 Winter Meeting on AI. WYDOT has no public AI policy |

---

## Verbatim Excerpts

The state-DOT AI policy space is thin on direct DOT-issued language. Most operative text is at the **statewide CIO or Governor** level. PDFs from CA, NV, AZ, and WA were not parseable via standard fetch (binary-encoded), so where we could not extract verbatim text directly, we have flagged it. Below are the cleanest excerpts available from secondary primary-source reporting and from the readable HTML pages.

### Arizona — Statewide Policy P2000 (Generative AI Policy)
Source: ASET; reported language summarized by analyst secondary source ([babl.ai analysis](https://babl.ai/arizona-sets-guardrails-for-government-use-of-generative-ai/)). Operative restrictions paraphrased from the policy:

> Confidential data shall not be entered into publicly accessible AI systems without authorization. AI shall not be used for sensitive communications. All AI-generated works must adhere to copyright standards, and agencies must ensure vendors provide proper licensing for AI model training data. Agencies must disclose AI tool usage in public-facing content through annotations.

**Posture:** Permissive but with explicit data-handling fence. Annual training mandatory.

### California — Executive Order N-12-23 (Newsom, Sep 6, 2023)
Per [genai.ca.gov](https://www.genai.ca.gov/ca-action/executive-order/) and [govops.ca.gov](https://www.govops.ca.gov/generative-ai-genai-executive-order/):

> "Deployment of GenAI technologies must be evaluated through a risk assessment based on the National Institute of Standards and Technology's AI Risk Management Framework, as well as relevant portions of the [State Administrative Manual] and State Information Management Manual."

### California — Executive Order N-5-26 (Newsom, Mar 30, 2026)
Per [Governor's Office press release](https://www.gov.ca.gov/2026/03/30/as-trump-rolls-back-protections-governor-newsom-signs-first-of-its-kind-executive-order-to-strengthen-ai-protections-and-responsible-use/):

> Directs the California Department of Technology and Department of General Services to "implement new trust and safety obligations on artificial intelligence (AI) companies seeking to contract with California agencies," directs the state CISO to review federal supply-chain risk designations and issue procurement guidance, and directs CDT to provide government employees access to "generative AI tools that have privacy and cybersecurity safeguards."

### California — Caltrans CDAO Position Description (Feb 2025)
Per [CalHR CEA Action Proposal](https://www.calhr.ca.gov/wp-content/uploads/sites/361/2025/09/caltrans-chief-data-and-artificial-intelligence-officer-directors-office.pdf):

> The CDAO has "broad, enterprise-wide policy-making authority over Caltrans' data governance, artificial intelligence (AI), and generative AI (GenAI) programs… The CDAO is the authority for policy on ethical AI practices, data governance, and compliance with privacy laws, state technology mandates, and industry standards. This includes creating and enforcing policies to prevent bias, promote transparency, and protect individual rights in all AI-enabled systems."

### Washington — Executive Order 24-01 (Inslee, Jan 30, 2024)
Per [WaTech bulletin](https://watech.wa.gov/watech/news/2024/gov-inslee-signs-executive-order-prepare-state-generative-ai) and [governor.wa.gov medium](https://medium.com/wagovernor/generative-ai-inslee-executive-order-prepares-washington-for-opportunities-challenges-54c2eea11096):

> WaTech is directed to develop "initial guidelines for how the government may procure, use and monitor the use of generative AI." WaTech and the Office of Equity must work with community members to "develop guidelines for agencies to analyze how generative AI might affect vulnerable communities." OFM (State Human Resources Division), with WaTech, "shall assess the impact of generative AI on the state workforce."

(Adopted as statewide IT policy Dec 11, 2025.)

### Washington — WaTech Interim Guidelines
Per [WaTech policy page](https://watech.wa.gov/policies/interim-guidelines-purposeful-and-responsible-use-generative-artificial-intelligence-ai-washington):

> "Agencies must incorporate Washington state's AI Principles into agency implementation of AI-enabled technology and Generative AI and consider guidelines for public sector procurement, deployment and monitoring of Generative AI technology."

### Nevada — Policy on the Responsible and Ethical Use of AI (CIO Galluzi, Gov. Lombardo, Dec 2024)
Per [it.nv.gov](https://www.it.nv.gov/siteassets/itnew.nv.gov/content/governance/Policy_on_the_Responsible_and_Ethical_Use_of_Artificial_Intelligence_in_Nevada_-_CIO_Signed.pdf) (PDF not parseable; per state press summary):

> The policy "prohibits agency-level AI policies from being more lenient than the statewide one, as well as the use of AI to create discriminatory content or use personal data without anonymization."

### Oregon — EIS Interim Guidelines for Responsible Use of Generative AI
Per [oregon.gov EIS](https://www.oregon.gov/eis/cyber-security-services/Documents/Interim_AI_Guidelines_V1.5%201.pdf) (PDF not parseable; per Securiti / state summary):

> "Users must not use GenAI tools in any way that violates laws, regulations, organizational policies, or contractual obligations. AI-generated content used in official state capacity should be clearly labeled as such, and details of its review and editing process should be provided, allowing for transparent authorship and responsible content evaluation."

### New Mexico — Government Use of AI Transparency Act (HB0184, 2024)
Per [nmlegis.gov](https://www.nmlegis.gov/Sessions/24%20Regular/bills/house/HB0184.HTML):

> Agencies must submit inventories of AI systems including "the system name and vendor, a description of capabilities and uses, whether the system was used to make or inform consequential decisions, and whether the system was assessed using local data." First inventories were due October 1, 2024; aggregate report to Governor and Legislature January 1, 2025.

### Alaska — Administrative Orders 359 & 360 (Dunleavy, 2025)
Per [gov.alaska.gov](https://gov.alaska.gov/admin-orders/administrative-order-no-359/):

> AO 359 directs state agencies to "utilize technology and artificial intelligence (AI) to review large datasets in order to determine how State of Alaska funds are actually being spent." AO 360 directs agencies to "leverage technology, such as artificial intelligence, to support digitization, automation, and public access to permitting information."

(These are pro-deployment directives, not guardrail policies.)

### Colorado — SB24-205 Colorado AI Act
Per [leg.colorado.gov](https://leg.colorado.gov/bills/sb24-205):

> Imposes requirements on developers and deployers of "high-risk artificial intelligence systems" that make "consequential decisions" in employment, education, financial services, health care, housing, insurance, and legal services. Effective date delayed by SB 25B-004 to **June 30, 2026**. AG has exclusive enforcement authority.

(CDOT is bound only if it deploys a "high-risk" system per the statutory definition — operationally narrow.)

### Utah — Artificial Intelligence Policy Act (SB149, 2024)
Per [le.utah.gov](https://le.utah.gov/~2024/bills/static/SB0149.html):

> First-in-nation transparency requirement: any organization using GenAI in consumer-facing interactions must disclose that the consumer is interacting with AI. Created the Office of AI Policy in the Department of Commerce. Effective May 1, 2024.

### Hawaii — HB2152 (2024)
Per [legiscan.com](https://legiscan.com/HI/text/HB2152/id/2896940):

> Directs the Office of Enterprise Technology Services to consult with each state agency, department, and branch of government and to "establish criteria for evaluating the impact of generative AI on the state workforce, and based on the consultations, create guidelines to help each agency, department, and branch best support its employees in using generative AI effectively." Guidelines must build on the White House Blueprint for an AI Bill of Rights and the NIST AI RMF.

### Montana — EO 5-2025 (Gianforte, Aug 11, 2025)
Per [Daily Montanan reporting](https://dailymontanan.com/2025/08/11/gianforte-announces-executive-order-bolstering-workforce-development-in-trades-and-ai/):

> Creates the **406 JOBS Initiative**: "directs the Department of Labor to promote and expand opportunities that equip Montanans with AI skills and integrate AI tools to support job seekers." Workforce-focused, not a guardrail policy. SB 212 ("Right to Compute Act") establishes a state-protected right to use compute resources, including AI.

---

## Quick Read — 150-word synthesis

Of the 13 western state DOTs, **zero** publish their own standalone AI acceptable-use policy. The bucket distribution falls on the **statewide policies that bind each DOT**:

- **ENCOURAGE-with-guardrails (8):** Arizona, California, Idaho (corrected 2026-05-11 — see Idaho row note), Nevada, Oregon, Utah, Washington — plus Alaska, where two 2025 administrative orders are explicitly pro-AI but lack data-handling fences.
- **SILENT at DOT level (5):** Colorado, Hawaii (framework still being built), Montana, New Mexico (transparency-only), Wyoming.
- **FORBID (0):** No western state DOT operates under an explicit prohibition on cloud AI uploads. The strictest language is Arizona's P2000 ("confidential data shall not be entered into publicly accessible AI systems without authorization"), Nevada's policy floor ("agency-level AI policies cannot be more lenient than statewide"), and Idaho's tiered restriction (Critical data prohibited from GenAI without AI Executive Committee authorization).

**Most surprising finding:** Caltrans is the **clear outlier on the upside** — it has a named CDAO (Vidhu Shekhar), 18,000 employees with Microsoft Copilot access, and the first GenAI vendor contracts in any state DOT. The next-most-mature Western DOT is roughly two years behind it.

**Gaps to flag for follow-up:** Direct full text of WA EO 24-01 §3-7, NV CIO policy §IV (data-classification table), and AZ P2000 §5 (procurement) — PDFs are binary-encoded and need manual download for verbatim quoting. No federal-aid-specific procurement language located at any DOT; FHWA's posture appears to flow through generic CFR 200 procurement rules rather than AI-specific guidance.

---

## Sources

- [California EO N-12-23 (Sep 6, 2023)](https://www.gov.ca.gov/wp-content/uploads/2023/09/AI-EO-No.12-_-GGN-Signed.pdf)
- [California EO N-5-26 (Mar 30, 2026)](https://www.gov.ca.gov/wp-content/uploads/2026/03/3.30-FINAL-Trusted-AI-Procurement-EO-N-5-26.pdf)
- [California State GenAI Guidelines (Mar 2024)](https://www.govops.ca.gov/wp-content/uploads/sites/11/2024/03/3.a-GenAI-Guidelines.pdf)
- [Caltrans CDAO position (CalHR, Sep 2025)](https://www.calhr.ca.gov/wp-content/uploads/sites/361/2025/09/caltrans-chief-data-and-artificial-intelligence-officer-directors-office.pdf)
- [Caltrans CDAO bio (Vidhu Shekhar)](https://dot.ca.gov/about-caltrans/executive-biographies/chief-data-ai-officer)
- [Washington EO 24-01 (Jan 30, 2024)](https://governor.wa.gov/sites/default/files/exe_order/24-01%20-%20Artificial%20Intelligence%20(tmp).pdf)
- [WaTech Interim Guidelines for GenAI](https://watech.wa.gov/policies/interim-guidelines-purposeful-and-responsible-use-generative-artificial-intelligence-ai-washington)
- [WaTech AI announcement (Inslee)](https://watech.wa.gov/watech/news/2024/gov-inslee-signs-executive-order-prepare-state-generative-ai)
- [Arizona P2000 Generative AI Policy](https://aset.az.gov/sites/default/files/2024-03/P2000%20-%20Generative%20AI%20Policy.pdf)
- [Arizona policy analysis (BABL.ai)](https://babl.ai/arizona-sets-guardrails-for-government-use-of-generative-ai/)
- [Nevada Statewide AI Policy (CIO Galluzi, Dec 2024)](https://www.it.nv.gov/siteassets/itnew.nv.gov/content/governance/Policy_on_the_Responsible_and_Ethical_Use_of_Artificial_Intelligence_in_Nevada_-_CIO_Signed.pdf)
- [Oregon EIS Interim AI Guidelines V1.5](https://www.oregon.gov/eis/cyber-security-services/Documents/Interim_AI_Guidelines_V1.5%201.pdf)
- [Oregon State Government AI Advisory Council Action Plan (Feb 2025)](https://www.oregon.gov/eis/Documents/SG%20AI%20Final%20Recommended%20Action%20Plan%2020250211.pdf)
- [Colorado SB24-205](https://leg.colorado.gov/bills/sb24-205)
- [Utah AI Policy Act SB149 (2024)](https://le.utah.gov/~2024/bills/static/SB0149.html)
- [Utah DTS AI Initiatives](https://dts.utah.gov/what-we-are-doing/our-initiatives/artificial-intelligence/)
- [Hawaii HB2152 (2024)](https://legiscan.com/HI/text/HB2152/id/2896940)
- [Hawaii ETS Policies](https://ets.hawaii.gov/policies/)
- [Idaho ITS — Artificial Intelligence Governance Policy, Standard, and Guideline (P.ITS-01 / S.ITS-01 / G.ITS-01), Aug 2025 PDF](https://its.idaho.gov/wp-content/uploads/2024/09/AI-PSG_FINALAug2025.pdf)
- [Idaho's AI Advantage: A Framework for Responsible Innovation, Aug 2025 PDF](https://its.idaho.gov/wp-content/uploads/2025/08/Idaho-AI-Advantage-Framework.pdf)
- [Idaho ITS AI Help Center](https://its.idaho.gov/ai/)
- [Idaho ITS Policy & Governance index](https://its.idaho.gov/policy-governance/)
- [New Mexico HB0184 (2024)](https://www.nmlegis.gov/Sessions/24%20Regular/bills/house/HB0184.HTML)
- [Alaska Admin Order 359](https://gov.alaska.gov/admin-orders/administrative-order-no-359/)
- [Alaska Admin Order 360](https://gov.alaska.gov/admin-orders/administrative-order-no-360/)
- [Montana EO 5-2025 (406 JOBS)](https://dailymontanan.com/2025/08/11/gianforte-announces-executive-order-bolstering-workforce-development-in-trades-and-ai/)
- [Wyoming A&I AI page](https://ai.wyo.gov/)
- [Caltrans GenAI vendor awards (2024)](https://dot.ca.gov/news-releases/news-release-2024-016)
- [Caltrans Copilot rollout (2025)](https://www.govtech.com/artificial-intelligence/caltrans-officials-early-ai-users-look-to-expand-adoption)
- [ADOT pilot reporting (Microsoft)](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/arizona-department-of-transportation-innovates-with-azure-ai-vision/4405832)
- [UDOT tire-anomaly AI (Deseret News)](https://www.deseret.com/utah/2025/12/17/how-ai-is-helping-udot-catch-previously-undetected-truck-tire-problems/)
