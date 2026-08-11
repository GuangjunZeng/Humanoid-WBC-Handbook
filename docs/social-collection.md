# 社交平台按需采集

本项目按用户要求执行一次有限更新，不创建定时任务、后台监控或推送。检索范围由开放的 WBC 工程问题本体驱动，七个论文 domain 只是可选分类提示，不是采集边界。

## 三个平台的实现等级

| 平台 | 实现 | 自动化能力 | 必须人工完成 |
|---|---|---|---|
| X | 已登录可见浏览器（默认免费）+ 官方 API（付费可选） | 自动搜索/打开指定帖子、有限展开回复、图文截图分析、规范化和去重；API 模式另支持 recent/all 与增量状态 | 一次性登录；会话失效、验证码或风险控制时处理；审核候选结论 |
| 知乎 | 官方搜索 API + 已登录可见浏览器 | 自动发现候选、打开具体回答/文章、提取正文/有限评论/图片、规范化和去重 | 一次性申请 API 或登录；会话失效、验证码、付费/不可访问时处理 |
| 小红书 | 已登录可见浏览器 + 无网络队列 fallback | 自动搜索、逐帖打开、正文/有限评论提取、图片截图分析、规范化和去重 | 一次性登录；会话失效、验证码或风险控制时处理 |

可见浏览器模式由用户明确触发并使用现有登录会话；它不读取 Cookie/浏览器配置，不提交账号凭据，不调用隐藏接口，不绕过 CAPTCHA/付费墙，也不创建后台任务。技术可见性不等于平台正式数据授权，因此所有运行保持有限、可见、可停止，社区结果仍是待验证候选。

## 统一数据流

```text
config/social-queries.json
        |
        +--> social-browser-plan ------> X/小红书/知乎可见浏览器自动搜索/精读
        |                                     |
        |                                     v
        |                           social-browser-ingest
        |                                     |
        |                                     v
        |                       var/social-browser/candidates.json
        |
        +--> social-collect-x ----------> var/social-candidates/x.json（付费可选）
        |
        +--> social-collect-zhihu ------> var/social-candidates/zhihu.json
                                              |
                                              v
                                   AI 中文提炼 + 候选审核
                                              |
                                              v
                              var/social-captures/<run-id>.json
                                              |
                                              v
                              import-social-captures
                                              |
                                              v
                              data/sources/community.*.json
                                              |
                                              v
                              social-report（每条带原帖/回复链接）
```

`var/` 被 Git 忽略。API 原始候选、增量状态和人工复核队列不会进入发布仓库。

## X/小红书/知乎可见浏览器自动化

用户要求更新时，生成一个有限计划：

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
  --max-posts-per-run 15
```

可见浏览器 Agent 随后自动执行计划，无需用户逐帖打开。原始提取写入 `var/social-browser/raw-<run-id>.json`，再通过：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-browser-ingest \
  var/social-browser/raw-<run-id>.json
```

登录失效、验证码、风险控制、付费或不可访问页面会写成 blocker 并暂停该平台；另一个平台和已完成任务不丢失。每条浏览器候选固定为 `partial_visible`，表示有限运行中到达的可见子集，绝不表示全站或完整评论/回复树。完整浏览器算法、页面选择器、图片处理、原始页契约和恢复流程见 `docs/social-browser-automation.md`。

## X：默认免费可见浏览器采集

按查询搜索相关性排序的 Top 结果并自动打开有限帖子；这更适合回收历史工程经验，而不是只看最新 Post：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-browser-plan \
  --platform x \
  --scope optimization_ik_qp_mpc \
  --max-results-per-query 3 \
  --max-comments-per-post 200 \
  --max-reply-expansions 100 \
  --reply-depth-limit 10 \
  --post-time-budget-seconds 300 \
  --max-posts-per-run 10
```

直接读取一条指定 Post 及有限可见回复：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-browser-plan \
  --platform x \
  --post 'https://x.com/user/status/1234567890' \
  --max-comments-per-post 500 \
  --max-reply-expansions 100 \
  --reply-depth-limit 10 \
  --post-time-budget-seconds 600
```

