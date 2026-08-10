# 社交平台按需采集

本项目按用户要求执行一次有限更新，不创建定时任务、后台监控或推送。检索范围由开放的 WBC 工程问题本体驱动，七个论文 domain 只是可选分类提示，不是采集边界。

## 三个平台的实现等级

| 平台 | 实现 | 自动化能力 | 必须人工完成 |
|---|---|---|---|
| X | 官方 X API v2 | 搜索、指定帖子、线程、媒体、指标、recent/all、增量状态 | 申请开发者凭据；审核候选结论 |
| 知乎 | 官方知乎数据开放平台搜索 API | 最多 10 条/查询的标题、摘要、作者、指标和原帖 URL；已见去重 | 申请邀测；选择是否精读原帖 |
| 小红书 | 无网络人工复核队列 | 生成查询、导入链接/搜索摘要、规范化、去重、状态管理 | 搜索/打开原帖、确认相关性、提供获准分析的内容 |

技术上能在网页中读取内容，不等于获得批量自动采集授权。X 和知乎只调用官方 API；小红书适配器不会登录平台、读取 DOM、复用 Cookie 或抓取正文/评论。

## 统一数据流

```text
config/social-queries.json
        |
        +--> social-collect-x ----------> var/social-candidates/x.json
        |
        +--> social-collect-zhihu ------> var/social-candidates/zhihu.json
        |
        +--> social-queue-xiaohongshu -> var/social-review/xiaohongshu.json
                                              |
                                              v
                              人工选择 + AI 中文提炼
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

## X：官方 API 全自动采集

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

最近七天按配置搜索，并自动保存每个查询的 `since_id`：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-collect-x \
  --scope optimization_ik_qp_mpc \
  --output var/social-candidates/x.json
```

指定一条帖子或恢复一条回复线程：

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

实现会显式请求 `note_tweet`、`article`、`conversation_id`、`referenced_tweets`、作者和媒体字段。候选原帖链接统一为 `https://x.com/<username>/status/<id>`；同一帖子命中多个 scope 时合并 `matches[]`。

默认状态文件是 `var/social-state/x.json`。只有显式使用 `--no-state` 才关闭增量更新。网页浏览只可用于人工复核，不是批量采集后端。

官方文档：

- https://docs.x.com/x-api/posts/search/introduction
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

硬边界：官方搜索 API 只提供有限摘要、指标、原帖链接和可能存在的精选评论；当前最大 `Count=10`，没有全量分页，不代表完整正文或完整评论。候选 JSON 会明确保存：

```json
{
  "full_text_available": false,
  "canonical_url": "https://www.zhihu.com/question/123/answer/456"
}
```

需要精读时，由人工选择原帖；删除、登录限制、付费或不可访问内容不会绕过。官方文档：https://developer.zhihu.com/docs?key=zhihu_search 。

## 小红书：人工在环候选队列

生成完整 WBC 检索计划和空队列；命令不联网：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-queue-xiaohongshu \
  --output var/social-review/xiaohongshu.json
```

每个任务同时包含：

- `external_discovery_query`：交给获准使用的搜索服务或人工搜索；
- `manual_platform_search_url`：用户手动在平台内检查；
- `max_candidates`：有限候选上限；
- `automation_boundary`：明确禁止自动登录、DOM 抽取、正文和评论采集。

外部搜索或人工分享得到链接后，准备候选文件：

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

人工确认后用决策文件更新状态：

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

状态只能是 `pending_manual_review`、`approved_for_analysis`、`rejected_irrelevant` 或 `unavailable`。队列只存规范化原帖 URL 和有限搜索摘要，`content_collected=false`；短期 `xsec_token` 会被删除。

如需批量自动获取笔记正文/评论，必须先取得小红书书面授权或正式数据接口。官方用户协议：https://agree.xiaohongshu.com/h5/terms/ZXXY20220331001/-1 。

## 中文工程问题提炼与原帖链接

进入 `data/sources/` 前必须由人审查候选并生成中文为主的原创摘要。`engineering_qa` 每张卡片必须包含：

- `question_zh`、`answer_zh`；
- `answer_status=resolved|partial|unresolved|conflicting`；
- `source_locator`；
- `source_url`；
- `verification_status=community_candidate`。

如果解答来自 X 回复，`source_url` 必须指向那条回复，而不是强制退回线程根帖。知乎应优先使用具体回答 URL。小红书评论无法生成稳定链接时，应保留根帖 URL，并在 `source_locator` 中记录评论作者和显示时间。

原帖只提出问题、没有解答时，保留为 `unresolved`，不得用模型常识补齐。社区观察要成为工程指导，仍需论文、官方文档、源码或 Issue 独立验证。

## 持续扩展范围

`config/social-queries.json` 使用开放 `scopes[]`。发现新的机器人、仿真栈、固件、求解器、传感器或实机故障时，新增稳定 `scope_id` 和少量高信息检索词，不修改七域枚举。必须保留 `open_ended_wbc_field_notes` 作为新兴问题入口。

所有更新均由用户显式触发；不存在 schedule、推送或后台循环。
