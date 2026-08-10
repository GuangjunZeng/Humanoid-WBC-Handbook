# Xiaohongshu source feasibility

Status: `MANUAL_REVIEW_ONLY_UNLESS_WRITTEN_PERMISSION`

Last reviewed: 2026-08-10 (Asia/Shanghai)

## Decision

The public Xiaohongshu developer surfaces reviewed for this project do not provide a general-purpose API for searching arbitrary public notes or reading their full text and comments. A signed-in browser may technically display this material, but technical visibility is not platform authorization for batch collection.

The current Xiaohongshu User Service Agreement restricts reading, copying, adopting, or statistically processing platform information without written permission and also restricts unauthorized scraping/simulated downloading. Therefore this project does not implement Playwright/DOM extraction, cookie reuse, hidden API calls, signature emulation, CAPTCHA handling, or background collection.

Official references:

- User agreement: https://agree.xiaohongshu.com/h5/terms/ZXXY20220331001/-1
- Sharing/open platform: https://agora.xiaohongshu.com/doc

## Implemented path

`social-queue-xiaohongshu` performs no network access. It:

1. generates open-ended WBC search phrases and finite task limits;
2. records external discovery queries and manual platform search links;
3. imports canonical `/explore/<24-hex-note-id>` links and short search snippets from an allowed source;
4. strips `xsec_token` and other transient parameters;
5. deduplicates links and preserves earlier human decisions;
6. tracks `pending_manual_review`, `approved_for_analysis`, `rejected_irrelevant`, or `unavailable`.

The queue always records `content_collected=false`. An approved candidate may be summarized only after a human selects the post and supplies or opens material they are permitted to use. Store original Chinese summaries, short necessary excerpts, and the canonical post link—not a platform archive.

Full-text/comment automation requires Xiaohongshu's written permission or a contracted data interface. Platform unavailability never blocks the offline handbook.
