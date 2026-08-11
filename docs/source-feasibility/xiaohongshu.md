# Xiaohongshu source feasibility

Status: `VISIBLE_BROWSER_ASSISTED_USER_AUTHORIZATION_REQUIRED`

Last reviewed: 2026-08-10 (Asia/Shanghai)

## Decision

The public Xiaohongshu developer surfaces reviewed for this project do not provide a general-purpose API for searching arbitrary public notes or reading their full text and comments. A signed-in browser may technically display this material, but technical visibility is not platform authorization for batch collection.

The current Xiaohongshu User Service Agreement restricts reading, copying, adopting, or statistically processing platform information without written permission and also restricts unauthorized scraping/simulated downloading. A user-authorized visible-browser workflow therefore remains operationally and contractually conditional: it is bounded, user-triggered, read-only, and fail-closed. It is not represented as an official API or platform-approved bulk data service.

Official references:

- User agreement: https://agree.xiaohongshu.com/h5/terms/ZXXY20220331001/-1
- Sharing/open platform: https://agora.xiaohongshu.com/doc

## Implemented paths

`social-browser-plan` plus the interactive browser Agent implements the primary efficiency path:

1. checks an already signed-in visible session using multiple page signals;
2. runs a finite subset of open WBC queries;
3. extracts search links and uses resolved in-memory navigation URLs;
4. opens at most the configured number of detail pages;
5. extracts public title/body/author/date, bounded comments, metrics, and image screenshot tasks;
6. writes only canonical `/explore/<24-hex-note-id>` links and browser candidates;
7. stops on login expiry, CAPTCHA, risk control, denial, or unavailable content.

It never reads cookies/profiles, stores credentials/access tokens, calls hidden APIs, bypasses verification/paywalls, creates a schedule, or publishes a candidate automatically. Full extracted text is confined to ignored `var/` pending original Chinese analysis; the published source layer keeps summaries, short necessary excerpts, and canonical links.

`social-queue-xiaohongshu` remains the no-network fallback. It:

1. generates open-ended WBC search phrases and finite task limits;
2. records external discovery queries and manual platform search links;
3. imports canonical `/explore/<24-hex-note-id>` links and short search snippets from an allowed source;
4. strips `xsec_token` and other transient parameters;
5. deduplicates links and preserves earlier human decisions;
6. tracks `pending_manual_review`, `approved_for_analysis`, `rejected_irrelevant`, or `unavailable`.

The queue always records `content_collected=false`. Browser-extracted candidates instead record `content_collected=true`, `access_mode=authorized_visible_browser`, and `review_status=pending_analysis`; neither format is automatically accepted as engineering evidence.

For durable commercial-scale or unattended full-text/comment collection, obtain Xiaohongshu's written permission or a contracted data interface. Platform unavailability never blocks the offline handbook.
