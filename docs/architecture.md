# Conceptual architecture

This diagram describes the public demonstration concept, not the private implementation.

```mermaid
flowchart LR
 M[Mission] --> S[Simulated specialists]
 S --> W[Illustrative execution waves]
 W --> R[Human review]
 R --> E[Report export]
```

The original project documentation describes 20–50 scripted specialist roles, ten teams, four waves, visualization and JSON/Markdown exports. These are simulated workflows, not independent model calls. A future live coordinator would need authentication, budgets, cancellation, queues and verified evidence. No private prompts, role roster, integration code or production topology is disclosed.
