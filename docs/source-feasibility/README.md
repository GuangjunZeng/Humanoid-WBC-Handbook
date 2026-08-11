# Information-source feasibility gate

Date: 2026-08-10 (Asia/Shanghai)

Decision: `CONDITIONAL GO`

The handbook can be built reproducibly from GitHub, arXiv, official documentation, and public project pages. Community platforms add operational context but are never required for builds, tests, or published conclusions.

| Source class | Status | Supported acquisition | Runtime role |
|---|---|---|---|
| GitHub repositories, Issues, Releases, commits | `PASS` | Public GitHub application/API or explicit URL import | Core evidence |
| arXiv papers | `PASS` | Atom metadata, HTML, PDF | Core evidence |
| Official docs and project pages | `PASS` | Public HTTPS pages | Core evidence |
| Hugging Face pages | `CONDITIONAL_PASS` | Public web pages; API is not assumed | Supplemental/core when independently reachable |
| Bilibili | `CONDITIONAL_PASS` | Public discovery and video metadata | Supplemental context |
| X | `FREE_VISIBLE_BROWSER_IMPLEMENTED_LOGIN_REQUIRED` | Default bounded signed-in browser search/detail/replies/media with `partial_visible`; official API remains paid opt-in | Supplemental context; free mode needs login and is never complete coverage |
| Zhihu | `OFFICIAL_API_PLUS_VISIBLE_BROWSER_ENRICHMENT` | Official invited-preview search API; bounded signed-in browser enrichment after user authorization | Supplemental engineering context |
| Xiaohongshu | `VISIBLE_BROWSER_ASSISTED_USER_AUTHORIZATION_REQUIRED` | Bounded signed-in browser search/detail extraction; no-network queue fallback | Supplemental engineering context; not a dependency |
| Discord and gated communities | `SKIPPED_OPTIONAL` | Authorized membership plus manual import | Not a dependency |

## Global collection rules

- Respect authentication, robots directives, rate limits, copyright, quotation limits, and platform terms.
- Never collect cookies/profiles, call hidden/private endpoints, automate credentials, or bypass CAPTCHA, risk controls, paywalls, or membership gates.
- A visible-browser run requires an explicit user request, an already signed-in session, finite limits, and fail-closed stop states. It is not a background crawler and does not itself establish platform permission.
- Preserve canonical URL, access mode, capture time, author/publisher metadata, license when known, and an integrity hash for imported material.
- Store concise original summaries and only short necessary excerpts. Do not redistribute restricted full text, video, images, or bulk comments.
- Treat views, likes, stars, and comment counts as attention signals only. They do not increase technical evidence strength.
- Require at least one stronger independent source before converting a community observation into engineering guidance.

## Reproducible acceptance boundary

Offline tests use repository-owned synthetic fixtures. Network adapters are optional and must fail closed with actionable diagnostics. A clean checkout must still be able to import a manual record, normalize it, validate an Engineering Claim, build the local index, and answer a question with citations.

Platform-specific evidence and restrictions are recorded in this directory. The executable on-demand workflow is defined in `docs/social-collection.md`; it does not change the rule that platform access failures must fail closed and never block the offline handbook.
