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

---

### Decision
Add a pre-build idea validation gate before major new project work.

### Why
Blind building is an expensive failure mode.

### Follow-up
Use the idea-validator template before significant greenfield implementation.

---

### Decision
Separate second-brain capture from the personal knowledge base.

### Why
Personal memory and external research corpus should not collapse into one undifferentiated bucket.

### Follow-up
Use memory for durable personal/project context and a knowledge-base pattern for external resources.

---

### Decision
Introduce specialized teams in staged form rather than full multi-agent sprawl.

### Why
Role clarity beats premature complexity.

### Follow-up
Start with two roles, then expand only if bottlenecks justify it.