这两种命令都不需要 `X_BEARER_TOKEN`，也不产生 API 读取费用。可见浏览器 Agent 自动执行搜索、逐帖打开、正文展开和自适应回复展开：只要仍有可见展开控件或滚动后出现新 Post ID 就继续；连续三轮无新增、达到回复/展开/深度/时间护栏，或触发登录与风控才停止。默认每帖最多保存 200 条回复，可显式提高到 500；默认最多 100 次展开操作、10 层、300 秒。它不读取 Cookie、不调用隐藏接口、不绕过登录/验证/风控。结果必须带原帖或精确回复链接以及 `collection_completeness.status=partial_visible`；受保护、删除、折叠、受限或未渲染内容不在覆盖范围内。

## X：官方 API 付费可选模式

先审查查询数和读取上限，不需要凭据也不会联网：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-collect-x \
  --scope optimization_ik_qp_mpc \
  --max-posts-per-query 10 \
  --dry-run \
  --output var/social-candidates/x-plan.json
```

在 X Developer Console 创建 App，将 App-only Bearer Token 只放入本机环境变量：

```bash
export X_BEARER_TOKEN='replace-in-your-shell-only'
```

最近七天按配置搜索，并自动保存每个查询的 `since_id` 与未完成分页游标：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-collect-x \
  --scope optimization_ik_qp_mpc \
  --output var/social-candidates/x.json
```

指定一条帖子或采集一条回复线程：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-collect-x \
  --post 'https://x.com/user/status/1234567890'

PYTHONPATH=src python3 -m wbc_handbook social-collect-x \
  --conversation 'https://x.com/user/status/1234567890'
```

历史回填使用 Full Archive，并先用 `--dry-run` 评估费用：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-collect-x \
  --mode all \
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2026-01-01T00:00:00Z \
  --scope sim_to_sim_and_sim_to_real \
  --max-posts-per-query 100
```

实现会显式请求 `note_tweet`、`article`、`conversation_id`、`referenced_tweets`、作者和媒体字段，并关联引用 Post 的正文与链接。候选原帖链接统一为 `https://x.com/<username>/status/<id>`；同一帖子命中多个 scope 时合并 `matches[]`。

默认状态文件是 `var/social-state/x.json`。如果本轮读取上限先到而 API 仍返回 `next_token`，状态文件会保存游标并保持旧 `since_id`；下一次先读完剩余页，确认窗口完成后才推进高水位。因此有限运行不会永久跳过未读取 Post。只有显式使用 `--no-state` 才关闭该保护和增量更新。

HTTP 429、5xx 和临时网络错误会有限自动重试；最终失败的查询保留原游标并记录 `request_failures`，其他查询仍可完成。程序以非零退出码提示部分失败。完整状态机、重试参数和费用边界见 `docs/x-api-automation.md`。只有用户明确接受付费并配置凭据时才运行本节；否则继续使用上一节的免费有限可见浏览器模式。

官方文档：

- https://docs.x.com/x-api/posts/search/introduction
- https://docs.x.com/x-api/posts/search/integrate/paginate
- https://docs.x.com/x-api/fundamentals/conversation-id
- https://docs.x.com/developer-guidelines
- https://docs.x.com/x-api/getting-started/pricing

## 知乎：官方 API 自动发现

知乎开放平台当前为邀测，需要向 `openplatform@zhihu.com` 说明使用场景和预计调用量，取得 Access Secret 后放入环境变量：

```bash
export ZHIHU_ACCESS_SECRET='replace-in-your-shell-only'
```

先生成不联网的计划：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-collect-zhihu \
  --query '人形机器人 WBC QP 调试' \
  --dry-run \
  --output var/social-candidates/zhihu-plan.json
```

执行一次官方搜索：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-collect-zhihu \
  --scope optimization_ik_qp_mpc \
  --count 10 \
  --output var/social-candidates/zhihu.json
```

默认状态文件 `var/social-state/zhihu.json` 保存每个查询已见的内容 ID，再次运行只输出新候选。`--refresh-known` 可重新输出已见候选。

官方搜索 API 只提供有限摘要、指标、原帖链接和可能存在的精选评论；当前最大 `Count=10`，没有全量分页，不代表完整正文或完整评论。候选 JSON 会明确保存：

```json
{
  "full_text_available": false,
  "canonical_url": "https://www.zhihu.com/question/123/answer/456"
}
```

高价值候选会交给已登录可见浏览器自动精读并保存具体回答/文章链接；用户不需要逐帖打开。删除、登录限制、付费、验证码或不可访问内容不会绕过。官方文档：https://developer.zhihu.com/docs?key=zhihu_search 。

## 小红书：可见浏览器主路径

运行一个有限 scope 示例：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-browser-plan \
  --platform xiaohongshu \
  --scope optimization_ik_qp_mpc \
  --max-results-per-query 3 \
  --max-posts-per-run 6
