# Transit Authorities — Reading Notes

Installment 3 of the Transportation AI Policy Tracker. Eight major US transit authorities, scored per methodology.md (FORBID / ENCOURAGE / PARTIAL / SILENT) with contractor-binding flags.

**Scoring date:** 2026-09-07
**Researcher:** Hermes Agent (subagent for JosephD130/transportation-ai-policy-tracker)

---

## Summary table

| Agency | Bucket | Contractor-binding | Key source |
|---|---|---|---|
| MTA (New York) | SILENT | No | MTA Board minutes (Feb 2026) |
| WMATA (Washington DC) | ENCOURAGE | Yes | AI Terms Annex (Sept 2025, rev. Mar 2026) |
| LA Metro (Los Angeles) | SILENT | No | Metro Board Report 2024-0437 (July 2024) |
| BART (San Francisco Bay Area) | SILENT | No | BART FY27 Preliminary Budget (Mar 2026) |
| MBTA (Boston) | ENCOURAGE | Yes | MA EOTSS GenAI Policy (Jan 2025) |
| CTA (Chicago) | SILENT | No | CTA FY2026 Budget Book (Nov 2025) |
| SEPTA (Philadelphia) | SILENT | No | ITS International / Hayden AI (Jul 2025) |
| Sound Transit (Seattle) | SILENT | No | Sound Transit Innovation & Technology pages |

**Distribution:** 2 ENCOURAGE, 0 FORBID, 0 PARTIAL, 6 SILENT.
**Contractor-binding:** 2 of 8 (WMATA, MBTA).

---

## MTA (Metropolitan Transportation Authority) — New York

**Bucket:** SILENT
**Contractor-binding:** No

### What was found

The MTA is one of the most active AI-deploying transit agencies in the country, yet it has no standalone AI-specific policy, Acceptable Use Policy, or AI governance framework.

**AI deployments identified:**
- **TrackInspect** — Predictive track maintenance pilot with Google Public Sector. Pixel smartphones on R46 subway cars capture vibration/audio data; AI/ML models on Google Cloud generate predictive insights. Presented at Google Public Sector GenAI Live & Labs event. 92% defect detection rate vs. human inspectors. Uses GenAI for NLP maintenance-history queries. (MTA press release, 2025)
- **OMNY AI Chatbot** — Customer-facing chatbot for OMNY fare system. Board approved $12.9M contract modification (Cubic) in June 2025, including retroactive services from Oct 2022–May 2025.
- **AI Weapons Detection Pilot** — Board Motion 34.1 (April 2024) directed staff to research weapons detection technologies using AI, machine learning, millimeter wave radar. Pilot approved July 2024 ($65.1M LOP for Enhanced Access Control).
- **AI Video Analytics RFI** — RFI 0000532398 for AI-based real-time video analytics on subway/bus cameras: forbidden object detection, unattended items, behavioral pattern analysis. Dec 2024 RFI deadline.
- **AI Track Intrusion Detection** — April 2026 contract notice for AI-supported track intrusion detection system (pre-intrusion behavior detection, erratic movement flagging). Aiming to award contract by end of 2026. (Route Fifty, June 2026)
- **AI Fare Gates** — Testing AI-enabled fare gates at select stations.
- **Project Management AI** — Capital Program Committee Feb 2026 minutes: C&D transitioning to new PMIS that will "integrate emerging artificial intelligence tools to support project oversight and decision-making."

**Governance gap:** No AI-specific Acceptable Use Policy, no AI procurement annex, no employee-facing AI governance document found on mta.info. NYSDOT (parent state DOT) was classified SILENT in Installment 1; NY State Comptroller's April 2025 audit found NYSDOT had no in-house AI policy and was piloting three AI systems with no formal governance.

### Sources searched
- mta.info board minutes (2025-2026)
- mta.info procurement documents (RFIs, RFEIs, contract modifications)
- mta.info press releases
- Route Fifty (June 2026) — track intrusion AI
- Gothamist / The City Reporter (Jan 2026) — AI video analytics
- No AI policy, AI governance, or AI AUP documents found

### Verbatim clause
> "Internally, C&D is transitioning to a new project management information system designed to provide clearer oversight of cost and schedule performance across projects. Although less visible to the public, Mr. Torres-Springer noted that the system will significantly improve management productivity and allow the agency to integrate emerging artificial intelligence tools to support project oversight and decision-making." — MTA Joint Board Minutes, Feb 25, 2026

