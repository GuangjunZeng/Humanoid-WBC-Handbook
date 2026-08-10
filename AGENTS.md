# Repository instructions for paper-library work

When the user explicitly asks to update the paper library or one paper topic, follow `docs/on-demand-paper-update.md` end to end. The update is user-triggered and bounded: do not create a schedule, subscription, push, Feishu/email/message workflow, or unattended background job.

For deep paper briefs, reuse only the single-paper analysis method described in `docs/paper-interpretation.md`. Do not invoke or reproduce Scholar Inbox, daily-digest, recommendation-push, or delivery features from `paper-daily`.

Treat `content/papers/catalog.json` as the canonical coverage inventory and `content/papers/registry.json` as the quality-gated deep-read set. A discovered paper enters as `queued`; promote it to `deep_read` only after the full PDF, official-code status, key figures, Chinese-first brief, safety boundary, and all repository checks pass.

Use primary records for paper identity and official-code status. Do not substitute a third-party reimplementation for author code. Keep classic-field anchors, papers with verified official code, hardware/negative evidence, and topic-role gaps visible in the update report.
