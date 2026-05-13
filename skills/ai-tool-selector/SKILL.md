---
name: ai-tool-selector
description: Recommend the single best primary enterprise AI tool (ChatGPT, Claude, or Copilot — at a specific tier) for a client based on a structured intake. Use this skill whenever Jim says "tool selection", "which AI tool", "AI recommendation", "jump start tool pick", "primary AI", "ChatGPT vs Claude vs Copilot", "what should they buy", "pick an AI", or any time he is scoping a Stellis Jump Start engagement and needs to recommend an enterprise AI platform. Also trigger when reviewing or updating an existing client recommendation, or when running the intake interview for a new client.
---

# AI Tool Selector

Recommends the **single primary enterprise AI tool** for a client engagement. Output is one tool at one specific tier (e.g., "Copilot for Microsoft 365 Business Standard add-on" or "ChatGPT Enterprise") with rationale, runner-up, rejected options, cost estimate, and risks.

**Scope guardrails:**
- Vendors in scope: ChatGPT (OpenAI), Claude (Anthropic), Copilot (Microsoft). No others in v1.
- **One tool per intake**, but a single client may run the skill multiple times with different *engagement scopes* (e.g., once for leadership/knowledge workers, once for ops/customer service). The intake asks for engagement scope first; subsequent recommendations are framed around that scope, not the whole company.
- This is for the Stellis Jump Start methodology.

**Tier universe (verify in Phase 3):**
- ChatGPT: Business, Enterprise, ChatGPT for Healthcare
- Claude: Team, Enterprise
- Copilot: M365 Copilot Business (≤300 users), M365 Copilot Enterprise

## Workflow

The skill runs in four phases. Do them in order.

### Phase 1 — Intake

Ask whether this is a new client or continuing an existing one:
- **New client:** Run the intake interview. Read `references/intake.md` for the question set and branching logic. Capture answers into the intake JSON schema (see `references/schemas.md`).
- **Existing client:** Ask Jim for the client folder path. Load the existing `intake.json` and ask whether anything has changed before proceeding.

Save the intake as `intake.json` inside the client folder Jim specifies. If he hasn't specified one, ask for the path.

### Phase 2 — Hard Constraint Filter (Rules)

Read `references/rules.md` and apply each rule against the intake JSON. Rules are deterministic gates — they eliminate vendors/tiers, they don't score them.

Produce an interim filter result listing:
- Vendors/tiers that pass all hard constraints
- Vendors/tiers eliminated, with the specific rule that eliminated them

If **zero** options pass, stop and tell Jim. Don't fabricate a recommendation. The honest answer ("none of the three primary vendors fit this client's constraints") is sometimes the right one and is itself valuable.

### Phase 3 — Live Verification

Before reasoning, web-search to verify current facts for the surviving options. Search for each of:
- Current pricing per seat for the surviving tiers
- Current seat minimums or commitment requirements
- Any tier changes, renames, or deprecations in the last 90 days
- Current security/compliance certifications relevant to the client's industry (e.g., HIPAA BAA availability, FedRAMP status, SOC 2)

If a search result contradicts `references/vendors.md`, **trust the search** for the recommendation and flag the discrepancy at the end of the memo so Jim can update the knowledge file.

### Phase 4 — Fit Reasoning and Memo

For the surviving options, reason about fit using the intake context. Consider:
- Ecosystem alignment (M365 shop vs Google Workspace vs mixed)
- Team's AI maturity and change tolerance
- Use case priorities ranked in intake
- Buyer profile and budget envelope
- Strategic factors Jim noted in free-text intake fields

Produce the recommendation memo using the template in `assets/memo_template.md`. The memo has six sections: primary recommendation, runner-up with switching conditions, rejected options with one-line reasons, total annual cost estimate, top three risks/caveats, and any vendor knowledge file discrepancies surfaced during verification.

Save the memo as `recommendation.md` in the client folder alongside `intake.json`.

## Output

Two artifacts in the client folder:
- `intake.json` — structured client profile
- `recommendation.md` — the memo Jim hands to the client

Present both files to Jim using `present_files` at the end.

## Maintenance

The vendor knowledge file (`references/vendors.md`) is the slowest-moving part of the skill but still drifts. Jim should refresh it quarterly. The skill flags discrepancies during live verification — when those accumulate, that's the signal to update the file.

## When Jim Pushes Back

If Jim disagrees with the recommendation, don't capitulate. Ask what specifically is wrong:
- Is a hard constraint missing or miscoded? → Update intake, re-run.
- Is the rule wrong? → Flag for `references/rules.md` revision.
- Is the fit reasoning off? → Explain the trade-off and let Jim override with rationale captured in the memo.

The skill is calibration tooling, not an oracle. Jim's judgment wins; the skill's job is to make the reasoning explicit.

## Reference files

- `references/intake.md` — interview script with branching logic
- `references/rules.md` — hard constraint rules (deterministic filter)
- `references/vendors.md` — vendor knowledge base (tiers, pricing, features)
- `references/schemas.md` — JSON schema for intake.json
- `assets/memo_template.md` — output memo template