```

在登录会话有效时，浏览器 Agent 自动完成站内搜索、结果卡去重、逐帖打开、正文和有限评论提取、图片截图队列及 canonical URL 生成。新版搜索结果 `/search_result/<note-id>` 的临时 resolved URL 只用于内存导航；落盘统一为 `/explore/<note-id>`，不保存 `xsec_token` 或临时图片 URL。

真实页面选择器和恢复规则维护在 `docs/social-browser-automation.md`。如果浏览器不可用，可使用无网络 fallback：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-queue-xiaohongshu \
  --output var/social-review/xiaohongshu.json
```

fallback 任务同时包含：

- `external_discovery_query`：交给获准使用的搜索服务或人工搜索；
- `manual_platform_search_url`：用户手动在平台内检查；
- `max_candidates`：有限候选上限；
- `automation_boundary`：明确禁止自动登录、DOM 抽取、正文和评论采集。

外部搜索或人工分享得到链接后，也可准备候选文件：

```json
{
  "candidates": [{
    "url": "https://www.xiaohongshu.com/explore/abcdef0123456789abcdef01",
    "query": "humanoid WBC 调试",
    "scope_id": "open_ended_wbc_field_notes",
    "title": "搜索结果显示标题",
    "snippet": "搜索结果中允许保存的短摘要",
    "discovery_source": "external_search"
  }]
}
```

导入、规范化和去重：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-queue-xiaohongshu \
  --candidates var/xhs-discovered-links.json \
  --output var/social-review/xiaohongshu.json
```

人工 fallback 确认后用决策文件更新状态：

```json
{
  "decisions": [{
    "canonical_url": "https://www.xiaohongshu.com/explore/abcdef0123456789abcdef01",
    "review_status": "approved_for_analysis",
    "review_note": "人工确认与 WBC 实机调试直接相关。"
  }]
}
```

```bash
PYTHONPATH=src python3 -m wbc_handbook social-queue-xiaohongshu \
  --decisions var/xhs-review-decisions.json
