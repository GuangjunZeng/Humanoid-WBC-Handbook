# 小红书、知乎与 X 可见浏览器采集规范

本规范定义用户明确要求更新时的自主采集流程。它不创建定时任务；不要求用户逐帖打开。只在首次/过期登录、验证码、风险控制、付费或不可访问页面出现时暂停并请求用户处理。

## 能力边界

浏览器 Agent 可以自动完成：

1. 加载开放式 WBC 查询和已收录 URL；
2. 检查当前页面是否确实登录，而不是只检查头像元素；
3. 搜索、提取结果链接并去重；
4. 打开有限数量的新帖子或回答；
5. 提取标题、正文、作者、日期、首屏/有限展开评论或回复及互动指标；
6. 对图片帖截图并进入视觉分析队列；
7. 删除 `xsec_token`、`utm_*` 等临时导航参数；
8. 生成中文工程问题候选、解答候选和精确原帖链接。

X 的免费模式只能承诺 `partial_visible`：读取当前登录会话可见且在有限展开后到达的帖子、回复和媒体。它不声称覆盖全站、完整回复树、折叠/删除/受保护内容，也不调用页面背后的隐藏接口。

浏览器 Agent 不得读取 Cookie、local storage、浏览器配置、密码或短信验证码；不得调用隐藏接口、绕过 CAPTCHA/风险控制/付费墙；不得关注、点赞、评论、发布或修改账号；不得把候选直接发布为 reviewed claim。

## 一次按需运行

先生成有限任务：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-browser-plan \
  --platform xiaohongshu \
  --platform zhihu \
  --platform x \
  --max-results-per-query 3 \
  --max-comments-per-post 200 \
  --max-reply-expansions 100 \
  --reply-depth-limit 10 \
  --post-time-budget-seconds 300 \
  --max-posts-per-run 15 \
  --output var/social-browser/plan.json
```

也可以只运行一个 scope 或临时查询：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-browser-plan \
  --platform xiaohongshu \
  --scope optimization_ik_qp_mpc \
  --max-posts-per-run 6

PYTHONPATH=src python3 -m wbc_handbook social-browser-plan \
  --platform zhihu \
  --query '人形机器人 WBC QP 不可行 调试'

PYTHONPATH=src python3 -m wbc_handbook social-browser-plan \
  --platform x \
  --query 'humanoid WBC QP infeasible'

PYTHONPATH=src python3 -m wbc_handbook social-browser-plan \
  --platform x \
  --post 'https://x.com/user/status/1234567890' \
  --max-comments-per-post 20
```

之后由可见浏览器 Agent 读取 `plan.json` 并执行任务。执行结果先写入忽略目录：

```text
var/social-browser/raw-<run-id>.json
```

再执行确定性清洗：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-browser-ingest \
  var/social-browser/raw-<run-id>.json \
  --output var/social-browser/candidates.json
```

`candidates.json` 仍是分析候选，不是 `SourceRecord`。Agent 必须先按 `docs/social-collection.md` 提炼中文工程问题、适用环境、原帖解答、限制和原帖链接，再交给 `import-social-captures`。

## 浏览器原始页契约

原始文件只保存在 Git 忽略的 `var/` 下。浏览器导航可以临时使用平台生成的访问参数，但不得把这些参数写入文件；记录规范化 URL 即可。

```json
{
  "run_id": "browser-example",
  "plan_run_id": "browser-plan-example",
  "pages": [
    {
      "task_id": "browser-xiaohongshu-0001",
      "platform": "xiaohongshu",
      "url": "https://www.xiaohongshu.com/explore/abcdef0123456789abcdef01",
      "page_state": "ready",
      "scope_id": "optimization_ik_qp_mpc",
      "domain_hints": ["loco_manipulation_wbc"],
      "query": "人形机器人 WBC QP 调试",
      "title": "页面标题",
      "author_display": "页面公开作者名",
      "published_display": "页面显示日期",
      "body_text": "页面正文，仅保存在 var/ 中等待分析。",
      "selected_comments": [
        {
          "author_display": "评论者公开名",
          "text": "有限、与工程问题直接相关的评论。",
          "published_display": "页面显示时间"
        }
      ],
      "media": [
        {
          "index": 1,
          "kind": "image",
          "alt_text": "图片替代文字",
          "screenshot_path": "var/social-browser/media/post-id-1.png",
          "requires_visual_analysis": true
        }
      ],
      "selector_matches": ["#detail-title", "#detail-desc"]
    }
  ]
}
```

登录、验证或访问失败页也写入 `pages[]`，但只保存最小状态，不保存整页 DOM：

```json
{
  "task_id": "browser-zhihu-0001",
  "platform": "zhihu",
  "url": "https://www.zhihu.com/signin?next=%2F",
  "visible_text": "验证码登录 密码登录"
}
```

`social-browser-ingest` 会把它归为 `login_required` blocker，不会伪造内容候选。

## 小红书执行算法

1. 打开 `/explore`，用多信号确认登录：真实 feed 卡片或个人主页链接存在，且页面不含“登录后查看搜索结果/扫码登录”等文案。
2. 直接打开任务中的 `search_url`。
3. 搜索页同时支持新版 `/search_result/<24-hex-id>` 和旧版 `/explore/<24-hex-id>` 链接。
4. 必须读取 DOM 的 resolved `element.href` 用于本次导航；不能使用可能丢失 `xsec_token` 的原始 `getAttribute('href')`。该 resolved URL 只在内存中使用。
5. 从两种路由提取 note ID；落盘只写 `https://www.xiaohongshu.com/explore/<note-id>`。
6. 依次读取 `#detail-title`、`#detail-desc`、`.username`、`.date`；评论使用 `.comment-item` 等选择器，并以“作者 + 前 80 字”去重。
7. “展开更多/查看更多/更多回复”使用自适应展开：持续操作直到没有可见控件、连续三轮没有新增评论、达到评论上限或单帖时间预算；遇风控立即停止。
8. 图片优先匹配 `.note-slider-img`、`.swiper-slide img` 和 `.note-content img`。对含关键日志、表格、配置或示意图的图片截图并分析，不保存临时 CDN URL。
9. 每次最多打开 `max_posts_per_run` 条详情；发现验证码、风险控制或会话失效立即停止该平台余下任务。

