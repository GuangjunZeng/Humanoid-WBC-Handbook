# WBC 社交与 GitHub Issues 增量发现机制

本机制只在用户明确要求更新时运行，不创建定时任务、后台监控或推送。目标是长期扩大知乎、
小红书、X 和 GitHub Issues 的工程经验覆盖，同时避免每轮机械重复同一批搜索。

## 1. 不重复不是“永不再看”

完全禁止重复会漏掉后续评论、修复状态和正文更新，因此项目采用五层身份与刷新规则：

1. `query_signature`：`platform + scope_id + 规范化查询` 的稳定摘要，阻止同轮重复查询；
2. `canonical_url`：去除 X/小红书临时参数、知乎搜索参数和 GitHub 跟踪参数后的根来源键；
3. `content_sha256` / `issue_updated_at`：正文没变则跳过，Issue 更新或新评论时允许重新进入候选；
4. 评论/回复链接：X 回复保留自己的 status URL，GitHub 评论保留
   `#issuecomment-<id>`，小红书无法精确链接时保留根帖和评论定位；
5. `matches[]`：同一来源命中多个 scope/查询时只存一份正文，但保留全部发现路径。

浏览器查询收益账本位于 `var/social-state/discovery.json`。每次成功任务记录新增 URL、重复 URL、
阻断状态和连续零新增次数。零新增查询采用指数退避，基础间隔默认 24 小时、最多 30 天；这只是
下一次用户触发运行时的选择规则，不会自动唤醒任务。`--refresh-queries` 可由用户显式覆盖。
搜索页正常完成但没有候选时，执行器必须写入 `page_state=empty_results`；它会作为“已完成、零新增”
进入退避账本，而不是被误记成 blocker。登录、验证码、风控和不可访问仍是 blocker，不会增加
零新增次数；没有执行回执的计划任务也不会被假定为已搜索。

计划器按“从未搜索 → 上轮新增证据 → 到期刷新”排序，并按 `scope_id` 轮询，避免一个宽泛主题耗尽整个平台预算。
默认每个平台只选 8 个查询，其余写入计划的 `query_selection.skipped[]`，不会丢失。

## 2. 从帖子和评论延伸 WBC 子话题

`social-evolve-queries` 同时读取正文、标题和评论，并把每个技术实体连同以下证据写入
`var/social-state/query-frontier.json`：

- 根帖/Issue URL；
- 精确回复或 `#issuecomment-...` URL（存在时）；
- `正文 / 标题 / 评论 @作者` 定位；
- 出现该术语的短上下文；
- 原 scope、平台、首次和最近发现时间。

为避免搜索自我污染，自动晋级遵守以下护栏：

- 受控技术实体（例如 Pinocchio、OCS2、Isaac Lab、qpOASES、EtherCAT）有一个来源即可激活；
- 未知代码标识符/缩写必须至少出现在两个独立根 URL，且至少一次位于标题或技术评论；
- 已被固定查询覆盖的术语标记为 `covered`，继续展示但默认不生成重复查询；
- 达到门槛的术语标记为 `ready`；证据尚少的标记为 `needs_more_evidence`，两者都完整展示；
- 主题数和每主题根来源数不做用户可见截断；执行预算只作用于单轮计划，不删除或隐藏主题；
- 下一轮仍受每个平台查询预算、scope 轮询和收益账本约束；不会直接改写固定配置或无限递归。

生成的扩展查询仍以 WBC 为锚点：中文平台使用
`人形机器人 WBC <术语> 调试`，X 使用英文调试查询，GitHub 使用仓库内 Issue 查询。每条扩展
始终可追溯到触发它的原帖或评论。

完整报告由 `social-frontier-report` 生成到 `content/social-query-frontier.md`。使用者可从中选择
任意 `topic_id`，再运行 `social-browser-plan --topic <topic_id>` 或
`github-issue-plan --topic <topic_id>` 定向执行。

## 3. 三个平台的扩充流程

生成低重复计划：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-browser-plan \
  --platform x --platform zhihu --platform xiaohongshu \
  --max-queries-per-platform 8 \
  --max-results-per-query 3 \
  --max-posts-per-run 20 \
  --state var/social-state/discovery.json \
  --frontier var/social-state/query-frontier.json \
  --output var/social-browser/plan.json
```

由当前已登录可见浏览器执行计划后，导入原始页并同时更新收益账本与查询前沿：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-browser-ingest \
  var/social-browser/raw-<run-id>.json \
  --plan var/social-browser/plan.json \
  --state var/social-state/discovery.json \
  --frontier var/social-state/query-frontier.json \
  --output var/social-browser/candidates-<run-id>.json
```

计划中的 `known_canonical_urls` 同时来自已发布 `data/sources/` 和跨运行账本。因此浏览器搜索页
可以直接略过旧 URL，把有限详情页预算留给新来源；已知来源只有在用户显式刷新或后续更新检查时
重新打开。登录、验证码、风控和不可访问页面仍形成 blocker，已完成任务不会重跑。

## 4. GitHub Issues 超大规模搜索

GitHub 使用文档化 REST Search/Issue Comments API；`GITHUB_TOKEN` 是可选的免费额度提升，不是
付费 API，也不会写入仓库。匿名模式可运行但速率低，大规模回填建议使用免费 GitHub token。

`config/github-issue-search.json` 当前覆盖 34 个 WBC 相关仓库、23 组工程查询和 6 个历史/滚动
时间窗。计划按“查询 × 相关仓库批次 × 时间窗”拆分任务，以绕开 GitHub 单个搜索最多返回
1000 条的上限。每个任务默认最多 10 页 × 100 条，并保存未完成 `next_page`；全局预算即使在
某页中途耗尽，也会从同一页恢复，已见 canonical URL 会自动跳过，因此不会丢掉页尾。

```bash
PYTHONPATH=src python3 -m wbc_handbook github-issue-plan \
  --config config/github-issue-search.json \
  --state var/social-state/github-issues.json \
  --frontier var/social-state/query-frontier.json \
  --max-tasks-per-run 40 \
  --output var/github-issues/plan.json

PYTHONPATH=src python3 -m wbc_handbook github-issue-collect \
  --plan var/github-issues/plan.json \
  --state var/social-state/github-issues.json \
  --max-issues-per-run 1000 \
  --max-comments-per-issue 100 \
  --output var/github-issues/candidates.json
```

当 Codex 已连接 GitHub App 时，可以用连接器执行同一批搜索和评论读取，再确定性合并导出：

```bash
PYTHONPATH=src python3 -m wbc_handbook github-issue-ingest-connector \
  var/github-issues/connector-search-a.json \
  var/github-issues/connector-search-b.json \
  --comments var/github-issues/connector-comments.json \
  --output var/github-issues/candidates.json
```

两种路径都以 `https://github.com/<owner>/<repo>/issues/<number>` 去重；Issue 正文改变或
`updated_at` 前进时允许刷新。评论答案必须保存精确 `#issuecomment-<id>`，不能只指向仓库首页。

## 5. 候选、审阅与发布边界

大量原始发现结果先留在 Git 忽略的 `var/`；最小 URL/标题/查询元数据合并到可提交的
`data/social-candidate-index.json`，状态为 `reviewed / technical_pending / excluded`。它们只有经过以下步骤才能进入手册：

1. 中文原创提炼，关键术语使用 `中文（English, ABBR）`；
2. 区分环境、症状、诊断、原因、尝试、修复、结果、限制和安全边界；
3. 标记 `resolved / partial / unresolved / conflicting`；
4. 解答来自评论时使用精确评论链接；
5. 图片没有逐像素确认时明确写出限制；
6. 计算经验级与问题级三级可信度，人工调整必须写中文理由；
7. 运行 `import-social-captures`、`social-inventory`、`social-report` 和仓库验证。

GitHub Issue 入库为 `kind=issue`、`verification_status=issue_candidate`；是否能作为正式工程结论的
独立证据，还要看回复者身份、复现、修复 PR/版本和与源码/文档的一致性。搜索数量本身不等于
证据强度。完整规则见 [`social-credibility-and-inventory.md`](social-credibility-and-inventory.md)。

## 6. 2026-08-10 首轮基线

- GitHub 连接器执行 32 个宽窄查询命中 1076 次，跨查询规范化后为 1067 个独立 Issue；
- 30 个高相关 Issue 补充了 161 条评论，全部保留精确评论链接；
- 9 个证据链清晰的 Issue 已完成中文审阅并进入候选手册；
- 查询前沿在全量迁移后提取 3,568 个去重主题和 8,061 条触发证据：168 个 `ready`、3,330 个 `needs_more_evidence`、70 个 `covered`；
- 最小候选索引包含 1,127 个唯一 URL：56 个 `reviewed`、1,071 个 `technical_pending`；
- 三个社交平台继续使用可见浏览器模式，并在下一次用户触发时按新账本轮询扩充。

上述数字是一次有限运行的基线，不代表 GitHub 或三个平台的全部内容。

## 7. 2026-08-11 高质量经验扩充

- 新增核验 9 个来源、提炼 20 张工程经验卡，主手册由 64 张增至 84 张；
- 新增问题覆盖奖励局部最优、Humanoid-Gym 依赖与 Sim2Sim、50/250 Hz 遥操作队列、CANopen 周期丢帧、legged_control 真机适配、G1 首次上机，以及 3 个 GitHub 数值/接口案例；
- 5 张卡达到 `可信度很高`，均提供官方源码或已合并 PR 的精确核验引用；演示数据、未合并 PR、未闭环 Issue 和评论争议继续显示为 `值得参考` 或 `需要实际验证`；
- 当前最小候选索引为 1,131 个唯一 URL：65 个 `reviewed`、1,066 个 `technical_pending`、0 个 `excluded`；
- 查询前沿为 3,577 个去重主题和 8,080 条触发证据：168 个 `ready`、3,339 个 `needs_more_evidence`、70 个 `covered`；
- 小红书本轮搜索与详情页均触发登录/App 可见性限制，没有把不可读正文伪造成经验卡；已完成的知乎、X 与 GitHub 结果正常保留。

这些数字仍是用户触发的一次有限扩充。下一轮从完整待整理索引和查询前沿继续轮转，不以本轮数量作为上限。

## 8. 2026-08-11 原帖证据优先扩充

