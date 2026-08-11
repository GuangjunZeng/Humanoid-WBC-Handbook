# X source feasibility

Status: `FREE_VISIBLE_BROWSER_IMPLEMENTED_LOGIN_REQUIRED; OFFICIAL_API_OPTIONAL_PAID`

Last reviewed: 2026-08-10 (Asia/Shanghai)

## Decision

The project defaults to a user-triggered signed-in visible-browser workflow because the user does not want paid API access. It automates bounded search, status-page navigation, visible post/reply extraction, media screenshot review, canonicalization and deduplication. Every result is explicitly `partial_visible`; it is not represented as all X posts, a complete reply tree, an unattended crawler, or an X-authorized bulk data service.

The official X API v2 adapter remains available only as an explicit paid option. Current X pricing is pay-per-use, and current X terms restrict crawling/scraping without prior written consent. The browser workflow therefore stays visible, finite, user-triggered and fail-closed; it never reads cookies, calls hidden endpoints, bypasses controls, or runs in the background.

Official references:

- Search overview: https://docs.x.com/x-api/posts/search/introduction
- Recent search: https://docs.x.com/x-api/posts/search-recent-posts
- Full archive search: https://docs.x.com/x-api/posts/search-all-posts
- Pagination: https://docs.x.com/x-api/posts/search/integrate/paginate
- Conversation IDs: https://docs.x.com/x-api/fundamentals/conversation-id
- Rate limits: https://docs.x.com/x-api/fundamentals/rate-limits
- Developer guidelines: https://docs.x.com/developer-guidelines
- Pricing: https://docs.x.com/x-api/getting-started/pricing
- Terms of Service: https://x.com/en/tos

## Implemented free path

`social-browser-plan --platform x` supports:

- live-search URLs generated from any configured or ad-hoc WBC query;
- exact status URLs through repeatable `--post` arguments;
- machine-readable `article[data-testid=tweet]`, `tweetText`, author/time, reply permalink, image and video recipes;
- adaptive visible reply expansion until exhaustion or a guardrail (default: up to 100 expansion actions, 200 stored replies, 10 levels and 300 seconds per root Post; configurable to 500 replies/600 seconds);
- exact root/reply canonical URLs, Post IDs and optional parent/conversation IDs;
- visible image/video screenshot paths under ignored `var/social-browser/media/` plus visual-analysis status;
- login, CAPTCHA, rate/risk, protected/deleted and unavailable stop states;
- mandatory `partial_visible` coverage metadata and no hidden network calls.

On 2026-08-10 the available public browser session reached X's login page and the implementation correctly classified its “email or username / continue with Google” signals as `login_required`. Authenticated end-to-end search/reply/media validation remains pending until the user signs in in the same visible browser.

## Optional paid API path

`social-collect-x` supports:

- recent search and paid full-archive search;
- exact post lookup by numeric ID or `x.com`/`twitter.com` status URL;
- root lookup plus `conversation_id:<id>` thread search;
- explicit long-post `note_tweet`, X Article, author, media, metrics, references, edit history, and safety/withheld fields;
- stable `https://x.com/<username>/status/<id>` links;
- post-ID deduplication with multiple query/scope matches;
- per-query `since_id` state under ignored `var/`;
- lossless bounded pagination: unfinished `next_token` windows resume before the
  `since_id` high-water mark advances;
- automatic bounded retry for 429/5xx and temporary network failures using X rate-limit headers;
- query-level partial-failure records that preserve old state and allow other queries to finish;
- finite API error diagnostics for deleted, protected, withheld, or missing Posts;
- no-network `--dry-run` query/cost plans.

The App-only Bearer Token is read from `X_BEARER_TOKEN`. It is never accepted as a CLI value or written to output. Raw API candidates remain under `var/`; the repository publishes only reviewed summaries, short necessary excerpts, Post IDs/links, and derived engineering cards.

The executable commands, cursor state machine, retry behavior, historical backfill and failure recovery are specified in `docs/x-api-automation.md`. It is not invoked by the default free workflow. A real API smoke test still requires the local environment to provide `X_BEARER_TOKEN` and the App to have sufficient credits/endpoint entitlement; synthetic tests never substitute for that credentialed check.

Protected, blocked, deleted, or withheld posts are not bypassed. Before distributing a raw dataset, re-check X's current developer policy, display requirements, compliance/deletion obligations, and resource pricing.