---

## WMATA (Washington Metropolitan Area Transit Authority) — Washington DC

**Bucket:** ENCOURAGE
**Contractor-binding:** Yes

### What was found

WMATA has the most developed AI governance of any transit authority surveyed, with a published AI Terms Annex incorporated into its Standard IT Terms and Conditions and a Board-level Digital & AI Ecosystem Acceleration priority program.

**AI governance documents:**
- **Artificial Intelligence (AI) Terms — Annex** (Last updated Sept 28, 2025; revised March 17, 2026). Incorporated by reference into all IT contracts. Defines AI Technology broadly (deep learning, ML, neural networks, transformers, LLMs, reinforcement learning, automated decision-making). Key provisions:
  - **Data ownership:** WMATA Data (including AI Input and AI Output) remains sole property of WMATA.
  - **Training prohibition:** "Contractor will not attempt to use WMATA Data to train, enhance, test, validate, update, develop, fine-tune, adapt or improve any artificial intelligence model or other AI Technology including (but not limited to) generative or agentic artificial intelligence models and large language models."
  - **AI Program requirement:** Contractor must implement and maintain a documented governance and risk management program for AI Technology, identifying, testing for, monitoring, and mitigating risks (ethics, bias, reliability, security, safety).
  - **Compliance:** Contractor must comply with all applicable AI legislation, conduct regular audits, and notify WMATA of material risks.
  - **Indemnification:** Contractor indemnifies WMATA for claims arising from failure to meet Annex obligations.
  - **Survival:** Obligations survive contract termination.
- **Standard IT Terms and Conditions** (Dec 17, 2025) — Incorporates AI Terms Annex into all IT procurements.

**Board-level AI strategy:**
- **Digital & AI Ecosystem Acceleration** — Priority program in the Strategic Transformation Plan (STP). Board receives periodic updates. March 2026 update: "Foundational Data Security and Responsible Artificial Intelligence: Ongoing Data tagging, AI Policy, Data Warehousing, AI Security."
- **AI use cases in production/planned:** AI-generated job descriptions, intelligent contract search, fare evasion video analytics, bus fleet maintenance AI copilot, customer chatbot, AI Rule Book digitization, supply chain parts prediction.
- **Microsoft Copilot:** 15x increase in CoPilot interactions reported (March 2026).
- **AI training:** Rollout across departments in 2H 2025.

### Sources
- AI Terms Annex: https://www.wmata.com/content/dam/wmata-com/business/Artificial-Intelligence-AI-Terms-Annex-September-28-2025.pdf
- Standard IT Terms: https://www.wmata.com/content/dam/wmata-com/business/Standard-IT-Terms-and-Conditions-December-17-2025.pdf
- Board Digital & AI Ecosystem Acceleration Update (March 2026): https://www.wmata.com/content/dam/wmata-com/migrated-assets/about/board/meetings/board-pdfs/upload/3a-digital-ai-ecosystem-acceleration-update.pdf

### Verbatim clause
> "Contractor will not attempt to use WMATA Data to train, enhance, test, validate, update, develop, fine-tune, adapt or improve any artificial intelligence model or other AI Technology including (but not limited to) generative or agentic artificial intelligence models and large language models." — WMATA AI Terms Annex, §B.ii

> "Contractor has implemented an AI Program, and is and shall remain in compliance with such policies and procedures as well as all applicable laws and good industry practice for the ethical and responsible use of AI Technology, including for transparency, human interpretability, non-discrimination, mitigation of bias, safety, efficacy, security, reliability, and oversight of the AI Technology, Training Data, AI Inputs, and other data input into or otherwise used in connection with AI Technology and conducts regular audits to ensure compliance with the same." — WMATA AI Terms Annex, §D.i(c)

---

## LA Metro (Los Angeles County Metropolitan Transportation Authority) — Los Angeles

**Bucket:** SILENT
**Contractor-binding:** No

### What was found

LA Metro deploys AI across multiple programs but has no standalone agency-wide AI policy. Governance exists only in the narrow context of law enforcement/public safety analytics.