- 从 `technical_pending` 中逐条读取 13 个 GitHub Issue 的正文、全部评论及可定位的关联 PR/commit，新增 16 张工程经验卡，主手册由 84 张增至 100 张；
- 只把原线程明确写出的环境、症状、诊断、处理、结果和限制写入卡片：原帖没有说明的根因保持空缺，只有建议而没有复测的内容标为 `unresolved` 或 `需要实际验证`；
- 纯提问、只有“我也遇到”而没有解法、或回复未回答原问题的候选继续保留为 `technical_pending`，不为追求卡片数量而补写解答；
- 新卡中 3 张因源码/合并 PR 与回归测试完成精确交叉核验而为 `可信度很高`，10 张作者确认或有完整工程记录而为 `值得参考`，3 张未闭环而为 `需要实际验证`；全库当前为 8 / 67 / 25；
- 典型闭环包括 Isaac Lab PR #1509 修复显式执行器速度限制传播、MuJoCo commit `1cda1e7` 修复退化 inverse weights 并加入 1000 步回归测试；维护者仅给出方向的帖子没有被提升为正式修复；
- 候选索引保持 1,131 个唯一 URL，其中 78 个 `reviewed`、1,053 个 `technical_pending`；查询前沿为 3,581 个主题和 8,110 条原始证据，下一轮继续按未审阅候选轮转。

## 9. 2026-08-11 原帖证据优先扩充（第二轮）

- 继续逐条读取 15 个 GitHub Issue 的正文、全部公开评论及可定位的关联 PR/commit，新增 17 张工程经验卡，主手册由 100 张增至 117 张；
- 新卡中 4 张因已合并修复提交或正式源码变更与原线程闭环而为 `可信度很高`，6 张因作者/维护者确认或步骤与结果完整而为 `值得参考`，7 张因结论冲突、缺少复测或只回答了部分问题而为 `需要实际验证`；全库当前为 12 / 73 / 32；
- 对同一线程中的矛盾经验没有强行合并成单一答案：例如 whole_body_tracking #42 的 Isaac Sim/Isaac Lab/rsl-rl 版本组合按三条冲突经验完整展示，IsaacLab #1618 的执行器模型与加速度读数也保留为 `conflicting`；
- 精确核验的闭环包括 human2humanoid commit `0c6fd6f` 同步 19 自由度名称/维度，以及 IsaacLab PR #1809 在 `sim.reset()` 后、首次 IMU 读取前执行 `scene.update()`；PR 未勾选的测试项仍作为限制显示；
- 只有建议但没有原作者复测、转到讨论区后没有答案、或关联 PR 未合并的候选继续保留为 `technical_pending`，没有为增加卡片数补写原因或修复；
- 候选索引仍为 1,131 个唯一 URL，其中 93 个 `reviewed`、1,038 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,583 个主题和 8,139 条原始证据：175 个 `ready`、3,338 个 `needs_more_evidence`、70 个 `covered`。

## 10. 2026-08-11 原帖证据优先扩充（第三轮）

- 继续完整读取 6 个 TSID/Pinocchio Issue 的正文、全部公开评论和可定位的关联 PR 补丁，新增 7 张工程经验卡，主手册由 117 张增至 124 张；
- TSID #160 的 `nq != nv` 姿态任务修复和 TSID #158 的默认位置界修复均核对到已合并 PR、合并提交与实际代码差异，因此新增 2 张 `可信度很高`；
- Pinocchio #2531 的 MuJoCo/Pinocchio 四元数顺序、#2702 的 `LOCAL_WORLD_ALIGNED` 导数版本边界、#2060 的四元数归一化数值复测均只按原作者或维护者明确写出的结果整理，新增 3 张 `值得参考`；
- Pinocchio #2519 虽已关闭，但原作者后续固定基最小复现没有答案；维护者建议的 FreeFlyer 路径与社区 CasADi `Jdot` 函数均未在原线程完成交叉验证，故作为同一问题下 2 条 `需要实际验证` 经验并列展示；
- 全库当前分级为 14 / 76 / 34；答案状态为 28 个 `resolved`、71 个 `partial`、19 个 `unresolved`、6 个 `conflicting`；
- 候选索引仍为 1,131 个唯一 URL，其中 99 个 `reviewed`、1,032 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,584 个主题和 8,157 条原始证据：175 个 `ready`、3,339 个 `needs_more_evidence`、70 个 `covered`。

## 11. 2026-08-11 原帖证据优先扩充（第四轮）

- 完整读取 4 个 Pinocchio Issue 的正文与共 41 条公开评论，新增 5 张经验卡，主手册由 124 张增至 129 张；
- continuous URDF 关节的 `nq=2/nv=1`、`buildReducedModel` 的 Python 调用链、FreeFlyer 合法随机配置和 `difference` 的流形输入边界均由项目成员说明及原线程复现支撑，新增 4 张 `值得参考`；
- Pinocchio #1593 中“只应使用局部关节速度”的判断只有原作者一句自我分析，项目成员后续没有回应也没有修正后输出，因此单独生成 1 张 `unresolved / 需要实际验证` 卡，没有混入已确认的四元数归一化答案；
- Pinocchio #1232 的用户示例虽自称 working，但其浮动基前 7 个参考配置全部为 0，线程没有讨论四元数有效性；手册只保留已确认的命名空间、Joint ID、参考配置和几何模型重载，不把整段数值例子升级为通用模板；
- 全库当前分级为 14 / 80 / 35；答案状态为 31 个 `resolved`、72 个 `partial`、20 个 `unresolved`、6 个 `conflicting`；
- 候选索引为 1,131 个唯一 URL，其中 103 个 `reviewed`、1,028 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,584 个主题和 8,167 条原始证据：176 个 `ready`、3,338 个 `needs_more_evidence`、70 个 `covered`。

## 12. 2026-08-11 原帖证据优先扩充（第五轮）

- 完整读取 7 个 Pinocchio、TSID 和 IsaacLab Issue 的正文与全部本地留存公开评论，新增 11 张经验卡，主手册由 129 张增至 140 张；
- TSID #157 将维护者的双重反馈诊断、位置控制人形常用的开环模型状态加 F/T/IMU 稳定器、以及原作者真机 hacks 拆为同一问题下 3 条独立经验，没有把机器人特定偏置写成通用参数；
- IsaacLab #2307 将作者已确认的 `max_angular_velocity` 度制单位问题与仍未解释的“施力时超过上限”分开标记；Issue 关闭没有被当作后者已经修复；
- IsaacLab #5018 按作者澄清拆分 startup latency 与 runtime ms/step：前者由 Newton 0.2.0 升级到 1.0.0 Beta 3.0v 后解决，后者由完整分段基准指向同一步重复读取 `sensor.data`，二者不混作同一根因；
- Pinocchio #2854、#1388 分别保留独立复现/维护者修复声明和固定关节惯量合并边界；关联 PR 未读取 diff 时只作为精确链接，不补写接口或补丁细节；
- 全库当前分级为 14 / 90 / 36；答案状态为 35 个 `resolved`、78 个 `partial`、21 个 `unresolved`、6 个 `conflicting`；
- 候选索引为 1,131 个唯一 URL，其中 110 个 `reviewed`、1,021 个 `technical_pending`、0 个 `excluded`；查询前沿仍为 3,584 个主题，原始证据增至 8,181 条：176 个 `ready`、3,338 个 `needs_more_evidence`、70 个 `covered`。

## 13. 2026-08-11 原帖证据优先扩充（第六轮）

- 完整读取 Pinocchio #446 的 14 条评论、Pinocchio #671 的 60 条评论以及 IsaacLab #2324 的 4 条评论，新增 7 张 `值得参考` 经验卡，主手册由 140 张增至 147 张；
- Pinocchio #446 把 Jcom 坐标旋转、WORLD/LOCAL Jacobian 作用点、`data.v[id]` 坐标表达和 FreeFlyer 质量矩阵表示拆成同一问题下 3 条经验；只保留维护者定义及作者固定基/单位姿态对照，没有从长矩阵自行推导通用变换；
- Pinocchio #671 把 armature 对角近似、Featherstone 式 ABA 更新和 `computeAllTerms + Cholesky` 路径分开记录，明确保留遗漏电机 Coriolis/centrifugal effects、gear ratio、特定 revolute sketch、SEA 不适用和 preview API 不稳定等限制；
- IsaacLab #2324 的 H1_2 迁移只记录实践者明确写出的 URDF→USD、未命名迭代次数 4→400、上身碰撞集合和 acceleration reward 排查；由于没有字段名、版本、曲线或独立复现，400 没有被写成通用配置值；
- 只有追问、转到 Discussion、没有答案或回复明确标为 under review 的 8 个候选继续保留为 `technical_pending`，没有为增加卡片数采用未经原作者确认的建议；
- 全库当前分级为 14 / 97 / 36；答案状态为 37 个 `resolved`、83 个 `partial`、21 个 `unresolved`、6 个 `conflicting`；
- 候选索引为 1,131 个唯一 URL，其中 113 个 `reviewed`、1,018 个 `technical_pending`、0 个 `excluded`；查询前沿仍为 3,584 个主题，原始证据增至 8,201 条：176 个 `ready`、3,338 个 `needs_more_evidence`、70 个 `covered`。

## 14. 2026-08-11 原帖证据优先扩充（第七轮）

- 通过 GitHub 官方公开 API 完整读取 mc_rtc #92、TSID #222、Pinocchio #735、#1137、#1656 和 #2053 的正文与全部 25 条评论，新增 7 张工程经验卡，主手册由 147 张增至 154 张；
- mc_rtc #92 只记录原线程实际验证过的三项：`LogPolicy=threaded`、控制器及全部依赖采用 Release/RelWithDebInfo、关闭 CPU powersaving；作者确认尖峰和总耗时明显下降，但线程没有最坏执行时间，也没有给出硬实时保证；
- TSID #222 用原作者的分段计时把瓶颈定位到 HQP solve，协作者从安装命令发现 `eiquadprog` 未以 Release 构建；作者重建后确认循环从约 27 ms 恢复到 2 ms、完整示例少于 10 s，因此没有把维护者另一台 TALOS 的 1 kHz 经验写成所有平台的性能承诺；
- Pinocchio #735 将 `nq/nv` 的配置流形语义与 URDF 默认固定基拆成两张卡：continuous/revolute 的语义差异被保留，`JointModelFreeFlyer` 的 7/6 维增量由作者复测确认；#1137 与 #1656 分别只确认 FreeFlyer 的基座速度和 ABA 广义加速度采用 body/local frame，未回答的 centroidal、ZYX 和 acceleration transform 问题没有补写；
- Pinocchio #2053 有完整最小复现且维护者确认当时 `JointModelComposite` 支持不完整，但 Issue 仍 open、没有修复 PR/版本/复测，因此只生成 1 张 `unresolved / 需要实际验证` 卡；OCS2 #108 的社区回复对 hard inequality constraint 的处理方式相互否定且没有维护者结论，继续保留为 `technical_pending`；
- 本轮新增 6 张 `值得参考` 和 1 张 `需要实际验证`；全库当前分级为 14 / 103 / 37，答案状态为 43 个 `resolved`、83 个 `partial`、22 个 `unresolved`、6 个 `conflicting`；
- 候选索引仍为 1,131 个唯一 URL，其中 119 个 `reviewed`、1,012 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,588 个主题和 8,227 条原始证据：179 个 `ready`、3,339 个 `needs_more_evidence`、70 个 `covered`。

