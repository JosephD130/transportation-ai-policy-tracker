# Methodology

How the Transportation AI Policy Tracker classifies each entity.

---

## Scope (installment 1)

52 entities: the 50 US states, the District of Columbia, and Puerto Rico. For each, the operative AI policy that governs the state Department of Transportation (or equivalent) was identified.

Sources searched, in order:

1. The state DOT's own website (search terms: "artificial intelligence," "AI policy," "generative AI," "machine learning policy," "acceptable use policy AI," "ChatGPT").
2. The state CIO / Office of Information Technology / Department of Information Services published policies covering all executive-branch agencies (which includes the DOT).
3. Governor executive orders affecting state AI use.
4. Statewide statutes and codified rules (where they apply directly to AI use by state employees and contractors).
5. State Comptroller / Inspector General audits that specifically called out the DOT (e.g., NY OSC audit, April 2025).

If no AI-specific policy was found at any of those levels, the entity is classified as SILENT. Silent does not mean permitted — most silent entities still inherit a general IT acceptable-use policy that may limit AI use in practice, even when no AI-specific document exists.

---

## Bucket classification

Each entity falls into one of four buckets:

### FORBID

Explicit prohibition on entering non-public agency data, contract data, or restricted data into publicly available / commercial GenAI tools. Consequences are stated (discipline, termination, removal of system, contract violation).

Examples:
- **Iowa** (PY-AI, March 2025): *"The use of freely available AI tools by state entities is expressly prohibited without prior written approval from the Department of Management."*
- **Oklahoma** (OMES Standard): *"Any state employee who inputs, uploads, transmits or otherwise discloses any federally protected data into a public AI system…shall be terminated."*
- **Missouri (MoDOT)** Employee Conduct: *"MoDOT prohibits the use of unapproved, open AI systems (such as ChatGPT, Bing Chat, and other publicly available AI systems) for work-related purposes."*

### ENCOURAGE

Explicit permission to use AI under stated guardrails: training requirements, supervisor approval, human-in-the-loop, data classification limits, named-tool allow-lists, mandatory disclosure, citation rules.

Examples:
- **Texas** (TxDOT AI Strategic Plan FY 2025-2027): TxDOT operates an AI Risk Management Workgroup applying NIST AI RMF; Microsoft 365 Copilot deployed to 940+ staff.
- **Massachusetts** (EOTSS): first state to deploy ChatGPT enterprise across ~40K executive staff in a walled-off environment.
- **Tennessee** (Enterprise GenAI Policy): "Safeguards State data and limits the possibility of State data being actively used in consumption or training of public Generative AI solutions."

### PARTIAL

Hybrid postures or guideline-only documents that mix forbid + encourage signals, or that lack hard-enforcement language.

Examples:
- **Nebraska** (NITC 8-609): broad authorization paired with mandatory privacy/security review.
- **North Dakota** (NDIT guidelines): guideline tone, not prohibition.
- **South Dakota** (BIT guidance): "AI-generated content is a starting point, not the finished product."

### SILENT

No AI-specific policy at the DOT, the state CIO, or the Governor's office.

Examples (state DOT layer):
- **Wisconsin (WisDOT):** funded a research program but no use policy.
- **Wyoming (WYDOT):** "leave it to the districts/agencies."
- **Puerto Rico (DTOP):** AI Act bill pending; not yet enacted.
- **New York (NYSDOT):** technically governed by NY ITS policy but the NY State Comptroller's April 3, 2025 audit explicitly found NYSDOT had no in-house policy and was piloting three AI systems with no formal governance.

---

## Contractor-binding flag

A separate dimension. An entity is flagged "contractor-binding" if the operative AI policy explicitly extends to contractors, consultants, third parties, or vendors performing work on behalf of the agency.

Mere statements that "this policy applies to state employees" do not count. The policy must name contractors / third parties / consultants / vendors / temporary personnel as covered parties.

7 of 52 entities qualify:

- **Iowa** (PY-AI): "All Support Entity workforce members (employees and contractors) and any contracted third-party performing work on behalf of the Agency must comply with this Policy."
- **Kansas** (P8200.00): contractors "must disclose any use of generative AI or integrations with such platforms in their contracts."
- **Ohio** (DAS IT-17): "Only data that is public record should be entered by state employees, contractors or temporary personnel into generative AI tools."
- **Minnesota (MnDOT)** (IT-003): "Third parties working on behalf of MnDOT must work with MnDOT staff to ensure that any tools they use are approved by MnDOT before submitting private, confidential, protected, or otherwise not public data."
- **Louisiana** (OTS AI AUP): pre-procurement review gate effectively binds vendors and consultants.
- **District of Columbia** (Mayor's Order 2024-028): first major US city to mandate Responsible AI training for "all gov employees + contractors."
- **New Jersey** (Joint Circular 25-OIT-001): mandatory "Responsible AI for Public Professionals" course; flow-down language likely.

---

## What this Tracker does NOT do

- It does not interpret what an agency *should* do. It scores what each agency *has published*.
- It does not predict where each entity is heading. Where an agency has signaled forthcoming policy (e.g., West Virginia's "coming soon" AUP, Georgia's SB37 mandate for Dec 31, 2026), the entity is classified by what is currently published.
- It does not resolve conflicts between layers (state vs. federal, DOT vs. state CIO). Use the four-step protocol in the README to know which layer governs your specific situation.
- It is not legal advice. Verify with your firm's general counsel before relying on any classification for compliance decisions.

---

## Refresh schedule

- **Per Tracker installment issue (~6 weeks):** new layer added; full repo update.
- **Per quarterly refresh (Q1 2027 onward):** scan all 84+ entities for changes; PR-merge the diff; publish a refresh issue.
- **Reader corrections:** open a GitHub issue or PR with the corrected verbatim clause and a public source URL. Material corrections published in the next refresh.

---

## Sources

Each entity's source URLs are captured in the per-region notes (`regional-source-notes/`) and in the master CSV. Verbatim quotes are cited inline. Where a primary policy PDF returned binary content that could not be machine-parsed during the initial corpus pull, the verbatim quote came from a credible secondary source (state press release, GovTech, StateScoop, NASCIO, OSC audit) — those entries are flagged in the regional notes for re-verification before being relied upon for high-stakes citations.
