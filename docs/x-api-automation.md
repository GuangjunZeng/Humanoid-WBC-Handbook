# X 官方 API 按需全自动采集

这是显式选择付费官方 API 时使用的可选流程，不是项目默认 X 路径。默认免费路径见 `docs/social-browser-automation.md`。本流程在用户明确要求更新时运行一次，不创建定时任务。除首次申请开发者账号、购买读取额度并设置 `X_BEARER_TOKEN` 外，搜索、逐页读取、线程恢复、增量去重、媒体关联、错误重试和候选生成均由 `social-collect-x` 自动完成。

## 前置条件

1. 在 X Developer Console 创建 Project/App，并取得可读取公开 Post 的 App-only Bearer Token。
2. 在本机 shell 设置环境变量，不把 Token 写入命令、配置、日志或仓库：

```bash
export X_BEARER_TOKEN='set-this-only-in-your-local-shell'
```

3. 先用 `--dry-run` 查看查询数、端点、读取上限和费用边界。X 目前按读取资源计费，实际价格以 Developer Console 为准。

## 常规自动更新

```bash
PYTHONPATH=src python3 -m wbc_handbook social-collect-x \
  --max-posts-per-query 30 \
  --max-pages 3 \
  --output var/social-candidates/x.json
```

默认使用 recent search、`sort_order=recency` 和 `var/social-state/x.json`。再次运行时会自动使用每个查询的高水位 `since_id`，只处理新 Post。

状态文件按查询签名合并更新；只运行一个 `--scope` 不会删除其他未选 scope 的高水位或分页游标。

限定工程 scope：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-collect-x \
  --scope optimization_ik_qp_mpc \
  --scope communication_and_realtime
```

指定 Post 或回复线程：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-collect-x \
  --post 'https://x.com/user/status/1234567890'

PYTHONPATH=src python3 -m wbc_handbook social-collect-x \
  --conversation 'https://x.com/user/status/1234567890'
```

`--conversation` 会先查根帖，再以 `conversation_id:<id>` 搜索回复；每条候选保留自己的精确 `https://x.com/<username>/status/<id>` 链接。默认 recent 模式只覆盖当前 recent 时间窗中的回复；要恢复完整历史线程，应显式使用 `--mode all`，并确保 App 具有 full-archive 权限和读取额度。

## 无丢失分页与恢复

X recent search 每页最少 10 条、最多 100 条；full archive 每页最多 500 条。实现始终消费完整 API 页，因此当用户设置的单次上限小于 10 时，实际读取可能达到 10 条，但不会截断一页并永久漏帖。

如果本轮因 `max_pages` 或 `max_posts_per_query` 停止且响应仍有 `next_token`：

1. 把 `next_token`、原始 `since_id` 和本窗口首屏 `newest_id` 写入忽略目录下的状态文件；
2. 不推进正式 `newest_id` 高水位；
3. 下次运行先恢复未完成页；
4. 直到窗口没有下一页后，才把高水位推进到窗口首屏的 `newest_id`；
5. 再下一次运行才用该值作为新的 `since_id`。

这样即使一次更新被人为限制为少量页面，也不会跳过处在未读取页面中的 Post。不同 `mode`、起止时间和排序方式使用不同状态键，历史回填不会污染日常 recent 增量状态。

## 历史回填

```bash
PYTHONPATH=src python3 -m wbc_handbook social-collect-x \
  --mode all \
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2026-01-01T00:00:00Z \
  --max-posts-per-query 500 \
  --max-pages 10
```

Full archive 是否可用取决于当前 App 权限和付费方案。先运行同参数的 `--dry-run`，但 dry run 不代表账号已经获得端点授权。明确给出 `start_time` 和 `end_time` 的窗口在完整读取后会标记 `window_complete=true`；再次运行相同窗口时不会重复付费读取。只有明确需要重新抓取时才使用 `--no-state`。

## 自动重试和部分失败

- HTTP `429`、`500`、`502`、`503`、`504` 与临时网络错误默认最多重试三次；
- Full archive 请求主动保持至少 1 秒间隔，符合当前官方端点频率上限；
- 优先使用 `Retry-After` 或 `x-rate-limit-reset`，单次等待最多 30 秒；
- 可用 `--max-retries` 和 `--max-retry-wait-seconds` 调整，最大等待限制为 60 秒；
- `401/403` 不重试，通常表示 Token、App 权限、额度或端点授权问题；
- 某个查询最终失败时，程序保留它原来的高水位/分页游标，继续记录其他查询结果，并以非零退出码报告 `request_failures`；
- API 对删除、受保护或不存在 Post 返回的局部 `errors[]` 会转成有限诊断，不伪造候选。

## 候选内容

候选会保存：完整 `note_tweet` 文本、X Article 对象、作者、时间、语言、conversation/reply/reference 关系、引用 Post 的正文和链接、编辑历史、互动指标，以及照片/视频/GIF 的 alt text、预览、尺寸和 variants。含媒体的候选标记 `visual_analysis_pending=true`，供后续工程截图/图表解读；相同 Post 命中多个查询时合并 `matches[]`。

所有原始结果和游标只进入 Git 忽略的 `var/`。Bearer Token 不会序列化。候选仍需按 `docs/social-collection.md` 提炼为中文工程问题/解答，并保留原帖或精确回复链接；社区候选不会自动升级为 reviewed engineering claim。

## 官方依据

- Recent search：https://docs.x.com/x-api/posts/search-recent-posts
- Full archive search：https://docs.x.com/x-api/posts/search-all-posts
- Pagination：https://docs.x.com/x-api/posts/search/integrate/paginate
- Post lookup：https://docs.x.com/x-api/posts/get-posts-by-ids
- Fields and expansions：https://docs.x.com/x-api/fundamentals/data-dictionary
- Rate limits：https://docs.x.com/x-api/fundamentals/rate-limits
- Pricing：https://docs.x.com/x-api/getting-started/pricing
- Batch compliance：https://docs.x.com/x-api/compliance/batch-compliance/introduction
