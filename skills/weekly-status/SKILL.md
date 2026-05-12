---
name: weekly-status
description: Drafts Jim's weekly status email to Michael Levy (VP, Hyde Park Holdings) summarizing progress across the three AI Enablement Jumpstart engagements — Derby, NEPW, and Versant. Use this skill when Jim says "draft the weekly status", "write the Mike email", "status email for Mike", "weekly update for Hyde Park", or similar. Reads the current client profile and follow-up files to produce a concise, professional update. Do NOT send the email — produce ready-to-copy text only.
---

## What this skill produces

A weekly status email to Michael Levy, VP at Hyde Park Holdings, summarizing where each of the three jumpstart engagements stands. Mike is the portfolio sponsor — he governs and observes, attends selectively, and wants a clean summary without needing to dig into the details himself.

## Repo and file locations

**Repo:** `/Users/henleyswift/Documents/stellis/AI-Enablement-Jumpstart`

Read these files to build the email:

| Client | Profile | Follow-ups |
|--------|---------|------------|
| Derby | `clients/hyde-park/derby/derby-memory.md` | `clients/hyde-park/derby/FOLLOWUPS.md` |
| NEPW | `clients/hyde-park/nepw/nepw-memory.md` | `clients/hyde-park/nepw/FOLLOWUPS.md` |
| Versant | `clients/hyde-park/versant/versant-memory.md` | `clients/hyde-park/versant/FOLLOWUPS.md` |

Also check the `jumpstart-task-checklist-template.md` at `clients/hyde-park/` to orient each client's phase.

## Email format

**Subject:** Hyde Park AI Jumpstart — Week of [Monday's date]

**Greeting:** Hi Mike,

**Opening line:** One sentence — what week it is in the engagement and the overall tone (on track, one item to flag, etc.)

**Per-client section** (Derby, then NEPW, then Versant):

```
**[Client Name] — Week [N]: [Phase Name]**
- This week: [what happened — 1-2 bullets]
- Key development: [most important thing Mike should know — decision, blocker, new information]
- Next: [what's happening next week]
```

**Closing:**
- Flag any cross-portfolio items (things that affect all three or that Mike needs to decide)
- One line: "Happy to discuss any of these on our next call."
- Sign off as Jim

## What Mike needs to know (and what he doesn't)

**Include:**
- Which week/phase each client is in
- Any decisions made or confirmed this week
- Any blockers or items requiring Mike's attention
- Key upcoming milestones

**Exclude:**
- Granular task details (that's Jim's operational ledger, not Mike's concern)
- Technical detail that doesn't affect the engagement outcome
- Items already resolved and closed

## Calibration

Mike is a former investment banker (Macquarie, Veritas Capital) now running portfolio ops at a family office. He reads fast, expects precision, and doesn't need to be managed. Write like you're updating a smart, busy investor — not a client who needs hand-holding.

Keep each client section to 3-5 lines. The whole email should be readable in under 2 minutes.

## After drafting

Present the email as a clean copyable block with subject line. Do not add commentary unless Jim asks. If any of the profile files are missing or out of date (e.g., nepw-memory.md or versant-memory.md doesn't exist yet), note what's missing and draft with what's available.
