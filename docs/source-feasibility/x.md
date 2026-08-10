# X source feasibility

Status: `OFFICIAL_API_IMPLEMENTED_CREDENTIAL_REQUIRED`

Last reviewed: 2026-08-10 (Asia/Shanghai)

## Decision

X supports sustainable public-post collection through official X API v2. The project does not script x.com pages because X developer guidance requires official API use for automated data access.

Official references:

- Search overview: https://docs.x.com/x-api/posts/search/introduction
- Recent search: https://docs.x.com/x-api/posts/search-recent-posts
- Full archive search: https://docs.x.com/x-api/posts/search-all-posts
- Conversation IDs: https://docs.x.com/x-api/fundamentals/conversation-id
- Developer guidelines: https://docs.x.com/developer-guidelines
- Pricing: https://docs.x.com/x-api/getting-started/pricing

## Implemented path

`social-collect-x` supports:

- recent search and paid full-archive search;
- exact post lookup by numeric ID or `x.com`/`twitter.com` status URL;
- root lookup plus `conversation_id:<id>` thread search;
- explicit long-post `note_tweet`, X Article, author, media, metrics, references, edit history, and safety/withheld fields;
- stable `https://x.com/<username>/status/<id>` links;
- post-ID deduplication with multiple query/scope matches;
- per-query `since_id` state under ignored `var/`;
- no-network `--dry-run` query/cost plans.

The App-only Bearer Token is read from `X_BEARER_TOKEN`. It is never accepted as a CLI value or written to output. Raw API candidates remain under `var/`; the repository publishes only reviewed summaries, short necessary excerpts, Post IDs/links, and derived engineering cards.

Protected, blocked, deleted, or withheld posts are not bypassed. Before distributing a raw dataset, re-check X's current developer policy, display requirements, compliance/deletion obligations, and resource pricing.
