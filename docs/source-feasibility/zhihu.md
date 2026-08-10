# Zhihu source feasibility

Status: `OFFICIAL_API_IMPLEMENTED_ACCESS_APPROVAL_REQUIRED`

Last reviewed: 2026-08-10 (Asia/Shanghai)

## Decision

Zhihu now provides an official invited-preview Data Open Platform. The handbook uses only the official `GET /api/v1/content/zhihu_search` endpoint for automated discovery; it does not automate zhihu.com pages.

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

The candidate contract explicitly records `full_text_available=false`, `complete_comments=false`, and `pagination=false`. API search output is discovery context, not an arbitrary full-answer archive. A human selects candidates for any later close reading; deleted, private, paid, login-blocked, or unavailable material is not bypassed.
