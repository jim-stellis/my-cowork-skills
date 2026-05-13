# Hard Constraint Rules

Apply each rule in order against the intake JSON. Each rule eliminates one or more vendor/tier combinations. Rules are **deterministic** — no LLM reasoning at this stage. If a rule fires, the option is out.

Vendor/tier universe (full list — see `vendors.md` for details):

- **ChatGPT**: Business, Enterprise, ChatGPT for Healthcare
- **Claude**: Team, Enterprise
- **Copilot**: Microsoft 365 Copilot Business (SMB, ≤300 users), Microsoft 365 Copilot Enterprise

Note: tier names drift. Verify exact current names in Phase 3.

---

## Rule 1 — Microsoft tenant lock-in

**If** `productivity_suite = "m365_deep"` AND the client has indicated in Q23 or Q25 that data must remain in their Microsoft tenant:
- **Eliminate:** ChatGPT (all tiers), Claude (all tiers)
- **Rationale:** Only Microsoft 365 Copilot operates inside the M365 tenant boundary natively. ChatGPT and Claude live outside it. Claude's Office add-ins read open files but do not index the tenant.

## Rule 2 — Google Workspace primary

**If** `productivity_suite = "google_deep"`:
- **Flag (do not eliminate):** None of the three vendors integrates natively with Google Workspace the way Copilot does with M365. Surface this in the memo, including a note that Gemini (out of v1 scope) is likely the better answer and may already be paid for via existing Workspace subscription. ChatGPT and Claude become more viable here than in M365 shops because the "native ecosystem" advantage for Copilot disappears.

## Rule 3 — HIPAA BAA

**If** `regulatory_posture = "hipaa"` AND `baa_required = "yes"`:
- **Eliminate:** ChatGPT Business (no BAA — OpenAI's policy), Claude Team (no BAA — Anthropic's policy)
- **Surviving HIPAA-eligible options:** ChatGPT Enterprise, ChatGPT for Healthcare, Claude Enterprise (HIPAA-ready), Copilot M365 (within standard M365 BAA scope)
- **Important caveat for Claude:** the BAA does NOT currently cover Cowork or Claude for Office add-ins (Excel/PowerPoint/Word/Outlook). Surface this in the memo if the client's intended workflow relies on the Office add-ins.

## Rule 4 — Air-gap / on-prem

**If** `air_gap_required = "yes"`:
- **Eliminate:** All three vendors (all tiers).
- **Action:** Stop the skill. Output a memo explaining that none of the three primary vendors offers true air-gapped deployment, and recommend Jim explore Azure OpenAI in a private deployment, AWS Bedrock with Claude in a VPC, or an on-prem open-weights solution. This is out of scope for the Jump Start.

## Rule 5 — Seat minimums

**If** `ai_seat_count < tier_minimum_seats`:
- **Eliminate:** That tier.
- Current minimums (verify in Phase 3):
  - ChatGPT Business: 2
  - ChatGPT Enterprise: sales-managed, mid-market+ (~150 historical floor, may be relaxed)
  - Claude Team: 5
  - Claude Enterprise: ~70 (community-reported, verify)
  - Copilot M365 Business: 1 (no formal minimum, capped at 300)
  - Copilot M365 Enterprise: 1 (no formal minimum)

## Rule 6 — Seat ceiling (Copilot Business)

**If** `ai_seat_count > 300` AND option being evaluated is `Copilot M365 Business`:
- **Eliminate:** Copilot M365 Business (this tier is capped at 300 users)
- **Replace with:** Copilot M365 Enterprise as the surviving Copilot option

## Rule 7 — Budget ceiling

**If** `per_seat_budget_ceiling` is a number (not "no ceiling") AND `tier_list_price > per_seat_budget_ceiling`:
- **Eliminate:** That tier.
- **Note:** For Copilot, compare against the **all-in cost** (add-on + required base license), not the add-on alone. The client pays the full stack. For ChatGPT and Claude, compare against the add-on price (no base license required).
- **Note:** Use *list* price for filtering, but in the memo note that enterprise discounts of 10–30% are typical at scale (5–15% for Microsoft EA).