**AI deployments identified:**
- **Weapons Detection Pilot** — Board Motion 34.1 (April 2024) and July 2024 approval of $65.1M LOP for Enhanced Access Control, including pilot of two weapons detection technologies (Dual-lane metal detector + Millimeter Wave radar with AI camera). System combines AI with MMW radar and ultra-fast signal processing.
- **Bus Lane Enforcement** — Hayden AI partnership for automated bus lane and bus stop enforcement using geospatial mapping/computer vision on buses.
- **CCTV AI Upgrades** — Krekorian Amendment to Motion 34.1: "Recommendations for upgrades to the CCTV system on bus and rail facilities to support artificial intelligence and biometric technology to identify those individuals who are known repeat violent offenders, repeat disruptors to operations or individuals banned from the system by court order."
- **Millimeter Wave + AI + Facial Recognition Research** — Butts Amendment directed staff to research MMW scanners combined with video cameras and AI and facial recognition technology for train platforms.

**Governance documents (narrow scope):**
- **Bias-Free Policing Policy** — Requires non-discriminatory practices by contracted law enforcement entities; vendors must develop guidelines to mitigate biased policing, with mechanisms to identify, report, and address complaints.
- **Public Safety Analytics Policy** — Mandates transparency in algorithms, regular algorithmic audits, prompt software updates, diverse data sets, monitoring via KPIs. Aligned with White House Blueprint for an AI Bill of Rights.

**Gap:** These two policies govern law enforcement and public safety analytics only. No agency-wide AI Acceptable Use Policy, no AI procurement terms, no employee-facing AI use policy found on metro.net. The LA City ITA published a "Los Angeles A.I. Roadmap" (June 2024) but that applies to City of LA departments, not LA Metro (a separate county authority created by state statute).

### Sources
- Metro Board Report 2024-0437 (July 2024): https://datamade-metro-pdf-merger.s3.amazonaws.com/2024-0437.pdf
- Hayden AI press release: https://www.hayden.ai/press/hayden-ai-partners-with-la-metro-for-automated-bus-lane-and-bus-stop-enforcement-systems
- LA City ITA AI Roadmap (June 2024): https://ita.lacity.gov/news/ita-publishes-los-angeles-ai-roadmap
- No standalone AI policy found on metro.net

### Verbatim clause
> "Compliance with Bias-Free Policing and Public Safety Analytics Policies: As new security technologies are implemented, maintaining compliance with the Bias Free Policing and Public Safety Analytics Policies is crucial. In accordance with these two policies, Metro has adopted comprehensive strategies involving training, transparency, accountability, data management, and community engagement, which are relevant to the technologies discussed in this report. These two policies are also closely aligned with the White House Blueprint on AI Bill of Rights." — Metro Board Report 2024-0437, July 2024

---

## BART (San Francisco Bay Area Rapid Transit District) — San Francisco Bay Area

**Bucket:** SILENT
**Contractor-binding:** No

### What was found

BART has no AI-specific policy. The FY27 Preliminary Budget (March 2026) references AI features in the upcoming mobile app redesign. BART's Surveillance Technology Ordinance (2018) and Surveillance Use Policy govern surveillance deployments but are not AI-specific.

**AI references identified:**
- **Mobile App AI Features** — FY27 Preliminary Budget: "A new version of the BART mobile application is under development and will include artificial intelligence (AI) features designed to provide riders with real time and responsive information about trips and service conditions."
- **Surveillance Technology Ordinance (2018)** — Requires Board approval of Surveillance Use Policies and Surveillance Impact Reports for surveillance technology. Not AI-specific but covers AI-enabled surveillance.
- **BART Police Department Policy Manual (2024)** — Governs BPD; no AI-specific provisions located.

**Gap:** No AI-specific Acceptable Use Policy, no AI procurement governance, no employee-facing AI use policy. Board-adopted policies list (2013-2026) includes no AI policy. BART is a special-purpose district under California law and does not inherit from Caltrans or statewide AI policies.

### Sources
- BART FY27 Preliminary Budget Memo (March 2026): https://www.bart.gov/sites/default/files/2026-03/BART%20FY27%20Preliminary%20Budget%20Memo_FINAL_0.pdf
- BART Board-Adopted Policies: https://www.bart.gov/about/bod/policies
- BART Surveillance Technology Ordinance (2018): https://www.bart.gov/sites/default/files/docs/BART%20Surveillance%20Technology%20Ordinance%20%28Second%20Reading%20for%20Ordinance%29.pdf
- No standalone AI policy found