## 15. 2026-08-11 原帖证据优先扩充（第八轮）

- 通过 GitHub 官方公开 API 完整读取 TSID #131、#138、Pinocchio #1292 和 #1650 的正文与全部 25 条评论，新增 8 张工程经验卡，主手册由 154 张增至 162 张；只有提问且零回复的 OCS2 #101 和 #53 继续保留为 `technical_pending`；
- TSID #131 将重复 level-0 足端运动等式导致负接触力、以及仍未回答的 CoP hard constraint 失稳拆为两张卡：前者由协作者复现和原作者确认，后者没有因为 Issue 被关闭而伪装成已解决；
- TSID #138 将 floating-base dynamics 的六行硬等式含义与 soft Contact6D motion task 错计 `m_eq` 拆开；后一个 bug 精确核对到官方 commit `5a6b452`，补丁只在 `motionPriorityLevel==0` 时增加 equality count，因此达到 `可信度很高`，但没有猜测对应 release；
- Pinocchio #1292 只确认 `WORLD` 与 `LOCAL_WORLD_ALIGNED` 的作用点差异及作者复测；线程没有验证 3×3 Jacobian 截取、伪逆或 maximum feasible force，因此状态保持 `partial`；
- Pinocchio #1650 的足端 contact wrench→parent joint local `fext` 路径核对到原作者明确引用的 OCS2 commit `3566993` lines 189–225，并达到 `可信度很高`；手写 CRBA/Jacobian 与 RNEA 的结果接近但没有误差/速度基准，多接触 re-root/TSID/QP 只属未复现架构建议，分别保留为 `值得参考` 和 `需要实际验证`；
- 本轮新增 2 张 `可信度很高`、4 张 `值得参考`、2 张 `需要实际验证`；全库当前分级为 16 / 107 / 39，答案状态为 47 个 `resolved`、86 个 `partial`、23 个 `unresolved`、6 个 `conflicting`；
- 候选索引仍为 1,131 个唯一 URL，其中 123 个 `reviewed`、1,008 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,590 个主题和 8,246 条原始证据：181 个 `ready`、3,339 个 `needs_more_evidence`、70 个 `covered`。

## 16. 2026-08-11 原帖证据优先扩充（第九轮）

- 通过 GitHub 官方公开 API 完整读取 MuJoCo #832、#1607、#1684、#2638 和 Isaac Lab #1400 的正文与全部 60 条回复，新增 9 张工程经验卡，主手册由 162 张增至 171 张；MuJoCo #2423、Gazebo #3211 因零回复，Gazebo #2528 因只有用户对 Bullet/ODE 现象的对比且没有维护者诊断，继续保留为 `technical_pending`；
- MuJoCo #832 将三个不能混写的结论拆开：site force sensor 漏掉 tendon force 是协作者确认但尚未修复的缺口；passive spring/damper force 与 `sensor/tendonlimitfrc` 约束力的合成同时核对了维护者回复、官方 `engine_passive.c` 和 XML reference，达到 `可信度很高`；welded mounting-body workaround 在不同用户间存在质量偏差与焊缝伸长冲突，保留为 `conflicting / 需要实际验证`；
- MuJoCo #1607 保留了 MJX 缺少动态 `set_const` 时的预编译路径：先在原生 MuJoCo 编译随机 mass/inertia 模型，再 `put_model` 并拼接成 batch；同时记录整模型 batching 的内存开销和最终“MJX 不计划该特性，改看 MuJoCo Warp `set_const`”的项目方向，没有把单一用户 profiling 扩大为性能承诺；
- MuJoCo #1684 将可动对象位置放在 `mjx.Data`/环境 State 的 reset，primitive 尺寸放在 `mjx.Model.geom_size` 的维护者接口划分与异构模型限制拆开；对“预加载所有 mesh，将未用对象移出场景”只按原回复的未尝试/YMMV 标记为 `需要实际验证`，并保留静态 world-body 位置变更需重编译的边界；
- MuJoCo #2638 只沉淀原作者已执行的负试验：elliptic friction 不能消除漂移，timestep 降到 `1e-7` 仅减小幅度，friction=0 只是定位对照；原线程没有根因或修复，因此不编造解法；
- Isaac Lab #1400 保留首次约 60M 步触发的 GPU `compressContactStage`/CUDA/scene-corrupt 错误，以及原作者在 2.0.1+CCD 下仍复现和内存持续增长的后续；`MultiAssetSpawnerCfg` 和 256 links 只是用户推测，没有写成根因或已验证修复；
- 本轮新增 1 张 `可信度很高`、3 张 `值得参考`、5 张 `需要实际验证`；全库当前分级为 17 / 110 / 44，答案状态为 49 个 `resolved`、89 个 `partial`、26 个 `unresolved`、7 个 `conflicting`；
- 候选索引仍为 1,131 个唯一 URL，其中 128 个 `reviewed`、1,003 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,591 个主题和 8,263 条原始证据：182 个 `ready`、3,339 个 `needs_more_evidence`、70 个 `covered`。

## 17. 2026-08-11 原帖证据优先扩充（第十轮）

- 通过 GitHub 官方公开 API 完整读取 Crocoddyl #1087、Pinocchio #1515、#1759 和 #1343 的正文与全部 20 条回复，新增 4 张工程经验卡，主手册由 171 张增至 175 张；Pinocchio #1759 的两张原图也逐张分析，明确区分修正前的速度差异曲线与仅用于说明构型的机械臂截图；
- Crocoddyl #1087 只沉淀项目成员明确解释的 FDDP `cost`/dynamic infeasibility 权衡：联合监控 cost、不可行度和最终收敛；没有把持续发散、NaN 或无界增长推断为正常；
- Pinocchio #1515 保留项目贡献者给出的新增 Frame、相对 parent joint frame 的 `placement` 和更新 `model.frames[id].placement` 路径，但原作者只说会尝试、没有数值复测，因此状态为 `partial`；2024 年关于 Pinocchio 3x 是否发布的旧回复不作为当前产品状态；
- Pinocchio #1759 的原图直接显示位置曲线重合、速度曲线显著分离；答复者建议 `LOCAL_WORLD_ALIGNED` 后原作者报告似乎有效，项目贡献者随后认可回答。线程没有修正后的曲线，也没有直接回答 `dJ` 操作，因此没有外推到所有 PyBullet/Pinocchio 差异；
- Pinocchio #1343 只记录项目贡献者对浮动基欠驱动逆动力学的 TSID 路径与随后关闭，不自行补写接触、任务、权重或力矩限幅配置，也不把 RNEA 的能力范围作过度否定；
- 本轮新增 4 张 `值得参考`；全库当前分级为 17 / 114 / 44，答案状态为 52 个 `resolved`、90 个 `partial`、26 个 `unresolved`、7 个 `conflicting`，共 165 个稳定 `problem_id`；
- Crocoddyl #133、Isaac Lab #4257/#855/#423/#2374/#4521/#2810/#5809、Pinocchio #2144 和 OCS2 #53 等只有设计提案、追问、用户猜测、转讨论区或尚未审完的线程继续保留为 `technical_pending`，不为增加卡片数量补造解答；
- 候选索引仍为 1,131 个唯一 URL，其中 132 个 `reviewed`、999 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,591 个主题和 8,276 条原始证据：183 个 `ready`、3,338 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 189 个问题入口（175 张经验卡加 14 条正式 Engineering Claims）。

## 18. 2026-08-11 原帖证据优先扩充（第十一轮）

- 通过 GitHub 官方公开 API 完整读取 Isaac Lab #2391/#3155/#3162 和 Pinocchio #1140/#1977 的正文与全部 25 条 Issue 回复，同时核对关联 PR #2392/#3163/#3316 的合并元数据、全部补丁和必要讨论；新增 5 张工程经验卡，主手册由 175 张增至 180 张。
- Isaac Lab #2391 只把 zero-weight 分支造成的 `_step_reward` 过期可视化/日志值写入卡片；原帖明确说总奖励 `_reward_buf` 一直正确。PR #2392 已合并，但没有新增回归测试，这一限制已保留。
- Isaac Lab #3155 的两个真值表用例、`~torch.isclose` 修复、CPU/CUDA 回归测试和 0.45.3 changelog 形成闭环；卡片同时说明该谓词只检测 computed/applied torque 差异，不替代真实电机力矩与热保护。
- Isaac Lab #3162 的 `platform_height` 字段确认由 #2695 回归放错类，PR #3316 将其移入 `MeshRepeatedObjectsTerrainCfg.ObjectCfg` 后合并；PR 作者明确说先合并、单元测试以后再做，所以没有伪造修复后训练验证。
- Pinocchio #1140 的两张原始曲线已逐张分析：第一张显示 frame 速度实线/虚线明显分离，第二张显示部分 `qdot`/`diff(q)` 基本重合；两图都没有图例、轴名或单位，因此不从颜色猜测具体分量。原作者最终确认 free-flyer 速度/积分的全局坐标与 Pinocchio 局部约定不兼容，修正后得到预期结果。
- Pinocchio #1977 只采用项目贡献者明确给出的 Coriolis/Centrifugal 分类、`computeCoriolisMatrix @ qd` 对照和 `pin.neutral(model)` 要求；原作者关于转动关节对照为何没有交叉项的追问无人回答，因此保留为 `partial`。
- 本轮新增 3 张 `可信度很高`和 2 张 `值得参考`；全库当前分级为 20 / 116 / 44，答案状态为 56 个 `resolved`、91 个 `partial`、26 个 `unresolved`、7 个 `conflicting`，共 170 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 137 个 `reviewed`、994 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,592 个主题和 8,288 条原始证据：183 个 `ready`、3,339 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 194 个问题入口（180 张经验卡加 14 条正式 Engineering Claims）。

## 19. 2026-08-11 原帖证据优先扩充（第十二轮）

