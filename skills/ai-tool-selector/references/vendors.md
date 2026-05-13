# Vendor Knowledge Base

This file captures the **structure** of each vendor's enterprise offerings — tier shape, key features, and buyer-fit patterns. **Always verify exact pricing, current tier names, and feature availability via web search in Phase 3.** Tier names and prices drift; the M365 add-in landscape and BAA scope shifted meaningfully between January and May 2026.

Last reviewed: 2026-05-12 (cross-checked against vendor docs + Stellis SMB research March 2026; vendor docs preferred where they conflict)

---

## ChatGPT (OpenAI)

### Tiers in scope

**ChatGPT Business**
- Verified price (May 2026): **$20/seat/month annual** (dropped from $25 on April 2, 2026), **$25–$30/seat/month monthly**
- Seat minimum: **2**
- SSO: SAML (yes)
- Admin controls: workspace controls, SOC 2, audit logs
- Training opt-out: yes by default
- **BAA: NOT available on Business.** OpenAI explicitly does not offer a BAA for ChatGPT Business — confirmed in OpenAI's own help center
- Best fit: small-to-mid teams 2–500, mainstream productivity, no HIPAA

**ChatGPT Enterprise**
- Pricing band: custom, typically $60/seat/month at lower seat counts; lower at scale with negotiation
- Seat minimum: sales-managed (historical ~150 seat floor relaxed but still mid-market+; verify in Phase 3)
- SSO: SAML, SCIM
- Admin controls: full enterprise admin, audit logs, RBAC with custom roles, group-based feature controls
- Training opt-out: yes by default
- BAA: **available**, sales-managed only
- Compliance: SOC 2 Type 2, ISO 27001, 27017, 27018, 27701
- Data residency: US, EU, UK, Japan, Canada, South Korea, Singapore, Australia, India, UAE
- Best fit: 150+ seat orgs, compliance-sensitive, willing to negotiate enterprise contract

**ChatGPT for Healthcare** (new SKU, March 2026)
- Dedicated HIPAA-ready Enterprise variant; sales-managed
- Includes BAA, RBAC, audit logs, clinical search with citations
- GPT-5.2 specifically tuned/evaluated for clinical scenarios
- Pricing: based on Enterprise, contract-level shared credit pool (no per-seat caps)
- Best fit: healthcare providers, payers, healthcare data processors

### ChatGPT capabilities (May 2026)

- **Image generation**: gpt-image-2 / Images 2.0 (April 2026). High accuracy on in-image text. Commercially licensed. Effectively unlimited for Business+. **Decisive ChatGPT advantage** — Claude has no native image gen.
- **Excel add-in**: beta-only, US/Canada/Australia. **Missing: pivot tables, Power Query, VBA, macros, data validation, named ranges.** This is a significant gap for Excel-heavy clients.
- **PowerPoint add-in**: none
- **Word add-in**: none
- **Outlook add-in**: none
- **Deep Research**: globally available, 25–250 runs/month depending on tier, MCP/app connectors added Feb 2026
- **Agent Mode**: web automation, ~40 tasks/month at Business tier; Pro tier has more
- **Custom workflows**: GPTs, Projects, Skills, Codex
- **Workspace integrations**: 60+ app connectors out of the box

### ChatGPT fit profile

**Strong fit when:**
- Image generation is a top-3 use case (only ChatGPT has it natively at production quality among the three)
- Mainstream knowledge work, broad ecosystem, lowest adoption friction (highest brand recognition)
- Google Workspace shop (no native Copilot story; ChatGPT becomes default-of-defaults)
- Quantitative / statistical reasoning is core (mathematical benchmarks favor ChatGPT)
- Deep Research is a core use case (most mature, globally available)
- Need broad multimodal capability (image, voice, agent) in one tool

