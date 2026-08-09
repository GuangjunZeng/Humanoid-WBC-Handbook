# Single-paper interpretation workflow

This workflow reuses only the single-paper reading method selected from the local `paper-daily` skill. Its Scholar Inbox, scheduling, Feishu, messaging, state, and deduplication workflows are not part of this project.

## Required reading pass

1. Read the complete paper, including appendices relevant to implementation; do not rely on the abstract.
2. State the problem, why existing methods are insufficient, and the claimed contribution.
3. Trace the central mechanism as input → processing → output → reason it should help.
4. Explain decisive formulas and inspect at least three useful figures/tables.
5. Identify the most persuasive experiment, its baseline, metric, conditions, and whether the evidence supports the claim.
6. Find public code when available and map at least two paper components to specific files and functions/classes.
7. Separate author-stated limitations from independent engineering judgment.
8. Record robot, simulator, sensors, control rate, action space, training data, compute, and deployment assumptions when reported.
9. For hardware-facing results, document safety conditions, missing safeguards, and sim-to-real uncertainty.

## Output standard

A paper brief should read as a technical story: engineering pain, key idea, mechanism, evidence, implementation map, applicability, failure modes, and actionable—but bounded—takeaways. Every quantitative statement needs a section/figure/table locator. Unknown information stays explicitly unknown.

The completed brief is evidence input; it does not become a reviewed Engineering Claim automatically.
