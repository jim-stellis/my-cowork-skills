# Intake Interview

Walk Jim through these questions in order. Branch where noted. Capture answers into `intake.json` per the schema in `schemas.md`.

Ask **one section at a time**, not all questions at once. Confirm answers before moving on.

---

## Section 0 — Engagement Scope (NEW)

Before company facts, anchor what this recommendation is FOR. The skill recommends a single tool per intake; if the client needs different tools for different functions, the skill should be run multiple times with different scope answers.

S1. **Engagement scope** — what does this recommendation cover? Pick one:
   - Whole company / primary AI tool for everyone
   - A specific function or team (specify: e.g., "leadership and knowledge workers", "operations and customer service", "marketing", "engineering")
   - A specific use-case bundle (specify)

S2. **Approximate scope size** — how many seats are in scope for THIS recommendation? (number; may be smaller than total company headcount if scope is a function)

Treat this as the anchor for the rest of the intake. When a later question asks about "the workforce" or "the team," it means the people inside this scope, not the whole company.

---

## Section 1 — Company Profile

1. **Company name** (free text)
2. **Industry** (free text — capture verbatim, e.g., "regional commercial real estate," "boutique law firm," "specialty manufacturer")
3. **Total employee count** (number — whole company, not just scope)
4. **Nonprofit status** — choose one:
   - For-profit
   - 501(c)(3) nonprofit
   - 501(c)(6) association / AMC
   - Other nonprofit / government
5. **Regulatory posture** — choose one:
   - None / lightly regulated
   - Standard business (SOC 2 expected from vendors, no special industry rules)
   - Regulated — HIPAA
   - Regulated — financial services (GLBA, FINRA, SEC, banking)
   - Regulated — government / public sector (FedRAMP, CJIS, ITAR)
   - Regulated — other (capture details)

## Section 2 — Current Stack

6. **Productivity suite** — choose one:
   - Microsoft 365 (primary, deeply embedded — most work happens in Word/Excel/PowerPoint/Teams/SharePoint)
   - Microsoft 365 (using but not deeply embedded — mostly email and basic Office)
   - Google Workspace (primary, deeply embedded)
   - Google Workspace (using but not deeply embedded)
   - Mixed M365 + Google
   - Neither / other
7. **M365 tenant maturity** *(only ask if Q6 is M365)* — choose one:
   - Mature (clean SharePoint structure, consistent file org, active Teams usage, good data hygiene)
   - Mixed (some pockets organized, others messy)
   - Immature (disorganized SharePoint, weak file structure, email-first culture)
   - Don't know yet
8. **Identity provider** (free text — Entra ID/Azure AD, Okta, Google, JumpCloud, none, etc.)
9. **SSO required for the AI tool?** (yes / no / nice-to-have)
10. **SCIM required?** (yes / no) *Only ask if Q9 is yes.*
11. **Existing AI tools in use** (free text — list any current paid or free AI tools, pilots, individual subscriptions)

## Section 3 — Use Cases

12. **Top 3 use cases ranked** — what does the in-scope group most need AI to do? Ask Jim to rank top three from this list (or add custom):
    - Document drafting and editing (Word, email, proposals)
    - Meeting summarization and notes
    - Data analysis and spreadsheet work
    - Research and information synthesis
    - Coding / engineering support
    - Customer-facing chatbot or support
    - Knowledge base Q&A across internal docs
    - Image / visual content creation
    - Sales enablement (call notes, follow-ups, CRM)
    - Presentation creation (slide decks)
    - Other (specify)

13. **Image generation requirement** *(only ask if Q12 includes "Image / visual content creation")* — is image generation:
    - Required (a deal-breaker)
    - Strongly preferred (nice but not deal-breaking)
    - Marginal (could be solved another way)

14. **Excel feature dependencies** *(only ask if Q12 includes "Data analysis and spreadsheet work")* — does the client rely on any of these in their daily Excel work?
    - Pivot tables
    - Power Query
    - VBA / macros
    - Named ranges / complex data validation
    - Financial data connectors (S&P, FactSet, PitchBook, etc.)
    - None of these — basic Excel only