### Verbatim clause
> "A new version of the BART mobile application is under development and will include artificial intelligence (AI) features designed to provide riders with real time and responsive information about trips and service conditions." — BART FY27 Preliminary Budget Memo, March 2026

---

## MBTA (Massachusetts Bay Transportation Authority) — Boston

**Bucket:** ENCOURAGE
**Contractor-binding:** Yes

### What was found

MBTA inherits the Massachusetts Executive Office of Technology Services and Security (EOTSS) Enterprise Use and Development of Generative AI Policy (effective Jan 31, 2025, Document ID AI.001). MBTA is an executive branch agency under MassDOT and is bound by EOTSS enterprise policies.

**Key policy provisions (EOTSS GenAI Policy):**
- **Scope:** Applies to all Executive Department Agencies and "all state employees, contractors, consultants, vendors, and interns, including full-time, part-time, or voluntary (hereinafter referred to as 'Personnel')."
- **Fact-checking/human verification:** "Commonwealth Agencies and Offices must implement a continuous processes for fact checking and human verification of Generative AI-generated content."
- **Bias mitigation:** "Bias identification, management and mitigation must be considered at all stages of the Generative AI development lifecycle, designing, developing, deploying, evaluating, using, and auditing."
- **Disclosure/attribution:** "Generative AI content used by Commonwealth Agencies and Offices must be clearly labeled in a conspicuous manner, including details of its review, and editing process."
- **Procurement gate:** "Commonwealth Agencies and Offices must notify and seek approval from the Commonwealth Chief Technology Officer (CTO) if they intend to procure Generative AI specific software or services from a third-party vendor."
- **AI Catalog:** EOTSS maintains a GenAI Catalog of approved solutions.
- **AI Sandbox:** Testing environment for AI use cases.

**MBTA-specific AI use:**
- **Safety Committee (July 2025):** Chair Koutoujian asked about AI use. Mark Molewyk (Quality Management) discussed AI for audit plans and video monitoring. Meredith Sandberg (Director) said "AI can be useful for documentation purposes and video monitoring, but that staff were approaching its use cautiously." Chair Koutoujian noted "it is important to have human redundancy when using AI and to not blindly follow leads."
- **Bus Transit Signal Priority** — AI used to improve bus travel times in Allston corridor (Feb 2025).
- **Chatbot** — Customer service chatbot in testing since 2024 (internal tool for representatives).

**Statewide context:** Massachusetts IT Strategic Plan 2026-2028 includes "Roll out AI Assistant" and "Provide AI trainings and guidance" as enterprise priorities. Governor Healey's AI Strategic Task Force (EO 628/629) and the FutureTech Act (July 2024, $25M for AI projects) provide additional state-level AI governance.

### Sources
- EOTSS GenAI Policy (Jan 31, 2025): https://www.mass.gov/doc/enterprise-use-and-development-of-generative-artificial-intelligence-policy-0/download
- MBTA Safety Committee Minutes (July 2025): https://cdn.mbta.com/sites/default/files/2025-09/2025-7-17-mbta-safety-meeting-minutes.pdf
- Massachusetts IT Strategic Plan 2026-2028: https://www.mass.gov/doc/statewide-it-strategy-for-2026-2028-pdf/download
- Mass.gov AI page: https://www.mass.gov/artificial-intelligence-at-the-commonwealth

### Verbatim clause
> "This Policy applies to all state employees, contractors, consultants, vendors, and interns, including full-time, part-time, or voluntary (hereinafter referred to as 'Personnel'). Commonwealth Agencies and Offices must implement a continuous processes for fact checking and human verification of Generative AI-generated content and ensure that all Generative AI practices comply with applicable laws, regulations, policies, and guidelines including those concerning discrimination, privacy, and data protection." — MA EOTSS Enterprise Use and Development of Generative AI Policy, Jan 31, 2025

---

## CTA (Chicago Transit Authority) — Chicago

**Bucket:** SILENT
**Contractor-binding:** No

### What was found

CTA has no standalone AI-specific policy. The FY2026 Budget Book references AI in security and customer experience contexts.

