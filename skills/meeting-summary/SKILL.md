---
name: meeting-summary
description: Produces a formatted, ready-to-send meeting summary email from a Read.AI transcript (or any text transcript). The email leads with key decisions made, followed by a discussion summary calibrated to meeting length, and closes with a follow-up table showing each action item and its owner. Use this skill whenever the user pastes a transcript, attaches a transcript file, or says something like "summarize this meeting", "write up the meeting notes", "send a recap", "create follow-up items from this call", or "draft the meeting summary email". Do NOT wait for the user to ask for a specific format — if a transcript is present and a summary is needed, use this skill.
---

## What this skill produces

A ready-to-copy email with three sections, in this order:

1. **Decisions Made** — the most important output; what was actually decided
2. **What We Covered** — context and discussion that supports the decisions
3. **Follow-up Items** — a table of actions, owners, and due dates

## Input

The user will provide a transcript in one of these forms:
- Pasted text directly in the chat
- A file attachment (Read.AI export, .txt, .md, or similar)

Read.AI transcripts include speaker names and timestamps. Use speaker names to identify attendees. Ignore "Unidentified Speaker" lines for the attendee list but do read them for content.

## Step 1 — Extract the key facts

Before writing anything, identify:

- **Meeting title and date** — usually in the first line of a Read.AI transcript
- **Named attendees** — speakers who appear by name (exclude "Unidentified Speaker")
- **Actual decisions** — things that were agreed upon, confirmed, or resolved; not just topics discussed
- **Discussion topics** — the substance of what was talked about, grouped by theme
- **Follow-up items** — explicit action items; infer owner from context (who said they would do it, or who it was assigned to); capture due dates if mentioned

## Step 2 — Write the email

### Greeting

- 1 attendee (besides the sender): `Hi [Name],`
- 2 attendees: `Hi [Name] and [Name],`
- 3 or more attendees: `Hi all,`

Follow the greeting with one short line: `Thanks for [the time / a productive session / joining today]. Here's a recap.`

### Decisions Made

Lead with this section. Only include real decisions — things that were agreed, confirmed, or resolved. If no actual decisions were made (e.g., a pure status update or discovery call), omit this section entirely rather than padding it with non-decisions.

Each bullet should be a clear, self-contained statement of what was decided — not a topic, not a question answered, but a decision.

### What We Covered

Calibrate the number of bullets to meeting length:
- Under 20 minutes: 2–3 bullets
- 20–45 minutes: 3–5 bullets
- 45–90 minutes: 5–7 bullets
- Over 90 minutes: up to 7 bullets (still summarize; don't pad)

Each bullet covers a distinct topic or theme. If a topic led directly to a decision already captured above, the bullet here should give the context behind it — not repeat the decision.

Group related points into a single bullet rather than fragmenting them. Aim for the level of detail a busy attendee needs to reconstruct the meeting, not a transcript.

### Follow-up Items

Format as a markdown table:

| Item | Owner | Due |
|------|-------|-----|
| [Action, stated as something to be done] | [First name or full name as used in the meeting] | [Date if mentioned, otherwise TBD] |

Rules:
- Every row needs an owner. If ownership wasn't explicit, infer from context (who discussed it, who was asked about it). If truly unclear, use the meeting organizer.
- State each item as an action, not a topic ("Send survey draft" not "Survey").
- If a due date was mentioned, use it. If "this week" was said, use the specific date if known from context, otherwise "This week."
- Order by due date where possible, with TBD items at the bottom.

## Step 3 — Subject line

Format: `Meeting Summary — [Meeting Title], [Date]`

If the transcript doesn't have a clear meeting title, infer one from the content (e.g., "AI Governance Review — Derby" rather than "Meeting Summary — May 12").

## Output format

Present the email as a clean copyable block. Start with the subject line, then the full email body. Do not add commentary above or below unless the user asks a question.

## Edge cases

- **No decisions made:** Skip the Decisions section. Open directly with "What We Covered."
- **No follow-up items:** Skip the table. End after the summary.
- **Very short meeting (under 10 min):** One short paragraph instead of bullets may be more appropriate than forcing a three-section structure.
- **Multiple meetings in one transcript:** Ask the user which meeting to summarize, or summarize each separately if they're clearly distinct.
