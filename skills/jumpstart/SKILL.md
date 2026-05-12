---
name: jumpstart
description: Manages Jim's AI Enablement Jumpstart client knowledge and task tracking across Derby, NEPW, and Versant. Use this skill whenever Jim says "update [client]", "what's open for [client]", "where are we with [client]", "status", "add a follow-up for", "mark this done", or anything involving client memory, task lists, or open commitments across the three Hyde Park jumpstart engagements. Also triggers when Jim pastes meeting notes or a transcript and wants to capture updates for a specific client. Do NOT require Jim to use specific commands — if context makes the intent clear, use this skill.
---

## What this skill manages

Jim runs AI Enablement Jumpstart engagements for three Hyde Park portfolio companies simultaneously:
- **Derby Supply Chain Solutions** — Louisville, KY — ~400 employees, 70 in scope for AI launch
- **NEPW Logistics** — Portland, ME — ~55 employees, 3PL / warehousing
- **Versant Supply Chain** — [details in versant-memory.md]

**Repo:** `/Users/henleyswift/Documents/stellis/AI-Enablement-Jumpstart`
**CLAUDE.md** in the repo root has full conventions — read it for branching, commit, and workflow rules.

## Per-client file structure

Each client lives under `clients/hyde-park/<client>/`:

| File | Purpose |
|------|---------|
| `<client>-memory.md` | Living client profile — stakeholders, tech stack, decisions, timeline, open questions, insights |
| `FOLLOWUPS.md` | Running commitments ledger — owed by Jim, waiting on client, open questions, done |
| `calls/<date>-<topic>.md` | Raw call notes (read-only reference) |
| `delivered/` | As-sent snapshots |
| `jumpstart-task-checklist-template.md` | At `clients/hyde-park/` — 9-week process checklist (reference for where clients are) |

The `<client>-memory.md` files are the primary knowledge store. FOLLOWUPS.md tracks commitments and is updated after every meeting.

## Operations

### 1 — Update a client profile + follow-ups from a meeting

**Triggers:** Jim shares a transcript, meeting summary, or notes and says "update Derby" or similar.

**Steps:**
1. Read the client's `<client>-memory.md` and `FOLLOWUPS.md`
2. Read the source material (transcript, notes, or meeting summary)
3. Extract:
   - **New facts** — stakeholder info, system details, decisions made, anything not already in the profile
   - **Profile corrections** — things that contradict or update what's there (flag these explicitly)
   - **New commitments** — things Jim owes the client (go to Active section of FOLLOWUPS.md)
   - **New waiting-on items** — things the client owes Jim
   - **New open questions**
4. Update `<client>-memory.md`:
   - Add new facts to the relevant sections
   - Add a timestamped entry to the Insights & Observations section (newest first)
   - Do NOT rewrite or reformat sections that aren't changing — surgical updates only
5. Update `FOLLOWUPS.md`:
   - Add new items to Active or Waiting sections with today's date
   - Mark items done if the meeting resolved them (move to Done with closed-on date)
6. Show Jim a summary of what changed — what was added, what was resolved, what was flagged
7. Remind Jim to commit: suggest a branch name following the CLAUDE.md convention (`<client>/post-call-<YYYY-MM-DD>`) and a commit message. Do NOT auto-commit.

### 2 — Show client status

**Triggers:** "status derby", "where are we with NEPW", "what's open for Versant"

**Steps:**
1. Read `<client>-memory.md` and `FOLLOWUPS.md`
2. Also check the `jumpstart-task-checklist-template.md` to orient where they are in the 9-week process
3. Produce a concise status view:
   - **Phase:** which week they're in and what's happening
   - **Open — owed by Jim:** items from FOLLOWUPS Active section
   - **Open — waiting on client:** items from FOLLOWUPS Waiting section
   - **Key context:** 2-3 most relevant profile facts for right now
   - **Next:** what's coming up next in the engagement

Keep it scannable — this is a quick situational check, not a full briefing.

### 3 — Cross-client overview

**Triggers:** "status all", "overview", "what's on my plate across clients", "where are all three"

**Steps:**
1. Read memory + FOLLOWUPS for Derby, NEPW, and Versant
2. Produce a one-page summary:
   - One row per client: phase, # open items owed by Jim, # waiting on client, most urgent item
   - Any items that are overdue or flagged as urgent
   - What's coming up this week across all three

### 4 — Mark items done / add follow-ups

**Triggers:** "mark this done for Derby", "add a follow-up for NEPW", "Leah confirmed the dates"

Update FOLLOWUPS.md directly — move items to Done with today's date, or add new items. Show the change and remind Jim to commit.

## Writing style for profile updates

The `<client>-memory.md` files have a specific structure (see derby-memory.md as the reference). When updating:

- **Add to the relevant section** — don't create new top-level sections unless the content genuinely doesn't fit anywhere
- **Insights & Observations** gets a new timestamped bullet for every meeting, always at the top (newest first)
- **Open commitments** section should stay in sync with FOLLOWUPS.md — they overlap intentionally (FOLLOWUPS is the operational ledger; the profile section is the summary view)
- **Flag contradictions** — if something in the transcript contradicts the profile, call it out explicitly before updating. Don't silently overwrite.
- Write in the same voice as the existing profile — factual, direct, with opinion and analysis where useful (e.g., "CRITICAL — confirmed 4/27", "Reconciliation hypothesis")

## What NOT to do

- Don't auto-commit. Per CLAUDE.md: always show the diff and let Jim decide what to stage.
- Don't reformat or rewrite sections that aren't changing.
- Don't create new files without asking — use the existing structure.
- Don't conflate FOLLOWUPS.md with the task checklist. FOLLOWUPS tracks commitments; the checklist tracks process milestones.

## Relationship to other skills

- **meeting-summary** runs first → produces the email + provides the transcript as input
- **weekly-status** runs after → reads the updated profile files to draft the Mike Levy email
- This skill is the data layer both depend on
