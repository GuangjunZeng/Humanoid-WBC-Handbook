# Xiaohongshu source feasibility

Status: `PENDING_AUTHORIZED_SESSION`

Last probed: 2026-08-10 (Asia/Shanghai)

## Decision summary

Xiaohongshu can only be an optional, user-initiated evidence source. The project must not ship an unattended crawler, private/hidden API client, cookie reader, CAPTCHA workaround, or background search job for this platform.

Anonymous web access loads the search interface but hides results behind `登录后查看搜索结果`. External search did not reliably discover relevant note URLs. The official `robots.txt` declares `User-agent: *` and `Disallow: /`.

The platform passes only after a user-authorized browser session proves that a relevant result, its note body, and its comments can be read through the visible DOM. Until then it is not a usable collector.

## Permitted acquisition path

1. The user explicitly opens a visible browser session and signs in.
2. The user or operator initiates a small, problem-specific search from the handbook ontology.
3. The tool reads only information already visible in the authorized page DOM.
4. A human selects relevant notes; there is no unattended pagination or bulk traversal.
5. The project stores normalized metadata, a concise original summary, claim candidates, short necessary excerpts, and the canonical source link.
6. Full post text, images, video, and bulk comments are not republished in the repository.

## Login-session acceptance test

Run these checks one at a time in the visible signed-in browser:

1. Search `G1 motion tracking 抖` and confirm at least one result card is visible, or record a valid zero-result outcome.
2. Search `Isaac Lab 人形机器人 NaN` and confirm the query can be changed without a login/CAPTCHA loop.
3. Open one technically relevant note and record whether the following are visible:
   - canonical note URL or stable note identifier;
   - title/body text;
   - author display name and profile link;
   - publication/update time when present;
   - hashtags/topics;
   - displayed attention counts;
   - comment text, author, timestamp, likes, and reply context when present.
4. Refresh or reopen the canonical URL once to test stability.
5. Stop immediately if the platform presents CAPTCHA, unusual-traffic, or risk-control warnings.

Pass condition: result discovery plus one relevant note and its available comments can be read without bypassing controls. A zero-result query does not fail the platform if search and note access are otherwise proven with another ontology query.

## Normalized output boundary

| Field | Required | Notes |
|---|---:|---|
| `platform` | yes | Constant `xiaohongshu` |
| `canonical_url` | yes | Keep the user-visible source URL |
| `captured_at` | yes | ISO 8601 timestamp with timezone |
| `query` | yes | Exact ontology-derived search phrase |
| `title` | when visible | Do not infer a missing title |
| `author_display` | when visible | Public display value only |
| `published_at` | when visible | Preserve uncertainty if relative |
| `attention` | optional | Prioritization only, never evidence strength |
| `summary` | yes | Original concise summary, not copied body text |
| `excerpt` | optional | Short, necessary, attributed excerpt only |
| `comment_context` | optional | Selected engineering context, not bulk comments |
| `access_mode` | yes | `authorized_visible_browser` or `manual_import` |

## Fallback

If authorized browser reading remains unavailable, use `manual_import`: the user supplies a URL plus selected text or screenshots they are permitted to use. The handbook records provenance and summarizes the evidence; it does not attempt to fetch the source automatically.

Xiaohongshu must never be required for the offline test suite, reproducible build, or a troubleshooting conclusion. A claim needs stronger independent evidence before publication as guidance.

## Probe evidence

- Anonymous in-app browser search: interface visible; results blocked by login.
- External web search: no dependable relevant note discovery for the tested humanoid/WBC queries.
- Official `https://www.xiaohongshu.com/robots.txt`: generic automated crawling disallowed.
- Chrome/external browser control: unavailable in the current environment.
