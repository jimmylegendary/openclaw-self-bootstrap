# Build Note

## Goal link
- Help the user validate lightweight lead tracking before buying a full CRM.

## What was built
- A local single-page prototype for importing CSV leads and tagging them by status.

## Why this was chosen
- It matches an active goal.
- It can be reviewed quickly in the morning.
- It stays local and does not require external APIs.

## Files / paths
- `projects/overnight/2026-03-17-lead-tracker-prototype/`
- `projects/overnight/2026-03-17-lead-tracker-prototype/BUILD_NOTE.md`

## How to run or test
1. `cd projects/overnight/2026-03-17-lead-tracker-prototype`
2. Open `index.html` in a browser.
3. Load `sample-leads.csv` and try moving records between statuses.

## Current status
- done: import, local persistence, basic status board, sample data
- unfinished: duplicate detection, export, mobile layout polish

## Suggested next move
- If the user likes the workflow, turn it into a small local app with a saved project list and CSV export.