## Rule 8 — Training data opt-out

**If** `training_opt_out = "must"`:
- **Eliminate:** Any tier where the default is to train on customer data and there is no opt-out.
- **Note:** All three vendors' paid business/enterprise tiers default to NOT training on customer data. This rule almost never fires for the three in-scope vendors at business+ tiers, but verify for the specific tier in Phase 3.

## Rule 9 — Data residency

**If** `data_residency = "eu"`:
- **Verify in Phase 3** which vendors/tiers currently offer EU data residency commitments. As of May 2026, ChatGPT Enterprise offers EU residency; Claude Enterprise offers US-only inference at 1.1x pricing (EU not yet standard); Copilot follows M365 tenant residency. Eliminate those without confirmed EU options.

**If** `data_residency = "us"`:
- Generally satisfied by all three vendors at business/enterprise tiers. Verify.

## Rule 10 — Identity / SSO required

**If** `sso_required = "yes"`:
- **Do NOT eliminate Team tiers indiscriminately.** As of May 2026:
  - ChatGPT Business: SAML SSO ✓
  - Claude Team: SAML SSO + JIT provisioning ✓ (confirmed in Anthropic's help center)
  - Copilot: native Entra ID ✓
- All business/team-tier options support SSO. Only eliminate consumer tiers (Pro, Plus, Max, Free) — which shouldn't be in the universe anyway.
- If `sso_required = "yes"` AND the client requires **SCIM** specifically: eliminate Team tiers, force Enterprise comparison (SCIM is Enterprise-only at both ChatGPT and Claude).

## Rule 11 — Government / FedRAMP

**If** `regulatory_posture = "government"`:
- **Verify in Phase 3** which vendors currently hold FedRAMP authorization at what impact level. As of May 2026:
  - ChatGPT: ChatGPT Gov / Azure OpenAI Service (via Microsoft) for FedRAMP environments
  - Claude: Available in AWS Secret region (IL6) via Bedrock; Claude for Government for FedRAMP High; not the standard Enterprise plan
  - Copilot: GCC, GCC-High, DoD support available
- If no standard in-scope tier qualifies, stop and recommend GovCloud-specific solutions (out of Jump Start scope).

## Rule 12 — Excel feature dependencies (NEW)

**If** `excel_critical_features` includes any of: pivot tables, Power Query, VBA, macros, data validation, named ranges, AND `top_use_cases` includes "Data analysis and spreadsheet work" in top-3:
- **Eliminate:** ChatGPT Business and ChatGPT Enterprise *for this use case* (their Excel add-in beta does not support these features; available only in US/CA/AU).
- Surviving: Claude (Excel add-in GA May 7, 2026 supports pivot tables, charts, conditional formatting, financial data connectors), Copilot (native Excel integration with full feature support).
- **Note:** This is a use-case-conditional elimination. If Excel isn't top-3, this rule doesn't fire.

## Rule 13 — Image generation as a primary use case (NEW)

**If** `top_use_cases` includes "Image / visual content creation" in top-3 AND `image_gen_required = "yes"`:
- **Eliminate:** Claude (all tiers — no native image generation).
- Surviving: ChatGPT (gpt-image-2, commercially licensed, production-quality), Copilot (limited image gen — flag as weak).
- **Note:** If image gen is ranked top-3 but the client clarifies it's nice-to-have rather than required, treat as a fit factor in Phase 4, not a hard elimination.

---

## Filter output

After running all rules, produce a structured filter result:

```
SURVIVING OPTIONS:
- <vendor>:<tier> — passes all rules

ELIMINATED:
- <vendor>:<tier> — eliminated by Rule N (<short reason>)
```

If zero options survive, escalate to Jim with the rule list and ask whether any constraint can be relaxed.
