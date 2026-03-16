# Architecture Decisions

## 2026-03-17

### Decision
Prefer operating workflows and guardrails before adding many third-party skills.

### Why
This improves safety, consistency, and resumability.

### Follow-up
Use the skill-vetting workflow before new skill installation.

---

### Decision
Treat morning brief as manual-first, automation-second.

### Why
Low-quality scheduled briefs become noise quickly.

### Follow-up
Tune content manually before adding cron.

---

### Decision
Use structured handoff/review artifacts for non-trivial delegated work.

### Why
This reduces hidden context and makes future sessions easier to resume.