**Weaker fit when:**
- M365 file-level integration is required (Excel beta is functionally limited; no PowerPoint/Word add-in)
- Highest writing quality matters (Claude generally preferred for long-form prose)
- HIPAA workload at SMB scale (no Business-tier BAA — must jump to Enterprise/Healthcare)
- Coding work spans large, complex codebases (Claude generally preferred)

---

## Claude (Anthropic)

### Tiers in scope

**Claude Pro** (individual; mentioned for context, not typical enterprise pick)
- $20/month
- Includes Claude for Excel, PowerPoint, Word (GA May 7, 2026), Outlook (beta)
- Not the right answer for company-wide deployment; flag if surfaced

**Claude Team**
- Verified price (May 2026): Standard seats **$25/seat/month annual** ($30 monthly); Premium seats $100/seat/month annual ($125 monthly, adds Claude Code)
- Seat minimum: **5**
- Mix Standard and Premium within same org
- Maximum 150 seats — above that requires Enterprise
- SSO: **SAML SSO + JIT provisioning supported on Team** (this changed from earlier; Anthropic's own help center confirms)
- Admin controls: central billing, role-based permissions, per-user and org-level spend caps, domain capture
- Training opt-out: yes by default — Anthropic does not train on customer data
- BAA: **NOT available on Team**
- Best fit: 5–150 seat teams, strong writing/reasoning needs, hard cost controls desired

**Claude Enterprise**
- Sales-assisted; pricing custom (community reports ~$60/seat with ~70-seat minimum, scaling up; per-token usage billed separately on usage-based contracts)
- 500K context window (vs 200K on Team)
- SAML SSO, SCIM, audit logs, HIPAA-readiness, custom data retention, domain capture, dedicated support
- **BAA: available** — Enterprise admins can self-activate HIPAA-ready configuration with click-to-accept BAA (since April 2026). Covers chat + projects; does NOT cover Cowork or Claude for Office add-ins (still treated as beta from a BAA perspective)
- Compliance: SOC 2 Type 2, ISO 27001, NIST 800-171r3 attestation for CUI
- Data residency: US-only inference available at 1.1x pricing
- Best fit: enterprise orgs prioritizing writing quality, document workflows, long-context work, regulated industries

### Claude capabilities (May 2026)

- **Image generation**: **none natively**. Decisive Claude weakness.
- **Excel add-in**: **GA May 7, 2026**. Reads multi-tab workbooks, supports pivot tables, charts, conditional formatting. MCP connectors for financial data (S&P Global, LSEG, PitchBook, FactSet, Daloopa, Moody's). Choose Sonnet 4.6 or Opus 4.6/4.7.
- **PowerPoint add-in**: **GA May 7, 2026**. Respects slide master/layouts/fonts/colors. Generates native charts and diagrams (not images). URL-to-deck, PDF-to-deck, full-deck translation, speaker notes.
- **Word add-in**: **GA May 7, 2026**. Edits appear as native tracked changes.
- **Outlook add-in**: **public beta May 7, 2026**. Email drafting, thread summarization.
- **Cross-app context**: Conversation context flows across Excel ↔ PowerPoint ↔ Word ↔ Outlook. Adjusting a number in Excel can auto-update charts in PowerPoint and figures in Word memos within the same session. **No competitor matches this today.**
- **Skills**: reusable multi-step workflows exposed as one-click actions inside the M365 add-ins, shareable org-wide
- **Claude Code**: integrated CLI for engineering work; on Premium Team seats or Enterprise
- **Deep Research**: still US/Japan/Brazil only as of latest check (verify in Phase 3 — geographic restriction is meaningful)
- **Context window**: 200K (Team), 500K (Enterprise standard), 1M (Opus 4.6+ available)
- **Multimodal**: text + image input; **no image output**

### Claude fit profile

**Strong fit when:**
- M365 file-level work is core — Excel modeling, PowerPoint decks, Word documents (the cross-app story is genuinely differentiated)
- Use cases skew toward writing, drafting, document analysis, reasoning-heavy work
- Long documents (contracts, research reports, codebases) are central
- Buyer values Anthropic's safety positioning (often resonates with healthcare, legal, nonprofits)
- Excel work requires pivot tables, financial data connectors, or large model files (where ChatGPT's Excel beta falls short)
- Coding workflows are central (especially with Claude Code on Premium seats)
- HIPAA-required workloads in M365-deep healthcare orgs (Enterprise+BAA, but note Office add-ins are NOT yet under BAA scope)

**Weaker fit when:**
- Image generation is a top-3 use case (deal-breaker — no native image gen)
- Brand recognition matters most for adoption (ChatGPT still wins recognition)
- Deep Research is critical and client is outside US/Japan/Brazil
- Voice / multimodal output beyond text is a hard requirement
- Tenant-grounded M365 search across SharePoint/Teams is the priority (Copilot wins this; Claude reads open files but doesn't index the tenant)

---

## Copilot (Microsoft)

### Tiers in scope

**Microsoft 365 Copilot Business** (SMB SKU — capped at 300 users)
- Verified price (May 2026): **$18/user/month** through June 30, 2026 (promo); **$21/user/month** after
- Requires qualifying base license: Microsoft 365 Business Basic, Standard, or Premium
- All-in cost example: $18 add-on + $14 Business Standard = ~$32/user/month total
- Best fit: <300-user SMBs already on M365 Business

**Microsoft 365 Copilot Enterprise**
- Verified price (May 2026): **$30/user/month annual commitment**
- Requires qualifying base license: M365 E3, E5, Business Standard, or Business Premium
- All-in cost example: $30 add-on + $36 E3 = ~$66/user/month total (the colleagues' doc's "$55–75+" range is the all-in figure)
- Now bundles Copilot for Sales, Service, Finance (no additional cost)
- Best fit: 300+ user orgs or any size needing E3/E5 features

### Copilot capabilities (May 2026)

- **M365 surface integration**: native + tenant-grounded across Word, Excel, PowerPoint, Outlook, Teams, SharePoint, OneDrive, Loop
- **Work IQ**: semantic index over tenant data; conversation memory; agents like Researcher, Analyst, Facilitator
- **Copilot Studio**: $200/tenant/month base for external agents (internal agents included)
- **Identity / admin**: native Entra ID, full M365 admin telemetry, audit logs, SSO, conditional access — strongest of the three for IT control
- **Image generation**: limited (not a core strength)
- **Coding**: separate product — GitHub Copilot
- **Deep Research**: not a feature
- **Data boundary**: stays inside the M365 tenant; this is its single biggest structural advantage
- **BAA**: available within standard M365 BAA scope (already in place for most M365 customers)

### Copilot fit profile

**Strong fit when:**
- Deep M365 user base — most work happens inside Word, Excel, Outlook, Teams, SharePoint
- IT prefers vendor consolidation under Microsoft (single bill, single identity provider, single audit surface)
- Tenant-boundary data security is a hard requirement
- Use cases are M365-grounded: drafting in Word, formulas in Excel, summarizing Teams meetings, finding answers across SharePoint
- Strong admin/governance and telemetry needs
- Already paying for E3/E5 and the base license is sunk cost

**Weaker fit when:**
- Google Workspace shop (no equivalent surface integration)
- M365 environment is immature — disorganized SharePoint, weak data hygiene, inconsistent file structure (Copilot's grounding only works as well as the underlying organization of the tenant; many SMBs aren't there yet)
- Use cases live outside the M365 surface area
- Buyer wants frontier-model feel for general AI work — Copilot's chat surface is more constrained than the underlying GPT models
- Output writing quality is paramount (Claude generally preferred for prose)
- Team values experimentation and custom workflows beyond what M365 surfaces support

---

## Vendor stability (May 2026)

Provided as a non-rule consideration. All three are operationally stable and unlikely to be near-term viability risks for a 12–36 month enterprise contract horizon.

- **OpenAI**: $852B post-money valuation (March 31, 2026 close on $122B round). ~$24B annualized revenue. Enterprise now ~40% of revenue. IPO prep underway with Goldman, JPMorgan, Morgan Stanley; earliest filing window Q4 2026.
- **Anthropic**: $380B post-money from Feb 2026 Series G ($30B raised). In active talks for a new round at **>$900B valuation** (Bloomberg, May 12, 2026). Revenue run rate $20–26B projected for 2026; reported >$45B annualized run rate by some sources. Growth outpacing OpenAI on a percentage basis.
- **Microsoft**: Public company, fortress balance sheet ($78B cash). AI business at $37B annual run rate (up 123% YoY). 20M+ paid Copilot seats. Lowest stability risk of the three by a wide margin — the right answer for buyers who care most about vendor longevity.

**Synthesis for memos**: "All three are stable; if vendor longevity is itself a top-3 selection criterion, Microsoft is the safest bet. OpenAI and Anthropic are both growing at rates that make near-term viability moot — but if a regulated buyer wants public-company financial transparency, only Microsoft offers it today."

## Reliability

Both ChatGPT and Claude experienced notable outages in early 2026 (ChatGPT: Feb 3–4 and March routing failure; Claude: March 2–3 and March 11 global). Microsoft 365 enterprise reliability is generally better but Copilot specifically can lag the broader M365 SLA. **Memo guidance**: don't over-promise uptime for AI-specific workloads; recommend backup workflows for time-sensitive tasks.

---

## Decision heuristics (for the reasoning layer)

These are pattern-matches Jim has historically used. They are heuristics, not rules — the LLM should weigh them against intake context.

1. **M365-deep + standard business + non-technical workforce + budget tolerance for the all-in** → **Copilot M365 Business** ($18 add-on) or **Enterprise** ($30 add-on) wins more often than not. Key risk: an immature M365 tenant (disorganized SharePoint, weak file hygiene) blunts Copilot's value — Claude or ChatGPT may produce a better outcome in that case.
2. **M365-deep + Excel/PowerPoint/Word are where the actual daily work happens + writing quality matters** → **Claude Team** (with add-ins) is now a serious contender against Copilot, especially since the May 7, 2026 cross-app GA. This is a new pattern post-March 2026.
3. **Google Workspace shop + M365-light + general knowledge work** → ChatGPT is usually the path of least resistance. (Note: Gemini would often be the right answer here, but is out of v1 scope. Surface this as a caveat in the memo.)
4. **Writing/research/legal/professional-services-heavy + values document quality** → Claude is often the better answer even when adoption is slightly harder.
5. **Regulated + need BAA + small seat count** → eliminates ChatGPT Business and Claude Team; forces Enterprise comparison. For healthcare specifically, ChatGPT for Healthcare and Claude Enterprise (HIPAA-ready) are the two paths.
6. **Tight budget + <50 seats + no compliance** → Business/Team tiers; ChatGPT Business at $20 is the new floor for the three vendors.
7. **Image generation is top-3 use case** → ChatGPT (Claude can't, Copilot is weak).
8. **Workforce lives in Excel and needs pivot tables/Power Query/macros** → Claude or Copilot, not ChatGPT (Excel beta limitation).

## Discrepancy log

Phase 3 verification on **2026-05-12** surfaced these drift items vs. prior state of this file:
- ChatGPT Business dropped from $25 to $20/seat/month annual on April 2, 2026.
- Copilot SMB Business tier exists at $18/seat (promo through June 30, then $21).
- Claude Team SSO + JIT confirmed at Team tier (not Enterprise-only).
- Claude for Word now GA (not just Excel + PowerPoint); Outlook in public beta.
- ChatGPT for Healthcare is a new sales-managed SKU (March 2026).
- Claude HIPAA-ready Enterprise now self-serve via click-to-accept BAA (April 2026 onward).

When discrepancies accumulate (3+ new ones), refresh this file.