- 通过 GitHub 官方公开 REST 完整读取 Isaac Lab #2054/#2103 和 ros2_control #668/#851/#859 的正文与全部 36 条回复，同时核对 PR #2098/#802 的合并状态和全部补丁，并逐像素读取 #2054 的 USD Drive 截图；新增 5 张工程经验卡，主手册由 180 张增至 185 张。
- Isaac Lab #2054 的截图只显示 USD `Max Force=88.0`，Python 端 `joint_effort_limits=1e9` 来自原帖文字与 G1 复现；已合并 PR #2098 将基类判断改为 `self.is_implicit_model`，并在最终补丁中核对未显式配置时继承 USD max effort，因此该卡为 `可信度很高`。卡片同时明确 USD 数值不等于真机电源、减速器与热安全值。
- Isaac Lab #2103 只按项目贡献者的原回复区分 `saturation_effort` 与 `effort_limit`：前者是驱动器峰值包络，后者是受整机当前供电与硬件条件限制的实际运行范围。8A/40 N·m 与 30A/约 100 N·m 被保留为实验室示例，没有改写为通用参数。
- ros2_control #668 将栈上局部量与默认堆分配分开，保留 `std::string`/container/resize、logging、`std::make_shared` 和 TLSF 初始化的审计边界；由于整库清理没有验收、Issue 是 stale 关闭，状态为 `partial`，没有写成已完成的实时修复。
- ros2_control #851 只确认当时 `controllers_lock_` 保护的是控制器存储列表，禁止的是同时加载新控制器；原线程没有延迟基准，因此没有声称 mutex 延迟为零。
- ros2_control #859 保留了关键分歧：`steady_clock` 可恢复墙钟 100 Hz，但原作者明确它不随仿真 real-time factor 缩放；项目成员更倾向由仿真器专用插件/节点在物理步内驱动更新。未合并 PR #802 和回复者明确称为 ChatGPT 版的 `rclcpp::Rate` 示例都没有被当作通用修复。
- Isaac Lab #262 虽标记 completed，但时间线中在关闭前引用的提交实际是历史编号重用造成的无关 AppLauncher 变更，未能证明 external wrench 缓冲已修复；本轮继续保留为 `technical_pending`，不根据“已关闭”自行补写解答。
- 本轮新增 1 张 `可信度很高`和 4 张 `值得参考`；全库当前分级为 21 / 120 / 44，答案状态为 59 个 `resolved`、93 个 `partial`、26 个 `unresolved`、7 个 `conflicting`，共 175 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 142 个 `reviewed`、989 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,593 个主题和 8,300 条原始证据：183 个 `ready`、3,340 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 199 个问题入口（185 张经验卡加 14 条正式 Engineering Claims）。

## 20. 2026-08-11 原帖证据优先扩充（第十三轮）

- 通过 GitHub 官方公开数据逐条核对 Pinocchio #2026、ros2_control #2049 以及 Isaac Lab #3266/#4999 的正文与全部 16 条回复，同时检查 Isaac Lab PR #3318 的审阅、测试更改和合并状态；新增 4 张工程经验卡，主手册由 185 张增至 189 张。
- Pinocchio #2026 只采用项目成员与原作者在同一线程确认的顺序问题：先 `model.createData()`、后 `model.addFrame()` 会让旧 Data 与已修改 Model 不一致；卡片要求完成 Model 修改后再创建 Data，但没有从该案例外推线程安全或其他内存模型结论。
- ros2_control #2049 保留了官方 demo→`GenericSystem`→真实硬件的分层隔离路径：原作者最终确认打开错误串口；另一用户的 Arduino/ESP32 固件未响应 read/write 仅作为“类似症状、不同硬件根因”展示。demo 中 `--param-file` key 错写和 FIFO 调度警告均没有被写成原始超时的根因。
- Isaac Lab #3266 的最小复现、三类摩擦属性同时写入、`static >= dynamic` 约束、已合并 PR #3318 和直接核对 PhysX buffer 的测试形成交叉核验，因此新增 1 张 `可信度很高` 卡；PR 页合并时只显示 10/13 checks 通过，这一可见限制仍保留在卡片中。
- Isaac Lab #4999 给出 Galaxea R1 Pro 浮动基 OSC 的修正前/后力矩、6 自由度索引对照和作者本地结果；但项目方只回复“会审查”，Issue 页也明确没有关联 PR。因此它只是 `值得参考`，关闭状态没有被当作官方修复；数百至约 1,500 N·m 的异常力矩同时触发了真机限流、夹紧和急停警示。
- Isaac Lab #4467 只说作者增加了几个类并重用 clone 解决 A1/Go2 `MultiUsdFileCfg` 问题，没有贴出类实现、回归测试或项目诊断；#5064 和其他未闭环候选也继续保留为 `technical_pending`，没有为增加数量补写缺失的实现。
- 本轮新增 1 张 `可信度很高`和 3 张 `值得参考`；全库当前分级为 22 / 123 / 44，答案状态为 63 个 `resolved`、93 个 `partial`、26 个 `unresolved`、7 个 `conflicting`，共 179 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 146 个 `reviewed`、985 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,593 个主题和 8,312 条原始证据：187 个 `ready`、3,336 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 203 个问题入口（189 张经验卡加 14 条正式 Engineering Claims）。

## 21. 2026-08-11 原帖证据优先扩充（第十四轮）

- 核对 Pinocchio #2046、#2753 和 #1290 的原帖正文、公开回复摘要、关闭关联，以及官方最小 CMake 示例、PR #2441/#2756、v3.5.0/v3.8.0 release 与 CHANGELOG；新增 3 张工程经验卡，主手册由 189 张增至 192 张。
- Pinocchio #2046 的 GDB 栈进入 Eigen `aligned_free`；维护者把问题指向跨库向量化/CPU 编译选项不一致，并建议统一链接 `pinocchio::pinocchio`。原作者最终确认一个依赖库单独启用了 `-march=native`，移除后段错误消失。该结论有维护者与作者同线程确认，但没有独立复现，因此为 `值得参考`；卡片明确没有把所有 `buildModel` 崩溃都归因于该选项。
- Pinocchio #2753 在 Ubuntu 24.04/Pinocchio 3.6.0 的完整 Kinova-Robotiq URDF 中，只识别一个 `revolute` mimic，漏掉四个 `continuous` mimic。Issue 关联 #2756 关闭，v3.8.0 release 与 CHANGELOG 明确新增 continuous URDF joint 的 mimic 解析，因此为 `可信度很高`；仍要求升级后核对实际 mimic 数量。
- Pinocchio #1290 记录了 mimic 支持不是一次性覆盖所有算法的版本边界。v3.5.0 只明确列出 `mimic=True` 解析入口，以及 FK、Jacobian/frame、ccrba、RNEA、CRBA 和 reachable workspace；continuous mimic 还需 v3.8.0/#2756。卡片没有把未列入 release 的算法推断为已支持，因此为 `可信度很高`。
- Isaac Lab #4320/#4502 只有完整复现但没有维护者结论或关联 PR；Isaac Lab #2810 的长回复明确标注仍在 review，且关键图片未完成核验。这些候选继续保留为 `technical_pending`，没有为增加卡片数补写原因或修复。
- 本轮新增 2 张 `可信度很高`和 1 张 `值得参考`；全库当前分级为 24 / 124 / 44，答案状态为 66 个 `resolved`、93 个 `partial`、26 个 `unresolved`、7 个 `conflicting`，共 182 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 149 个 `reviewed`、982 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,593 个主题和 8,321 条原始证据：187 个 `ready`、3,336 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 206 个问题入口（192 张经验卡加 14 条正式 Engineering Claims）。

## 22. 2026-08-11 原帖证据优先扩充（第十五轮）

- 通过 GitHub 官方公开 API 核对 Pinocchio #2917、Isaac Lab #267/#911/#1995 和 MuJoCo #2934 的原帖正文、全部 56 条评论、关联 commit/PR 状态，并实际读取 MuJoCo #2934 的关键时序图；新增 5 张工程经验卡，主手册由 192 张增至 197 张。
- Pinocchio #2917 只采用原作者与维护者同线程确认的 CMake 结论：`ament_target_dependencies` 没有按该工程方式传播 Pinocchio 所需的 Boost MPL/Fusion 编译定义，改用 `target_link_libraries(... pinocchio::pinocchio)` 后恢复。由于没有正式文档或独立复现交叉核验，等级保持 `值得参考`。
- Isaac Lab #267 将 `RigidBodyView` 与 PhysX `ArticulationView` 的 link 排序差异核对到作者确认和官方 commit `e3c40acf`；#911 将旋转基座下的 world/root-frame Jacobian 不一致核对到已合并 PR #967。两张卡均有明确环境、原线程闭环和正式源码/PR，达到 `可信度很高`。
- Isaac Lab #1995 明确区分“静态 collider 的 filtered-contact 检索 API 不支持”与“物理接触没有求解”；原作者给出 kinematic `RigidObjectCfg` 地面绕行配置，但底层支持状态没有版本修复证据，因此保留为 `partial / 值得参考`，也没有把后续参与者的 ray-caster 路径错误并入原根因。
- MuJoCo #2934 只保留参数扫描和接触级可观测量：固定 `kp=300` 时，评论记录 `kv=5/10/100` 对应约 `0.7/1.4/13.6 mm` 漂移，切向接触速度约 `0.012 m/s`；关键图显示 3.2 s 左右 actuator force 与物体净力先出现、可见滚转和位置随后变化。维护者仍要求纯 XML MRE，Issue 仍 open，因此降低 `kv` 只写作缓解/诊断，不写成最终修复；未经维护者确认的理论性评论被排除。
- 本轮新增 2 张 `可信度很高`和 3 张 `值得参考`；全库当前分级为 26 / 127 / 44，答案状态为 69 个 `resolved`、95 个 `partial`、26 个 `unresolved`、7 个 `conflicting`，共 187 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 154 个 `reviewed`、977 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,594 个主题和 8,331 条原始证据：187 个 `ready`、3,337 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 211 个问题入口（197 张经验卡加 14 条正式 Engineering Claims）。

## 23. 2026-08-11 原帖证据优先扩充（第十六轮）

- 通过 GitHub 官方公开 API 完整读取 Pinocchio #2683/#2825/#2844/#867 和 Isaac Lab #6885 的正文与全部 35 条回复，并核对 Pinocchio PR #2684 的合并元数据、全部补丁以及固定到 commit `031ebb13` 的 `getFrameKinematicHessian` 官方头文件；新增 5 张工程经验卡，主手册由 197 张增至 202 张。
- Pinocchio #2683 的最初“3.5.0 Jacobian 回归”判断被原作者自己推翻：实际是 C++ 调用方传了 3×nv 输出矩阵，3.5.0 不再自动 resize，非零角速度项位于第 5、6 行。已合并 PR #2684 对 frame/joint Jacobian 增加 6 行与 `model.nv` 列检查，因此该卡达到 `可信度很高`。
- Pinocchio #2825 只沉淀 fixed link/frame 不属于 joint kinematic chain、惯量与静态变换折叠规则，以及维护者给出的 `frame.placement * local_placement` 构造；原作者确认理解，但没有完整估计器回归，等级为 `值得参考`。
- Pinocchio #2844 与固定源码共同证明 Pinocchio 4 已有 `getFrameKinematicHessian` 的 frame-id overload 和 6×nv×nv 返回 tensor；但原线程没有调用者复测、binding/最低 release 边界或数值对照，因此诚实标为 `需要实际验证`，没有因官方函数存在而自动升级。
- Isaac Lab #6885 的四配置对照只在 GPU tensor pipeline + PhysX surface velocity 时丢失接触；维护者明确说明 GPU 当前不支持并要求使用 CPU。Issue 虽已关闭，GPU 原生路径仍没有修复；逐步覆写 root velocity 只作为原帖行为近似保留，状态为 `partial / 值得参考`。
- Pinocchio #867 只回答接触 QP 中 `d(J^Tλ)/dq` 的 tensor contraction：原作者确认带 external forces 的 RNEA derivatives 能避免完整 Hessian，并记录 Valkyrie `nv=32` 的 0.500/0.060/0.035 ms 对照。维护者估计的 0.015 ms 没有作者复测，未写入结果；旧环境时序也不外推为当前通用 benchmark。
- 本轮新增 1 张 `可信度很高`、3 张 `值得参考`和 1 张 `需要实际验证`；全库当前分级为 27 / 130 / 45，答案状态为 73 个 `resolved`、96 个 `partial`、26 个 `unresolved`、7 个 `conflicting`，共 192 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 159 个 `reviewed`、972 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,594 个主题和 8,341 条原始证据：187 个 `ready`、3,337 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 216 个问题入口（202 张经验卡加 14 条正式 Engineering Claims）。