2026-08-10 的真实页面验证结果：登录会话可以返回 20 条 WBC 搜索结果；新版结果卡使用 `/search_result/<id>`，带 resolved 访问参数后会落到 `/explore/<id>`；详情页 `#detail-title`、`#detail-desc`、`.username`、`.date`、评论和图片选择器均可命中。选择器仍必须按每次运行的可见 DOM 复核。

## 知乎执行算法

1. 优先运行官方 `social-collect-zhihu` 获得候选 URL；没有开放平台凭据时，可在已登录可见浏览器中执行计划的有限站内搜索。
2. 搜索结果中的回答链接为 `/question/<question-id>/answer/<answer-id>`；文章链接可能是 `//zhuanlan.zhihu.com/p/<id>`。必须读取 resolved `element.href`，再保存规范化的绝对 HTTPS URL。
3. 具体回答优先保存 `/question/<question-id>/answer/<answer-id>`，文章保存 `zhuanlan.zhihu.com/p/<id>`，不要只保存问题根链接。
4. 回答正文优先匹配 `.RichContent-inner`；文章正文优先匹配 `.Post-RichTextContainer`，再回退到 `.RichText`。作者使用 `.AuthorInfo-name`，时间使用 `.ContentItem-time`。
5. 评论正文优先匹配 `.CommentContent`；`.Comments-container` 只作为评论区存在和总数信号，不得把整个容器错误合并为一条评论。“展开其他 N 条回复”使用自适应展开，直到无新评论或命中计划护栏。
6. 正文图片依次匹配 `.Post-RichTextContainer img`、`.RichContent-inner img`、`img.origin_image` 和 `.RichText img`；排除 `.Avatar`、`.sticker`、广告和相关推荐卡，只把正文内工程图送入截图分析队列。
7. 页面跳转到 `/signin` 或出现“验证码登录/密码登录/登录注册”时，记录 `login_required` 并请求用户登录；不得提交手机号、密码或验证码。
8. 盐选、付费、删除、私密或不可访问内容记录 `access_denied`/`unavailable`，不绕过。

2026-08-10 的真实页面验证结果：登录会话可直接完成站内搜索；查询“人形机器人 WBC 调试”返回 1 个具体回答和 16 篇文章。文章搜索链接为协议相对 URL，resolved `element.href` 可稳定导航到 canonical 文章页。回答页的 `h1.QuestionHeader-title`、`.RichContent-inner`、`.AuthorInfo-name`、`.ContentItem-time` 均命中；文章页的 `h1.Post-Title`、`.Post-RichTextContainer`、`.AuthorInfo-name`、`.ContentItem-time` 均命中。实测评论正文使用 `.CommentContent`，含图文章的正文图片同时命中 `.Post-RichTextContainer img`、`img.origin_image` 和 `img[data-original]`。选择器仍必须在每次运行时按可见 DOM 复核。

## X 免费可见浏览器执行算法