15. **Connectors needed** — does the tool need to read from any of these out of the box?
    - SharePoint / OneDrive
    - Google Drive
    - Slack
    - Teams
    - Salesforce / HubSpot
    - Custom internal systems
    - None required

## Section 4 — Security & Constraints

16. **Data residency** — any geographic requirements? (US-only, EU-only, no requirement, other)
17. **Training data opt-out required?** (must — model cannot train on our data / preferred / no preference)
18. **DLP / admin controls needed?** (must have enterprise admin controls and audit logs / nice to have / no requirement)
19. **BAA required?** (yes — HIPAA / no) *Only ask if regulatory posture is HIPAA.*
20. **Air-gap or on-prem requirement?** (yes / no) *Only ask if regulatory posture is government or financial services.*

## Section 5 — Budget

21. **Per-seat monthly budget ceiling** (USD — what's the absolute max per seat per month? Allow "no ceiling" as an answer.)
22. **All-in or add-on?** When you state the per-seat budget, are you thinking:
    - All-in (includes any required base licenses like M365)
    - Add-on only (the AI tool itself, base licenses are separate)
    - Don't know — show me both
23. **Total annual budget envelope** (USD — what's the total earmarked for the AI platform per year? Allow "no ceiling" as an answer.)
24. **Procurement constraints** — anything unusual? (annual prepay required, vendor consolidation preference, must go through specific reseller, EA renewal cycle, etc. — free text)

## Section 6 — Team & Change

25. **AI maturity of the in-scope workforce** — choose one:
    - Novice (most users have never seriously used an AI tool)
    - Mixed (some power users, most novices)
    - Intermediate (most users have used ChatGPT or similar casually)
    - Advanced (team includes builders, prompt-savvy users, existing AI workflows)
26. **Change tolerance** — choose one:
    - Low (will resist anything that changes their workflow)
    - Medium (will adopt with structured rollout and training)
    - High (eager early adopters, willing to experiment)
27. **Executive sponsorship strength** — choose one:
    - Strong (CEO/exec actively driving)
    - Moderate (supportive but not driving)
    - Weak (no clear sponsor)

## Section 7 — Strategic Free-Text

28. **What does success look like in 6 months?** (free text — capture Jim's read of the client's actual goal, in their language if possible)
29. **What's the biggest risk if we get the tool choice wrong?** (free text — captures the asymmetry: e.g., "they'll abandon AI entirely," "they'll waste $200k on shelfware," "competitor advantage")
30. **Vendor stability concern?** — does the client specifically care about vendor longevity, public-company financial transparency, or IPO/M&A risk? (yes / no / they brought it up unprompted)
31. **Any tools they've already ruled in or out, and why?** (free text)

---

## Branching rules

- If **scope size < 25** AND **regulatory posture = none**: skip Q18 (DLP), default to "nice to have."
- If **Q6 = Google Workspace (deeply embedded)**: flag that none of the three in-scope vendors is a perfect native fit, AND that Gemini (out of v1 scope) is likely the better answer. Ask in Q31 whether they'd consider activating Gemini.
- If **regulatory posture = government**: warn Jim that the three-vendor scope may not be sufficient and recommend checking whether GovCloud/FedRAMP-specific solutions are needed before proceeding.
- If **Q4 = 501(c)(6) AMC**: note that neither vendor documents multi-tenant AMC models well. Likely requires separate subscriptions per client association — flag for Jim.
- If **Q4 = 501(c)(3)**: surface Claude's nonprofit positioning in the memo (Goodstack 75% discount, Blackbaud/Candid/Benevity connectors, AI Fluency for Nonprofits course). Both vendors offer ~$8/seat through Goodstack.

## After intake

Read back a 5-bullet summary of the captured profile and confirm with Jim before proceeding to Phase 2.