## 24. 2026-08-11 原帖证据优先扩充（第十七轮）

- 完整读取 human2humanoid #13/#17/#6/#18、TSID #247 及 #18 原作者链接的 PHC #96，共 6 个 Issue 正文、全部 30 条评论、TSID fork commit `eb03d05` 的完整 patch 和 human2humanoid 固定 commit `fb7ed5f` 的 penalty-curriculum 代码；新增 5 个根来源、6 张工程经验卡，主手册由 202 张增至 208 张。
- human2humanoid #13 只确认项目作者明确公开的接口边界：Vision Pro 或 RGB+HybrIK 提供人体 global keypoint positions，实机 sparse-input 路径不重复离线 whole-body retargeting。后续关于 RGB/Isaac Gym 坐标变换的追问没有回答，因此卡片为 `partial / 值得参考`，没有补写标定矩阵。
- human2humanoid #17 的奖励图和 GIF 首帧均已核验：mean reward 在约 1.2M steps 达到更高区间、1.5M 后总体下降，但图中没有 penalty coefficient；项目源码则明确按 average episode length 增减并裁剪 penalty scale。原作者只说问题已解决、没有披露最终动作，因此 100000 iterations 仅作为原线程建议，不写成通用收敛阈值。
- human2humanoid #6 保留项目作者给出的 H2O 数据清洗原规则：先 retarget 全部 AMASS，训练无 domain randomization/penalty reward 的 privileged teacher，任一 timestep 的 reference motion distance >0.5 m 就剔除整条 motion；0.5 m 明确限定为该项目经验，不外推到其他机器人。
- TSID #247 的 binding 报错核对到维护者回复和作者 fork patch：`TaskContactForceEquality` 需为 `Contact6d`、`ContactPoint`、`ContactTwoFramePositions` 分别暴露 constructor overload。作者确认可实例化，但没有上游 PR/发布和完整 force-control example，卡片不暗示官方版本已修复。
- human2humanoid #18 跨到原作者自答的 PHC #96 后拆为两张卡：`smpl_pose_modifier` 未对齐 T-pose 时，shape fitting 只调 betas/scale，修正后作者报告 loss 从 200+ 降至约 40；自定义 XML 中无-joint 中间 body 导致 65 bodies/51 valid rotations，作者用 near-static joints 补齐。三张关键图只支持“姿态/关键点对齐明显改善”，第二个 workaround 明确保留模型拓扑和动力学复测风险。
- human2humanoid #20 主要是用户互相推测，#29 最终只确认项目没有 MuJoCo sim-to-sim infra，Crocoddyl #1518 只有“用 numdiff 验证”的建议；这些线程继续保持 `technical_pending`，没有为增加卡数生成未经确认的答案。
- 本轮新增 6 张 `值得参考`；全库当前分级为 27 / 136 / 45，答案状态为 76 个 `resolved`、99 个 `partial`、26 个 `unresolved`、7 个 `conflicting`，共 198 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 164 个 `reviewed`、967 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,597 个主题和 8,357 条原始证据：190 个 `ready`、3,337 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 222 个问题入口（208 张经验卡加 14 条正式 Engineering Claims）。

## 25. 2026-08-11 原帖证据优先扩充（第十八轮）

- 通过 GitHub 官方公开 API 完整读取 Isaac Lab #1604/#1999/#2074/#2127 与 Pinocchio #1357/#1761/#2604 的正文和全部 32 条评论，并核对 Isaac Lab PR #1416/#2019/#2128/#3563 的合并状态、修改文件和测试；新增 7 个来源、7 张工程经验卡，主手册由 208 张增至 215 张。
- Isaac Lab #1999 将 Go2 rough RSL-RL 后期 `value function loss=inf` 与大动作/上一动作观测的反馈放大核对到原作者 `Works` 确认和已合并 PR #2019；卡片没有编造 `clip_actions` 的通用阈值。#2127 的 6D joint reaction wrench 精确核对到已合并 PR #2128 的 `(num_instances, num_bodies, 6)`、parent-body-frame 定义和 CPU/CUDA 静态数值测试。两张卡均达到 `可信度很高`。
- Isaac Lab #2074 明确区分 `net_forces_w` 的净法向接触力与摩擦力；旧版 `get_friction_data` 在原作者环境仍返回全零，不能冒充修复。后续已合并 PR #3563 新增 `track_friction_forces` 和 `friction_forces_w` 并附测试，因此新版本路径达到 `可信度很高`。线程中的两张图均已读取：曲线只支持“两个轴分量为零”的症状，MuJoCo 箭头截图只表达作者期望，没有被当作修复结果。
- Isaac Lab #1604 的 `add (0,0)` 对照只证明该实现先恢复 `default_joint_stiffness` 再随机化；贡献者认可分离 default/randomization 的方向，但所指 PR #1416 未合并且不是 actuator-gain 直接修复，因此保持 `partial / 值得参考`。
- Pinocchio #1357 与既有 #1137 描述同一 FreeFlyer q/v frame 问题，复用稳定 `problem_id` 聚合为第二个独立原线程，没有制造近似重复问题；#2604 由项目贡献者解释无接触前向动力学应使用 `aba`、`forwardDynamics` 是约束动力学重载，且原作者确认解决。两张卡为 `值得参考`。
- Pinocchio #1761 中维护者只在作者明确“固定世界方向外力映射到 torque”后回答使用 `LOCAL_WORLD_ALIGNED`；没有作者数值复测、wrench 排列或作用点验证，因此保持 `partial / 需要实际验证`，没有自行补写完整力矩公式。
- 本轮新增 3 张 `可信度很高`、3 张 `值得参考`和 1 张 `需要实际验证`；全库当前分级为 30 / 139 / 46，答案状态为 81 个 `resolved`、101 个 `partial`、26 个 `unresolved`、7 个 `conflicting`，共 204 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 171 个 `reviewed`、960 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,597 个主题和 8,371 条原始证据：190 个 `ready`、3,337 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 229 个问题入口（215 张经验卡加 14 条正式 Engineering Claims）。

## 26. 2026-08-11 原帖证据优先扩充（第十九轮）

- 完整读取 Crocoddyl #1395/#880/#682 与 OCS2 #24/#27/#56 的正文和全部 28 条评论，核对 Crocoddyl PR #1396/#1403 的元数据、PR #1403 完整 patch 和固定合并提交；新增 6 个根来源、8 张工程经验卡，主手册由 215 张增至 223 张。
- Crocoddyl #1395 的 TALOS whole-body manipulation `NaN cost / iteration 0` 被原作者定位到 `xBounds` 中带 `0*x0` 的 `ResidualModelState` 构造；协作者复现，维护者 PR #1403 把该处改为不传错误参考状态的构造并合入 `devel`。卡片达到 `可信度很高`，但明确保留“原作者没有在合并后再次留言复跑”的边界，也没有把 PR 中其他 notebook 修改都归为同一根因。
- OCS2 #27 拆为两张卡：一张记录作者确认的 quaternion→Euler ZYX 微小计算错误，修正后四足可行走；另一张记录 observation feedback 低通滤波在当前步行中有效，但贡献者警告其人工 phase shift/delay 可能妨碍更动态动作。两段 GIF 均在多个时刻核验，只支持 RViz/RaiSim 姿态错位和跳变症状，没有被用于反推频率或滤波参数。
- OCS2 #56 中第二位用户复现静止失稳，贡献者明确把问题归到 generated terrain 与 `ZeroVelocityConstraint.positionErrorGain` 的平地假设冲突：平地设 `generateTerrain=false`，粗糙地形设 `positionErrorGain=0.0`；原作者确认有效，且两处官方配置链接可定位，因此达到 `可信度很高`。卡片没有猜测原作者最终采用了两种方案中的哪一种。
- OCS2 #24 只有“零速度接触约束长时间积分漂移、world-frame 命令与内部 ground notion 分离”的贡献者解释，没有当时可复测补丁，保持 `partial / 需要实际验证`。静态图清楚显示绿色目标轨迹高于机器人；MP4 播放器未能提供可核验帧，限制已写入图片分析而没有补写视频运动过程。
- Crocoddyl #880 把“friction cone/CoP 不足，需要 contact wrench cone，启用后移除单独 friction 或 CoP cost”整理为 `resolved / 值得参考`；脚板不对齐 world frame 时，原线程只有“constructor 第一个参数定义 rotation”的一句接口提示，没有矩阵约定或复测，因此另拆为 `partial / 需要实际验证`。足板图只用于确认非平行支撑几何，没有被当作旋转矩阵证据。
- Crocoddyl #682 原样保留维护者之间的层次差异：当时 API 的实用途径是 velocity/impact velocity penalty 与 `CostModelImpulseCoM`，但 formulation 本身并不禁止 acceleration cost。由于版本未知且没有软着陆复测，卡片标为 `conflicting / 需要实际验证`；线程后半段无关的 visualization error 未混入该问题。
- 本轮新增 2 张 `可信度很高`、3 张 `值得参考`和 3 张 `需要实际验证`；全库当前分级为 32 / 142 / 49，答案状态为 85 个 `resolved`、104 个 `partial`、26 个 `unresolved`、8 个 `conflicting`，共 212 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 177 个 `reviewed`、954 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,600 个主题和 8,389 条原始证据：192 个 `ready`、3,338 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 237 个问题入口（223 张经验卡加 14 条正式 Engineering Claims）。

## 27. 2026-08-11 原帖证据优先扩充（第二十轮）