**AI deployments identified:**
- **Gun Detection Pilot** — "In 2024, CTA began piloting a proactive Artificial Intelligence (AI)-based software that leverages CTA's security cameras to specifically monitor for and alert security officials to only brandished firearms." (FY2026 Budget Book)
- **Customer Experience AI** — FY2026 Budget Book: "provide customers with a more personal experience through additional AI."
- **Bus Lane Enforcement** — Chicago Transit Board approved contract with Hayden AI for automated bus lane enforcement (in partnership with Philadelphia Parking Authority model).
- **AI Chatbot** — "Chat with CTA" multi-lingual chatbot launched with Google AI (public sector partnership).

**Gap:** No AI-specific Acceptable Use Policy, no AI procurement terms, no overarching AI governance framework found on transitchicago.com. CTA is governed by the Chicago Transit Board (7 members, 4 appointed by Chicago mayor, 3 by suburban mayors). Subject to Illinois state law but no Illinois statewide AI policy binding CTA was identified. The Regional Transportation Authority (RTA) oversees CTA, Metra, Pace but has no AI policy.

### Sources
- CTA FY2026 Budget Book: https://cst.brightspotcdn.com/9c/b0/c9bab8dc45b29c3a0aa9a418f543/fy2026-budget-book.pdf
- CTA press release (gun detection): https://www.transitchicago.com/cta-leverages-extensive-security-camera-network-to-pilot-gun-detection-technology/
- Google Public Sector chatbot: https://publicsector.google.com/ai/chicago-transit-authority-launches-a-multi-lingual-chatbot-for-more-a-more-seamless-commute/
- No standalone AI policy found

### Verbatim clause
> "In 2024, CTA began piloting a proactive Artificial Intelligence (AI)-based software that leverages CTA's security cameras to specifically monitor for and alert security officials to only brandished firearms." — CTA FY2026 Budget Book

---

## SEPTA (Southeastern Pennsylvania Transportation Authority) — Philadelphia

**Bucket:** SILENT
**Contractor-binding:** No

### What was found

SEPTA has no standalone AI-specific policy. The agency operates one of the largest automated bus lane enforcement programs in the US using Hayden AI.

**AI deployments identified:**
- **Bus Lane Enforcement (Hayden AI)** — 152 buses and 38 trolleys equipped with Hayden AI cameras for automated bus lane and bus stop enforcement. Pilot began 2023 (7 buses on Routes 21 and 42, 4,174 lane-blocks and 32,218 stopping incidents in 70 days). Scaled citywide May 2025. In first month of full enforcement (June 2025), captured violations dropped 51% year-over-year. $14.5M in fines issued May 2025–June 2026. Median bus travel time dropped 41 seconds.
- **Trolley Lane Enforcement** — AI cameras on trolleys T1-T5 and G1 route for "no parking" enforcement in trolley lanes (March 2026).
- **Internal AI use** — Job postings reference AI tool familiarity.

**Gap:** No AI-specific Acceptable Use Policy, no AI procurement governance, no overarching AI framework found on septa.org. SEPTA is a Pennsylvania state-created authority. No Pennsylvania statewide AI policy binding SEPTA was identified. The Philadelphia Parking Authority (PPA) is a partner in enforcement but PPA has no public AI policy either.

### Sources
- ITS International (July 2025): https://itsinternational.com/feature/make-way-bus-streets-philadelphia
- The Conversation / Metropolitan Digital: https://metropolitandigital.com/the-conversation/20671-philadelphia-is-using-ai-driven-cameras-to-keep-bus-lanes-clear-%E2%80%93-transparency-can-help-build-trust-in-the-system
- Streamline Feed (Kenya): https://streamlinefeed.co.ke/news/septa-ai-cameras-halve-illegal-parking-in-philadelphia-bus-lanes
- No standalone AI policy found on septa.org

### Verbatim clause
> "In partnership with the Southeastern Pennsylvania Transportation Authority (SEPTA), PPA worked with Hayden AI to install our vision AI technology on 152 Septa buses and 38 trolleys. Unlike stationary cameras, Hayden AI installs automated camera enforcement technology on transit vehicles themselves – the buses and trolleys that connect riders with destinations across the city every day." — ITS International, July 2025

---

## Sound Transit (Central Puget Sound Regional Transit Authority) — Seattle

**Bucket:** SILENT
**Contractor-binding:** No

### What was found

Sound Transit has no standalone AI-specific policy. The agency's Innovation and Technology Fund supports AI-adjacent programs, and job postings reference AI pilot programs.

