# WBC 工程经验全量展示、分级与候选清单规范

本规范持续约束社交平台与 GitHub Issues 的开发。它适用于中文和英文原帖；整理内容始终以中文为主，专业术语使用 `中文（English, ABBR）`。点赞、浏览、收藏和作者粉丝数不参与任何等级判定。

## 五个互不替代的概念

1. **展示范围**：所有发现的 WBC 子话题、工程问题和技术候选均可查看；不以等级隐藏内容。
2. **搜索调度**：每次用户触发的运行仍有平台查询、详情页、回复和时间预算；预算不是展示上限。
3. **可信度**：说明一条经验或一个问题获得了哪些核验，不等同于答案是否闭环。
4. **解答状态**：`resolved / partial / unresolved / conflicting` 描述原线程给出的解决进度。
5. **正式结论**：社区经验只有通过现有 primary/secondary evidence gate 才能成为 `EngineeringClaim`；可信度等级本身没有升级权限。

## 全量查询前沿

`query-frontier.json` 保存全部去重主题和全部触发根来源，不对主题数或单主题来源数做用户可见截断。主题状态固定为：

- `ready`：证据达到默认自动搜索门槛；
- `needs_more_evidence`：已发现但证据尚少，仍完整展示；
- `covered`：固定查询已经覆盖，继续展示但默认不重复生成查询。

每轮选择顺序为“从未搜索 → 上轮新增证据 → 到期刷新 → scope 轮询”。连续零结果继续指数退避；登录、验证码、风控和不可访问属于 blocker，不伪装成零结果。未被本轮预算选中的 `ready` 主题保留在前沿，后续继续轮转。

完整前沿由下列命令生成：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-frontier-report \
  --frontier var/social-state/query-frontier.json \
  --state var/social-state/discovery.json \
  --output content/social-query-frontier.md
```

使用者可从完整清单中定向选择下一轮，不受默认状态限制：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-browser-plan --platform x --topic <topic_id>
PYTHONPATH=src python3 -m wbc_handbook github-issue-plan --topic <topic_id>
```

## 经验级三级制

每张 `engineering_qa` 必须增加稳定 `problem_id`、`problem_title_zh`、`verification_refs` 和 `credibility`。可见等级只能是：

| 等级 | 判定标准 |
|---|---|
| `可信度很高` | 问题已闭环、环境明确、无冲突，并有正式资料交叉核验或独立复现的精确引用；依赖图片时图片已经完成分析 |
| `值得参考` | 环境、症状、处理过程和结果形成完整工程记录，或得到作者/维护者确认，但尚缺正式资料交叉核验或独立复现 |
| `需要实际验证` | 单一经验、环境或结果缺失、尚未复现、仅有问题线索、依赖未读清图片，或处于 unresolved/conflicting 状态 |

### 原帖保真与禁止补写

工程卡必须能从原帖正文、精确评论/回复、原帖图片或原帖直接关联的 PR/commit 中逐项追溯。整理者不得用领域常识替原作者补齐根因、修复步骤、结果或适用范围。

- 原帖没有说明的字段保持空数组，或在中文答案中明确写“原帖未说明”；不得为了让卡片看起来完整而推测。
- 只有建议、没有复测结果时，建议可以作为排查入口展示，但解答保持 `unresolved` 或 `partial`，不得改写成 `effective_fixes`。
- 来自评论的结论必须保存精确 `#issuecomment-<id>` 或平台可提供的回复定位；不同用户、不同机器人和不同版本的经验分别标注，不合并成一个统一结论。
- 外部论文、源码、官方文档或 PR 只能作为 `verification_refs` 单独标识；不得把外部资料中的解释冒充为原帖作者的说法。
- 图片承担参数、日志、曲线或结构证据时必须完成图片分析；没有读清时设置 `visual_evidence_required=true`、`visual_evidence_verified=false`，且不得抄写无法确认的数值。
- 每个捕获批次保留读取范围和停止原因；纯提问、只有“我也遇到”或离题回复的候选继续留在 `technical_pending`，不为增加卡片数量而制造答案。