- 通过 GitHub 连接器完整读取 Pinocchio #1959/#2141/#1779/#1534/#2092 与 Isaac Lab #4320 的正文和全部 39 条评论，并核对 Pinocchio PR #1963 的完整 diff、审阅、合并提交和 C++/Python 收敛日志；新增 6 个来源、6 张工程经验卡，主手册由 223 张增至 229 张。
- Pinocchio #1959 的旧 IK 示例把目标 frame 中的 `log6` 残差与当前 body frame 的 Jacobian 混用；已合入 PR #1963 把残差统一到局部 frame，并加入 `Jlog6` 任务 Jacobian 修正，官方 C++/Python 示例均给出收敛日志，因此达到 `可信度很高`。卡片同时保留两个边界：原用户没有在 GEN3 Lite 上复测，PR 也没有实现关节限位约束。
- Pinocchio #2141 只整理维护者完整断言脚本验证过的 LOCAL-frame 结论：`getFrameJacobianTimeVariation` 返回空间加速度对应的 `dJs/dt`，经典点加速度需增加 `omega×Jl`；`LOCAL_WORLD_ALIGNED` 和 `Jc=Js.copy()` 的后续追问没有回答，未自行外推。#1779 则严格保留 wrench 位于世界原点且 world-aligned 的回复限定，以及原作者“回答完全足够”的确认。
- Pinocchio #1534 的 continuous-joint 配置只确认 `q=pin.normalize(model,q)` 和 `[cos(theta), sin(theta)]` 参数化；由于没有修正后的 -4.905 数值或完整 walking 模型复测，状态为 `partial`。#2092 只确认 2023 年含外力静力矩二阶导仍需研究和工程实现；原作者的 CppADCodeGen 只是计划，没有被写成有效修复或性能结论。
- Isaac Lab #4320 明确拆开 GPU/Fabric 的 UI 可见性与 runtime actuator gain：维护者确认 Fabric 下 USD/UI 不显示运行时修改，但后续回复“gain 会生效”与原作者“相同配置仍不工作”直接冲突。因此该卡完整展示为 `conflicting / 需要实际验证`，Issue 的 closed 状态没有被当作技术闭环。
- Isaac Lab #4521 只有礼貌性回复，Pinocchio #1795 的原作者也明确说未定位根因；这些以及只有转 Discussion、用户推测或未审完的候选继续保留为 `technical_pending`，没有为增加卡片数量补写解答。
- 本轮新增 1 张 `可信度很高`、4 张 `值得参考`和 1 张 `需要实际验证`；全库当前分级为 33 / 146 / 50，答案状态为 88 个 `resolved`、106 个 `partial`、26 个 `unresolved`、9 个 `conflicting`，共 218 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 183 个 `reviewed`、948 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,601 个主题和 8,402 条原始证据：192 个 `ready`、3,339 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 243 个问题入口（229 张经验卡加 14 条正式 Engineering Claims）。

## 28. 2026-08-11 原帖证据优先扩充（第二十一轮）

- 通过 GitHub 连接器完整读取 Pinocchio #1215/#1252/#1473/#1872/#2177/#1395 的正文和全部 43 条评论，并核对 PR #1474 的完整 diff、合并状态与固定提交，以及原线程直接引用的 contact-dynamics、CasADi RNEA derivative 和 floating-base viewer 源码；新增 6 个来源、7 张工程经验卡，主手册由 229 张增至 236 张。
- Pinocchio #1473 的原作者用“只改变 FreeFlyer position 时 h1/h2 相同”进一步验证解析 `dh_dq` 的三列不应非零，维护者随后确认 q 偏导漏项；已合入 PR #1474 给 `dh_dq/dhdot_dq` 的角动量块补项并修改有限差分测试。因此该卡达到 `可信度很高`，但不猜测首个修复 release，也保留原作者没有在合并后发布新矩阵的边界。
- Pinocchio #1215 只把维护者明确给出的通用决策树写入卡片：已有 M、已有 ABA、只做 M^-1v 和需要完整 M^-1 时分别考虑 Cholesky/computeMinverse。原作者指出接触矩阵源码使用 Cholesky、与“已做 ABA 后优先 computeMinverse”的关系未解释；因此状态保持 `partial`，没有自行指定该特例的最快算法，也没有修正原帖未说明的矩阵转置。
- Pinocchio #1252 拆为两张已闭环经验：`computeCentroidalMomentum` 的原点在 CoM、坐标轴 world-aligned，线/角动量均使用该约定；固定机械臂 base 与 planar/prismatic mobile base 的惯量贡献取决于是否被建模为可动自由度。线程没有给向量排列和数值测试，本卡没有扩写这些细节。
- Pinocchio #1872 的 Composite Joint/CasADi 与解析 RNEA 导数差异只有维护者的支持边界判断和 FreeFlyer+`integrate/difference` 建议；原作者没有复测，最后关于 error-state/Euler/quaternion 优化变量的追问也没有答案，因此为 `partial / 需要实际验证`。#2177 则由原作者扩展官方 viewer 后确认 Translation+SphericalZYX 复合根关节速度在 WORLD frame，明确不覆盖 FreeFlyer 的 LOCAL 约定。
- Pinocchio #1395 与已入库 #2141 复用同一稳定 `problem_id` 聚合：只需 classical `Jdot*qdot` 时，把 qddot 置零运行 forward kinematics，再读取 `getFrameClassicalAcceleration` 的 drift；原作者确认这一用法。后续用户未经项目方确认的手工矩阵公式未被采纳，也没有制造重复工程问题。
- 本轮新增 1 张 `可信度很高`、5 张 `值得参考`和 1 张 `需要实际验证`；全库当前分级为 34 / 151 / 51，答案状态为 93 个 `resolved`、108 个 `partial`、26 个 `unresolved`、9 个 `conflicting`，共 224 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 189 个 `reviewed`、942 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,601 个主题和 8,426 条原始证据：193 个 `ready`、3,338 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 250 个问题入口（236 张经验卡加 14 条正式 Engineering Claims）。

## 29. 2026-08-11 原帖证据优先扩充（第二十二轮）

- 本轮主动跨出单一动力学库，通过 GitHub 连接器完整读取 Isaac Lab #1759/#2252/#2369/#2636/#2654、MuJoCo #2765 和 ros2_control #1574/#2089/#2808/#3145 的正文与全部 60 条公开评论，并核对 MuJoCo 固定修复提交、Isaac Lab 固定源码以及 ros2_control PR #2091/#3197 的 diff、review、测试和合并状态；新增 10 个来源、11 张工程经验卡，主手册由 236 张增至 247 张。
- Isaac Lab #2369 将 `joint_drive` 与 actuator gains 的关系固定到 commit `3b6d615`：implicit actuator 把 gains 写入 PhysX，explicit actuator 将 PhysX stiffness/damping 清零后自行计算力矩。源码与团队回复交叉一致，达到 `可信度很高`；评论中未逐项核验的通用调参数字没有被采用。
- MuJoCo #2765 的非方形 hfield rangefinder 错测核对到 commit `7b9f5bd`：边缘高度索引的行跨度由 `nrow` 修为 `ncol`，并新增 4×3 hfield 回归测试，因此达到 `可信度很高`。原帖三张截图只说明症状，结论来自最小代码、源码 diff 与测试。
- ros2_control #2089 将固定 0.99 阈值导致的异频硬件额外跳周期，收敛为比较“现在执行/再跳一周期”的 timing error；作者完成多频率 mock 与 UR16e+KUKA KR50 真机验证，PR #2091 已合并。#3145 则在没有虚构实测 jitter 的前提下，只记录 RT/non-RT 共享锁迁移到 `prio_inherit_recursive_mutex` 的已合并源码缓解。
- ros2_control #1574 被拆为两张卡：I2C IMU 读取导致大抖动由作者停读 A/B 确认，标为 `resolved / 值得参考`；`update(time, period)` 与相邻调用时间差仍不一致、维护者未复现，单独保留为 `unresolved / 需要实际验证`。#2808 只把 rmw_zenoh→Fast DDS 的作者 A/B 当作环境特定规避，未把 stale 关闭误写为 Zenoh 根因修复。
- Isaac Lab #2252 只确认 Isaac Sim 4.5 的 `get_generalized_mass_matrices` 与官方 OSC 示例，没有补写原线程未回答的完整 gravity/Coriolis API；#2636 的 ONNX/`ActionTerm` scale-clipping 分层回复含不确定措辞且无复测，保持 `需要实际验证`；#2654 只确认 G1 资产配置本身不是站立控制器，H1 模板没有被包装成可直接部署的 G1 成品策略。
- 本轮新增 4 张 `可信度很高`、5 张 `值得参考`和 2 张 `需要实际验证`；全库当前分级为 38 / 156 / 53，答案状态为 99 个 `resolved`、112 个 `partial`、27 个 `unresolved`、9 个 `conflicting`，共 235 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 199 个 `reviewed`、932 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,603 个主题和 8,455 条原始证据：194 个 `ready`、3,339 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 261 个问题入口（247 张经验卡加 14 条正式 Engineering Claims）。

## 30. 2026-08-11 原帖证据优先扩充（第二十三轮）

- 通过 GitHub 连接器完整读取 Isaac Lab #386/#2807/#3505、MuJoCo #2777/#3286/#3330 和 ros2_control #808/#649/#2758 的正文与全部 62 条公开 Issue 评论，并核对 MuJoCo commit `3434f5d`、ros2_control PR #1570/#2760 的完整 patch、非 bot 评论、测试与合并状态；新增 9 个来源、11 张工程经验卡，主手册由 247 张增至 258 张。
- Isaac Lab #386 被拆成两个未过度归因的实机问题：必须打印并逐项对齐 legged-gym/Orbit/实机的 joint ordering，作者确实发现 motor order 不同；作者把 GO1 actuator net 换成 PD 并重训后不再踢腿到 power protection，但两项改动没有单独消融，所以两张卡均保持 `partial / 值得参考`，并加入吊架、低增益、限幅和急停要求。
- Isaac Lab #3505 记录了 state-based 可复现、RGB 任务不可复现的多版本 A/B。作者的 PyTorch/cuDNN deterministic、`PYTHONHASHSEED`、`CUBLAS_WORKSPACE_CONFIG` 和双人 AA OFF/FXAA 复测均未解决；团队明确当前 rendering pipeline 为 stochastic。卡片不依赖曲线图片，也没有把未来 Isaac Sim 6.0/Newton 方向写成现有修复。
- MuJoCo #2777 对齐到正式 commit `3434f5d`：只通过 `contact pair` 碰撞的 mesh 过去没有计算 convex hull，提交修改编译路径并新增专门回归测试，因此达到 `可信度很高`。#3286 则按维护者逐行诊断保留为用户 Python factory 缩进错误：outer factory 返回 `None` 后 modifier 不执行，不能误写成 LuGre/sysid 库缺陷。
- MuJoCo #3330 同时展示 rigid flex 的能力和失败边界：简单模型确实得到 concave collision；复杂模型降到 40/5 FPS并在静态穿透时出现大量接触和 `findEdges` 错误。提高 `nconmax` 只消除 arena memory 警告、不能阻止退出，因此没有把 rigid flex 包装成复杂焊接场景的完整 Coal 替代。
- ros2_control #649 被拆成两层：组件级 `rw_rate` 已由合并 PR #1570 的实现、文档和测试正式支持，达到 `可信度很高`；单个 hardware component 内的高频位置/低频电压仍需拆 component 或在 `read` 内计数节流并复用缓存值，按 state interface 自动请求子集仍未实现。#808 只记录 Humble apt 与当时源码版的作者 A/B，明确 `master` commit 缺失和实时循环 `print` 的测量扰动。
- ros2_control #2758 的同接口控制器同时激活回归核对到 PR #2760：修复会在 mode switch 前检查当前/未来 command-interface 占用并提前失败。PR 初版没有解决原作者 UR 场景，修订后维护者跑过 UR tests、原作者确认 regression 修复、两位维护者批准并合并，因此达到 `可信度很高`。
- 本轮新增 3 张 `可信度很高`和 8 张 `值得参考`；全库当前分级为 41 / 164 / 53，答案状态为 104 个 `resolved`、118 个 `partial`、27 个 `unresolved`、9 个 `conflicting`，共 246 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 208 个 `reviewed`、923 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,606 个主题和 8,479 条原始证据：195 个 `ready`、3,341 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 272 个问题入口（258 张经验卡加 14 条正式 Engineering Claims）。