1. 打开 `https://x.com/` 检查真实 feed/Post 卡片。出现 “Join X today”“Sign in to X”“电子邮箱或用户名”或 `/i/flow/login` 时记录 `login_required`；不得代填账号、密码、验证码，也不得读取 Cookie/local storage。
2. 搜索任务默认打开相关性排序的 Top 结果 `https://x.com/search?q=<query>&src=typed_query`，用于发现历史工程经验；结果卡使用 `article[data-testid='tweet']`。从卡片内 `a[href*='/status/']` 或包裹 `time` 的链接读取 resolved URL，规范化为 `https://x.com/<username>/status/<id>` 并按 Post ID 去重。
3. 详情页以 canonical status URL 为根。普通 Post 正文读取 `[data-testid='tweetText']`；若可见“Show more/显示更多”，最多点击一次展开帖子文本，并在成功后显式写入 `full_text_available=true`。X Article 会显示 `/article/<id>` 路由且可能没有 `tweetText`，此时读取根 `article[data-testid='tweet']` 内当前可见的标题、分节、列表和正文，剔除作者栏、互动计数与 Premium 提示后仍引用 status canonical URL；不得把后面的 “Discover more/发现更多” 推荐卡混入正文或回复。
4. 回复仍是 `article[data-testid='tweet']`。排除根 Post 后，分别提取 `[data-testid='tweetText']`、`[data-testid='User-Name']`、`time` 和自身 status permalink；保存 `post_id`、`parent_post_id`、`conversation_id`、`depth` 和精确回复链接。缺少可靠父子关系时留空，不根据页面顺序臆造。
5. “Show more replies/Show replies/显示更多回复/显示回复”不再固定只点三次，而是执行 `until_exhausted_or_guardrail`：每轮点击当前可见展开控件、滚动回复区、重新按 Post ID 去重计数；有新增则继续，连续三轮没有新增才判定稳定。默认最多执行 100 次展开操作、保存 200 条可见回复、追踪 10 层，并给每个根 Post 300 秒；用户可把回复上限提高到 500、时间提高到 600 秒。任何登录、验证码、rate limit 或风险控制都优先停止，且不能通过网络面板或隐藏接口补抓。
6. 搜索成功且确认没有结果时保存 `page_state=empty_results`。这个状态不是访问失败：导入后会为该
   查询记录一次零新增并触发指数退避；登录、验证码、风控等仍按 blocker 保存，不能伪装成空结果。
6. 图片匹配 `div[data-testid='tweetPhoto'] img` 或 `/photo/` 卡片，视频匹配 `data-testid='videoPlayer'`/`videoComponent`。截图只写入 `var/social-browser/media/`，候选保存相对 `screenshot_path`、alt text 和中文视觉摘要，不保存带签名的 CDN 地址。
7. 每条候选固定写入 `collection_completeness.status=partial_visible`、可见回复数、展开次数、到达深度和停止原因。受保护、删除、折叠、受限或未渲染回复不计入，也不得把关注数、点赞数当作技术可信度。
8. 出现 rate limit、错误重载页、验证码、账号验证或访问限制时立即停止 X 剩余任务，保存已完成任务和 blocker，等待用户在同一可见浏览器处理后从未完成 `task_id` 继续。

2026-08-10 的登录态验证同时覆盖了普通 Post、具体回复和 X Article：Article 在 status URL 内呈现 `/article/<id>` 专注模式入口、正文分节与列表，可通过可见根 Article 容器完整读取；测试文章约 1.3 万字符，未使用隐藏接口。

2026-08-10 的公开未登录页验证结果：`https://x.com/` 返回登录入口，包含“电子邮箱或用户名”“使用 Google 继续”等信号，已被分类为 `login_required`，不会误当成可采集 feed。搜索、详情、回复与媒体选择器已经写入机器可读 recipe 和离线测试；真实登录态端到端验证需要用户先在同一可见浏览器完成登录。

## 工程分析与原帖链接

自动提取完成后，无论原帖是中文还是英文，Agent 都以中文为主生成整理结果；关键术语首次出现时采用
`中文（English, ABBR）`，并在 `bilingual_terms[]` 中保存规范形式。例如：
`全身控制（Whole-Body Control, WBC）`、`二次规划（Quadratic Programming, QP）`。
产品名、仓库名、代码标识符、CLI 参数和数学符号保留原文拼写，但不能替代中文解释。随后生成：

- 原帖明确描述的环境、症状、诊断、尝试、有效修复、结果和限制；
- `resolved|partial|unresolved|conflicting` 状态；
- 正文/评论定位；
- 小红书规范化原帖 URL，或知乎具体回答/文章 URL；
- 图片中的关键日志/参数说明；
- `verification_status=community_candidate`；
- 一至十二个与本卡直接相关的 `bilingual_terms`；
- `collection_completeness.status=partial_visible` 及可见回复数量/展开深度；

原帖没有答案时必须保留 `unresolved`；模型不得补写一个看似合理的答案。社区结论只有经过论文、官方文档、源码或 Issue 独立验证后，才可能进入 reviewed engineering claim。

## 失败恢复

| 状态 | 自动动作 | 用户动作 |
|---|---|---|
| `login_required` | 停止该平台余下任务并保存进度 | 在同一浏览器登录后要求继续 |
| `captcha` | 停止，不尝试绕过 | 用户决定是否亲自完成验证 |
| `risk_control` | 停止本轮并降低后续规模 | 等待平台恢复；不要切换隐藏接口 |
| `access_denied` | 跳过并记录 | 决定是否放弃该来源 |
| `unavailable` | 跳过并保留 canonical URL | 无需逐帖处理 |

登录恢复后，从未完成的 `task_id` 继续；不重跑已成功且已去重的帖子。

跨运行查询轮换、帖子/评论驱动的新子话题前沿，以及 GitHub Issues 的大规模增量搜索不由页面
选择器实现，统一遵循 [`social-discovery-evolution.md`](social-discovery-evolution.md)。浏览器执行
时必须把任务中的 `query_signature`、`origin` 和 `frontier_topic_id` 原样带回原始页，以便收益
账本和延伸话题保持可追溯。