结构如下：

```json
{
  "problem_id": "problem.optimization_ik_qp_mpc.<stable-id>",
  "problem_title_zh": "QP 求解不可行时如何定位？",
  "credibility": {
    "computed_grade": "值得参考",
    "final_grade": "值得参考",
    "rationale_zh": "环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。",
    "basis": {
      "source_basis": "engineering_practice_record",
      "reproduction": "steps_and_results_complete",
      "applicability": "environment_clear",
      "independent_source_ids": [],
      "conflict_present": false,
      "visual_evidence_required": false,
      "visual_evidence_verified": false
    }
  },
  "verification_refs": []
}
```

`source_basis` 使用 `primary_cross_checked / maintainer_or_author_confirmed / engineering_practice_record / problem_signal_only`；`reproduction` 使用 `independent_reproduction / original_thread_confirmation / steps_and_results_complete / not_reproduced`；`applicability` 使用 `environment_version_match / environment_clear / partially_clear / environment_unknown`。

规则先生成 `computed_grade`。审阅者可以调整 `final_grade`，但等级不同就必须填写 `override_rationale_zh`。升级到 `可信度很高` 必须提供可定位的论文、官方文档、源码、PR 或独立复现引用；存在冲突、环境未知或关键图片未分析时不能升级。`verification_refs` 中每项必须包含 `relation`、精确 `locator`，以及 `source_id` 或绝对 `source_url` 二者之一。

## 问题级综合等级

手册按 `problem_id` 聚合同一问题的全部经验。同一 scope 内只有组件、症状和适用环境一致时才合并；不能确认一致的近似问题保持分开。

- 至少一条 `可信度很高` 经验已有正式核验或独立支持，且无冲突：问题为 `可信度很高`；
- 至少一条 `值得参考` 或更高经验，且无未解决冲突：问题为 `值得参考`；
- 只有待验证经验，或不同来源结论冲突：问题为 `需要实际验证`。

每个问题下必须完整列出全部经验，包括相互冲突的来源。每条都保留独立等级和理由、解答状态、环境、症状、原因、处理、结果、限制、图片分析以及原帖或精确回复链接。

## 最小化全量候选索引

`data/social-candidate-index.json` 是可提交、可审计的唯一候选清单。它只保存 canonical URL、标题、平台、scope、查询来源、首次/最近发现时间、审阅状态和关联问题 ID；禁止保存正文、完整评论、Cookie、凭据、原始 DOM 或临时媒体地址。

状态固定为：

- `reviewed`：已进入问题手册；
- `technical_pending`：技术相关但尚未完成结构化整理；无法确定时保守归入这里；
- `excluded`：广告、营销、离题、重复或没有工程信息，必须记录中文原因。

构建与生成报告：

```bash
PYTHONPATH=src python3 -m wbc_handbook social-inventory \
  var/github-issues/candidates.json \
  var/social-browser/candidates.json \
  --decisions var/social-review/triage-decisions.json \
  --output data/social-candidate-index.json

PYTHONPATH=src python3 -m wbc_handbook social-report \
  --data-dir data \
  --inventory data/social-candidate-index.json \
  --output content/social-engineering-candidates.md \
  --pending-output content/social-engineering-pending
```

主手册只放 `reviewed` 的结构化经验；`technical_pending` 在待整理首页和 scope 分页中完整展示原链接；`excluded` 不进入主手册，但继续保留 URL 和中文原因，并显示原因分布。任何状态变化都必须可审计，不允许静默丢弃。

## 每次改动的验收不变量

- 前沿主题数、触发来源数、问题数、经验数、候选数和排除数均可从生成物重新统计；
- 单轮计划遵守预算，但多轮轮转不会永久饿死 `ready` 主题；
- 每张经验卡都有等级、中文理由和原帖/精确回复链接；
- 图片参与结论而未完成分析时，等级保持 `需要实际验证`；
- 所有技术候选最终只能处于三种审阅状态之一；
- 社交经验不因等级自动进入正式结论；
- 用户可见文档只使用本规范的三个等级名称，不引入数值分数或贬损性标签。
