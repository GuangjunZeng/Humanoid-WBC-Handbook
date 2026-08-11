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