**AI-adjacent programs identified:**
- **Innovation and Technology Fund** — $75M from 2016 voter-approved ST3 measure. Supports "parking monitoring technology, video analytics tools and accuracy of our in-vehicle automatic passenger counting systems."
- **AI Pilot Programs** — Job postings (2025-2026) for Collaboration & Productivity Services Intern and Senior Technical Project Manager reference "planning, execution, tracking, and documentation of AI pilot programs across enterprise collaboration platforms" and "creating, supporting and managing AI pilot programs from kickoff through evaluation."
- **SMART Grant (with SDOT)** — $2M federal grant for Rainier Valley safety. "One technology, based on real-time video analytics and using artificial intelligence, would allow safety messages to be broadcast in real-time to bicyclists and pedestrians, connected vehicles, warning devices and advanced transportation controllers."
- **2025 Board Annual Program Review** — Mentions AI in context of enterprise initiatives and ERP modernization.

**Gap:** No AI-specific Acceptable Use Policy, no AI procurement terms, no overarching AI governance framework found on soundtransit.org. Sound Transit is a regional special-purpose district (Pierce, Snohomish, King Counties). It does not inherit from Seattle's AI policy (2025-2026 AI Plan, Mayor's IT Subcabinet AI Workgroup) or Washington state policies. Seattle's Q1 2026 AI Usage Report mentions Sound Transit only as a partner in the SMART grant, not as inheriting Seattle's governance.

### Sources
- Sound Transit Innovation & Technology: https://www.soundtransit.org/system-expansion/innovation-technology
- Sound Transit 2025 Board Annual Program Review: https://www.soundtransit.org/st_sharepoint/download/sites/PRDA/FinalRecords/2025/2025%20Board%20Annual%20Program%20Review%2011-07-2025.pdf
- Sound Transit jobs: https://www.soundtransit.org/get-to-know-us/jobs
- Seattle Q1 2026 AI Usage Report: https://clerk.seattle.gov/~cfpics/cf_323759_q1.pdf
- No standalone AI policy found on soundtransit.org

### Verbatim clause
> "Sound Transit's work to test parking monitoring technology, video analytics tools and accuracy of our in-vehicle automatic passenger counting systems all fall within this program. ... Support planning, execution, tracking, and documentation of AI pilot programs across enterprise collaboration platforms." — Sound Transit Innovation & Technology pages / job postings

---

## Cross-cutting observations

1. **Only 2 of 8 transit authorities have published AI governance:** WMATA (via AI Terms Annex) and MBTA (via inherited MA EOTSS policy). Both are contractor-binding.

2. **The rest are SILENT despite heavy AI use:** MTA, LA Metro, CTA, and SEPTA are among the most aggressive AI-deploying transit agencies in the country (predictive maintenance, weapons detection, bus lane enforcement, chatbots) yet have no AI-specific governance documents.

3. **State inheritance is inconsistent:** MBTA inherits Massachusetts' EOTSS policy. MTA does NOT inherit any NY State AI policy (because none exists — NYSDOT was SILENT in Installment 1). BART does not inherit California or Caltrans AI governance. Sound Transit does not inherit Seattle's AI policy.

4. **Contractor question mostly unanswered:** 6 of 8 agencies leave the consultant/contractor question unanswered. Only WMATA and MBTA explicitly bind contractors to AI rules.

5. **Pattern mirrors Installment 1:** As with state DOTs, the operative AI policy is usually NOT at the transit agency — it's either inherited from a parent state (MBTA/MA), embedded in procurement terms (WMATA), or absent entirely (the other 6).

6. **APTA released an AI Primer (May 2026):** The American Public Transportation Association published "Artificial Intelligence (AI) and Machine Learning (ML) in Public Transit: A Primer" with four companion Guidance Briefs (Tool & Infrastructure Needs, Policy and Governance Needs, Agency Readiness and Staff Capacity, Implementation Guide). This is industry guidance, not binding policy, but signals the sector is moving toward formal governance.

---

## Methodology note

Per methodology.md: each agency's website was searched for "artificial intelligence," "AI policy," "generative AI," "machine learning policy," "acceptable use policy AI," "ChatGPT." Board minutes, procurement documents, and press releases were reviewed. PDFs were text-extracted. If no AI-specific policy was found at any level, the entity was classified SILENT. Silent does not mean permitted — most silent agencies still inherit general IT acceptable-use policies that may limit AI use in practice, even when no AI-specific document exists.