## 31. 2026-08-11 原帖证据优先扩充（第二十四轮）

- 通过 GitHub 连接器复审 Isaac Lab #904/#1384/#2054/#2391/#2635/#2963、Crocoddyl #743/#979 和 OCS2 #108 的正文与全部 70 条公开 Issue 评论，并核对 Isaac Lab PR #940/#1509/#1654/#1873/#2022/#2098/#2392 与 Crocoddyl PR #1067 的合并状态和源码补丁。9 个根来源共生成 10 张结构化卡：其中 6 个来源、7 张卡为净新增，#1384/#2054/#2391 的 3 张既有卡保留稳定 `problem_id` 并升级证据链；主手册由 258 张增至 265 张。
- Isaac Lab #904 拆成两个不混因的问题：环境 seed 必须早于 terrain、PhysX 和 buffer 构造，已由合并 PR #940 与同进程 observation/reward 测试闭环，达到 `可信度很高`；固定/seeded actions 加 2000 步 tensor hash 只能证明该用户同硬件环境一致、把剩余差异定位到 PPO，rough terrain 仍有未闭环报告，因此第二张卡为 `partial / 值得参考`。
- Isaac Lab #2054 沿用前轮直接读取的 USD `Max Force=88.0` 图片分析，并增加第二使用者独立现象、维护者确认、PR #2098 与合并提交引用；修复只说明 implicit actuator 未显式配置时继承 USD max effort，绝不把 1e9 或 USD 值当成实机安全力矩。#2391 则严格区分 per-term `_step_reward` stale value 与一直正确的 total `_reward_buf`，并保留 PR 未新增回归测试的限制。
- Isaac Lab #1384 不再停在过渡性的 PR #1509：卡片完整记录后续 #1654 引入 `velocity_limit_sim/effort_limit_sim`、#1873 回退 implicit actuator 的旧 `velocity_limit` 自动传播，明确 DCMotor no-load speed/torque-speed 语义与 PhysX hard clamp 必须分离，并绑定 0.34.0 附近版本而不声称永久当前行为。
- Isaac Lab #2635 对齐到合并 PR #2022：SB3 训练保存 `model_vecnormalize.pkl`，play 按 checkpoint 路径加载并设置 `training=False`、`norm_reward=False`，同时复用训练期 `agent.yaml`。#2963 只确认作者 instrumentation 观察到 GO1 ActuatorNet 每 sim step 调用；团队没有回答 50/200 Hz 应如何匹配，也无实机结果，因此保持 `unresolved / 需要实际验证`。
- Crocoddyl #979 中作者在 `JMinvJt_damping=0` 下把 Euler 换为 RK4 后文字确认飞行相角动量恢复恒定，两位维护者将其解释为 numerical integrator drift；由于缺少 commit、误差阈值和独立复现，等级为 `值得参考`。#743 只提炼有正式修复的 Armijo 子问题：PR #1067 修正 free-subspace gradient 与 convergence check；线程中 LLT/LDLT/PivLU 和未合并 speedup 观察没有被写成通用推荐。
- OCS2 #108 完整暴露社区冲突：一条回复称 hard inequality 使用 relaxed barrier，后续源码讨论又认为可能进入 HPIPM，原回复者随后承认只确认 equality path；没有维护者、版本化 MRE 或修复，故标为 `conflicting / 需要实际验证`，delta/mu 调参未被包装成答案，并加入独立 runtime monitor/command clamp 的硬件安全边界。
- 本轮净增 3 张 `可信度很高`、2 张 `值得参考`和 2 张 `需要实际验证`；全库当前分级为 44 / 166 / 55，答案状态为 108 个 `resolved`、119 个 `partial`、28 个 `unresolved`、10 个 `conflicting`，共 253 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 214 个 `reviewed`、917 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,611 个主题和 8,499 条原始证据：197 个 `ready`、3,344 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 279 个问题入口（265 张经验卡加 14 条正式 Engineering Claims）。

## 32. 2026-08-11 原帖证据优先扩充（第二十五轮）

- 通过 GitHub 连接器完整读取 Isaac Lab #4305/#3823/#5126/#5918/#5806/#4366/#4580、Crocoddyl #1104、TSID #165 和 OCS2 #34 的正文与全部 45 条公开 Issue 评论，同时核对 Isaac Lab PR #4306/#6377/#6378/#6384/#4604 与 TSID PR #218 的完整状态、补丁和必要审阅；新增 10 个来源、11 张工程经验卡，主手册由 265 张增至 276 张。
- Isaac Lab #4305 的 reset 首帧 IMU 尖峰对齐到已合并 #4306：补丁按 `env_ids` 清零 `_prev_lin_vel_w/_prev_ang_vel_w`，原作者确认首帧线加速度为重力、角加速度为零。#5126 的 nested URDF ContactSensor 初始化由 PhysX #6378 与 OVPhysX #6384 分别改成 per-body path expressions，并加入嵌套层级回归；#5918 则由 #6377 让 rigid-body/mass property writers 继续穿过 nested bodies。四张卡均有合并代码和精确测试/确认，达到 `可信度很高`。
- Isaac Lab #3823 修正了一个常见频率误解：explicit actuator 的 effort 随每次 sim-step `write_data_to_sim` 重新计算，target 通常才按 control frequency 更新；implicit PhysX PD 同样每个 sim step 重算。该回复只有维护者说明和随时间变化的 `main` 源码链接，所以为 `值得参考`，没有伪造固定版本的正式核验。
- Isaac Lab #5806 保留独立回复的关键因果边界：Newton/PhysX gain buffer 确有写入差异，proposed redirect 也被独立得到；但 stock Go2 的 `mjw_model.nu==0` 且 joints 为 EFFORT mode，nonzero gains 实际 inert，约 0.118 rad rest-pose 差不能归因于双控制器。Issue 仍开放，补丁未合并，因此只形成 `partial / 值得参考` 诊断卡。
- Isaac Lab #4366 完整展示冲突，不把参数经验包装成答案：原作者先称 compliance 3e5/3e2 有效，随后撤回推荐并把 dt=0.005 作为规避；另一用户却在 `0.005/4` 仍看到机器人飞起和 NaN。线程无维护者根因或修复，故为 `conflicting / 需要实际验证`，多张图片也没有被用于额外像素推断。
- Isaac Lab #4580 的固定 commit 调用链说明 permanent world force 只在 reset 时投影到 local frame，后续会随 body frame 转向；维护者认可问题，但开放 PR #4604 又被指出不能正确保持 permanent local-force rotation，作者也同意这一评审。因此只记录根因与验证方法，不把 #4604 写成修复。
- Crocoddyl #1104 按时间线采用最终维护者更正：constraints 下不能因 `dVexp<0` 跳过 `dV/tryStep`，否则会破坏 optimality/feasibility 权衡；早期相反建议不再适用。TSID #165 则拆成两张卡：已合并 #218 只闭环 two-frame rigid contact，任意 internal passive joints 仍需 formulation 的 torque-zero equality，不能用 zero torque-limit hack 或闭链 contact 代替。
- OCS2 #34 只提炼原帖可复用的 profiling 顺序：性能运行关闭昂贵的 numerical-stability eigenvalue checks，开启 phase summary，再按 adaptive stepping、LQ approximation 和 backward pass 定位；作者报告 input cost 调整降低 backward-pass 时间，但未给最终毫秒数，故不作 39-DoF 实时性能承诺。
- 本轮新增 4 张 `可信度很高`、6 张 `值得参考`和 1 张 `需要实际验证`；全库当前分级为 48 / 172 / 56，答案状态为 114 个 `resolved`、123 个 `partial`、28 个 `unresolved`、11 个 `conflicting`，共 264 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 224 个 `reviewed`、907 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,620 个主题和 8,524 条原始证据：199 个 `ready`、3,351 个 `needs_more_evidence`、70 个 `covered`；静态检索页为 290 个问题入口（276 张经验卡加 14 条正式 Engineering Claims）。

## 33. 2026-08-11 原帖证据优先扩充（第二十六轮）