```

fallback 状态只能是 `pending_manual_review`、`approved_for_analysis`、`rejected_irrelevant` 或 `unavailable`。队列只存规范化原帖 URL 和有限搜索摘要，`content_collected=false`。浏览器运行的临时原始结果先写入 `var/social-browser/`，图片截图只写入 `var/social-browser/media/`；导入后只保留去令牌、去签名媒体 URL 的候选。候选记录 `content_collected=true`、`access_mode=authorized_visible_browser`、`collection_completeness.status=partial_visible` 和 `review_status=pending_analysis`。两种候选都不会自动发布。

浏览器模式不是官方批量数据接口。若要长期无人值守或商业规模采集，仍应取得小红书书面授权或正式数据服务。官方用户协议：https://agree.xiaohongshu.com/h5/terms/ZXXY20220331001/-1 。

## 中文工程问题提炼与原帖链接

进入 `data/sources/` 前必须由人审查候选并生成中文为主的原创摘要。`engineering_qa` 每张卡片必须包含：

- `question_zh`、`answer_zh`；
- `problem_id`、`problem_title_zh`；
- `bilingual_terms`：一至十二个 `中文（English, ABBR）` 形式的关键术语；
- `answer_status=resolved|partial|unresolved|conflicting`；
- `source_locator`；
- `source_url`；
- `verification_status=community_candidate`；
- `credibility` 与 `verification_refs`，等级只使用 `可信度很高 / 值得参考 / 需要实际验证`。

如果解答来自 X 回复，`source_url` 必须指向那条回复，而不是强制退回线程根帖。知乎应优先使用具体回答 URL。小红书评论无法生成稳定链接时，应保留根帖 URL，并在 `source_locator` 中记录评论作者和显示时间。

原帖只提出问题、没有解答时，保留为 `unresolved`，不得用模型常识补齐。社区观察要成为工程指导，仍需论文、官方文档、源码或 Issue 独立验证。

### 中文优先与双语术语规则

这套规则对中文帖子和英文帖子完全一致：

1. 标题、摘要、工程问题、候选解答、图片分析、限制和安全提示均以中文为主；不得把英文原帖直接拼接成“解读”。
2. 专业术语首次出现使用 `中文（English, ABBR）`，例如 `域随机化（Domain Randomization, DR）`；后文可使用中文或公认缩写。
3. 产品/项目名（如 MuJoCo、Isaac Lab）、函数名、配置键、命令行参数和公式保留原拼写，并在中文句子中解释其作用。
4. 不要求逐句中英对照，也不为了凑双语术语添加与该问题无关的词。`bilingual_terms` 只能列本卡实际涉及的概念。
5. 英文原帖的技术主张先做中文原创转述；必要短引文仍受版权限制，并必须紧邻原帖链接。

导入器会检查 `question_zh` 和 `answer_zh` 的实质中文内容，并根据统一机器人术语表推断
`bilingual_terms`；遇到新术语无法可靠匹配时必须由审阅者显式补写，不能静默用英文占位。
现有数据可用下列命令检查，不会联网：

```bash
PYTHONPATH=src python3 scripts/migrate_social_bilingual_terms.py --data-dir data
```

## 工程问题查询手册

审阅后的候选由 `social-report` 生成
[`content/social-engineering-candidates.md`](../content/social-engineering-candidates.md)。
手册顶部包含当前全部开放 WBC 工程 scope 的覆盖矩阵，并统计每个平台的已审阅来源、
问题数、经验数、三级分布和 `unresolved / conflicting` 项。同一 `problem_id` 下完整聚合所有帖子经验；每张卡继续保留：

- 中文问题与解答，关键术语中英文结合；
- 环境、症状、诊断、原因、尝试、结果、限制和安全提示；
- `resolved / partial / unresolved / conflicting`；
- 根帖或具体回复原始链接与定位描述；
- 可见媒体中的日志、参数、配置或结构图分析；如果像素或图表未完整可读，必须明示限制；
- `community_candidate` 与 `partial_visible`，以及回复展开次数、深度和停止原因。

候选数量和正式入册数量允许不同：所有候选先进入 `data/social-candidate-index.json`。技术相关但
尚未结构化的进入 `technical_pending` 附录，无法判断时也保守保留；广告、营销、离题、重复或
没有工程信息的候选进入 `excluded` 并记录中文原因。排除项不进入主手册，但不会从审计索引静默消失。

按需刷新手册：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-browser-plan --platform x --max-posts-per-run 20
PYTHONPATH=src python3 -m wbc_handbook social-browser-plan --platform zhihu --max-posts-per-run 20
PYTHONPATH=src python3 -m wbc_handbook social-browser-plan --platform xiaohongshu --max-posts-per-run 20
PYTHONPATH=src python3 -m wbc_handbook import-social-captures var/social-browser/reviewed-captures.json --data-dir data
PYTHONPATH=src python3 -m wbc_handbook social-inventory var/social-browser/candidates.json --data-dir data
PYTHONPATH=src python3 -m wbc_handbook social-report --data-dir data --inventory data/social-candidate-index.json --output content/social-engineering-candidates.md --pending-output content/social-engineering-pending
```

这些命令只生成任务、导入已审阅结果和重建手册；实际受登录保护的平台读取仍由用户明确触发的
可见浏览器 Agent 完成，不创建定时或关闭 Codex 后继续运行的后台爬虫。

## 持续扩展范围

`config/social-queries.json` 使用开放 `scopes[]`。发现新的机器人、仿真栈、固件、求解器、传感器或实机故障时，新增稳定 `scope_id` 和少量高信息检索词，不修改七域枚举。必须保留 `open_ended_wbc_field_notes` 作为新兴问题入口。

所有更新均由用户显式触发；不存在 schedule、推送或后台循环。

## 跨运行去重、自进化查询与 GitHub Issues

三平台计划不再默认重放全部固定查询：`var/social-state/discovery.json` 记录每个
`query_signature` 的新增/重复 URL 收益，连续零新增查询指数退避，并按 scope 轮询下一批。
`social-browser-ingest` 同时从正文、标题和评论更新证据化查询前沿；未知术语必须获得两个独立
来源且至少一次出现在标题或技术评论。前沿完整保存并展示 `ready / needs_more_evidence / covered`
全部主题；每轮执行仍受查询和详情页预算约束。完整规则见
[`social-credibility-and-inventory.md`](social-credibility-and-inventory.md)。

GitHub Issues 使用 `config/github-issue-search.json` 的仓库、工程查询和时间窗运行免费 REST
回填，Issue 根链接与 `#issuecomment-<id>` 评论链接均为强制字段。完整算法、命令、状态恢复和
2026-08-10 首轮基线见 [`social-discovery-evolution.md`](social-discovery-evolution.md)。
