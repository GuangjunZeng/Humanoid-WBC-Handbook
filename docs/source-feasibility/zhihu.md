# Zhihu source feasibility

Status: `OFFICIAL_API_PLUS_VISIBLE_BROWSER_ENRICHMENT`

Last reviewed: 2026-08-10 (Asia/Shanghai)

## Decision

Zhihu now provides an official invited-preview Data Open Platform. The handbook prefers the official `GET /api/v1/content/zhihu_search` endpoint for discovery, then can use a user-authorized visible signed-in browser for bounded close reading of selected answers/articles. The browser path is not an official bulk-content API and remains subject to the platform terms and page access controls.

Official references:

- Search API documentation: https://developer.zhihu.com/docs?key=zhihu_search
- Platform terms: https://www.zhihu.com/term/zhihu-terms
- Access contact: `openplatform@zhihu.com`

The request uses `Authorization: Bearer <Access Secret>` and `X-Request-Timestamp`. Secrets are read from `ZHIHU_ACCESS_SECRET`, never CLI arguments or repository files.

## Implemented path

`social-collect-zhihu` supports:

- configured or ad-hoc WBC queries;
- at most 10 results per query;
- title, bounded content summary, content type/ID, author, metrics, canonical URL, times, and selected comments when the API returns them;
- canonical question, answer, article, and pin routes;
- per-query seen-ID state under ignored `var/`;
- no-network `--dry-run` planning.

The API candidate contract explicitly records `full_text_available=false`, `complete_comments=false`, and `pagination=false`. API search output is discovery context, not an arbitrary full-answer archive.

`social-browser-plan` supplies the enrichment path. A visible browser Agent can automatically open canonical answer/article candidates, extract bounded public body/comment content, queue image analysis, normalize URLs, and deduplicate them. The user does not open each item individually; intervention is limited to initial/expired login, CAPTCHA, risk control, paid content, or unavailable pages. The workflow never submits credentials/verification codes, reads cookies/profiles, bypasses access controls, creates a schedule, or auto-publishes community conclusions.

The signed-in path was live-validated on 2026-08-10 against Zhihu search, one answer detail page, one long-form article with comments, and one image-bearing article. The maintained selectors and protocol-relative article-link rule are recorded in `docs/social-browser-automation.md`; validation confirms technical operability, not platform authorization for unattended bulk collection.