- 通过 GitHub 连接器完整读取 MuJoCo #2155/#3258/#2774、Gazebo #3289/#2223 和 qpOASES #37/#47/#48/#50/#83 的正文与全部 56 条公开评论，并核对 DART PR #2493 的完整补丁、合并状态、审阅、测试覆盖和 MuJoCo Warp 官方 `ray` 文档；新增 10 个来源、10 张工程经验卡，主手册由 276 张增至 286 张。
- MuJoCo #2155 记录的是明确的后端能力决定：MJX 不计划支持 hfield ray casting，维护者指向官方 MuJoCo Warp `ray` 文档；没有把它扩写成两后端接口、性能或数值完全等价。#3258 同样只确认 MJX 当前不支持 batched `geom_dataid`，作者未公开的 monkey patch 不登记为有效修复。
- MuJoCo #2774 完整保留早期维护者解释与 2026 年逐行纠正之间的冲突。详细 frozen-state 记录显示 fallback 可能构造非正交 contact frame，差异集中在 pyramidal friction；但维护者只重新打开并表示会检查，尚无确认或合并修复，所以仍为 `conflicting / 需要实际验证`。
- Gazebo #3289 对齐到已合并 DART PR #2493：DART 6.16.5 把表示“使用全局默认值”的 slip-compliance `-1.0` sentinel 错误报警，6.16.6 修复后原作者复测告警消失，形成 `可信度很高` 卡。#2223 则同时展示原作者通过插件顺序解决和后续相同顺序仍失败的反例，不能把 `UserCommands` 置于 `Contact` 前包装成通用修复。
- qpOASES #37/#47/#83 分别沉淀 C++ row-major `A`、qpOASES_e 默认 50/100 静态维度上限和每次 `hotstart` 前重置 input/output `nWSR`；三项均只采用维护者明确写出的参数语义。#48 的 zero-stepsize 三步排查没有作者结果，因此保持 `partial / 需要实际验证`。
- qpOASES #50 中维护者收到作者 ACADO 导出代码后独立重放 300×300 QP，确认 QP 42/43 正常而 QP 44 Hessian 非正定并触发 Cholesky failure，达到 `可信度很高`；该结论没有外推为所有 ACADO/qpOASES internal error 的统一根因。
- 本轮新增 3 张 `可信度很高`、4 张 `值得参考`和 3 张 `需要实际验证`；全库当前分级为 51 / 176 / 59，答案状态为 121 个 `resolved`、124 个 `partial`、28 个 `unresolved`、13 个 `conflicting`，共 274 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 234 个 `reviewed`、897 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,631 个主题和 8,560 条原始证据：200 个 `ready`、3,360 个 `needs_more_evidence`、71 个 `covered`；静态检索页为 300 个问题入口（286 张经验卡加 14 条正式 Engineering Claims）。

## 34. 2026-08-11 原帖证据优先扩充（第二十七轮）

- 通过 GitHub 连接器完整读取 OSQP #43/#53/#97/#109/#125/#205/#255/#276/#376/#424/#609/#485 的正文与全部 63 条公开 Issue 评论，并核对 PR #256 的完整补丁、讨论、批准和合并提交；新增 12 个来源、12 张工程经验卡，主手册由 286 张增至 298 张。
- OSQP #109 通过维护者给出的不可行证书检查和约束违背数值，排除了 quadprog 返回向量为可行解的判断；原作者把有限下界 `-1000` 改为真正的 `-inf`/`-OSQP_INFTY` 后确认恢复。#125 则明确区分求解残差容差与 infeasibility tolerance：维护者对附件复跑 `eps_abs=eps_rel=1e-6`，迭代由 25 增至 125，约束违背降至约 `1e-14`/`1e-12`，并链接正式收敛与不可行性文档，因此达到 `可信度很高`。
- OSQP #205 将 MATLAB 与 codegen MEX 的迭代数差异定位到按运行时间触发的 adaptive rho；关闭自适应时两端均为 1225 次迭代，固定 `adaptive_rho_interval=25` 后原作者在原始和简化问题上确认一致。#376 则由维护者给出可运行代码，确认 `update` 必须保持初始化时的稀疏模式，`Ax` 按列优先非零项、`Px` 按 `triu(P)` 非零项传入；原作者确认此前更新方式错误。
- OSQP #43 只登记项目常量应使用 `OSQP_INFTY`，不把通用 `INFINITY` 当成 OSQP 定义；#53 保留病态 `P`（维护者计算 `cond(P)=9860981.74`）下收紧 `eps_abs/eps_rel` 可改善 OSQP/CVXOPT 一致性的复跑，但作者没有发布最终结果；#97 记录 ADMM 不保证有限步严格原始可行，以及 polishing 依赖正确 active-set guess，作者得到约 `5e-10` 的残差并认为够用，但 polishing 仍失败。
- OSQP #276 只采用原作者确认的两项缓解：把 `eps_abs/eps_rel=1e-8` 放宽到约 `1e-4`，并缩放条件数很大的 `P`；早期“warm-start 污染”只是未确认猜测，没有写成根因。#424 的首轮 CUDA NaN 最终由原作者定位到 `l/u` 的 double-to-float 转换产生 NaN/Inf，改为全 float 后原始 NaN 消失；后续 CPU/GPU 解和性能差异仍未闭环，卡片明确限制范围。
- OSQP #609 只把非负变量出现约 `-0.0131`、收紧到 `1e-7` 后仍有约百个负值且最小约 `-1e-4`、polishing 失败等原帖观测写入卡片；把负变量裁成零仅是带风险的后处理，必须重新检查全部一般约束 `Ax≤b`，因此为 `partial / 值得参考`。
- OSQP #255 与 #485 复用同一稳定 `problem_id` 并完整暴露冲突：历史 PR #256 将不可行性检查中的负 epsilon 改为正 epsilon、加入 `OSQP_DIVISION_TOL` 并合入 `develop-0.x`，该“历史修复事实”有正式补丁支撑；但 #485 指出正 epsilon 条件在 lhs=0 时可能误判 singleton feasible problem，且有第二位用户报告改回符号后才找到解。#485 无维护者回复和完整 MRE，聚合问题保持“需要实际验证”，不声称当前 OSQP 已普遍修复。
- 两张图片只用于限定原帖症状：#276 的运行时间/状态图没有被用于根因推断，#424 的截图只显示首轮 NaN；所有根因、操作和结果均来自帖子正文、明确评论或直接关联的正式补丁，没有从关闭标签、图片像素或作者未确认的建议补写结论。
- 本轮新增 2 张 `可信度很高`、9 张 `值得参考`和 1 张 `需要实际验证`；全库当前分级为 53 / 185 / 60，答案状态为 130 个 `resolved`、126 个 `partial`、28 个 `unresolved`、14 个 `conflicting`，共 285 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 246 个 `reviewed`、885 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,646 个主题和 8,601 条原始证据：203 个 `ready`、3,372 个 `needs_more_evidence`、71 个 `covered`；静态检索页应为 312 个问题入口（298 张经验卡加 14 条正式 Engineering Claims）。

## 35. 2026-08-11 原帖证据优先扩充（第二十八轮）

- 本轮从剩余候选中优先选择 WBC 实时执行和接触仿真线程，完整读取 ros_control #6/#8/#10/#130/#211、ros2_control #118/#1796/#2020/#2113/#3356、RaiSim #322 和 gz-sim #880 的正文与全部 64 条 Issue 评论，并核对 ros_control PR #209/#210、ros2_controllers PR #1215 的完整补丁、合并状态、审阅和测试；新增 12 个来源、13 张工程经验卡，主手册由 298 张增至 311 张。
- ros_control #6/#8/#10 被严格限制为旧 RTAI/ROS 1 实现经验：#6 只登记 `/proc/rtai/scheduler` + 逐段注释重编译的 syscall 定位法，维护者无定位的 `Fixed` 没有被扩写成 commit；#8 记录非实时线程阻塞等待同一发布锁时，实时线程 `unlockAndPublish()` 会进入 futex 路径；#10 只确认切换列表 `clear()` 被移出实时分支，不推断每次 `clear()` 必然分配。
- ros_control #130 拆为两张卡：一张保留 RTT `configureHook` 初始化、`updateHook` 执行 `read → update → write` 的外部实时执行器结构；另一张保留 per-component `CallbackQueue`、非实时 spinner 与 `RealtimeBuffer` 数据交接，并明确禁止非实时 callback 持有实时线程所需的普通锁。后续 `rtt_ros_control_example` 与 `hal_ros_control` 使用反馈只支持旧 ROS 1 架构，不外推为 ROS 2 模板。
- ros_control #211 对齐到硬件复现和已合并 PR #209/#210：`prepareSwitch()` 在非实时路径做可能耗时的准备，`doSwitch()` 与 controller start/stop 在实时 `update()` 中提交并必须非阻塞。ros_canopen 参与者确认修订后的 Indigo 变更符合预期，因此达到 `可信度很高`；同时完整保留慢速 CANopen 需 3–4 个或更多周期、首批新命令可能丢失的适用边界，绝不写成任意硬件单周期完成物理切换。
- ros2_control #118 只把一台 Linux 5.4.47 PREEMPT_RT 主机的 `cyclictest` A/B 作为基线方法：不含 ACPI 时四线程 Max 为 30–45 µs，含 ACPI 时作者报告 7000–8000 µs；自动化 ros2_control 实时测试仍未完成，也没有把关闭 ACPI 包装成通用生产优化。
- ros2_control #1796 对齐到已合并 ros2_controllers PR #1215：`ForceTorqueSensorBroadcaster` 新增六轴 offset 参数、运行期刷新、chainable state interfaces 和单元测试，达到 `可信度很高`；原作者当时在 Humble 无法构建，故明确限定为包含 merge commit `4343c7a` 的版本，不声称已经 backport。#2020 则完整保留 `memlock 102400` 失败、`1024000` 启动后 `bad_alloc`、`unlimited` 可用和 `lock_memory=false` 放弃锁内存保证的差异，没有推荐任意固定倍数。
- ros2_control #2113 由维护者版本说明、官方 demo 源码和原作者 Jazzy/Foxglove 复测闭环：hardware component 使用 `get_logger()` 后日志进入 rosout，达到 `可信度很高`，但不外推到 Iron，也不允许在实时 read/write 路径高频打印。#3356 只有原作者逐项排除和 overlay A/B：禁用两个 pal_statistics registry/publish 路径后进程约从 13% 降到 1%；没有维护者结论或合并修复，且本地 patch 会删除观测 topic，因此保留 `partial / 值得参考`。
- RaiSim #322 明确保留失败结果：`dt=0.001 s` 和多组 ERP 对作者均无改善；项目作者建议时间滤波和更大碰撞网格三角形，却没有作者复测，降低摩擦更被明确标注为未测试。因此该卡为 `partial / 需要实际验证`，没有补写滤波 cutoff、ERP 范围或稳定性结论。gz-sim #880 也只把 Focal DART 6.9.2-2build4 与 Bionic Gazebo fork 的摩擦支持差异、三条版本 workaround 作为排查入口，原作者未回报结果。
- 本轮涉及的图像/GIF只在原帖中表达 syscall 后的观测界面、接触力跳变或 skid-steer 运动症状；卡片的原因、操作和结果均来自正文、明确评论或正式补丁，没有从图片像素反推参数和根因。
- 本轮新增 3 张 `可信度很高`、9 张 `值得参考`和 1 张 `需要实际验证`；全库当前分级为 56 / 194 / 61，答案状态为 138 个 `resolved`、131 个 `partial`、28 个 `unresolved`、14 个 `conflicting`，共 298 个稳定 `problem_id`。
- 候选索引仍为 1,131 个唯一 URL，其中 258 个 `reviewed`、873 个 `technical_pending`、0 个 `excluded`；查询前沿为 3,657 个主题和 8,637 条原始证据：208 个 `ready`、3,378 个 `needs_more_evidence`、71 个 `covered`；静态检索页应为 325 个问题入口（311 张经验卡加 14 条正式 Engineering Claims）。
