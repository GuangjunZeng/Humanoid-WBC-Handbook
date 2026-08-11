# WBC 社交平台工程问题查询手册

> 生成时间：2026-08-11T03:52:49+08:00。所有已发现经验均按问题聚合并完整展示；等级仅说明核验基础，不会自动升级为正式 `EngineeringClaim`。

## 等级与使用

- `可信度很高`：问题闭环、环境明确、无冲突，并有正式资料交叉核验或独立复现；依赖图片时图片已完成分析。
- `值得参考`：环境、症状、处理和结果形成完整工程记录，但尚缺正式交叉核验或独立复现。
- `需要实际验证`：单一经验、信息缺项、尚未复现、图片尚待分析，或结论仍有冲突。
- 点赞、浏览、收藏和作者粉丝数不参与等级判定。
- 无论原帖是中文还是英文，整理均以中文为主；关键术语采用 `中文（English, ABBR）`。
- `community_candidate`、`issue_candidate` 与 `partial_visible` 分别表示来源类型和采集可见范围，不替代可信度或解答状态。
- 更新按需触发：查询前沿、搜索调度、可信度、解答状态和正式结论是五个互不替代的概念。

## 总览

- 已审阅来源：146
- 工程问题：179；工程经验：189
- 经验等级：可信度很高 22 / 值得参考 123 / 需要实际验证 44
- 解答状态：resolved 63 / partial 93 / unresolved 26 / conflicting 7
- Scope 覆盖：32/32

| 工程范围 | `scope_id` | X | 知乎 | 小红书 | GitHub Issues | 问题 | 经验 | 需实际验证 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 开放式 WBC 工程经验 | `open_ended_wbc_field_notes` | 1 | 1 | 1 | 0 | 5 | 5 | 1 |
| 安装、依赖与版本兼容 | `environment_setup_dependencies` | 1 | 3 | 1 | 2 | 10 | 12 | 4 |
| 仿真器与工具链 | `simulation_toolchain` | 1 | 0 | 1 | 3 | 5 | 6 | 2 |
| 训练不稳定与崩溃 | `training_instability` | 1 | 0 | 1 | 0 | 2 | 2 | 0 |
| 奖励、课程与随机化 | `reward_curriculum_randomization` | 1 | 1 | 0 | 2 | 6 | 6 | 1 |
| 性能、显存与并行仿真 | `compute_performance_memory` | 0 | 1 | 1 | 2 | 5 | 5 | 3 |
| 动作重定向与数据质量 | `retargeting_and_dataset` | 2 | 1 | 0 | 0 | 3 | 3 | 0 |
| 跟踪与遥操 | `tracking_and_teleoperation` | 1 | 1 | 1 | 0 | 3 | 3 | 2 |
| 状态估计、标定与时间同步 | `state_estimation_calibration` | 1 | 1 | 0 | 6 | 9 | 9 | 2 |
| 通信、时延与实时性 | `communication_and_realtime` | 0 | 1 | 1 | 0 | 2 | 2 | 1 |
| sim-to-sim 与 sim-to-real | `sim_to_sim_and_sim_to_real` | 2 | 1 | 1 | 4 | 12 | 12 | 2 |
| 足式运动、接触与地形 | `locomotion_contact_terrain` | 1 | 0 | 0 | 3 | 4 | 4 | 2 |
| IK/QP/MPC/WBC 优化问题 | `optimization_ik_qp_mpc` | 1 | 2 | 1 | 15 | 23 | 26 | 3 |
| 力控、接触操作与载荷 | `force_control_manipulation` | 1 | 1 | 1 | 1 | 6 | 6 | 2 |
| 电机、减速器、温升与磨损 | `hardware_actuator_thermal` | 1 | 0 | 1 | 1 | 3 | 5 | 2 |
| 部署、固件与 SDK | `deployment_firmware_sdk` | 2 | 1 | 0 | 0 | 6 | 6 | 0 |
| 安全、跌倒、冲击与起身 | `safety_fall_recovery` | 2 | 0 | 1 | 0 | 3 | 3 | 2 |
| 传感器与感知接口 | `sensing_and_perception` | 1 | 0 | 1 | 0 | 2 | 2 | 0 |
| 复现、日志、评估与调试方法 | `reproducibility_and_debugging` | 1 | 0 | 0 | 0 | 1 | 1 | 0 |
| 机械集成、负载与配重 | `mechanical_payload_integration` | 0 | 1 | 0 | 1 | 2 | 2 | 0 |
| communication_realtime_control | `communication_realtime_control` | 0 | 2 | 0 | 0 | 5 | 5 | 5 |
| contact_force_friction | `contact_force_friction` | 0 | 0 | 0 | 8 | 11 | 11 | 3 |
| debugging_logging_reproducibility | `debugging_logging_reproducibility` | 0 | 0 | 0 | 2 | 2 | 2 | 1 |
| dynamics_mass_inertia_actuation | `dynamics_mass_inertia_actuation` | 0 | 0 | 0 | 1 | 1 | 1 | 0 |
| dynamics_model_validation | `dynamics_model_validation` | 0 | 0 | 0 | 1 | 1 | 1 | 0 |
| hardware_actuator_thermal_power | `hardware_actuator_thermal_power` | 0 | 0 | 0 | 8 | 8 | 8 | 1 |
| joint_mapping_frames_conventions | `joint_mapping_frames_conventions` | 0 | 0 | 0 | 12 | 14 | 16 | 3 |
| model_asset_and_urdf_usd | `model_asset_and_urdf_usd` | 0 | 0 | 0 | 4 | 4 | 4 | 0 |
| realtime_control_latency | `realtime_control_latency` | 0 | 0 | 0 | 6 | 6 | 6 | 0 |
| retargeting_dataset_quality | `retargeting_dataset_quality` | 0 | 0 | 0 | 5 | 5 | 5 | 0 |
| simulator_physics_numerics | `simulator_physics_numerics` | 0 | 0 | 0 | 2 | 2 | 2 | 1 |
| training_reward_curriculum | `training_reward_curriculum` | 0 | 1 | 0 | 4 | 8 | 8 | 1 |

平台列是已审阅入库来源数；全部技术候选见待整理附录。

## 开放式 WBC 工程经验 (`open_ended_wbc_field_notes`)

### Unitree G1 反复做 IMU/电机标定仍左右摇摆、走不直时，还应检查什么？

- `problem_id`：`problem.open_ended_wbc_field_notes.8168315f470015df`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：被Unitree G1标定搞到崩溃的一周**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：该案例最终把问题指向实验室固件版本过旧；更新后作者称明显改善。因此在重复标定无效时，应记录并核对控制器/机器人固件版本与兼容矩阵，再决定是否继续调 IMU 或 pelvis 参数。原帖未给出具体版本号，仍需官方文档或 Issue 验证。
- 证据状态：`community_candidate`
- 来源定位：正文及评论区作者 02-26 的“破案了”更新
- 原帖/精确回复：[被Unitree G1标定搞到崩溃的一周](https://www.xiaohongshu.com/explore/699e2081000000001a01d6aa)
- 平台/作者：Xiaohongshu / 意大利在逃番茄王子🍅
- 关键术语：全身控制（Whole-Body Control, WBC）；状态估计（State Estimation）；惯性测量单元（Inertial Measurement Unit, IMU）；软件开发工具包（Software Development Kit, SDK）；执行器（Actuator）
- 环境：Unitree G1 实验室真机，遥控行走模式，设备位于标定/支撑架附近。
- 症状：左右摇摆明显、走不直、机身歪；修改 pelvis 角度未见即时效果。
- 诊断：重复用水平仪校准 IMU，并进行全身电机标定；随后核对实验室固件版本。
- 原因：实验室设备固件版本过旧。
- 处理过程：多次 IMU 调平、全身电机 Calibration、修改 pelvis 角度。
- 有效处理：升级 G1 实验室固件版本。
- 结果：作者评论称更新固件后‘好多了’，但没有量化直线误差或摇摆幅度。
- 限制：没有披露旧/新固件版本号、升级步骤和是否完全恢复。
- 安全提示：严重摇摆时应停止自由行走，在安全架或防护区域完成固件与标定检查。
- 图片分析：可见图片显示 Unitree G1 位于实验室支撑/标定装置旁，说明问题发生在真机调试环境；画面没有显示固件版本、标定参数或日志，因此不能从图片确认根因。
- 采集完整性：`partial_visible`；可见回复 4；展开 0 次；回复深度 2/10；停止原因：all_visible_comments_loaded
- 适用边界：适用于症状突然出现且重复标定无效的 G1；其他型号不能直接套用。

### 该 weighted-QP WBC 为什么没有保留支撑腿静止约束？

- `problem_id`：`problem.open_ended_wbc_field_notes.1a729932fc089eb6`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：【开源】基于NMPC和WBC的双足机器人控制框架简介**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：评论说明 Legged Control 原库除接触力跟踪外还有支撑腿不移动约束，但本框架作者在调试时加入该约束会出问题，因此将其去掉。现有内容没有证明移除后在所有接触工况都正确，也没有给出导致冲突的具体约束残差。
- 证据状态：`community_candidate`
- 来源定位：评论区“为什么 wbc 中没有支撑腿约束”回复串
- 原帖/精确回复：[【开源】基于NMPC和WBC的双足机器人控制框架简介](https://zhuanlan.zhihu.com/p/686462478)
- 平台/作者：Zhihu / mcpocket
- 关键术语：全身控制（Whole-Body Control, WBC）；二次规划（Quadratic Programming, QP）；模型预测控制（Model Predictive Control, MPC）；状态估计（State Estimation）；统一机器人描述格式（Unified Robot Description Format, URDF）；关节力矩（Joint Torque）
- 环境：MuJoCo 仿真；OCS2 NMPC；Pinocchio 动力学；qpOASES weighted-QP WBC；SolidWorks 导出 URDF。
- 症状：自有模型的足端轨迹方向异常或 dummy 节点不响应指令。；一条评论测得 LQ Approximation 1528.7 ms，占 SQP 总时间 93.5049%。
- 诊断：先用 OCS2 dummy 隔离 MPC，再用 Cheat Controller 直接读取仿真真值隔离状态估计器。；检查 URDF 转动惯量、足端运动学约束及 weighted-QP 的 H 矩阵权重。
- 原因：SolidWorks URDF 插件直接导出的惯量矩阵可能错误。；支撑腿静止约束在该作者调试时导致问题，因而被移除；SQP 线性化瓶颈尚无确认原因。
- 处理过程：作者先完成 Cheat Controller，再加入并调稳线性卡尔曼状态估计器。；从 SolidWorks 质量属性按 link 坐标系和负张量记法重新填写惯量。
- 有效处理：对模型迁移，采用 dummy→Cheat Controller→状态估计器的分层验证，并修正惯量参数。
- 结果：原作者报告仿真框架能够稳定运行；支撑腿约束和 SQP 线性化慢的问题没有给出复现后的最终修复。
- 限制：主要证据来自仿真与评论区，未提供同一流程在真实人形机器人和高速运动下的独立验证。
- 安全提示：错误惯量、接触约束或状态估计不得直接上实机，应先在 dummy 和仿真中验证力矩、接触力及限位。
- 采集完整性：`partial_visible`；可见回复 21；展开 2 次；回复深度 2/10；停止原因：no_visible_expand_controls
- 适用边界：只描述该仓库的工程取舍，不能推广为 WBC 通用设计结论。

### 迁移 OCS2 NMPC + weighted-QP WBC 到自有机器人时，推荐怎样分层调试？

- `problem_id`：`problem.open_ended_wbc_field_notes.b87fed5e4994737d`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：【开源】基于NMPC和WBC的双足机器人控制框架简介**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：候选流程是先在 OCS2 dummy 节点验证最优控制问题（Optimal Control Problem, OCP），再用 Cheat Controller 读取仿真真值验证控制器，最后接入状态估计器；同时不要直接信任 SolidWorks URDF 插件生成的惯量矩阵，应按质量属性、link 坐标系和负张量记法重新计算。
- 证据状态：`community_candidate`
- 来源定位：正文“仿真环境”“MPC部分”“状态观测器”及模型迁移评论串
- 原帖/精确回复：[【开源】基于NMPC和WBC的双足机器人控制框架简介](https://zhuanlan.zhihu.com/p/686462478)
- 平台/作者：Zhihu / mcpocket
- 关键术语：全身控制（Whole-Body Control, WBC）；二次规划（Quadratic Programming, QP）；模型预测控制（Model Predictive Control, MPC）；状态估计（State Estimation）；统一机器人描述格式（Unified Robot Description Format, URDF）；关节力矩（Joint Torque）
- 环境：MuJoCo 仿真；OCS2 NMPC；Pinocchio 动力学；qpOASES weighted-QP WBC；SolidWorks 导出 URDF。
- 症状：自有模型的足端轨迹方向异常或 dummy 节点不响应指令。；一条评论测得 LQ Approximation 1528.7 ms，占 SQP 总时间 93.5049%。
- 诊断：先用 OCS2 dummy 隔离 MPC，再用 Cheat Controller 直接读取仿真真值隔离状态估计器。；检查 URDF 转动惯量、足端运动学约束及 weighted-QP 的 H 矩阵权重。
- 原因：SolidWorks URDF 插件直接导出的惯量矩阵可能错误。；支撑腿静止约束在该作者调试时导致问题，因而被移除；SQP 线性化瓶颈尚无确认原因。
- 处理过程：作者先完成 Cheat Controller，再加入并调稳线性卡尔曼状态估计器。；从 SolidWorks 质量属性按 link 坐标系和负张量记法重新填写惯量。
- 有效处理：对模型迁移，采用 dummy→Cheat Controller→状态估计器的分层验证，并修正惯量参数。
- 结果：原作者报告仿真框架能够稳定运行；支撑腿约束和 SQP 线性化慢的问题没有给出复现后的最终修复。
- 限制：主要证据来自仿真与评论区，未提供同一流程在真实人形机器人和高速运动下的独立验证。
- 安全提示：错误惯量、接触约束或状态估计不得直接上实机，应先在 dummy 和仿真中验证力矩、接触力及限位。
- 采集完整性：`partial_visible`；可见回复 21；展开 2 次；回复深度 2/10；停止原因：no_visible_expand_controls
- 适用边界：适用于 OCS2/Pinocchio/MuJoCo 类模型驱动双足控制框架；尚未在具体自有实机上独立复现。

### 更换模型后 OCS2 SQP 的 LQ Approximation 占 93.5% 且机器人不动，如何解决？

- `problem_id`：`problem.open_ended_wbc_field_notes.f3b9e42ea768b51b`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：【开源】基于NMPC和WBC的双足机器人控制框架简介**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：原评论仅给出性能分解：LQ Approximation 1528.7 ms、Solve QP 8.36 ms，未得到作者确认的根因或修复。可据此把排查重点放在线性化、自动微分模型、URDF 惯量/运动学与约束导数，但这些是待验证方向，不是原帖已解决方案。
- 证据状态：`community_candidate`
- 来源定位：评论区包含 SQP Benchmarking 的提问
- 原帖/精确回复：[【开源】基于NMPC和WBC的双足机器人控制框架简介](https://zhuanlan.zhihu.com/p/686462478)
- 平台/作者：Zhihu / mcpocket
- 关键术语：全身控制（Whole-Body Control, WBC）；二次规划（Quadratic Programming, QP）；模型预测控制（Model Predictive Control, MPC）；状态估计（State Estimation）；统一机器人描述格式（Unified Robot Description Format, URDF）；关节力矩（Joint Torque）
- 环境：MuJoCo 仿真；OCS2 NMPC；Pinocchio 动力学；qpOASES weighted-QP WBC；SolidWorks 导出 URDF。
- 症状：自有模型的足端轨迹方向异常或 dummy 节点不响应指令。；一条评论测得 LQ Approximation 1528.7 ms，占 SQP 总时间 93.5049%。
- 诊断：先用 OCS2 dummy 隔离 MPC，再用 Cheat Controller 直接读取仿真真值隔离状态估计器。；检查 URDF 转动惯量、足端运动学约束及 weighted-QP 的 H 矩阵权重。
- 原因：SolidWorks URDF 插件直接导出的惯量矩阵可能错误。；支撑腿静止约束在该作者调试时导致问题，因而被移除；SQP 线性化瓶颈尚无确认原因。
- 处理过程：作者先完成 Cheat Controller，再加入并调稳线性卡尔曼状态估计器。；从 SolidWorks 质量属性按 link 坐标系和负张量记法重新填写惯量。
- 有效处理：对模型迁移，采用 dummy→Cheat Controller→状态估计器的分层验证，并修正惯量参数。
- 结果：原作者报告仿真框架能够稳定运行；支撑腿约束和 SQP 线性化慢的问题没有给出复现后的最终修复。
- 限制：主要证据来自仿真与评论区，未提供同一流程在真实人形机器人和高速运动下的独立验证。
- 安全提示：错误惯量、接触约束或状态估计不得直接上实机，应先在 dummy 和仿真中验证力矩、接触力及限位。
- 采集完整性：`partial_visible`；可见回复 21；展开 2 次；回复深度 2/10；停止原因：no_visible_expand_controls
- 适用边界：适用于出现同类 OCS2 SQP 性能分解的模型迁移案例。

### 评估统一 whole-body policy 时，为什么要把 progress 与 full success 分开？

- `problem_id`：`problem.open_ended_wbc_field_notes.9db00d01d494f2f4`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ω-0 全身多任务策略：成功率与进展率必须分开**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该线程显示 ω-0 的 progress 约 90.3%，而完全成功约 81.8%；模型可能已推进任务却仍未满足成功标准。应同时报告两者并分类失败，而不是只看头条成功率。
- 证据状态：`community_candidate`
- 来源定位：根帖与 @ManpreetBola 对 Table 2 的回复
- 原帖/精确回复：[ω-0 全身多任务策略：成功率与进展率必须分开](https://x.com/manpreetbola/status/2086708892873232510)
- 平台/作者：X / Jianfei Yang @Jianfei_AI
- 关键术语：关节力矩（Joint Torque）；质心（Center of Mass, CoM）
- 环境：40+ 小时；24 任务；4,827 片段；11 项实机评估。
- 症状：progress 90.3% 高于 full success 81.8%，存在未完成尾部。
- 诊断：同时报告 progress、full success、任务分项与失败类型。
- 原因：模型能推进任务但未满足最终判定。
- 处理过程：统一模型同时生成全身动作并预测视觉 latent。
- 结果：根帖报告 81.8% 实机成功；回复称 ψ-0 44.5%、progress 90.3%。
- 限制：数值需论文 Table 2 核对；帖子未给控制层失败分类。
- 安全提示：多任务成功率不能替代力矩、碰撞和跌倒安全评估。
- 图片分析：截图清楚显示 40+ 小时、24 任务、4,827 片段和 81.8% 等文本指标；没有 Table 2 或失败分布。
- 采集完整性：`partial_visible`；可见回复 3；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于全身多任务/长时序人形策略评测。

## 安装、依赖与版本兼容 (`environment_setup_dependencies`)

### Isaac Sim/Lab 安装后出现 CUDA 动态库符号错误，应该先查什么？

- `problem_id`：`problem.environment_setup_dependencies.1b7f93e80405e892`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Sim 5.1 / Isaac Lab 2.3.2 三种安装路径与 CUDA 冲突处理**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该帖的可操作做法是先核对 Python、Isaac Sim、PyTorch/CUDA 与 Isaac Lab 提交是否成套，再检查 LD_LIBRARY_PATH 是否把系统 CUDA 库置于 Isaac Sim 自带库之前；Binary 路径下可临时 unset LD_LIBRARY_PATH 后重试，并用 create_empty.py 分层验证。远程 GUI 问题仍需单独核对图形栈。
- 证据状态：`community_candidate`
- 来源定位：正文“方式1/2/3”及 libcusparse 报错段落
- 原帖/精确回复：[Isaac Sim 5.1 / Isaac Lab 2.3.2 三种安装路径与 CUDA 冲突处理](https://zhuanlan.zhihu.com/p/2010051873546183158)
- 平台/作者：Zhihu / 糯米词​​
- 关键术语：统一计算设备架构（Compute Unified Device Architecture, CUDA）
- 环境：Python 3.11；Isaac Sim 5.1.0；PyTorch 2.7.0 + CUDA 12.8；Isaac Lab 2.3.2 示例提交。
- 症状：Binary 安装可能报 libcusparse.so.12 的 undefined symbol；远程/headless 用户评论无法看到 GUI。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：系统 CUDA/LD_LIBRARY_PATH 与 Isaac Sim 自带 CUDA 库冲突；远程环境缺少可用图形栈。
- 处理过程：固定版本、执行 create_empty.py 和 Ant/ANYmal 训练作为分层验证；冲突时临时 unset LD_LIBRARY_PATH。
- 结果：正文给出可执行命令链；评论中的远程 GUI 问题没有统一解法。
- 限制：版本组合会过时；没有提供完整硬件/驱动矩阵。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：正文媒体位与命令块共同说明三种安装路径；关键可执行信息是版本锁定、_isaac_sim 符号链接和 LD_LIBRARY_PATH 排查，图片本身未提供性能曲线。
- 采集完整性：`partial_visible`；可见回复 1；展开 0 次；回复深度 1/10；停止原因：no_visible_expand_controls
- 适用边界：版本组合会过时；没有提供完整硬件/驱动矩阵。

### Isaac Sim/Lab 安装完成却在首次验证或训练时卡死，如何判断是安装还是资产问题？

- `problem_id`：`problem.environment_setup_dependencies.8ea75a6b0d4021e4`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 2.0 安装后卡死：S3 资产与本地缓存路径排查**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先看进程是否在拉取云端 USD 资产，再把资产包离线下载并让 isaacsim.exp.base.kit、user.config.json 指向本地目录；随后把 Isaac Sim 资产加载与 Isaac Lab 训练分开验证。远程无 GUI 属于另一个问题，不能用这套资产修复代替图形栈诊断。
- 证据状态：`community_candidate`
- 来源定位：正文图2–图12说明及远程服务器评论
- 原帖/精确回复：[Isaac Lab 2.0 安装后卡死：S3 资产与本地缓存路径排查](https://www.xiaohongshu.com/explore/67cd7b7d0000000029012c40)
- 平台/作者：Xiaohongshu / 今天又学2小时
- 关键术语：强化学习（Reinforcement Learning, RL）
- 环境：Isaac Sim 4.5；Isaac Lab 2.0；pip；国内网络；本地或远程 Ubuntu/Windows 场景。
- 症状：Isaac Sim/Isaac Lab 验证或 RL 训练阶段卡死，看起来像安装失败；远程服务器看不到 GUI。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：默认从 Amazon S3 拉 USD 资产；pip 未升级导致缺模块；远程环境缺可用图形/streaming。
- 处理过程：升级 pip，下载资产包并配置本地资产目录，再分别验证 Isaac Sim 资产页和 Isaac Lab 训练。
- 结果：作者称本地训练可正常启动；评论中的 headless 回放/远程 GUI 没有统一解法。
- 限制：图中具体配置值未逐字符导出；版本固定且会过时。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：14 个图位按正文图2–12串起 pip、离线资产包、isaacsim.exp.base.kit、user.config.json 与训练验证；关键配置含本地资产路径，但未逐字符 OCR 复写图片。
- 采集完整性：`partial_visible`；可见回复 35；展开 6 次；回复深度 2/10；停止原因：all_visible_comments_loaded
- 适用边界：图中具体配置值未逐字符导出；版本固定且会过时。

### 想保留 Isaac Lab 风格 API、但减少 Isaac Sim 依赖时，mjlab 提供了什么？

- `problem_id`：`problem.environment_setup_dependencies.942f699f52388d1e`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：用 mjlab 降低 Isaac Sim 依赖的候选工具链**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原帖候选方案是使用基于 MuJoCo Warp 的 mjlab：保留 Isaac Lab-style API，同时提供原生 MuJoCo、较少依赖、viewer/debugger、domain randomization、RGB-D、terrain 与 multi-GPU。帖子没有版本兼容和基准数据，迁移前仍需小任务验证。
- 证据状态：`community_candidate`
- 来源定位：根帖功能列表
- 原帖/精确回复：[用 mjlab 降低 Isaac Sim 依赖的候选工具链](https://x.com/alacritic_super/status/2081753839380861374)
- 平台/作者：X / Praveen Kumar Verma @Alacritic_Super
- 关键术语：仿真到现实（Simulation-to-Real, Sim2Real）；域随机化（Domain Randomization, DR）；图形处理器（Graphics Processing Unit, GPU）；应用程序接口（Application Programming Interface, API）；执行器（Actuator）；质心（Center of Mass, CoM）
- 环境：mjlab；MuJoCo Warp；Isaac Lab-style API；GPU 训练。
- 症状：原帖没有具体安装报错。
- 诊断：比较 API 兼容、依赖数量、viewer/debugger、传感器与 terrain 功能。
- 原因：Isaac Sim 栈较重，但原帖未量化其依赖成本。
- 处理过程：选择 mjlab 作为轻量候选。
- 结果：帖子列出支持人形 locomotion、manipulation、imitation、RL、Sim2Real 和 multi-GPU。
- 限制：无安装日志、版本矩阵、性能基准和项目迁移结果。
- 安全提示：更换仿真器后必须重新核对接触、关节、执行器和传感器模型再上实机。
- 图片分析：截图是功能清单，列出 MuJoCo Warp、Isaac Lab-style API、minimal dependencies 等；没有安装命令、错误日志或速度对比图。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于评估人形 RL 仿真工具链，不能视为现有 Isaac Lab 项目的无损替换。

### 机器人在仿真中趴地运动，应该直接改 WBC 参数吗？

- `problem_id`：`problem.environment_setup_dependencies.2359199d348dacec`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：legged_control / OCS2 编译与启动的分层排障记录**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：不能。该评论没有提供控制模式、关节顺序、初始姿态、重力补偿、接触状态、力矩输出或日志，帖子也没有给出回复。应先记录这些最小复现信息，再区分模型映射、控制器未成功切换、状态估计或接触约束问题；现阶段状态为未解决（unresolved）。
- 证据状态：`community_candidate`
- 来源定位：可见评论 #1
- 原帖/精确回复：[legged_control / OCS2 编译与启动的分层排障记录](https://zhuanlan.zhihu.com/p/628450886)
- 平台/作者：Zhihu / 糯米词
- 关键术语：全身控制（Whole-Body Control, WBC）；二次规划（Quadratic Programming, QP）；模型预测控制（Model Predictive Control, MPC）；状态估计（State Estimation）；应用程序接口（Application Programming Interface, API）；关节力矩（Joint Torque）
- 环境：Ubuntu + ROS Noetic；catkin-tools；OCS2、Pinocchio、hpp-fcl；Unitree A1 Gazebo 仿真。
- 症状：move_base_msgs、rospkg、defusedxml、empy 或 catkin 缺失；控制器调用实时调度接口时无权限；机器人趴地运动。
- 诊断：先只编译并运行 OCS2 的 DDP/SQP 示例，再分开编译 legged_controllers、Gazebo 与真机硬件包；每个终端显式 source ROS 和工作空间环境；保留完整首个错误而非只看末尾连锁报错。；按正文、7 条可见评论与一个图像位交叉整理；社区经验尚未由官方文档、源码或 Issue 独立验证。
- 原因：依赖包或 Python 模块未安装；构建工具链指向错误的 Python 解释器；终端未 source；实时调度能力或资源限制不足。；‘趴地运动’缺少控制模式、关节状态、接触力和日志，现阶段不能可靠定因。
- 处理过程：按具体错误补齐 ros-noetic-navigation、python3-catkin-tools 或 Python 模块，并用 -DPYTHON_EXECUTABLE=/usr/bin/python3 固定解释器。；评论建议用 root 启动以绕过 sched_setscheduler 权限；该做法权限过宽，只作为待验证候选，不直接升级为推荐解法。
- 有效处理：正文对缺少 move_base_msgs、catkin-tools 和 empy/Python 解释器不匹配给出了对应命令；是否适用于当前发行版仍需复核。
- 结果：正文形成从 OCS2 示例、控制器、仿真到真机依赖的分层启动路径；评论中的实时权限和趴地问题未获得充分闭环。
- 限制：文章面向 ROS Noetic 和较旧依赖组合；直接切换系统 Python 或全程使用 root 都可能污染环境或扩大权限。；评论不能单独链接，只能保留根帖链接与可见评论定位。
- 安全提示：涉及实时调度时优先核对 ulimit、组权限和最小 Linux capability，不把‘sudo su 后运行整个控制栈’作为默认做法。；进入真机前先在仿真与吊装条件下限速、限力、设置急停并记录关节/接触日志。
- 图片分析：正文唯一工程图位用于展示可选步态/控制模式，需结合 load_controller.launch 的配置与 rqt 指令阅读；图片没有提供关节、接触力或优化器日志，因此不能解释评论中的‘机器人趴地’症状。
- 采集完整性：`partial_visible`；可见回复 7；展开 1 次；回复深度 2/10；停止原因：all_visible_comments_loaded
- 适用边界：仅作为信息缺口与排障顺序提示，不能当成根因判断。

### legged_control / OCS2 首次编译出现缺包、Python 模块或 catkin 命令错误，如何按层定位？

- `problem_id`：`problem.environment_setup_dependencies.3029694f9d601191`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：legged_control / OCS2 编译与启动的分层排障记录**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先固定 Ubuntu、ROS Noetic、Python 与目标提交版本，显式加载工作空间环境（Workspace Environment Sourcing），只编译并运行 OCS2 的差分动态规划（Differential Dynamic Programming, DDP）或顺序二次规划（Sequential Quadratic Programming, SQP）示例；通过后再依次加入 legged_controllers、Gazebo 和真机硬件包。对 move_base_msgs、catkin-tools、empy 等错误按首个缺失项补依赖，必要时用 -DPYTHON_EXECUTABLE=/usr/bin/python3 固定构建解释器，避免盲目反复全量编译。
- 证据状态：`community_candidate`
- 来源定位：正文‘编译源码/报错解决/使用’段落
- 原帖/精确回复：[legged_control / OCS2 编译与启动的分层排障记录](https://zhuanlan.zhihu.com/p/628450886)
- 平台/作者：Zhihu / 糯米词
- 关键术语：全身控制（Whole-Body Control, WBC）；二次规划（Quadratic Programming, QP）；模型预测控制（Model Predictive Control, MPC）；应用程序接口（Application Programming Interface, API）；安全急停（Emergency Stop, E-Stop）
- 环境：Ubuntu + ROS Noetic；catkin-tools；OCS2、Pinocchio、hpp-fcl；Unitree A1 Gazebo 仿真。
- 症状：move_base_msgs、rospkg、defusedxml、empy 或 catkin 缺失；控制器调用实时调度接口时无权限；机器人趴地运动。
- 诊断：先只编译并运行 OCS2 的 DDP/SQP 示例，再分开编译 legged_controllers、Gazebo 与真机硬件包；每个终端显式 source ROS 和工作空间环境；保留完整首个错误而非只看末尾连锁报错。；按正文、7 条可见评论与一个图像位交叉整理；社区经验尚未由官方文档、源码或 Issue 独立验证。
- 原因：依赖包或 Python 模块未安装；构建工具链指向错误的 Python 解释器；终端未 source；实时调度能力或资源限制不足。；‘趴地运动’缺少控制模式、关节状态、接触力和日志，现阶段不能可靠定因。
- 处理过程：按具体错误补齐 ros-noetic-navigation、python3-catkin-tools 或 Python 模块，并用 -DPYTHON_EXECUTABLE=/usr/bin/python3 固定解释器。；评论建议用 root 启动以绕过 sched_setscheduler 权限；该做法权限过宽，只作为待验证候选，不直接升级为推荐解法。
- 有效处理：正文对缺少 move_base_msgs、catkin-tools 和 empy/Python 解释器不匹配给出了对应命令；是否适用于当前发行版仍需复核。
- 结果：正文形成从 OCS2 示例、控制器、仿真到真机依赖的分层启动路径；评论中的实时权限和趴地问题未获得充分闭环。
- 限制：文章面向 ROS Noetic 和较旧依赖组合；直接切换系统 Python 或全程使用 root 都可能污染环境或扩大权限。；评论不能单独链接，只能保留根帖链接与可见评论定位。
- 安全提示：涉及实时调度时优先核对 ulimit、组权限和最小 Linux capability，不把‘sudo su 后运行整个控制栈’作为默认做法。；进入真机前先在仿真与吊装条件下限速、限力、设置急停并记录关节/接触日志。
- 图片分析：正文唯一工程图位用于展示可选步态/控制模式，需结合 load_controller.launch 的配置与 rqt 指令阅读；图片没有提供关节、接触力或优化器日志，因此不能解释评论中的‘机器人趴地’症状。
- 采集完整性：`partial_visible`；可见回复 7；展开 1 次；回复深度 2/10；停止原因：all_visible_comments_loaded
- 适用边界：适用于 ROS Noetic + catkin-tools 的 legged_control / OCS2 栈；命令和包名需按当前发行版复核。

### 控制器启动时报 sched_setscheduler 无权限，是否应直接用 root 运行？

- `problem_id`：`problem.environment_setup_dependencies.dd17da802368497a`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：legged_control / OCS2 编译与启动的分层排障记录**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：评论给出的候选办法是进入 root 后重新 source ROS 与工作空间环境再启动，但这会让整个控制栈获得过宽权限。更稳妥的排查是先确认实时调度权限（Real-Time Scheduling Permission）、ulimit、用户组与进程所需的最小 capability，并只对必要组件授权；在官方文档或可复现实验确认前，本帖不能把全程 root 运行视为正式解法。
- 证据状态：`community_candidate`
- 来源定位：可见评论 #2–#3（sched_setscheduler 权限讨论）
- 原帖/精确回复：[legged_control / OCS2 编译与启动的分层排障记录](https://zhuanlan.zhihu.com/p/628450886)
- 平台/作者：Zhihu / 糯米词
- 关键术语：全身控制（Whole-Body Control, WBC）；二次规划（Quadratic Programming, QP）；模型预测控制（Model Predictive Control, MPC）；应用程序接口（Application Programming Interface, API）；安全急停（Emergency Stop, E-Stop）
- 环境：Ubuntu + ROS Noetic；catkin-tools；OCS2、Pinocchio、hpp-fcl；Unitree A1 Gazebo 仿真。
- 症状：move_base_msgs、rospkg、defusedxml、empy 或 catkin 缺失；控制器调用实时调度接口时无权限；机器人趴地运动。
- 诊断：先只编译并运行 OCS2 的 DDP/SQP 示例，再分开编译 legged_controllers、Gazebo 与真机硬件包；每个终端显式 source ROS 和工作空间环境；保留完整首个错误而非只看末尾连锁报错。；按正文、7 条可见评论与一个图像位交叉整理；社区经验尚未由官方文档、源码或 Issue 独立验证。
- 原因：依赖包或 Python 模块未安装；构建工具链指向错误的 Python 解释器；终端未 source；实时调度能力或资源限制不足。；‘趴地运动’缺少控制模式、关节状态、接触力和日志，现阶段不能可靠定因。
- 处理过程：按具体错误补齐 ros-noetic-navigation、python3-catkin-tools 或 Python 模块，并用 -DPYTHON_EXECUTABLE=/usr/bin/python3 固定解释器。；评论建议用 root 启动以绕过 sched_setscheduler 权限；该做法权限过宽，只作为待验证候选，不直接升级为推荐解法。
- 有效处理：正文对缺少 move_base_msgs、catkin-tools 和 empy/Python 解释器不匹配给出了对应命令；是否适用于当前发行版仍需复核。
- 结果：正文形成从 OCS2 示例、控制器、仿真到真机依赖的分层启动路径；评论中的实时权限和趴地问题未获得充分闭环。
- 限制：文章面向 ROS Noetic 和较旧依赖组合；直接切换系统 Python 或全程使用 root 都可能污染环境或扩大权限。；评论不能单独链接，只能保留根帖链接与可见评论定位。
- 安全提示：涉及实时调度时优先核对 ulimit、组权限和最小 Linux capability，不把‘sudo su 后运行整个控制栈’作为默认做法。；进入真机前先在仿真与吊装条件下限速、限力、设置急停并记录关节/接触日志。
- 图片分析：正文唯一工程图位用于展示可选步态/控制模式，需结合 load_controller.launch 的配置与 rqt 指令阅读；图片没有提供关节、接触力或优化器日志，因此不能解释评论中的‘机器人趴地’症状。
- 采集完整性：`partial_visible`；可见回复 7；展开 1 次；回复深度 2/10；停止原因：all_visible_comments_loaded
- 适用边界：适用于 Linux 实时调度权限类错误；具体授权方式取决于部署与安全策略。

### Humanoid-Gym 最小复现应锁定哪些依赖版本？

- `problem_id`：`problem.environment_setup_dependencies.1d33e0782b8efa5f`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Humanoid-Gym 固定依赖、训练导出与 Sim2Sim 复现链**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：按该帖和官方仓库的共同配置，使用 Python 3.8、PyTorch 1.13.1、CUDA 11.7、NumPy 1.23 与 Isaac Gym Preview 4；先运行 Isaac Gym 自带示例，再以 editable 模式安装 humanoid-gym。不要混用较新的 NumPy/PyTorch 后再把错误归因于策略。
- 证据状态：`community_candidate`
- 来源定位：正文步骤 1—3；官方 README Installation
- 原帖/精确回复：[Humanoid-Gym 固定依赖、训练导出与 Sim2Sim 复现链](https://zhuanlan.zhihu.com/p/1913666425719075983)
- 平台/作者：Zhihu / 未来科技
- 关键术语：依赖锁定（dependency pinning）；可编辑安装（editable install）；版本矩阵（compatibility matrix）
- 环境：Python 3.8；PyTorch 1.13.1；CUDA 11.7；NumPy 1.23；Isaac Gym Preview 4；Humanoid-Gym main 分支文档。
- 症状：依赖漂移导致安装或运行失败。；未先运行 play.py 时缺少可供 sim2sim 加载的 JIT policy。
- 诊断：逐项核对官方 README 的版本矩阵、训练命令、导出顺序和模型路径。
- 原因：Python/PyTorch/CUDA/NumPy 版本组合不匹配。；训练 checkpoint 未经 play.py 导出或模型路径写错。
- 处理过程：按固定版本创建环境并运行 Isaac Gym 示例。；先 train，再 play 导出策略，最后把导出的 model.pt 传给 sim2sim.py。
- 有效处理：使用官方 README 对应的依赖组合和执行顺序。
- 结果：正文命令与 roboterax/humanoid-gym 官方 README 逐项一致。
- 限制：该技术栈较旧；迁移到其他机器人仍需修改资产、关节映射、默认姿态与 PD 增益。
- 安全提示：sim2sim 通过后也不能直接无保护上真机；先核对动作尺度、关节顺序、限位和急停。
- 图片分析：页面主要以命令块表达安装与导出链；没有依赖图片才能成立的结论。
- 独立核验引用：[source_code · README Installation：Python 3.8、PyTorch 1.13.1/CUDA 11.7、NumPy 1.23、Isaac Gym Preview 4](https://github.com/roboterax/humanoid-gym)
- 采集完整性：`partial_visible`；可见回复 1；展开 0 次；回复深度 1/10；停止原因：no_visible_expand_controls
- 适用边界：适用于该仓库文档对应的旧版 Isaac Gym 技术栈。

### Humanoid-Gym 训练后进入 MuJoCo Sim2Sim，正确的导出顺序是什么？

- `problem_id`：`problem.environment_setup_dependencies.6bfeb6202fad65e3`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Humanoid-Gym 固定依赖、训练导出与 Sim2Sim 复现链**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：先用 train.py 训练，再运行 play.py；play.py 会导出供部署使用的 JIT 模型。最后把 logs/XBot_ppo/exported/policies 下的策略路径交给 sim2sim.py。适配新机器人时还必须核对 MJCF 与 URDF 的 joint mapping，不能只替换文件名。
- 证据状态：`community_candidate`
- 来源定位：正文步骤 4—7；官方 README Usage Guide / Sim-to-sim
- 原帖/精确回复：[Humanoid-Gym 固定依赖、训练导出与 Sim2Sim 复现链](https://zhuanlan.zhihu.com/p/1913666425719075983)
- 平台/作者：Zhihu / 未来科技
- 关键术语：即时编译模型（JIT model）；仿真到仿真（Sim2Sim）；关节映射（joint mapping）
- 环境：Python 3.8；PyTorch 1.13.1；CUDA 11.7；NumPy 1.23；Isaac Gym Preview 4；Humanoid-Gym main 分支文档。
- 症状：依赖漂移导致安装或运行失败。；未先运行 play.py 时缺少可供 sim2sim 加载的 JIT policy。
- 诊断：逐项核对官方 README 的版本矩阵、训练命令、导出顺序和模型路径。
- 原因：Python/PyTorch/CUDA/NumPy 版本组合不匹配。；训练 checkpoint 未经 play.py 导出或模型路径写错。
- 处理过程：按固定版本创建环境并运行 Isaac Gym 示例。；先 train，再 play 导出策略，最后把导出的 model.pt 传给 sim2sim.py。
- 有效处理：使用官方 README 对应的依赖组合和执行顺序。
- 结果：正文命令与 roboterax/humanoid-gym 官方 README 逐项一致。
- 限制：该技术栈较旧；迁移到其他机器人仍需修改资产、关节映射、默认姿态与 PD 增益。
- 安全提示：sim2sim 通过后也不能直接无保护上真机；先核对动作尺度、关节顺序、限位和急停。
- 图片分析：页面主要以命令块表达安装与导出链；没有依赖图片才能成立的结论。
- 独立核验引用：[source_code · README Usage Guide：play.py 导出 JIT，随后 sim2sim.py 加载；新机器人需检查 joint mapping](https://github.com/roboterax/humanoid-gym)
- 采集完整性：`partial_visible`；可见回复 1；展开 0 次；回复深度 1/10；停止原因：no_visible_expand_controls
- 适用边界：适用于 Humanoid-Gym 的 PPO/JIT 导出链；其他导出格式需另查。

### rsl-rl 4.0.x 下 Isaac Lab 的 play.py 卡在 OnPolicyRunner 初始化，并警告 obs_groups 为空，如何验证和临时处理？

- `problem_id`：`problem.environment_setup_dependencies.9a4afa2edccfefe7`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：rsl-rl 4.0 缺少 obs_groups 时 play.py 卡在 OnPolicyRunner 初始化**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原帖的可复现处理是在 agent_cfg.to_dict() 后显式加入观测组（observation groups）映射：actor 和 critic 都读取 policy 组，再把该字典传给 OnPolicyRunner。作者报告初始化由 16 分钟以上的卡死恢复到 1 秒内。应先核对自己的 actor/critic 实际需要哪些观测组，不能机械复制到不同观测空间；该 Issue 仍未关闭，因此这只是有完整复测记录的临时补丁，不是已合并根修复。
- 证据状态：`issue_candidate`
- 来源定位：Issue #5363 正文的 Steps to reproduce、Stuck log、Working patch 与 System Info
- 原帖/精确回复：[rsl-rl 4.0 缺少 obs_groups 时 play.py 卡在 OnPolicyRunner 初始化](https://github.com/isaac-sim/IsaacLab/issues/5363)
- 平台/作者：GitHub Issues / 100milliongold
- 关键术语：观测组（observation groups）；策略观测（policy observations）；执行器网络（actor）；价值网络（critic）；初始化阻塞（initialization hang）
- 环境：Isaac Lab 2.1.1；Isaac Sim 6.0.0-rc.22；Python 3.12；rsl-rl 4.0.x；Isaac-Ant-v0；4 个环境；livestream=2。
- 症状：日志提示 obs_groups 为空且缺少 actor；初始化卡住 16 分钟以上；CPU 约 700%—800%，GPU 约 30% 但没有实际推进。
- 诊断：观察 rsl-rl 对 obs_groups、actor 和 critic 的警告；检查 RslRlBaseRunnerCfg.to_dict() 传给 OnPolicyRunner 的字典是否含观测组映射。
- 原因：原帖把问题定位为 Isaac Lab 配置字典与 rsl-rl 4.0.x 新观测组契约不匹配，缺少 obs_groups 时下游解析没有正确回退。
- 处理过程：在创建 OnPolicyRunner 前复制 agent_cfg 字典，并显式设置 obs_groups={actor:\[policy\], critic:\[policy\]}。
- 有效处理：作为原帖已复测的临时补丁，在传入 OnPolicyRunner 前显式提供 actor/critic 对 policy 观测组的映射。
- 结果：原帖报告补丁后 runner 在 1 秒内完成初始化，并按预期打印 Actor Model 与 Critic Model。
- 限制：Issue 仍为 Open，补丁只在原帖的版本组合和 Isaac-Ant-v0 上复测；不能视为已合并的上游修复，也不能直接假定所有自定义多观测组任务都应使用同一映射。
- 适用边界：原帖明确验证于 Isaac Lab 2.1.1、Isaac Sim 6.0.0-rc.22、Python 3.12、rsl-rl 4.0.x 和 Isaac-Ant-v0；其他版本与自定义观测组需重新核对。

### whole_body_tracking 出现 obs_groups KeyError 时，版本组合经验为何不能直接照搬？

- `problem_id`：`problem.environment_setup_dependencies.obs_groups_version_matrix`
- 问题综合等级：**需要实际验证** — 不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。
- 经验数量：3（全部列出，不隐藏待验证或冲突来源）

**经验 1：obs_groups KeyError 的版本组合经验互相冲突**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突。
- 解答状态：`conflicting`
- 候选解答：一位用户在 Isaac Sim 5.0 下由 Lab 2.2.1 降到 2.2.0 后成功，并在 5070 Ti 上再次确认；但原提问者使用同一大版本组合仍出现 KeyError，另有用户又报告 Lab 2.2.1/Sim 5.0 可运行。因此这只能作为候选组合，必须同时核对 rsl-rl-lib、安装方式、项目提交和实际任务。
- 证据状态：`issue_candidate`
- 来源定位：Issue #42 评论 issuecomment-3456264137、3460662935、3467978265、3556476632
- 原帖/精确回复：[obs_groups KeyError 的版本组合经验互相冲突](https://github.com/HybridRobotics/whole_body_tracking/issues/42#issuecomment-3456264137)
- 平台/作者：GitHub Issues / kelly-0919
- 关键术语：观测组（observation groups）；依赖矩阵（dependency matrix）；版本回退（version downgrade）
- 环境：原帖：Isaac Sim 5.0.0、Isaac Lab 包显示 0.47.1、Python 3.11；评论涉及 Isaac Lab 2.1.0/2.2.0/2.2.1、Isaac Sim 4.5/5.0、rsl-rl-lib 2.2.0/2.3.0、Ubuntu 22.04、RTX 5070/5070 Ti。
- 症状：rsl_rl/runners/on_policy_runner.py 在访问 self.cfg\['obs_groups'\] 时抛出 KeyError；某些组合修复后又出现 infos\['observations'\] 缺少 rnd_state。
- 诊断：同时记录 Isaac Sim、Isaac Lab、rsl-rl-lib、Python、安装方式和项目提交，不要只记录 Isaac Lab 大版本；分别在 Isaac-Ant-v0 与项目任务上复测。
- 处理过程：降级 Isaac Lab；切换 Isaac Sim/Lab 组合；按官方 pip 安装文档重装并设置项目 PYTHONPATH；固定 rsl-rl-lib 2.2.0 或 2.3.0。
- 结果：不同参与者在不同机器上报告了相互不完全兼容的成功/失败组合；唯一共同结论是必须把整个依赖矩阵一起核验。
- 限制：Issue 无维护者回复、无锁文件和最小复现仓库；原帖的 0.47.1 与评论中的 2.x 命名也未解释，因此不能据此发布唯一推荐版本。
- 独立核验引用：[conflict · 原提问者报告相同 Lab 2.2.0/Sim 5.0 大版本组合仍失败](https://github.com/HybridRobotics/whole_body_tracking/issues/42#issuecomment-3460662935)；[conflict · 另一用户报告 Lab 2.2.1/Sim 5.0 可运行](https://github.com/HybridRobotics/whole_body_tracking/issues/42#issuecomment-3556476632)
- 适用边界：仅适用于评论中列出的 Isaac Sim/Lab、GPU 和安装路径；结论存在同线程反例。

**经验 2：obs_groups KeyError 的版本组合经验互相冲突**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突。
- 解答状态：`conflicting`
- 候选解答：原提问者报告该组合在绕过 Torch 版本问题后可以运行；但另一用户在 Ubuntu 22.04/RTX 5070 的同一 Sim/Lab 大版本上遇到 GuardOnDataDependentSymNode，无法运行该项目。因此它不是通用解法，只是一个有反例的环境快照。
- 证据状态：`issue_candidate`
- 来源定位：Issue #42 评论 issuecomment-3460662935 与 3556476632
- 原帖/精确回复：[obs_groups KeyError 的版本组合经验互相冲突](https://github.com/HybridRobotics/whole_body_tracking/issues/42#issuecomment-3460662935)
- 平台/作者：GitHub Issues / kelly-0919
- 关键术语：数据依赖符号节点（data-dependent symbolic node）；版本组合（version combination）；兼容性（compatibility）
- 环境：原帖：Isaac Sim 5.0.0、Isaac Lab 包显示 0.47.1、Python 3.11；评论涉及 Isaac Lab 2.1.0/2.2.0/2.2.1、Isaac Sim 4.5/5.0、rsl-rl-lib 2.2.0/2.3.0、Ubuntu 22.04、RTX 5070/5070 Ti。
- 症状：rsl_rl/runners/on_policy_runner.py 在访问 self.cfg\['obs_groups'\] 时抛出 KeyError；某些组合修复后又出现 infos\['observations'\] 缺少 rnd_state。
- 诊断：同时记录 Isaac Sim、Isaac Lab、rsl-rl-lib、Python、安装方式和项目提交，不要只记录 Isaac Lab 大版本；分别在 Isaac-Ant-v0 与项目任务上复测。
- 处理过程：降级 Isaac Lab；切换 Isaac Sim/Lab 组合；按官方 pip 安装文档重装并设置项目 PYTHONPATH；固定 rsl-rl-lib 2.2.0 或 2.3.0。
- 结果：不同参与者在不同机器上报告了相互不完全兼容的成功/失败组合；唯一共同结论是必须把整个依赖矩阵一起核验。
- 限制：Issue 无维护者回复、无锁文件和最小复现仓库；原帖的 0.47.1 与评论中的 2.x 命名也未解释，因此不能据此发布唯一推荐版本。
- 独立核验引用：[conflict · 同一 Sim 4.5/Lab 2.1.0 大版本组合出现不同兼容性错误](https://github.com/HybridRobotics/whole_body_tracking/issues/42#issuecomment-3556476632)
- 适用边界：仅对应原提问者的未完整公布环境；同线程存在 Ubuntu 22.04/RTX 5070 反例。

**经验 3：obs_groups KeyError 的版本组合经验互相冲突**

- 独立等级：**需要实际验证** — 来源结论存在未解决冲突。
- 解答状态：`partial`
- 候选解答：同线程用户报告：固定 rsl-rl-lib 2.2.0 后 obs_groups 错误消失，但出现 rnd_state 缺失；改为 rsl-rl-lib 2.3.0 后两类错误都消失。该结果只来自一位用户，且与其他评论未锁定 rsl-rl 版本的环境不能直接比较，应把 rsl-rl-lib 版本作为独立变量复测。
- 证据状态：`issue_candidate`
- 来源定位：Issue #42 评论 issuecomment-3779506470
- 原帖/精确回复：[obs_groups KeyError 的版本组合经验互相冲突](https://github.com/HybridRobotics/whole_body_tracking/issues/42#issuecomment-3779506470)
- 平台/作者：GitHub Issues / kelly-0919
- 关键术语：强化学习观测组（rsl-rl obs_groups）；随机网络蒸馏状态（rnd_state）；依赖固定（dependency pinning）
- 环境：原帖：Isaac Sim 5.0.0、Isaac Lab 包显示 0.47.1、Python 3.11；评论涉及 Isaac Lab 2.1.0/2.2.0/2.2.1、Isaac Sim 4.5/5.0、rsl-rl-lib 2.2.0/2.3.0、Ubuntu 22.04、RTX 5070/5070 Ti。
- 症状：rsl_rl/runners/on_policy_runner.py 在访问 self.cfg\['obs_groups'\] 时抛出 KeyError；某些组合修复后又出现 infos\['observations'\] 缺少 rnd_state。
- 诊断：同时记录 Isaac Sim、Isaac Lab、rsl-rl-lib、Python、安装方式和项目提交，不要只记录 Isaac Lab 大版本；分别在 Isaac-Ant-v0 与项目任务上复测。
- 处理过程：降级 Isaac Lab；切换 Isaac Sim/Lab 组合；按官方 pip 安装文档重装并设置项目 PYTHONPATH；固定 rsl-rl-lib 2.2.0 或 2.3.0。
- 结果：不同参与者在不同机器上报告了相互不完全兼容的成功/失败组合；唯一共同结论是必须把整个依赖矩阵一起核验。
- 限制：Issue 无维护者回复、无锁文件和最小复现仓库；原帖的 0.47.1 与评论中的 2.x 命名也未解释，因此不能据此发布唯一推荐版本。
- 独立核验引用：[conflict · 同线程其他成功/失败组合未记录 rsl-rl-lib 精确版本，无法归并为单一根因](https://github.com/HybridRobotics/whole_body_tracking/issues/42)
- 适用边界：评论者使用 Isaac Lab 2.2.0、Isaac Sim 5.0.0、Ubuntu 22.04、RTX 5070；没有维护者或第二个独立复现。

## 仿真器与工具链 (`simulation_toolchain`)

### 为什么同一组 PD 增益在 MuJoCo 和 Isaac Lab 表现差很多？

- `problem_id`：`problem.simulation_toolchain.61377c1e78305f03`
- 问题综合等级：**需要实际验证** — 不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo 显式 actuator PD 与 Isaac Lab 隐式 PD 的数值差异讨论**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突；当前仅形成问题线索。
- 解答状态：`conflicting`
- 候选解答：先核对两端 actuator 语义：是否显式算 torque、是否使用 solver 内隐式 PD、力矩限幅和 delay model 是否一致。评论指出 Isaac Lab 可换 DC/delay motor，因此不能把差异一概归因于平台；应在相同时间步、限幅和关节模型下做 A/B。
- 证据状态：`community_candidate`
- 来源定位：根帖机制对比与关于 DC/delay motor 的评论
- 原帖/精确回复：[MuJoCo 显式 actuator PD 与 Isaac Lab 隐式 PD 的数值差异讨论](https://www.xiaohongshu.com/explore/6a4251c000000000210235c3)
- 平台/作者：Xiaohongshu / ROBOT知识观测站
- 关键术语：仿真到现实（Simulation-to-Real, Sim2Real）；比例-微分控制（Proportional-Derivative Control, PD Control）；执行器（Actuator）；关节力矩（Joint Torque）；端到端时延（End-to-End Latency）；求解器（Solver）
- 环境：MuJoCo 与 Isaac Lab/PhysX 位置/PD 控制。
- 症状：相同目标位置和 kp/kd 在两个仿真器中可能产生不同稳定性与 Sim2Real gap。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：PD 是否在 actuator 层显式生成力矩，还是与动力学约束在 solver 内联合求解。
- 处理过程：正文做机制对比；评论建议切换 Isaac Lab 的显式/延迟电机模型。
- 结果：形成检查假设，没有给同模型定量 A/B 结果。
- 限制：框图和结论高度简化；需对照具体 actuator/solver 配置与官方文档。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：三张可见图比较策略目标→PD→动力学链；结构上突出 MuJoCo actuator 显式力矩与 PhysX solver 内隐式约束，评论指出图过度简化且 Isaac Lab 可换执行器。
- 采集完整性：`partial_visible`；可见回复 8；展开 1 次；回复深度 2/10；停止原因：all_visible_comments_loaded
- 适用边界：框图和结论高度简化；需对照具体 actuator/solver 配置与官方文档。

### Isaac Lab 训练、MuJoCo 对照后，怎样的证据才足以说明 Sim2Real 成功？

- `problem_id`：`problem.simulation_toolchain.6c6a1038cefdb174`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 训练、MuJoCo 对照与实机 Sim2Real 的四足案例**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该帖只提供仿真/实机并排视频和约 10 mm 越障结果，可作为演示但不足以验收。至少还应记录模型版本、控制频率、接触/姿态误差、重复成功率与失败样本；这些补充项不是原帖已给出的解答。
- 证据状态：`community_candidate`
- 来源定位：根帖正文与并排视频
- 原帖/精确回复：[Isaac Lab 训练、MuJoCo 对照与实机 Sim2Real 的四足案例](https://x.com/fu_s_nail/status/2086778083697467678)
- 平台/作者：X / fusnail @fu_s_nail
- 关键术语：全身控制（Whole-Body Control, WBC）；仿真到现实（Simulation-to-Real, Sim2Real）；仿真到仿真（Simulation-to-Simulation, Sim2Sim）；动力学（Dynamics）
- 环境：Isaac Lab 训练；MuJoCo 实时显示；四足真机。
- 症状：原帖未报告失败，只展示约 10 mm 台阶通过。
- 诊断：把仿真和实机画面并列比较，但没有误差曲线或状态日志。
- 处理过程：将 Isaac Lab 策略部署真机并在 MuJoCo 中同步做视觉对照。
- 结果：视频称可越过约 10 mm 台阶。
- 限制：非人形；没有成功率、动力学参数、控制频率或跨仿真器误差。
- 安全提示：实机越障应先限速、限力，并记录足端接触与姿态误差。
- 图片分析：截图显示左侧仿真四足、右侧真实台阶场景的并排视频缩略图；能确认对照形式，但看不到状态曲线、控制参数或重复次数。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于足式机器人跨 Isaac Lab、MuJoCo 和实机的有限验收。

### Isaac Sim 飞轮角速度上限表现异常

- `problem_id`：`problem.simulation_toolchain.isaac_flywheel_angular_limit_2307`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：2（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Sim 的 max_angular_velocity 单位与常见弧度量不一致，且力矩下超限仍未解释**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原帖作者自行确认，max_angular_velocity=100 在这里按度/秒解释，不是他按 Isaac Sim 其他量习惯所假定的弧度/秒。该值对测试过低，飞轮撤去驱动力后会降到这个上限。因此排查顺序应先把目标角速度从 rad/s 与 deg/s 明确换算，再看摩擦、阻尼或电机模型。原帖没有给更正后的具体数值和曲线，所以本卡只保留单位结论。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2307，作者自查 issuecomment-2832847910
- 原帖/精确回复：[Isaac Sim 的 max_angular_velocity 单位与常见弧度量不一致，且力矩下超限仍未解释](https://github.com/isaac-sim/IsaacLab/issues/2307#issuecomment-2832847910)
- 平台/作者：GitHub Issues / VoytekK
- 关键术语：最大角速度（maximum angular velocity）；度每秒（degrees per second）；弧度每秒（radians per second）；直流电机模型（DCMotor model）
- 环境：Isaac Lab commit 09590912792d4421c84f053c5c13c31391bb5c30；Isaac Sim 4.5.0-rc.36；Windows 11 Pro 23H2；RTX 4060 Laptop；CUDA Toolkit 11.8。
- 症状：所有显式摩擦和 damping 为 0、DCMotor 力矩被裁成非负，但飞轮在力矩下降阶段速度下降。；角速度施加力矩时超过 max_angular_velocity，滑行时才降到配置值。
- 诊断：先核对 max_angular_velocity 的单位和数量级，而不是只检查 DCMotor 的 velocity_limit/velocity_limit_sim。；把单位误配导致的回落与施力时超限行为分开记录。
- 原因：作者确认 max_angular_velocity=100 按度制解释，对该飞轮测试过低。；施力期间超限的内部原因在原线程未确定。
- 处理过程：作者把 DCMotor 输出裁为非负并清零摩擦/阻尼；之后自查单位并把剩余超限问题交给维护者。
- 有效处理：对已确认的单位问题，按度/秒解释 max_angular_velocity，并把目标物理上限换算后配置。
- 结果：作者承认错误数值是自身配置问题；维护者未回答施力时超限的剩余问题，Issue 后来关闭。
- 限制：原帖没有给出更正后的具体 max_angular_velocity 数值或复测曲线。；不能把 Issue 关闭等同于施力时超限已修复。
- 安全提示：将仿真限速误当成 rad/s 可能让执行器约束与实机上限相差约 57.3 倍；部署前应统一单位并做独立限速测试。
- 图片分析：原帖曲线由作者在正文逐图说明：力矩约 100 ms 后下降，速度同期下降，约 170 ms 力矩为零后速度稳定；本卡不从未做像素级读取的图片补充数值，单位结论来自作者后续文字自查。
- 独立核验引用：[issue · 作者确认 max_angular_velocity 使用度制且原值过低](https://github.com/isaac-sim/IsaacLab/issues/2307#issuecomment-2832847910)
- 适用边界：对应 Isaac Sim 4.5.0-rc.36 / Isaac Lab 指定 commit 的 RigidBodyPropertiesCfg；其他版本应查本地 schema/documentation。

**经验 2：Isaac Sim 的 max_angular_velocity 单位与常见弧度量不一致，且力矩下超限仍未解释**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索；尚未形成可核对的复现记录。
- 解答状态：`unresolved`
- 候选解答：没有。作者在修正单位认识后仍明确保留这一问题，维护者只回复正在调查 Isaac Lab 的实现，随后没有给原因、补丁或验证结果就关闭了 Issue。因此该行为必须继续标为未解决，不能用“Issue 已关闭”推断成已修复。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2307，剩余问题 issuecomment-2832847910；维护者调查回复 issuecomment-2838861298；关闭回复 issuecomment-2932416524
- 原帖/精确回复：[Isaac Sim 的 max_angular_velocity 单位与常见弧度量不一致，且力矩下超限仍未解释](https://github.com/isaac-sim/IsaacLab/issues/2307#issuecomment-2838861298)
- 平台/作者：GitHub Issues / VoytekK
- 关键术语：速度上限（velocity limit）；施加力矩（applied torque）；滑行（coasting）；待解释行为（behavior pending explanation）
- 环境：Isaac Lab commit 09590912792d4421c84f053c5c13c31391bb5c30；Isaac Sim 4.5.0-rc.36；Windows 11 Pro 23H2；RTX 4060 Laptop；CUDA Toolkit 11.8。
- 症状：所有显式摩擦和 damping 为 0、DCMotor 力矩被裁成非负，但飞轮在力矩下降阶段速度下降。；角速度施加力矩时超过 max_angular_velocity，滑行时才降到配置值。
- 诊断：先核对 max_angular_velocity 的单位和数量级，而不是只检查 DCMotor 的 velocity_limit/velocity_limit_sim。；把单位误配导致的回落与施力时超限行为分开记录。
- 原因：作者确认 max_angular_velocity=100 按度制解释，对该飞轮测试过低。；施力期间超限的内部原因在原线程未确定。
- 处理过程：作者把 DCMotor 输出裁为非负并清零摩擦/阻尼；之后自查单位并把剩余超限问题交给维护者。
- 有效处理：对已确认的单位问题，按度/秒解释 max_angular_velocity，并把目标物理上限换算后配置。
- 结果：作者承认错误数值是自身配置问题；维护者未回答施力时超限的剩余问题，Issue 后来关闭。
- 限制：原帖没有给出更正后的具体 max_angular_velocity 数值或复测曲线。；不能把 Issue 关闭等同于施力时超限已修复。
- 安全提示：将仿真限速误当成 rad/s 可能让执行器约束与实机上限相差约 57.3 倍；部署前应统一单位并做独立限速测试。
- 图片分析：原帖曲线由作者在正文逐图说明：力矩约 100 ms 后下降，速度同期下降，约 170 ms 力矩为零后速度稳定；本卡不从未做像素级读取的图片补充数值，单位结论来自作者后续文字自查。
- 独立核验引用：[issue · 维护者仅表示正在调查施力时超过 max_angular_velocity 的行为](https://github.com/isaac-sim/IsaacLab/issues/2307#issuecomment-2838861298)；[issue · Issue 后来关闭但没有原因、补丁或验证结果](https://github.com/isaac-sim/IsaacLab/issues/2307#issuecomment-2932416524)
- 适用边界：只说明指定 Isaac Sim/Isaac Lab 环境中的未解释行为；其他版本需最小复现。

### IsaacLab Fabric 克隆导致 ContactSensor 环境数错配

- `problem_id`：`problem.simulation_toolchain.isaac_factory_fabric_contact_sensor_3758`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Factory 的 clone_in_fabric 会让 USD Stage 遍历只看见 env_0，导致 ContactSensor 环境数错配**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：作者后续确认 clone_in_fabric=True 会把除 env_0 外的环境创建成 USD Fabric instance proxy；这些代理不出现在 USD Stage Traverse()，所以 find_matching_prims 只返回 env_0，而 PhysX 仍有 512 个实体。线程中可见的规避方式是 clone_in_fabric=False。手工把 _num_envs 写成 512 只证明维度错配，不应作为可扩展修复。另一用户指出关闭 Fabric 会显著拖慢初始化，但没有获得更高性能替代方案。
- 证据状态：`issue_candidate`
- 来源定位：Issue #3758，作者根因更正 issuecomment-3421152534；替代方案未回答 issuecomment-3455895289
- 原帖/精确回复：[Factory 的 clone_in_fabric 会让 USD Stage 遍历只看见 env_0，导致 ContactSensor 环境数错配](https://github.com/isaac-sim/IsaacLab/issues/3758#issuecomment-3421152534)
- 平台/作者：GitHub Issues / Shua-Kang
- 关键术语：实例代理（instance proxy）；场景克隆（USD Fabric cloning）；场景遍历（Stage traversal）；接触传感器（ContactSensor）
- 环境：IsaacLab commit d6a544defb166a4c9b1fbd6261599a4b60b609e3；Isaac Sim 5.0.0；Windows 11；RTX 4090；CUDA 12.8；Driver 572.47；512 env。
- 症状：find_matching_prims 只返回 /World/envs/env_0；ContactSensor 得到 _num_envs=1、PhysX body count=512，初始化因 body 数不匹配失败。
- 诊断：同时检查 USD Stage traversal、clone_in_fabric 配置和 PhysX view.count；不要用 Stage 树中只显示 env_0 推断物理环境只有一个。
- 原因：clone_in_fabric=True 时，其余环境成为 USD Fabric instance proxies，不进入 USD Stage Traverse()，而 PhysX 仍创建全部环境。
- 处理过程：作者将 _num_envs 手工改为 512 后 PPO 可运行，并进一步定位 clone_in_fabric；另一用户确认关掉该选项会让初始化明显变慢。
- 有效处理：线程明确可见的规避方式是设置 clone_in_fabric=False；手工硬编码 _num_envs=512 只用于确认错配，不是通用修复。
- 结果：根因由作者在后续评论中修正并解释；保留 Fabric 性能的替代方案没有得到回答。
- 限制：clone_in_fabric=False 的初始化代价可能很高；线程没有给出既保留 Fabric 又正确发现 sensor prim 的方案。
- 独立核验引用：[issue · 作者纠正根因并解释 Fabric instance proxy、Stage traversal 与 PhysX 数量差异](https://github.com/isaac-sim/IsaacLab/issues/3758#issuecomment-3421152534)；[issue · 另一用户指出 clone_in_fabric=False 的初始化性能代价并询问替代方案，未获回答](https://github.com/isaac-sim/IsaacLab/issues/3758#issuecomment-3455895289)
- 适用边界：对应指定 IsaacLab commit、Isaac Sim 5.0 Factory 任务与 clone_in_fabric=True；其他任务的克隆顺序和 sensor 初始化路径需单独核对。

### IsaacLab 局部清零外力误影响所有并行环境

- `problem_id`：`problem.simulation_toolchain.isaac_partial_external_wrench_clear_4392`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：IsaacLab 按 env_ids 清零 external wrench 会误关全局标志，可用完整缓冲区调用规避**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：不要把一个全零小张量配合单个 env_ids 直接调用该版本的 API，因为全局 has_external_wrench 可能被关掉。作者实测可工作的规避方式是维护 shape=(num_envs, ...) 的完整 force/torque 缓冲区，把目标环境那一行设为零，然后第二次调用不传 env_ids、写回完整张量。作者提出按更新后的内部缓冲区决定全局标志的代码修改，但明确说不确定兼容性，且没有维护者确认，因此只记录为候选修复。
- 证据状态：`issue_candidate`
- 来源定位：Issue #4392，完整缓冲区 workaround 与未验证补丁 issuecomment-3757880219
- 原帖/精确回复：[IsaacLab 按 env_ids 清零 external wrench 会误关全局标志，可用完整缓冲区调用规避](https://github.com/isaac-sim/IsaacLab/issues/4392#issuecomment-3757880219)
- 平台/作者：GitHub Issues / Soappyooo
- 关键术语：外部力旋量（external wrench）；并行环境索引（environment IDs, env_ids）；内部缓冲区（internal buffer）；全局使能标志（global enable flag）
- 环境：Isaac Lab main commit a466d4e；Isaac Sim 5.0；并行环境中的 RigidObject。
- 症状：对 env 0 调用零 force/torque + env_ids 后，所有非 reset 环境的 external wrench 也变为零。
- 诊断：区分内部每环境 force/torque buffer 与全局 has_external_wrench 开关；检查第二次调用输入是否全零以及 env_ids 与 tensor 第一维是否匹配。
- 原因：当前实现按本次输入 forces.any()/torques.any() 设置全局 has_external_wrench，而不是按更新后的完整内部缓冲区判断。
- 处理过程：参与者建议构造完整 num_envs 张量；作者指出传完整张量同时带单个 env_ids 会 shape 不符，并改为不带 env_ids 的完整缓冲区调用。；作者提出改为检查 _external_force_b/_external_torque_b 的可能补丁，但未确认兼容性。
- 有效处理：已由作者明确测试可工作的 workaround：保留完整 num_envs force/torque 缓冲区，将目标环境行置零，然后不传 env_ids 写回完整缓冲区。
- 结果：作者回复完整缓冲区、不传 env_ids 的片段确实可工作；局部 env_ids API 语义本身没有被确认修复。
- 限制：完整缓冲区写回增加数据管理成本；作者给出的源码修改只是 possible fix，不能当成已合并方案。；InteractiveScene.reset 已会重置 buffer 的场景不一定需要额外调用。
- 安全提示：扰动或安全恢复测试应记录每个环境实际 wrench；不要只看调用参数推断外力仍在生效。
- 独立核验引用：[issue · 作者纠正 shape/env_ids 组合，确认完整缓冲区无 env_ids 的片段可工作，并将源码改动标为不确定的 possible fix](https://github.com/isaac-sim/IsaacLab/issues/4392#issuecomment-3757880219)
- 适用边界：对应 Isaac Lab commit a466d4e / Isaac Sim 5.0 的 RigidObject；新版实现需先查看函数语义和最小复现。

## 训练不稳定与崩溃 (`training_instability`)

### 人形 locomotion 一开始完全训不出来，reward 应该怎么减法排查？

- `problem_id`：`problem.training_instability.186e149ec8328d77`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Locomotion 训练效果差时先关 Domain Randomization、缩小 reward 集合**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：评论给出的候选流程是先关闭 Domain Randomization，在理想环境只留最直接任务奖励；确认策略能完成基本目标后，再针对具体失败逐项加入姿态、能量、平滑等约束，最后恢复随机化。原帖没有复训结果，所以仍是 partial。
- 证据状态：`community_candidate`
- 来源定位：评论“先把 domain ran 关了”与“不要一下用很多奖励”
- 原帖/精确回复：[Locomotion 训练效果差时先关 Domain Randomization、缩小 reward 集合](https://www.xiaohongshu.com/explore/688c990a0000000023020d55)
- 平台/作者：Xiaohongshu / popi
- 关键术语：强化学习（Reinforcement Learning, RL）；域随机化（Domain Randomization, DR）；应用程序接口（Application Programming Interface, API）；质心（Center of Mass, CoM）
- 环境：人形 locomotion 强化学习，具体框架/硬件未披露。
- 症状：训练效果一直很差，不知道如何根据行为调整 reward。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：评论怀疑一开始同时启用过多奖励/正则和 domain randomization，掩盖主任务信号。
- 处理过程：先关 DR，删除非必要正则，仅保留任务奖励；根据可见失败行为逐项添加约束。
- 结果：没有作者复训结果。
- 限制：缺少代码、曲线和平台信息；属于方法论建议。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：三个媒体位未给可读取的 reward 曲线或日志；有效工程信息来自高赞评论的减法排查策略。
- 采集完整性：`partial_visible`；可见回复 13；展开 1 次；回复深度 2/10；停止原因：all_visible_comments_loaded
- 适用边界：缺少代码、曲线和平台信息；属于方法论建议。

### 人类视频里存在穿模和错误接触时，SUGAR 如何避免把坏状态直接用于训练？

- `problem_id`：`problem.training_instability.d1beb94863815e31`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：SUGAR：把物理错误的人类视频当粗草稿而非直接参考**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：帖子称不从物理损坏帧 reset，而是从持续扩大的 simulation-validated state pool 取种子；视频只作为粗草稿，推理阶段不再重放。该方法仍依赖动捕和状态输入，需论文/代码验证。
- 证据状态：`community_candidate`
- 来源定位：根帖细节段落
- 原帖/精确回复：[SUGAR：把物理错误的人类视频当粗草稿而非直接参考](https://x.com/clankrmedia/status/2063981858983985429)
- 平台/作者：X / clankr @clankrmedia
- 关键术语：惯性测量单元（Inertial Measurement Unit, IMU）；动作重定向（Motion Retargeting）；动力学（Dynamics）
- 环境：每任务约 100 个视频；仿真验证状态池；G1 状态策略。
- 症状：直接重放会出现穿透、错误接触和不稳定 reset。
- 诊断：识别物理损坏帧，并测试不同视频数量下成功率。
- 原因：视频只提供粗运动，不包含可靠机器人接触和动力学。
- 处理过程：从仿真验证状态池抽取训练种子，推理时丢弃视频参考。
- 有效处理：避免从物理损坏帧 reset 是帖子给出的关键处理。
- 结果：帖子称 20→50→100 视频时成功率逐步上升，并在 G1 上零样本运行。
- 限制：仍依赖 motion capture、state-based policy，且技能粗糙；具体数字需论文核对。
- 安全提示：视频动作上实机前必须过滤穿透、错误接触、关节限位和恢复失败。
- 图片分析：截图是 SUGAR 方法文字说明，未展示 reset 状态池、成功率曲线或失败恢复画面。
- 采集完整性：`partial_visible`；可见回复 2；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于从人类视频构造 G1 操作技能训练数据。

## 奖励、课程与随机化 (`reward_curriculum_randomization`)

### Humanoid-Gym 策略在 Isaac Gym 正常、到 MuJoCo 崎岖地形就摔，先怎么缩小问题？

- `problem_id`：`problem.reward_curriculum_randomization.9c3578529240064f`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Humanoid-Gym Sim2Sim 崎岖地形失败的 curriculum 调整记录**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：这篇经验先把失败归因到训练地形覆盖不足：启用 trimesh 和地形课程（terrain curriculum），增加崎岖地形比例与噪声，再加入 command curriculum 并从原 checkpoint 续训。作者报告崎岖地形由易摔改善为不摔，但仍未达到官方策略，说明这只是候选处置而非充分解法。
- 证据状态：`community_candidate`
- 来源定位：正文 sim2sim 两次失败与调整段落
- 原帖/精确回复：[Humanoid-Gym Sim2Sim 崎岖地形失败的 curriculum 调整记录](https://zhuanlan.zhihu.com/p/1941080281860804637)
- 平台/作者：Zhihu / LeoTime
- 关键术语：仿真到仿真（Simulation-to-Simulation, Sim2Sim）；域随机化（Domain Randomization, DR）；课程学习（Curriculum Learning）；比例-微分控制（Proportional-Derivative Control, PD Control）；质心（Center of Mass, CoM）；大规模并行仿真（Massively Parallel Simulation）
- 环境：Humanoid-Gym；Isaac Gym 训练；MuJoCo sim2sim；num_envs=1024。
- 症状：Isaac Gym 中正常，MuJoCo 平地跌跌撞撞；崎岖地形数步后摔倒。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：初始训练只有平地，地形覆盖与噪声不足，策略鲁棒性弱。
- 处理过程：启用 trimesh/curriculum，增大崎岖地形比例和噪声，增加 command curriculum，基于旧 checkpoint 续训。
- 结果：约 3000 回合后 terrain_level≈10、mean_reward≈140；平地抗外力改善，后续崎岖地形不摔但仍弱于官方策略。
- 限制：单作者经验；没有多种子成功率，评论另有‘MuJoCo 关节不动’未解决。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：三个可见视频时间点分别对应平地 sim2sim、崎岖地形失败和调整后结果；它们能确认行为变化，但没有多种子曲线或逐帧状态日志。
- 采集完整性：`partial_visible`；可见回复 3；展开 0 次；回复深度 1/10；停止原因：no_visible_expand_controls
- 适用边界：单作者经验；没有多种子成功率，评论另有‘MuJoCo 关节不动’未解决。

### 如何把人形真机在线适配限制在更安全、低维的搜索空间？

- `problem_id`：`problem.reward_curriculum_randomization.264b621c4da6baa3`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Robot-Trains-Robot：用物理教师降低真机在线适配风险**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：Robot-Trains-Robot 的候选方案是仿真中用 domain randomization 学 physics latent，上真机后冻结大部分策略，仅优化一个 latent variable；同时由力传感教师臂负责保护、curriculum、perturbation、failure detection 和 reset。
- 证据状态：`community_candidate`
- 来源定位：根帖方法与 walking/swing-up 段落
- 原帖/精确回复：[Robot-Trains-Robot：用物理教师降低真机在线适配风险](https://x.com/rohanpaul_ai/status/1959169753173409880)
- 平台/作者：X / Rohan Paul @rohanpaul_ai
- 关键术语：仿真到现实（Simulation-to-Real, Sim2Real）；域随机化（Domain Randomization, DR）；课程学习（Curriculum Learning）；应用程序接口（Application Programming Interface, API）；质心（Center of Mass, CoM）；动力学（Dynamics）
- 环境：仿真预训练；力传感教师臂；行走与 swing-up。
- 症状：固定教师臂/无调度时学习弱或风险高。
- 诊断：比较 compliant scheduling、fixed-arm baseline 和不同帮助/扰动阶段。
- 原因：真机动力学偏差和难度突变使在线探索不稳定。
- 处理过程：教师臂跟随、逐步降低、同步跑台、塑形奖励与自动 reset。
- 有效处理：只优化一个 physics latent，并由教师臂调度和保护。
- 结果：帖子称 compliant scheduling 优于 fixed arm；未给出具体数值。
- 限制：是论文解读，硬件边界和统计结果需核对原文。
- 安全提示：在线学习需独立力/位姿限位、失效检测和物理支撑。
- 图片分析：截图显示教师臂、力传感、奖励塑形和自动 reset 的文字说明；没有硬件控制图或安全阈值。
- 采集完整性：`partial_visible`；可见回复 3；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于具备外部支撑/教师装置的真机适配。

### MJX 通过预编译模型批次随机化质量与惯量

- `problem_id`：`problem.reward_curriculum_randomization.mjx_precompiled_model_randomization_1607`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MJX 质量与惯量随机化的编译常量边界**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：维护者建议不在训练 reset 里现改这类字段，而是先在原生 MuJoCo 中生成多个随机模型，让每个模型完成正确编译，再逐个 put_model 到 MJX，并用 JAX tree map/concatenate 形成大 batch。线程参与者报告整模型 batching 能运行，但更占内存；body_mass 单字段批处理出现 shape error。因此这是受限的预生成工程路径，不是任意每回合重新编译。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1607，维护者预编译建议 issuecomment-2338654955；用户批处理结果 issuecomment-2564692501
- 原帖/精确回复：[MJX 质量与惯量随机化的编译常量边界](https://github.com/google-deepmind/mujoco/issues/1607#issuecomment-2338654955)
- 平台/作者：GitHub Issues / GitHub Issue 作者
- 关键术语：预编译模型（precompiled model）；批处理（batching）；派生字段（derived field）；树映射/拼接（tree map/concatenate）
- 环境：MuJoCo/MJX 公开 Issue #1607，2024–2026 年回复；JAX 批量 model 与 environment reset。
- 症状：改动 body mass/inertia 后无法在 MJX 内重算依赖这些字段的派生常量。；只对 body_mass 字段做局部 batching 时，线程参与者报告 shape error；完整模型 batching 会增加内存使用。
- 诊断：区分可直接 batching 的字段与需要 compiler/set_const 重算派生常量的字段。；分别验证单字段 batching 与整个 mjx.Model batching 的 shape 和内存成本。
- 原因：MJX 当时没有可在 JAX 内调用的 model compiler/set_const 路径，需重编译的字段不适合在 reset 中动态改。
- 处理过程：维护者建议先在原生 MuJoCo 中构建多个随机模型，完成编译后逐个 put_model，再用 JAX tree map/concatenate 形成批次。；用户测试了 friction 字段批处理、body_mass 局部批处理和整个 model 批处理。
- 有效处理：对 MJX 当时的边界，将所需质量/惯量随机组合预先在原生 MuJoCo 编译，再转换和堆叠为训练 batch。；若需要原生 set_const 能力，最终维护者给出的项目方向是 MuJoCo Warp，而不是等待 MJX 实现。
- 结果：维护者给出可保证 compiler-dependent fields 一致的预编译模型方案。；线程参与者报告完整模型 batching 可行，但存在额外内存成本。；2026 年维护者明确说 MJX 不计划该特性。
- 限制：预编译方案只能从预先生成的随机组合中取样，不是每次 reset 任意改参并在 MJX 内重算。；整个 model 批处理的内存开销由线程用户报告，原线程没有统一 benchmark。；Toddlerbot/Brax 社区 workaround 的 1024 环境耗时只是单一用户 profiling，本批次没有把它升级为通用结论。
- 独立核验引用：[maintainer_confirmation · 维护者建议在原生 MuJoCo 预先编译随机模型，再 put_model 并拼接](https://github.com/google-deepmind/mujoco/issues/1607#issuecomment-2338654955)；[issue · 参与者报告 friction 字段、body_mass 字段和整模型 batching 的不同结果与内存边界](https://github.com/google-deepmind/mujoco/issues/1607#issuecomment-2564692501)
- 适用边界：适用于可在训练前枚举/采样有限质量惯量组合的 MJX 环境；需同时评估 model batch 的内存容量。

### MJX 不计划提供动态 set_const

- `problem_id`：`problem.reward_curriculum_randomization.mjx_set_const_not_planned_1607`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MJX 质量与惯量随机化的编译常量边界**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：按该 Issue 的最终维护者回复，该特性不在 MJX 计划中，他直接指向 MuJoCo Warp 的 set_const。这是项目方向结论，不是对 MuJoCo Warp 所有随机化字段和性能的实测承诺；迁移前仍要核对目标版本的 set_const 文档和支持字段。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1607，维护者最终回复 issuecomment-4707873695
- 原帖/精确回复：[MJX 质量与惯量随机化的编译常量边界](https://github.com/google-deepmind/mujoco/issues/1607#issuecomment-4707873695)
- 平台/作者：GitHub Issues / GitHub Issue 作者
- 关键术语：派生常量（derived constants）；模型常量重算（set_const）；域随机化（domain randomization）；质量与惯量（mass and inertia）
- 环境：MuJoCo/MJX 公开 Issue #1607，2024–2026 年回复；JAX 批量 model 与 environment reset。
- 症状：改动 body mass/inertia 后无法在 MJX 内重算依赖这些字段的派生常量。；只对 body_mass 字段做局部 batching 时，线程参与者报告 shape error；完整模型 batching 会增加内存使用。
- 诊断：区分可直接 batching 的字段与需要 compiler/set_const 重算派生常量的字段。；分别验证单字段 batching 与整个 mjx.Model batching 的 shape 和内存成本。
- 原因：MJX 当时没有可在 JAX 内调用的 model compiler/set_const 路径，需重编译的字段不适合在 reset 中动态改。
- 处理过程：维护者建议先在原生 MuJoCo 中构建多个随机模型，完成编译后逐个 put_model，再用 JAX tree map/concatenate 形成批次。；用户测试了 friction 字段批处理、body_mass 局部批处理和整个 model 批处理。
- 有效处理：对 MJX 当时的边界，将所需质量/惯量随机组合预先在原生 MuJoCo 编译，再转换和堆叠为训练 batch。；若需要原生 set_const 能力，最终维护者给出的项目方向是 MuJoCo Warp，而不是等待 MJX 实现。
- 结果：维护者给出可保证 compiler-dependent fields 一致的预编译模型方案。；线程参与者报告完整模型 batching 可行，但存在额外内存成本。；2026 年维护者明确说 MJX 不计划该特性。
- 限制：预编译方案只能从预先生成的随机组合中取样，不是每次 reset 任意改参并在 MJX 内重算。；整个 model 批处理的内存开销由线程用户报告，原线程没有统一 benchmark。；Toddlerbot/Brax 社区 workaround 的 1024 环境耗时只是单一用户 profiling，本批次没有把它升级为通用结论。
- 独立核验引用：[maintainer_confirmation · 维护者明确说特性不计划用于 MJX，并指向 MuJoCo Warp set_const](https://github.com/google-deepmind/mujoco/issues/1607#issuecomment-4707873695)；[official_documentation · 维护者回复指向的 MuJoCo Warp set_const 官方 API 页面；本卡不外推其支持字段](https://mujoco.readthedocs.io/en/latest/mjwarp/api.html#mujoco_warp.set_const)
- 适用边界：适用于该 Issue 在 2026 年关闭时的 MJX 产品方向；后续版本仍应重新核对官方发布说明。

### MJX 随机化位置与 primitive 尺寸的接口划分

- `problem_id`：`problem.reward_curriculum_randomization.mjx_data_position_model_size_randomization_1684`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MJX 位置、尺寸与异构对象随机化的数据边界**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：维护者的划分是：对象位置属于 mjx.Data/环境 State，在 environment reset function 中采样并传给 pipeline_init；基本几何的尺寸则通过 mjx.Model.geom_size 做 domain randomization。这个划分对 primitive 有维护者说明，但 mesh 形状更难，且原线程没有证明所有 size 变更在当前版本都不需重算模型常量，应对目标版本做数值检查。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1684，primitive/geom_size 回复 issuecomment-2123601780；Data/State 位置划分 issuecomment-2123618064；reset 说明 issuecomment-2123625406
- 原帖/精确回复：[MJX 位置、尺寸与异构对象随机化的数据边界](https://github.com/google-deepmind/mujoco/issues/1684#issuecomment-2123618064)
- 平台/作者：GitHub Issues / GitHub Issue 作者
- 关键术语：环境重置（environment reset）；状态数据（mjx.Data / State）；基本几何（primitive geometry）；几何尺寸（geom_size）
- 环境：MuJoCo/MJX 公开 Issue #1684，2024–2026 年回复；JAX 静态 shape 与批量模型。
- 症状：用户不确定 reset 时的位置随机化应修改 mjx.Model 还是 mjx.Data。；不同 shape/对象数的模型不能直接 stack 到同一 MJX batch。；作为 world body 的静态对象若在 reset 中改位置，线程回复说需重编译。
- 诊断：先判断随机量是每环境的 state（例如可动对象 qpos）、model parameter（例如 geom_size）还是编译期拓扑/静态 world geometry。；对异构模型检查 JAX pytree 形状是否一致，不只检查结构名称。
- 原因：MJX 不支持将形状/对象数不同的 heterogeneous models 直接堆叠成一个 batch。；JAX 运算的静态 shape 使不同数量的对象不能在单一 compiled batch 中自由变长。
- 处理过程：维护者建议在 environment reset 中随机化 mjx.Data/环境 State 中的位置。；对 primitive 尺寸，维护者指向 mjx.Model.geom_size 的 domain randomization。；对不同对象数量，回复提出 host dispatch，或预加载最大数量并将未用对象移出工作区。
- 有效处理：把可动对象的位置随机化放在 environment reset 对 mjx.Data/环境 State 的初始化中，而不是为每个位置重建 model。
- 结果：维护者给出 position/data 与 primitive-size/model 的接口划分。；异构 mesh/对象数的单 batch 没有官方直接支持；掩码方案没有在原线程验证。
- 限制：维护者说 mesh 尺寸/形状随机化比 primitive 更难。；将所有 mesh 都加载并移出未用对象的回复明确标为未尝试/YMMV。；max_contact_points/max_geom_pairs 可节省部分碰撞检测工作，但回复明确说不会省掉其他 JAX engine work。；原线程未确认所有 geom_size 变更在新版本中都无需 set_const/重编译，因此本卡不做这一外推。
- 独立核验引用：[maintainer_confirmation · 维护者说明 primitive shape/size 可按教程随机化 geom_size，mesh 更难](https://github.com/google-deepmind/mujoco/issues/1684#issuecomment-2123601780)；[maintainer_confirmation · 维护者区分 mjx.Data/State 中的位置与 mjx.Model 中的 geom_size](https://github.com/google-deepmind/mujoco/issues/1684#issuecomment-2123618064)；[maintainer_confirmation · 维护者说明 reset 指环境 reset function 并给出 pipeline_init 示例方向](https://github.com/google-deepmind/mujoco/issues/1684#issuecomment-2123625406)
- 适用边界：适用于 MJX 中可动对象位置和 primitive geom_size 的随机化；mesh、world-body 静态几何与版本相关常量需单独核对。

### MJX 异构模型与对象数量掩码方案

- `problem_id`：`problem.reward_curriculum_randomization.mjx_heterogeneous_object_masking_1684`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MJX 位置、尺寸与异构对象随机化的数据边界**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：原线程的维护者/协作者回答是，MJX 不支持直接 stack heterogeneous models。可选方向是 host 侧 dispatch，或事先加载最大对象数，再将未用对象移出工作区并持续固定 qpos。但回复对后一 mesh 技巧明确写了未尝试/YMMV；max_contact_points/max_geom_pairs 也只能节省部分碰撞检测，不会消除其他引擎运算。因此这是待实测的有界 workaround，不是已验证的变长模型支持。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1684，异构模型与最大数量方向 issuecomment-2123601780；未尝试/YMMV issuecomment-2599343381；碰撞开销边界 issuecomment-2599358830
- 原帖/精确回复：[MJX 位置、尺寸与异构对象随机化的数据边界](https://github.com/google-deepmind/mujoco/issues/1684#issuecomment-2599343381)
- 平台/作者：GitHub Issues / GitHub Issue 作者
- 关键术语：异构模型（heterogeneous models）；主机侧调度（host dispatch）；对象掩码（object masking）；静态形状（static shape）
- 环境：MuJoCo/MJX 公开 Issue #1684，2024–2026 年回复；JAX 静态 shape 与批量模型。
- 症状：用户不确定 reset 时的位置随机化应修改 mjx.Model 还是 mjx.Data。；不同 shape/对象数的模型不能直接 stack 到同一 MJX batch。；作为 world body 的静态对象若在 reset 中改位置，线程回复说需重编译。
- 诊断：先判断随机量是每环境的 state（例如可动对象 qpos）、model parameter（例如 geom_size）还是编译期拓扑/静态 world geometry。；对异构模型检查 JAX pytree 形状是否一致，不只检查结构名称。
- 原因：MJX 不支持将形状/对象数不同的 heterogeneous models 直接堆叠成一个 batch。；JAX 运算的静态 shape 使不同数量的对象不能在单一 compiled batch 中自由变长。
- 处理过程：维护者建议在 environment reset 中随机化 mjx.Data/环境 State 中的位置。；对 primitive 尺寸，维护者指向 mjx.Model.geom_size 的 domain randomization。；对不同对象数量，回复提出 host dispatch，或预加载最大数量并将未用对象移出工作区。
- 有效处理：把可动对象的位置随机化放在 environment reset 对 mjx.Data/环境 State 的初始化中，而不是为每个位置重建 model。
- 结果：维护者给出 position/data 与 primitive-size/model 的接口划分。；异构 mesh/对象数的单 batch 没有官方直接支持；掩码方案没有在原线程验证。
- 限制：维护者说 mesh 尺寸/形状随机化比 primitive 更难。；将所有 mesh 都加载并移出未用对象的回复明确标为未尝试/YMMV。；max_contact_points/max_geom_pairs 可节省部分碰撞检测工作，但回复明确说不会省掉其他 JAX engine work。；原线程未确认所有 geom_size 变更在新版本中都无需 set_const/重编译，因此本卡不做这一外推。
- 独立核验引用：[maintainer_confirmation · 维护者说明不同 shape 模型不能 stack，并提出 host dispatch 或最大对象数方向](https://github.com/google-deepmind/mujoco/issues/1684#issuecomment-2123601780)；[issue · 协作者明确说加载所有 mesh 并移出未用对象的技巧未尝试/YMMV](https://github.com/google-deepmind/mujoco/issues/1684#issuecomment-2599343381)；[maintainer_confirmation · 协作者限定 max_contact_points/max_geom_pairs 只节省部分碰撞检测工作](https://github.com/google-deepmind/mujoco/issues/1684#issuecomment-2599358830)
- 适用边界：仅适用于能容忍固定最大模型 shape、额外物体开销和位置掩码风险的 MJX 环境；静态 world object 的位置变更另有重编译边界。

## 性能、显存与并行仿真 (`compute_performance_memory`)

### MuJoCo 完整双足项目只有 3 FPS，但单独 XML 有 102 FPS，如何继续定位？

- `problem_id`：`problem.compute_performance_memory.4e3690ce38c0cc7d`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo 双足项目只有 2–3 FPS 的分层性能排查**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：现有对照说明不应先怪 GPU 或 MuJoCo 本体：应把 viewer/render、控制循环、日志/绘图和 mj_step 分开计时，并用 glxinfo/vulkaninfo 核查是否落到 llvmpipe。评论中的 WSL 用户改用 D3D12 后约 30 FPS，但原帖根因仍未确认，因此状态是 unresolved。
- 证据状态：`community_candidate`
- 来源定位：正文基准对比；评论中 llvmpipe→D3D12 案例
- 原帖/精确回复：[MuJoCo 双足项目只有 2–3 FPS 的分层性能排查](https://zhuanlan.zhihu.com/p/1909630787583742013)
- 平台/作者：Zhihu / aiorbits
- 关键术语：图形处理器（Graphics Processing Unit, GPU）；每秒帧数（Frames Per Second, FPS）
- 环境：Ubuntu 20.04；Python 3.8.20；MuJoCo 2.3.6；RTX 4080 笔记本。
- 症状：完整项目 2–3 FPS，GPU 几乎不用且 CPU 也不高；简单模型上千 FPS，单独目标 XML 约 102 FPS。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：原帖未定因；评论中一个 WSL 案例发现渲染落到 llvmpipe。
- 处理过程：禁用 matplotlib 线程、降低分辨率、换简单模型、对目标 XML 单独跑 5000 step。
- 结果：问题主体仍未解决；评论者在 WSL 配置 D3D12 后约 30 FPS。
- 限制：评论方案只适用于 WSL 软件渲染情形，不能外推到原作者原生 Ubuntu。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：两个媒体位用于展示低 FPS/运行状态；正文给出的 3 FPS、102 FPS 与上千 FPS 对照比截图像素更可检索，未见 profiler 时间线。
- 采集完整性：`partial_visible`；可见回复 5；展开 0 次；回复深度 1/10；停止原因：no_visible_expand_controls
- 适用边界：评论方案只适用于 WSL 软件渲染情形，不能外推到原作者原生 Ubuntu。

### Legged Gym 开更多环境或 Horovod 多 GPU 没变快，应该测什么？

- `problem_id`：`problem.compute_performance_memory.5bf7c5b9e9005cd3`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Legged Gym 的 num_envs 与多 GPU 收益为什么会饱和**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：不要只看 num_envs：记录每秒仿真步、policy update 时间、显存、GPU 利用率、跨 GPU 同步时间，并保持 batch/mini-batch 与更新比可比。社区称 4090 在一万多环境后收益饱和，但 Horovod 如何配置仍未解决。
- 证据状态：`community_candidate`
- 来源定位：根帖与关于 4090/一万环境的评论
- 原帖/精确回复：[Legged Gym 的 num_envs 与多 GPU 收益为什么会饱和](https://www.xiaohongshu.com/explore/6899d862000000002203b228)
- 平台/作者：Xiaohongshu / 小红薯66D6C80D
- 关键术语：图形处理器（Graphics Processing Unit, GPU）；大规模并行仿真（Massively Parallel Simulation）
- 环境：Legged Gym/Isaac Gym；评论者称 RTX 4090；num_envs 4096→10000+。
- 症状：Horovod 打开后似乎没变化；增加 num_envs 后收益饱和。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：可能受显存、采样/优化比、同步通信和任务统计效率共同限制，但原帖未测。
- 处理过程：社区建议先按显存提高 num_envs，并回看 Learning to Walk in Minutes。
- 结果：单个评论称 4090 可开一万多但更高无收益；多 GPU 问题未解决。
- 限制：硬件和 batch/mini-batch 配置缺失，不能把一万环境作为通用值。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：三个媒体位没有显示可读取的 GPU profiler、显存或吞吐曲线；因此一万环境的说法保持为待验证评论经验。
- 采集完整性：`partial_visible`；可见回复 12；展开 1 次；回复深度 2/10；停止原因：all_visible_comments_loaded
- 适用边界：硬件和 batch/mini-batch 配置缺失，不能把一万环境作为通用值。

### IsaacLab 同一步重复读取接触传感器造成运行时开销

- `problem_id`：`problem.compute_performance_memory.isaac_contact_repeated_reads_5018`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Newton 接触传感器的启动延迟与每步读取开销是两个独立性能问题**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原线程中的详细基准把各段拆开：Dexsuite 512 env 的 full 为 16.70 ms、无 contact consumers 为 10.09 ms、缓存后 13.33 ms；solver.update_contacts 仅 0.053 ms，四个 SensorContact.update 合计 0.181 ms，并观察到每步 28 次 sensor.data 访问。8192-env synthetic 对照中重复读取 2.09 ms、缓存 0.43 ms、solver.update_contacts 0.052 ms。对类似代码，应先统计同一步重复访问，再把 contact tensor 缓存一次供 reward/observation 复用；这些数字只适用于该基准。
- 证据状态：`issue_candidate`
- 来源定位：Issue #5018，完整运行时基准 issuecomment-4188564146
- 原帖/精确回复：[Newton 接触传感器的启动延迟与每步读取开销是两个独立性能问题](https://github.com/isaac-sim/IsaacLab/issues/5018#issuecomment-4188564146)
- 平台/作者：GitHub Issues / jkkim-irim
- 关键术语：接触消费者（contact consumer）；张量缓存（tensor caching）；数据物化（data materialization）；每步耗时（milliseconds per step, ms/step）
- 环境：启动问题：Newton 0.2.0→1.0.0 Beta 3.0v，4096 env。；运行时基准：IsaacLab develop；Newton backend；Linux 5.15；NVIDIA L40；Dexsuite 64–512 env 与 synthetic 512–8192 env。
- 症状：Newton 0.2.0 + 4096 env + 特定 contact pairs 时，接近 10 分钟才到第一训练 iteration；启动后运行速度可接受。；多个 reward/observation term 在同一 step 重复读取 contact sensor，接触消费者开销随环境数增加。
- 诊断：先区分 time-to-first-iteration 与稳态 ms/step，不能只用“scaling 慢”描述。；分别计时 solver.update_contacts、SensorContact.update、reward/observation managers，并统计每步 sensor.data 访问次数。
- 原因：启动延迟与 Newton 0.2.0 版本相关，作者报告升级后消失。；运行时基准显示重复 consumer-side sensor.data 更新/物化远大于隔离的 Newton contact generation。
- 处理过程：作者升级 Newton；工程师对 full、no_contact_consumers、cached_contact_consumers 做同任务对照，并在 8192 env synthetic benchmark 重复验证。
- 有效处理：启动延迟：升级 Newton 1.0.0 Beta 3.0v。；运行时：每个 simulation step 缓存一次 contact tensor，并在多个 reward/observation term 复用。
- 结果：作者报告高环境数初始化明显加快，维护者因升级解决而关闭。；512 env 缓存从 16.70 ms 降至 13.33 ms；8192 env 重复读取 2.09 ms，缓存读取 0.43 ms。
- 限制：启动结果来自原作者单一任务，没有给升级前后完整基准表。；运行时测试不是原作者的 startup 问题，不能用缓存解释那 10 分钟；缓存也只回收部分总步时。
- 独立核验引用：[issue · 工程师给出两类任务、分段计时、访问次数和缓存对照的完整基准](https://github.com/isaac-sim/IsaacLab/issues/5018#issuecomment-4188564146)
- 适用边界：适用于 IsaacLab develop + Newton、同一步多个 reward/observation term 重复访问 sensor.data 的任务；不同传感器数和 GPU 需重新 profile。

### Newton 多环境接触传感器启动延迟过高

- `problem_id`：`problem.compute_performance_memory.newton_contact_startup_5018`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Newton 接触传感器的启动延迟与每步读取开销是两个独立性能问题**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：作者澄清问题是 time to first iteration（首轮迭代等待时间），不是稳态 ms/step：Newton 0.2.0 在 4096 env 下接近 10 分钟，训练开始后运行可接受。升级到 Newton 1.0.0 Beta 3.0v 后，他报告启动延迟已解决、初始化明显更快，维护者据此关闭。线程没有给完整前后时间表，因此可优先升级并重测，但不能外推到所有任务。
- 证据状态：`issue_candidate`
- 来源定位：Issue #5018，作者澄清与升级结果 issuecomment-4188629387；维护者关闭确认 issuecomment-4204879364
- 原帖/精确回复：[Newton 接触传感器的启动延迟与每步读取开销是两个独立性能问题](https://github.com/isaac-sim/IsaacLab/issues/5018#issuecomment-4188629387)
- 平台/作者：GitHub Issues / jkkim-irim
- 关键术语：启动延迟（startup latency）；首轮迭代时间（time to first iteration）；并行环境（parallel environments）；版本升级（version upgrade）
- 环境：启动问题：Newton 0.2.0→1.0.0 Beta 3.0v，4096 env。；运行时基准：IsaacLab develop；Newton backend；Linux 5.15；NVIDIA L40；Dexsuite 64–512 env 与 synthetic 512–8192 env。
- 症状：Newton 0.2.0 + 4096 env + 特定 contact pairs 时，接近 10 分钟才到第一训练 iteration；启动后运行速度可接受。；多个 reward/observation term 在同一 step 重复读取 contact sensor，接触消费者开销随环境数增加。
- 诊断：先区分 time-to-first-iteration 与稳态 ms/step，不能只用“scaling 慢”描述。；分别计时 solver.update_contacts、SensorContact.update、reward/observation managers，并统计每步 sensor.data 访问次数。
- 原因：启动延迟与 Newton 0.2.0 版本相关，作者报告升级后消失。；运行时基准显示重复 consumer-side sensor.data 更新/物化远大于隔离的 Newton contact generation。
- 处理过程：作者升级 Newton；工程师对 full、no_contact_consumers、cached_contact_consumers 做同任务对照，并在 8192 env synthetic benchmark 重复验证。
- 有效处理：启动延迟：升级 Newton 1.0.0 Beta 3.0v。；运行时：每个 simulation step 缓存一次 contact tensor，并在多个 reward/observation term 复用。
- 结果：作者报告高环境数初始化明显加快，维护者因升级解决而关闭。；512 env 缓存从 16.70 ms 降至 13.33 ms；8192 env 重复读取 2.09 ms，缓存读取 0.43 ms。
- 限制：启动结果来自原作者单一任务，没有给升级前后完整基准表。；运行时测试不是原作者的 startup 问题，不能用缓存解释那 10 分钟；缓存也只回收部分总步时。
- 独立核验引用：[issue · 作者区分 startup 与 runtime，并报告升级 Newton 后 startup latency 解决](https://github.com/isaac-sim/IsaacLab/issues/5018#issuecomment-4188629387)；[maintainer_confirmation · 维护者因升级已解决而关闭 Issue](https://github.com/isaac-sim/IsaacLab/issues/5018#issuecomment-4204879364)
- 适用边界：适用于 Newton 0.2.0 的 4096-env 接触任务；目标版本兼容性和实际 time-to-first-iteration 应重新测量。

### Isaac Lab 长时训练的 GPU contact 崩溃与内存增长

- `problem_id`：`problem.compute_performance_memory.isaaclab_long_run_gpu_contact_crash_1400`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 长时训练的 GPU contact stage 崩溃与持续复现边界**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突。
- 解答状态：`unresolved`
- 候选解答：没有。协作者确认这是 known issue，并曾说计划在 2.0 修复；但原作者后来明确报告在 Isaac Lab 2.0.1 且开启 CCD 后问题仍存在，memory 仍持续增长。线程没有精确修复 commit、根因或通过长时复测；MultiAssetSpawnerCfg 和 256 links 只是用户推测，不应写成结论。当前只能把版本、触发步数、contact sensor 数、CCD 和内存曲线纳入 soak test。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1400，known issue issuecomment-2470592676；2.0 计划 issuecomment-2590839226；2.0.1+CCD 仍复现 issuecomment-2700179359
- 原帖/精确回复：[Isaac Lab 长时训练的 GPU contact stage 崩溃与持续复现边界](https://github.com/isaac-sim/IsaacLab/issues/1400#issuecomment-2700179359)
- 平台/作者：GitHub Issues / GitHub Issue 作者
- 关键术语：接触压缩阶段（contact compression stage）；连续碰撞检测（continuous collision detection, CCD）；长时稳定性测试（soak test）；内存增长（memory growth）
- 环境：首次报告：Isaac Sim 4.2、当时最新 Isaac Lab、10 个 contact sensors，约 60M 步后触发。；后续复现：Isaac Lab 2.0.1，开启 CCD，用户报告内存仍持续增长。
- 症状：GPU compressContactStage1/2 失败、CUDA context 错误与 scene corrupt。；长时运行过程中 memory 持续增长，最终崩溃。
- 诊断：用版本、contact sensor 数量、触发步数、CCD 状态与内存趋势建立长时 soak-test 记录。；把维护者确认的 known issue 与用户自行怀疑的 MultiAssetSpawnerCfg/256-link 原因分开。
- 原因：维护者只确认为 known issue，未在线程给出精确内存泄漏点或 contact-stage 根因。；MultiAssetSpawnerCfg 的两个 rigid objects 与 256 links 限制是用户推测，不能当作已确认原因。
- 处理过程：项目方曾说计划在 2.0 修复。；原作者升级到 2.0.1 并开启 CCD 后重新运行。
- 结果：项目协作者确认这是 known issue，但原线程未提供已合入修复的精确链接。；原作者在 2.0.1+CCD 下仍报告问题存在且内存持续增长。
- 限制：原线程没有最终根因、修复 PR/commit 或作者通过复测。；不能将开启 CCD、升级到 2.0.1、减少 assets 或将 links 限制在 256 以内写成已验证修复。；首次触发约 60M 步，短时单元测试不足以否定。
- 安全提示：大规模训练应保留定期 checkpoint 与显存/主存趋势，避免长时崩溃丢失全部进度。
- 独立核验引用：[maintainer_confirmation · 项目协作者确认为 known issue](https://github.com/isaac-sim/IsaacLab/issues/1400#issuecomment-2470592676)；[maintainer_confirmation · 协作者说计划在 2.0 修复，但未给精确修复定位](https://github.com/isaac-sim/IsaacLab/issues/1400#issuecomment-2590839226)；[issue · 原作者报告 2.0.1+CCD 下仍复现并观察到内存持续增长](https://github.com/isaac-sim/IsaacLab/issues/1400#issuecomment-2700179359)
- 适用边界：适用于 Isaac Sim 4.2/当时 Isaac Lab 以及原作者后续 2.0.1+CCD 长时训练记录；不证明所有版本或场景必然触发。

## 动作重定向与数据质量 (`retargeting_and_dataset`)

### PBHC 动作模仿从视频/AMASS 到 G1 部署，最容易断在哪些接口？

- `problem_id`：`problem.retargeting_and_dataset.9e7c3abaa6da2e6f`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：PBHC 从 SMPL 数据、重定向、训练到 ONNX 部署的实践链**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：帖子给出的主链是 SMPL 数据字段→Mink/PHC 重定向→接触过滤与可视化→humanoidverse 训练/评测→ONNX→MuJoCo/真机推理。工程上要固定帧率、关节映射和机器人配置；评论指向 PR #22 的 G1 代码，但仅有马步出拳个例，仍需源码和安全限制验证。
- 证据状态：`community_candidate`
- 来源定位：正文“数据处理/retarget/训练/部署”与 PR #22 评论
- 原帖/精确回复：[PBHC 从 SMPL 数据、重定向、训练到 ONNX 部署的实践链](https://zhuanlan.zhihu.com/p/1919018795747505440)
- 平台/作者：Zhihu / 未来科技
- 关键术语：开放神经网络交换格式（Open Neural Network Exchange, ONNX）；每秒帧数（Frames Per Second, FPS）；应用程序接口（Application Programming Interface, API）；动作重定向（Motion Retargeting）
- 环境：Python 3.8；Isaac Gym Preview 4；PBHC/humanoidverse；MuJoCo；G1。
- 症状：官方 README 对数据集处理和真机部署说明不足；评论者称重定向折腾两三天。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：数据格式、工具链和部署代码分散；模型格式与推理框架接口不一致。
- 处理过程：明确 poses/trans/framerate 字段，分别给出 Mink/PHC retarget、过滤、可视化、训练、ONNX 与 MuJoCo 推理命令。
- 结果：评论称 PR #22 的 ONNX 代码可在 G1 部署马步出拳示例。
- 限制：真机结果是单个评论个例；PR、版本和安全参数需独立核验。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：三个媒体位配合正文展示动作数据/重定向/部署流程；可确认工具链存在，但没有逐帧接触误差或真机安全参数。
- 采集完整性：`partial_visible`；可见回复 14；展开 100 次；回复深度 2/10；停止原因：reply_expansion_limit
- 适用边界：真机结果是单个评论个例；PR、版本和安全参数需独立核验。

### 大规模人类动作数据物理不可行时，PHUMA 如何处理？

- `problem_id`：`problem.retargeting_and_dataset.66998894d913c595`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：PHUMA：用物理正则缓解大规模动作数据的可执行性问题**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：它从 MoCap/视频扩展数据，并在 retargeting 中加入 physical regularizing loss，目标是同时保留规模和动态可行性。线程称达到 3× AMASS 规模、未见动作跟踪约提升 20%，但应回到论文核对指标。
- 证据状态：`community_candidate`
- 来源定位：根帖及作者 1/4–4/4 线程
- 原帖/精确回复：[PHUMA：用物理正则缓解大规模动作数据的可执行性问题](https://x.com/lee_kyungmin21/status/1984337004558238173)
- 平台/作者：X / Kyungmin Lee @lee_kyungmin21
- 关键术语：全身控制（Whole-Body Control, WBC）；关节力矩（Joint Torque）；动作重定向（Motion Retargeting）；动作跟踪（Motion Tracking）
- 环境：MoCap+人类视频；物理正则重定向；未见动作模仿与路径跟随评测。
- 症状：大规模数据可能物理不可行，小规模高质量数据泛化不足。
- 诊断：比较 unseen motion tracking 和 path following。
- 原因：纯运动学重定向没有强制动态可行性。
- 处理过程：加入 physical regularizing loss。
- 有效处理：候选方法是在重定向阶段施加物理正则。
- 结果：线程称规模 3× AMASS，未见视频跟踪提升约 20%。
- 限制：数值需论文表格确认；未说明硬件 WBC 结果。
- 安全提示：重定向数据上实机前仍需关节限位、接触和力矩可行性验证。
- 图片分析：截图视频缩略图展示大量人形动作网格，支持“动作集合”语境；不能单独证明 3× 规模或 20% 提升。
- 采集完整性：`partial_visible`；可见回复 4；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于人形运动跟踪数据构建。

### 为什么动作重定向不能只匹配姿态，还要保留 contact？

- `problem_id`：`problem.retargeting_and_dataset.9b279820f94716b4`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：动作相同但接触不同：C2Dex 的接触一致重定向**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：因为人手和机器人手形态不同，同一运动可能形成完全不同的接触。C2Dex 的候选解法是从单目视频恢复稳定的 object-side contacts，并在重定向时显式保留；帖子称这样可覆盖 8 个实机任务，但尚需论文和代码验证。
- 证据状态：`community_candidate`
- 来源定位：根帖正文
- 原帖/精确回复：[动作相同但接触不同：C2Dex 的接触一致重定向](https://x.com/heetezition/status/2086692869734387815)
- 平台/作者：X / Hitesh @heetezition
- 关键术语：接触约束（Contact Constraint）；动作重定向（Motion Retargeting）；全身遥操作（Whole-Body Teleoperation）
- 环境：单目人类视频；灵巧手重定向；8 个实机任务。
- 症状：动作轨迹相似但物体侧接触不稳定或错误。
- 诊断：把物体侧 contact preservation 与纯姿态匹配分开评估。
- 原因：机器人形态与人手不同，姿态相同不代表接触几何相同。
- 处理过程：先恢复稳定物体侧接触，再以接触约束重定向。
- 有效处理：候选方法是在 retargeting 中显式保留 object-side contact。
- 结果：帖子称 24 段视频覆盖 8 个实机任务。
- 限制：没有失败率、接触力误差或跨手型消融；内容是论文摘要。
- 安全提示：接触重定向上实机前应限力并检查穿透、关节限位和物体滑移。
- 图片分析：截图展示问题说明和 C2Dex 标识，未显示接触点、力曲线或重定向失败对比。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于灵巧手和接触操作重定向；不直接等同于双足全身接触。

## 跟踪与遥操 (`tracking_and_teleoperation`)

### 全身遥操作中操作者和机器人朝向不同，怎样避免映射正确却伤到人？

- `problem_id`：`problem.tracking_and_teleoperation.01d30991e3ad555b`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：G1 全身遥操作踢到操作员：朝向映射与端到端延迟风险**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：这条事故说明必须显式定义世界系/机体系朝向语义，并在腿部大幅动作前做速度、工作空间和人机距离守卫；绝对式与增量式映射应按变量分别设计。帖子没有给出复测，且延迟只是目测，所以只能作为 unresolved 安全案例。
- 证据状态：`community_candidate`
- 来源定位：回答正文的朝向映射与延迟分析
- 原帖/精确回复：[G1 全身遥操作踢到操作员：朝向映射与端到端延迟风险](https://www.zhihu.com/question/1988539129605091831/answer/1988581076453584934)
- 平台/作者：Zhihu / huyoust​
- 关键术语：全身遥操作（Whole-Body Teleoperation）；端到端时延（End-to-End Latency）
- 环境：G1 全身遥操作；操作者与机器人面对不同方向。
- 症状：操作者抬腿时机器人向前踢中操作者；动作复刻后续仍可见延迟。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：答主认为主要是朝向/主从映射策略与空间隔离不足，不是简单归因于传感器缺失。
- 处理过程：正文对比绝对式、增量式和混合映射，并强调事故危险性。
- 结果：没有给出修改后的复测结果。
- 限制：0.3–0.5 s 为视频目测；评论大量跑题，不能作为技术证据。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：七个可见媒体位展示操作者抬腿、G1 朝向和命中后的动作序列；图像支持空间朝向风险，但 0.3–0.5 s 延迟仍只是作者目测。
- 采集完整性：`partial_visible`；可见回复 28；展开 2 次；回复深度 2/10；停止原因：no_visible_expand_controls
- 适用边界：0.3–0.5 s 为视频目测；评论大量跑题，不能作为技术证据。

### G1 遥操作长时间站立时脚部关节过热，姿态层面可先查什么？

- `problem_id`：`problem.tracking_and_teleoperation.19f2ddca0644c82d`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：G1 全身遥操作长时站立：手臂姿态与脚部关节热负载**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先记录手臂姿态、整机 COM 与脚踝/足部关节持续扭矩和温度；该评论建议把手臂放到腰后减少静态负载，但没有 A/B 数据。应用前应设温度守卫并通过小幅姿态扫描验证。
- 证据状态：`community_candidate`
- 来源定位：评论“长时间站立不动…脚部关节过热”
- 原帖/精确回复：[G1 全身遥操作长时站立：手臂姿态与脚部关节热负载](https://www.xiaohongshu.com/explore/6a3c1cf9000000000702e2c6)
- 平台/作者：Xiaohongshu / 阿钰
- 关键术语：关节力矩（Joint Torque）；全身遥操作（Whole-Body Teleoperation）；质心（Center of Mass, CoM）；有效载荷（Payload）；热漂移（Thermal Drift）
- 环境：G1 全身遥操作，长时间站立/抱重物等场景。
- 症状：长时间站立时脚部关节过热；手臂/腿部负载可能限制遥操作任务。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：评论认为手臂姿态改变质心，使脚部关节持续力矩增大。
- 处理过程：评论建议静止时将手臂置于腰后平衡重心。
- 结果：没有温度曲线或复测时长。
- 限制：单条评论经验，机器人版本和控制器未知。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：三个媒体位展示全尺寸人形/遥操作场景，但没有 COM、关节扭矩或温度热图；姿态—热负载关系来自评论。
- 采集完整性：`partial_visible`；可见回复 5；展开 0 次；回复深度 1/10；停止原因：all_visible_comments_loaded
- 适用边界：单条评论经验，机器人版本和控制器未知。

### 15k FPS、2 ms 推理能否证明动作在 G1 实机上可用？

- `problem_id`：`problem.tracking_and_teleoperation.738bd42f58f32114`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：仿真 15k FPS/2 ms 不等于 G1 实机可复现**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：不能。该回复指出物理 G1 的瓶颈可能是 contact dynamics 和 actuators，而非生成帧率；还需验证 retargeting、控制周期、关节限位和实机稳定性。当时机器人集成版本尚未发布，所以结论是 unresolved。
- 证据状态：`community_candidate`
- 来源定位：针对 MotionBricks 演示的具体回复
- 原帖/精确回复：[仿真 15k FPS/2 ms 不等于 G1 实机可复现](https://x.com/msall276676/status/2086755806356082799)
- 平台/作者：X / K2sus | AI @MsAll276676
- 关键术语：全身控制（Whole-Body Control, WBC）；每秒帧数（Frames Per Second, FPS）；执行器（Actuator）；关节力矩（Joint Torque）；接触约束（Contact Constraint）；动作重定向（Motion Retargeting）
- 环境：MotionBricks 仿真演示；物理 G1 尚待集成。
- 症状：没有实机结果，reproducibility 仍在进行。
- 诊断：分离 inference latency、contact dynamics、actuator bandwidth 与 retargeting 成功率。
- 原因：真实瓶颈在接触与执行器，而非渲染/生成帧率。
- 处理过程：回复者要求等待机器人集成并做实机重定向验证。
- 结果：截至该回复没有实机复现结果。
- 限制：属于批判性回复，不是实验报告。
- 安全提示：生成动作部署前必须通过关节限位、速度/力矩、接触稳定性和跌倒保护检查。
- 采集完整性：`partial_visible`；可见回复 1；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于从动画/仿真生成器向真实人形控制栈迁移。

## 状态估计、标定与时间同步 (`state_estimation_calibration`)

### 足部 IMU 融合后里程计反而漂移，除了滤波参数还应检查什么？

- `problem_id`：`problem.state_estimation_calibration.51dca6889971758b`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：足部 IMU 时空错位导致里程计漂移的主动标定思路**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先检查足部 IMU 与编码器的时间偏移和旋转外参，再检查标定动作是否提供三轴充分激励。A2I-Calib 的候选思路是最小化足端角速度协方差条件数并主动执行标定轨迹；其效果应回到论文/代码独立验证。
- 证据状态：`community_candidate`
- 来源定位：正文“问题表述/足部 IMU 标定噪声敏感性/系统概述”
- 原帖/精确回复：[足部 IMU 时空错位导致里程计漂移的主动标定思路](https://zhuanlan.zhihu.com/p/30907235807)
- 平台/作者：Zhihu / 第一具身范式
- 关键术语：强化学习（Reinforcement Learning, RL）；状态估计（State Estimation）；惯性测量单元（Inertial Measurement Unit, IMU）；典型相关分析（Canonical Correlation Analysis, CCA）；时间戳同步（Timestamp Synchronization）
- 环境：多 IMU 腿式机器人；足部 IMU + 关节编码器；仿真与真实四足。
- 症状：足部 IMU 约束不一致造成严重里程计漂移。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：IMU/编码器时间偏移、旋转外参错误、常规步态激励不足以及噪声放大。
- 处理过程：优化足端角速度协方差条件数，生成正弦/余弦基函数轨迹，并用 RL 控制器稳定执行主动标定。
- 结果：帖子称仿真和实机标定误差、里程计精度改善，具体数字需回论文核验。
- 限制：不是人形平台；文章属于论文解读，结论需对照原论文和代码。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：八个图位对应 A2I-Calib 系统、足端运动与实验；正文可读结构是条件数优化轨迹→RL 执行→CCA 标定，具体数值图需回原论文逐图核验。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_expand_controls
- 适用边界：不是人形平台；文章属于论文解读，结论需对照原论文和代码。

### 同一 LiDAR-inertial SLAM 在积雪后漂移从 4% 升到 46%，应先如何复现问题？

- `problem_id`：`problem.state_estimation_calibration.f7d9563497760132`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：季节变化使 LiDAR-inertial SLAM 漂移从 4% 升到 46%**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：原帖可操作的部分是用带 GNSS ground truth 的多季节数据按同一路线回放，并同步检查 LiDAR、radar、camera 与 IMU；它没有给出修复。应把季节域偏移作为独立测试维度，而不能只在单季节标定。
- 证据状态：`community_candidate`
- 来源定位：根帖 FoMo 数据说明
- 原帖/精确回复：[季节变化使 LiDAR-inertial SLAM 漂移从 4% 升到 46%](https://x.com/datascienceharp/status/2085807961998541292)
- 平台/作者：X / harpreet @DataScienceHarp
- 关键术语：全身控制（Whole-Body Control, WBC）；状态估计（State Estimation）；惯性测量单元（Inertial Measurement Unit, IMU）；激光雷达（Light Detection and Ranging, LiDAR）；同时定位与建图（Simultaneous Localization and Mapping, SLAM）
- 环境：魁北克森林；12 次部署；-19°C 至 18°C；积雪约 1 m。
- 症状：同一路线漂移从 4% 升至 46%。
- 诊断：使用 GNSS ground truth 对齐多传感器 MCAP 回放并跨季节比较。
- 原因：积雪改变道路几何与 LiDAR 外观，导致长期场景不一致。
- 处理过程：发布多季节传感器数据和 FiftyOne 多模态回放。
- 结果：量化了季节域偏移，但原帖未给出修复算法。
- 限制：非人形；4%/46% 定义与算法配置需查数据卡。
- 安全提示：定位漂移未受控时应降低自主速度，并用独立真值/失效检测限制 WBC 导航指令。
- 图片分析：截图重复展示漂移 4%→46% 和传感器/温度范围，未包含轨迹图或误差定义。
- 采集完整性：`partial_visible`；可见回复 1；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于长期部署的状态估计回归测试。

### Isaac Lab 的 IMU 指向普通 Xform 时提示缺少 RigidBodyAPI，原因和版本化处理方式是什么？

- `problem_id`：`problem.state_estimation_calibration.df5def3ff483287d`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：旧版 Isaac Lab 的 IMU 不能直接挂在普通 Xform，后续已合并自动父刚体发现**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：在原帖的 Isaac Lab v2.1.1/Isaac Sim 4.5.0 环境中，IMU 通过 create_rigid_body_view 读取 PhysX 刚体的位姿、速度和质心缓冲，所以目标 prim 必须具有 RigidBodyAPI；仅有 transform 的 Xform 会初始化失败。后续已合并的 PR #3864 增加了 Xform 挂载和可用父刚体自动发现，并带测试。实际处理应先判断安装版本是否包含该 PR：包含时使用新行为；不包含时必须把目标对准可用刚体或评估回移该修复，不能把新版能力假定为旧版已有。
- 证据状态：`issue_candidate`
- 来源定位：Issue #3088 的环境、报错与作者代码分析；已合并 PR #3864
- 原帖/精确回复：[旧版 Isaac Lab 的 IMU 不能直接挂在普通 Xform，后续已合并自动父刚体发现](https://github.com/isaac-sim/IsaacLab/issues/3088)
- 平台/作者：GitHub Issues / GiulioRomualdi
- 关键术语：惯性测量单元（IMU）；刚体 API（RigidBodyAPI）；变换节点（Xform prim）；父刚体自动发现（automatic parent-body discovery）；物理缓冲（PhysX buffers）
- 环境：Isaac Lab v2.1.1；Isaac Sim 4.5.0；ergoCub；目标 prim=/ergoCub/root_link/torso_1/waist_imu_0；原始实现提交 77a6498。
- 症状：ImuCfg 初始化抛出 RuntimeError: Failed to find a RigidBodyAPI for the prim paths。
- 诊断：检查目标 prim 是否拥有 UsdPhysics.RigidBodyAPI；沿 imu.py 的 create_rigid_body_view、get_transforms、get_velocities 和 get_coms 调用确认数据来自 PhysX 刚体缓冲。
- 原因：旧版 IMU 实现只能从 PhysX 为刚体维护的位姿、速度和质心缓冲读取数据，普通 Xform 没有这些刚体数据。
- 处理过程：提问者自行修改 IMU 以支持 Xform；后续官方 PR #3864 基于相关工作实现自动寻找可用父刚体，并增加测试。
- 有效处理：使用包含已合并 PR #3864 的版本，使 IMU 可指向 Xform 并自动发现可用父刚体；旧版环境不能假定任意 Xform 都可直接创建 rigid body view。
- 结果：PR #3864 于 2025-12-10 合并到 isaac-sim/IsaacLab main，PR 描述明确对应 #3088，并勾选已添加证明修复有效的测试。
- 限制：原 Issue 页面当前仍显示 Open；修复是否存在于某个具体发行版需按目标安装版本核对，不能只看 main 的合并日期。
- 安全提示：更换 IMU 参考 prim 或升级实现后，应核对输出参考系、偏置和安装外参，再用于闭环 WBC。
- 图片分析：原帖包含目标 prim 的界面截图，但根因与修复结论均可由文字报错、源码调用链和已合并 PR 独立支撑；未从截图推断额外信息。
- 独立核验引用：[pull_request · PR 描述明确实现 Xform IMU 挂载与可用父刚体自动发现，对应 #3088；2025-12-10 合并到 main，并包含测试](https://github.com/isaac-sim/IsaacLab/pull/3864)；[source_code · PR #3864 合并提交 df2c5c3](https://github.com/isaac-sim/IsaacLab/commit/df2c5c3)
- 适用边界：旧行为明确对应 Isaac Lab v2.1.1/Isaac Sim 4.5.0；新行为对应包含 2025-12-10 合并 PR #3864 的代码版本。

### IsaacLab 静止 IMU 出现微小非零加速度和角速度时，如何区分浮点误差与重力偏置？

- `problem_id`：`problem.state_estimation_calibration.4cc6a27b4f2a6129`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：静止 IMU 的微小非零读数与 Z 轴重力偏置应分开判断**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原帖 collaborator 的判断是：x/y 线加速度约 1e-6 的偏差以及角速度的微小偏差属于浮点误差；Z 轴偏差来自实现中添加的重力偏置，可通过配置更改。应先按量级和方向分类，再决定是否改 gravity offset。这个回答不代表接触场景中的大幅加速度误差也只是浮点噪声。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1294，collaborator 回复 issuecomment-2567861220
- 原帖/精确回复：[静止 IMU 的微小非零读数与 Z 轴重力偏置应分开判断](https://github.com/isaac-sim/IsaacLab/issues/1294#issuecomment-2567861220)
- 平台/作者：GitHub Issues / jtigue-bdai
- 关键术语：线加速度（linear acceleration）；角速度（angular velocity）；浮点误差（floating-point error）；重力偏置（gravity offset）
- 环境：IsaacLab IMU 线程；提案上下文为 Isaac Sim 4.2；用户把 IMU 挂在地面静止方块上；用户具体提交未说明。
- 症状：静止状态下 x/y 线加速度和角速度出现微小偏差，Z 轴也存在偏移。
- 诊断：先查看数值量级；把约 1e-6 的横向/角速度偏差与 Z 轴重力偏置分开；检查 IMU 配置中的 gravity offset。
- 原因：collaborator 将 x/y 与角速度的微小偏差归为浮点误差，将 Z 偏差归为配置中添加的重力偏置。
- 处理过程：用户采集静止方块 IMU 数据并绘图；维护者按量级和轴向解释。
- 有效处理：若 Z 轴偏差不符合任务定义，按目标观测约定调整 IMU 的重力偏置配置；不要为了消除 1e-6 量级浮点误差盲目增加复杂滤波。
- 结果：collaborator 给出明确分类，但原用户没有继续报告改配置后的结果。
- 限制：该结论只覆盖评论中的静止、小量级偏差；原提案同时指出有限差分加速度在接触/速度噪声下会产生显著噪声且依赖采样率，两者不能混为一类。
- 图片分析：用户评论包含曲线截图，但本卡只采用 collaborator 在文字中明确给出的量级和原因；未从截图补读数。
- 独立核验引用：[maintainer_confirmation · collaborator 明确区分 1e-6 浮点误差与 Z 轴重力偏置](https://github.com/isaac-sim/IsaacLab/issues/1294#issuecomment-2567861220)
- 适用边界：适用于静止刚体的微小偏差检查；接触、IdealPDActuator 或不同版本下的大幅异常需另行诊断。

### ObservationManager 首次读取 IMU 数据时报 update must be called，scene.update 应放在什么位置？

- `problem_id`：`problem.state_estimation_calibration.953c3f7d50283959`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ObservationManager 首次读取 IMU 前必须在 sim.reset 后更新 scene**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：原线程和已合并 PR #1809 的处理都是：先执行 sim.reset()，再执行 scene.update(dt=physics_dt)，之后才加载 managers 或读取 IMU.data。把 scene.update 放在 sim.reset 前会访问尚未建立的 articulation 数据。包含 PR #1809 的版本已在 ManagerBasedEnv 和 DirectRLEnv 初始化中补上这一步；旧版本可按同一顺序回移并复测。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1423 复测 issuecomment-2657349510；已合并 PR #1809；合并提交 157c6b74
- 原帖/精确回复：[ObservationManager 首次读取 IMU 前必须在 sim.reset 后更新 scene](https://github.com/isaac-sim/IsaacLab/issues/1423#issuecomment-2657349510)
- 平台/作者：GitHub Issues / diracdelta7
- 关键术语：观测管理器（ObservationManager）；场景更新（scene update）；惯性测量单元（IMU）；初始化顺序（initialization order）
- 环境：原帖提交 84b2d2d8849e86752aa5a948d5f818d8430eec5a；Isaac Sim 4.2.0-rc.17；Ubuntu 20.04；RTX A6000；CUDA 11.8；ManagerBasedRLEnv/ANYmal-D；后续 DirectRLEnv/ANYmal-C 复测。
- 症状：ObservationManager 在准备 term 维度时访问 asset.data.lin_acc_b，IMU._dt 未设置，抛出 RuntimeError: The update function must be called before the data buffers are accessed the first time。
- 诊断：沿初始化调用链确认 ObservationManager 在传感器第一次 scene.update 前读数据；检查 scene.update 与 sim.reset/load_managers 的相对顺序。
- 原因：环境初始化未在提取 IMU.data 前更新 scene，导致 IMU._dt 和其他场景缓冲未填充。
- 处理过程：社区先手工在初始化加入 scene.update；DirectRLEnv 用户把它放在 sim.reset 前时遇到 Articulation._data 不存在，交换顺序后成功。
- 有效处理：在 sim.reset() 之后、load_managers() 或首次传感器观测读取之前调用 self.scene.update(dt=self.physics_dt)；或使用已包含 PR #1809 的版本。
- 结果：DirectRLEnv 用户确认修正顺序后工作正常；PR #1809 合并到主仓库，Issue 随合并提交 157c6b74 关闭。
- 限制：PR #1809 的测试复选框未勾选；使用旧分支手工回移时仍需对自己的传感器和环境初始化流程做回归测试。
- 独立核验引用：[pull_request · PR 明确修复 #1423，在 ManagerBasedEnv 和 DirectRLEnv 初始化时更新 scene，已合并](https://github.com/isaac-sim/IsaacLab/pull/1809)；[source_code · PR #1809 合并提交](https://github.com/isaac-sim/IsaacLab/commit/157c6b74ed4d9892c5e5ccc0d38d7835f27e98f9)；[independent_reproduction · DirectRLEnv 用户确认先 reset 后 update 时工作正常](https://github.com/isaac-sim/IsaacLab/issues/1423#issuecomment-2657349510)
- 适用边界：原始问题对应 Isaac Sim 4.2/旧 IsaacLab main；修复对应包含 2025-02-14 合并 PR #1809 的版本。

### IsaacLab 中受控静止机器人的 body_acc_w 明显错误时，能否直接改用 ImplicitActuatorCfg 或 IMU 读数？

- `problem_id`：`problem.state_estimation_calibration.4a7dcb4994390d00`
- 问题综合等级：**需要实际验证** — 不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：受控静止机器人 body_acc 异常在执行器模型和版本间存在冲突**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突。
- 解答状态：`conflicting`
- 候选解答：原线程不能支持一个通用答案。维护者在 ANYmal、Spot、Unitree 上复现旧问题，并报告其 ImplicitActuatorCfg 配置不再出现，但原提问者尝试后仍错误；IMU 线加速度来自有限差分，可绕开该数据路径但维护者明确提醒会有噪声；团队在 Isaac Sim 5.0 又无法复现。应把执行器配置、版本和独立加速度基准组成对照实验，确认后再选数据源。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1618 评论 issuecomment-2573089344 至 3076020376
- 原帖/精确回复：[受控静止机器人 body_acc 异常在执行器模型和版本间存在冲突](https://github.com/isaac-sim/IsaacLab/issues/1618)
- 平台/作者：GitHub Issues / Csfalpha
- 关键术语：刚体加速度（rigid-body acceleration）；隐式执行器配置（ImplicitActuatorCfg）；理想比例微分执行器（IdealPDActuator）；有限差分（finite difference）
- 环境：原帖 ANYmal-C、dt=0.005、2 个环境、旧 omni.isaac.lab API；评论复现覆盖 Spot/Unitree；后续核对 Isaac Sim 5.0。具体原始提交未说明。
- 症状：受控静止时基座 Z 加速度超过 5；移除关节位置目标和写入后机器人下落，加速度曲线反而符合预期。
- 诊断：对比施加/不施加关节驱动；对比 IdealPDActuator 派生模型与 ImplicitActuatorCfg；同时记录 body_acc_w 和 IMU 有限差分线加速度；在 Isaac Sim 5.0 复测。
- 原因：collaborator 观察问题与 IdealPDActuator 派生执行器有关，但原作者的反例说明该解释尚未闭环。
- 处理过程：切换到 ImplicitActuatorCfg；用 IMU 有限差分线加速度替代；升级/复测 Isaac Sim 5.0。
- 结果：维护者能够在多种机器人上复现旧环境异常；ImplicitActuatorCfg 对维护者有效但对原作者无效；团队在 Isaac Sim 5.0 未复现。
- 限制：线程没有给出原作者在精确 ImplicitActuatorCfg 配置或 Isaac Sim 5.0 下的最终复测；不能把任一替代方案写成通用修复。
- 安全提示：在 body_acc 未经独立运动学/有限差分核验前，不应用它直接估算外力或触发实机安全动作。
- 图片分析：原帖含异常/正常加速度曲线，但维护者已用文字确认复现和冲突；本卡不从曲线提取额外数值。
- 独立核验引用：[conflict · 原提问者报告切换 ImplicitActuator 后结果仍错误](https://github.com/isaac-sim/IsaacLab/issues/1618#issuecomment-2597325994)；[conflict · 团队在 Isaac Sim 5.0 无法复现旧问题](https://github.com/isaac-sim/IsaacLab/issues/1618#issuecomment-3076020376)
- 适用边界：适用于旧 IsaacLab/Isaac Sim 环境中使用显式 IdealPD 类执行器并读取刚体加速度的场景；版本边界尚未闭环。

### Whole Body Tracking 中 anchor_body 必须等于 USD 根链接或主 IMU 所在链接吗？

- `problem_id`：`problem.state_estimation_calibration.ec77676abbf7a02f`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：G1 部署中 torso 与 pelvis 的 anchor_body 选择**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原帖维护者表示不必：该实现允许把任意刚体设为锚定刚体（anchor body），部署时会对所选参考体进行相应处理，因此 torso 不等于 pelvis 本身不是 bug。帖子没有说明这种处理的具体变换，也没有回答不同 IMU 精度问题，迁移模型时仍需核对代码中的坐标变换。
- 证据状态：`issue_candidate`
- 来源定位：Issue #7，维护者回复 issuecomment-3197873848 及后续未回答追问
- 原帖/精确回复：[G1 部署中 torso 与 pelvis 的 anchor_body 选择](https://github.com/HybridRobotics/whole_body_tracking/issues/7#issuecomment-3197873848)
- 平台/作者：GitHub Issues / Josh00-Lu
- 关键术语：锚定刚体（anchor body）；根链接（root link）；惯性测量单元（IMU）
- 环境：HybridRobotics/whole_body_tracking；Unitree G1；USD root=pelvis；anchor_body=torso。
- 症状：提问者预期 torso/pelvis 参考系不同可能产生偏移；未报告实际失败。
- 诊断：核对 anchor_body、USD 根链接与部署观测参考系。
- 处理过程：维护者说明部署链会处理所选 anchor_body。
- 结果：维护者确认 anchor_body 可选择任意 body，且该设置不是 bug。
- 限制：帖子没有解释选择 torso 的设计原因，也没有回答 torso 与 pelvis IMU 精度差异。
- 独立核验引用：[maintainer_confirmation · 维护者确认任意 body 可作为 anchor_body 且部署时会处理](https://github.com/HybridRobotics/whole_body_tracking/issues/7#issuecomment-3197873848)
- 适用边界：适用于 HybridRobotics/whole_body_tracking 的 anchor_body 机制；不能直接外推到其他状态估计实现。

### Human2Humanoid 没有外部动作捕捉（MoCap）时，实机根位置从哪里获得？

- `problem_id`：`problem.state_estimation_calibration.0a2a23879b4a6fa3`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Human2Humanoid 无外部 MoCap 时的实机根位姿与 VR 对齐**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：项目贡献者明确说明使用 ZED Mini 的视觉—惯性里程计（VIO）估计真实根位置，并指向仓库的 hardware_code/zed_odometry.py。帖子没有说明漂移、延迟以及 root_rot/root_vel 的完整生成方式，这些字段仍需以脚本为准。
- 证据状态：`issue_candidate`
- 来源定位：Issue #8，贡献者回复 issuecomment-2417965415
- 原帖/精确回复：[Human2Humanoid 无外部 MoCap 时的实机根位姿与 VR 对齐](https://github.com/LeCAR-Lab/human2humanoid/issues/8#issuecomment-2417965415)
- 平台/作者：GitHub Issues / Axian12138
- 关键术语：视觉—惯性里程计（visual-inertial odometry, VIO）；根位置（root position）；动作捕捉（motion capture, MoCap）
- 环境：LeCAR-Lab/human2humanoid；ZED Mini VIO；VR 实时遥操作。
- 症状：部署代码需要 root_pos/root_rot/root_vel，但机器人本体观测不能直接给出全局根位置。
- 诊断：检查 hardware_code/zed_odometry.py；检查 VR 与 ZED 坐标系偏移。
- 原因：VR 与 ZED 原点/坐标系之间存在未对齐偏移。
- 处理过程：使用 ZED Mini VIO 估计根位置。；实时遥操作前对齐 VR 与 ZED 的偏移。
- 有效处理：项目作者使用 ZED Mini VIO，并显式进行 VR—ZED 偏移对齐。
- 结果：项目贡献者两次确认上述部署实现。
- 限制：原帖没有给出 VIO 漂移、延迟、root_rot/root_vel 具体计算和标定精度。
- 图片分析：Issue 正文截图用于指出策略所需的 p^real 字段；具体方案来自文字回复与代码链接。
- 独立核验引用：[source_code · 作者回复指向的 ZED odometry 实现文件](https://github.com/LeCAR-Lab/human2humanoid/blob/main/hardware_code/zed_odometry.py)
- 适用边界：适用于 human2humanoid 的 ZED Mini 硬件部署链。

### Human2Humanoid 实时遥操作中，VR 与 ZED VIO 的坐标系需要怎样处理？

- `problem_id`：`problem.state_estimation_calibration.7f4808cb820dcb51`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Human2Humanoid 无外部 MoCap 时的实机根位姿与 VR 对齐**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原线程中，提问者提出 VR 与 ZED 坐标系需先对齐的理解，项目贡献者确认两者之间存在偏移，必须在实时遥操作前完成对齐。帖子没有给出标定算法或变换矩阵，不能从回复中补写具体计算步骤。
- 证据状态：`issue_candidate`
- 来源定位：Issue #8，贡献者回复 issuecomment-2426752129
- 原帖/精确回复：[Human2Humanoid 无外部 MoCap 时的实机根位姿与 VR 对齐](https://github.com/LeCAR-Lab/human2humanoid/issues/8#issuecomment-2426752129)
- 平台/作者：GitHub Issues / Axian12138
- 关键术语：坐标系对齐（frame alignment）；外参偏移（extrinsic offset）；实时遥操作（real-time teleoperation）
- 环境：LeCAR-Lab/human2humanoid；ZED Mini VIO；VR 实时遥操作。
- 症状：部署代码需要 root_pos/root_rot/root_vel，但机器人本体观测不能直接给出全局根位置。
- 诊断：检查 hardware_code/zed_odometry.py；检查 VR 与 ZED 坐标系偏移。
- 原因：VR 与 ZED 原点/坐标系之间存在未对齐偏移。
- 处理过程：使用 ZED Mini VIO 估计根位置。；实时遥操作前对齐 VR 与 ZED 的偏移。
- 有效处理：项目作者使用 ZED Mini VIO，并显式进行 VR—ZED 偏移对齐。
- 结果：项目贡献者两次确认上述部署实现。
- 限制：原帖没有给出 VIO 漂移、延迟、root_rot/root_vel 具体计算和标定精度。
- 图片分析：Issue 正文截图用于指出策略所需的 p^real 字段；具体方案来自文字回复与代码链接。
- 独立核验引用：[maintainer_confirmation · 项目贡献者确认实时遥操作前需对齐 VR 与 ZED 偏移](https://github.com/LeCAR-Lab/human2humanoid/issues/8#issuecomment-2426752129)
- 适用边界：适用于同时使用 VR 目标与 ZED VIO 世界系的 human2humanoid 遥操作。

## 通信、时延与实时性 (`communication_and_realtime`)

### Unitree SDK2 节点都运行了却互相发现不到，先对齐哪几项？

- `problem_id`：`problem.communication_and_realtime.4681f1a0cb209af8`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Cyclone DDS 与 Unitree SDK2 的版本、Domain、Topic、IDL、QoS 对齐清单**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：按帖子先核对 Domain ID、Topic 名、IDL 数据类型和 QoS，再核对 Cyclone DDS 核心 C 库、C++/Python 绑定与 unitree_sdk2 的版本是否一致。该文示例用 0.10.2，但当前项目不能盲目照搬版本，应以当前 SDK 锁定为准。
- 证据状态：`community_candidate`
- 来源定位：正文“DDS 定义/库之间关系/安装”
- 原帖/精确回复：[Cyclone DDS 与 Unitree SDK2 的版本、Domain、Topic、IDL、QoS 对齐清单](https://zhuanlan.zhihu.com/p/1941592838388290457)
- 平台/作者：Zhihu / 花生狗
- 关键术语：机器人操作系统 2（Robot Operating System 2, ROS 2）；数据分发服务（Data Distribution Service, DDS）；服务质量（Quality of Service, QoS）；软件开发工具包（Software Development Kit, SDK）；端到端时延（End-to-End Latency）
- 环境：Linux；Cyclone DDS C/C++/Python；unitree_sdk2(_python)；示例版本 0.10.2。
- 症状：跨语言/ROS2/Unitree SDK 组合时容易出现发现失败、类型或 ABI 兼容问题。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：Domain/Topic/IDL/QoS 任一不一致，或核心 C 库与绑定版本混用。
- 处理过程：逐层列出库关系，固定版本并从 C 核心库、C++/Python 绑定到 SDK 分层安装。
- 结果：正文给出构建目录和工具；没有端到端延迟或丢包测量。
- 限制：版本示例可能过时；必须对照当前 Unitree SDK 和 Cyclone DDS 官方文档。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：可见结构图将 Domain、Topic、IDL、QoS 映射为 DDS 通信契约；它是概念关系图，不是时延/丢包测量。
- 采集完整性：`partial_visible`；可见回复 1；展开 0 次；回复深度 1/10；停止原因：no_visible_expand_controls
- 适用边界：版本示例可能过时；必须对照当前 Unitree SDK 和 Cyclone DDS 官方文档。

### ROS2 控制链丢包，QoS 已调仍无效，下一层查什么？

- `problem_id`：`problem.communication_and_realtime.d8618eaecd2ec8f0`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ROS 2 丢包不只看 QoS：复制、优先级与跨网段发现**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：按正文可先查三层：进程内/进程间复制是否打满 CPU，图像点云是否挤占控制通道，DDS discovery 是否跨 VLAN 可达。应以抓包、topic statistics 和端到端时延验证；帖子没有复测数据，不能把‘90%’当事实。
- 证据状态：`community_candidate`
- 来源定位：根帖三项列表
- 原帖/精确回复：[ROS 2 丢包不只看 QoS：复制、优先级与跨网段发现](https://www.xiaohongshu.com/explore/6a27d9b40000000021021bdb)
- 平台/作者：Xiaohongshu / 机械行枢
- 关键术语：全身控制（Whole-Body Control, WBC）；机器人操作系统 2（Robot Operating System 2, ROS 2）；数据分发服务（Data Distribution Service, DDS）；服务质量（Quality of Service, QoS）；端到端时延（End-to-End Latency）；共享内存（Shared Memory）
- 环境：ROS2 工业组网；图像/点云与控制指令共网；多 VLAN。
- 症状：调 QoS 三天仍丢包、延迟或断连。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：用户态反复拷贝占满 CPU；无话题/网络优先级；跨网段 discovery 未配置。
- 处理过程：建议开启共享内存/零拷贝、隔离或优先控制流量、配置跨网段发现。
- 结果：帖子未给实施后的丢包率/延迟。
- 限制：‘90%’是未经验证的宣传性数字；具体实现取决于 DDS 与网络设备。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：三张信息图概括共享内存/零拷贝、话题优先级、跨 VLAN discovery；未见抓包、丢包率或端到端时延曲线。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：all_visible_comments_loaded
- 适用边界：‘90%’是未经验证的宣传性数字；具体实现取决于 DDS 与网络设备。

## sim-to-sim 与 sim-to-real (`sim_to_sim_and_sim_to_real`)

### 为什么 Unitree G1 的同一 C++ 控制代码有时有效、有时机器人完全不动，而 Python SDK 正常？

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.5def7656cf044bd2`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Unitree G1实机踩坑记录**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：该案例的根因是 C++ 对包含未确定 padding 的控制消息 struct 原始内存计算 CRC32，导致校验值随内存内容变化；Python 版本按零 padding 计算。将 C++ 序列化/CRC 输入改成与 Python 完全一致的零填充字节布局后恢复。评论说明问题位于 SDK2 的 crc32 路径，不一定由 ROS 2 引起。
- 证据状态：`community_candidate`
- 来源定位：正文及评论区“单纯用 SDK2”回复串
- 原帖/精确回复：[Unitree G1实机踩坑记录](https://www.xiaohongshu.com/explore/69f479fe0000000022027ace)
- 平台/作者：Xiaohongshu / decision
- 关键术语：全身控制（Whole-Body Control, WBC）；仿真到现实（Simulation-to-Real, Sim2Real）；惯性测量单元（Inertial Measurement Unit, IMU）；机器人操作系统 2（Robot Operating System 2, ROS 2）；数据分发服务（Data Distribution Service, DDS）；软件开发工具包（Software Development Kit, SDK）
- 环境：Unitree G1 真机；ROS 2 + Unitree C++ SDK2；对照 Unitree Python SDK；MuJoCo sim-to-real 评论案例。
- 症状：C++ 控制消息被间歇性拒绝，机器人完全不动。；评论中的另一故障表现为真机乱动而 MuJoCo 稳定。
- 诊断：对比相同控制轨迹在 C++ 和 Python SDK 中计算出的 CRC。；乱动分支检查 joint index、observation/action 顺序与 scale、IMU、XML 与真机型号。
- 原因：C++ 编译器 struct padding 字节未初始化为零，导致对原始内存计算的 CRC 不确定。；真机乱动可能来自关节/观测映射、缩放或模型文件不匹配。
- 处理过程：先排查 ROS，再用 Python SDK 重放相同轨迹作对照。；将 C++ CRC32 序列化/计算方式改成 Python 的零填充实现。
- 有效处理：确保 CRC 输入中的 padding 确定为零，并让 C++ 与 Python 的字节布局和 CRC 算法一致。
- 结果：作者报告修改 C++ CRC 计算后正常工作；真机乱动的评论分支仍未解决。
- 限制：原帖没有给出补丁链接、SDK 版本、消息类型和最小复现；乱动排查清单只是评论经验。
- 安全提示：CRC 或关节映射异常时禁止继续下发高力矩动作；先悬空/安全架、低增益并验证消息字节与关节顺序。
- 图片分析：可见图片是“Unitree G1 实机踩坑记录”的标题/正文卡片，可确认问题主题和真机上下文，但没有展示 CRC 字节、代码 diff 或控制日志，无法仅靠图片复核修复。
- 采集完整性：`partial_visible`；可见回复 14；展开 2 次；回复深度 3/10；停止原因：all_visible_comments_loaded
- 适用边界：适用于同一 payload 在 C++/Python CRC 不同且症状为消息被拒绝或机器人完全不动的 SDK2 版本。

### MuJoCo 中稳定但 G1 真机乱动时，评论给出了哪些优先检查项？

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.ec5503ce13049436`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Unitree G1实机踩坑记录**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：评论候选清单是 joint index 顺序、observation 顺序、observation scale、action scale、IMU，以及 XML/机器人型号是否一致。该分支用户表示部分项目已检查但仍未定位，因此这只是排查入口，不是已验证修复。
- 证据状态：`community_candidate`
- 来源定位：评论区“mujoco 里挺稳、真机乱动”回复串
- 原帖/精确回复：[Unitree G1实机踩坑记录](https://www.xiaohongshu.com/explore/69f479fe0000000022027ace)
- 平台/作者：Xiaohongshu / decision
- 关键术语：全身控制（Whole-Body Control, WBC）；仿真到现实（Simulation-to-Real, Sim2Real）；惯性测量单元（Inertial Measurement Unit, IMU）；机器人操作系统 2（Robot Operating System 2, ROS 2）；数据分发服务（Data Distribution Service, DDS）；软件开发工具包（Software Development Kit, SDK）
- 环境：Unitree G1 真机；ROS 2 + Unitree C++ SDK2；对照 Unitree Python SDK；MuJoCo sim-to-real 评论案例。
- 症状：C++ 控制消息被间歇性拒绝，机器人完全不动。；评论中的另一故障表现为真机乱动而 MuJoCo 稳定。
- 诊断：对比相同控制轨迹在 C++ 和 Python SDK 中计算出的 CRC。；乱动分支检查 joint index、observation/action 顺序与 scale、IMU、XML 与真机型号。
- 原因：C++ 编译器 struct padding 字节未初始化为零，导致对原始内存计算的 CRC 不确定。；真机乱动可能来自关节/观测映射、缩放或模型文件不匹配。
- 处理过程：先排查 ROS，再用 Python SDK 重放相同轨迹作对照。；将 C++ CRC32 序列化/计算方式改成 Python 的零填充实现。
- 有效处理：确保 CRC 输入中的 padding 确定为零，并让 C++ 与 Python 的字节布局和 CRC 算法一致。
- 结果：作者报告修改 C++ CRC 计算后正常工作；真机乱动的评论分支仍未解决。
- 限制：原帖没有给出补丁链接、SDK 版本、消息类型和最小复现；乱动排查清单只是评论经验。
- 安全提示：CRC 或关节映射异常时禁止继续下发高力矩动作；先悬空/安全架、低增益并验证消息字节与关节顺序。
- 图片分析：可见图片是“Unitree G1 实机踩坑记录”的标题/正文卡片，可确认问题主题和真机上下文，但没有展示 CRC 字节、代码 diff 或控制日志，无法仅靠图片复核修复。
- 采集完整性：`partial_visible`；可见回复 14；展开 2 次；回复深度 3/10；停止原因：all_visible_comments_loaded
- 适用边界：适用于策略输出能运行但动作方向/幅度异常的 sim-to-real 案例；不适用于 CRC 导致完全不动。

### 人形机器人 sim-to-real 和多机差异，是否可以用任务策略与在线适配模块解耦来处理？

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.7adeffd8272a05fb`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：人形机器人，强化学习，从算法和硬件层面理性分析sim&real之间的gap如何解决？**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原帖候选方案是让任务策略在理想模型上完成任务，再由独立适配模块针对电机零位、装配、CoM、惯量等实例差异快速学习修正；评论建议用特定动作进行 online RL，直到指令与执行状态对齐。该思路尚无原帖实验验证，不能视为已证明优于 domain randomization。
- 证据状态：`community_candidate`
- 来源定位：回答全文及评论区“标定模块权重策略要怎么做”回复
- 原帖/精确回复：[人形机器人，强化学习，从算法和硬件层面理性分析sim&real之间的gap如何解决？](https://www.zhihu.com/question/1936180383021536212/answer/1943251717090156921)
- 平台/作者：Zhihu / 未来科技
- 关键术语：全身控制（Whole-Body Control, WBC）；强化学习（Reinforcement Learning, RL）；仿真到现实（Simulation-to-Real, Sim2Real）；域随机化（Domain Randomization, DR）；执行器（Actuator）；关节力矩（Joint Torque）
- 环境：人形机器人强化学习策略从理想仿真模型部署到真实硬件；具体训练器和控制频率未说明。
- 症状：真机动作与指令不对齐；多机差异超出训练时域随机化（domain randomization）的覆盖范围后可能失效。
- 诊断：逐项考虑电机零位、机械加工/装配、CoM、惯量、模型简化与多机标定偏差。
- 原因：理想模型与具体真机实例之间存在不可完全消除的参数和装配差异。
- 处理过程：现有常见做法是增加噪声与泛化范围；作者认为这只能扩大响应覆盖。
- 有效处理：作者建议把理想任务策略与可快速学习或持续修正的实例适配模块解耦。
- 结果：原回答和评论没有提供部署结果、收敛速度或跨机器人对比。
- 限制：属于个人方案设想，缺少算法细节、稳定性边界和消融实验。
- 安全提示：在线学习直接作用于真机前应设置动作、力矩、速度和跌倒保护边界，并先离线或在安全架上验证。
- 采集完整性：`partial_visible`；可见回复 2；展开 1 次；回复深度 2/10；停止原因：no_visible_expand_controls
- 适用边界：适用于具备可观测校准动作和安全在线适配条件的人形机器人；不适用于无安全约束的直接实机探索。

### 现场扫描能否单独保证零微调 sim-to-real？

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.287b162284567179`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：在真实部署场地扫描中训练 RGB 人形机器人策略**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：可见回复并未确认。回复者指出摩擦、质量、杂物和地面柔顺性仍可能破坏迁移；现场持续变化时还需要设计重扫描 cadence（频率）。因此扫描保真度不能替代物理参数验证和运行中变更检测。
- 证据状态：`community_candidate`
- 来源定位：@TabDuoBao 与 @Robo_Reliance 的可见回复
- 原帖/精确回复：[在真实部署场地扫描中训练 RGB 人形机器人策略](https://x.com/tabduobao/status/2086739190709199105)
- 平台/作者：X / Lukas Ziegler @lukas_m_ziegler
- 关键术语：全身控制（Whole-Body Control, WBC）；仿真到现实（Simulation-to-Real, Sim2Real）；域随机化（Domain Randomization, DR）
- 环境：真实办公室 360° 扫描；度量尺度 Gaussian Splat；同源碰撞网格；Isaac Sim/Lab；RGB-only 导航策略。
- 症状：通用假场景只教会结构，无法覆盖真实材质、照明和语义；真机碰撞会造成硬件损伤和长时间复位。
- 诊断：核对视觉重建与碰撞网格是否来自同一场地和尺度；记录摩擦、质量、地面柔顺性与现场变化。
- 原因：视觉外观和物理碰撞几何不一致；域随机化未覆盖杂物、摩擦、质量或地面柔顺性；场地变化使已有扫描过期。
- 处理过程：用一次 360° 扫描生成 Gaussian Splat 与碰撞网格，并在同一场景中训练 RGB 策略。
- 有效处理：原帖候选方案是现场重建加同源碰撞网格，再结合 domain randomization 和大视觉编码器。
- 结果：作者声称无需真机微调即可部署，并把现场适配从数月缩短到数天；原帖没有量化验证。
- 限制：未披露机器人、任务成功率、随机化参数、失败案例或独立复现；回复指出杂物、地面柔顺性和重扫描频率仍是边界。
- 安全提示：真实场地部署前应在低速、限力和防碰撞条件下验证碰撞网格、深度遮挡、玻璃门与地面顺应性。
- 图片分析：可见截图展示根帖前半段文字，确认其比较通用随机无纹理场景与真实办公室重建；截图没有日志、物理参数或成功率曲线，不能验证“零真机微调”结论。
- 采集完整性：`partial_visible`；可见回复 3；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于宣称无需真机微调的现场重建方案。

### RGB-only 人形机器人策略在通用仿真中难以 sim-to-real 时，原帖采用了什么场景构建方法？

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.748e37ecc7834601`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：在真实部署场地扫描中训练 RGB 人形机器人策略**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：候选流程是扫描真实部署场地，用同一重建生成度量尺度 3D Gaussian Splat 与碰撞网格，再在 Isaac Sim/Lab 中训练并加入域随机化（domain randomization）和大视觉编码器。这样试图让视觉和物理几何一致。原帖没有给出独立实验，因此只能作为待验证方案。
- 证据状态：`community_candidate`
- 来源定位：根帖正文
- 原帖/精确回复：[在真实部署场地扫描中训练 RGB 人形机器人策略](https://x.com/lukas_m_ziegler/status/2086724387261055463)
- 平台/作者：X / Lukas Ziegler @lukas_m_ziegler
- 关键术语：全身控制（Whole-Body Control, WBC）；仿真到现实（Simulation-to-Real, Sim2Real）；域随机化（Domain Randomization, DR）
- 环境：真实办公室 360° 扫描；度量尺度 Gaussian Splat；同源碰撞网格；Isaac Sim/Lab；RGB-only 导航策略。
- 症状：通用假场景只教会结构，无法覆盖真实材质、照明和语义；真机碰撞会造成硬件损伤和长时间复位。
- 诊断：核对视觉重建与碰撞网格是否来自同一场地和尺度；记录摩擦、质量、地面柔顺性与现场变化。
- 原因：视觉外观和物理碰撞几何不一致；域随机化未覆盖杂物、摩擦、质量或地面柔顺性；场地变化使已有扫描过期。
- 处理过程：用一次 360° 扫描生成 Gaussian Splat 与碰撞网格，并在同一场景中训练 RGB 策略。
- 有效处理：原帖候选方案是现场重建加同源碰撞网格，再结合 domain randomization 和大视觉编码器。
- 结果：作者声称无需真机微调即可部署，并把现场适配从数月缩短到数天；原帖没有量化验证。
- 限制：未披露机器人、任务成功率、随机化参数、失败案例或独立复现；回复指出杂物、地面柔顺性和重扫描频率仍是边界。
- 安全提示：真实场地部署前应在低速、限力和防碰撞条件下验证碰撞网格、深度遮挡、玻璃门与地面顺应性。
- 图片分析：可见截图展示根帖前半段文字，确认其比较通用随机无纹理场景与真实办公室重建；截图没有日志、物理参数或成功率曲线，不能验证“零真机微调”结论。
- 采集完整性：`partial_visible`；可见回复 3；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于部署地点可预先扫描、以 RGB 感知为主的固定场地任务；动态或大范围开放环境不一定适用。

### 真实数据已经较充足时，simulation prior 对 real-robot MBRL 是否仍有明显收益？

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.00fb3539f608b903`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Real-robot MBRL 使用仿真先验的适用边界**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：作者给出的限制是收益会变得有限；同时，真实机器人 MBRL 往往依赖简化动力学，或受可处理 domain gap 上限约束。该帖没有给出数据量阈值，因此应把它作为实验设计警告：按真实数据规模做有/无仿真先验的对照，而不是默认先验总有帮助。
- 证据状态：`community_candidate`
- 来源定位：根帖 Limitations 段落
- 原帖/精确回复：[Real-robot MBRL 使用仿真先验的适用边界](https://x.com/breadli428/status/2086783235929870363)
- 平台/作者：X / Chenhao Li @breadli428
- 关键术语：全身控制（Whole-Body Control, WBC）；强化学习（Reinforcement Learning, RL）；惯性测量单元（Inertial Measurement Unit, IMU）；模型式强化学习（Model-Based Reinforcement Learning, MBRL）；动力学（Dynamics）
- 环境：真实机器人 MBRL；引用的 loco-manipulation 工作；具体控制频率与硬件配置未在根帖披露。
- 症状：仿真先验的收益随真实数据增加而减小；domain gap 超过方法承受范围后性能提升有限。
- 诊断：比较有/无 simulation prior 在不同真实数据规模下的收益；明确模型只覆盖 kinematics 还是完整 dynamics。
- 原因：仿真与真实系统的 domain gap 超过模型先验可修正范围；为可学习性而简化动力学限制了收益。
- 处理过程：以简化的运动学模型作为真实机器人 MBRL 的模型结构。
- 结果：作者只陈述适用边界，没有在该帖给出新的性能数字。
- 限制：不能从这条短帖推导阈值、数据量或适用于所有人形机器人的结论。
- 安全提示：若 domain gap 未量化，应先在受限动作、低速和安全区域比较仿真先验与真实数据驱动模型。
- 图片分析：可见截图包含根帖限制说明及被引用工作的走廊视频缩略图，缩略图可见 SIM-MODEL / 1000 Samples 字样；没有成功率、误差曲线或消融表，不能用于量化性能。
- 采集完整性：`partial_visible`；可见回复 1；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于评估 real-robot MBRL 是否值得增加仿真先验的项目。

### Whole Body Tracking 策略在 MuJoCo 或实机部署不稳时，可以直接改部署端 kp/kd 吗？

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.22589929ede0d271`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Whole Body Tracking 部署时 PD 增益与训练环境不一致**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该仓库成员在原帖中明确要求：部署端的比例—微分增益（kp/kd）应与训练环境保持一致，仿真和实机都不应在部署阶段任意改动。原帖没有给出修改后的复测结果，因此这条经验用于先排除增益不一致，不能证明该案例只有这一项原因。
- 证据状态：`issue_candidate`
- 来源定位：Issue #16，维护者回复 issuecomment-3214861972
- 原帖/精确回复：[Whole Body Tracking 部署时 PD 增益与训练环境不一致](https://github.com/HybridRobotics/whole_body_tracking/issues/16#issuecomment-3214861972)
- 平台/作者：GitHub Issues / flynndong123
- 关键术语：比例—微分增益（PD gains）；仿真到仿真（Sim2Sim）；仿真到现实（Sim-to-Real）
- 环境：HybridRobotics/whole_body_tracking；walk_subject.csv；自写 MuJoCo 部署代码；具体版本未说明。
- 症状：机器人在 MuJoCo 中不能正常行走。
- 诊断：对照训练环境与部署端的 kp/kd。
- 原因：帖子把部署端 PD 增益不一致列为需要首先排除的问题。
- 处理过程：提问者尝试自写 MuJoCo 部署代码；评论中另有用户建议外部 RoboJuDo 配置，但没有作者验证。
- 结果：维护者给出增益一致性要求；原提问者没有回报修改后的运行结果。
- 限制：原帖没有公布训练/部署增益数值、模型版本或修复后视频；不能据此判断该案例的唯一根因。
- 图片分析：原帖包含异常视频，但本卡结论只来自文字描述和维护者回复，不把视频当作根因证据。
- 独立核验引用：[maintainer_confirmation · 仓库成员明确要求部署 kp/kd 与训练环境一致](https://github.com/HybridRobotics/whole_body_tracking/issues/16#issuecomment-3214861972)
- 适用边界：适用于使用同一训练策略、PD 动作解释和机器人模型的 Sim2Sim/Sim-to-Real 部署。

### Isaac Lab 中策略动作与 qpos 不一致时，原线程建议先检查什么？

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.c3716502d45b9db5`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 动作与 qpos 不一致的 Sim-to-Real 排查入口**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索；尚未形成可核对的复现记录；关键图片尚未完成分析。
- 解答状态：`unresolved`
- 候选解答：Isaac Lab 贡献者建议先从两层排查：一是调准机器人仿真并核对使用的执行器模型；二是在模型基本可信后，用动作/关节等域随机化扩大训练分布，提高对关节位置误差的鲁棒性。该线程没有解决提问者的具体 qpos 偏差，因此这只是排查顺序，不是已验证修复。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1077，贡献者回复 issuecomment-2389655396；后续转 Discussion
- 原帖/精确回复：[Isaac Lab 动作与 qpos 不一致的 Sim-to-Real 排查入口](https://github.com/isaac-sim/IsaacLab/issues/1077#issuecomment-2389655396)
- 平台/作者：GitHub Issues / WangYCheng23
- 关键术语：关节位置（joint position, qpos）；执行器模型（actuator model）；域随机化（domain randomization）
- 环境：自定义 ALOHA URDF 转 USD；自定义开关家具环境；implicit actuator；角度单位为 rad。
- 症状：仿真 qpos 与动作不一致；单步动作变化可超过 1 rad；实机通过插值能跟随。
- 诊断：贡献者建议先确认机器人调参状态和执行器模型，再考虑噪声与域随机化。
- 原因：线程只提出执行器模型和仿真校准方向，没有确认具体根因。
- 处理过程：提问者使用 implicit actuator、动作率与关节速度惩罚；计划实机插值。；贡献者建议检查 Ideal PD/自定义 actuator，并扩展训练域。
- 结果：Issue 被转入 Discussion；没有最终修复或对照结果。
- 限制：没有回答 decimation/dt 的具体设置，也没有解释该 ALOHA qpos 偏差的唯一原因。
- 图片分析：Issue 图展示 action 与 qpos 曲线差异，但当前没有完成像素级数值读取，因此图片相关结论保持未验证。
- 适用边界：适用于自定义资产/执行器模型导致的动作—状态偏差初筛；具体 ALOHA 问题未闭环。

### Go1 用户在同一线程中报告哪些设置减少了足端滑动并完成部署？

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.72b028d6ccaf0735`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Go2 足端拖地导致 Sim-to-Real 失败的摩擦、奖励与执行器经验**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该用户称自己使用较宽摩擦随机化、保证 dynamic friction 不超过 static friction、为四足配置 actuator-net，并把 physics dt 设得约比 policy dt 快 10 倍；奖励表中同时提高 air_time/foot_clearance、加入 action_smoothness 与 foot_slip。其部署用 ONNX Runtime 和 Docker 自写脚本。线程只有作者自述，没有独立复现，具体权重不得直接移植到 Go2 或人形机器人。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1784，Go1 工程记录 issuecomment-2720040586 与部署补充 issuecomment-2757597034
- 原帖/精确回复：[Go2 足端拖地导致 Sim-to-Real 失败的摩擦、奖励与执行器经验](https://github.com/isaac-sim/IsaacLab/issues/1784#issuecomment-2720040586)
- 平台/作者：GitHub Issues / Ashutosh781
- 关键术语：执行器网络（actuator network）；动作平滑（action smoothness）；策略周期（policy timestep）
- 环境：Isaac Lab locomotion；Unitree Go2 提问环境；社区 Go1/ANYmal-D 经验；具体 Isaac Lab commit 未说明。
- 症状：仿真足端不抬高、拖地。；实机策略不能移动或容易摔倒。；摩擦随机化后出现 pronking-like gait。
- 诊断：检查 friction combine mode。；检查足端 contact sensor 与 air-time reward。；对照摩擦随机化范围、奖励项、执行器模型和 policy/physics dt。
- 原因：仿真接触摩擦组合方式与资产/奖励使拖脚成为可利用行为。；执行器模型与实机动力学不匹配。
- 处理过程：提问者随机化足端静摩擦 0.8—2.0、动摩擦 0.6—1.6。；贡献者说明 Isaac Gym 的 average 与 Isaac Lab locomotion 示例的 multiply 组合差异。；Go1 用户报告使用更宽摩擦范围、actuator-net、约 10 倍 physics/policy 频率比和特定足端奖励。
- 结果：提问者称摩擦随机化帮助很大并取得初步 Go2 Sim-to-Real，但仍容易摔倒。；Go1 用户称其配置获得良好迁移和较少足端滑动，但没有独立复现。
- 限制：线程混合 Go2、Go1 和 ANYmal-D；数值不可跨机器人直接照搬。；社区用户明确说部分建议基于个人测试或尚未测试；帖子没有统一闭环。
- 适用边界：Unitree Go1 的个人工程记录；仅作为 Go2/足式系统的实验起点。

### 从 Isaac Gym 迁移摩擦参数到 Isaac Lab 时，为什么要先核对 friction combine mode？

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.cbbd75c684ec40dc`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Go2 足端拖地导致 Sim-to-Real 失败的摩擦、奖励与执行器经验**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：Isaac Lab 贡献者在原线程指出，旧 Isaac Gym 采用 average，而 Isaac Lab 的 locomotion 示例改用 multiply。其举例：脚摩擦为 1、地面为 0 时，average 得到 0.5，而 multiply 得到 0。因此直接搬运摩擦参数会改变等效接触摩擦。该回复解释了参数语义差异，但没有单独证明它就是 Go2 失败的唯一原因。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1784，贡献者回复 issuecomment-2660884892 的 Friction Combination
- 原帖/精确回复：[Go2 足端拖地导致 Sim-to-Real 失败的摩擦、奖励与执行器经验](https://github.com/isaac-sim/IsaacLab/issues/1784#issuecomment-2660884892)
- 平台/作者：GitHub Issues / Ashutosh781
- 关键术语：摩擦组合模式（friction combine mode）；平均组合（average）；乘积组合（multiply）
- 环境：Isaac Lab locomotion；Unitree Go2 提问环境；社区 Go1/ANYmal-D 经验；具体 Isaac Lab commit 未说明。
- 症状：仿真足端不抬高、拖地。；实机策略不能移动或容易摔倒。；摩擦随机化后出现 pronking-like gait。
- 诊断：检查 friction combine mode。；检查足端 contact sensor 与 air-time reward。；对照摩擦随机化范围、奖励项、执行器模型和 policy/physics dt。
- 原因：仿真接触摩擦组合方式与资产/奖励使拖脚成为可利用行为。；执行器模型与实机动力学不匹配。
- 处理过程：提问者随机化足端静摩擦 0.8—2.0、动摩擦 0.6—1.6。；贡献者说明 Isaac Gym 的 average 与 Isaac Lab locomotion 示例的 multiply 组合差异。；Go1 用户报告使用更宽摩擦范围、actuator-net、约 10 倍 physics/policy 频率比和特定足端奖励。
- 结果：提问者称摩擦随机化帮助很大并取得初步 Go2 Sim-to-Real，但仍容易摔倒。；Go1 用户称其配置获得良好迁移和较少足端滑动，但没有独立复现。
- 限制：线程混合 Go2、Go1 和 ANYmal-D；数值不可跨机器人直接照搬。；社区用户明确说部分建议基于个人测试或尚未测试；帖子没有统一闭环。
- 独立核验引用：[maintainer_confirmation · Isaac Lab 贡献者解释 Gym 与 Lab 的摩擦组合差异](https://github.com/isaac-sim/IsaacLab/issues/1784#issuecomment-2660884892)
- 适用边界：适用于从 Isaac Gym/legged-gym 向 Isaac Lab locomotion 环境迁移摩擦配置。

### Go2 拖脚策略中，足端摩擦随机化在原帖取得了什么结果？

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.f61ed3d0eb448d35`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Go2 足端拖地导致 Sim-to-Real 失败的摩擦、奖励与执行器经验**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：提问者报告把足端静摩擦范围设为 0.8—2.0、动摩擦设为 0.6—1.6 后，机器人更愿意抬脚，并获得一些初步 Sim-to-Real 迁移；但步态仍不完善且容易摔倒。后续又报告无 feet-air-time reward 时形成类似 pronking 的步态。因此这些数值是一次 Go2 试验记录，不是通用推荐。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1784，提问者回复 issuecomment-2643828231 与 issuecomment-2686774035
- 原帖/精确回复：[Go2 足端拖地导致 Sim-to-Real 失败的摩擦、奖励与执行器经验](https://github.com/isaac-sim/IsaacLab/issues/1784#issuecomment-2643828231)
- 平台/作者：GitHub Issues / Ashutosh781
- 关键术语：摩擦随机化（friction randomization）；足端离地时间奖励（feet-air-time reward）；跃步步态（pronking gait）
- 环境：Isaac Lab locomotion；Unitree Go2 提问环境；社区 Go1/ANYmal-D 经验；具体 Isaac Lab commit 未说明。
- 症状：仿真足端不抬高、拖地。；实机策略不能移动或容易摔倒。；摩擦随机化后出现 pronking-like gait。
- 诊断：检查 friction combine mode。；检查足端 contact sensor 与 air-time reward。；对照摩擦随机化范围、奖励项、执行器模型和 policy/physics dt。
- 原因：仿真接触摩擦组合方式与资产/奖励使拖脚成为可利用行为。；执行器模型与实机动力学不匹配。
- 处理过程：提问者随机化足端静摩擦 0.8—2.0、动摩擦 0.6—1.6。；贡献者说明 Isaac Gym 的 average 与 Isaac Lab locomotion 示例的 multiply 组合差异。；Go1 用户报告使用更宽摩擦范围、actuator-net、约 10 倍 physics/policy 频率比和特定足端奖励。
- 结果：提问者称摩擦随机化帮助很大并取得初步 Go2 Sim-to-Real，但仍容易摔倒。；Go1 用户称其配置获得良好迁移和较少足端滑动，但没有独立复现。
- 限制：线程混合 Go2、Go1 和 ANYmal-D；数值不可跨机器人直接照搬。；社区用户明确说部分建议基于个人测试或尚未测试；帖子没有统一闭环。
- 适用边界：Unitree Go2 / 该用户的 Isaac Lab 训练设置；跨资产与地面材料需重测。

### Human2Humanoid 是否必须在策略蒸馏（policy distillation）阶段加入观测噪声？

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.ff52500370c9eae6`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Human2Humanoid 蒸馏阶段未加入观测噪声**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该项目贡献者只确认了一项项目事实：他们的蒸馏阶段没有加噪声，并称部署效果良好。帖子没有说明为何可行，也没有给出与加噪配置的比较，因此只能复用为 Human2Humanoid 的实现记录，不能当作其他机器人无需噪声随机化的结论。
- 证据状态：`issue_candidate`
- 来源定位：Issue #21，贡献者回复 issuecomment-2518578080
- 原帖/精确回复：[Human2Humanoid 蒸馏阶段未加入观测噪声](https://github.com/LeCAR-Lab/human2humanoid/issues/21#issuecomment-2518578080)
- 平台/作者：GitHub Issues / naivate
- 关键术语：策略蒸馏（policy distillation）；观测噪声（observation noise）；域随机化（domain randomization）
- 环境：LeCAR-Lab/human2humanoid；蒸馏阶段；具体 commit 和传感器配置未说明。
- 症状：代码审阅者发现蒸馏观测没有显式加噪。
- 处理过程：作者团队按无观测噪声的蒸馏配置完成部署。
- 结果：项目贡献者称该配置在其部署中运行良好。
- 限制：没有量化结果、对照实验、版本或适用传感器范围；不能推广为一般的“不需要噪声”。
- 独立核验引用：[maintainer_confirmation · 项目贡献者确认蒸馏未加噪且完成部署](https://github.com/LeCAR-Lab/human2humanoid/issues/21#issuecomment-2518578080)
- 适用边界：仅限该项目报告的蒸馏与部署流程；缺少版本和传感器环境。

## 足式运动、接触与地形 (`locomotion_contact_terrain`)

### 足底多维触觉对人形 WBC 可能补充什么信息？

- `problem_id`：`problem.locomotion_contact_terrain.79c948ee59fe27db`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：用足底多维触觉补充不平地面接触反馈**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：候选价值是直接提供压力/接触反馈，帮助识别不平地面、滑移和支撑变化；但该帖没有说明如何进入状态估计或 WBC，也无对照数据，因此效果仍待验证。
- 证据状态：`community_candidate`
- 来源定位：根帖正文
- 原帖/精确回复：[用足底多维触觉补充不平地面接触反馈](https://x.com/xrobohub/status/2085776135443693614)
- 平台/作者：X / RoboHub @XRoboHub
- 关键术语：全身控制（Whole-Body Control, WBC）；状态估计（State Estimation）；关节力矩（Joint Torque）；接触约束（Contact Constraint）
- 环境：T800；足底多维触觉；不平地面。
- 症状：原帖未展示具体跌倒或误判。
- 诊断：应比较有/无触觉时接触识别、滑移和姿态误差。
- 原因：缺少直接足底压力/接触反馈。
- 处理过程：在脚底集成多维触觉。
- 结果：帖子只称可改善平衡和地形感知，无量化。
- 限制：没有传感器参数、融合算法或实机对照。
- 安全提示：新增触觉不可替代力矩限位和接触失效保护。
- 图片分析：截图视频帧显示 T800 在暗场中做动态动作，无法辨认足底传感器结构或读数。
- 采集完整性：`partial_visible`；可见回复 3；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于足底接触观测不足的人形平台。

### Isaac Lab 重复物体地形缺少 platform_height 字段

- `problem_id`：`problem.locomotion_contact_terrain.isaaclab_repeated_objects_missing_platform_height_3162`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 重复物体地形缺少 platform_height 配置**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：原帖指出 repeated_objects_terrain 会读 cfg.platform_height，但相应的重复物体配置没有该字段。已合并 PR #3316 确认字段被误放在 MeshPyramidStairsTerrainCfg，并将 platform_height: float = -1.0 移到 MeshRepeatedObjectsTerrainCfg.ObjectCfg；负值代表平台高度与物体高度相同。该 PR 没有新增单元测试或 changelog，升级或回移后应亲自运行 repeated-object terrain 生成检查。
- 证据状态：`issue_candidate`
- 来源定位：Isaac Lab #3162 正文的 AttributeError 与环境；已合并 PR #3316 的描述、检查清单和文件补丁
- 原帖/精确回复：[Isaac Lab 重复物体地形缺少 platform_height 配置](https://github.com/isaac-sim/IsaacLab/issues/3162)
- 平台/作者：GitHub Issues / heleiduan
- 关键术语：重复物体地形（repeated-objects terrain）；配置字段（configuration attribute）；平台高度（platform height）；属性错误（AttributeError）
- 环境：Isaac Lab release v2.2.0，commit 46dff135f44683f031edf346e544fcfd8456b2bb；Isaac Sim 4.5；Ubuntu 22.04；RTX 5090；CUDA 12.8；GPU driver 570。
- 症状：repeated_objects_terrain 在读取 cfg.platform_height 时抛出 AttributeError: 'MeshRepeatedBoxesTerrainCfg' object has no attribute 'platform_height'。
- 诊断：对照 repeated_objects_terrain 的字段读取与 MeshRepeatedObjectsTerrainCfg.ObjectCfg 定义，检查 platform_width 附近是否定义 platform_height。；区分重复物体地形配置与金字塔楼梯地形配置，避免把字段补到不会被 repeated_objects_terrain 使用的类中。
- 原因：PR #3316 说明 platform_height 在 #2695 引入的回归中被误放到 MeshPyramidStairsTerrainCfg，而不在 MeshRepeatedObjectsTerrainCfg.ObjectCfg。
- 处理过程：原帖对照了调用代码和配置定义，提出应将字段放到重复物体配置的 platform_width 之后。；PR #3316 实际移动了字段，并修正了一处无关的 num_waves 整数默认值。
- 有效处理：使用已合并 PR #3316：从 MeshPyramidStairsTerrainCfg 删除 platform_height，在 MeshRepeatedObjectsTerrainCfg.ObjectCfg 中增加 platform_height: float = -1.0；负值仍表示使用 object height。
- 结果：PR #3316 于 2025-09-04 合并到 main，关联关闭 #3162。
- 限制：PR #3316 检查清单明确未新增证明修复有效的测试，也未更新 changelog。；补丁同时包含 num_waves 类型和格式整理；本卡只把 platform_height 移动作为 #3162 的修复。；原帖和 PR 没有提供修复后地形截图或目标 WBC 训练结果。
- 独立核验引用：[pull_request · 已合并 PR 确认参数放错类，并将其移到 MeshRepeatedObjectsTerrainCfg.ObjectCfg；检查清单未加测试](https://github.com/isaac-sim/IsaacLab/pull/3316)；[source_code · PR #3316 合并提交](https://github.com/isaac-sim/IsaacLab/commit/e57da49397fbcde5ecee501479f048957a598c22)；[issue · 项目贡献者确认问题出现在 PR #2695 合并之后](https://github.com/isaac-sim/IsaacLab/issues/3162#issuecomment-3206272649)；[issue · PR 作者明确表示先合并，单元测试将来再做](https://github.com/isaac-sim/IsaacLab/pull/3316#issuecomment-3254190994)
- 适用边界：适用于包含 #2695 回归、但尚未包含 #3316 的 Isaac Lab 重复物体 mesh terrain 配置；原帖为 v2.2.0/Isaac Sim 4.5。

### MuJoCo 高频摩擦接触的单向漂移

- `problem_id`：`problem.locomotion_contact_terrain.mujoco_high_frequency_contact_drift_2638`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo 高频交替驱动下的接触漂移与未闭环负试验**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突。
- 解答状态：`unresolved`
- 候选解答：没有。原作者按建议改成 elliptic friction 后仍有漂移；将 timestep 降到 1e-7 时漂移减小但未消失，1e-6 也有类似结果。只有将 friction coefficients 设为 0 时行为正常，这只能作为摩擦相关性对照，不是有摩擦任务的修复。原线程没有根因、补丁或已通过的回归测试。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2638，现象区分 issuecomment-2904345405；elliptic 尝试 issuecomment-2914692123；timestep/friction 对照 issuecomment-2921313334 与 2921314882
- 原帖/精确回复：[MuJoCo 高频交替驱动下的接触漂移与未闭环负试验](https://github.com/google-deepmind/mujoco/issues/2638#issuecomment-2921313334)
- 平台/作者：GitHub Issues / GitHub Issue 作者
- 关键术语：椭圆摩擦锥（elliptic friction cone）；仿真步长（simulation timestep）；接触漂移（contact drift）；负试验（negative test）
- 环境：MuJoCo 3.3.0，Linux，原始 timestep=1e-4，高频交替 motor 和摩擦接触。
- 症状：模型在交替驱动下持续向左漂移。；降低 timestep 后漂移减小但仍存在。
- 诊断：协作者先区分本帖的左向漂移与文档所述 friction-cone 内受力时的 slip。；对比 pyramidal/elliptic friction cone、timestep 1e-4 到 1e-7，以及摩擦系数为零的行为。
- 原因：原线程只能确定现象与摩擦参数相关，且对 timestep 敏感；没有确认引擎根因。
- 处理过程：按协作者建议将 friction cone 改为 elliptic。；将 timestep 降到 1e-6 乃至 1e-7。；将 friction coefficients 设为 0 作为对照。
- 结果：elliptic friction 没有消除漂移。；timestep=1e-7 时漂移较小，但仍存在；1e-6 也有类似结果。；friction coefficients=0 时，原作者报告行为正常。
- 限制：原 Issue 尚未关闭根因，没有维护者修复或回归测试。；把摩擦系数设为零只是定位对照，不是有摩擦接触任务的可用修复。；更小 timestep 只降低了幅度，不能写成解决方案。
- 安全提示：用此类模型验收真机接触控制前，需做时间步长、摩擦模型与激励频率的独立收敛检查。
- 独立核验引用：[maintainer_confirmation · 协作者区分本帖单向漂移与文档所述 friction-cone slip](https://github.com/google-deepmind/mujoco/issues/2638#issuecomment-2904345405)；[issue · 原作者报告 elliptic friction 后漂移仍存在](https://github.com/google-deepmind/mujoco/issues/2638#issuecomment-2914692123)；[issue · 原作者报告 timestep=1e-7 只降低漂移，friction=0 时行为正常](https://github.com/google-deepmind/mujoco/issues/2638#issuecomment-2921313334)；[issue · 原作者补充 timestep=1e-6 的类似结果](https://github.com/google-deepmind/mujoco/issues/2638#issuecomment-2921314882)
- 适用边界：严格限于原帖 MuJoCo 3.3.0、Linux、高频交替驱动与该接触模型；不能直接外推到所有足式机器人。

### MuJoCo 平坦 hfield 设置 positive margin 后异常弹跳，应如何判断是否是控制器问题？

- `problem_id`：`problem.locomotion_contact_terrain.87b0a9351706c261`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo hfield 使用正 margin 时出现异常弹跳**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；关键图片尚未完成分析。
- 解答状态：`unresolved`
- 候选解答：原帖用同一最小模型对照了 hfield/plane 和 margin>0/margin=0；只有 hfield 的正 margin 组合出现弹跳。MuJoCo 协作者确认当时 positive margin 总体支持不好并在修复。因此在对应版本中应先做这个接触参数消融，不能直接把弹跳归因于 WBC。线程尚无正式修复。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1817 最小 XML；协作者回复 issuecomment-2256481378
- 原帖/精确回复：[MuJoCo hfield 使用正 margin 时出现异常弹跳](https://github.com/google-deepmind/mujoco/issues/1817#issuecomment-2256481378)
- 平台/作者：GitHub Issues / Josh00-Lu
- 关键术语：高度场（height field, hfield）；接触裕量（contact margin）；参数消融（parameter ablation）
- 环境：macOS 14.5；MuJoCo 3.1.6 与 3.2.0；RK4；timestep=0.002；最小 hopper XML。
- 症状：hfield + positive margin 出现持续异常弹跳。
- 诊断：对照 hfield/plane 与 margin=1/0。
- 原因：MuJoCo 协作者确认 positive margin 支持存在问题。
- 处理过程：提问者提供可直接运行的最小 XML 和视频。
- 结果：维护者确认问题方向并保持 Issue 开放等待修复。
- 限制：没有已合并修复；不能从回复推断当前所有新版本仍有同一问题。
- 图片分析：原帖视频显示弹跳，但未做逐帧分析；卡片只依赖最小 XML 对照和维护者确认。
- 独立核验引用：[maintainer_confirmation · MuJoCo 协作者确认 positive margins 支持问题，修复尚未完成](https://github.com/google-deepmind/mujoco/issues/1817#issuecomment-2256481378)
- 适用边界：MuJoCo 3.1.6/3.2.0 的 hfield positive-margin 接触；其他版本需复测。

## IK/QP/MPC/WBC 优化问题 (`optimization_ik_qp_mpc`)

### 1 Hz 云端 Pi0.5 指令接到 100 Hz MPC 后持续抖动，应先验证哪些接口时序问题？

- `problem_id`：`problem.optimization_ik_qp_mpc.c39344a8e29643f6`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：💬Pi0.5 云端推理 + 高频 MPC，抖动问题求解**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原帖只形成候选排查方向：记录 action chunk 大小与每个样本的时间戳，确认 100 Hz 周期之间是否停住或重复陈旧目标，并测量云端往返延迟及抖动。仅做无时间语义的插值是否足够尚无结论；需要把目标保持/插值/缓冲方案与 MPC horizon 一起实验验证。
- 证据状态：`community_candidate`
- 来源定位：正文四个讨论问题及唯一可见评论
- 原帖/精确回复：[💬Pi0.5 云端推理 + 高频 MPC，抖动问题求解](https://www.xiaohongshu.com/explore/6a2a8788000000003502e5d3)
- 平台/作者：Xiaohongshu / 思蔚机器人
- 关键术语：全身控制（Whole-Body Control, WBC）；模型预测控制（Model Predictive Control, MPC）；应用程序接口（Application Programming Interface, API）；关节力矩（Joint Torque）；端到端时延（End-to-End Latency）；时延抖动（Latency Jitter）
- 环境：云端 RTX 4090 运行 Pi0.5；1 Hz 策略输出；本地 100 Hz MPC；网络往返链路。
- 症状：机械臂持续抖动，轨迹不平顺。
- 诊断：核对策略/控制频率比、action chunk 大小、旧目标复用方式、端到端延迟和延迟抖动。
- 原因：低频策略指令在 100 Hz 控制周期之间发生断层或停住。；MPC 反复跟踪陈旧目标，加上网络时延波动产生不连续纠偏。
- 处理过程：原帖只提出候选原因和讨论问题，未报告已实施的插值、缓冲或时间戳对齐方案。
- 结果：截至可见内容没有固定答案或验证结果。
- 限制：缺少 action chunk、时延分布、目标插值、MPC horizon/代价和抖动频谱数据。
- 安全提示：在抖动根因未确认前限制速度、加速度和力矩，并先在仿真或低功率模式验证多速率桥接。
- 图片分析：可见图片是帖子标题和参数摘要卡片，显示 1 Hz 云端推理、100 Hz 本地 MPC 及抖动问题；未包含控制曲线、网络时延直方图或日志，不能从图片确定抖动频率和根因。
- 采集完整性：`partial_visible`；可见回复 1；展开 0 次；回复深度 1/10；停止原因：all_visible_comments_loaded
- 适用边界：适用于低频远端策略与高频本地 MPC/WBC 的多速率系统；不代表 Pi0.5 官方推荐架构。

### WBC 的 floating_base_weight 是否越大越好？

- `problem_id`：`problem.optimization_ik_qp_mpc.3c6db17790b54178`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：mpc + wbc weight param 对四足机器人的影响**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：不是。该案例从 1e-6 增到 1e6 时接触力峰值约由 80 N 到 110 N且基体速度波动减小，但增到 1e14 后出现大幅不稳定力峰并摔倒。应在有限范围内结合力、速度和约束残差扫描，而不是单调增大。
- 证据状态：`community_candidate`
- 来源定位：正文“wbc weight param”及 fig3/fig6/1e14 失稳图
- 原帖/精确回复：[mpc + wbc weight param 对四足机器人的影响](https://zhuanlan.zhihu.com/p/650468275)
- 平台/作者：Zhihu / 杨子
- 关键术语：全身控制（Whole-Body Control, WBC）；二次规划（Quadratic Programming, QP）；模型预测控制（Model Predictive Control, MPC）；关节力矩（Joint Torque）；时延抖动（Latency Jitter）；动力学（Dynamics）
- 环境：四足机器人 trot 步态仿真；机器人质量示例约 20 kg，总重力约 200 N。
- 症状：mpc_alpha=0.1 时足底力偏小。；floating_base_weight=1e14 时足底力出现稀疏大峰值并导致摔倒。
- 诊断：比较不同权重下的足底力、基体角速度和线速度曲线。
- 原因：mpc_alpha 是力幅值惩罚项，过大抑制接触力；过小则可能放大实机对加速度变化的敏感性。；过大的 floating_base_weight 过度压低浮基动力学松弛代价与接触力之间的平衡。
- 处理过程：测试 mpc_alpha=0.1、0.0002 和约 5e-5；测试 floating_base_weight=1e-6、1e6、1e14。
- 有效处理：把 mpc_alpha 调低到能在 trot 支撑相产生接近单脚半体重的接触力，再有限度增加 floating_base_weight。
- 结果：floating_base_weight 从 1e-6 增到 1e6 时足底力峰值约从 80 N 增至 110 N且速度波动变小；1e14 时失稳摔倒。
- 限制：数值来自特定四足仿真，作者明确表示结论仍待他人指正；不能直接复制到人形机器人或不同归一化代价。
- 安全提示：权重扫描必须设置接触力、力矩与状态限幅；1e14 量级已在仿真中导致摔倒，不能直接上实机。
- 图片分析：图像“mpc_alpha=0.1”同时展示四足仿真和足底力曲线；曲线幅值较低，与正文所述支撑力不足相符，但截图本身未给出统一坐标标定。；图像“floating_base_weight=1e6”显示较规则的周期性足底力波形，峰值约在 110 N 附近；可用于和正文所述 1e-6 时约 80 N 的结果比较。；图像“floating_base_weight=1e14”显示稀疏而幅值很大的足底力尖峰，对应正文中的接触力不稳定和摔倒现象。
- 采集完整性：`partial_visible`；可见回复 2；展开 0 次；回复深度 1/10；停止原因：no_visible_expand_controls
- 适用边界：属于单一四足仿真观察，必须在目标控制器的代价缩放下重做参数扫描。

### MPC 的接触力权重 mpc_alpha 过大或过小时会怎样？

- `problem_id`：`problem.optimization_ik_qp_mpc.9f43bf1f0efb97ff`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：mpc + wbc weight param 对四足机器人的影响**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：在该仿真中，mpc_alpha 过大会强烈惩罚足端力，使支撑力不足；减小它会提高足底力。作者以 trot 支撑脚约承担半个机器人重量为经验目标。评论提醒权重过小会使实机对加速度变化敏感并可能剧烈抖动，因此不能只追求更大接触力。
- 证据状态：`community_candidate`
- 来源定位：正文“MPC weight param”及首条评论
- 原帖/精确回复：[mpc + wbc weight param 对四足机器人的影响](https://zhuanlan.zhihu.com/p/650468275)
- 平台/作者：Zhihu / 杨子
- 关键术语：全身控制（Whole-Body Control, WBC）；二次规划（Quadratic Programming, QP）；模型预测控制（Model Predictive Control, MPC）；关节力矩（Joint Torque）；时延抖动（Latency Jitter）；动力学（Dynamics）
- 环境：四足机器人 trot 步态仿真；机器人质量示例约 20 kg，总重力约 200 N。
- 症状：mpc_alpha=0.1 时足底力偏小。；floating_base_weight=1e14 时足底力出现稀疏大峰值并导致摔倒。
- 诊断：比较不同权重下的足底力、基体角速度和线速度曲线。
- 原因：mpc_alpha 是力幅值惩罚项，过大抑制接触力；过小则可能放大实机对加速度变化的敏感性。；过大的 floating_base_weight 过度压低浮基动力学松弛代价与接触力之间的平衡。
- 处理过程：测试 mpc_alpha=0.1、0.0002 和约 5e-5；测试 floating_base_weight=1e-6、1e6、1e14。
- 有效处理：把 mpc_alpha 调低到能在 trot 支撑相产生接近单脚半体重的接触力，再有限度增加 floating_base_weight。
- 结果：floating_base_weight 从 1e-6 增到 1e6 时足底力峰值约从 80 N 增至 110 N且速度波动变小；1e14 时失稳摔倒。
- 限制：数值来自特定四足仿真，作者明确表示结论仍待他人指正；不能直接复制到人形机器人或不同归一化代价。
- 安全提示：权重扫描必须设置接触力、力矩与状态限幅；1e14 量级已在仿真中导致摔倒，不能直接上实机。
- 图片分析：图像“mpc_alpha=0.1”同时展示四足仿真和足底力曲线；曲线幅值较低，与正文所述支撑力不足相符，但截图本身未给出统一坐标标定。；图像“floating_base_weight=1e6”显示较规则的周期性足底力波形，峰值约在 110 N 附近；可用于和正文所述 1e-6 时约 80 N 的结果比较。；图像“floating_base_weight=1e14”显示稀疏而幅值很大的足底力尖峰，对应正文中的接触力不稳定和摔倒现象。
- 采集完整性：`partial_visible`；可见回复 2；展开 0 次；回复深度 1/10；停止原因：no_visible_expand_controls
- 适用边界：只适用于代价定义、质量和力归一化相近的 MPC；具体数值需重新标定。

### 200 Hz 学习策略是否足以直接替代高频低层控制环？

- `problem_id`：`problem.optimization_ik_qp_mpc.45d8941039d8b688`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：关于 Figure 01 低层 WBC、QP 与直接力矩输出的技术讨论**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：回复者推测 200 Hz 虽已很高，但仍不等价于 1 kHz 以上的快速低层控制；是否需要额外 whole-body constrained controller 取决于系统时延、执行器带宽和安全约束。原串没有测试结果，结论未解决。
- 证据状态：`community_candidate`
- 来源定位：@iandanforth 关于 200 Hz 与 1 kHz+ 的回复
- 原帖/精确回复：[关于 Figure 01 低层 WBC、QP 与直接力矩输出的技术讨论](https://x.com/iandanforth/status/1767957601751302285)
- 平台/作者：X / huaijiang @huaijiangzhu
- 关键术语：全身控制（Whole-Body Control, WBC）；二次规划（Quadratic Programming, QP）；应用程序接口（Application Programming Interface, API）；执行器（Actuator）；关节力矩（Joint Torque）；接触约束（Contact Constraint）
- 环境：Figure 01 双臂操作公开演示；学习策略约 200 Hz；讨论者假设存在更高频低层控制环。
- 症状：没有报告具体故障；讨论关注 200 Hz 策略频率是否足以直接承担低层力矩控制。
- 诊断：区分学习策略输出的 setpoint 与实际低层跟踪器；检查是否存在任务空间加速度目标、全身动力学约束和直接力矩输出。
- 原因：200 Hz 学习模型可能不足以替代 1 kHz 级快速约束控制；冗余任务空间命令需要动力学和约束消解。
- 处理过程：讨论者提出 QP-based task-space inverse dynamics 作为可能结构。
- 结果：形成了一个可实现的 QP 表述，但没有得到 Figure 团队确认，也没有控制日志或源码。
- 限制：核心结构使用 I'd guess 等推测语气；不得把它写成 Figure 01 已确认架构。
- 安全提示：直接力矩控制必须同时验证动力学、接触约束、扭矩/速度限位和控制周期；不能依据社交平台推测直接上实机。
- 采集完整性：`partial_visible`；可见回复 8；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于低频学习策略与高频 WBC/执行器控制的多速率架构设计。

### 学习策略给出 task-space setpoint 后，QP-based WBC 如何求关节力矩？

- `problem_id`：`problem.optimization_ik_qp_mpc.dbcd76d74f91b430`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：关于 Figure 01 低层 WBC、QP 与直接力矩输出的技术讨论**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该讨论给出的候选表述是：把任务写成最小化 task-space acceleration error，在约束中加入 whole-body dynamics，再由 constrained QP 求 joint torque。这个说明可作为理解 task-space inverse dynamics 的工程入口，但它只是对 Figure 01 的推测，不是官方架构说明。
- 证据状态：`community_candidate`
- 来源定位：@huaijiangzhu 根回复及后续具体 QP 解释
- 原帖/精确回复：[关于 Figure 01 低层 WBC、QP 与直接力矩输出的技术讨论](https://x.com/huaijiangzhu/status/1767955458055118951)
- 平台/作者：X / huaijiang @huaijiangzhu
- 关键术语：全身控制（Whole-Body Control, WBC）；二次规划（Quadratic Programming, QP）；应用程序接口（Application Programming Interface, API）；关节力矩（Joint Torque）；接触约束（Contact Constraint）；动力学（Dynamics）
- 环境：Figure 01 双臂操作公开演示；学习策略约 200 Hz；讨论者假设存在更高频低层控制环。
- 症状：没有报告具体故障；讨论关注 200 Hz 策略频率是否足以直接承担低层力矩控制。
- 诊断：区分学习策略输出的 setpoint 与实际低层跟踪器；检查是否存在任务空间加速度目标、全身动力学约束和直接力矩输出。
- 原因：200 Hz 学习模型可能不足以替代 1 kHz 级快速约束控制；冗余任务空间命令需要动力学和约束消解。
- 处理过程：讨论者提出 QP-based task-space inverse dynamics 作为可能结构。
- 结果：形成了一个可实现的 QP 表述，但没有得到 Figure 团队确认，也没有控制日志或源码。
- 限制：核心结构使用 I'd guess 等推测语气；不得把它写成 Figure 01 已确认架构。
- 安全提示：直接力矩控制必须同时验证动力学、接触约束、扭矩/速度限位和控制周期；不能依据社交平台推测直接上实机。
- 采集完整性：`partial_visible`；可见回复 8；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于需要把冗余任务空间目标映射为满足全身动力学约束力矩的控制器设计。

### OCS2 全身 NMPC 中支撑足零速度约束一直违反时，应先改哪里？

- `problem_id`：`problem.optimization_ik_qp_mpc.ea25d896b6308df9`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OCS2 全身 NMPC 中支撑足零速度约束持续违反**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先确认该约束是否被写成仅依赖状态的等式；社区回复建议把它重写为加速度层的状态—输入等式约束，并避免仅用惩罚项硬压等式残差。梯度计算占时较大时，可再评估 Pinocchio 的解析导数。
- 证据状态：`issue_candidate`
- 来源定位：社区技术回复 @FenglongSong
- 原帖/精确回复：[OCS2 全身 NMPC 中支撑足零速度约束持续违反](https://github.com/leggedrobotics/ocs2/issues/106#issuecomment-2269221824)
- 平台/作者：GitHub Issues / lrchit
- 关键术语：全身控制（Whole-Body Control, WBC）；非线性模型预测控制（Nonlinear Model Predictive Control, NMPC）；顺序二次规划（Sequential Quadratic Programming, SQP）；接触约束（Contact Constraint）
- 环境：OCS2、Pinocchio、全身 NMPC、状态为 q 与 ν、输入为地面反力与关节力矩。
- 症状：支撑足持续滑移，部分运行直接崩溃。
- 诊断：先区分纯状态等式约束与状态—输入等式约束，再核对所用 SQP 求解器支持范围。
- 原因：把足端零速度写成纯状态等式约束，而该求解路径无法直接处理。
- 处理过程：原作者尝试约束观察器和惩罚方法，但滑移仍存在。
- 有效处理：社区建议改为加速度层足端约束，使其成为状态—输入等式约束。
- 结果：回复给出可执行重构方向，但原作者没有在 Issue 中贴出最终实测结果。
- 限制：结论来自社区实践；回复还说明其对 OCS2 SQP 能力的判断基于此前版本，应按当前版本复核。
- 安全提示：实机前应检查足端约束残差和摩擦裕度，避免把仿真滑移带入硬件。
- 图片分析：Issue 含足端约束观察器截图和滑移视频；本轮只依据作者文字描述确认现象，图中具体数值尚未逐像素复核。
- 适用边界：适用于以 q、ν 为状态并用 SQP 求解的 OCS2 全身 NMPC；其他求解器需重新确认约束支持。

### 把 legged_control 迁移到自研足式机器人，最小需要改哪两层？

- `problem_id`：`problem.optimization_ik_qp_mpc.a81b614d6edd02df`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Legged-Control 真机适配边界与 NMPC-WBC 安全启动顺序**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：硬件层仿照 UnitreeHW 继承 LeggedHW，实现 read() 和 write()；模型层仿照 legged_unitree_description 编写 xacro/URDF，并满足框架使用的 joint/link 命名约定。这样可把平台差异收敛在硬件接口与模型描述，不必侵入 NMPC/WBC 主体。
- 证据状态：`community_candidate`
- 来源定位：正文‘你自己开发的机器人’；官方 README Deploy and Develop
- 原帖/精确回复：[Legged-Control 真机适配边界与 NMPC-WBC 安全启动顺序](https://zhuanlan.zhihu.com/p/567381895)
- 平台/作者：Zhihu / 廖洽源
- 关键术语：硬件抽象层（hardware abstraction layer）；机器人描述（URDF/xacro）；读写接口（read/write interface）
- 环境：ROS/ros-control；OCS2；A1；作者使用 11 代 NUC，NMPC 频率接近 200 Hz；仓库当前注明停止维护。
- 症状：直接修改主仓库会让硬件适配难以维护。；真机误启 cheater controller 或在机载机运行 Gazebo 会造成错误状态/资源风险。
- 诊断：对照官方仓库目录检查硬件接口、描述文件、控制器和状态估计是否分层。
- 原因：硬件读写接口与关节命名未满足框架假设。；把仿真真值状态或仿真负载带到真机流程。
- 处理过程：继承 LeggedHW 并实现 read()/write()。；仿照 unitree_description 生成 URDF 并保持 joint/link 命名约定。；真机只启动真实状态估计和 legged_controller。
- 有效处理：通过 ros-control 硬件接口隔离平台差异；按官方启动顺序分离 simulation 与 hardware。
- 结果：官方 README 列出多个实验室在 A1 上跑通，并给出 2 小时至 1 天的历史记录；作者文与仓库结构一致。
- 限制：仓库已停止维护；版本、依赖和安全边界需按当前 fork 重新验证。
- 安全提示：官方 README 明确真机不得启动 cheater controller；首次控制应使用吊架、低增益、限力和急停。
- 图片分析：正文框架图展示目标轨迹→NMPC→WBC→前馈力矩+低增益 PD，以及 IMU/电机状态→卡尔曼滤波；仓库 README 文字与此一致。
- 独立核验引用：[source_code · README Deploy and Develop：继承 LeggedHW 实现 read/write，并保持描述文件 joint/link 命名](https://github.com/qiayuanl/legged_control)
- 采集完整性：`partial_visible`；可见回复 10；展开 1 次；回复深度 2/10；停止原因：remaining_comments_collapsed
- 适用边界：适用于该 ROS1/ros-control 框架；仓库已停止维护，现代系统需评估迁移成本。

### Legged-Control 从仿真切到真机时，哪些启动方式必须禁止？

- `problem_id`：`problem.optimization_ik_qp_mpc.ed9f426f438d13bd`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Legged-Control 真机适配边界与 NMPC-WBC 安全启动顺序**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：不要在机载计算机上编译/运行 Gazebo 仿真模块，也不要在真实硬件启动 legged_cheater_controller，因为它依赖仿真真值状态。真机应启动硬件接口、真实状态估计和 legged_controller，并在低风险条件下逐级放开目标与增益。
- 证据状态：`community_candidate`
- 来源定位：官方 README Build / Quick Start 的硬件警告，正文框架与状态估计说明
- 原帖/精确回复：[Legged-Control 真机适配边界与 NMPC-WBC 安全启动顺序](https://zhuanlan.zhihu.com/p/567381895)
- 平台/作者：Zhihu / 廖洽源
- 关键术语：真值状态（ground-truth state）；状态估计（state estimation）；机载计算（onboard computing）
- 环境：ROS/ros-control；OCS2；A1；作者使用 11 代 NUC，NMPC 频率接近 200 Hz；仓库当前注明停止维护。
- 症状：直接修改主仓库会让硬件适配难以维护。；真机误启 cheater controller 或在机载机运行 Gazebo 会造成错误状态/资源风险。
- 诊断：对照官方仓库目录检查硬件接口、描述文件、控制器和状态估计是否分层。
- 原因：硬件读写接口与关节命名未满足框架假设。；把仿真真值状态或仿真负载带到真机流程。
- 处理过程：继承 LeggedHW 并实现 read()/write()。；仿照 unitree_description 生成 URDF 并保持 joint/link 命名约定。；真机只启动真实状态估计和 legged_controller。
- 有效处理：通过 ros-control 硬件接口隔离平台差异；按官方启动顺序分离 simulation 与 hardware。
- 结果：官方 README 列出多个实验室在 A1 上跑通，并给出 2 小时至 1 天的历史记录；作者文与仓库结构一致。
- 限制：仓库已停止维护；版本、依赖和安全边界需按当前 fork 重新验证。
- 安全提示：官方 README 明确真机不得启动 cheater controller；首次控制应使用吊架、低增益、限力和急停。
- 图片分析：正文框架图展示目标轨迹→NMPC→WBC→前馈力矩+低增益 PD，以及 IMU/电机状态→卡尔曼滤波；仓库 README 文字与此一致。
- 独立核验引用：[source_code · README 明确 simulation 不在 onboard computer 运行，real hardware 不得启动 legged_cheater_controller](https://github.com/qiayuanl/legged_control)
- 采集完整性：`partial_visible`；可见回复 10；展开 1 次；回复深度 2/10；停止原因：remaining_comments_collapsed
- 适用边界：适用于 legged_control；其他框架也应明确真值状态与实测状态的边界。

### Isaac Lab 浮动基机器人差分 IK 异常时，为什么 joint_ids 会取错 Jacobian 列？

- `problem_id`：`problem.optimization_ik_qp_mpc.6e6c26f5b03edfc2`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 浮动基差分 IK 的 Jacobian 关节索引偏移**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：PhysX 为浮动基 articulation 返回的 Jacobian 在关节列之前含 6 个根位姿自由度；直接用 joint_ids 会整体左移 6 列。对应版本的修复是在浮动基分支为索引加 6。升级版本应优先按当前 API 的自由度布局计算偏移，并用有限差分验证。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1032 描述；merged PR #1033 description/commit d282255
- 原帖/精确回复：[Isaac Lab 浮动基差分 IK 的 Jacobian 关节索引偏移](https://github.com/isaac-sim/IsaacLab/issues/1032)
- 平台/作者：GitHub Issues / lorenwel
- 关键术语：浮动基（floating base）；雅可比矩阵（Jacobian）；根位姿自由度（root-pose DOFs）
- 环境：Isaac Sim 4.0.0；Isaac Lab commit 9ab6b48；floating-base articulation。
- 症状：DifferentialInverseKinematicsAction 在浮动基系统不能正确工作。
- 诊断：检查 PhysX Jacobian 最后一维，确认前 6 列对应根位姿而非驱动关节。
- 原因：固定基系统的 joint_ids 被直接用于浮动基 Jacobian，缺少 6 列根自由度偏移。
- 处理过程：在浮动基分支索引时对 joint_ids 加 6。
- 有效处理：PR #1033 修改索引并合入 isaac-sim/IsaacLab main。
- 结果：代码所有者批准，commit d282255 于 2024-09-25 合并，Issue 关闭。
- 限制：适用于该 API/版本布局；升级后应查当前张量契约，不能永远硬编码 +6。
- 安全提示：部署到真机前用有限差分或可视化验证 Jacobian 方向和列映射。
- 独立核验引用：[pull_request · merged PR：浮动基 Jacobian joint indices 加 6；code owner approved；commit d282255](https://github.com/isaac-sim/IsaacLab/pull/1033)
- 适用边界：Isaac Sim 4.0.0 / 当时 Isaac Lab；其他版本需核对 Jacobian tensor contract。

### Pinocchio 的 Jdot 或 dJdq 不一致时，JointModelFreeFlyer 和直接自动微分方案是否已经验证？

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_jdot_composite_joint`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：2（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio Composite Joint 下 dJdq/Jdot 不一致的两个处理方向都仍需复测**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：没有。维护者只说明 Translation+SphericalZYX 的 JointModelComposite 尚未完整支持，并建议用 JointModelFreeFlyer；原作者没有回报该替换后的结果，随后还用两个普通转动关节构造了新的异常最小例子，但没有得到答复。因此 FreeFlyer 是维护者给出的排查方向，不是该线程已复测的通用修复。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2519，维护者说明 issuecomment-2554021580 与建议 issuecomment-2555687851；原作者后续最小复现 issuecomment-2555915806
- 原帖/精确回复：[Pinocchio Composite Joint 下 dJdq/Jdot 不一致的两个处理方向都仍需复测](https://github.com/stack-of-tasks/pinocchio/issues/2519#issuecomment-2555687851)
- 平台/作者：GitHub Issues / min-dai
- 关键术语：雅可比时间变化率（Jacobian time variation）；复合关节模型（JointModelComposite）；自由浮动关节模型（JointModelFreeFlyer）；局部世界对齐坐标系（LOCAL_WORLD_ALIGNED）
- 环境：原始模型使用 JointModelComposite(Translation + SphericalZYX) 与 LOCAL_WORLD_ALIGNED；后续最小复现为两个转动关节；2026 评论使用 Pinocchio CasADi 接口，具体版本未说明。
- 症状：原模型中两个 dJdq 结果不同；改为两转动关节最小模型后，原作者仍报告 dJ 与手算预期存在偏差。
- 诊断：先识别根关节模型是否为尚未完整支持的 JointModelComposite；同时用最小模型、解析预期或自动微分交叉比较 Jdot 和 Jdot*qdot。
- 原因：维护者只明确指出 JointModelComposite 可能是原始问题主因且未完整支持；后续固定基最小复现的原因没有答案。
- 处理过程：维护者建议 JointModelFreeFlyer；原作者补充两转动关节最小复现；另一用户提供 CasADi jacobian(J,q)@qdot 的替代函数。
- 结果：Issue 在 2024-12-19 关闭，但没有原作者确认 FreeFlyer 解决问题；2026 的 CasADi 方案也没有线程复测或维护者确认。
- 限制：不能把关闭状态视为修复完成；不能把未验证的 CasADi 代码当成与 Pinocchio 所有参考系约定等价。
- 图片分析：原作者的后续最小复现包含输出截图，但本卡只采用其文字、代码和手写预期，不从截图补读矩阵数值。
- 独立核验引用：[maintainer_confirmation · 维护者说明 JointModelComposite 尚未完整支持](https://github.com/stack-of-tasks/pinocchio/issues/2519#issuecomment-2554021580)；[issue · 原作者给出不含 Composite Joint 的最小复现，但线程没有后续答案](https://github.com/stack-of-tasks/pinocchio/issues/2519#issuecomment-2555915806)
- 适用边界：原始建议针对 Translation+SphericalZYX JointModelComposite；后续固定基两关节异常不在该建议的已验证范围内。

**经验 2：Pinocchio Composite Joint 下 dJdq/Jdot 不一致的两个处理方向都仍需复测**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：没有。2026 年评论者提供的代码先计算 Frame Jacobian，将 J 展平后求 ca.jacobian(J_flat,q)@qdot，再重排成 6×nv；这只是该评论者分享的处理方法。线程没有给出与解析结果、Pinocchio 修复版本或其他参考系的数值对照，也没有维护者确认，因此只能作为待复现实验方案。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2519，社区方案 issuecomment-5217419143
- 原帖/精确回复：[Pinocchio Composite Joint 下 dJdq/Jdot 不一致的两个处理方向都仍需复测](https://github.com/stack-of-tasks/pinocchio/issues/2519#issuecomment-5217419143)
- 平台/作者：GitHub Issues / min-dai
- 关键术语：自动微分（automatic differentiation, AD）；雅可比时间变化率（Jacobian time variation）；卡萨迪（CasADi）；局部坐标系（LOCAL）
- 环境：原始模型使用 JointModelComposite(Translation + SphericalZYX) 与 LOCAL_WORLD_ALIGNED；后续最小复现为两个转动关节；2026 评论使用 Pinocchio CasADi 接口，具体版本未说明。
- 症状：原模型中两个 dJdq 结果不同；改为两转动关节最小模型后，原作者仍报告 dJ 与手算预期存在偏差。
- 诊断：先识别根关节模型是否为尚未完整支持的 JointModelComposite；同时用最小模型、解析预期或自动微分交叉比较 Jdot 和 Jdot*qdot。
- 原因：维护者只明确指出 JointModelComposite 可能是原始问题主因且未完整支持；后续固定基最小复现的原因没有答案。
- 处理过程：维护者建议 JointModelFreeFlyer；原作者补充两转动关节最小复现；另一用户提供 CasADi jacobian(J,q)@qdot 的替代函数。
- 结果：Issue 在 2024-12-19 关闭，但没有原作者确认 FreeFlyer 解决问题；2026 的 CasADi 方案也没有线程复测或维护者确认。
- 限制：不能把关闭状态视为修复完成；不能把未验证的 CasADi 代码当成与 Pinocchio 所有参考系约定等价。
- 图片分析：原作者的后续最小复现包含输出截图，但本卡只采用其文字、代码和手写预期，不从截图补读矩阵数值。
- 独立核验引用：[issue · 评论者给出 CasADi 直接计算 Jdot 的完整函数，但没有结果对照](https://github.com/stack-of-tasks/pinocchio/issues/2519#issuecomment-5217419143)
- 适用边界：仅适用于能够使用 Pinocchio CasADi 模型并明确 J(q)、qdot 与参考系约定的场景；尚未在原线程交叉验证。

### Pinocchio 3.3 的 LOCAL_WORLD_ALIGNED 速度配置导数与 CppAD 不一致时，应如何定位版本和参考系边界？

- `problem_id`：`problem.optimization_ik_qp_mpc.e7febfb8784bf534`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 3.3 的 LOCAL_WORLD_ALIGNED 速度配置导数与 CppAD 不一致**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原帖的完整复现表明，Pinocchio 3.3.0 中 LOCAL_WORLD_ALIGNED 的对 q 导数不匹配，而对 v 导数匹配，LOCAL/WORLD 对照也正常。项目成员说明 LOCAL 之外的参考系含额外修正；维护者随后明确称该问题已在 Pinocchio 4 修复。因此应先用原帖同样的 integrate+CppAD 对照确认，再在目标 Pinocchio 4 构建上复测。不能仅为了数值一致改用不同参考系，除非任务定义允许。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2702，项目成员解释 issuecomment-2973723866；维护者版本说明 issuecomment-2992232477
- 原帖/精确回复：[Pinocchio 3.3 的 LOCAL_WORLD_ALIGNED 速度配置导数与 CppAD 不一致](https://github.com/stack-of-tasks/pinocchio/issues/2702#issuecomment-2992232477)
- 平台/作者：GitHub Issues / Zionshang
- 关键术语：局部世界对齐坐标系（LOCAL_WORLD_ALIGNED）；解析导数（analytical derivative）；自动微分（automatic differentiation, AD）；配置流形（configuration manifold）
- 环境：Ubuntu 22.04；Pinocchio 3.3.0；Go2 URDF；JointModelFreeFlyer；CppAD；原帖完整 C++ 复现。
- 症状：v_partial_dq 与 CppAD djoint_vel_dq 不一致；v_partial_dv 一致；改用 WORLD 或 LOCAL 后作者观察结果正确。
- 诊断：同时比较对 q 和 v 的导数；对 CppAD 路径先调用 integrate 满足流形约束；分别测试 LOCAL、WORLD 与 LOCAL_WORLD_ALIGNED。
- 原因：项目成员说明速度、integrate 和 difference 的定义对应 LOCAL；其他参考系会加入额外修正，而原有自动微分系统不能开箱即用处理这些修正。
- 处理过程：原作者在 CppAD 中通过 integrate 处理配置流形，并交叉比较三种参考系。
- 有效处理：维护者表示该 LOCAL_WORLD_ALIGNED 导数已在 Pinocchio 4 修复；线程没有提供可精确定位的提交。
- 结果：维护者确认问题已知并给出 Pinocchio 4 修复边界；原作者没有在 Pinocchio 4 上回报复测。
- 限制：在没有精确提交和升级复测的情况下，不能把任意 Pinocchio 4 构建都自动视为已验证；改用 LOCAL/WORLD 只能在任务语义允许时作为对照，不应为匹配数值而改变参考系定义。
- 独立核验引用：[maintainer_confirmation · 维护者说明 LOCAL_WORLD_ALIGNED 导数已在 Pinocchio 4 修复](https://github.com/stack-of-tasks/pinocchio/issues/2702#issuecomment-2992232477)；[maintainer_confirmation · 项目成员解释 LOCAL 定义与其他参考系额外修正](https://github.com/stack-of-tasks/pinocchio/issues/2702#issuecomment-2973723866)
- 适用边界：已明确复现于 Ubuntu 22.04、Pinocchio 3.3.0、Go2 FreeFlyer；Pinocchio 4 的修复仍需在目标构建复测。

### TSID 只设置速度界时出现非预期 QP 不可行，应如何检查 TaskJointPosVelAccBounds 的默认位置界？

- `problem_id`：`problem.optimization_ik_qp_mpc.ee1a0c4101fa8789`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：TSID 旧版位置上下界默认值写反会让仅设置速度界的任务潜在不可行**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：检查旧版构造函数是否把 qMin/qMax 写成 +1e10/-1e10。该顺序使下界大于上界；常规显式重设位置界会掩盖问题，但只设置速度界时可能触发不可行。已合并 PR #159 将默认值改为 qMin=-1e10、qMax=+1e10。旧版除回移修复外，也必须在使用前显式设置正确位置界。
- 证据状态：`issue_candidate`
- 来源定位：Issue #158，维护者确认 issuecomment-1056957094 与修复确认 issuecomment-1292023533；已合并 PR #159
- 原帖/精确回复：[TSID 旧版位置上下界默认值写反会让仅设置速度界的任务潜在不可行](https://github.com/stack-of-tasks/tsid/issues/158#issuecomment-1292023533)
- 平台/作者：GitHub Issues / paulinejmaurice
- 关键术语：关节位置界（joint position bounds）；速度界（velocity bounds）；不可行问题（infeasible problem）；二次规划（Quadratic Programming, QP）
- 环境：2022-03 的 TSID TaskJointPosVelAccBounds 旧实现；具体发行版本和机器人未说明。
- 症状：默认 qMin=+1e10、qMax=-1e10，导致 qMin>qMax；依赖默认位置界时可能生成不可行约束。
- 诊断：打印或检查 TaskJointPosVelAccBounds 构造后的 qMin/qMax；确认是否在使用前显式重设位置界。
- 原因：构造函数中默认上下界的正负号交换。
- 处理过程：提问者定位到构造代码；维护者确认并请求提交 PR。
- 有效处理：采用已合并 PR #159，把默认 qMin 改为 -1e10、qMax 改为 +1e10；旧版也可显式设置正确位置界避免依赖错误默认值。
- 结果：PR #159 于 2022-03-02 合并，维护者后续明确回复该问题已由 #159 修复。
- 限制：原线程没有给出一个实际 QP 失败日志或新增回归测试；影响条件是未覆盖默认位置界。
- 安全提示：实机前仍应检查配置后的实际上下界，不能只依赖极大默认值作为安全限位。
- 独立核验引用：[pull_request · PR 交换 qMin/qMax 默认值并已合并](https://github.com/stack-of-tasks/tsid/pull/159)；[source_code · PR #159 合并提交](https://github.com/stack-of-tasks/tsid/commit/672de79de6ec83618b699428fc9574dbef8d5f1a)；[maintainer_confirmation · 维护者确认报告正确并请求修复 PR](https://github.com/stack-of-tasks/tsid/issues/158#issuecomment-1056957094)
- 适用边界：适用于包含错误默认值的 TSID 旧版本；若调用方总是显式覆盖位置界，该特定错误不会直接触发。

### TSID 姿态任务在 nq != nv 的球关节或连续关节机器人上，如何正确计算关节配置误差？

- `problem_id`：`problem.optimization_ik_qp_mpc.4336ee335cd76f7b`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：TSID 姿态任务在 nq 不等于 nv 时必须用流形差分计算关节误差**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：不能继续用 q.tail(na) 与参考逐元素相减。已合并 PR #161 的实现先区分关节配置维数 nq_actuated 与执行器速度维数 na，用 neutral 配置构造包含根部的增广参考，把关节参考写入尾部，然后调用 pinocchio::difference(model, ref_augmented, q)，最后取末尾 na 个速度空间误差。该 PR 同时加入含球关节模型的姿态收敛测试。
- 证据状态：`issue_candidate`
- 来源定位：Issue #160 完整讨论；关闭回复 issuecomment-1231751666；已合并 PR #161 与合并提交 4caf44f
- 原帖/精确回复：[TSID 姿态任务在 nq 不等于 nv 时必须用流形差分计算关节误差](https://github.com/stack-of-tasks/tsid/issues/160#issuecomment-1231751666)
- 平台/作者：GitHub Issues / EtienneAr
- 关键术语：配置流形（configuration manifold）；流形差分（manifold difference）；关节姿态任务（joint posture task）；浮动基（floating base）
- 环境：TSID 旧提交 b0d6bff；问题覆盖 revolute unbounded joint 与 spherical joint；PR #161 的测试模型包含球关节，固定基测试中 nq != nv。
- 症状：配置向量按 na 裁剪时维数错误，且流形配置的 difference(q1,q2) 不等于 q2-q1，姿态任务误差计算不正确。
- 诊断：比较 model.nq、model.nv、robot.na 与关节类型；检查姿态参考是配置空间还是速度空间维数；对球关节/连续关节使用 Pinocchio 流形差分而不是逐元素相减。
- 原因：旧实现假设除根关节外所有关节均满足 nq=nv，并把关节配置裁剪长度与执行器速度维数 na 混用。
- 处理过程：讨论先澄清姿态参考不应包含浮动基；维护者建议构造包含浮动基配置的增广参考，执行完整模型 difference 后取关节部分。
- 有效处理：采用已合并 PR #161：RobotWrapper 显式保存 nq_actuated/is_fixed_base；用 neutral 配置构造增广参考，把关节参考写入尾部；计算 pinocchio::difference(model, ref_augmented, q) 后取末尾 na 个速度空间误差。
- 结果：PR #161 于 2022-04-11 合并；补丁新增含球关节的 7-DoF 模型，并在最多 1000 步的姿态任务测试中要求误差单调下降并达到 1e-8；原作者随后以 PR 已合并关闭 Issue。
- 限制：PR 中 nq_actuated 对浮动基按 nq-7 处理；自定义根关节或其他配置结构仍应核对该假设和目标 TSID 版本。
- 独立核验引用：[pull_request · PR 修复 nq != nv 的 TaskJointPosture，并加入含球关节回归测试，已合并](https://github.com/stack-of-tasks/tsid/pull/161)；[source_code · PR #161 合并提交](https://github.com/stack-of-tasks/tsid/commit/4caf44f54e65067d1f4862d5114bc3af7fc40f75)；[maintainer_confirmation · 维护者确认需要修复，但要求姿态参考仍只包含关节部分](https://github.com/stack-of-tasks/tsid/issues/160#issuecomment-1060381798)
- 适用边界：适用于包含球关节、无界转动关节等 nq != nv 结构并使用包含 PR #161 的 TSID；自定义根关节需复核 nq_actuated 假设。

### Pinocchio difference 对 FreeFlyer 默认位置上界返回 NaN 时，怎样区分非法流形输入与真实关节限位？

- `problem_id`：`problem.optimization_ik_qp_mpc.8e1c4cf9a514a227`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio difference 只对合法流形配置有定义，不能直接把默认极值界当配置**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：pin.difference 的两个输入必须是关节配置流形上的合法配置。原线程中 FreeFlyer 的 upperPositionLimit 把 max-float 同时放进平移和四元数，旋转部分不是合法单位四元数，因此返回 NaN；维护者也说明 FreeFlyer 旋转界通常没有意义。线程复现表明，保留大平移但把旋转设为合法的 \[0,0,0,1\] 后，difference 才返回预期平移差。该做法只说明输入有效性，不等于得到了一套通用运行时限位 API。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1752，维护者边界说明 issuecomment-1259556298/1259557411；有效 FreeFlyer 对照 issuecomment-1263723540
- 原帖/精确回复：[Pinocchio difference 只对合法流形配置有定义，不能直接把默认极值界当配置](https://github.com/stack-of-tasks/pinocchio/issues/1752#issuecomment-1263723540)
- 平台/作者：GitHub Issues / stephane-caron
- 关键术语：流形差分（manifold difference）；李群（Lie group）；自由浮动关节（JointModelFreeFlyer）；关节限位（joint limits）
- 环境：Pinocchio 2.6.4；Python 最小示例；JointModelFreeFlyer、JointModelRZ 与 JointModelRUBZ 对照。
- 症状：FreeFlyer neutral 到 upperPositionLimit 的 difference 返回 6 个 NaN；不同关节类型对 max-float 默认界表现不同。
- 诊断：检查传给 difference 的两个向量是否都是该关节流形上的合法配置；对 FreeFlyer 单独检查旋转四元数单位范数；不要把 max-float 默认占位自动视为运行时关节界。
- 原因：difference 定义在 Lie group 配置上；FreeFlyer 的 max-float 旋转分量不是合法四元数，默认界还可能来自内部占位计算，输出不能保证固定。
- 处理过程：维护者建议区分无界关节类型和有效输入；讨论者分别测试全 1e20 FreeFlyer 与大平移加单位四元数。
- 有效处理：确保传入 difference 的旋转部分是合法流形元素；线程示例用大平移加 \[0,0,0,1\] 单位四元数后得到 \[1e20,1e20,1e20,0,0,0\]。
- 结果：原作者表示初始 difference API 问题已由 PR #1753 处理；维护者最后确认应在 Pinocchio 中为无界关节使用合适的 neutral 边界，但运行时限位到切空间的统一映射留到后续问题。
- 限制：线程不支持把 1e20 当成通用安全限位，也没有给出所有关节类型的统一 runtime-limit API；输入极值仍可能导致数值问题。
- 安全提示：实机 IK/WBC 限位必须来自明确的硬件/URDF 约束；不要把库的默认极大占位当作安全边界。
- 独立核验引用：[maintainer_confirmation · 维护者说明 difference 作用于 Lie group，有效输入由使用者保证](https://github.com/stack-of-tasks/pinocchio/issues/1752#issuecomment-1259556298)；[maintainer_confirmation · 维护者说明 FreeFlyer 旋转界无一般意义，NaN 来自该部分](https://github.com/stack-of-tasks/pinocchio/issues/1752#issuecomment-1259557411)；[issue · 原作者对比非法全极值配置与合法单位四元数配置的实际输出](https://github.com/stack-of-tasks/pinocchio/issues/1752#issuecomment-1263723540)
- 适用边界：复现对应 Pinocchio 2.6.4 的 FreeFlyer/转动关节；其他版本和关节模型仍须检查配置流形与实际运行时限位。

### 位置控制机器人中的 TSID 真实状态反馈不稳定

- `problem_id`：`problem.optimization_ik_qp_mpc.tsid_position_control_feedback_157`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：3（全部列出，不隐藏待验证或冲突来源）

**经验 1：位置控制机器人把真实状态直接送入 TSID 会形成双重反馈与状态不一致**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：维护者指出两个明确风险：底层关节位置控制器已经用真实关节状态闭环，再在 TSID 中反馈一次会形成双重反馈；原代码还用 q_real、v_real 求得 a_sol，却从另一套虚拟 q_tsid、v_tsid 开始积分，状态与加速度不匹配。他表示不知道这种结构的干净通用解，干净路径是关节力矩控制。若硬件只能位置控制，线程支持的边界是不要把真实关节状态按该方式直接重复闭环。
- 证据状态：`issue_candidate`
- 来源定位：Issue #157，TSID 维护者说明 issuecomment-1054461123
- 原帖/精确回复：[位置控制机器人把真实状态直接送入 TSID 会形成双重反馈与状态不一致](https://github.com/stack-of-tasks/tsid/issues/157#issuecomment-1054461123)
- 平台/作者：GitHub Issues / simon-armleder
- 关键术语：任务空间逆动力学（Task-Space Inverse Dynamics, TSID）；双重反馈（double feedback）；虚拟状态（virtual state）；力矩控制（torque control）
- 环境：TSID；Gazebo 与 PyBullet；位置控制机器人；实践者举出 iCub/Talos，提问者最终在未指明型号的真机验证。
- 症状：只积分虚拟/命令状态时可运行；用真实状态计算任务误差和 QP 后系统很快发散。；真实浮动基 ground truth 或 estimator 状态直接反馈仍导致不稳定。；换重阶段腹股沟和踝关节出现很大的跟踪误差。
- 诊断：区分 QP 使用的状态、积分起点和底层位置 PID 的反馈位置；检查 a_sol 是否对应 q_real 却从 q_tsid 积分。；确认关节反馈是否已由底层位置伺服闭环；把浮动基/接触稳定问题与关节位置闭环分开。
- 原因：真实状态同时进入 TSID 和底层位置控制器造成双重反馈。；用真实状态求得的加速度从另一套虚拟状态积分，二者不一致。
- 处理过程：维护者给出虚拟状态开环 TSID 与力矩控制边界；实践者分享模型状态 TSID 加足底 F/T/IMU stabilizer；提问者尝试真实浮动基、笛卡尔末端误差积分、接触参考和增益调整。
- 有效处理：通用且干净的线程内方案是使用关节力矩控制；位置控制机器人常用虚拟模型状态运行 TSID，并由 F/T 或 IMU 稳定器修改 CoM 等参考。；提问者的特定真机方案是不使用真实浮动基状态，按实测关节重算末端位姿来修正参考，并在 QP 后对腹股沟/踝关节加小偏置。
- 结果：提问者报告方案在仿真和真机工作；线程没有给出稳定裕度、参数范围或跨机器人复现。
- 限制：维护者明确表示不知道把真实状态直接送入位置控制 TSID 的干净通用解。；末端误差积分和关节偏置是提问者自称的 hacks，不能直接当作其他机器人通用参数。；接触参考高度、落脚反弹和 swing/contact gain 的讨论没有形成维护者确认的统一规则。
- 安全提示：实机应用偏置和参考积分前应设置幅值、速度和积分防饱和边界，并在保护条件下逐步验证；原帖没有提供这些安全边界。
- 图片分析：作者评论包含支撑脚参考/虚拟位姿曲线和两个落脚视频，并在文字中解释蓝绿曲线、参考高度与反弹现象；本卡没有从图片或视频补读数值，通用结论只采用文字确认。
- 独立核验引用：[maintainer_confirmation · 维护者解释双重反馈和 a_sol 与积分状态不一致，并说明力矩控制边界](https://github.com/stack-of-tasks/tsid/issues/157#issuecomment-1054461123)
- 适用边界：适用于 TSID 外层输出位置、机器人底层又有位置 PID 的架构；力矩控制接口的闭环结构不同。

**经验 2：位置控制机器人把真实状态直接送入 TSID 会形成双重反馈与状态不一致**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：线程中的人形机器人实践者说明，iCub、Talos 等位置控制机器人通常让 TSID 使用模型中的理论/虚拟状态开环计算，再用足底力/力矩传感器和/或 IMU 构造 stabilizer（稳定器），由稳定器修改 TSID 参考，例如调整质心 CoM 参考。他还说曾尝试只闭环浮动基、关节仍保留理论状态，但没有在评论中给出该方案的完整条件和结果，因此这部分不能写成确定解法。
- 证据状态：`issue_candidate`
- 来源定位：Issue #157，iCub/Talos 实践说明 issuecomment-1083217810
- 原帖/精确回复：[位置控制机器人把真实状态直接送入 TSID 会形成双重反馈与状态不一致](https://github.com/stack-of-tasks/tsid/issues/157#issuecomment-1083217810)
- 平台/作者：GitHub Issues / simon-armleder
- 关键术语：开环 TSID（open-loop TSID）；稳定器（stabilizer）；力/力矩传感器（force/torque sensor）；质心参考（center-of-mass reference, CoM reference）
- 环境：TSID；Gazebo 与 PyBullet；位置控制机器人；实践者举出 iCub/Talos，提问者最终在未指明型号的真机验证。
- 症状：只积分虚拟/命令状态时可运行；用真实状态计算任务误差和 QP 后系统很快发散。；真实浮动基 ground truth 或 estimator 状态直接反馈仍导致不稳定。；换重阶段腹股沟和踝关节出现很大的跟踪误差。
- 诊断：区分 QP 使用的状态、积分起点和底层位置 PID 的反馈位置；检查 a_sol 是否对应 q_real 却从 q_tsid 积分。；确认关节反馈是否已由底层位置伺服闭环；把浮动基/接触稳定问题与关节位置闭环分开。
- 原因：真实状态同时进入 TSID 和底层位置控制器造成双重反馈。；用真实状态求得的加速度从另一套虚拟状态积分，二者不一致。
- 处理过程：维护者给出虚拟状态开环 TSID 与力矩控制边界；实践者分享模型状态 TSID 加足底 F/T/IMU stabilizer；提问者尝试真实浮动基、笛卡尔末端误差积分、接触参考和增益调整。
- 有效处理：通用且干净的线程内方案是使用关节力矩控制；位置控制机器人常用虚拟模型状态运行 TSID，并由 F/T 或 IMU 稳定器修改 CoM 等参考。；提问者的特定真机方案是不使用真实浮动基状态，按实测关节重算末端位姿来修正参考，并在 QP 后对腹股沟/踝关节加小偏置。
- 结果：提问者报告方案在仿真和真机工作；线程没有给出稳定裕度、参数范围或跨机器人复现。
- 限制：维护者明确表示不知道把真实状态直接送入位置控制 TSID 的干净通用解。；末端误差积分和关节偏置是提问者自称的 hacks，不能直接当作其他机器人通用参数。；接触参考高度、落脚反弹和 swing/contact gain 的讨论没有形成维护者确认的统一规则。
- 安全提示：实机应用偏置和参考积分前应设置幅值、速度和积分防饱和边界，并在保护条件下逐步验证；原帖没有提供这些安全边界。
- 图片分析：作者评论包含支撑脚参考/虚拟位姿曲线和两个落脚视频，并在文字中解释蓝绿曲线、参考高度与反弹现象；本卡没有从图片或视频补读数值，通用结论只采用文字确认。
- 独立核验引用：[issue · 实践者基于 mc_rtc/TSID 以及 iCub/Talos 经验描述开环模型状态加传感器稳定器](https://github.com/stack-of-tasks/tsid/issues/157#issuecomment-1083217810)
- 适用边界：针对带底层位置控制、足底 F/T 或 IMU 的人形；稳定器结构、参考修正量和增益需按机器人单独设计。

**经验 3：位置控制机器人把真实状态直接送入 TSID 会形成双重反馈与状态不一致**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：作者最终没有使用真实浮动基状态。他报告两个对其真机重要的 hack：一是用实测关节状态重新做正向运动学，按末端位姿误差调整 TSID 参考；二是在 QP 计算后给腹股沟和踝关节加入小偏置，以减轻换重时的大跟踪误差。作者明确报告仿真和真机可运行，但没有给偏置数值、积分边界、稳定性指标或其他机器人复现，所以只能把它们作为有结果的特定工程记录，不能复制参数。
- 证据状态：`issue_candidate`
- 来源定位：Issue #157，作者最终真机结果 issuecomment-1103196763；前序末端参考说明 issuecomment-1083362668
- 原帖/精确回复：[位置控制机器人把真实状态直接送入 TSID 会形成双重反馈与状态不一致](https://github.com/stack-of-tasks/tsid/issues/157#issuecomment-1103196763)
- 平台/作者：GitHub Issues / simon-armleder
- 关键术语：正向运动学（forward kinematics, FK）；末端执行器（end effector）；关节偏置（joint offset）；重量转移（weight shift）
- 环境：TSID；Gazebo 与 PyBullet；位置控制机器人；实践者举出 iCub/Talos，提问者最终在未指明型号的真机验证。
- 症状：只积分虚拟/命令状态时可运行；用真实状态计算任务误差和 QP 后系统很快发散。；真实浮动基 ground truth 或 estimator 状态直接反馈仍导致不稳定。；换重阶段腹股沟和踝关节出现很大的跟踪误差。
- 诊断：区分 QP 使用的状态、积分起点和底层位置 PID 的反馈位置；检查 a_sol 是否对应 q_real 却从 q_tsid 积分。；确认关节反馈是否已由底层位置伺服闭环；把浮动基/接触稳定问题与关节位置闭环分开。
- 原因：真实状态同时进入 TSID 和底层位置控制器造成双重反馈。；用真实状态求得的加速度从另一套虚拟状态积分，二者不一致。
- 处理过程：维护者给出虚拟状态开环 TSID 与力矩控制边界；实践者分享模型状态 TSID 加足底 F/T/IMU stabilizer；提问者尝试真实浮动基、笛卡尔末端误差积分、接触参考和增益调整。
- 有效处理：通用且干净的线程内方案是使用关节力矩控制；位置控制机器人常用虚拟模型状态运行 TSID，并由 F/T 或 IMU 稳定器修改 CoM 等参考。；提问者的特定真机方案是不使用真实浮动基状态，按实测关节重算末端位姿来修正参考，并在 QP 后对腹股沟/踝关节加小偏置。
- 结果：提问者报告方案在仿真和真机工作；线程没有给出稳定裕度、参数范围或跨机器人复现。
- 限制：维护者明确表示不知道把真实状态直接送入位置控制 TSID 的干净通用解。；末端误差积分和关节偏置是提问者自称的 hacks，不能直接当作其他机器人通用参数。；接触参考高度、落脚反弹和 swing/contact gain 的讨论没有形成维护者确认的统一规则。
- 安全提示：实机应用偏置和参考积分前应设置幅值、速度和积分防饱和边界，并在保护条件下逐步验证；原帖没有提供这些安全边界。
- 图片分析：作者评论包含支撑脚参考/虚拟位姿曲线和两个落脚视频，并在文字中解释蓝绿曲线、参考高度与反弹现象；本卡没有从图片或视频补读数值，通用结论只采用文字确认。
- 独立核验引用：[issue · 作者描述按实测关节状态重算末端位姿并积分误差修正参考](https://github.com/stack-of-tasks/tsid/issues/157#issuecomment-1083362668)；[issue · 作者报告仿真和真机工作，并列出两个自称 hacks](https://github.com/stack-of-tasks/tsid/issues/157#issuecomment-1103196763)
- 适用边界：仅适用于作者所述位置控制系统的经验路径；机器人型号、关节偏置和积分增益没有公开。

### Crocoddyl FDDP 中 cost 与动态不可行度的权衡

- `problem_id`：`problem.optimization_ik_qp_mpc.crocoddyl_fddp_cost_infeasibility_tradeoff_1087`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Crocoddyl FDDP 成本上升与动态不可行度权衡**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：不足以。项目成员明确解释，FDDP 还处理动态可行性（dynamic feasibility），因此可能允许 cost 小幅上升来换取不可行度（infeasibility）下降；FDDP 的 dynamics rollout 可解释为一种 nonlinear search。工程上应同时看 cost、动态不可行度和最终收敛。原帖没有给出曲线或阈值，所以这条答复不能替持续发散、NaN 或最终不收敛背书。
- 证据状态：`issue_candidate`
- 来源定位：Crocoddyl #1087，项目成员唯一回复 issuecomment-1231303043
- 原帖/精确回复：[Crocoddyl FDDP 成本上升与动态不可行度权衡](https://github.com/loco-3d/crocoddyl/issues/1087#issuecomment-1231303043)
- 平台/作者：GitHub Issues / GitHub Issue 作者
- 关键术语：动态可行性（dynamic feasibility）；不可行度（infeasibility）；动态学展开（dynamics rollout）；非线性搜索（nonlinear search）
- 环境：Crocoddyl SolverFDDP；原帖未说明版本、机器人、代价项或约束设置。
- 症状：求解过程中个别迭代的 cost 增加。
- 诊断：不要只看 cost；同时记录动态不可行度、接受步长和最终收敛状态。；区分维护者所说的小幅 cost/infeasibility 权衡与持续发散或无界增长。
- 原因：项目成员说明 FDDP 可能以小幅 cost 增加换取 dynamic infeasibility 减少。
- 处理过程：项目成员从 FDDP 的动态可行性处理和 dynamics rollout 解释该现象。
- 有效处理：该线程给的是判读方法而非参数修复：联合检查 cost 与 infeasibility，而不是要求每一步 cost 单调下降。
- 结果：项目成员回答后关闭 Issue；原作者没有补充数值复测。
- 限制：原回复只说 cost 可以小幅增加，不能据此把持续增大、NaN 或最终不收敛判为正常。；线程没有提供可复现 OCP、版本或曲线，不能给出通用阈值。
- 安全提示：将求解器用于真机 WBC 前，应对 cost、动态不可行度、约束违反和控制量同时设置停止与回退条件。
- 独立核验引用：[maintainer_confirmation · 项目成员说明 FDDP 可用小幅 cost 增加换取 infeasibility 下降，并解释 dynamics rollout](https://github.com/loco-3d/crocoddyl/issues/1087#issuecomment-1231303043)
- 适用边界：适用于原帖所问的 Crocoddyl SolverFDDP 中间迭代判读；没有版本与 OCP 配置，不能外推具体数值阈值。

### Pinocchio 连杆任意点 Jacobian 的附加 Frame 表示

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_arbitrary_link_point_frame_jacobian_1515`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 任意连杆点 Jacobian 的附加 Frame 方法**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：项目贡献者给出的做法是先用 model.addFrame(Frame(name, joint_support_id, 0, placement)) 把该点加入模型，再走 Frame Jacobian 路径；其中 placement 是相对父关节坐标系（parent joint frame）的位姿。目标点实时变化时，回复明确可更新 model.frames\[your_frame_id\].placement。原作者没有回报数值验证，因此这是一条由项目贡献者确认、但仍需在目标模型中做有限差分校验的方法。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1515，添加 Frame issuecomment-908163738；placement 参考系 issuecomment-912373797；修改 placement issuecomment-912374322；用户未复测 issuecomment-912401354
- 原帖/精确回复：[Pinocchio 任意连杆点 Jacobian 的附加 Frame 方法](https://github.com/stack-of-tasks/pinocchio/issues/1515#issuecomment-908163738)
- 平台/作者：GitHub Issues / GitHub Issue 作者
- 关键术语：坐标帧（Frame）；帧雅可比矩阵（frame Jacobian）；父关节坐标系（parent joint frame）；位姿（placement）
- 环境：Pinocchio 模型；原帖未说明版本、具体机械臂和 Python/C++ 绑定。
- 症状：现有 getJointJacobian 与 getFrameJacobian 只覆盖已有 joint/frame，目标点位于连杆上的其他位置。
- 诊断：先确定承载目标点的 parent joint，再把目标点 placement 表达在该 parent joint frame 中。；区分目标点 placement 的实时变化与 parent joint 拓扑变化；原回复只明确了 placement 字段的修改。
- 原因：目标点没有作为模型 Frame 表示，因此不能直接调用 frame Jacobian 接口。
- 处理过程：项目贡献者建议用 model.addFrame 添加 Frame，并给出构造调用。；项目贡献者说明可修改 model.frames\[your_frame_id\].placement。
- 有效处理：为目标点增加以支撑 joint 为父节点的 Frame；placement 相对 parent joint frame 表示，再通过 frame Jacobian 路径计算。；目标点位置变化时，按回复修改对应 Frame 的 placement。
- 结果：贡献者认为该方法足以处理提问；原作者仅表示会尝试，没有提供数值对照。
- 限制：原线程没有 Jacobian 数值校验、有限差分对照或性能测量。；回复没有明确说明如何安全地改变 parent_idx，本卡不推断该操作。；2024 年旧回复所述 Pinocchio 3x 尚未发布不是当前版本状态，不能继续沿用。
- 安全提示：用于接触力或操作约束前，应以有限差分或已知刚体运动验证 Frame placement、坐标系与 Jacobian 行列顺序。
- 独立核验引用：[maintainer_confirmation · 项目贡献者给出 addFrame 调用](https://github.com/stack-of-tasks/pinocchio/issues/1515#issuecomment-908163738)；[maintainer_confirmation · 项目贡献者明确 placement 相对 parent joint frame](https://github.com/stack-of-tasks/pinocchio/issues/1515#issuecomment-912373797)；[maintainer_confirmation · 项目贡献者说明可修改 model.frames\[your_frame_id\].placement](https://github.com/stack-of-tasks/pinocchio/issues/1515#issuecomment-912374322)；[issue · 原作者只说会尝试，没有提供数值复测](https://github.com/stack-of-tasks/pinocchio/issues/1515#issuecomment-912401354)
- 适用边界：适用于原帖所述 Pinocchio 模型中的连杆任意点；版本和语言绑定未说明，使用前需核对当前 API。

### PyBullet 与 Pinocchio 末端速度的 ReferenceFrame 对齐

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_bullet_velocity_reference_frame_1759`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：PyBullet 与 Pinocchio 末端速度不一致的参考系修正**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原线程验证的是先对齐参考系（ReferenceFrame）：答复者建议将 Pinocchio 的速度/Jacobian 改为 LOCAL_WORLD_ALIGNED，原作者报告似乎工作正常，Pinocchio 项目贡献者随后认可该回答。答复还说明 WORLD 表达固定坐标系中的 spatial velocity，而 LOCAL_WORLD_ALIGNED 是将 LOCAL body Jacobian 用连杆相对世界的旋转 R 对齐到世界方向，可写成 J_lwa=\[R,0;0,R\]J_local。原图只证明修正前位置重合而速度不一致；没有修正后曲线和版本，因此不能外推到所有仿真器差异。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1759，建议 issuecomment-1263820871；原作者确认 issuecomment-1263826765；参考系解释 issuecomment-1263871379；项目贡献者认可 issuecomment-1266738973
- 原帖/精确回复：[PyBullet 与 Pinocchio 末端速度不一致的参考系修正](https://github.com/stack-of-tasks/pinocchio/issues/1759#issuecomment-1263820871)
- 平台/作者：GitHub Issues / GitHub Issue 作者
- 关键术语：参考坐标系（ReferenceFrame）；局部世界对齐（LOCAL_WORLD_ALIGNED）；空间速度（spatial velocity）；刚体雅可比矩阵（body Jacobian）
- 环境：Barrett WAM，PyBullet 仿真与 Pinocchio 对比；关节 1 和 4 设为 pi/2，机械臂无 motor 驱动并自由下落；版本未说明。
- 症状：原图中 Pinocchio 与 Bullet 的 Y 轴位置曲线基本重合。；原图中速度曲线明显分离，初段 Pinocchio 为正而 Bullet 为负；原代码使用 WORLD 或未明确匹配的 Jacobian。
- 诊断：先检查 Pinocchio Jacobian/Frame velocity 的 ReferenceFrame，再与 PyBullet 返回速度的表达坐标系对齐。；同一条速度链路中的 Jacobian、速度和 dJ 应明确使用一致参考系；原线程只验证了速度切换。
- 原因：线程回答将差异定位到 WORLD 与目标比较量的参考系不一致。
- 处理过程：社区答复者建议请求 LOCAL_WORLD_ALIGNED。；原作者按建议切换后报告似乎工作正常。
- 有效处理：对原帖这组 PyBullet 对比，使用 LOCAL_WORLD_ALIGNED 表达 Pinocchio 末端速度/Jacobian。
- 结果：原作者确认改用 LOCAL_WORLD_ALIGNED 后似乎有效。；Pinocchio 项目贡献者随后感谢答复者并认可其回答。
- 限制：线程没有修正后的图、数值误差或软件版本。；这不能证明所有 Bullet/Pinocchio 速度差异都由 ReferenceFrame 导致。；原作者询问 dJ 是否也需相同参考系，但线程没有直接给出 dJ 的明确操作答案。
- 安全提示：把任务空间速度送入 WBC 前，应以统一 ReferenceFrame 记录数值，并用有限差分位置验证速度方向和尺度。
- 图片分析：原 Issue 的双层曲线图：上方 Pos 中 Pinocchio 与 Bullet 曲线几乎完全重合；下方 Vel 中两条曲线明显分离，初段方向相反，接近末段突变后的数值也不同。这是切换 LOCAL_WORLD_ALIGNED 之前的症状图，不是修复后验证图。；原 Issue 的第二张图显示 Barrett WAM 在棋盘地面上的初始姿态，只能辅助确认机械臂构型；图中没有可读参数、日志或坐标轴定义。
- 独立核验引用：[issue · 社区答复者建议改用 LOCAL_WORLD_ALIGNED](https://github.com/stack-of-tasks/pinocchio/issues/1759#issuecomment-1263820871)；[issue · 原作者报告该建议似乎有效](https://github.com/stack-of-tasks/pinocchio/issues/1759#issuecomment-1263826765)；[issue · 答复者解释 WORLD、LOCAL 与 LOCAL_WORLD_ALIGNED 的关系](https://github.com/stack-of-tasks/pinocchio/issues/1759#issuecomment-1263871379)；[maintainer_confirmation · Pinocchio 项目贡献者认可该回答](https://github.com/stack-of-tasks/pinocchio/issues/1759#issuecomment-1266738973)
- 适用边界：严格适用于原帖 Barrett WAM、PyBullet/Pinocchio 速度比较和该 ReferenceFrame 误配；软件版本未说明。

### Pinocchio 浮动基欠驱动逆动力学的 TSID 路径

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_underactuated_inverse_dynamics_tsid_1343`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：浮动基欠驱动逆动力学从 RNEA 转向 TSID**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：在原线程中，Pinocchio 项目贡献者明确建议使用 TSID（Task Space Inverse Dynamics），说明它实现了所请求的功能、提供 Python bindings，并基于 Pinocchio；随后将 Issue 判为解决。能直接沉淀的结论只有这条项目路径：不要把 RNEA 的全广义力输出直接等同于欠驱动执行器命令。线程没有提供 TSID 的接触、任务、权重或力矩限幅配置，落地仍需按目标机器人补齐并验证。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1343，TSID 建议 issuecomment-730571974；项目贡献者关闭 issuecomment-730576108
- 原帖/精确回复：[浮动基欠驱动逆动力学从 RNEA 转向 TSID](https://github.com/stack-of-tasks/pinocchio/issues/1343#issuecomment-730571974)
- 平台/作者：GitHub Issues / GitHub Issue 作者
- 关键术语：递归牛顿-欧拉算法（Recursive Newton-Euler Algorithm, RNEA）；任务空间逆动力学（Task Space Inverse Dynamics, TSID）；浮动基（floating base）；欠驱动系统（underactuated system）
- 环境：Pinocchio rnea 与浮动基欠驱动系统；原帖未说明版本、接触模型和机器人。
- 症状：rnea 返回与系统广义速度维数对应的力向量，而实际执行器输入少于系统状态/自由度。
- 诊断：先确认需求是给定 q、v、a 的 RNEA 广义力计算，还是包含接触与任务约束的欠驱动逆动力学控制问题。
- 原因：提问把 RNEA 的广义力输出与欠驱动系统的执行器输入直接对应。
- 处理过程：项目贡献者建议转用基于 Pinocchio 的 TSID，并指出其提供 Python bindings。
- 有效处理：对于原帖所述浮动基欠驱动逆动力学需求，采用 TSID 处理，而不是把 RNEA 输出直接当作执行器命令。
- 结果：项目贡献者将问题标记为已解决；原作者没有报告实际配置或运行结果。
- 限制：线程没有给出 TSID 任务、接触、约束或权重配置。；不能从这两条回复推断 Pinocchio 所有约束动力学能力，也不能把 TSID 写成无需建模即可工作的通用修复。
- 安全提示：真机使用前需单独验证执行器选择矩阵、接触约束、力矩限幅和浮动基动力学残差。
- 独立核验引用：[maintainer_confirmation · Pinocchio 项目贡献者明确建议使用 TSID 并说明其功能与 Python bindings](https://github.com/stack-of-tasks/pinocchio/issues/1343#issuecomment-730571974)；[maintainer_confirmation · 项目贡献者随后将问题判为已解决](https://github.com/stack-of-tasks/pinocchio/issues/1343#issuecomment-730576108)
- 适用边界：适用于原帖所述输入少于系统状态/自由度的浮动基腿式逆动力学需求；具体 TSID 配置未提供。

### Pinocchio 修改 Model 后复用旧 Data 引发内存崩溃

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_recreate_data_after_model_mutation_2026`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 修改 Model 后继续复用旧 Data 导致随机崩溃**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原代码先执行 model.createData()，然后 model.addFrame(frame)，再用旧 data 计算 Jacobian。项目成员指出 Data 创建后不应再修改 Model；原作者确认这就是自己的顺序。处理方式是先完成 addFrame 等模型修改，再创建 Data；后续再改 Model 时也应重建 Data。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #2026，项目成员诊断 issuecomment-1664403489，作者确认 issuecomment-1664425533
- 原帖/精确回复：[Pinocchio 修改 Model 后继续复用旧 Data 导致随机崩溃](https://github.com/stack-of-tasks/pinocchio/issues/2026#issuecomment-1664425533)
- 平台/作者：GitHub Issues / 未显示
- 关键术语：模型数据生命周期（Model/Data lifecycle）；操作帧（operational frame）；帧雅可比（frame Jacobian）；段错误（segmentation fault）
- 环境：Pinocchio 2.6.19（pip）；Python 3.10.4；UR5 URDF；x86_64 Linux，Intel i7-8550U。
- 症状：同一脚本不稳定地出现 Segmentation fault、Bus error、corrupted double-linked list 或 double free or corruption。
- 诊断：按执行顺序检查 model.createData() 与 model.addFrame()：原示例在 Data 已创建后又改变了 Model 的 frame 结构。
- 原因：项目成员定位为先创建 Pinocchio Data，后修改 Pinocchio Model；原作者确认这一顺序确实存在。
- 处理过程：项目成员建议把 model.createData() 移到 model.addFrame(frame) 之后；另一位贡献者同意这一诊断，原作者确认顺序错误。
- 有效处理：先完成 addFrame 等所有 Model 结构修改，再调用 model.createData()；如果 Model 之后又被修改，在运行 Jacobian/运动学算法前重新创建对应 Data。
- 结果：原作者回复确认自己在初始化 Data 之后才添加 frames，并接受修正。Issue 随后以 completed 关闭。
- 限制：原线程没有给出调整后的完整运行输出或回归测试。；现象与版本边界来自 Pinocchio 2.6.19；不应推断其他版本一定以同样的崩溃形式表现。
- 安全提示：对实机 WBC，动力学数据结构不一致时应阻止下发力矩，不能仅依赖进程崩溃作为保护。
- 独立核验引用：[maintainer_confirmation · 项目成员指出先创建 Data 后修改 Model 的顺序问题，建议在修改 Model 后创建 Data](https://github.com/stack-of-tasks/pinocchio/issues/2026#issuecomment-1664403489)；[issue · 原作者确认自己确实在 Data 初始化之后才添加 frames](https://github.com/stack-of-tasks/pinocchio/issues/2026#issuecomment-1664425533)
- 适用边界：适用于原帖 Pinocchio 2.6.19/Python 3.10.4 及类似的运行期 Model 结构修改流程；其他版本需重新核对 API 语义。

### Isaac Lab 浮动基 OSC 动力学索引错位导致异常力矩

- `problem_id`：`problem.optimization_ik_qp_mpc.isaaclab_floating_base_osc_index_offset_4999`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 浮动基 OSC 读取错位动力学索引导致力矩爆炸**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：作者发现 Jacobian 路径已使用对浮动基加 6 偏移的 self._jacobi_joint_idx，但 _compute_dynamic_quantities() 仍用未偏移的 self._joint_ids 截取广义质量矩阵与重力项。他在原帖 commit f4aa17f 上将两者统一改为 self._jacobi_joint_idx，报告 R1 Pro 不再抖动，力矩回到约 -16至4 N·m 量级，惯性解耦和重力补偿也能运行。这仅是原作者的本地验证；项目未确认、无关联 PR，其他版本必须先核对索引语义。
- 证据状态：`issue_candidate`
- 来源定位：Isaac Lab #4999 正文中的修正前/后力矩、索引对照和本地结果；项目评论 issuecomment-4081678102 仅说待审查
- 原帖/精确回复：[Isaac Lab 浮动基 OSC 读取错位动力学索引导致力矩爆炸](https://github.com/isaac-sim/IsaacLab/issues/4999)
- 平台/作者：GitHub Issues / Vitamin0304
- 关键术语：操作空间控制（Operational Space Control, OSC）；浮动基（floating base）；广义质量矩阵（generalized mass matrix）；重力补偿（gravity compensation）；惯性动力学解耦（inertial dynamics decoupling）
- 环境：Isaac Lab commit f4aa17f87e2e5db5484f0b5974918573e8918ce2；Isaac Sim 5.10；Ubuntu 22.04；RTX 3090；CUDA 12.8；driver 570.211；Galaxea R1 Pro 左臂。
- 症状：机器人剧烈抖动；作者列出的实际力矩多次到达±600–1500 N·m，而修正后序列约为 -15.9至3.76 N·m。
- 诊断：对照 __init__ 中用于 Jacobian 的 self._jacobi_joint_idx 与 _compute_dynamic_quantities() 中用于 generalized mass matrix/gravity 的 self._joint_ids。；对浮动基模型检查关节索引是否需跨过前 6 个基座广义速度维度，并同时比较修正前后控制力矩。
- 原因：作者定位为 _compute_dynamic_quantities() 用未偏移的 self._joint_ids 截取质量矩阵和重力向量，从而把底盘/轮组等动力学项错配给机械臂关节。
- 处理过程：作者在本地将 mass matrix 和 gravity 的行列索引从 self._joint_ids 替换为 self._jacobi_joint_idx。
- 有效处理：对原帖提交 f4aa17f 的本地实验，在 _compute_dynamic_quantities() 中以 self._jacobi_joint_idx 同时索引 generalized mass matrices 的两个维度和 gravity compensation forces。
- 结果：作者报告本地修改后 R1 Pro 恢复稳定控制，力矩不再爆炸，并且 inertial_dynamics_decoupling=True 与 gravity_compensation=True 可用。
- 限制：该结论是 Issue 作者的单一机器人本地修改记录；项目回复只说团队会审查，没有确认根因或修复。；Issue 页明确显示没有关联 branch/PR；关闭状态不能替代合并补丁或回归测试。；原帖没有独立复现、自动化测试、真机结果或官方发布版本；其他浮动基 articulation 必须核对自身索引布局。
- 安全提示：原帖异常力矩达数百至约 1500 N·m；在真机转移前必须以软件力矩夹紧、驱动器限流、低增益和急停独立阻断这类索引错位。
- 独立核验引用：[issue · 原帖给出 commit/环境、修正前后力矩、完整索引修改以及作者本地结果](https://github.com/isaac-sim/IsaacLab/issues/4999)；[issue · 项目协作者只表示团队会审查；该回复不是对根因或修复的确认](https://github.com/isaac-sim/IsaacLab/issues/4999#issuecomment-4081678102)
- 适用边界：仅直接适用于原帖 Isaac Lab commit f4aa17f/Isaac Sim 5.10 的 Galaxea R1 Pro 浮动基 OSC 实验；其他机器人和版本需验证广义索引布局。

### TSID 逆动力学 QP 中前六个硬等式的含义

- `problem_id`：`problem.optimization_ik_qp_mpc.tsid_floating_base_six_equalities_138`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：TSID 的 m_eq 六行浮动基动力学与软接触计数缺陷**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：不是。项目协作者明确说明，这 6 行用于 enforce floating-base dynamics，而不是 base position。剩余 joint dynamics 不以同样方式加入，是因为该 formulation 没有把 joint torques 作为优化变量。这个解释依赖当前决策变量设计，不能外推为所有 WBC QP 的固定模板。
- 证据状态：`issue_candidate`
- 来源定位：Issue #138，项目协作者解释 issuecomment-887863758
- 原帖/精确回复：[TSID 的 m_eq 六行浮动基动力学与软接触计数缺陷](https://github.com/stack-of-tasks/tsid/issues/138#issuecomment-887863758)
- 平台/作者：GitHub Issues / jacqueszhong
- 关键术语：浮动基动力学（floating-base dynamics）；硬等式约束（hard equality constraint）；关节力矩（joint torque）；决策变量（decision variable）
- 环境：2021 年 TSID devel；Issue 引用 commit 0969328 的 inverse-dynamics-formulation-acc-force.cpp；修复 commit 为 5a6b452。
- 症状：用户误以为前 6 个等式约束是在 enforce base position。；soft-priority Contact6D motion task 没有进入 hard equality level，却仍被计入 m_eq。
- 诊断：区分 floating-base dynamics rows 与 base pose task。；比较 motionPriorityLevel 与 addRigidContact 内 m_eq 计数条件。
- 原因：前 6 行是未驱动浮动基动力学；joint torque 不作为决策变量，所以不需要把剩余 joint dynamics 加成同类约束。；旧代码无条件累加 motionConstr.rows()，没有检查 motionPriorityLevel。
- 处理过程：项目协作者复核代码后确认第二点是 bug，并提交修复。
- 有效处理：commit 5a6b452 仅在 motionPriorityLevel==0 时执行 m_eq += motionConstr.rows()。
- 结果：维护者确认 bug 已在 devel 修复；官方提交的 patch 与 Issue 描述完全对应。
- 限制：线程没有给发布版本号，也没有展示触发 bug 的数值控制结果。；前 6 行解释适用于该 inverse-dynamics formulation 的变量选择，不等于所有 WBC QP 都应固定使用 6 行。
- 独立核验引用：[maintainer_confirmation · 项目协作者区分 floating-base dynamics 与 base position，并说明 joint torque 不作为变量](https://github.com/stack-of-tasks/tsid/issues/138#issuecomment-887863758)
- 适用边界：适用于原帖 2021 年 TSID InverseDynamicsFormulationAccForce 及其不显式优化 joint torque 的变量设计。

### TSID 把软接触运动任务错误计入硬等式数量

- `problem_id`：`problem.optimization_ik_qp_mpc.tsid_soft_contact_meq_bug_138`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：TSID 的 m_eq 六行浮动基动力学与软接触计数缺陷**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：这是已确认的代码缺陷。项目协作者先表示软化为 penalty 后不应增加 equality count，随后确认已在 devel 修复。官方 commit 5a6b452 的实际补丁把无条件 m_eq += motionConstr.rows() 改为只有 motionPriorityLevel==0 时才增加，因此软优先级 contact motion task 不再被计入硬等式数量。线程没有给出包含该提交的正式 release 版本。
- 证据状态：`issue_candidate`
- 来源定位：Issue #138，维护者确认 issuecomment-890048340；官方修复 commit 5a6b452
- 原帖/精确回复：[TSID 的 m_eq 六行浮动基动力学与软接触计数缺陷](https://github.com/stack-of-tasks/tsid/issues/138#issuecomment-890048340)
- 平台/作者：GitHub Issues / jacqueszhong
- 关键术语：软接触运动任务（soft contact motion task）；惩罚项（penalty term）；约束数量（constraint count）；运动优先级（motion priority level）
- 环境：2021 年 TSID devel；Issue 引用 commit 0969328 的 inverse-dynamics-formulation-acc-force.cpp；修复 commit 为 5a6b452。
- 症状：用户误以为前 6 个等式约束是在 enforce base position。；soft-priority Contact6D motion task 没有进入 hard equality level，却仍被计入 m_eq。
- 诊断：区分 floating-base dynamics rows 与 base pose task。；比较 motionPriorityLevel 与 addRigidContact 内 m_eq 计数条件。
- 原因：前 6 行是未驱动浮动基动力学；joint torque 不作为决策变量，所以不需要把剩余 joint dynamics 加成同类约束。；旧代码无条件累加 motionConstr.rows()，没有检查 motionPriorityLevel。
- 处理过程：项目协作者复核代码后确认第二点是 bug，并提交修复。
- 有效处理：commit 5a6b452 仅在 motionPriorityLevel==0 时执行 m_eq += motionConstr.rows()。
- 结果：维护者确认 bug 已在 devel 修复；官方提交的 patch 与 Issue 描述完全对应。
- 限制：线程没有给发布版本号，也没有展示触发 bug 的数值控制结果。；前 6 行解释适用于该 inverse-dynamics formulation 的变量选择，不等于所有 WBC QP 都应固定使用 6 行。
- 独立核验引用：[maintainer_confirmation · 项目协作者确认第二点是 bug 且已在 devel 修复](https://github.com/stack-of-tasks/tsid/issues/138#issuecomment-890048340)；[source_code · 官方提交把 m_eq 累加置于 motionPriorityLevel==0 条件内](https://github.com/stack-of-tasks/tsid/commit/5a6b452861247b44593cf6041b014edd72c059f8)
- 适用边界：适用于 commit 5a6b452 之前的 TSID InverseDynamicsFormulationAccForce::addRigidContact 计数逻辑；具体 release 需按提交包含关系核对。

## 力控、接触操作与载荷 (`force_control_manipulation`)

### 怎样避免只看厂商‘100 Hz 带宽’就误判力控关节？

- `problem_id`：`problem.force_control_manipulation.556c947d2366852b`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：力控关节验收：带宽、精度、反驱与热漂移四类测试**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：必须记录测试负载惯量、力矩幅值、温度和采样率：用阶跃测上升时间/超调，用扫频取 -3 dB 带宽，再做多力矩点精度、正反向重复、反驱与长时温漂。该帖给的是验收框架而非合格阈值。
- 证据状态：`community_candidate`
- 来源定位：正文四项‘期末考’
- 原帖/精确回复：[力控关节验收：带宽、精度、反驱与热漂移四类测试](https://zhuanlan.zhihu.com/p/2061931048615801633)
- 平台/作者：Zhihu / 秦素兵 力控模组
- 关键术语：全身控制（Whole-Body Control, WBC）；比例-微分控制（Proportional-Derivative Control, PD Control）；关节力矩（Joint Torque）；有效载荷（Payload）；反向驱动性（Backdrivability）；热漂移（Thermal Drift）
- 环境：高采样率外部力矩传感器；空载/带载；堵转；1–100 Hz 以上扫频。
- 症状：样本标称力矩精度/带宽缺少负载、幅值和温度条件，实机表现不可比。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：空载小幅测试掩盖带载带宽下降、滞回、温漂与减速器阻力。
- 处理过程：阶跃与扫频、10/50/100% 额定扭矩静态精度、正反向重复、锯齿分辨率、断电/零力矩反驱、长时热漂移。
- 结果：形成验收框架，但帖子没有给出实测数据。
- 限制：非行业标准；阈值需按平台、安全等级和传感器精度定义。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：单个媒体位未提供可读取的阶跃或 Bode 曲线；验收框架来自正文，带宽/精度没有图上实测数字。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_expand_controls
- 适用边界：非行业标准；阈值需按平台、安全等级和传感器精度定义。

### 重力补偿后机械臂不掉，但拖动很涩，为什么不能直接把 KD 调大？

- `problem_id`：`problem.force_control_manipulation.80f2aae5e1c51edb`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：重力补偿能托住但拖动很涩：KD、MIT 模式与结构负载讨论**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：高 KD 会把关节速度直接变成阻尼力矩，能压住振动却破坏反驱手感。先核对重力模型和摩擦，再在限幅/安全保护下逐轴降低 kd、记录 tau/速度/电流；结构负载过大也应单独处理。该帖没有给最终参数。
- 证据状态：`community_candidate`
- 来源定位：根帖 J2 kd=0.8 与 MIT 参数评论
- 原帖/精确回复：[重力补偿能托住但拖动很涩：KD、MIT 模式与结构负载讨论](https://www.xiaohongshu.com/explore/69e33c59000000002102cdd0)
- 平台/作者：Xiaohongshu / 特仑输
- 关键术语：比例-微分控制（Proportional-Derivative Control, PD Control）；执行器（Actuator）；关节力矩（Joint Torque）；质心（Center of Mass, CoM）；有效载荷（Payload）；重力补偿（Gravity Compensation）
- 环境：6 轴机械臂；MIT 控制；J2 kd=0.8，其余约 0.1/0。
- 症状：机械臂能稳住，但 J2/J3 阻尼感强，向下拖动不丝滑。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：J2 kd 过大直接增加速度阻尼；近端关节负载与模型补偿误差也可能迫使用户用高 kd 压振。
- 处理过程：作者使用 kp=0、较小 kd、tau 重力补偿；评论讨论把 J4 靠近 J3 以减轻负载。
- 结果：没有调参后的复测，也没有电流/摩擦数据。
- 限制：非全尺寸人形；‘前几步角度’表述含混。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：候选未发现可见媒体；J2 kd=0.8、其余 0.1/0 与 MIT 参数来自正文/评论文本。
- 采集完整性：`partial_visible`；可见回复 29；展开 4 次；回复深度 2/10；停止原因：all_visible_comments_loaded
- 适用边界：非全尺寸人形；‘前几步角度’表述含混。

### whole-body manipulation 中，为什么静态 IK 可解还不够？

- `problem_id`：`problem.force_control_manipulation.35ce923ac0cea053`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：用 200 万轨迹/姿态构建任务条件动态可达图**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：静态 IK 只说明某一姿态可能存在关节解，未必满足任务条件和动态到达过程。该帖通过每臂 200 万轨迹/姿态构建 dynamic reachability map，并与 IK solver 核对；但没有实机结果，因此只是候选方法。
- 证据状态：`community_candidate`
- 来源定位：根帖正文
- 原帖/精确回复：[用 200 万轨迹/姿态构建任务条件动态可达图](https://x.com/stash_pomichter/status/2074911470471856133)
- 平台/作者：X / stash @stash_pomichter
- 关键术语：逆运动学（Inverse Kinematics, IK）；关节力矩（Joint Torque）；求解器（Solver）
- 环境：人形双臂操作框架；每臂 200 万轨迹/姿态采样。
- 症状：原帖未给出失败案例。
- 诊断：用 IK solver 核对采样可达图。
- 原因：只看静态 IK 无法覆盖任务条件与动态到达性。
- 处理过程：按任务条件构建动态可达图。
- 有效处理：在规划前用可达图过滤候选目标是帖子暗示的方案。
- 结果：完成开源实现，但无实机成功率。
- 限制：缺少采样范围、IK 误差、动态约束和硬件结果。
- 安全提示：可达图不能替代碰撞、力矩、速度和自碰检查。
- 图片分析：截图的视频帧包含场景点云和人形模型，可见彩色可达区域；没有图例、误差阈值或碰撞信息。
- 采集完整性：`partial_visible`；可见回复 6；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于双臂/全身操作目标筛选。

### MuJoCo 站点力传感器漏掉 tendon force

- `problem_id`：`problem.force_control_manipulation.mujoco_site_sensor_omits_tendon_force_832`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo 肌腱力测量的站点传感器缺口、力分解与焊接转接方案**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突。
- 解答状态：`unresolved`
- 候选解答：不是。项目协作者检查后说，site force sensor 的引擎路径处理运动树产生的力和 constraint forces，但跳过了 tendon force，并认为这很可能是 bug。因此零读数只能说该 sensor 路径没有给出 tendon force，不能证明 tendon 无张力；该直接传感器缺口在原 Issue 中仍未闭环。
- 证据状态：`issue_candidate`
- 来源定位：Issue #832，项目协作者诊断 issuecomment-1520720813；后续仍未修复 issuecomment-1794890260
- 原帖/精确回复：[MuJoCo 肌腱力测量的站点传感器缺口、力分解与焊接转接方案](https://github.com/google-deepmind/mujoco/issues/832#issuecomment-1520720813)
- 平台/作者：GitHub Issues / GitHub Issue 作者
- 关键术语：站点力传感器（site force sensor）；肌腱力（tendon force）；约束力（constraint force）；运动树（kinematic tree）
- 环境：MuJoCo 公开 Issue #832，2023–2025 年回复；被动 tendon、tendon limit constraint 和 site/weld force sensor。；官方源码定位到 commit 100b1a06fd8f6a184a3e495adff3ff044b1ff4f2 的 engine_passive.c 377–415 行。
- 症状：tendon 上有力时，附着点的 force sensor 仍读到零。；welded mounting-body workaround 在部分模型中产生转接体伸长和力值偏差。
- 诊断：先区分被动弹簧/阻尼力与 tendon limit 约束力，不把一个零值 site sensor 当成两者的总和。；对照 engine_passive.c 的 tendon spring/damper 计算，并对照 XML reference 中 tendonlimitfrc 的约束力定义。；若使用 welded mounting body，同时检查转接体质量、焊缝软性和 tendon 伸长。
- 原因：项目协作者确认 site force sensor 的当时实现漏掉 tendon force，并将其称为缺口/缺陷。；weld workaround 的误差与额外 mounting body 的质量和软 weld constraint 有关，但原线程未给出通用误差模型。
- 处理过程：用一个自由 mounting body 作为 tendon 附着点，将其焊接到目标体并测量 weld force。；有用户将 weld solref 调到 0.0002 1，报告伸长只是部分改善。；按维护者最后的建议分别计算 passive force 和读取 tendonlimitfrc。
- 有效处理：对 passive force，按官方引擎源码的 tendon spring/damper 定义计算；对 constraint force，使用 sensor/tendonlimitfrc；需总力时将两部分相加。
- 结果：原线程用户确认被动弹簧力计算对其模型有效。；site sensor 直接漏读 tendon force 的引擎缺口在该 Issue 中仍未标记为修复。；welded mounting-body workaround 的结果在不同用户间有冲突。
- 限制：引擎源码中的 frc_spring 是局部计算变量，不应被改写成稳定公开 API 名称。；tendonlimitfrc 只表示 tendon limit 约束力，不自动包含被动弹簧与阻尼力。；焊接转接体方案未获得维护者验证，且有已知软性与质量偏差。
- 安全提示：将仿真 tendon force 用于真机限力或保护前，应用已知负载独立校准被动力、约束力与传感器符号。
- 独立核验引用：[maintainer_confirmation · 项目协作者说明 site sensor 路径漏掉 tendon force 并将其判断为可能的 bug](https://github.com/google-deepmind/mujoco/issues/832#issuecomment-1520720813)；[issue · 2023 年后续回复说明缺口尚未修复且文档已提及](https://github.com/google-deepmind/mujoco/issues/832#issuecomment-1794890260)
- 适用边界：适用于原 Issue 讨论的 MuJoCo site force sensor 与 tendon 附着点；新版本使用前仍需检查当前实现和回归测试。

### MuJoCo 被动 tendon force 与限位约束力的合成

- `problem_id`：`problem.force_control_manipulation.mujoco_tendon_total_force_decomposition_832`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo 肌腱力测量的站点传感器缺口、力分解与焊接转接方案**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：维护者最后将两部分分开：被动部分按 tendon 长度超出 spring-length interval 后的刚度项，再加上与 tendon velocity 相关的阻尼项；限位约束力用 sensor/tendonlimitfrc 读取；需要 total force 时再将两部分相加。官方 engine_passive.c 给出 spring/damper 实现，XML reference 明确 tendonlimitfrc 是 tendon limit constraint force sensor，原线程用户确认被动弹簧力路径对其模型有效。源码局部变量 frc_spring 不应被当作对外 API。
- 证据状态：`issue_candidate`
- 来源定位：Issue #832，维护者分解方法 issuecomment-3148619744；用户确认 issuecomment-3152635424；官方源码 377–415 行与 XML tendonlimitfrc 文档
- 原帖/精确回复：[MuJoCo 肌腱力测量的站点传感器缺口、力分解与焊接转接方案](https://github.com/google-deepmind/mujoco/issues/832#issuecomment-3148619744)
- 平台/作者：GitHub Issues / GitHub Issue 作者
- 关键术语：被动肌腱力（passive tendon force）；肌腱限位约束力（tendon limit constraint force）；刚度（stiffness）；阻尼（damping）
- 环境：MuJoCo 公开 Issue #832，2023–2025 年回复；被动 tendon、tendon limit constraint 和 site/weld force sensor。；官方源码定位到 commit 100b1a06fd8f6a184a3e495adff3ff044b1ff4f2 的 engine_passive.c 377–415 行。
- 症状：tendon 上有力时，附着点的 force sensor 仍读到零。；welded mounting-body workaround 在部分模型中产生转接体伸长和力值偏差。
- 诊断：先区分被动弹簧/阻尼力与 tendon limit 约束力，不把一个零值 site sensor 当成两者的总和。；对照 engine_passive.c 的 tendon spring/damper 计算，并对照 XML reference 中 tendonlimitfrc 的约束力定义。；若使用 welded mounting body，同时检查转接体质量、焊缝软性和 tendon 伸长。
- 原因：项目协作者确认 site force sensor 的当时实现漏掉 tendon force，并将其称为缺口/缺陷。；weld workaround 的误差与额外 mounting body 的质量和软 weld constraint 有关，但原线程未给出通用误差模型。
- 处理过程：用一个自由 mounting body 作为 tendon 附着点，将其焊接到目标体并测量 weld force。；有用户将 weld solref 调到 0.0002 1，报告伸长只是部分改善。；按维护者最后的建议分别计算 passive force 和读取 tendonlimitfrc。
- 有效处理：对 passive force，按官方引擎源码的 tendon spring/damper 定义计算；对 constraint force，使用 sensor/tendonlimitfrc；需总力时将两部分相加。
- 结果：原线程用户确认被动弹簧力计算对其模型有效。；site sensor 直接漏读 tendon force 的引擎缺口在该 Issue 中仍未标记为修复。；welded mounting-body workaround 的结果在不同用户间有冲突。
- 限制：引擎源码中的 frc_spring 是局部计算变量，不应被改写成稳定公开 API 名称。；tendonlimitfrc 只表示 tendon limit 约束力，不自动包含被动弹簧与阻尼力。；焊接转接体方案未获得维护者验证，且有已知软性与质量偏差。
- 安全提示：将仿真 tendon force 用于真机限力或保护前，应用已知负载独立校准被动力、约束力与传感器符号。
- 独立核验引用：[maintainer_confirmation · 维护者区分 passive force、constraint force 并说明 total force 由两者相加](https://github.com/google-deepmind/mujoco/issues/832#issuecomment-3148619744)；[source_code · 官方源码给出 tendon spring 长度区间、刚度项、阻尼项及 Jacobian 映射](https://github.com/google-deepmind/mujoco/blob/100b1a06fd8f6a184a3e495adff3ff044b1ff4f2/src/engine/engine_passive.c#L377-L415)；[official_documentation · 官方 XML reference 将 tendonlimitfrc 定义为 tendon limit constraint force sensor](https://mujoco.readthedocs.io/en/latest/XMLreference.html#sensor-tendonlimitfrc)；[issue · 原线程用户确认被动弹簧力计算对其模型有效](https://github.com/google-deepmind/mujoco/issues/832#issuecomment-3152635424)
- 适用边界：适用于同时包含被动 tendon spring/damper 与 tendon limit constraint 的 MuJoCo 模型；只有其中一项时应只保留对应力分量。

### 焊接转接体测量 tendon force 的误差与冲突

- `problem_id`：`problem.force_control_manipulation.mujoco_weld_mount_tendon_workaround_conflict_832`
- 问题综合等级：**需要实际验证** — 不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo 肌腱力测量的站点传感器缺口、力分解与焊接转接方案**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突。
- 解答状态：`conflicting`
- 候选解答：原线程不支持把它当成通用方案。早期用户说该 workaround 看起来可用，但也说额外 mounting bodies 的质量会导致读数偏差；后来另一用户报告软 weld constraint 使 tendon 经过 mounting body 时产生伸长，solref="0.0002 1" 也只能部分改善。线程没有维护者验收或统一误差界，因此必须在目标模型中与已知 tendon force 独立对比。
- 证据状态：`issue_candidate`
- 来源定位：Issue #832，workaround issuecomment-1816986241；伸长反例 issuecomment-2500739225；solref 部分改善 issuecomment-2500866159
- 原帖/精确回复：[MuJoCo 肌腱力测量的站点传感器缺口、力分解与焊接转接方案](https://github.com/google-deepmind/mujoco/issues/832#issuecomment-1816986241)
- 平台/作者：GitHub Issues / GitHub Issue 作者
- 关键术语：焊接约束（weld constraint）；转接体（mounting body）；约束软性（constraint softness）；求解参考（solver reference, solref）
- 环境：MuJoCo 公开 Issue #832，2023–2025 年回复；被动 tendon、tendon limit constraint 和 site/weld force sensor。；官方源码定位到 commit 100b1a06fd8f6a184a3e495adff3ff044b1ff4f2 的 engine_passive.c 377–415 行。
- 症状：tendon 上有力时，附着点的 force sensor 仍读到零。；welded mounting-body workaround 在部分模型中产生转接体伸长和力值偏差。
- 诊断：先区分被动弹簧/阻尼力与 tendon limit 约束力，不把一个零值 site sensor 当成两者的总和。；对照 engine_passive.c 的 tendon spring/damper 计算，并对照 XML reference 中 tendonlimitfrc 的约束力定义。；若使用 welded mounting body，同时检查转接体质量、焊缝软性和 tendon 伸长。
- 原因：项目协作者确认 site force sensor 的当时实现漏掉 tendon force，并将其称为缺口/缺陷。；weld workaround 的误差与额外 mounting body 的质量和软 weld constraint 有关，但原线程未给出通用误差模型。
- 处理过程：用一个自由 mounting body 作为 tendon 附着点，将其焊接到目标体并测量 weld force。；有用户将 weld solref 调到 0.0002 1，报告伸长只是部分改善。；按维护者最后的建议分别计算 passive force 和读取 tendonlimitfrc。
- 有效处理：对 passive force，按官方引擎源码的 tendon spring/damper 定义计算；对 constraint force，使用 sensor/tendonlimitfrc；需总力时将两部分相加。
- 结果：原线程用户确认被动弹簧力计算对其模型有效。；site sensor 直接漏读 tendon force 的引擎缺口在该 Issue 中仍未标记为修复。；welded mounting-body workaround 的结果在不同用户间有冲突。
- 限制：引擎源码中的 frc_spring 是局部计算变量，不应被改写成稳定公开 API 名称。；tendonlimitfrc 只表示 tendon limit 约束力，不自动包含被动弹簧与阻尼力。；焊接转接体方案未获得维护者验证，且有已知软性与质量偏差。
- 安全提示：将仿真 tendon force 用于真机限力或保护前，应用已知负载独立校准被动力、约束力与传感器符号。
- 独立核验引用：[issue · 用户提供 welded mounting-body workaround 并报告额外质量导致偏差](https://github.com/google-deepmind/mujoco/issues/832#issuecomment-1816986241)；[conflict · 另一用户报告软 weld constraint 导致伸长](https://github.com/google-deepmind/mujoco/issues/832#issuecomment-2500739225)；[conflict · 调紧 solref 只能部分改善](https://github.com/google-deepmind/mujoco/issues/832#issuecomment-2500866159)
- 适用边界：仅作为 MuJoCo 模型中的试验性 workaround；必须核对 mounting-body 质量、weld solref、伸长与相位误差。

## 电机、减速器、温升与磨损 (`hardware_actuator_thermal`)

### G1 双臂前举后手臂过热下线并带倒右腿，优先怎样止损和定位？

- `problem_id`：`problem.hardware_actuator_thermal.256da6e8fc9421c3`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：G1 双臂前举 1–2 分钟过热下线并连锁倒地**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：先把跌落风险隔离：保护绳/支架、人员退场，并实时记录每个电机温度、力矩、电流和 fault 时间线，在第一个热告警前主动降级/停机。再对比左右肩、手臂姿态和环境散热；评论给出的 85/90°C 只能作为待官方核验线索。
- 证据状态：`community_candidate`
- 来源定位：根帖复现描述与温度/停机/返厂评论
- 原帖/精确回复：[G1 双臂前举 1–2 分钟过热下线并连锁倒地](https://www.xiaohongshu.com/explore/6a5108b9000000000602095c)
- 平台/作者：Xiaohongshu / 叽叽喳喳
- 关键术语：执行器（Actuator）；关节力矩（Joint Torque）；全身遥操作（Whole-Body Teleoperation）；热漂移（Thermal Drift）
- 环境：Sonic 全身遥操作；双臂前举持续保持；室内。
- 症状：1–2 分钟右臂过热下线，随后右腿下线，机器人颠簸倒地。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：评论怀疑肩关节持续力矩与散热不足；也有人建议返厂排查关节 gap，未定因。
- 处理过程：社区建议用 App/电机状态监温、设报警后关闭程序并吊挂降温、缩短持续抬臂、外部风冷或返厂。
- 结果：没有作者修复后的结果；多位评论者称遇到类似过热。
- 限制：85/90°C 阈值未由官方资料独立核验；不能用风扇替代故障诊断。
- 安全提示：必须先防跌落：吊挂/保护绳、人员隔离、温度预警和故障级联停机。
- 图片分析：三个媒体位展示 G1 遥操作/姿态，不包含可读取的温度时间序列；1–2 分钟、85/90°C 线索来自正文和评论，仍需官方/遥测核验。
- 采集完整性：`partial_visible`；可见回复 12；展开 0 次；回复深度 1/10；停止原因：all_visible_comments_loaded
- 适用边界：85/90°C 阈值未由官方资料独立核验；不能用风扇替代故障诊断。

### 38°C 户外跑动视频能否证明 QDD 热管理安全？

- `problem_id`：`problem.hardware_actuator_thermal.b2ea2ebfc9009db1`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：38°C 户外人形运动测试暴露的 QDD 热管理缺口**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：不能。帖子只显示 AI Sapiens 完成户外运动，回复也在追问 QDD 如何应对高温；缺少温度、电流、持续时间和降额数据，因此热安全仍 unresolved。
- 证据状态：`community_candidate`
- 来源定位：根帖与 @stevencheng 的热管理追问
- 原帖/精确回复：[38°C 户外人形运动测试暴露的 QDD 热管理缺口](https://x.com/stevencheng/status/2086147943976087792)
- 平台/作者：X / Humanoids daily @humanoidsdaily
- 关键术语：准直接驱动（Quasi-Direct Drive, QDD）；应用程序接口（Application Programming Interface, API）；执行器（Actuator）；关节力矩（Joint Torque）；热漂移（Thermal Drift）
- 环境：38°C 首尔户外；1.3 m、34 kg、23 DoF 人形。
- 症状：原帖未报告过热，只展示压力测试。
- 诊断：应记录绕组/驱动器温度、电流、扭矩、持续时间和降额事件；原帖缺失。
- 原因：高环境温度减少散热余量。
- 处理过程：进行户外运动演示。
- 结果：可见演示完成，但热性能没有量化。
- 限制：无法从成功视频推断连续工作热安全。
- 安全提示：高温测试应设置温度/电流保护和自动降额，不能只观察是否跌倒。
- 图片分析：截图主要是平台规格和 38°C 描述，没有温度曲线、热像或执行器日志。
- 采集完整性：`partial_visible`；可见回复 5；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于 QDD 人形机器人的高温连续运行验收。

### Pinocchio 中 armature/reflected inertia 的动力学处理边界

- `problem_id`：`problem.hardware_actuator_thermal.pinocchio_armature_dynamics_671`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：3（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio armature 处理要区分质量矩阵对角近似、快速 ABA 与完整电机传动模型**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：维护者接受把正值 armature 加到 M 的对角作为临时工程方案，并要求检查 armature 为正；但这只覆盖较大的 reflected inertia 影响，不包含电机自转和支撑关节运动带来的 Coriolis/centrifugal effects。线程还指出，若电机与关节不是强刚性连接，例如 Series Elastic Actuator，就不能把电机惯量强制嵌入同一个关节质量矩阵。使用前必须确认 model.armature 是否已经包含 gear ratio 折算，不能把 rotor inertia 再重复折算。
- 证据状态：`issue_candidate`
- 来源定位：Issue #671，临时方案 issuecomment-463259454；建模限制 issuecomment-463552141/553836338；gear ratio 提醒 issuecomment-554000732
- 原帖/精确回复：[Pinocchio armature 处理要区分质量矩阵对角近似、快速 ABA 与完整电机传动模型](https://github.com/stack-of-tasks/pinocchio/issues/671#issuecomment-553836338)
- 平台/作者：GitHub Issues / proyan
- 关键术语：电枢惯量（armature inertia）；反射转子惯量（reflected rotor inertia）；齿轮传动比（gear ratio）；串联弹性执行器（Series Elastic Actuator, SEA）
- 环境：2019–2022 年 Pinocchio 开发线程；用户自定义 Revolute ABA sketch；性能测试 nq=37、nv=32；pinocchio3-preview/3x 状态说明。
- 症状：早期版本虽保存 rotor inertia/gear ratio，但 forwardDynamics/ImpulseDynamics 的内部质量矩阵不使用 armature。；自定义 abaWithMot 初版不满足 (M+Imot)*a+b=u；修正 visitor data 后作者报告正常。
- 诊断：先确认 model 中保存的是已折算 armature 还是 rotor inertia 与 gear ratio，避免漏乘或重复乘传动比。；用 CRBA 得到 M、RNEA 得到 b，检查 (M+I_armature)*a+b-u 的残差。；区分刚性反射惯量近似与 Series Elastic Actuator 的双侧动力学，后者不能强行并入单一 M 对角。
- 原因：早期算法没有消费已加载的 rotor/armature 数据。；用户初版 AbaBackwardStep 把 revolute calc_aba 的 data 误写为旧 data，而非 jdata.derived()。
- 处理过程：讨论对比独立 withArmature 算法、直接后处理 M/RNEA、ABA 内更新 D_i，以及未来 actuator/transmission model。；用户实现 Featherstone 式对角更新并用动力学残差检查；另测 ABA 与 Eigen LLT。
- 有效处理：简单路径：computeAllTerms 后把正的 armature 加到质量矩阵对角，再求解；维护者建议优先试 Pinocchio sparse Cholesky 而非 Eigen LLT。；快速 ABA 近似：在 backward pass 使用 D_i = S_i^T U_i + I_rot；用户修正为 jdata.derived() 后报告工作正常。；维护者最终说明 armature 功能已在 pinocchio-3x 完成，但线程没有给最终 API。
- 结果：用户报告自定义 ABA 修正后动力学残差正常；其测试中 ABA 比 Eigen LLT 快 20–25%。；维护者最终写明 pinocchio-3x 已完成，早期 preview 的 API/bug 警告仍应作为历史版本边界。
- 限制：对角近似不包含电机旋转和支撑关节运动带来的 Coriolis/centrifugal effects。；线程中的 sketch 只实现特定 revolute joint，且维护者提醒 gear ratio；不能直接复制为所有 joint 类型。；Eigen LLT 性能对照不能代表 Pinocchio sparse Cholesky，用户明确没有完成后者 benchmark。；串联弹性执行器不满足电机与关节强刚性连接假设，需要独立 transmission/actuation dynamics。
- 安全提示：实机力矩与加速度预测前应确认 rotor inertia、gear ratio、armature 的单位和折算位置；重复折算会放大惯性，漏折算会低估执行器负担。
- 独立核验引用：[maintainer_confirmation · 维护者接受对角临时方案并要求 armature 为正](https://github.com/stack-of-tasks/pinocchio/issues/671#issuecomment-463259454)；[maintainer_confirmation · 维护者指出该方案遗漏电机与支撑关节运动的 Coriolis 效应](https://github.com/stack-of-tasks/pinocchio/issues/671#issuecomment-553836338)；[maintainer_confirmation · 维护者提醒用户实现还要考虑 gear ratio](https://github.com/stack-of-tasks/pinocchio/issues/671#issuecomment-554000732)
- 适用边界：主要适用于刚性传动、可用每自由度正值 reflected armature 近似的模型；柔顺或耦合传动需单独建模。

**经验 2：Pinocchio armature 处理要区分质量矩阵对角近似、快速 ABA 与完整电机传动模型**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：线程依据 Featherstone 式 9.28 给出近似：在 ABA backward pass 把 D_i 更新为 S_i^T U_i + I_rot，使反射惯量进入局部求逆。用户的初版残差不对，后来发现 AbaBackwardStep 中 revolute calc_aba 应使用 jdata.derived() 而不是旧 data；修正后他报告工作正常。验证方法是用 CRBA/RNEA 检查 (M+I_armature)*a+b-u 残差。该 sketch 只覆盖特定 revolute joint，并省略较小的电机 Coriolis 效应，不能当作完整 actuator model。
- 证据状态：`issue_candidate`
- 来源定位：Issue #671，ABA 结构 issuecomment-553834924；Featherstone 更新 issuecomment-553839281；作者修正与结果 issuecomment-553911858/553963329
- 原帖/精确回复：[Pinocchio armature 处理要区分质量矩阵对角近似、快速 ABA 与完整电机传动模型](https://github.com/stack-of-tasks/pinocchio/issues/671#issuecomment-553963329)
- 平台/作者：GitHub Issues / proyan
- 关键术语：关节空间惯量算法（Articulated-Body Algorithm, ABA）；反向遍历（backward pass）；动力学残差（dynamics residual）；转动关节（revolute joint）
- 环境：2019–2022 年 Pinocchio 开发线程；用户自定义 Revolute ABA sketch；性能测试 nq=37、nv=32；pinocchio3-preview/3x 状态说明。
- 症状：早期版本虽保存 rotor inertia/gear ratio，但 forwardDynamics/ImpulseDynamics 的内部质量矩阵不使用 armature。；自定义 abaWithMot 初版不满足 (M+Imot)*a+b=u；修正 visitor data 后作者报告正常。
- 诊断：先确认 model 中保存的是已折算 armature 还是 rotor inertia 与 gear ratio，避免漏乘或重复乘传动比。；用 CRBA 得到 M、RNEA 得到 b，检查 (M+I_armature)*a+b-u 的残差。；区分刚性反射惯量近似与 Series Elastic Actuator 的双侧动力学，后者不能强行并入单一 M 对角。
- 原因：早期算法没有消费已加载的 rotor/armature 数据。；用户初版 AbaBackwardStep 把 revolute calc_aba 的 data 误写为旧 data，而非 jdata.derived()。
- 处理过程：讨论对比独立 withArmature 算法、直接后处理 M/RNEA、ABA 内更新 D_i，以及未来 actuator/transmission model。；用户实现 Featherstone 式对角更新并用动力学残差检查；另测 ABA 与 Eigen LLT。
- 有效处理：简单路径：computeAllTerms 后把正的 armature 加到质量矩阵对角，再求解；维护者建议优先试 Pinocchio sparse Cholesky 而非 Eigen LLT。；快速 ABA 近似：在 backward pass 使用 D_i = S_i^T U_i + I_rot；用户修正为 jdata.derived() 后报告工作正常。；维护者最终说明 armature 功能已在 pinocchio-3x 完成，但线程没有给最终 API。
- 结果：用户报告自定义 ABA 修正后动力学残差正常；其测试中 ABA 比 Eigen LLT 快 20–25%。；维护者最终写明 pinocchio-3x 已完成，早期 preview 的 API/bug 警告仍应作为历史版本边界。
- 限制：对角近似不包含电机旋转和支撑关节运动带来的 Coriolis/centrifugal effects。；线程中的 sketch 只实现特定 revolute joint，且维护者提醒 gear ratio；不能直接复制为所有 joint 类型。；Eigen LLT 性能对照不能代表 Pinocchio sparse Cholesky，用户明确没有完成后者 benchmark。；串联弹性执行器不满足电机与关节强刚性连接假设，需要独立 transmission/actuation dynamics。
- 安全提示：实机力矩与加速度预测前应确认 rotor inertia、gear ratio、armature 的单位和折算位置；重复折算会放大惯性，漏折算会低估执行器负担。
- 独立核验引用：[issue · 贡献者引用 Featherstone 式 9.28 给出 D_i 的 armature 更新和近似边界](https://github.com/stack-of-tasks/pinocchio/issues/671#issuecomment-553839281)；[issue · 用户报告修正实现错误后工作正常](https://github.com/stack-of-tasks/pinocchio/issues/671#issuecomment-553911858)；[issue · 用户精确指出错误是 calc_aba 中未改用 jdata.derived()](https://github.com/stack-of-tasks/pinocchio/issues/671#issuecomment-553963329)
- 适用边界：适用于线程中的刚性反射惯量近似和特定 revolute joint sketch；正式版本应优先核对目标 Pinocchio 的内置 armature 支持。

**经验 3：Pinocchio armature 处理要区分质量矩阵对角近似、快速 ABA 与完整电机传动模型**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：维护者给出的替代路径是 computeAllTerms 后把 armature 加到质量矩阵对角，再对 M 做 Cholesky 求解；他建议使用 pinocchio::cholesky 的 sparse Cholesky，而不是 Eigen::LLT。用户只测了自定义 ABA 对 Eigen LLT：在 nq=37、nv=32 的模型上快 20–25%，没有测试 Pinocchio sparse 实现，所以不能把该比例外推。版本方面，维护者先称功能位于 pinocchio3-preview 并警告 API 可能变化、仍可能有 bug，后续只写“Done in pinocchio-3x”；线程没有给最终 release 号或 API 示例。
- 证据状态：`issue_candidate`
- 来源定位：Issue #671，Cholesky 路径 issuecomment-553836029/553963329；用户 benchmark issuecomment-553882755；3.x 状态 issuecomment-888498268/1117049845
- 原帖/精确回复：[Pinocchio armature 处理要区分质量矩阵对角近似、快速 ABA 与完整电机传动模型](https://github.com/stack-of-tasks/pinocchio/issues/671#issuecomment-1117049845)
- 平台/作者：GitHub Issues / proyan
- 关键术语：全量动力学计算（computeAllTerms）；稀疏乔列斯基分解（sparse Cholesky decomposition）；质量矩阵对角（mass-matrix diagonal）；性能基准（performance benchmark）
- 环境：2019–2022 年 Pinocchio 开发线程；用户自定义 Revolute ABA sketch；性能测试 nq=37、nv=32；pinocchio3-preview/3x 状态说明。
- 症状：早期版本虽保存 rotor inertia/gear ratio，但 forwardDynamics/ImpulseDynamics 的内部质量矩阵不使用 armature。；自定义 abaWithMot 初版不满足 (M+Imot)*a+b=u；修正 visitor data 后作者报告正常。
- 诊断：先确认 model 中保存的是已折算 armature 还是 rotor inertia 与 gear ratio，避免漏乘或重复乘传动比。；用 CRBA 得到 M、RNEA 得到 b，检查 (M+I_armature)*a+b-u 的残差。；区分刚性反射惯量近似与 Series Elastic Actuator 的双侧动力学，后者不能强行并入单一 M 对角。
- 原因：早期算法没有消费已加载的 rotor/armature 数据。；用户初版 AbaBackwardStep 把 revolute calc_aba 的 data 误写为旧 data，而非 jdata.derived()。
- 处理过程：讨论对比独立 withArmature 算法、直接后处理 M/RNEA、ABA 内更新 D_i，以及未来 actuator/transmission model。；用户实现 Featherstone 式对角更新并用动力学残差检查；另测 ABA 与 Eigen LLT。
- 有效处理：简单路径：computeAllTerms 后把正的 armature 加到质量矩阵对角，再求解；维护者建议优先试 Pinocchio sparse Cholesky 而非 Eigen LLT。；快速 ABA 近似：在 backward pass 使用 D_i = S_i^T U_i + I_rot；用户修正为 jdata.derived() 后报告工作正常。；维护者最终说明 armature 功能已在 pinocchio-3x 完成，但线程没有给最终 API。
- 结果：用户报告自定义 ABA 修正后动力学残差正常；其测试中 ABA 比 Eigen LLT 快 20–25%。；维护者最终写明 pinocchio-3x 已完成，早期 preview 的 API/bug 警告仍应作为历史版本边界。
- 限制：对角近似不包含电机旋转和支撑关节运动带来的 Coriolis/centrifugal effects。；线程中的 sketch 只实现特定 revolute joint，且维护者提醒 gear ratio；不能直接复制为所有 joint 类型。；Eigen LLT 性能对照不能代表 Pinocchio sparse Cholesky，用户明确没有完成后者 benchmark。；串联弹性执行器不满足电机与关节强刚性连接假设，需要独立 transmission/actuation dynamics。
- 安全提示：实机力矩与加速度预测前应确认 rotor inertia、gear ratio、armature 的单位和折算位置；重复折算会放大惯性，漏折算会低估执行器负担。
- 独立核验引用：[maintainer_confirmation · 维护者给出 computeAllTerms、对角更新和 Cholesky 路径](https://github.com/stack-of-tasks/pinocchio/issues/671#issuecomment-553836029)；[issue · 用户报告自定义 ABA 对 Eigen LLT 的 20–25% 性能差异及 nq/nv](https://github.com/stack-of-tasks/pinocchio/issues/671#issuecomment-553882755)；[maintainer_confirmation · 维护者警告 preview API 可能变化且仍可能有 bug](https://github.com/stack-of-tasks/pinocchio/issues/671#issuecomment-888498268)；[maintainer_confirmation · 维护者最终说明已在 pinocchio-3x 完成](https://github.com/stack-of-tasks/pinocchio/issues/671#issuecomment-1117049845)
- 适用边界：性能数字只对应用户的 nq=37、nv=32 模型和 Eigen LLT；Pinocchio 3.x 的具体 API/版本必须在本地文档与源码核对。

## 部署、固件与 SDK (`deployment_firmware_sdk`)

### WSL 中 Unitree SDK2 已编译，但访问不到 G1，怎么分层验证？

- `problem_id`：`problem.deployment_firmware_sdk.d7082f96792c522e`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Unitree SDK2 编译与 WSL 直连 G1 的网络备忘**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先确认使用与 CPU 架构匹配的库；再让 WSL 网卡真正进入 G1 的 192.168.123.0/24 网段，配置固定地址后先 ping 192.168.123.161，最后运行最小示例。帖子采用桥接方案，但具体 Windows/WSL 版本和网络安全策略需独立核验。
- 证据状态：`community_candidate`
- 来源定位：正文‘Hack 操作’及评论的架构/固件讨论
- 原帖/精确回复：[Unitree SDK2 编译与 WSL 直连 G1 的网络备忘](https://zhuanlan.zhihu.com/p/1903761818360455378)
- 平台/作者：Zhihu / 李国宝​​
- 关键术语：数据分发服务（Data Distribution Service, DDS）；软件开发工具包（Software Development Kit, SDK）
- 环境：Ubuntu 20.04/22.04/24.04；x86_64/aarch64；Windows 11 WSL；G1 网段 192.168.123.0/24。
- 症状：SDK 能编译但 WSL 与机器人网络隔离；评论另有 x86 误加载 aarch64 libddsc。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：WSL 虚拟网卡与宿主物理网段隔离；库目录/CPU 架构选错；固件可能过旧。
- 处理过程：桥接网卡、给 WSL eth0 配同网段固定 IP、ping 机器人；用 ankle_swing 示例验证。
- 结果：作者称网线直连和 WSL 桥接可用；评论中的固件问题只给出升级结论。
- 限制：网络桥接有系统与安全风险；无线可用性未确认；版本需对照官方 SDK。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：四个截图位用于 SDK 编译、ankle_swing 与 Windows 网桥步骤；配置重点是 CPU 架构匹配、192.168.123.x 网段和 ping 验证。
- 采集完整性：`partial_visible`；可见回复 7；展开 0 次；回复深度 1/10；停止原因：no_visible_expand_controls
- 适用边界：网络桥接有系统与安全风险；无线可用性未确认；版本需对照官方 SDK。

### 开源人形项目要形成可复现闭环，LeRobot Humanoid 线程列出了哪些环节？

- `problem_id`：`problem.deployment_firmware_sdk.568ef914364a3624`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：LeRobot Humanoid 全栈闭环：从设计到真机部署**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：线程给出 design→simulation→data collection→system identification→policy training→real deployment，并把 hardware/CAD、runtime/calibration、sim、identification 和 motion training library 一起发布。是否能直接复现仍需按版本与安全测试验收。
- 证据状态：`community_candidate`
- 来源定位：根帖及作者闭环回复
- 原帖/精确回复：[LeRobot Humanoid 全栈闭环：从设计到真机部署](https://x.com/robotsdigest/status/2057507899359043871)
- 平台/作者：X / Robots Digest  @robotsdigest
- 关键术语：全身控制（Whole-Body Control, WBC）；惯性测量单元（Inertial Measurement Unit, IMU）；有效载荷（Payload）；系统辨识（System Identification）；安全急停（Emergency Stop, E-Stop）
- 环境：约 2.5k 美元 3D 打印人形；开源软硬件栈。
- 症状：帖子未报告具体故障。
- 诊断：检查 CAD、运行时、标定、仿真、识别和训练是否版本绑定。
- 原因：缺失任一层会把系统集成成本转嫁给复现者。
- 处理过程：发布全栈并给出 blog/code。
- 有效处理：候选机制是闭环版本化全栈，而非单独模型。
- 结果：帖子宣称可构建、拆解、修复、仿真和真机训练。
- 限制：未核对实际 BOM、构建时长和控制性能。
- 安全提示：低成本/3D 打印结构仍需载荷、疲劳、限位和急停验证。
- 图片分析：截图展示 LeRobot Humanoid 论文/项目封面和全栈清单，未包含构建误差、控制频率或实机性能。
- 采集完整性：`partial_visible`；可见回复 3；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于设计开源人形的最小复现清单。

### G1 吊在吊架上且脚离地时，为什么不能直接进入平衡或行走模式？

- `problem_id`：`problem.deployment_firmware_sdk.49686ebdf3dd0b36`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Unitree G1 首次上机的校准、安全、Jetson 与 SDK 排查顺序**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：平衡策略仍会按有地面支撑的假设寻找恢复动作，脚底没有接触时可能驱动腿部大幅运动。吊架应保留用于防跌倒，但双脚需实际接触地面并留有合适松量，再进入 balance/walk policy。
- 证据状态：`community_candidate`
- 来源定位：文章第 1 节 Expert tip
- 原帖/精确回复：[Unitree G1 首次上机的校准、安全、Jetson 与 SDK 排查顺序](https://x.com/clankrmedia/status/2062158494363537690)
- 平台/作者：X / clankr (@clankrmedia)
- 关键术语：支撑接触（support contact）；平衡策略（balance policy）；吊架（gantry）
- 环境：Unitree G1 EDU；机载 Jetson 开发计算单元；SDK2 期望 Ubuntu 20.04、GCC 9.4、CMake 3.10+。
- 症状：脚不接地时平衡策略仍试图找支撑并驱动腿部。；遥操作或 policy 运行中出现可听见的过热告警。；SDK 示例不通时难以区分网络、DDS 和代码问题。
- 诊断：先在 Explore App 检查状态、报警、温度、网络与校准。；SSH 后检查接口和 SDK2 示例，先读状态再写控制。
- 原因：平衡策略的接触/状态假设不成立。；持续运动造成局部电机热积累。；Jetson 镜像与机器人内部软件栈不同步。；网卡或 DDS 配置错误。
- 处理过程：保持吊架但让双脚实际接地后再启平衡。；过热时停止任务、固定吊架、回 idle，并从外部温和冷却后查根因。；保留厂商镜像，按官方文档安装 SDK。；先编译并运行只读状态示例。
- 结果：作者给出亲历性的安全与调试顺序，但未提供温度曲线或独立复现实验。
- 限制：帖子为个人经验汇总；外部风扇只是应急措施，不能替代热源和载荷诊断。
- 安全提示：始终保留吊架、清场、急停路径和低风险初始姿态；控制示例必须在只读状态链路验证后再逐步放开。
- 图片分析：X Article 的关键内容均在可见正文；配图主要展示 G1 本体和防护，不承担日志或参数证据。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_replies
- 适用边界：适用于 G1 EDU 的初次校准与平衡策略测试。

### G1 SDK2 接入时，怎样用最小风险顺序区分网络、DDS 与控制代码问题？

- `problem_id`：`problem.deployment_firmware_sdk.be9f5d36d0a2ef41`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Unitree G1 首次上机的校准、安全、Jetson 与 SDK 排查顺序**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先让机器人和 Jetson 网络连通，确认正确网卡；编译 SDK2 官方示例；首先运行只读 robot-state 示例验证 CycloneDDS 与状态接收；成功后才尝试写控制。这样可把环境/网络问题与控制逻辑分开，并减少首次调试时的真机风险。
- 证据状态：`community_candidate`
- 来源定位：文章第 4 节 first development ritual
- 原帖/精确回复：[Unitree G1 首次上机的校准、安全、Jetson 与 SDK 排查顺序](https://x.com/clankrmedia/status/2062158494363537690)
- 平台/作者：X / clankr (@clankrmedia)
- 关键术语：数据分发服务（DDS）；只读冒烟测试（read-only smoke test）；网络接口（network interface）
- 环境：Unitree G1 EDU；机载 Jetson 开发计算单元；SDK2 期望 Ubuntu 20.04、GCC 9.4、CMake 3.10+。
- 症状：脚不接地时平衡策略仍试图找支撑并驱动腿部。；遥操作或 policy 运行中出现可听见的过热告警。；SDK 示例不通时难以区分网络、DDS 和代码问题。
- 诊断：先在 Explore App 检查状态、报警、温度、网络与校准。；SSH 后检查接口和 SDK2 示例，先读状态再写控制。
- 原因：平衡策略的接触/状态假设不成立。；持续运动造成局部电机热积累。；Jetson 镜像与机器人内部软件栈不同步。；网卡或 DDS 配置错误。
- 处理过程：保持吊架但让双脚实际接地后再启平衡。；过热时停止任务、固定吊架、回 idle，并从外部温和冷却后查根因。；保留厂商镜像，按官方文档安装 SDK。；先编译并运行只读状态示例。
- 结果：作者给出亲历性的安全与调试顺序，但未提供温度曲线或独立复现实验。
- 限制：帖子为个人经验汇总；外部风扇只是应急措施，不能替代热源和载荷诊断。
- 安全提示：始终保留吊架、清场、急停路径和低风险初始姿态；控制示例必须在只读状态链路验证后再逐步放开。
- 图片分析：X Article 的关键内容均在可见正文；配图主要展示 G1 本体和防护，不承担日志或参数证据。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_replies
- 适用边界：适用于 Unitree SDK2/SDK2 Python 的 G1 接入。

### 为什么不应把机载 Jetson 当普通 Linux 主机随意重刷镜像？

- `problem_id`：`problem.deployment_firmware_sdk.c7fbc801d6b7f987`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Unitree G1 首次上机的校准、安全、Jetson 与 SDK 排查顺序**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：G1 的开发计算单元与内部运动控制侧存在配套的软件和网络关系；自行重刷可能让版本、驱动或通信配置失配，把普通系统问题扩大成整机问题。应先备份现状、遵循厂商升级路径，并把业务环境放在可回滚的虚拟环境或容器中。
- 证据状态：`community_candidate`
- 来源定位：文章第 3 节 onboard Jetson
- 原帖/精确回复：[Unitree G1 首次上机的校准、安全、Jetson 与 SDK 排查顺序](https://x.com/clankrmedia/status/2062158494363537690)
- 平台/作者：X / clankr (@clankrmedia)
- 关键术语：机载计算单元（onboard computer）；软件栈一致性（software-stack consistency）；可回滚环境（rollback-safe environment）
- 环境：Unitree G1 EDU；机载 Jetson 开发计算单元；SDK2 期望 Ubuntu 20.04、GCC 9.4、CMake 3.10+。
- 症状：脚不接地时平衡策略仍试图找支撑并驱动腿部。；遥操作或 policy 运行中出现可听见的过热告警。；SDK 示例不通时难以区分网络、DDS 和代码问题。
- 诊断：先在 Explore App 检查状态、报警、温度、网络与校准。；SSH 后检查接口和 SDK2 示例，先读状态再写控制。
- 原因：平衡策略的接触/状态假设不成立。；持续运动造成局部电机热积累。；Jetson 镜像与机器人内部软件栈不同步。；网卡或 DDS 配置错误。
- 处理过程：保持吊架但让双脚实际接地后再启平衡。；过热时停止任务、固定吊架、回 idle，并从外部温和冷却后查根因。；保留厂商镜像，按官方文档安装 SDK。；先编译并运行只读状态示例。
- 结果：作者给出亲历性的安全与调试顺序，但未提供温度曲线或独立复现实验。
- 限制：帖子为个人经验汇总；外部风扇只是应急措施，不能替代热源和载荷诊断。
- 安全提示：始终保留吊架、清场、急停路径和低风险初始姿态；控制示例必须在只读状态链路验证后再逐步放开。
- 图片分析：X Article 的关键内容均在可见正文；配图主要展示 G1 本体和防护，不承担日志或参数证据。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_replies
- 适用边界：适用于保修和厂商镜像约束下的 G1 EDU。

### G1 运行遥操作或策略时出现电机过热告警，第一步怎么做？

- `problem_id`：`problem.deployment_firmware_sdk.e16ecf5ca28fe2e3`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Unitree G1 首次上机的校准、安全、Jetson 与 SDK 排查顺序**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先停止当前动作，确保机器人受吊架保护并回到 idle；记录具体电机、负载、持续时间和温度，再检查姿态、增益与任务占空比。帖子提到可用小风扇温和外部冷却作为应急，但这不是根因修复，未确认安全温度前不要继续高负载。
- 证据状态：`community_candidate`
- 来源定位：文章第 2 节 overheating warning 段
- 原帖/精确回复：[Unitree G1 首次上机的校准、安全、Jetson 与 SDK 排查顺序](https://x.com/clankrmedia/status/2062158494363537690)
- 平台/作者：X / clankr (@clankrmedia)
- 关键术语：热保护（thermal protection）；空闲模式（idle mode）；占空比（duty cycle）
- 环境：Unitree G1 EDU；机载 Jetson 开发计算单元；SDK2 期望 Ubuntu 20.04、GCC 9.4、CMake 3.10+。
- 症状：脚不接地时平衡策略仍试图找支撑并驱动腿部。；遥操作或 policy 运行中出现可听见的过热告警。；SDK 示例不通时难以区分网络、DDS 和代码问题。
- 诊断：先在 Explore App 检查状态、报警、温度、网络与校准。；SSH 后检查接口和 SDK2 示例，先读状态再写控制。
- 原因：平衡策略的接触/状态假设不成立。；持续运动造成局部电机热积累。；Jetson 镜像与机器人内部软件栈不同步。；网卡或 DDS 配置错误。
- 处理过程：保持吊架但让双脚实际接地后再启平衡。；过热时停止任务、固定吊架、回 idle，并从外部温和冷却后查根因。；保留厂商镜像，按官方文档安装 SDK。；先编译并运行只读状态示例。
- 结果：作者给出亲历性的安全与调试顺序，但未提供温度曲线或独立复现实验。
- 限制：帖子为个人经验汇总；外部风扇只是应急措施，不能替代热源和载荷诊断。
- 安全提示：始终保留吊架、清场、急停路径和低风险初始姿态；控制示例必须在只读状态链路验证后再逐步放开。
- 图片分析：X Article 的关键内容均在可见正文；配图主要展示 G1 本体和防护，不承担日志或参数证据。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_replies
- 适用边界：适用于 G1 EDU；温度阈值和冷却方式应以厂商要求为准。

## 安全、跌倒、冲击与起身 (`safety_fall_recovery`)

### 安全摔倒控制应在什么时候接管正常 WBC？

- `problem_id`：`problem.safety_fall_recovery.965dc5a77c3e73c7`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：SafeFall：G1 不可恢复跌倒预测与保护动作的社区论文摘要**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该帖描述的结构是先用轻量预测器判断跌倒已不可恢复，再由专门 RL 策略接管，而非全程干扰正常控制。帖子列出的预警与减伤数字尚未独立核验，不能直接作为上线阈值；需要重点验证误报、漏报和接管延迟。
- 证据状态：`community_candidate`
- 来源定位：根帖 SafeFall 机制与效果段落
- 原帖/精确回复：[SafeFall：G1 不可恢复跌倒预测与保护动作的社区论文摘要](https://www.xiaohongshu.com/explore/6925f768000000001e037fc9)
- 平台/作者：Xiaohongshu / 小博爱科研（机器人版）
- 关键术语：全身控制（Whole-Body Control, WBC）；强化学习（Reinforcement Learning, RL）；惯性测量单元（Inertial Measurement Unit, IMU）；关节力矩（Joint Torque）；端到端时延（End-to-End Latency）；门控循环单元（Gated Recurrent Unit, GRU）
- 环境：Unitree G1；IMU + 关节编码器；多方向/绊倒场景。
- 症状：不可恢复跌倒将造成峰值冲击、扭矩和脆弱部件碰撞。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：正常控制器失去可恢复性后仍继续执行，缺少专门保护接管。
- 处理过程：GRU 预测不可避免跌倒，触发 RL 策略分散冲击并保护关键部件。
- 结果：帖子列出 410 ms、<0.1%、68.3%/78.4%/99.3% 等数字。
- 限制：这是社区论文摘要；数字、‘首个’和 arXiv 2511.18509v1 必须回原论文核验。
- 安全提示：保护策略上线前必须在仿真、吊挂和软垫环境逐级验收，验证误触发和接管时序。
- 图片分析：11 个媒体位用于概述 SafeFall 预测与保护动作/实验；帖子列出的 410 ms 和减伤百分比需回原论文图表核验，不能仅凭社交平台图片采信。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：all_visible_comments_loaded
- 适用边界：这是社区论文摘要；数字、‘首个’和 arXiv 2511.18509v1 必须回原论文核验。

### 为什么行走中的 G1 不能简单把“断电”当作安全急停？

- `problem_id`：`problem.safety_fall_recovery.77676ba42eae8751`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：G1 行走时直接断电的急停可能触发失控跌倒**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：因为双足稳定依赖主动控制，直接切断动力可能造成不可控跌倒并扩大碰撞风险。该帖只确认风险并链接研究，没有提供已验证修复；应进一步设计并验证受控减速、保护姿态、制动与隔离策略。
- 证据状态：`community_candidate`
- 来源定位：根帖与 source 回复
- 原帖/精确回复：[G1 行走时直接断电的急停可能触发失控跌倒](https://x.com/noclipepe/status/2086582709082583420)
- 平台/作者：X / noclipepe @noclipepe
- 关键术语：全身控制（Whole-Body Control, WBC）；安全急停（Emergency Stop, E-Stop）
- 环境：Unitree G1 行走；人员/物体可能在跌倒范围内。
- 症状：切断动力后出现不可控跌倒风险。
- 诊断：区分 power cut、受控制动、保护姿态和外部支撑；评估跌倒包络。
- 原因：双足稳定依赖持续主动控制，断电不是静态安全态。
- 处理过程：帖子引用一项研究提出问题。
- 结果：原帖明确把安全停止标为未解决工程问题。
- 限制：没有给出速度、姿态、跌倒方向或急停实现细节；需核对论文。
- 安全提示：实机急停设计必须评估受控减速、保护姿态、制动器和人员隔离，不能默认断电即安全。
- 图片分析：截图清晰展示“断电急停可能导致失控跌倒”的文字论点；未显示实验工况、跌倒轨迹或安全边界。
- 采集完整性：`partial_visible`；可见回复 3；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于行走或动态任务中的人形机器人急停设计。

### 为什么不能仅凭一段无失误舞蹈视频判断人形 WBC 鲁棒？

- `problem_id`：`problem.safety_fall_recovery.4addd02187d0626a`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：舞蹈演示应关注姿态转换恢复，而非只看编排动作**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：视频可观察连续 pose transition 和重心迁移，但评论指出动作可能编排并反复练习；没有外扰、失败次数、状态/接触曲线或控制器信息，所以只能形成定性观察，不能证明鲁棒恢复。
- 证据状态：`community_candidate`
- 来源定位：根帖与 @0xAxia 质疑/作者回复
- 原帖/精确回复：[舞蹈演示应关注姿态转换恢复，而非只看编排动作](https://x.com/0xsyrex/status/2086786639037112356)
- 平台/作者：X / Syrex.eth @0xSyrex
- 关键术语：全身控制（Whole-Body Control, WBC）；质心（Center of Mass, CoM）
- 环境：现场舞蹈演示；连续手臂/腿部动作。
- 症状：原帖未报告失败，只观察无可见 reset。
- 诊断：关注髋部、站姿重整和转换间是否有可见修正。
- 原因：连续重心转移对平衡控制提出更强瞬态要求。
- 处理过程：用舞蹈视频做定性观察。
- 结果：演示保持平衡，但可能经过编排与练习。
- 限制：无法从视频推断算法鲁棒性或通信实时性。
- 安全提示：演示不等于抗扰验证；需独立推推、恢复和失败测试。
- 图片分析：截图是作者对姿态转换、髋部恢复和连续平衡的文字分析，未显示状态曲线或扰动实验。
- 采集完整性：`partial_visible`；可见回复 5；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于评审人形演示视频的证据强度。

## 传感器与感知接口 (`sensing_and_perception`)

### 模仿学习策略出现规律性‘抽搐’，怎样判断是控制问题还是采集时间戳问题？

- `problem_id`：`problem.sensing_and_perception.4071f254339249b0`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：具身数据视频、动作与传感器时间戳错位导致策略‘抽搐’**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先离线对齐视频事件、动作边沿和 IMU/关节状态，估计固定 offset 与随时间漂移；把主时钟、原始时间戳和同步事件都保留，再用可视化重放检查。帖子只给原则，具体阈值需由控制周期与任务带宽决定。
- 证据状态：`community_candidate`
- 来源定位：根帖正文
- 原帖/精确回复：[具身数据视频、动作与传感器时间戳错位导致策略‘抽搐’](https://www.xiaohongshu.com/explore/6a0be22200000000370340c8)
- 平台/作者：Xiaohongshu / 以物思智能制造项目部
- 关键术语：全身控制（Whole-Body Control, WBC）；惯性测量单元（Inertial Measurement Unit, IMU）；全身遥操作（Whole-Body Teleoperation）；时间戳同步（Timestamp Synchronization）
- 环境：视频、动作命令和多传感器异步采集。
- 症状：训练后策略像抽搐；视频与动作/传感器对齐偏移。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：多个独立时钟、未记录 offset、缺同步脉冲与离线对齐质检。
- 处理过程：建议选主时钟、记录偏移、使用同步信号并建立离线质检指标。
- 结果：没有公开实现或复测数据。
- 限制：缺少时钟源、采样率、漂移模型和可接受误差阈值。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：五张信息图围绕主时钟、偏移、同步信号和离线质检；未见原始时间戳散点或 cross-correlation 曲线，不能据图确定阈值。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：all_visible_comments_loaded
- 适用边界：缺少时钟源、采样率、漂移模型和可接受误差阈值。

### 推理时 sampling MPC 需要大量 rollout，而通用模拟器达不到实时预算时怎么办？

- `problem_id`：`problem.sensing_and_perception.7757e87bbdd5c9fb`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：RGB real2sim + 256 并行 rollout 的推理时 MPPI 精炼**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该案例采用任务专用模拟器：RGB real2sim 映射状态，单 RTX 4090 上运行 256 个并行环境、H=5 的 MPPI，对基础策略轨迹实时精炼。作者称通用模拟器未满足其速度/稳定性组合，但需论文复核基准。
- 证据状态：`community_candidate`
- 来源定位：作者 1/3 与 2/3 线程
- 原帖/精确回复：[RGB real2sim + 256 并行 rollout 的推理时 MPPI 精炼](https://x.com/fanshi_robot/status/2074920170641068157)
- 平台/作者：X / Fan Shi RSS 2026 @fanshi_robot
- 关键术语：全身控制（Whole-Body Control, WBC）；模型预测控制（Model Predictive Control, MPC）；状态估计（State Estimation）；惯性测量单元（Inertial Measurement Unit, IMU）；动力学（Dynamics）
- 环境：单 RTX 4090；256 并行环境；H=5；RGB 状态估计。
- 症状：现有模拟器无法同时提供所需速度与稳定准确的可变形动力学。
- 诊断：比较 rollout 吞吐、动力学稳定性和推理成功率。
- 原因：可变形动力学与大批量闭环 rollout 的计算需求冲突。
- 处理过程：构建自定义模拟器并用 MPPI 精炼轨迹。
- 有效处理：候选方案是任务专用 simulator + RGB real2sim + 256 并行 MPPI。
- 结果：作者称提升推理成功率，但线程无数值。
- 限制：非 WBC/人形任务；参数不能直接迁移。
- 安全提示：real2sim 估计误差必须进入 MPC 安全约束和失败回退。
- 图片分析：截图视频帧显示双臂可变形布料任务和方法要点；没有 rollout 延迟或成功率曲线。
- 采集完整性：`partial_visible`；可见回复 3；展开 0 次；回复深度 1/10；停止原因：no_growth_after_visible_scroll
- 适用边界：适用于高吞吐 sampling-based MPC 的工具链取舍，非直接人形结论。

## 复现、日志、评估与调试方法 (`reproducibility_and_debugging`)

### WBC/机器人项目要做到可查询和可复现，最小记录单位应是什么？

- `problem_id`：`problem.reproducibility_and_debugging.27dc52abc910b011`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：机器人复现的最小单位不是模型，而是完整部署元组**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该 Article 主张不是单独模型，而是 (policy/model, embodiment, task, environment) 元组，并随附 action/state space、控制频率、URDF/MJCF、标定、安全限位、仿真配置、训练运行和实机结果。它是社区架构提案，但非常适合作为候选数据契约。
- 证据状态：`community_candidate`
- 来源定位：X Article 第 3–4 节
- 原帖/精确回复：[机器人复现的最小单位不是模型，而是完整部署元组](https://x.com/mexitlan/status/2052237191620047312)
- 平台/作者：X / Diego Prats |  @mexitlan
- 关键术语：全身控制（Whole-Body Control, WBC）；仿真到现实（Simulation-to-Real, Sim2Real）；惯性测量单元（Inertial Measurement Unit, IMU）；统一机器人描述格式（Unified Robot Description Format, URDF）；机器人模型格式（MuJoCo Modeling Format, MJCF）
- 环境：跨策略、机体、任务、环境；Franka/UR5/LeRobot 示例。
- 症状：训练 loss 正常但成功率 0%；选错 URDF 后 sim-to-real 失败；旧仿真配置不可重跑。
- 诊断：把 action/state space、控制频率、机体、任务、环境、URDF、标定、安全限位与结果绑定。
- 原因：机器人价值单元是完整元组，现有 hub 只以模型为中心。
- 处理过程：文章提出四类 registry/bundle 机制。
- 有效处理：候选数据模型是版本化完整 deployment bundle，并关联实机/仿真结果与社区复现。
- 结果：是架构建议，尚非已部署平台。
- 限制：文章中的案例和 30% 说法需回到各原始链接核对。
- 安全提示：公开 bundle 不应省略安全限位、标定版本和已知失效边界。
- 图片分析：截图展示 Article 标题、TL;DR 和流程示意图；示意图只能说明文章结构，具体四类 artifact 需以正文为准。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：article_body_loaded_without_visible_replies
- 适用边界：适用于建立 WBC 工程问题与复现 bundle 查询系统。

## 机械集成、负载与配重 (`mechanical_payload_integration`)

### CAD 转 URDF 后仿真能动，但策略真机明显跑偏，先核对哪些机械量？

- `problem_id`：`problem.mechanical_payload_integration.cb8bbd6e2846b904`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：SolidWorks→URDF 后的质量、惯量、坐标系与碰撞体验收**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先对照 SolidWorks 质量评估逐 link 核对 mass、COM 和 inertia（包括非对角项符号），再核对 joint 轴/坐标系、机械限位、effort 的 Nm 与 velocity 的 rad/s；同时简化碰撞体而不要改错视觉/惯性。该清单未给容差，需由平台测量精度定义。
- 证据状态：`community_candidate`
- 来源定位：正文 A/B/C 检查项
- 原帖/精确回复：[SolidWorks→URDF 后的质量、惯量、坐标系与碰撞体验收](https://zhuanlan.zhihu.com/p/2001625303685034796)
- 平台/作者：Zhihu / 风拂过你的头发
- 关键术语：全身控制（Whole-Body Control, WBC）；统一机器人描述格式（Unified Robot Description Format, URDF）；关节力矩（Joint Torque）；质心（Center of Mass, CoM）
- 环境：SolidWorks 装配体→URDF→MuJoCo/Isaac Sim；RViz/VS Code 检查。
- 症状：策略真机跑偏、仿真加载失败或变慢、关节方向/限位错误。
- 诊断：按正文、可见评论和媒体说明交叉整理；未经论文/源码/官方文档独立验证。
- 原因：质量/重心/惯性张量导出不准，惯量非对角项符号错误，网格面数过多或碰撞体过细。
- 处理过程：手工回填 inertial 字段，核对总质量、关节坐标系和限位，简化碰撞几何，用 MuJoCo/RViz 可视化。
- 结果：形成导出后验收清单；没有量化误差阈值。
- 限制：个人经验；闭链结构仍需在目标仿真器中额外建约束。
- 安全提示：社区候选只用于形成排查假设；涉及真机时先限速、限力、隔离人员并保留日志。
- 图片分析：候选未发现可见媒体；质量、惯性和碰撞体验收完全来自正文，未声称看到了图片证据。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_expand_controls
- 适用边界：个人经验；闭链结构仍需在目标仿真器中额外建约束。

### Pinocchio 固定关节链中无法直接隔离工具惯量

- `problem_id`：`problem.mechanical_payload_integration.pinocchio_fixed_link_tool_inertia_1388`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 会把固定关节链的惯量合并，旧接口不能直接隔离末端工具惯量**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：维护者确认固定关节链的惯量会被合并，因为算法层不需要分别保留。对法兰→F/T 传感器→工具的结构，最后一个 data.com 子树包含三者，不能当成工具自身的质量与质心。原帖当时可执行的处理有两种：从原始 URDF parser/tree 读取单体信息，或像提问团队一样把工具惯量作为独立参数传给控制库。维护者最后称 #1415 已解决，但线程没有展示新 API，本卡不补写其用法。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1388，维护者合并语义 issuecomment-773507916；用户临时方案 issuecomment-773599051；PR 状态 issuecomment-811858647
- 原帖/精确回复：[Pinocchio 会把固定关节链的惯量合并，旧接口不能直接隔离末端工具惯量](https://github.com/stack-of-tasks/pinocchio/issues/1388#issuecomment-773507916)
- 平台/作者：GitHub Issues / domire8
- 关键术语：固定关节（fixed joint）；惯量（inertia）；质心（center of mass, CoM）；力/力矩传感器（force/torque sensor）
- 环境：Franka Panda；URDF；法兰→固定关节 F/T 传感器→固定关节工具；2021 年 Pinocchio 线程，具体发布版本未说明。
- 症状：固定关节只作为 frame 保留，最后一个 data.com 子树包含法兰、F/T 传感器和工具的合并惯量，无法隔离工具。
- 诊断：确认目标是工具自身惯量还是最后一个可动关节后的完整刚性子树；不要把 data.com 最后一项直接视为工具参数。
- 原因：维护者确认算法层不需要固定链内部的分离惯量，因此解析时将其合并。
- 处理过程：维护者建议通过原始 URDF tree/parser 访问信息，并讨论为 Frame 保存惯量；用户说明在等待功能期间把工具信息作为独立参数传入。
- 有效处理：旧接口下，原帖团队把工具惯量作为控制库的独立参数；另一条维护者建议是直接读取原始 URDF parser/tree 信息。；维护者后来称 PR #1415 已解决该问题，但原线程未展示具体调用方式。
- 结果：团队用独立工具参数继续研究；维护者最终把线程标为由 #1415 解决。
- 限制：未读取 #1415 diff，不能声称哪个 Pinocchio 版本、Frame 字段或 API 可直接返回固定链单体惯量。
- 安全提示：力传感器重力补偿使用错误的合并惯量会把法兰和传感器重量重复计入；实机前应逐项核对质量、质心、坐标系和安装方向。
- 独立核验引用：[maintainer_confirmation · 维护者确认固定链惯量被合并并建议访问原始 URDF tree](https://github.com/stack-of-tasks/pinocchio/issues/1388#issuecomment-773507916)；[issue · 用户说明暂时把工具信息作为独立参数传给控制库](https://github.com/stack-of-tasks/pinocchio/issues/1388#issuecomment-773599051)；[pull_request · 维护者称解决该问题的 PR；本轮未读取补丁细节](https://github.com/stack-of-tasks/pinocchio/pull/1415)
- 适用边界：适用于 URDF 固定关节链和需要单独工具惯量的 F/T 重力补偿；新版本能力需结合 #1415 和本地 API 核对。

## communication_realtime_control (`communication_realtime_control`)

### 50 Hz 遥操作上层接 250 Hz 执行层时，为什么队列会越积越多并产生突发震荡？

- `problem_id`：`problem.communication_realtime_control.6536ecbd3107ee9b`
- 问题综合等级：**需要实际验证** — 不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：50 Hz 遥操作到 250 Hz 执行层的队列溢出与欠载抖动**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突；尚未形成可核对的复现记录。
- 解答状态：`conflicting`
- 候选解答：平均频率相等不代表瞬时生产与消费严格同步。Python 调度、ROS 传输和插值批量写入会造成 burst；若队列满后丢弃新目标，执行层继续消费旧轨迹，于是延时不断增长，恢复时目标发生跳变。应记录双端单调时钟和队列水位，并设置有界缓冲、过期命令丢弃和目标连续性保护。
- 证据状态：`community_candidate`
- 来源定位：现象描述、队列满丢报文段及可见评论质疑
- 原帖/精确回复：[50 Hz 遥操作到 250 Hz 执行层的队列溢出与欠载抖动](https://zhuanlan.zhihu.com/p/1898317277964768890)
- 平台/作者：Zhihu / 非要我改用户名
- 关键术语：生产者—消费者（producer-consumer）；队列水位（queue depth）；时延抖动（latency jitter）
- 环境：上层遥操作 50 Hz/20 ms；下层 C++ 执行 250 Hz/4 ms；ROS topic；最大队列 5000，队列累计 10 条后执行。
- 症状：队列满后丢弃新报文，动作出现长延时和突然大幅震荡。；主动丢弃 1/5 报文后延时减小，但队列周期耗空并持续抖动。
- 诊断：同时记录上层生产时间戳、下层消费时间戳、队列深度、丢包计数和执行目标连续性。
- 原因：Python 与 C++ 端时钟/调度没有对齐。；固定五等分插值没有处理网络抖动和生产消费偏差。
- 处理过程：把每个 20 ms 命令拆成 5 份供 4 ms 执行层消费。；主动丢弃 1/5 报文降低队列增长。；计划把 Python 中间层改为 C++。
- 结果：第一个方案仍会队列满；第二个方案降低延时但出现欠载抖动；最终 C++ 改写方向没有公开复现结果。
- 限制：评论对文章部分总线事实提出质疑；没有公开时间戳曲线、丢包率或最终改写结果。
- 安全提示：真机测试前限制关节速度、位置增量和力矩；队列异常时保持最后安全目标或进入阻尼模式，不应把缺帧直接转成突变。
- 图片分析：正文 Mermaid 图解释了上层异步写队列、下层严格周期取队列的结构；图是概念结构，不是实测时序证据。
- 采集完整性：`partial_visible`；可见回复 8；展开 1 次；回复深度 2/10；停止原因：nested_replies_collapsed
- 适用边界：适用于非实时上层到高频伺服层的命令桥接；具体结论需用本机时间戳验证。

### 为降低遥操作延时而固定丢弃一部分报文，为什么反而出现持续抖动？

- `problem_id`：`problem.communication_realtime_control.74a1f28025b2c0c1`
- 问题综合等级：**需要实际验证** — 不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：50 Hz 遥操作到 250 Hz 执行层的队列溢出与欠载抖动**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突；尚未形成可核对的复现记录。
- 解答状态：`conflicting`
- 候选解答：固定丢包使平均生产率低于 250 Hz 消费率时，队列会周期耗空；如果空队列被解释成无目标、零值或突然保持，关节目标就不连续。更稳妥的是按目标时间戳重采样，在有界延迟预算内插值，并对欠载采用最后安全值、速度限制或阻尼退化，同时监控 underrun。
- 证据状态：`community_candidate`
- 来源定位：主动丢弃 1/5 后队列执行空与抖动段
- 原帖/精确回复：[50 Hz 遥操作到 250 Hz 执行层的队列溢出与欠载抖动](https://zhuanlan.zhihu.com/p/1898317277964768890)
- 平台/作者：Zhihu / 非要我改用户名
- 关键术语：队列欠载（buffer underrun）；时间戳重采样（timestamp resampling）；安全保持（safe hold）
- 环境：上层遥操作 50 Hz/20 ms；下层 C++ 执行 250 Hz/4 ms；ROS topic；最大队列 5000，队列累计 10 条后执行。
- 症状：队列满后丢弃新报文，动作出现长延时和突然大幅震荡。；主动丢弃 1/5 报文后延时减小，但队列周期耗空并持续抖动。
- 诊断：同时记录上层生产时间戳、下层消费时间戳、队列深度、丢包计数和执行目标连续性。
- 原因：Python 与 C++ 端时钟/调度没有对齐。；固定五等分插值没有处理网络抖动和生产消费偏差。
- 处理过程：把每个 20 ms 命令拆成 5 份供 4 ms 执行层消费。；主动丢弃 1/5 报文降低队列增长。；计划把 Python 中间层改为 C++。
- 结果：第一个方案仍会队列满；第二个方案降低延时但出现欠载抖动；最终 C++ 改写方向没有公开复现结果。
- 限制：评论对文章部分总线事实提出质疑；没有公开时间戳曲线、丢包率或最终改写结果。
- 安全提示：真机测试前限制关节速度、位置增量和力矩；队列异常时保持最后安全目标或进入阻尼模式，不应把缺帧直接转成突变。
- 图片分析：正文 Mermaid 图解释了上层异步写队列、下层严格周期取队列的结构；图是概念结构，不是实测时序证据。
- 采集完整性：`partial_visible`；可见回复 8；展开 1 次；回复深度 2/10；停止原因：nested_replies_collapsed
- 适用边界：适用于上层采样率低于下层控制率的遥操作链。

### 确认反馈周期丢帧后，修复和安全兜底应分哪两层？

- `problem_id`：`problem.communication_realtime_control.0555df34f0b94e29`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：CANopen 关节力控周期震荡的时序排查方法**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：通信层先量化总线负载和每个 TPDO 周期，选择降低发送频率、拆分总线或迁移 CAN-FD；控制层同时定义缺帧语义，短暂缺帧可保持最近可信值或按时间戳插值，超过阈值则切入阻尼/安全停机。保持和插值都有风险，必须结合力矩变化率与 watchdog 验证。
- 证据状态：`community_candidate`
- 来源定位：第 4.5 节后续方向与第 6 节实用技巧
- 原帖/精确回复：[CANopen 关节力控周期震荡的时序排查方法](https://zhuanlan.zhihu.com/p/2060484317202191732)
- 平台/作者：Zhihu / ATEMall发布
- 关键术语：总线负载（bus load）；看门狗（watchdog）；降级模式（degraded mode）
- 环境：CANopen；演示节点 NodeID=1；目标力矩 8 N·m；允许波动 ±5%；演示周期约 40 ms。
- 症状：TorqueActual 与 MotorCurrent 同时归零后弹回。；上位机台架出现周期性抽搐。
- 诊断：用 DBC 解码力矩、电流、StatusWord 和温度。；回到原始 CAN 帧检查缺帧，不把 UI 的填充值当总线原始值。；按时间窗口与报文 ID 检查 TPDO 周期。
- 原因：多个节点导致总线负载过高，TPDO 在固定相位周期丢失。；上位机把未收到反馈的拍误处理为零。
- 处理过程：同步观察力矩和电流排除单一力矩传感器漂移。；查看 StatusWord 和原始帧区分停机与丢帧。；建议调整 TPDO 周期、改 CAN-FD、拆分总线或对缺帧保持/插值。
- 结果：演示案例将定位范围收敛到周期丢帧；未提供真实产品修复后的复测数据。
- 限制：作者明确说明 DBC、信号数据和时间戳为演示性构造；工具仓库功能说明存在，但该案例结果不能当作真实独立复现。
- 安全提示：缺帧时不得无条件写零力矩或零位置；应使用经过安全评估的保持/插值/阻尼降级，并设置丢帧阈值和急停。
- 图片分析：正文表格给出 0.020/0.040/0.052 s 等演示时序；作者已注明为构造数据，因此只提炼排查流程，不把图表当真实测试证据。
- 独立核验引用：[source_code · README 声明支持 DBC 解码、按 ID/时间过滤、周期/负载率和错误帧分析；不验证帖子中的构造案例数据](https://github.com/ATEMall/can-log-analyzer)
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_comments
- 适用边界：适用于高频关节反馈闭环；安全策略需按机器人危险分析设计。

### 关节力矩与电流同时周期归零时，怎样快速缩小故障范围？

- `problem_id`：`problem.communication_realtime_control.24323df1c9aecb5a`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：CANopen 关节力控周期震荡的时序排查方法**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：先确认图上的零是原始帧值还是上位机在缺帧时的默认填充值；再把 TorqueActual 与 MotorCurrent 对齐。两者同时掉通常不支持单一力矩传感器漂移假设，应继续检查驱动状态和反馈帧是否存在。该帖使用构造数据演示，结论必须用目标系统原始日志复核。
- 证据状态：`community_candidate`
- 来源定位：第 4.3 节力矩/电流时序与填零说明
- 原帖/精确回复：[CANopen 关节力控周期震荡的时序排查方法](https://zhuanlan.zhihu.com/p/2060484317202191732)
- 平台/作者：Zhihu / ATEMall发布
- 关键术语：反馈帧（feedback frame）；默认填零（zero filling）；信号相关性（signal correlation）
- 环境：CANopen；演示节点 NodeID=1；目标力矩 8 N·m；允许波动 ±5%；演示周期约 40 ms。
- 症状：TorqueActual 与 MotorCurrent 同时归零后弹回。；上位机台架出现周期性抽搐。
- 诊断：用 DBC 解码力矩、电流、StatusWord 和温度。；回到原始 CAN 帧检查缺帧，不把 UI 的填充值当总线原始值。；按时间窗口与报文 ID 检查 TPDO 周期。
- 原因：多个节点导致总线负载过高，TPDO 在固定相位周期丢失。；上位机把未收到反馈的拍误处理为零。
- 处理过程：同步观察力矩和电流排除单一力矩传感器漂移。；查看 StatusWord 和原始帧区分停机与丢帧。；建议调整 TPDO 周期、改 CAN-FD、拆分总线或对缺帧保持/插值。
- 结果：演示案例将定位范围收敛到周期丢帧；未提供真实产品修复后的复测数据。
- 限制：作者明确说明 DBC、信号数据和时间戳为演示性构造；工具仓库功能说明存在，但该案例结果不能当作真实独立复现。
- 安全提示：缺帧时不得无条件写零力矩或零位置；应使用经过安全评估的保持/插值/阻尼降级，并设置丢帧阈值和急停。
- 图片分析：正文表格给出 0.020/0.040/0.052 s 等演示时序；作者已注明为构造数据，因此只提炼排查流程，不把图表当真实测试证据。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_comments
- 适用边界：适用于能同步采集电流、力矩与原始总线帧的关节台架。

### 如何用 StatusWord 和原始帧区分电机没出力与 CANopen TPDO 丢帧？

- `problem_id`：`problem.communication_realtime_control.7d9d352bb14053c8`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：CANopen 关节力控周期震荡的时序排查方法**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：在异常时间窗同时查看 TPDO1/TPDO2：如果对应帧缺失，而相邻帧的 StatusWord 仍保持运行使能，优先按通信缺帧排查；如果帧存在且状态字进入故障，再转向驱动器。关键是检查帧存在性，不能只看已经经过上位机补值的曲线。
- 证据状态：`community_candidate`
- 来源定位：第 4.4 节状态字与 TPDO 缺帧判断
- 原帖/精确回复：[CANopen 关节力控周期震荡的时序排查方法](https://zhuanlan.zhihu.com/p/2060484317202191732)
- 平台/作者：Zhihu / ATEMall发布
- 关键术语：状态字（StatusWord）；过程数据对象（TPDO）；报文存在性（frame presence）
- 环境：CANopen；演示节点 NodeID=1；目标力矩 8 N·m；允许波动 ±5%；演示周期约 40 ms。
- 症状：TorqueActual 与 MotorCurrent 同时归零后弹回。；上位机台架出现周期性抽搐。
- 诊断：用 DBC 解码力矩、电流、StatusWord 和温度。；回到原始 CAN 帧检查缺帧，不把 UI 的填充值当总线原始值。；按时间窗口与报文 ID 检查 TPDO 周期。
- 原因：多个节点导致总线负载过高，TPDO 在固定相位周期丢失。；上位机把未收到反馈的拍误处理为零。
- 处理过程：同步观察力矩和电流排除单一力矩传感器漂移。；查看 StatusWord 和原始帧区分停机与丢帧。；建议调整 TPDO 周期、改 CAN-FD、拆分总线或对缺帧保持/插值。
- 结果：演示案例将定位范围收敛到周期丢帧；未提供真实产品修复后的复测数据。
- 限制：作者明确说明 DBC、信号数据和时间戳为演示性构造；工具仓库功能说明存在，但该案例结果不能当作真实独立复现。
- 安全提示：缺帧时不得无条件写零力矩或零位置；应使用经过安全评估的保持/插值/阻尼降级，并设置丢帧阈值和急停。
- 图片分析：正文表格给出 0.020/0.040/0.052 s 等演示时序；作者已注明为构造数据，因此只提炼排查流程，不把图表当真实测试证据。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_comments
- 适用边界：适用于 CANopen TPDO 映射明确、能读取原始日志的系统。

## contact_force_friction (`contact_force_friction`)

### Newton 中 nconmax 增大后出现巨大虚假接触力，应如何定位？

- `problem_id`：`problem.contact_force_friction.ccbaeeadb7f07d95`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Newton CollisionPipeline 中 nconmax 增大触发虚假接触力**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：先用相同场景对比 nconmax 和 use_mujoco_contacts，确认问题是否来自 CollisionPipeline，而不是 WBC 本身。该 Issue 的修复已在 Newton PR #2112 合入 main；旧版本可临时切换 MuJoCo contacts，但不应只抬高 illegal_contact 阈值。
- 证据状态：`issue_candidate`
- 来源定位：修复合入确认 @camevor
- 原帖/精确回复：[Newton CollisionPipeline 中 nconmax 增大触发虚假接触力](https://github.com/isaac-sim/IsaacLab/issues/5069#issuecomment-4124618823)
- 平台/作者：GitHub Issues / rafaelcathomen
- 关键术语：接触力（Contact Force）；碰撞检测（Collision Detection）；全身控制（Whole-Body Control, WBC）
- 环境：Isaac Lab、Newton CollisionPipeline、MJWarpSolverCfg、Anymal-C 平地速度环境。
- 症状：nconmax≤16 时只有溢出警告；nconmax=32 时非法接触力达到异常数量级。
- 诊断：对比 use_mujoco_contacts 开关、nconmax 和 illegal_contact 阈值，隔离接触管线。
- 原因：CollisionPipeline 在较高接触容量下纳入了不应存在的接触。
- 处理过程：临时提高非法接触阈值，以及切换 use_mujoco_contacts=True。
- 有效处理：维护者指向 Newton PR #2112，并确认修复已合入 main。
- 结果：评论确认 main 分支已经包含修复。
- 限制：应记录实际 Newton/Isaac Lab 版本；旧发行版仍可能需要临时切换接触后端。
- 安全提示：不要仅通过提高非法接触阈值掩盖异常接触力后直接迁移到实机。
- 适用边界：适用于对应版本的 Newton/Isaac Lab CollisionPipeline；升级后仍应复现接触力尺度。

### Isaac Lab reset 后 ContactSensor 数据陈旧，应怎样处理？

- `problem_id`：`problem.contact_force_friction.e61af38c52293587`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab reset 后 ContactSensor 仍返回复位前数据**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先把它当作后端相关的已知时序问题，用逐帧最小复现确认首个有效接触样本。评论称 Newton 已有修复，而 PhysX 当时仍无通用绕行方案；因此应在 reset 后增加观测有效性检查，并按后端版本复测。
- 证据状态：`issue_candidate`
- 来源定位：后端状态更新 @ooctipus
- 原帖/精确回复：[Isaac Lab reset 后 ContactSensor 仍返回复位前数据](https://github.com/isaac-sim/IsaacLab/issues/4970#issuecomment-4190614556)
- 平台/作者：GitHub Issues / issue reporter
- 关键术语：接触传感器（Contact Sensor）；接触力（Contact Force）；状态估计（State Estimation）
- 环境：Isaac Lab ManagerBasedRLEnv、ContactSensor、reset 流程。
- 症状：复位后第一批接触观测不是新 episode 的状态。
- 诊断：用最小脚本在 reset 前后逐帧记录 net_forces_w，区分后端和传感器更新时序。
- 原因：传感器缓存和物理后端 reset/update 时序不同步。
- 处理过程：作者提供完整最小复现；评论对比 Newton 与 PhysX 状态。
- 有效处理：Newton 路径已有修复 PR；PhysX 路径在该评论时间点没有公认通用修复。
- 结果：问题仍为部分解决，后端不同导致可用方案不同。
- 限制：不能把 Newton 修复直接视为 PhysX 已修复；需按实际后端和版本复测。
- 安全提示：reset 后首帧接触观测应设有效性门槛，避免陈旧力触发错误控制或终止。
- 适用边界：适用于 reset 后立即读取 ContactSensor 的环境；Newton 与 PhysX 必须分开判断。

### IsaacLab ContactSensor 的世界系接触力如何转换到指尖或刚体局部系？

- `problem_id`：`problem.contact_force_friction.2a6475b059053f23`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ContactSensor 输出始终是世界系，局部力需要用刚体姿态自行旋转**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：原帖 contributor 明确说明 ContactSensor 总是返回世界系（world frame）接触力。要得到局部系，应先从 body_state_w、ContactSensor.track_pose 或 FrameTransformer 获得目标刚体相对世界的姿态，再用 isaaclab.utils.math 旋转力向量。FrameTransformer 本身只给位姿变换，不直接转换力。原线程未给出完整公式和复测，也未回答 get_measured_joint_forces 的坐标系，因此实现时必须用已知方向载荷验证。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1968，contributor 回复 issuecomment-2692423150
- 原帖/精确回复：[ContactSensor 输出始终是世界系，局部力需要用刚体姿态自行旋转](https://github.com/isaac-sim/IsaacLab/issues/1968#issuecomment-2692423150)
- 平台/作者：GitHub Issues / kbkartik
- 关键术语：世界坐标系（world frame）；刚体坐标系（body frame）；接触力（contact force）；坐标变换器（FrameTransformer）
- 环境：Isaac Lab ContactSensor；Shadow Hand 指尖；具体版本未说明。
- 症状：API 只直接提供世界系接触力，用户需要指尖局部系表达。
- 诊断：确认字段名后缀 _w 表示世界系；获取传感器刚体相对世界的姿态，再对力向量做坐标旋转。
- 处理过程：维护者建议用 math utilities；相对位姿可由 FrameTransformer、body_state_w 或 track_pose 提供。
- 结果：世界系输出和可用姿态来源得到 contributor 确认；精确变换代码和 joint force 坐标系问题没有在原线程闭环。
- 限制：原帖没有给出完整四元数方向、主动/被动旋转约定和复测；get_measured_joint_forces 的坐标系仍未回答。
- 安全提示：用于力控前必须用已知方向的测试力验证旋转方向和符号。
- 独立核验引用：[maintainer_confirmation · contributor 确认 ContactSensor 始终返回世界系力，并列出姿态来源](https://github.com/isaac-sim/IsaacLab/issues/1968#issuecomment-2692423150)
- 适用边界：适用于该线程版本的 IsaacLab ContactSensor 世界系字段；具体数学函数名和四元数约定需按目标版本核对。

### Isaac Lab 关节摩擦随机化违反 PhysX 动静摩擦约束

- `problem_id`：`problem.contact_force_friction.isaaclab_joint_friction_randomization_constraint_3266`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 随机化静摩擦时会违反 PhysX 动静摩擦约束**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：原实现只改 static friction，而分开的 setter 还会通过 set_dof_friction_properties 覆写整组属性，因此 static 可低于保留的 dynamic 值。已合并 PR #3318 同时处理静、动和黏性摩擦，将系数限制为非负并维持 dynamic≤static；审阅后的测试直接核对 PhysX buffer 而不只是 Isaac Lab 内部缓存。
- 证据状态：`issue_candidate`
- 来源定位：Isaac Lab #3266 最小复现与 issuecomment-3219603398/3219638763，已合并 PR #3318 及其 PhysX buffer 测试审阅链
- 原帖/精确回复：[Isaac Lab 随机化静摩擦时会违反 PhysX 动静摩擦约束](https://github.com/isaac-sim/IsaacLab/issues/3266#issuecomment-3242776016)
- 平台/作者：GitHub Issues / GiulioRomualdi
- 关键术语：域随机化（Domain Randomization, DR）；静摩擦（static friction）；库仑摩擦（Coulomb friction）；黏性摩擦（viscous friction）；回归测试（regression test）
- 环境：Isaac Lab commit 9d6321463067c541ce1a24531ff87f99a18fd8f7；Isaac Sim 5.0；Ubuntu 22.04；NVIDIA L40S；CUDA 12.4；driver 550.107.02。
- 症状：static friction=10、dynamic friction=10，对 static friction 使用 0.5–1.5 scale 随机化时，PhysX 报 Static friction effort must be greater than or equal to dynamic friction effort。
- 诊断：同时读取 static、dynamic 和 viscous 三类关节摩擦属性，不能只检查被随机化的 static 值。；检查连续调用 write_joint_friction_coefficient_to_sim 与 dynamic setter 时，set_dof_friction_properties 是否每次覆写整组 friction properties。
- 原因：原实现只随机化 static friction，没有保持 static≥dynamic；作者在评论中还确认了分别写入时的整组属性覆写问题。
- 处理过程：作者在 Issue 评论中提交一个同时生成 static/dynamic/viscous 数值、限制为非负并保持 dynamic≤static 的补丁。；PR #3318 经多轮审阅后修改测试，从只对照 Isaac Lab 内部 data 改为核对 root_physx_view 中实际写入的 buffer。
- 有效处理：使用包含已合并 PR #3318 的 Isaac Lab 版本，使关节参数随机化同时处理静摩擦、动摩擦（Coulomb friction）和黏性摩擦，并维持 static≥dynamic。
- 结果：PR #3318 于 2025-09-29 合并到 main；PR 页显示合并提交 21bcb47，Issue 同日以 completed 关闭。；最终 PR 勾选了测试、文档和 changelog，并在审阅中将摩擦断言改为对照 PhysX simulator buffer。
- 限制：初始提交的测试曾出现 CPU/CUDA device 不一致以及数值未写入 simulator 的失败；后续补丁对此进行修正。；PR 页合并时显示 13 项检查中 10 项通过，原页没有展示其余 3 项的具体状态；目标版本仍应运行摩擦 buffer 对照。；原 Issue 针对 Isaac Sim 5.0 的三类摩擦 API；更旧 Isaac Sim 的能力边界必须按对应版本处理。
- 安全提示：摩擦随机化范围还需与真实关节、润滑、温度和执行器特性对照；满足 PhysX 数学约束不等于参数具有物理真实性。
- 独立核验引用：[issue · 作者说明两个 friction setter 都会调用 set_dof_friction_properties 并覆写属性](https://github.com/isaac-sim/IsaacLab/issues/3266#issuecomment-3219603398)；[pull_request · 2025-09-29 已合并；审阅包含 static/dynamic/viscous 同时写入、约束处理与 PhysX buffer 测试](https://github.com/isaac-sim/IsaacLab/pull/3318)；[source_code · PR #3318 页显示的 main 合并提交](https://github.com/isaac-sim/IsaacLab/commit/21bcb47)；[source_code · 审阅后将 friction 断言改为核对 simulator/PhysX 中实际值的测试提交](https://github.com/isaac-sim/IsaacLab/commit/445f3b2)
- 适用边界：适用于 Isaac Sim 5.0 与相应 Isaac Lab 关节摩擦随机化路径；更旧版本不一定支持 dynamic/viscous 分开设置。

### TSID 的 CoP task 作为硬约束时仿真失稳

- `problem_id`：`problem.contact_force_friction.tsid_cop_level0_unresolved_131`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：TSID 接触力出现负值时先检查重复的足端运动等式约束**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索；尚未形成可核对的复现记录。
- 解答状态：`unresolved`
- 候选解答：没有。原作者在确认 level_foot=1 解决负接触力后，明确说 CoP task 作为 constraint 时机器人仍会消失，并询问是否有相似原因；后续只有贡献者建议关闭 Issue，没有给技术诊断、参数修改或复测。因此这不能被并入已解决的重复足端约束问题，只能保留为待复现线索。
- 证据状态：`issue_candidate`
- 来源定位：Issue #131，作者报告剩余 CoP constraint 问题 issuecomment-804237029；后续无技术回答
- 原帖/精确回复：[TSID 接触力出现负值时先检查重复的足端运动等式约束](https://github.com/stack-of-tasks/tsid/issues/131#issuecomment-804237029)
- 平台/作者：GitHub Issues / NahuelVilla
- 关键术语：压力中心（center of pressure, CoP）；硬约束（hard constraint）；求解器可行性（solver feasibility）；仿真失稳（simulation instability）
- 环境：2021 年 TSID Python 脚本；eiquadprog；双足接触；复现者使用 Ubuntu 16.04/Python 3.5 相关 robotpkg，但原作者系统版本未说明。
- 症状：脚在接触中但支撑需求较小时，求解结果出现负 ground contact force。；CoP task 放在 priority level 0 作为 constraint 时，机器人在脚本中直接消失或落下。
- 诊断：用 HQPData.print_all() 检查各 priority level 的 equality/inequality 任务。；协作者发现 level 0 同时含 task-right-foot 与 contact_rfoot_motion_task，并对左脚存在同类重复。
- 原因：eiquadprog 不能处理原 HQP 中重复的足端运动等式约束。；CoP constraint 的后续失败原因没有在原线程确认。
- 处理过程：协作者把 level_foot 设为 1 后复现问题消失；原作者随后采用同一调整。
- 有效处理：对原脚本，把重复的 foot motion task 从 level 0 移开，即设置 level_foot=1。
- 结果：原作者明确确认 level_foot=1 解决最初的负接触力问题。；CoP task 作为 constraint 时机器人消失的问题仍存在且没有答案。
- 限制：该修改只在原脚本和 eiquadprog 配置中确认，不能当作所有负接触力的通用修复。；线程没有给修改前后的接触力数值、求解器状态或 CoP constraint 的进一步诊断。；依赖导入问题的处理不能证明 WBC 约束已经正确。
- 安全提示：实体机器人使用前应独立验证 unilateral force、摩擦锥、CoP 和求解器可行性状态，不能只观察姿态。
- 独立核验引用：[issue · 作者明确区分已解决的负力问题与仍存在的 CoP constraint 失败](https://github.com/stack-of-tasks/tsid/issues/131#issuecomment-804237029)
- 适用边界：严格限于原作者同一 TSID 脚本中的 CoP priority-0 配置；环境、日志和求解器状态均不完整。

### TSID 冗余足端等式约束导致接触力异常

- `problem_id`：`problem.contact_force_friction.tsid_redundant_contact_equalities_131`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：TSID 接触力出现负值时先检查重复的足端运动等式约束**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：项目协作者打印 HQP，发现 level 0 同时存在 task-right-foot 和 contact_rfoot_motion_task，左脚也有同类重复；他指出 eiquadprog 不处理冗余 equality constraints。把 level_foot 设为 1 后，协作者复现中的问题消失，原作者也确认这解决了最初的负接触力问题。该结论只覆盖原脚本的重复约束，不能替代对摩擦锥、单侧力和其他求解器配置的检查。
- 证据状态：`issue_candidate`
- 来源定位：Issue #131，HQP 诊断 issuecomment-804188047；协作者复测 issuecomment-804190180；作者确认 issuecomment-804237029
- 原帖/精确回复：[TSID 接触力出现负值时先检查重复的足端运动等式约束](https://github.com/stack-of-tasks/tsid/issues/131#issuecomment-804237029)
- 平台/作者：GitHub Issues / NahuelVilla
- 关键术语：层级二次规划（hierarchical quadratic programming, HQP）；冗余等式约束（redundant equality constraint）；单侧接触力（unilateral contact force）；优先级层（priority level）
- 环境：2021 年 TSID Python 脚本；eiquadprog；双足接触；复现者使用 Ubuntu 16.04/Python 3.5 相关 robotpkg，但原作者系统版本未说明。
- 症状：脚在接触中但支撑需求较小时，求解结果出现负 ground contact force。；CoP task 放在 priority level 0 作为 constraint 时，机器人在脚本中直接消失或落下。
- 诊断：用 HQPData.print_all() 检查各 priority level 的 equality/inequality 任务。；协作者发现 level 0 同时含 task-right-foot 与 contact_rfoot_motion_task，并对左脚存在同类重复。
- 原因：eiquadprog 不能处理原 HQP 中重复的足端运动等式约束。；CoP constraint 的后续失败原因没有在原线程确认。
- 处理过程：协作者把 level_foot 设为 1 后复现问题消失；原作者随后采用同一调整。
- 有效处理：对原脚本，把重复的 foot motion task 从 level 0 移开，即设置 level_foot=1。
- 结果：原作者明确确认 level_foot=1 解决最初的负接触力问题。；CoP task 作为 constraint 时机器人消失的问题仍存在且没有答案。
- 限制：该修改只在原脚本和 eiquadprog 配置中确认，不能当作所有负接触力的通用修复。；线程没有给修改前后的接触力数值、求解器状态或 CoP constraint 的进一步诊断。；依赖导入问题的处理不能证明 WBC 约束已经正确。
- 安全提示：实体机器人使用前应独立验证 unilateral force、摩擦锥、CoP 和求解器可行性状态，不能只观察姿态。
- 独立核验引用：[maintainer_confirmation · 项目协作者从 HQP 输出定位重复足端运动等式约束](https://github.com/stack-of-tasks/tsid/issues/131#issuecomment-804188047)；[maintainer_confirmation · 项目协作者确认 level_foot=1 后复现问题消失](https://github.com/stack-of-tasks/tsid/issues/131#issuecomment-804190180)；[issue · 原作者确认该调整解决最初问题](https://github.com/stack-of-tasks/tsid/issues/131#issuecomment-804237029)
- 适用边界：适用于原帖 2021 年 TSID/eiquadprog 双足脚本及其 priority 配置；不同求解器和任务集合需重新打印 HQP。

### Pinocchio 足端力映射使用了错误的 Jacobian 参考系

- `problem_id`：`problem.contact_force_friction.pinocchio_foot_force_lwa_1292`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：从足端 Jacobian 估算接触力时不要把 WORLD 当作足端世界对齐坐标系**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：维护者指出，原帖的 WORLD Jacobian 以世界原点为作用点，好像该点附着于 LF_FOOT；它不是作者需要的足端中心量。LOCAL_WORLD_ALIGNED 则以 LF_FOOT frame 为中心、坐标轴与世界系对齐。作者改用 LOCAL_WORLD_ALIGNED 后确认力数值合理得多。原线程没有验证 3×3 截取、伪逆和 peak torque 映射的其余假设，所以只能确认参考系修正，不能把结果称为严格最大接触力。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1292，维护者参考系诊断 issuecomment-692582302；作者复测 issuecomment-692611643
- 原帖/精确回复：[从足端 Jacobian 估算接触力时不要把 WORLD 当作足端世界对齐坐标系](https://github.com/stack-of-tasks/pinocchio/issues/1292#issuecomment-692611643)
- 平台/作者：GitHub Issues / oliwiermelon
- 关键术语：局部世界对齐坐标系（local-world-aligned frame, LOCAL_WORLD_ALIGNED）；足端雅可比（foot-frame Jacobian）；接触力映射（contact-force mapping）；摩尔-彭若斯伪逆（Moore–Penrose pseudoinverse）
- 环境：2020 年 Pinocchio Python；FreeFlyer quadruped；q0 为单位 base quaternion；LF_FOOT Jacobian。
- 症状：使用 WORLD frame、截取 3×3 Jacobian 并对 J^T 做伪逆后，至少一个 x/y/z force 分量高一个数量级。
- 诊断：首先检查 Jacobian 的 reference frame 是否同时匹配所需作用点和坐标轴方向。
- 原因：WORLD 对应世界原点作用点，并不是以 LF_FOOT 为中心且 world-aligned 的足端坐标。
- 处理过程：作者把 computeFrameJacobian 的 reference frame 从 WORLD 改为 LOCAL_WORLD_ALIGNED。
- 有效处理：需要足端中心、世界轴对齐的接触力映射时，使用 LOCAL_WORLD_ALIGNED。
- 结果：作者确认修改 reference frame 后数值合理得多。
- 限制：线程没有证明 3×3 截取块可逆，也没有验证 pseudoinverse、其他腿耦合、浮动基平衡或摩擦约束。；数值更合理不等于已经计算出严格的 maximum feasible contact force。
- 安全提示：力矩限幅和接触可行域部署前必须在完整浮动基动力学与摩擦约束下复核。
- 独立核验引用：[maintainer_confirmation · 维护者解释 WORLD 作用点并建议 LOCAL_WORLD_ALIGNED](https://github.com/stack-of-tasks/pinocchio/issues/1292#issuecomment-692582302)；[issue · 原作者确认改用 LOCAL_WORLD_ALIGNED 后数值更合理](https://github.com/stack-of-tasks/pinocchio/issues/1292#issuecomment-692611643)
- 适用边界：适用于原帖 Pinocchio FreeFlyer quadruped 的 LF_FOOT 接触力坐标解释；其他 frame、作用点和力矩分配需单独建模。

### 手写 CRBA 接触方程与 Pinocchio RNEA 的精度和效率边界

- `problem_id`：`problem.contact_force_friction.pinocchio_manual_eom_vs_rnea_1650`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：把足端接触 wrench 送入 Pinocchio RNEA 时的父关节变换与多接触边界**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：线程参与者用质量矩阵、非线性项和各足 Jacobian 手写浮动基方程；原作者随后说该方法与直接 rnea 的结果非常接近。项目成员同时指出，这种手写组合没有利用运动树诱导的 sparsity，CRBA 的算法复杂度也高于 RNEA，因此把它作为常规逆动力学实现会很低效。原线程没有给误差或 benchmark，所以只能把它作为交叉检查路径，不能量化速度差或保证数值等价。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1650，实践者手写方法 issuecomment-1125218486；项目成员效率说明 issuecomment-1126962957；原作者结果对比 issuecomment-1129243412
- 原帖/精确回复：[把足端接触 wrench 送入 Pinocchio RNEA 时的父关节变换与多接触边界](https://github.com/stack-of-tasks/pinocchio/issues/1650#issuecomment-1129243412)
- 平台/作者：GitHub Issues / FenglongSong
- 关键术语：复合刚体算法（Composite Rigid Body Algorithm, CRBA）；非线性效应（nonlinear effects）；运动树稀疏性（kinematic-tree sparsity）；逆动力学（inverse dynamics）
- 环境：2022 年 Pinocchio C++；floating-base quadruped；foot-tip contact frames；作者最终采用 OCS2 commit 3566993 的 CentroidalModelRbdConversions.cpp。
- 症状：rnea 要求每个 joint 的 local-frame fext，但物理接触发生在没有 joint 的 foot-tip frame。；直接对 aligned_vector<Force> 调用 SE3 act 导致编译错误，提示 vector 没有 se3Action。
- 诊断：先找到 contact frame 的 parent joint 和两者相对 placement，再把 wrench 转到该 joint local frame。；区分单个 Force 元素与 model.njoints 长度的 force vector。；对比手写浮动基方程与 rnea 输出，并单独评估是否利用了 kinematic-tree sparsity。
- 原因：把 contact-frame force 直接放入 rnea，而没有转换作用点和局部表达。；错误地对整段 std::vector<Force> 调用 SE3 action。；手写 dense CRBA/Jacobian 运算没有利用 RNEA 的运动树递归稀疏结构。
- 处理过程：维护者建议 kMt.act(f_t)；作者随后采用 OCS2 固定提交中的 parent-joint force/wrench 构造。；另一参与者用 CRBA、nonLinearEffects 和 frame Jacobians 手写浮动基方程，原作者与 rnea 结果对比。；参与者讨论了单接触 re-root 与多接触 acceleration-level holonomic constraints 的求解边界。
- 有效处理：按 contact frame 的 parent joint 建立 fext 元素，把 world-frame force 旋转到 joint frame，并用 joint-to-contact translation×force 构造 moment；6D contact 再加 joint-frame contact torque。；把变换作用于单个 pinocchio::Force，而不是 aligned_vector<Force>。
- 结果：原作者确认采用所引 OCS2 代码后原问题解决。；原作者报告手写浮动基方程与 rnea 的结果非常接近，但没有给误差或速度基准。；多接触 QP/TSID 设计讨论没有在该线程提供实现复测。
- 限制：原作者引用的 OCS2 代码以特定 centroidal input 和 contact metadata 为前提，复制前必须核对自己的 frame parent、wrench 顺序和表达坐标。；线程没有提供 Pinocchio 具体 release、数值误差或运行时间测量。；关于 re-root、Schur complement 和 TSID 的多接触讨论是架构建议，不是该线程完成的实现。；原作者关于忽略 rnea 前六维的表述依赖其系统解释，线程没有把它验证为所有 floating-base robot 的通用操作。
- 安全提示：在实体机器人输出力矩前，应验证 fext 正负号、力矩参考点、frame transform 和未驱动基座动力学残差。
- 独立核验引用：[issue · 参与者给出 CRBA+nle+frame Jacobian 的手写路径](https://github.com/stack-of-tasks/pinocchio/issues/1650#issuecomment-1125218486)；[maintainer_confirmation · 项目成员说明该方法未利用 kinematic-tree sparsity 且比 RNEA 低效](https://github.com/stack-of-tasks/pinocchio/issues/1650#issuecomment-1126962957)；[issue · 原作者报告手写方法与 rnea 结果非常接近](https://github.com/stack-of-tasks/pinocchio/issues/1650#issuecomment-1129243412)
- 适用边界：适用于原帖 quadruped 的 inverse-dynamics 交叉检查；实时 WBC 是否可接受必须在目标维度和实现上 benchmark。

### 足端接触 frame 没有 joint 时构造 Pinocchio RNEA 外力

- `problem_id`：`problem.contact_force_friction.pinocchio_rnea_foot_wrench_1650`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：把足端接触 wrench 送入 Pinocchio RNEA 时的父关节变换与多接触边界**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：维护者先给出原则：若 kMt 是 tip frame 相对 knee joint frame 的 placement，则对单个 Force 使用 kMt.act(f_t)，不能对整段 vector<Force> 调用 act。原作者最终采用其明确引用的 OCS2 commit 3566993：找到 contact frame 的 parent joint，用 data.oMi\[jointIndex\].rotation().transpose() 把 world-frame force 旋转到 joint frame；linear 分量为该力，angular 分量为 joint-to-contact translation×force，6-DoF contact 还加旋转后的 contact torque，然后把 model.njoints 长度的 fext 传给 rnea。作者确认原问题解决。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1650，维护者变换原则 issuecomment-1123785731、单 Force 边界 issuecomment-1124949067；作者确认 issuecomment-1129243412、issuecomment-1189957188；OCS2 commit 3566993 lines 189–225
- 原帖/精确回复：[把足端接触 wrench 送入 Pinocchio RNEA 时的父关节变换与多接触边界](https://github.com/stack-of-tasks/pinocchio/issues/1650#issuecomment-1129243412)
- 平台/作者：GitHub Issues / FenglongSong
- 关键术语：递归牛顿-欧拉算法（Recursive Newton–Euler Algorithm, RNEA）；外部力旋量（external wrench）；父关节（parent joint）；空间力变换（spatial force transformation）
- 环境：2022 年 Pinocchio C++；floating-base quadruped；foot-tip contact frames；作者最终采用 OCS2 commit 3566993 的 CentroidalModelRbdConversions.cpp。
- 症状：rnea 要求每个 joint 的 local-frame fext，但物理接触发生在没有 joint 的 foot-tip frame。；直接对 aligned_vector<Force> 调用 SE3 act 导致编译错误，提示 vector 没有 se3Action。
- 诊断：先找到 contact frame 的 parent joint 和两者相对 placement，再把 wrench 转到该 joint local frame。；区分单个 Force 元素与 model.njoints 长度的 force vector。；对比手写浮动基方程与 rnea 输出，并单独评估是否利用了 kinematic-tree sparsity。
- 原因：把 contact-frame force 直接放入 rnea，而没有转换作用点和局部表达。；错误地对整段 std::vector<Force> 调用 SE3 action。；手写 dense CRBA/Jacobian 运算没有利用 RNEA 的运动树递归稀疏结构。
- 处理过程：维护者建议 kMt.act(f_t)；作者随后采用 OCS2 固定提交中的 parent-joint force/wrench 构造。；另一参与者用 CRBA、nonLinearEffects 和 frame Jacobians 手写浮动基方程，原作者与 rnea 结果对比。；参与者讨论了单接触 re-root 与多接触 acceleration-level holonomic constraints 的求解边界。
- 有效处理：按 contact frame 的 parent joint 建立 fext 元素，把 world-frame force 旋转到 joint frame，并用 joint-to-contact translation×force 构造 moment；6D contact 再加 joint-frame contact torque。；把变换作用于单个 pinocchio::Force，而不是 aligned_vector<Force>。
- 结果：原作者确认采用所引 OCS2 代码后原问题解决。；原作者报告手写浮动基方程与 rnea 的结果非常接近，但没有给误差或速度基准。；多接触 QP/TSID 设计讨论没有在该线程提供实现复测。
- 限制：原作者引用的 OCS2 代码以特定 centroidal input 和 contact metadata 为前提，复制前必须核对自己的 frame parent、wrench 顺序和表达坐标。；线程没有提供 Pinocchio 具体 release、数值误差或运行时间测量。；关于 re-root、Schur complement 和 TSID 的多接触讨论是架构建议，不是该线程完成的实现。；原作者关于忽略 rnea 前六维的表述依赖其系统解释，线程没有把它验证为所有 floating-base robot 的通用操作。
- 安全提示：在实体机器人输出力矩前，应验证 fext 正负号、力矩参考点、frame transform 和未驱动基座动力学残差。
- 独立核验引用：[maintainer_confirmation · 维护者给出 kMt.act(f_t) 的 joint-local force 变换原则](https://github.com/stack-of-tasks/pinocchio/issues/1650#issuecomment-1123785731)；[issue · 原作者确认问题解决并指向 OCS2 RNEA quadruped 示例](https://github.com/stack-of-tasks/pinocchio/issues/1650#issuecomment-1129243412)；[source_code · 原作者引用的固定提交逐项构造 parent-joint local fext 并调用 rnea](https://github.com/leggedrobotics/ocs2/blob/3566993b9fc5162f4c57ccb6f3d93aab92c5c2b1/ocs2_pinocchio/ocs2_centroidal_model/src/CentroidalModelRbdConversions.cpp#L189-L225)
- 适用边界：适用于原帖 floating-base quadruped、foot contact frame 及原作者引用的 OCS2 3566993 实现；其他 contact metadata 和 wrench convention 必须重核。

### 简单重设 RNEA 根节点不能处理多个接触约束

- `problem_id`：`problem.contact_force_friction.pinocchio_rnea_multicontact_boundary_1650`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：把足端接触 wrench 送入 Pinocchio RNEA 时的父关节变换与多接触边界**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：项目成员说明，把系统 root 人工放到单个 contact point 可以使用 RNEA，但一个系统只有一个 root，因此不能用这一办法同时处理多个 contact；而且该做法限制极强。多个 acceleration-based holonomic constraints 应通过 TSID 或通用 QP 等优化来施加，线程还提到 Schur-complement 路径和利用惯性矩阵/接触 Jacobian 结构。原线程没有实现或复测这些方案，所以它是架构边界，不是可直接复制的多接触控制器。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1650，项目成员关于单 root、多接触和 QP/TSID 的说明 issuecomment-1127623596
- 原帖/精确回复：[把足端接触 wrench 送入 Pinocchio RNEA 时的父关节变换与多接触边界](https://github.com/stack-of-tasks/pinocchio/issues/1650#issuecomment-1127623596)
- 平台/作者：GitHub Issues / FenglongSong
- 关键术语：完整约束（holonomic constraint）；多接触（multi-contact）；舒尔补（Schur complement）；任务空间逆动力学（Task-Space Inverse Dynamics, TSID）
- 环境：2022 年 Pinocchio C++；floating-base quadruped；foot-tip contact frames；作者最终采用 OCS2 commit 3566993 的 CentroidalModelRbdConversions.cpp。
- 症状：rnea 要求每个 joint 的 local-frame fext，但物理接触发生在没有 joint 的 foot-tip frame。；直接对 aligned_vector<Force> 调用 SE3 act 导致编译错误，提示 vector 没有 se3Action。
- 诊断：先找到 contact frame 的 parent joint 和两者相对 placement，再把 wrench 转到该 joint local frame。；区分单个 Force 元素与 model.njoints 长度的 force vector。；对比手写浮动基方程与 rnea 输出，并单独评估是否利用了 kinematic-tree sparsity。
- 原因：把 contact-frame force 直接放入 rnea，而没有转换作用点和局部表达。；错误地对整段 std::vector<Force> 调用 SE3 action。；手写 dense CRBA/Jacobian 运算没有利用 RNEA 的运动树递归稀疏结构。
- 处理过程：维护者建议 kMt.act(f_t)；作者随后采用 OCS2 固定提交中的 parent-joint force/wrench 构造。；另一参与者用 CRBA、nonLinearEffects 和 frame Jacobians 手写浮动基方程，原作者与 rnea 结果对比。；参与者讨论了单接触 re-root 与多接触 acceleration-level holonomic constraints 的求解边界。
- 有效处理：按 contact frame 的 parent joint 建立 fext 元素，把 world-frame force 旋转到 joint frame，并用 joint-to-contact translation×force 构造 moment；6D contact 再加 joint-frame contact torque。；把变换作用于单个 pinocchio::Force，而不是 aligned_vector<Force>。
- 结果：原作者确认采用所引 OCS2 代码后原问题解决。；原作者报告手写浮动基方程与 rnea 的结果非常接近，但没有给误差或速度基准。；多接触 QP/TSID 设计讨论没有在该线程提供实现复测。
- 限制：原作者引用的 OCS2 代码以特定 centroidal input 和 contact metadata 为前提，复制前必须核对自己的 frame parent、wrench 顺序和表达坐标。；线程没有提供 Pinocchio 具体 release、数值误差或运行时间测量。；关于 re-root、Schur complement 和 TSID 的多接触讨论是架构建议，不是该线程完成的实现。；原作者关于忽略 rnea 前六维的表述依赖其系统解释，线程没有把它验证为所有 floating-base robot 的通用操作。
- 安全提示：在实体机器人输出力矩前，应验证 fext 正负号、力矩参考点、frame transform 和未驱动基座动力学残差。
- 独立核验引用：[maintainer_confirmation · 项目成员说明单 root 限制，并给出 TSID/QP/Schur-complement 架构方向](https://github.com/stack-of-tasks/pinocchio/issues/1650#issuecomment-1127623596)
- 适用边界：适用于需要同时满足多个加速度级 holonomic contacts 的 floating-base WBC 设计；求解器实现与稳定性未在该线程验证。

### MuJoCo 夹持力充足但物体仍缓慢下滑时，noslip_iterations 在原帖中有什么实测作用？

- `problem_id`：`problem.contact_force_friction.37d4dea7eb784f2c`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo 正则化摩擦在抓持中产生稳定爬移**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：在 MuJoCo 3.8.1 的 45 g capsule 最小复现里，默认 elliptic/impratio=10 的下滑约为 155 µm/s；设置 noslip_iterations=10 后降至约 1.41 µm/s，约 110 倍改善。维护者确认这种正则化摩擦爬移是预期行为。该参数只在此 MRE 有量化结果，不能据此承诺其他抓取任务完全静止。
- 证据状态：`issue_candidate`
- 来源定位：Issue #3328 Summary/Observed/Analysis；维护者回复 issuecomment-4735966682
- 原帖/精确回复：[MuJoCo 正则化摩擦在抓持中产生稳定爬移](https://github.com/google-deepmind/mujoco/issues/3328#issuecomment-4735966682)
- 平台/作者：GitHub Issues / RLRK-dev
- 关键术语：正则化摩擦（regularized friction）；防滑迭代（noslip iterations）；切向爬移（tangential creep）
- 环境：MuJoCo 3.8.1；Python 3.12；Linux x86_64 CPU；45 g capsule；µ=0.7；timestep=0.002。
- 症状：默认 elliptic/impratio=10 下约 155 µm/s 稳态爬移；impratio=1 或 pyramidal 更快。
- 诊断：测量下落速度、法向力与转动，排除滚动和夹爪 z 运动。；分别扫描 cone、impratio、condim、solref 与 noslip_iterations。
- 原因：帖子把现象归因于正则化摩擦在原点附近的有限切向力—滑移速度映射；维护者确认行为符合预期。
- 处理过程：提高 impratio。；设置 noslip_iterations=10。；改变 cone、condim 和 solref。
- 结果：noslip_iterations=10 在该 MRE 中把爬移约降低 110 倍；维护者确认现象为预期行为，但没有给出通用参数建议。
- 限制：单一最小夹持模型；数值和缩放关系不能直接外推到其他几何、质量、时间步或大规模并行环境。
- 独立核验引用：[maintainer_confirmation · MuJoCo 协作者确认该行为 WAI，并建议改进文档](https://github.com/google-deepmind/mujoco/issues/3328#issuecomment-4735966682)
- 适用边界：MuJoCo 3.8.1 的正则化摩擦抓持模型；其他模型需重新测量爬移预算。

## debugging_logging_reproducibility (`debugging_logging_reproducibility`)

### 自定义 USD 地形使两台相同 GPU 的人形训练结果严重分歧时，能否直接归因于驱动？

- `problem_id`：`problem.debugging_logging_reproducibility.c68ffe084b877e7d`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：相同 RTX 4090 与容器下自定义 USD 地形训练不可复现**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：不能。维护者最初要求对齐驱动，但后续根据约两千步前结果相近、之后才分叉，认为它不像单纯驱动问题。当前应把主机驱动、该步附近的课程触发、自定义地形接触表示和 PVD 日志并列排查，原帖仍未给出最终根因。
- 证据状态：`issue_candidate`
- 来源定位：维护者最新调查回复 @RandomOakForest
- 原帖/精确回复：[相同 RTX 4090 与容器下自定义 USD 地形训练不可复现](https://github.com/isaac-sim/IsaacLab/issues/4599#issuecomment-3999339297)
- 平台/作者：GitHub Issues / githubLeoliu
- 关键术语：训练非确定性（Training Nondeterminism）；全身控制（Whole-Body Control, WBC）；物理可视化调试器（Physics Visual Debugger, PVD）
- 环境：Isaac Lab 2.1、Isaac Sim 4.5、RTX 4090、whole_body_tracking、自定义 USD 地形。
- 症状：本地能学会 mimic，云端机器人甚至无法站立；默认平面和内置地形生成器不触发。
- 诊断：对齐主机驱动，比较多随机种子分布，并检查约两千步附近是否有课程或条件触发；保留 PVD 记录。
- 原因：自定义地形表示可能改变接触建模或接触求解，但维护者尚未确认根因。
- 处理过程：作者比较默认平面、内置地形和自定义 USD，并记录前一百次迭代的 PVD。
- 结果：维护者仍在调查，尚无可验证最终修复。
- 限制：该 Issue 不能证明驱动版本或自定义地形就是根因，只能确定它们是排查变量。
- 安全提示：不要用单次训练曲线判断部署可靠性，应比较多种子统计和最终任务指标。
- 图片分析：Issue 的训练曲线比较图用于显示两台机器后期分叉；本轮未逐像素读取坐标值，时间点判断来自维护者对约两千步附近分叉的文字分析。
- 适用边界：适用于跨机器接触丰富型训练复现；不能外推为所有 Isaac Lab 训练都不可复现。

### 跨机器训练只有加入 net_forces_w 后才分叉，这个现象怎样利用？

- `problem_id`：`problem.debugging_logging_reproducibility.9ed592cd62bb0b48`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：G1 训练在不同电脑完全一致但加入 net_forces_w 后分叉**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：把它当作字段级消融证据：先对齐版本、驱动、后端和并行环境数，再逐项比较 net_forces_w 与其历史缓存进入观测或奖励后的首个分叉时刻。它能缩小非确定性入口，但原帖尚未证明底层根因。
- 证据状态：`issue_candidate`
- 来源定位：维护者解释 @RandomOakForest
- 原帖/精确回复：[G1 训练在不同电脑完全一致但加入 net_forces_w 后分叉](https://github.com/isaac-sim/IsaacLab/issues/4545#issuecomment-3861646985)
- 平台/作者：GitHub Issues / issue reporter
- 关键术语：训练非确定性（Training Nondeterminism）；接触力（Contact Force）；强化学习（Reinforcement Learning, RL）
- 环境：Isaac Lab 2.3.1、Isaac Sim 5.1.0、RSL-RL、Unitree G1。
- 症状：net_forces_w 触发差异，net_forces_w_history 不触发。
- 诊断：逐项切换观测/奖励字段，用第一个产生分叉的字段定位非确定性输入。
- 原因：即时接触力路径可能包含物理求解顺序相关的非确定性。
- 处理过程：作者对比即时接触力与历史缓存进入奖励/观测的行为。
- 有效处理：尚无根因修复；可先把字段级消融作为复现诊断方法。
- 结果：维护者给出解释和进一步排查方向，但没有确认具体底层缺陷。
- 限制：完全一致或不一致本身都不是错误证明，必须对齐版本、驱动、后端、环境数和代码。
- 适用边界：适用于 Isaac Lab/RSL-RL 接触丰富型训练的复现诊断。

## dynamics_mass_inertia_actuation (`dynamics_mass_inertia_actuation`)

### Crocoddyl 中质心代价不生效且共享 Jcom 为零，是缓存错误吗？

- `problem_id`：`problem.dynamics_mass_inertia_actuation.82654b27d8cd4fe9`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Crocoddyl 自由动力学中质心代价不生效且 Jcom 为零**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：在该 Issue 使用的自由前向动力学模型中不是缓存错误：维护者说明该模型按设计不更新全身质心信息，因此共享 com 与 Jcom 保持零。应先换用与接触/质心任务匹配的 action model，或显式计算并评估实时开销。
- 证据状态：`issue_candidate`
- 来源定位：维护者回复 @cmastalli
- 原帖/精确回复：[Crocoddyl 自由动力学中质心代价不生效且 Jcom 为零](https://github.com/loco-3d/crocoddyl/issues/914#issuecomment-782208702)
- 平台/作者：GitHub Issues / amirrazmjoo
- 关键术语：质心（Center of Mass, CoM）；雅可比矩阵（Jacobian Matrix）；前向动力学（Forward Dynamics）
- 环境：Crocoddyl DifferentialActionModelFreeFwdDynamics 与 Pinocchio 共享数据。
- 症状：data.shared.pinocchio.com\[0\] 和 Jcom 均为零；手动调用质心函数后生效但变慢。
- 诊断：先确认当前 differential action model 是否按设计更新全身质心数据。
- 原因：自由动力学模型默认不更新全身质心信息。
- 处理过程：用户在 cost 中直接调用 centerOfMass 和 jacobianCenterOfMass。
- 有效处理：根据任务动机选择会更新所需共享数据的模型，或显式计算并接受额外成本。
- 结果：维护者说明设计边界后，原作者确认问题得到解释并关闭 Issue。
- 限制：维护者同时质疑在无接触自由动力学中控制全身质心的物理动机；不能把该解释外推到接触动力学模型。
- 适用边界：适用于 DifferentialActionModelFreeFwdDynamics；接触模型与新版行为需另查。

## dynamics_model_validation (`dynamics_model_validation`)

### Pinocchio 浮动基 RNEA 的速度交叉项

- `problem_id`：`problem.dynamics_model_validation.pinocchio_freeflyer_rnea_velocity_cross_term_1977`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 浮动基 RNEA 中的速度交叉项与中性构型**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：项目贡献者明确回复，\[0,-1,0\] 是 Coriolis/Centrifugal 效应，可用 pin.computeCoriolisMatrix(model, data, q, qd) @ qd 单独计算对照。free-flyer 的配置不应全零，应用 pin.neutral(model) 保证四元数归一化；贡献者用 neutral 构型仍重现相同交叉项，因此它不是全零 q 单独造成。原帖对“换成转动关节速度后交叉项消失”的追问没有答复，所以保留为部分解答。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1977；Coriolis/centrifugal 解释 issuecomment-1571030718；neutral 构型与重现 issuecomment-1571032033
- 原帖/精确回复：[Pinocchio 浮动基 RNEA 中的速度交叉项与中性构型](https://github.com/stack-of-tasks/pinocchio/issues/1977#issuecomment-1571030718)
- 平台/作者：GitHub Issues / dsami2
- 关键术语：递归牛顿-欧拉算法（Recursive Newton-Euler Algorithm, RNEA）；科里奥利/离心效应（Coriolis/Centrifugal effects）；中性构型（neutral configuration）；浮动基（free flyer）
- 环境：Pinocchio Python API，buildModelFromUrdf(..., JointModelFreeFlyer())，1 kg 点质量模型；版本、操作系统与硬件未说明。
- 症状：qd=\[0,0,1,1,0,0\]、qdd=0 时，RNEA 返回 \[0,-1,9.81,0,0,0\]；无速度或仅 z 向线速度时没有 y=-1 项。；把 x 向角速度改成新增转动关节的速度后，原作者的追加例子中交叉项消失。
- 诊断：按项目贡献者回复，用 pin.computeCoriolisMatrix(model, data, q, qd) @ qd 单独计算速度相关偏置项，与 RNEA 额外项对照。；用 pin.neutral(model) 初始化 free-flyer 构型，避免全零四元数未归一化。
- 原因：项目贡献者明确该 \[0,-1,0\] 来自科里奥利/离心（Coriolis/Centrifugal）效应。
- 处理过程：原作者用三组 qd 输出对照偏置项，又用增加一个转动自由度的模型做了追加对照。；项目贡献者把原代码中的 q=0 替换为 pin.neutral(model)，并重现相同的 y=-1 输出。
- 有效处理：这不是需要删除的数值错误；将该项识别为 Coriolis/centrifugal 速度偏置，并使用 pin.neutral(model) 初始化有效 free-flyer 构型。
- 结果：项目贡献者给出了交叉项的分类和可单独计算路径，并用 neutral 构型重现原输出。
- 限制：原作者没有回复是否验证 computeCoriolisMatrix @ qd 与该项一致。；追加的转动关节模型为什么不再出现同样交叉项，线程没有给出解释，本卡不自行推断。；线程未说明 Pinocchio 版本，也没有把最小例子延伸到具体人形机器人的 WBC 数值。
- 独立核验引用：[maintainer_confirmation · 项目贡献者将 \[0,-1,0\] 归因于 Coriolis/Centrifugal 效应，并给出 computeCoriolisMatrix @ qd 对照方法](https://github.com/stack-of-tasks/pinocchio/issues/1977#issuecomment-1571030718)；[maintainer_confirmation · 项目贡献者提醒使用 pin.neutral(model)，并在 neutral 构型下重现相同输出](https://github.com/stack-of-tasks/pinocchio/issues/1977#issuecomment-1571032033)；[issue · 原作者的转动关节对照例子中交叉项消失，但该追问未获回复](https://github.com/stack-of-tasks/pinocchio/issues/1977#issuecomment-1571009804)
- 适用边界：适用于 Pinocchio free-flyer 最小模型中速度相关 RNEA 偏置项的识别；版本未说明，具体人形模型需独立核对。

## hardware_actuator_thermal_power (`hardware_actuator_thermal_power`)

### Isaac Lab 中怎样读取 ImplicitDrive 实际产生的关节力矩？

- `problem_id`：`problem.hardware_actuator_thermal_power.2d11e2e56733ba5a`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 无法直接读取 ImplicitDrive 的纯 PD 输出力矩**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：如果需要每步净关节力矩，应启用关节力传感器并读取 measured joint forces；维护者同时说明，当前 API 不提供把纯 ImplicitDrive PD 输出从接触和其他约束项中单独分离的量，因此日志字段必须明确其物理语义。
- 证据状态：`issue_candidate`
- 来源定位：维护者回复 @RandomOakForest
- 原帖/精确回复：[Isaac Lab 无法直接读取 ImplicitDrive 的纯 PD 输出力矩](https://github.com/isaac-sim/IsaacLab/issues/4136#issuecomment-3619337205)
- 平台/作者：GitHub Issues / issue reporter
- 关键术语：比例微分控制（Proportional-Derivative Control, PD）；关节力矩（Joint Torque）；力传感器（Force Sensor）
- 环境：Isaac Sim/Isaac Lab、Humanoid、ImplicitDrive、关节力传感器。
- 症状：反力可读取，但与期望的驱动器内部输出不是同一物理量。
- 诊断：先明确需要的是净关节力矩、关节反力还是 drive-only PD 力矩。
- 原因：接口语义不同：get_dof_actuation_forces 不代表内部 ImplicitDrive 输出。
- 处理过程：作者尝试 actuation forces 和 incoming joint force 接口。
- 有效处理：需要净关节力矩时启用 DOF force sensors，并读取 measured joint forces。
- 结果：纯 PD 输出仍没有独立公开 API；只能获取包含约束影响的净测量量。
- 限制：净关节力矩不能直接替代内部 PD 输出用于精确控制器分解。
- 安全提示：执行器保护逻辑必须标清使用的是命令、估计还是测量净力矩。
- 适用边界：适用于该 Issue 对应的 Isaac Sim/Isaac Lab 接口；API 版本更新后需复核。

### Isaac Lab 的 ImplicitActuatorCfg.effort_limit 应使用 N 还是 N·m？

- `problem_id`：`problem.hardware_actuator_thermal_power.5cb6eaa1ded58848`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ImplicitActuatorCfg 的 effort_limit 单位取决于关节类型**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原帖的 IsaacLab contributor 给出的规则是：移动关节（prismatic joint）产生线性力，单位为 N；转动关节（revolute joint）产生力矩，单位为 N·m。不能先统一按 N 填写后再自行用臂长换算。原帖没有覆盖不同 Isaac Lab 版本中 effort_limit 与 effort_limit_sim 的行为差异，因此配置时仍需核对目标版本。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1523，contributor 回复 issuecomment-2539834819；提问者确认 issuecomment-2540293139
- 原帖/精确回复：[ImplicitActuatorCfg 的 effort_limit 单位取决于关节类型](https://github.com/isaac-sim/IsaacLab/issues/1523#issuecomment-2539834819)
- 平台/作者：GitHub Issues / H-Hisamichi
- 关键术语：移动关节（prismatic joint）；转动关节（revolute joint）；力上限（effort limit）；关节力矩（joint torque）
- 环境：Isaac Lab ImplicitActuatorCfg/ArticulationCfg；具体软件版本和机器人未说明。
- 症状：配置接口没有让提问者明确区分移动关节与转动关节的 effort 单位。
- 诊断：先识别关节是移动关节还是转动关节，并确认执行器输出是线性力还是关节力矩。
- 处理过程：提问者在 contributor 回复后表示会把其转动关节参数按 N·m 设置。
- 有效处理：移动关节（prismatic joint）的 effort_limit 用 N；转动关节（revolute joint）的 effort_limit 用 N·m。
- 结果：提问者接受该解释并关闭问题；没有提供运行复测或具体数值。
- 限制：原帖没有说明 Isaac Lab 版本、关节资产单位缩放或实际配置值，也没有讨论 effort_limit 与 effort_limit_sim 的版本差异。
- 安全提示：力/力矩上限直接影响执行器保护与控制饱和，迁移到实机前必须再核对机器人厂商额定值和所用 Isaac Lab 版本。
- 独立核验引用：[maintainer_confirmation · IsaacLab contributor 区分移动关节 N 与转动关节 N·m](https://github.com/isaac-sim/IsaacLab/issues/1523#issuecomment-2539834819)
- 适用边界：适用于 Isaac Lab 关节执行器配置中的 effort 物理量；具体字段是否写入仿真求解器仍取决于版本和执行器类型。

### root_physx_view 调用 get_measured_joint_efforts 报 AttributeError 时，应该怎样选择正确 API？

- `problem_id`：`problem.hardware_actuator_thermal_power.9c92734950398cc2`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：get_measured_joint_efforts 属于高层 Articulation API，不存在于 root_physx_view**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：先不要把不同层级的方法混用：原帖 contributor 说明 get_measured_joint_efforts 属于 Isaac Sim 高层 Articulation 类，而 root_physx_view 暴露的是 physics tensor API。底层可读取 get_link_incoming_joint_force，但它是每个 DOF 的 6D 入射 wrench；提问者认为自己需要 get_dof_projected_joint_forces 和 get_dof_actuation_forces，却没有完成测试。因此可用这些名称作为排查入口，但不能把它们写成已验证的外力隔离方案。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2630 回复 issuecomment-2944927705 与 2945622792
- 原帖/精确回复：[get_measured_joint_efforts 属于高层 Articulation API，不存在于 root_physx_view](https://github.com/isaac-sim/IsaacLab/issues/2630#issuecomment-2944927705)
- 平台/作者：GitHub Issues / lorepieri8
- 关键术语：关节力（joint effort）；物理张量接口（physics tensor API）；入射关节力（incoming joint force）；自由度投影力（DOF projected force）
- 环境：IsaacLab Articulation/root_physx_view；具体 Isaac Lab/Sim 版本和机器人未说明。
- 症状：AttributeError: 'ArticulationView' object has no attribute 'get_measured_joint_efforts'。
- 诊断：先区分 Isaac Sim 高层 Articulation 类 API 与底层 physics tensor ArticulationView API；再明确需要 6D 入射 wrench、DOF 投影外力还是执行器力。
- 原因：在底层 root_physx_view 上调用了只属于 Isaac Sim 高层 Articulation 类的方法。
- 处理过程：Contributor 建议 get_link_incoming_joint_force；提问者进一步找到 get_dof_projected_joint_forces 和 get_dof_actuation_forces。
- 结果：API 层级错误得到确认；提问者认为 DOF projected/actuation forces 可能合用，但承诺测试后没有回报。
- 限制：原线程没有验证 get_dof_projected_joint_forces 是否等于目标外力，也没有明确各项是否包含约束反力、驱动力或符号约定。
- 安全提示：用于执行器保护或接触检测前，必须用已知载荷分别验证投影外力与驱动力。
- 独立核验引用：[maintainer_confirmation · contributor 明确区分高层 Articulation API 与 root_physx_view tensor API](https://github.com/isaac-sim/IsaacLab/issues/2630#issuecomment-2944927705)
- 适用边界：适用于区分 Isaac Sim 高层 Articulation API 与 IsaacLab root_physx_view tensor API；具体方法随版本可能变化。

### Isaac Lab 关节力矩越界终止谓词颠倒

- `problem_id`：`problem.hardware_actuator_thermal_power.isaaclab_joint_effort_limit_predicate_inverted_3155`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 关节力矩越界终止条件真假颠倒**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：旧实现把 torch.isclose(computed_torque, applied_torque) 直接当作越界标志，逻辑正好相反：两者相等表示没有裁剪，不等才表示 clipping。已合并 PR #3163 改为 ~torch.isclose，并用 CPU/CUDA、1/2 个 Panda articulation 的回归测试覆盖 0/0 与 100/50 两种情形。该检测器只识别 computed/applied torque 的差异，不能替代真实执行器限定或硬件安全保护。
- 证据状态：`issue_candidate`
- 来源定位：Isaac Lab #3155 正文真值表复现；作者回复 issuecomment-3179329133；已合并 PR #3163、回归测试与 0.45.3 changelog
- 原帖/精确回复：[Isaac Lab 关节力矩越界终止条件真假颠倒](https://github.com/isaac-sim/IsaacLab/issues/3155)
- 平台/作者：GitHub Issues / Maurice Rahme
- 关键术语：力矩裁剪（torque clipping）；计算力矩（computed torque）；应用力矩（applied torque）；终止谓词（termination predicate）；回归测试（regression test）
- 环境：Isaac Lab commit b5d094e5de0d35d0f6f87a0709394cbe230159d9（feature/isaacsim_5_0）；Isaac Sim 5.0；Ubuntu 22.04；RTX 5080；CUDA 12.8；GPU driver 570.144。；PR #3163 回归测试参数化覆盖 CPU 和 cuda:0、1 与 2 个 Panda articulation。
- 症状：computed_torque == applied_torque == 0 时，本应不终止，旧逻辑却返回 True。；computed_torque=100、applied_torque=50 模拟 actuator clipping 时，本应终止，旧逻辑却返回 False。
- 诊断：用无裁剪和有裁剪两组真值表检查终止谓词，不要仅从函数名猜测语义。；同时打印 computed_torque、applied_torque 和终止布尔值，确认不等是否来自 actuator clipping。
- 原因：旧实现直接把 torch.isclose 的结果当作 out_of_limits，但在该函数的定义中，相等恰好表示没有裁剪。
- 处理过程：原帖提供单关节最小复现和两个断言。；PR #3163 反转 isclose 结果，并加入 CPU/CUDA 下的两个回归用例。
- 有效处理：使用已合并 PR #3163：out_of_limits = ~torch.isclose(computed_torque, applied_torque)，再对关节维度执行 any。
- 结果：PR #3163 于 2025-08-21 合并，合并提交为 a60168a2dc0b7f56f76b8985d0bca2e79a4e5ef6；0.45.3 changelog 明确记录修复颠倒的 effort-limit 报告。；回归测试验证 0/0 不终止，100/50 终止。
- 限制：该函数判断的是 computed 与 applied torque 是否因裁剪而不同，不会验证配置的 effort limit 是否符合真实电机、减速器和热限制。；比较仍使用 torch.isclose 的默认容差；微小差异的分类取决于该容差。；PR 测试通过直接填充 computed/applied 缓冲来模拟 clipping，不是真实电机或物理执行器裁剪实验。
- 安全提示：真机 WBC 不应把该软件谓词当作唯一力矩安全链；仍需硬件限流、热保护与独立急停。
- 独立核验引用：[pull_request · 已合并 PR 反转 isclose 结果，更新 docstring/changelog，并新增 CPU/CUDA 回归测试](https://github.com/isaac-sim/IsaacLab/pull/3163)；[source_code · PR #3163 合并提交](https://github.com/isaac-sim/IsaacLab/commit/a60168a2dc0b7f56f76b8985d0bca2e79a4e5ef6)；[source_code · test_joint_effort_limits 在 CPU/CUDA 和 1/2 articulation 下验证无裁剪与模拟裁剪两种真值表](https://github.com/isaac-sim/IsaacLab/pull/3163/files)
- 适用边界：适用于使用 Isaac Lab joint_effort_out_of_limit 比较 computed/applied torque 的版本；原帖环境为 Isaac Sim 5.0 功能分支。

### Isaac Lab 隐式执行器未继承 USD 力矩上限

- `problem_id`：`problem.hardware_actuator_thermal_power.isaaclab_implicit_actuator_usd_effort_limit_2054`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 隐式执行器未继承 USD 关节力矩上限**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：#2054 的复现是在 effort_limit_sim/effort_limit 都未显式设置时出现。合并 PR #2098 表明，旧代码在 ActuatorBase 中错用 ActuatorBase.is_implicit_model 做判断，使隐式执行器走到显式执行器的 1e9 默认分支。修复改为 self.is_implicit_model，未显式配置时保留 USD/PhysX max effort，最终补丁也核对了该默认路径。升级前可在机器人配置里显式填写经硬件核实的上限，但不能用 1e9 作为真机保护。
- 证据状态：`issue_candidate`
- 来源定位：Isaac Lab #2054 正文、USD Max Force=88.0 截图、issuecomment-2721483228 的 G1 复现、issuecomment-2723958505 的独立现象与已合并 PR #2098
- 原帖/精确回复：[Isaac Lab 隐式执行器未继承 USD 关节力矩上限](https://github.com/isaac-sim/IsaacLab/issues/2054)
- 平台/作者：GitHub Issues / Hellod035
- 关键术语：隐式执行器（implicit actuator）；关节力矩上限（joint effort limit）；默认继承（default inheritance）；回归测试（regression test）
- 环境：Isaac Sim 4.5；Ubuntu 22.04；RTX 4090D；CUDA 12.4；GPU driver 550.144.03；Issue 标注 Isaac Lab Latest。；作者用 Isaac-Velocity-Flat-G1-v0 和 Legged_Lab g1_flat，在注释 effort_limit 或 effort_limit_sim 后复现。
- 症状：原帖截图中 USD Drive > Angular 显示 Type=force、Max Force=88.0，文字同时记录 robot.data.joint_effort_limits=1e9。；另一名使用者回复力矩上限没有从 Isaac Sim 读取，但速度上限能读取。
- 诊断：在同一 asset 上并列记录 USD Drive Max Force、root_physx_view.get_dof_max_forces() 和 asset.data.joint_effort_limits。；分别在设置与不设置 effort_limit_sim/effort_limit 时比较结果，避免把用户显式覆盖与 USD 默认继承混在一起。
- 原因：PR #2098 显示旧的 ActuatorBase 构造逻辑检查 ActuatorBase.is_implicit_model，即使子类 ImplicitActuator 已标记为隐式模型，该基类检查仍会走到显式执行器的 1e9 默认分支。
- 处理过程：作者在两个 G1 训练任务中注释显式上限复现 1e9。；评论中的临时建议是在机器人配置文件中显式写入力矩上限。；PR #2098 修正隐式模型判断，并合入 PR #2114 对关节属性和测试的改进。
- 有效处理：使用包含已合并 PR #2098 的版本：ActuatorBase 改用 self.is_implicit_model 判断，ImplicitActuator 在两个上限都未设置时保留 USD/PhysX 的 max effort。；无法升级时，可按评论中的办法在机器人配置里显式设置 effort_limit 或 effort_limit_sim，但必须使用已核实的硬件值。
- 结果：PR #2098 于 2025-03-19 合并，合并提交 d7da02da62b46153da3dc3e54585eea078e0d9cb；changelog 记录版本 0.36.3 修复隐式执行器的默认 effort limit 行为。；最终补丁的 articulation 测试在 effort_limit_sim 和 effort_limit 均为 None 时，期望 PhysX effort limit 等于 USD joint_drive_props.max_effort。
- 限制：原帖截图只能证明 USD UI 中 Max Force=88.0；Python 端 1e9 来自作者文字记录，不在截图中。；PR 主检查清单仍未勾选“新增证明修复的测试”，但最终合并补丁通过 #2114 修改了现有 effort-limit 测试；在目标 Isaac Lab/Isaac Sim 组合中仍应运行同样的三方对照。；这一修复保留 USD 限制，不保证 USD 中的数值与真实电机、减速器、电源和热限制一致。
- 安全提示：不得把 1e9 当作真机可用力矩；部署前要另行核对硬件限流、温升、减速器峰值与急停链路。
- 图片分析：原帖 699×259 截图已读取：Isaac Sim 属性面板中 Drive > Angular 显示 Type=force、Max Force=88.0、Target Position=0.0、Target Velocity=0.0、Damping=0.0、Stiffness=0.0。图中没有 Python 侧 1e9，该数值来自正文记录。
- 独立核验引用：[issue · 原作者在 Isaac Lab 和 Legged_Lab 的 G1 任务中注释显式上限后复现 1e9](https://github.com/isaac-sim/IsaacLab/issues/2054#issuecomment-2721483228)；[independent_reproduction · 另一名使用者报告速度上限能读取、力矩上限不能读取](https://github.com/isaac-sim/IsaacLab/issues/2054#issuecomment-2723958505)；[maintainer_confirmation · 项目贡献者确认 PR #2098 是修复，并表示增强了 effort/velocity limit 检查](https://github.com/isaac-sim/IsaacLab/issues/2054#issuecomment-2737536308)；[pull_request · 已合并修复：隐式执行器未配置上限时保留 USD max effort，并改进关节属性测试](https://github.com/isaac-sim/IsaacLab/pull/2098)；[source_code · PR #2098 合并提交](https://github.com/isaac-sim/IsaacLab/commit/d7da02da62b46153da3dc3e54585eea078e0d9cb)
- 适用边界：适用于 Isaac Lab 使用 ImplicitActuator，并期望在未设置 effort_limit_sim/effort_limit 时继承 USD Drive max effort 的版本；原环境为 Isaac Sim 4.5。

### Isaac Lab DCMotor 的峰值力矩与实际可用力矩

- `problem_id`：`problem.hardware_actuator_thermal_power.isaaclab_dcmotor_saturation_vs_effort_limit_2103`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab DCMotor 峰值力矩与实际可用力矩的区别**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：维护者将两者定义为不同层级：saturation_effort 是驱动器峰值力矩，effort_limit 是结合当前电流供应和整机硬件条件后实际允许的运行范围。因此零速附近仍被 effort_limit 限制是设计意图。只有整机能供给驱动器全能力时才提高该值；Spot 将其设为 infinity 是因为另有定制裁剪方案，不能照搬。
- 证据状态：`issue_candidate`
- 来源定位：Isaac Lab #2103 正文的 _clip_effort 公式、issuecomment-2737543184 的概念区分、issuecomment-2738166007 的电源示例和 issuecomment-2739805023 的作者确认
- 原帖/精确回复：[Isaac Lab DCMotor 峰值力矩与实际可用力矩的区别](https://github.com/isaac-sim/IsaacLab/issues/2103)
- 平台/作者：GitHub Issues / IoannisDadiotis
- 关键术语：峰值力矩（peak torque）；饱和力矩（saturation effort）；实际力矩上限（operating effort limit）；力矩—速度包络（torque-speed envelope）；电流供应（current supply）
- 环境：原帖链接到 Isaac Lab commit 91f53e2fe5702eb2fd4bc4de98ab19d320f772c9 的 DCMotor._clip_effort 实现。；维护者硬件示例：某实验室机器人板载电池 8A/约 40 N·m，驱动器 30A/约 100 N·m；未提供机器人型号和测试条件。
- 症状：在关节速度接近零时，速度相关的 saturation_effort 上界仍会被 torch.clip 再次限制到 effort_limit。
- 诊断：把驱动器峰值力矩、可用电流下的持续/实际力矩和速度上限分开核对，不要只从参数大小判断代码有错。；检查电池、母线、驱动器限流和传动系统的可用能力，再决定 effort_limit。
- 原因：这是两个不同物理语义的参数，不是 saturation_effort 未被使用：saturation_effort 建立驱动器峰值包络，effort_limit 再表示当前整机条件下允许的运行范围。
- 处理过程：作者用零速附近的裁剪公式说明实际输出不会超过 effort_limit，并追问这是否过于保守。；维护者用 8A/40 N·m 与 30A/约 100 N·m 的电源—驱动器差异说明设计意图。
- 有效处理：将 saturation_effort 设为驱动器峰值能力，将 effort_limit 设为经电源、热和其他硬件约束核实后的实际可用力矩。；只有在整机确实能长时间或按所需占空比使用驱动器全能力时，才按维护者建议提高 effort_limit；Spot 的 infinity 设置依赖另一套定制裁剪，不能单独照搬。
- 结果：作者在最后回复中确认解释已清楚，Issue 以 completed 关闭。
- 限制：8A/40 N·m 和 30A/约 100 N·m 只是维护者所在实验室的示例，不是通用参数。；原线程没有给出温度、持续时间、母线压降、减速器限制或真机复现数据。；把 effort_limit 设为 infinity 只在另有定制裁剪链路时才有该线程所述的语义。
- 安全提示：提高 effort_limit 前必须验证电池、驱动器、电机、减速器、线束和热保护，并保留独立硬件限流与急停。
- 独立核验引用：[maintainer_confirmation · 项目贡献者定义 saturation limit 为峰值、effort limit 为期望运行范围](https://github.com/isaac-sim/IsaacLab/issues/2103#issuecomment-2737543184)；[maintainer_confirmation · 项目贡献者给出电池 8A/驱动器 30A 示例、提高上限条件和 Spot 定制裁剪边界](https://github.com/isaac-sim/IsaacLab/issues/2103#issuecomment-2738166007)；[issue · 原作者确认解释已清楚](https://github.com/isaac-sim/IsaacLab/issues/2103#issuecomment-2739805023)
- 适用边界：适用于 Isaac Lab DCMotor 及类似同时建模驱动器峰值包络与整机实际力矩上限的执行器模型；数值必须按本机器人实测。

### Isaac Lab 显式执行器的速度限制为什么可能与 PhysX 实际限制不一致？

- `problem_id`：`problem.hardware_actuator_thermal_power.88761dd27f8b57d1`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：显式执行器 velocity_limit 未传播到 PhysX 求解器**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：原 Issue 的维护者说明：当时 ActuatorBaseCfg.velocity_limit 只有 DCMotor 用来计算扭矩—转速上限，没有写入 root_physx_view，因此导入 USD 中的求解器速度限制可能继续生效。合并的 PR #1509 将该限制传播到 PhysX，并增加对应测试。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1384 维护者讨论；merged PR #1509
- 原帖/精确回复：[显式执行器 velocity_limit 未传播到 PhysX 求解器](https://github.com/isaac-sim/IsaacLab/issues/1384#issuecomment-2465073195)
- 平台/作者：GitHub Issues / diegoaldarondo-fauna
- 关键术语：显式执行器（explicit actuator）；求解器级限制（solver-level limit）；扭矩—转速限制（torque-speed limit）
- 环境：Isaac Lab commit b9a49ca；Isaac Sim 4.0.0—4.2.0；Ubuntu 22.04；RTX 4090。
- 症状：DCMotor 的模型速度限制可能被 PhysX/导入资产速度限制静默覆盖或截断。
- 诊断：分别检查显式执行器的模型限制与 root_physx_view 的求解器限制。
- 原因：ActuatorBaseCfg.velocity_limit 未传播到 root_physx_view。
- 处理过程：维护者讨论区分模型级限制与求解器级限制。；PR #1509 实现速度限制传播。
- 有效处理：PR #1509 将 ActuatorBaseCfg 的 velocity_limits 传播到 articulation root_physx_view。
- 结果：PR #1509 于 2024-12-08 合并，merge commit 4ee4957e；PR 清单声明加入证明修复的测试。
- 限制：该行为对应历史版本；新版本字段命名和模型/求解器限制分工需查当前文档。
- 独立核验引用：[pull_request · merged PR：传播 ActuatorBaseCfg velocity_limits 到 root_physx_view；merge commit 4ee4957e；含测试声明](https://github.com/isaac-sim/IsaacLab/pull/1509)
- 适用边界：Isaac Lab 4.0.0—4.2.0 附近版本；新版本需核对模型级与 solver-level 限制字段。

### Isaac Lab IdealPDActuator 的 PD 力矩误差方向应按文档还是代码？

- `problem_id`：`problem.hardware_actuator_thermal_power.b22177e0eee46246`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab IdealPDActuator 文档与代码的误差符号相反**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：该版本应按代码：位置误差为 q_des-q，速度误差为 qdot_des-qdot，再乘 stiffness/damping 并加前馈力矩。Isaac Lab 贡献者确认代码实现正确、文档应更新。这个结论对应 Issue 指定的 commit 与 4.2.0 环境；其他版本应重新查看当前源码。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1643 正文代码对照；贡献者回复 issuecomment-2586156271
- 原帖/精确回复：[Isaac Lab IdealPDActuator 文档与代码的误差符号相反](https://github.com/isaac-sim/IsaacLab/issues/1643#issuecomment-2586156271)
- 平台/作者：GitHub Issues / Limorettle
- 关键术语：比例—微分控制器（PD controller）；位置误差（position error）；前馈力矩（feed-forward torque）
- 环境：Isaac Lab commit 8f3b9ca；Isaac Sim 4.2.0；Ubuntu 20.04；CUDA 12.2。
- 症状：文档写 (q-q_des) 与 (qdot-qdot_des)，代码写相反方向。
- 诊断：直接对照 API 文档和 IdealPDActuator.compute 的 error_pos/error_vel。
- 原因：API 文档公式符号写反。
- 处理过程：提问者提供公式、代码和参数定义；贡献者核对后确认。
- 有效处理：按代码中的 q_des-q 与 qdot_des-qdot 解释力矩；贡献者表示更新文档。
- 结果：贡献者确认代码正确，Issue 随后关闭。
- 限制：线程没有给出具体文档修复 PR；不能只凭关闭状态推断所有历史文档已更新。
- 独立核验引用：[maintainer_confirmation · Isaac Lab 贡献者确认代码正确、文档需更新](https://github.com/isaac-sim/IsaacLab/issues/1643#issuecomment-2586156271)
- 适用边界：Isaac Lab commit 8f3b9ca / Isaac Sim 4.2.0；新版本需核对当前实现。

## joint_mapping_frames_conventions (`joint_mapping_frames_conventions`)

### Pinocchio ABA 中移动基座侧向约束异常时，最先检查什么？

- `problem_id`：`problem.joint_mapping_frames_conventions.4a749f2959c209c9`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 约束前向动力学中的基座力坐标系误解**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：最先检查基座广义力的参考坐标系。该案例的根因是把作用于基座的广义力误当作机体系，而实际按世界系解释；修正这一点后原作者确认运行正常。若还要严格联立约束力和加速度，再考虑等式约束 QP。
- 证据状态：`issue_candidate`
- 来源定位：原作者解决确认 @micko-plz
- 原帖/精确回复：[Pinocchio 约束前向动力学中的基座力坐标系误解](https://github.com/stack-of-tasks/pinocchio/issues/984#issuecomment-564544773)
- 平台/作者：GitHub Issues / micko-plz
- 关键术语：前向动力学（Forward Dynamics）；坐标系（Coordinate Frame）；二次规划（Quadratic Programming, QP）
- 环境：Pinocchio、平面根关节、ABA、两轮差速移动操作机器人。
- 症状：对基座侧向力和局部 y 速度的计算产生矛盾。
- 诊断：逐项核对广义坐标、广义速度和广义力各分量使用的参考坐标系。
- 原因：误把输入 ABA 的基座力矩分量当作机体系，实际按世界系解释。
- 处理过程：作者检查关节雅可比、速度导数和约束前向动力学接口。
- 有效处理：按世界坐标系重新解释并构造基座广义力。
- 结果：原作者明确确认修正坐标系理解后代码可以工作。
- 限制：维护者指出严格的等式约束力与加速度耦合仍可能需要 QP；本例最终修复的是坐标系误解。
- 安全提示：实机底盘测试前应对每个广义力分量做坐标系单元测试。
- 适用边界：适用于 Pinocchio 平面/浮动基座模型和 ABA 输入构造。

### Pinocchio 中何时用 getJointJacobian，何时用 getFrameJacobian？

- `problem_id`：`problem.joint_mapping_frames_conventions.b9c8428a4a10de70`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 关节雅可比与 frame 雅可比的调用顺序和参考系**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：先调用 computeJointJacobians 更新缓存。若目标末端 frame 与关节重合，可读取关节雅可比；否则应按 frame_id 读取 frame 雅可比。还必须显式核对 WORLD、LOCAL 或 LOCAL_WORLD_ALIGNED，不能只比较矩阵数值而忽略表达点和参考系定义。
- 证据状态：`issue_candidate`
- 来源定位：维护者技术回复 @proyan
- 原帖/精确回复：[Pinocchio 关节雅可比与 frame 雅可比的调用顺序和参考系](https://github.com/stack-of-tasks/pinocchio/issues/1455#issuecomment-851466483)
- 平台/作者：GitHub Issues / kaixqu
- 关键术语：雅可比矩阵（Jacobian Matrix）；坐标系（Coordinate Frame）；末端执行器（End Effector, EE）
- 环境：Pinocchio、末端执行器 frame、WORLD/LOCAL/LOCAL_WORLD_ALIGNED 参考系。
- 症状：API 返回的雅可比与直觉中的末端速度映射不一致。
- 诊断：先检查是否调用 computeJointJacobians，再检查末端 frame 是否已定义及所选 reference frame。
- 原因：混淆了缓存计算函数与读取函数，也混淆了 Frame 类和表达参考系。
- 处理过程：讨论用 Talos 随机构型脚本对比 frame 与 parent joint 的 WORLD 雅可比。
- 有效处理：先计算全体关节雅可比；末端与关节重合时读取 joint Jacobian，否则读取 frame Jacobian。
- 结果：维护者给出可运行验证脚本并关闭 Issue，但后续仍有用户补充概念讨论。
- 限制：WORLD 下的相等关系依赖 Pinocchio 对该参考系速度场的定义，不能直接套到 LOCAL 或 LOCAL_WORLD_ALIGNED。
- 适用边界：适用于 Pinocchio 的关节/frame 雅可比 API；版本升级后应以当前文档和单元测试复核。

### IsaacLab 的关节执行器参数遇到 degree/radian 文档冲突时，应该采用哪套单位？

- `problem_id`：`problem.joint_mapping_frames_conventions.5ace538fe98a5b88`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：IsaacLab 旧接口的角度单位在 USD 操作与物理引擎路径间不统一**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录；适用环境未知。
- 解答状态：`partial`
- 候选解答：原帖 contributor 给出的历史规则是：经过 USD 操作的路径使用度（degrees），直接进入物理引擎的其他路径使用弧度（radians）。由于 Issue 仍开放且只表达了“应统一为 radians”的意向，没有逐字段和版本迁移表，所以不能把这句话当作当前版本的统一规则。实际配置时必须追踪字段落到 USD 还是 physics/tensor API，并对照目标版本源码验证。
- 证据状态：`issue_candidate`
- 来源定位：Issue #663，contributor 回复 issuecomment-2255516442
- 原帖/精确回复：[IsaacLab 旧接口的角度单位在 USD 操作与物理引擎路径间不统一](https://github.com/isaac-sim/IsaacLab/issues/663#issuecomment-2255516442)
- 平台/作者：GitHub Issues / GiulioRomualdi
- 关键术语：角度制（degrees）；弧度制（radians）；美元场景描述（USD）；物理引擎（physics engine）
- 环境：2024-07 的 IsaacLab 迁移与 actuator 文档；具体 release/commit 未说明；Issue 当前仍 Open。
- 症状：不同文档分别暗示 degree 与 radian，接口缺少逐字段单位说明。
- 诊断：追踪配置最终走 USD authoring 还是物理引擎/tensor API；对每个字段查目标版本源码和文档，不按统一单位猜测。
- 原因：Contributor 解释为 USD 使用 degrees、物理引擎使用 radians 的历史边界。
- 处理过程：维护者提出未来应统一为 radians。
- 结果：单位边界得到 contributor 解释，但线程没有提供统一完成的版本或字段迁移表。
- 限制：这是一条 2024 年的开放线程；不能据此假设当前所有接口仍保持相同约定，也不能把阻尼/刚度单位简化成只有角度制差异。
- 安全提示：将增益或速度限制用于实机前，必须通过单关节小幅命令和源码字段单位核对，避免 57.3 倍量级错误。
- 独立核验引用：[maintainer_confirmation · contributor 说明 USD degrees 与 physics radians 的历史边界](https://github.com/isaac-sim/IsaacLab/issues/663#issuecomment-2255516442)
- 适用边界：适用于解释 2024 年 IsaacLab/Isaac Sim 的历史单位边界；当前版本必须重新核对。

### Pinocchio 浮动基科氏矩阵看似随位置或姿态异常变化时，为什么应先检查四元数归一化？

- `problem_id`：`problem.joint_mapping_frames_conventions.0ce1582a1859efd0`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：未归一化浮动基四元数会造成 Pinocchio 科氏矩阵对姿态的伪差异**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原帖维护者首先指出输入四元数没有归一化。提问者改用精确 sin/cos 构造单位四元数后，矩阵差范数从约 0.00075 降到 5.16e-14。因此这类比较应先验证四元数单位范数并保留足够精度，再讨论算法或参考系问题。线程没有支持“必须始终用零位置和单位姿态”这一更强结论。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2060，维护者诊断 issuecomment-1723125266；原作者复测 issuecomment-1724525093
- 原帖/精确回复：[未归一化浮动基四元数会造成 Pinocchio 科氏矩阵对姿态的伪差异](https://github.com/stack-of-tasks/pinocchio/issues/2060#issuecomment-1724525093)
- 平台/作者：GitHub Issues / XuanLin
- 关键术语：科氏矩阵（Coriolis matrix）；四元数归一化（quaternion normalization）；浮动基（floating base）；数值误差（numerical error）
- 环境：Pinocchio Python API；JointModelFreeFlyer；原帖给出两连杆 URDF 与完整比较脚本；具体 Pinocchio/OS 版本未说明。
- 症状：不同位置和姿态输入下科氏矩阵差异明显，初始示例的矩阵差范数为 0.00075。
- 诊断：在判断算法或坐标系错误前检查配置向量中的四元数范数；改用严格归一化输入重复相同矩阵比较。
- 原因：维护者指出初始四元数只是从 Gazebo 截取两位小数，未满足单位范数。
- 处理过程：提问者用精确的 sin(pi/2)、cos(pi/2) 重建两组四元数并重新计算。
- 有效处理：确保传入 JointModelFreeFlyer 的四元数已归一化；不要用低精度截断后的四元数直接比较动力学量。
- 结果：归一化后差异范数降至 5.16e-14；提问者确认结果大幅改善。
- 限制：线程仍未关闭，5.16e-14 的残差没有进一步解释；原作者关于是否必须固定为零位置/单位姿态的问题没有得到回答。
- 独立核验引用：[maintainer_confirmation · 维护者指出输入四元数未归一化](https://github.com/stack-of-tasks/pinocchio/issues/2060#issuecomment-1723125266)；[issue · 原作者使用单位四元数复测，差异范数降到 5.16e-14](https://github.com/stack-of-tasks/pinocchio/issues/2060#issuecomment-1724525093)
- 适用边界：适用于 Pinocchio JointModelFreeFlyer 配置输入和动力学量对比；具体版本未说明。

### MuJoCo 状态传给 Pinocchio 后质心速度方向异常，应先检查什么？

- `problem_id`：`problem.joint_mapping_frames_conventions.8c7a96eff6290dee`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo 与 Pinocchio 四元数分量顺序不同会让质心速度方向看似相反**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：先检查浮动基四元数分量顺序。原作者最终定位到 MuJoCo 使用 wxyz，而 Pinocchio 使用 xyzw；直接把 qpos 传入会给 Pinocchio 错误姿态，并使质心速度方向看似异常。传递前应按目标 API 重排四元数，并用可视化或已知运动方向再次核对。原帖没有证明其余状态分量可全部原样复制。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2531，原作者自我定位并关闭线程的回复 issuecomment-2564969179
- 原帖/精确回复：[MuJoCo 与 Pinocchio 四元数分量顺序不同会让质心速度方向看似相反](https://github.com/stack-of-tasks/pinocchio/issues/2531#issuecomment-2564969179)
- 平台/作者：GitHub Issues / hang0610
- 关键术语：质心速度（center-of-mass velocity）；四元数（quaternion）；分量顺序（component ordering）；浮动基（floating base）
- 环境：原帖写明 Pinocchio 2.6.20、IOS（原文如此）；最小复现使用 Python 3.8、MuJoCo、NumPy、glfw 与 conda-forge Pinocchio。
- 症状：MuJoCo qvel\[2\] 为正，Pinocchio data.vcom\[0\]\[2\] 为负；把原姿态交给 Meshcat 后机器人姿态异常。
- 诊断：在怀疑 centerOfMass 算法前，先核对两个库的浮动基 qpos 布局和四元数分量顺序；用可视化检查姿态是否正确。
- 原因：MuJoCo 使用 wxyz，而 Pinocchio 使用 xyzw；原代码直接复用 qpos，未重排四元数。
- 处理过程：提问者提供最小脚本和模型，并用 Meshcat 可视化同一配置。
- 有效处理：在把 MuJoCo 浮动基配置传给 Pinocchio 前按目标 API 的 xyzw 顺序重排四元数；同时核对其余 q/v 布局。
- 结果：原作者明确回复已找到分量顺序问题，并在同一时间关闭 Issue；线程没有给出重排后的数值截图。
- 限制：原帖只明确确认四元数顺序；没有逐项说明所有 MuJoCo qvel 与 Pinocchio tangent vector 的映射，因此不能把整段状态数组视为通用直接兼容。
- 图片分析：原作者在回复中说明：使用 wxyz 配置进行 Meshcat 可视化时机器人姿态明显错误；本卡不从图片提取额外角度或数值。
- 独立核验引用：[issue · 原作者明确指出 MuJoCo wxyz 与 Pinocchio xyzw 的顺序差异](https://github.com/stack-of-tasks/pinocchio/issues/2531#issuecomment-2564969179)；[issue · 原作者提供最小脚本、模型与运行步骤](https://github.com/stack-of-tasks/pinocchio/issues/2531#issuecomment-2564084659)
- 适用边界：适用于 MuJoCo 浮动基 qpos 与 Pinocchio 配置之间的四元数转换；具体模型的整段 q/v 映射仍需单独核对。

### Pinocchio FreeFlyer 的随机配置导致 Jacobian/SE3 对照异常时，如何避免非法四元数？

- `problem_id`：`problem.joint_mapping_frames_conventions.1fca6b8a3ad3439b`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：随机生成未归一化浮动基四元数会使 Pinocchio Jacobian/SE3 对照失真**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：不要用相互独立的随机数直接填 FreeFlyer 四元数。项目成员建议使用 pinocchio.randomConfiguration(model, lowerLimits, upperLimits)，让生成结果满足模型配置流形；或者显式对随机 Quaternion 调用 normalize。原作者将未归一化四元数定位为错误 SE3 的原因，维护者对这一处理方向作了确认。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1593，原作者自我定位 issuecomment-1019748618；项目成员确认 issuecomment-1019809389
- 原帖/精确回复：[随机生成未归一化浮动基四元数会使 Pinocchio Jacobian/SE3 对照失真](https://github.com/stack-of-tasks/pinocchio/issues/1593#issuecomment-1019809389)
- 平台/作者：GitHub Issues / ghost
- 关键术语：自由浮动关节（JointModelFreeFlyer）；四元数归一化（quaternion normalization）；随机配置（random configuration）；三维特殊欧氏群（three-dimensional special Euclidean group, SE3）
- 环境：Pinocchio CasADi；JointModelFreeFlyer；用户提供外部 URDF；100 组随机配置/速度对照；具体 Pinocchio 版本未说明。
- 症状：getFrameJacobian、computeFrameJacobian、getJointJacobian 和 computeJointJacobian 乘速度后的结果与作者预期不一致。
- 诊断：先验证配置中的 FreeFlyer 四元数是否合法；使用 Pinocchio 提供的随机配置生成器或显式 normalize；再单独核对 Jacobian 的输入速度定义。
- 原因：原作者认为随机四元数不规则导致错误 SE3；项目成员确认并给出合法配置生成方式。原作者关于只使用 v_j 的第二判断未被回应。
- 处理过程：作者补充 URDF，并自行分析随机四元数和速度向量选择；项目成员针对四元数给出两种处理。
- 有效处理：使用 pinocchio.randomConfiguration(model, lowerLimits, upperLimits) 生成满足模型流形的配置，或对随机四元数调用 normalize。
- 结果：项目成员表示作者已解决问题并确认四元数处理方向；线程没有给出修正后的数值对照，也没有确认 v_j 结论。
- 限制：不能把未获回应的局部速度选择写成 Pinocchio API 的通用规则；具体 Jacobian 语义仍需对照目标函数文档和最小复现。
- 独立核验引用：[maintainer_confirmation · 项目成员建议 randomConfiguration 或 Quaternion.normalize](https://github.com/stack-of-tasks/pinocchio/issues/1593#issuecomment-1019809389)；[issue · 原作者把不规则随机四元数定位为错误 SE3 的原因](https://github.com/stack-of-tasks/pinocchio/issues/1593#issuecomment-1019748618)
- 适用边界：适用于 JointModelFreeFlyer 及其他以单位四元数承载旋转的 Pinocchio 配置；随机上下界仍需是模型允许范围。

### 该线程是否证明 getJointJacobian 的速度计算只应使用局部关节速度 v_j，而不能使用完整广义速度？

- `problem_id`：`problem.joint_mapping_frames_conventions.9deacd4d1e386766`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：随机生成未归一化浮动基四元数会使 Pinocchio Jacobian/SE3 对照失真**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索；尚未形成可核对的复现记录。
- 解答状态：`unresolved`
- 候选解答：没有。原作者在自我分析中写出这一判断，但项目成员后续只回应了四元数生成和归一化，没有确认速度向量选择，也没有给出修正后的数值结果。因此这条只能作为待复现线索，不能作为 Pinocchio Jacobian 的通用调用规则。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1593，原作者未获确认的第二条分析 issuecomment-1019748618
- 原帖/精确回复：[随机生成未归一化浮动基四元数会使 Pinocchio Jacobian/SE3 对照失真](https://github.com/stack-of-tasks/pinocchio/issues/1593#issuecomment-1019748618)
- 平台/作者：GitHub Issues / ghost
- 关键术语：关节雅可比（joint Jacobian）；广义速度（generalized velocity）；关节速度（joint velocity）；局部坐标系（LOCAL）
- 环境：Pinocchio CasADi；JointModelFreeFlyer；用户提供外部 URDF；100 组随机配置/速度对照；具体 Pinocchio 版本未说明。
- 症状：getFrameJacobian、computeFrameJacobian、getJointJacobian 和 computeJointJacobian 乘速度后的结果与作者预期不一致。
- 诊断：先验证配置中的 FreeFlyer 四元数是否合法；使用 Pinocchio 提供的随机配置生成器或显式 normalize；再单独核对 Jacobian 的输入速度定义。
- 原因：原作者认为随机四元数不规则导致错误 SE3；项目成员确认并给出合法配置生成方式。原作者关于只使用 v_j 的第二判断未被回应。
- 处理过程：作者补充 URDF，并自行分析随机四元数和速度向量选择；项目成员针对四元数给出两种处理。
- 有效处理：使用 pinocchio.randomConfiguration(model, lowerLimits, upperLimits) 生成满足模型流形的配置，或对随机四元数调用 normalize。
- 结果：项目成员表示作者已解决问题并确认四元数处理方向；线程没有给出修正后的数值对照，也没有确认 v_j 结论。
- 限制：不能把未获回应的局部速度选择写成 Pinocchio API 的通用规则；具体 Jacobian 语义仍需对照目标函数文档和最小复现。
- 独立核验引用：[issue · 原作者提出只使用 v_j，但线程没有维护者确认或修正后输出](https://github.com/stack-of-tasks/pinocchio/issues/1593#issuecomment-1019748618)
- 适用边界：仅记录该线程中的未验证判断；实际应按具体 Joint/Frame Jacobian API 的矩阵列定义核对。

### Pinocchio 与 MuJoCo 的浮动基动力学量参考系不一致

- `problem_id`：`problem.joint_mapping_frames_conventions.pinocchio_mujoco_freeflyer_frames_446`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：3（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 与 MuJoCo 的浮动基 Jcom 和惯性矩阵差异首先要对齐参考系表示**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：维护者把首要原因定位为坐标系：Pinocchio 的 center-of-mass Jacobian 用世界坐标表达，而原帖中的 MuJoCo 量被按腰部局部坐标理解。对该最小模型，他建议用 data.oMi\[1\].rotation.T * Jc 把 Pinocchio 结果旋转到局部表达；作者实测后报告误差大幅下降。因此不能把前三列直接与单位阵比较，必须先明确目标坐标系和正确 joint id。
- 证据状态：`issue_candidate`
- 来源定位：Issue #446，维护者坐标系诊断 issuecomment-374313755；作者复测 issuecomment-374501855
- 原帖/精确回复：[Pinocchio 与 MuJoCo 的浮动基 Jcom 和惯性矩阵差异首先要对齐参考系表示](https://github.com/stack-of-tasks/pinocchio/issues/446#issuecomment-374501855)
- 平台/作者：GitHub Issues / longwoo
- 关键术语：质心雅可比（center-of-mass Jacobian, Jcom）；世界坐标系（world frame）；局部坐标系（local frame）；自由浮动基（FreeFlyer）
- 环境：2018 年 Pinocchio Python/C++；MuJoCo 对照；用户提供浮动关节最小 URDF、双腿 URDF 状态与完整矩阵输出；具体发布版本未说明。
- 症状：带非单位基座姿态时，Pinocchio Jcom 的平移块出现约 1e-2 的非对角项，而用户预期单位阵。；固定基质量矩阵两边一致，加入 FreeFlyer 且基座旋转非单位后，质量矩阵前六行明显不同。
- 诊断：先确定被比较 Jacobian 的表达坐标系和作用点；把 Pinocchio 世界系 Jcom 旋转到目标局部坐标后再比较。；分别用单位基座旋转与非单位旋转对照 CRBA，确认差异是否只随浮动基表示变化。；用 RNEA 和合适参考系下的 Jcom 交叉验证质量矩阵，而不是只逐元素比较两个库的原始矩阵。
- 原因：Pinocchio Jcom 用世界坐标表达，用户的 MuJoCo 对照量按腰部局部坐标理解。；Pinocchio 的浮动基速度、加速度和力分量用第一刚体坐标表示，而 MuJoCo 对照矩阵按世界坐标表示。
- 处理过程：维护者给出 data.oMi\[1\].rotation.T * Jc 对照；作者应用旋转并报告误差明显下降。；作者比较固定基与 FreeFlyer，并将两边基座姿态设为单位；单位姿态下矩阵误差降到约 1e-8 至 1e-10 量级。
- 有效处理：比较 Jcom 前把两边转换到同一坐标表达；原线程对第一个浮动刚体使用 data.oMi\[1\].rotation.T 乘 Pinocchio Jc。；读取关节局部速度时先 forwardKinematics(model,data,q,qdot)，再用 data.v\[id\]；只改变坐标表达时分别旋转 linear/angular 分量，不平移作用点。
- 结果：作者确认 Jcom 旋转后与 MuJoCo 的差异大幅降低，并确认 WORLD/LOCAL 解释清楚。；作者在单位基座旋转实验中得到两边几乎一致的质量矩阵，并将剩余非单位旋转差异归因于浮动基表示。
- 限制：原线程没有给出通用的 MuJoCo↔Pinocchio 质量矩阵基变换公式，也没有把所有 bias 项差异完全闭环。；data.oMi\[1\] 只适合该最小模型的第一目标关节，实际系统必须使用正确 joint id。
- 独立核验引用：[maintainer_confirmation · 维护者说明 Pinocchio Jcom 用世界坐标表达并给出旋转对照](https://github.com/stack-of-tasks/pinocchio/issues/446#issuecomment-374313755)；[issue · 作者应用旋转后报告与 MuJoCo 的误差大幅下降](https://github.com/stack-of-tasks/pinocchio/issues/446#issuecomment-374501855)
- 适用边界：适用于原帖的浮动基最小模型和 Pinocchio/MuJoCo Jcom 对照；其他 API 的 Jacobian 作用点与参考系需分别查明。

**经验 2：Pinocchio 与 MuJoCo 的浮动基 Jcom 和惯性矩阵差异首先要对齐参考系表示**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：维护者说明，WORLD Jacobian 的 twist 用世界坐标表达，其线速度对应当前与世界原点重合、但附着于目标关节的点；LOCAL 对应目标关节中心并用关节局部坐标表达，两者通过 J_world = action(data.oMi\[k\]) * J_local 联系。要取关节局部速度，先调用 forwardKinematics(model,data,q,qdot)，再读 data.v\[id\]。若只想把同一作用点的速度改用世界坐标表达，应分别用 data.oMi\[id\].rotation() 旋转 linear 与 angular 分量，不能额外引入平移。Jcom 是系统质心速度向量的世界坐标表达，不套用 WORLD spatial twist 的世界原点作用点解释。
- 证据状态：`issue_candidate`
- 来源定位：Issue #446，Jacobian 定义 issuecomment-378168382；WORLD/LOCAL 作用点 issuecomment-380343908；Jcom 与 data.v 说明 issuecomment-380361182
- 原帖/精确回复：[Pinocchio 与 MuJoCo 的浮动基 Jcom 和惯性矩阵差异首先要对齐参考系表示](https://github.com/stack-of-tasks/pinocchio/issues/446#issuecomment-380361182)
- 平台/作者：GitHub Issues / longwoo
- 关键术语：空间速度（spatial velocity, twist）；配置切空间（configuration tangent space）；特殊欧氏群（special Euclidean group, SE3）；正向运动学（forward kinematics, FK）
- 环境：2018 年 Pinocchio Python/C++；MuJoCo 对照；用户提供浮动关节最小 URDF、双腿 URDF 状态与完整矩阵输出；具体发布版本未说明。
- 症状：带非单位基座姿态时，Pinocchio Jcom 的平移块出现约 1e-2 的非对角项，而用户预期单位阵。；固定基质量矩阵两边一致，加入 FreeFlyer 且基座旋转非单位后，质量矩阵前六行明显不同。
- 诊断：先确定被比较 Jacobian 的表达坐标系和作用点；把 Pinocchio 世界系 Jcom 旋转到目标局部坐标后再比较。；分别用单位基座旋转与非单位旋转对照 CRBA，确认差异是否只随浮动基表示变化。；用 RNEA 和合适参考系下的 Jcom 交叉验证质量矩阵，而不是只逐元素比较两个库的原始矩阵。
- 原因：Pinocchio Jcom 用世界坐标表达，用户的 MuJoCo 对照量按腰部局部坐标理解。；Pinocchio 的浮动基速度、加速度和力分量用第一刚体坐标表示，而 MuJoCo 对照矩阵按世界坐标表示。
- 处理过程：维护者给出 data.oMi\[1\].rotation.T * Jc 对照；作者应用旋转并报告误差明显下降。；作者比较固定基与 FreeFlyer，并将两边基座姿态设为单位；单位姿态下矩阵误差降到约 1e-8 至 1e-10 量级。
- 有效处理：比较 Jcom 前把两边转换到同一坐标表达；原线程对第一个浮动刚体使用 data.oMi\[1\].rotation.T 乘 Pinocchio Jc。；读取关节局部速度时先 forwardKinematics(model,data,q,qdot)，再用 data.v\[id\]；只改变坐标表达时分别旋转 linear/angular 分量，不平移作用点。
- 结果：作者确认 Jcom 旋转后与 MuJoCo 的差异大幅降低，并确认 WORLD/LOCAL 解释清楚。；作者在单位基座旋转实验中得到两边几乎一致的质量矩阵，并将剩余非单位旋转差异归因于浮动基表示。
- 限制：原线程没有给出通用的 MuJoCo↔Pinocchio 质量矩阵基变换公式，也没有把所有 bias 项差异完全闭环。；data.oMi\[1\] 只适合该最小模型的第一目标关节，实际系统必须使用正确 joint id。
- 独立核验引用：[maintainer_confirmation · 维护者定义 Jacobian 从配置切空间到 SE3 tangent，Jcom 到质心速度](https://github.com/stack-of-tasks/pinocchio/issues/446#issuecomment-378168382)；[maintainer_confirmation · 维护者说明 WORLD/LOCAL 的作用点和 placement action 关系](https://github.com/stack-of-tasks/pinocchio/issues/446#issuecomment-380343908)；[maintainer_confirmation · 维护者区分 Jcom 与 joint velocity，并给出 data.v\[id\] 的坐标旋转方法](https://github.com/stack-of-tasks/pinocchio/issues/446#issuecomment-380361182)
- 适用边界：适用于该时期 Pinocchio 的 Joint Jacobian、data.v 和 Jcom 约定；Frame API 及 LOCAL_WORLD_ALIGNED 需按对应版本文档另行核对。

**经验 3：Pinocchio 与 MuJoCo 的浮动基 Jcom 和惯性矩阵差异首先要对齐参考系表示**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：维护者说明质量矩阵把配置切空间中的加速度映射到余切空间中的力；Pinocchio 的 FreeFlyer 运动与力分量都在第一刚体坐标中表示，换一种表示会改变质量矩阵前六行的数值。作者先验证固定基矩阵完全一致、两边 FK 位姿一致，再把浮动基位置清零且姿态设为单位；此时两边矩阵误差降到约 1e-8 至 1e-10 量级。该实验支持参考系表示是主要差异，但线程没有给任意姿态下的完整矩阵变换公式。
- 证据状态：`issue_candidate`
- 来源定位：Issue #446，维护者质量矩阵表示说明 issuecomment-380809974；作者单位姿态对照 issuecomment-381078728
- 原帖/精确回复：[Pinocchio 与 MuJoCo 的浮动基 Jcom 和惯性矩阵差异首先要对齐参考系表示](https://github.com/stack-of-tasks/pinocchio/issues/446#issuecomment-381078728)
- 平台/作者：GitHub Issues / longwoo
- 关键术语：复合刚体算法（Composite Rigid Body Algorithm, CRBA）；质量矩阵（mass matrix）；余切空间（cotangent space）；广义力（generalized force）
- 环境：2018 年 Pinocchio Python/C++；MuJoCo 对照；用户提供浮动关节最小 URDF、双腿 URDF 状态与完整矩阵输出；具体发布版本未说明。
- 症状：带非单位基座姿态时，Pinocchio Jcom 的平移块出现约 1e-2 的非对角项，而用户预期单位阵。；固定基质量矩阵两边一致，加入 FreeFlyer 且基座旋转非单位后，质量矩阵前六行明显不同。
- 诊断：先确定被比较 Jacobian 的表达坐标系和作用点；把 Pinocchio 世界系 Jcom 旋转到目标局部坐标后再比较。；分别用单位基座旋转与非单位旋转对照 CRBA，确认差异是否只随浮动基表示变化。；用 RNEA 和合适参考系下的 Jcom 交叉验证质量矩阵，而不是只逐元素比较两个库的原始矩阵。
- 原因：Pinocchio Jcom 用世界坐标表达，用户的 MuJoCo 对照量按腰部局部坐标理解。；Pinocchio 的浮动基速度、加速度和力分量用第一刚体坐标表示，而 MuJoCo 对照矩阵按世界坐标表示。
- 处理过程：维护者给出 data.oMi\[1\].rotation.T * Jc 对照；作者应用旋转并报告误差明显下降。；作者比较固定基与 FreeFlyer，并将两边基座姿态设为单位；单位姿态下矩阵误差降到约 1e-8 至 1e-10 量级。
- 有效处理：比较 Jcom 前把两边转换到同一坐标表达；原线程对第一个浮动刚体使用 data.oMi\[1\].rotation.T 乘 Pinocchio Jc。；读取关节局部速度时先 forwardKinematics(model,data,q,qdot)，再用 data.v\[id\]；只改变坐标表达时分别旋转 linear/angular 分量，不平移作用点。
- 结果：作者确认 Jcom 旋转后与 MuJoCo 的差异大幅降低，并确认 WORLD/LOCAL 解释清楚。；作者在单位基座旋转实验中得到两边几乎一致的质量矩阵，并将剩余非单位旋转差异归因于浮动基表示。
- 限制：原线程没有给出通用的 MuJoCo↔Pinocchio 质量矩阵基变换公式，也没有把所有 bias 项差异完全闭环。；data.oMi\[1\] 只适合该最小模型的第一目标关节，实际系统必须使用正确 joint id。
- 独立核验引用：[maintainer_confirmation · 维护者解释质量矩阵映射和 Pinocchio FreeFlyer 的第一刚体坐标表示](https://github.com/stack-of-tasks/pinocchio/issues/446#issuecomment-380809974)；[issue · 作者把两边基座姿态设为单位后得到近零矩阵差，并总结表示差异](https://github.com/stack-of-tasks/pinocchio/issues/446#issuecomment-381078728)
- 适用边界：适用于原帖 FreeFlyer 模型的 CRBA/MuJoCo full mass matrix 对照；不能据此直接替换目标项目的广义坐标基变换。

### Pinocchio 浮动基速度坐标不一致导致 Jacobian 验证失配

- `problem_id`：`problem.joint_mapping_frames_conventions.pinocchio_freeflyer_velocity_local_frame_1140`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 浮动基速度坐标表达不一致导致 Jacobian 速度验证失配**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原作者最终确认，他们把浮动基速度、四元数传播和积分器都按全局坐标处理，与 Pinocchio Jacobian 所需的 free-flyer 局部速度约定不兼容。对齐局部表达后，作者得到预期结果。有限差分应用 q_plus = pin.integrate(model, q, v * eps) 在配置流形上进行，再对 frame 的世界位置做差分；C++ 输出式 Jacobian 还应核对 J 是否预先置零。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1140；有限差分 issuecomment-610328052；free-flyer 局部速度 issuecomment-611878250；原作者解决确认 issuecomment-614654251
- 原帖/精确回复：[Pinocchio 浮动基速度坐标表达不一致导致 Jacobian 速度验证失配](https://github.com/stack-of-tasks/pinocchio/issues/1140#issuecomment-614654251)
- 平台/作者：GitHub Issues / EnricoMingo
- 关键术语：浮动基（floating base, free flyer）；局部坐标（local coordinates）；局部坐标世界轴对齐（LOCAL_WORLD_ALIGNED）；配置流形（configuration manifold）；有限差分（finite difference）
- 环境：Pinocchio C++ getFrameJacobian 与浮动基系统；原帖未说明 Pinocchio 版本、机器人型号或操作系统。
- 症状：原帖第一张图中，frame 速度的实线与虚线在多个区间明显分离。；第二张图中，部分 qdot 与差分 q 的实线/虚线基本重合，说明并非所有数值微分都失败。
- 诊断：按项目贡献者代码用 q_plus = pin.integrate(model, q, v * eps) 构造流形上的邻近构型，再用 frame 世界位置差分对照 Jv。；核对 free-flyer 基座 twist 是按 Pinocchio 的局部坐标语义提供，不要把全局坐标速度直接传入。；C++ 使用带输出参数的 getFrameJacobian 时，按线程提示确保 J 预先置零。
- 原因：原作者最终确认：自己的浮动基速度、四元数传播和积分器使用全局坐标，与 Pinocchio 提供 Jacobian 时的局部 free-flyer 速度约定不兼容。
- 处理过程：项目贡献者给出 frame velocity、Jv 以及 pin.integrate 有限差分的最小 Python 对照代码。；讨论中一度出现对 getFrameVelocity 的错误说明，后来由原回复者明确更正；本卡不沿用已更正的旧解释。
- 有效处理：将浮动基速度、四元数传播和积分器与 Pinocchio 的 free-flyer 局部速度约定对齐；用 pin.integrate 而非对广义构型直接逐元 diff 做有限差分验证。
- 结果：原作者回复说问题已解决，改正坐标表达后得到开帖时期望的结果；项目贡献者随后按已解决关闭 Issue。
- 限制：原线程没有提供修正后曲线、Pinocchio 版本或数值误差。；原图没有图例、坐标轴名称和物理单位，无法从图中识别每条颜色对应的速度分量或计算方法。；回复中对 getFrameVelocity 的说明曾被原回复者更正；应以后续更正和当前 API 文档为准。
- 安全提示：将任务空间速度反馈用于真机前，应用小扰动、pin.integrate 和可视化同时验证基座 twist 的坐标表达。
- 图片分析：原帖第一张 687×516 曲线图中，一组蓝色实线/紫色虚线在峰值和末段存在偏差，浅蓝虚线/橙色实线在约 20–60 横轴区间明显分离；红/绿零值线重合。图无图例、轴名和单位，只能确认原作者所说的速度失配，不能从颜色推断具体分量。；原帖第二张 734×612 曲线图中，非零分量的实线/虚线在大部分横轴范围基本重合，零值线也重合，与正文所述“部分 qdot 和 diff(q) 符合预期”一致。同样因无图例、轴名和单位，不记录无法确认的物理分量。
- 独立核验引用：[maintainer_confirmation · 项目贡献者给出基于 pin.integrate 的 frame 位置有限差分代码](https://github.com/stack-of-tasks/pinocchio/issues/1140#issuecomment-610328052)；[maintainer_confirmation · 项目贡献者明确 free-flyer joint velocity 以 free flyer 局部坐标表达](https://github.com/stack-of-tasks/pinocchio/issues/1140#issuecomment-611878250)；[issue · 原作者确认根因为全局速度/积分与 Pinocchio Jacobian 不兼容，修正后得到预期结果](https://github.com/stack-of-tasks/pinocchio/issues/1140#issuecomment-614654251)；[issue · 原回复者明确更正前面对 getFrameVelocity 的说明](https://github.com/stack-of-tasks/pinocchio/issues/1140#issuecomment-613355302)
- 适用边界：适用于 Pinocchio 浮动基模型的 frame Jacobian 与数值微分验证；原帖未说明版本和具体机器人。

### Pinocchio 配置维度 nq 与速度维度 nv 不相等

- `problem_id`：`problem.joint_mapping_frames_conventions.pinocchio_nq_nv_manifold_735`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 中 nq 与 nv 不等以及 URDF 默认固定基的两个常见来源**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：维护者解释 q 是配置向量、v 是配置流形的切向量；四元数用 4 个配置分量表示 3 维角速度，所以一般 nq≥nv，不能用 q+=v 或 q1-q0 代替 integrate/difference。对原帖 HRP2 的异常倍数，维护者指出 URDF 使用了 continuous joint 参数化；作者把相关 joint type 改为 revolute 后确认 nq/nv 符合预期。但 continuous 与 revolute 的边界语义不同，工程上应先确认模型意图，不能只为对齐维度而改类型。
- 证据状态：`issue_candidate`
- 来源定位：Issue #735，流形解释 issuecomment-472342263；continuous 诊断 issuecomment-472343366；作者复测 issuecomment-472506592
- 原帖/精确回复：[Pinocchio 中 nq 与 nv 不等以及 URDF 默认固定基的两个常见来源](https://github.com/stack-of-tasks/pinocchio/issues/735#issuecomment-472506592)
- 平台/作者：GitHub Issues / ShihaoWang
- 关键术语：配置流形（configuration manifold）；切向量（tangent vector）；连续关节（continuous joint）；四元数（quaternion）
- 环境：2019 年 Pinocchio C++/Python；HRP2、ATLAS、TALOS URDF；具体软件版本未说明。
- 症状：HRP2 导入后 model.nq=60、model.nv=30，配置维度看似是速度维度两倍。；TALOS 直接 buildModel 后 model.nq=model.nv=32，没有预期的浮动基 7/6 个分量。
- 诊断：检查模型中的 spherical、FreeFlyer 和 continuous joint 参数化；不能把 nq 直接当作物理自由度数。；检查 buildModel 调用是否显式传入 JointModelFreeFlyer root_joint。
- 原因：四元数以 4 个配置分量表示 3 维角速度，continuous joint 也使用 nq 与 nv 不同的流形参数化。；URDF 本身不包含浮动基 joint，直接 buildModel 会把 base 固定到 universe。
- 处理过程：作者把 HRP2 中相关 joint type 从 continuous 改为 revolute 后重新查看 nq/nv。；作者按建议在 buildModel 时传入 JointModelFreeFlyer 后重新导入 TALOS。
- 有效处理：对配置采样、积分和差分使用 randomConfiguration、integrate 和 difference/differentiate 等流形接口，不直接 q+=v 或 q1-q0。；需要浮动基时显式调用带 JointModelFreeFlyer root_joint 的 buildModel 重载。
- 结果：作者把 continuous 改为 revolute 后报告 HRP2 的 nq/nv 符合其预期。；作者加入 FreeFlyer 后得到 TALOS model.nq=39、model.nv=38，与维护者预期一致。
- 限制：continuous 与 revolute 具有不同的角度边界语义，不能仅为让维度相等而在实际模型中盲目替换。；q\[0:3\] 与 q\[3:7\] 的 base translation/quaternion 排列只适用于已显式加入 FreeFlyer 的模型。；线程基于 2019 年接口；当前版本函数命名和 overload 应另行核对。
- 独立核验引用：[maintainer_confirmation · 维护者解释 quaternion 导致 nq 与 nv 不同，并要求使用流形 integrate/differentiate](https://github.com/stack-of-tasks/pinocchio/issues/735#issuecomment-472342263)；[maintainer_confirmation · 维护者指出原 HRP2 使用 continuous joint representation](https://github.com/stack-of-tasks/pinocchio/issues/735#issuecomment-472343366)；[issue · 原作者修改 joint type 后确认 nq/nv 变化符合解释](https://github.com/stack-of-tasks/pinocchio/issues/735#issuecomment-472506592)
- 适用边界：适用于原帖 2019 年 Pinocchio 和 HRP2/ATLAS/TALOS URDF；具体 joint 的 nq/nv 应从当前模型逐项确认。

### 从 URDF 构建 Pinocchio humanoid 模型时遗漏浮动基

- `problem_id`：`problem.joint_mapping_frames_conventions.pinocchio_urdf_freeflyer_735`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 中 nq 与 nv 不等以及 URDF 默认固定基的两个常见来源**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：项目贡献者说明，浮动基不在普通 URDF 中，直接 buildModel(filename, model) 会把 base 固定到 universe，q 中没有 base position/orientation。需要 humanoid 浮动基时，应构造 JointModelFreeFlyer root_joint 并调用带 root_joint 的 buildModel 重载。原作者按此修改后得到 TALOS model.nq=39、model.nv=38；相较固定基的 32/32，配置增加 7、速度增加 6。
- 证据状态：`issue_candidate`
- 来源定位：Issue #735，FreeFlyer 构建说明 issuecomment-472519415；作者复测 issuecomment-472560163
- 原帖/精确回复：[Pinocchio 中 nq 与 nv 不等以及 URDF 默认固定基的两个常见来源](https://github.com/stack-of-tasks/pinocchio/issues/735#issuecomment-472560163)
- 平台/作者：GitHub Issues / ShihaoWang
- 关键术语：自由浮动基（free-flyer base）；固定基（fixed base）；机器人描述格式（Unified Robot Description Format, URDF）；广义配置（generalized configuration）
- 环境：2019 年 Pinocchio C++/Python；HRP2、ATLAS、TALOS URDF；具体软件版本未说明。
- 症状：HRP2 导入后 model.nq=60、model.nv=30，配置维度看似是速度维度两倍。；TALOS 直接 buildModel 后 model.nq=model.nv=32，没有预期的浮动基 7/6 个分量。
- 诊断：检查模型中的 spherical、FreeFlyer 和 continuous joint 参数化；不能把 nq 直接当作物理自由度数。；检查 buildModel 调用是否显式传入 JointModelFreeFlyer root_joint。
- 原因：四元数以 4 个配置分量表示 3 维角速度，continuous joint 也使用 nq 与 nv 不同的流形参数化。；URDF 本身不包含浮动基 joint，直接 buildModel 会把 base 固定到 universe。
- 处理过程：作者把 HRP2 中相关 joint type 从 continuous 改为 revolute 后重新查看 nq/nv。；作者按建议在 buildModel 时传入 JointModelFreeFlyer 后重新导入 TALOS。
- 有效处理：对配置采样、积分和差分使用 randomConfiguration、integrate 和 difference/differentiate 等流形接口，不直接 q+=v 或 q1-q0。；需要浮动基时显式调用带 JointModelFreeFlyer root_joint 的 buildModel 重载。
- 结果：作者把 continuous 改为 revolute 后报告 HRP2 的 nq/nv 符合其预期。；作者加入 FreeFlyer 后得到 TALOS model.nq=39、model.nv=38，与维护者预期一致。
- 限制：continuous 与 revolute 具有不同的角度边界语义，不能仅为让维度相等而在实际模型中盲目替换。；q\[0:3\] 与 q\[3:7\] 的 base translation/quaternion 排列只适用于已显式加入 FreeFlyer 的模型。；线程基于 2019 年接口；当前版本函数命名和 overload 应另行核对。
- 独立核验引用：[maintainer_confirmation · 项目贡献者说明直接 URDF 构建是 fixed-base，并给出 JointModelFreeFlyer 重载](https://github.com/stack-of-tasks/pinocchio/issues/735#issuecomment-472519415)；[issue · 原作者加入 FreeFlyer 后确认 TALOS nq=39、nv=38](https://github.com/stack-of-tasks/pinocchio/issues/735#issuecomment-472560163)
- 适用边界：适用于原帖 Pinocchio URDF parser 和需要 6-DoF floating base 的 humanoid；固定基任务不应加入该 root joint。

### Pinocchio 浮动基配置与速度的坐标系约定

- `problem_id`：`problem.joint_mapping_frames_conventions.pinocchio_freeflyer_velocity_frame_1137`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 浮动基 q 与 v 使用不同坐标表达**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：不是。维护者确认，base translation 在 parent frame 表达；原帖的根关节 parent 是 world，所以 q 中基座位置和四元数是全局位姿。广义速度 v 的基座线速度和角速度则在 base/body frame 表达，之后才是 joint velocities。线程没有回答 ccrba/centroidal momentum 或 ZYX Euler 根关节的后续问题，因此这张卡只覆盖 FreeFlyer q/v 的基本约定。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1137，维护者确认 issuecomment-608520990；未回答的后续边界 issuecomment-1051994666、issuecomment-1133769283
- 原帖/精确回复：[Pinocchio 浮动基 q 与 v 使用不同坐标表达](https://github.com/stack-of-tasks/pinocchio/issues/1137#issuecomment-608520990)
- 平台/作者：GitHub Issues / xinsongyan
- 关键术语：广义配置（generalized configuration）；广义速度（generalized velocity）；父坐标系（parent frame）；机体坐标系（body frame）
- 环境：2020 年 Pinocchio floating-base robot；用户此前使用 RBDL；具体版本和机器人未说明。
- 症状：用户不确定 q 中基座位姿和 v 中基座线/角速度应使用 world 还是 local frame。
- 诊断：分别核对 configuration 的 base translation/quaternion 与 tangent velocity 的表达坐标，不假设二者都在 world frame。
- 原因：Pinocchio 的配置位置和广义速度采用不同表达约定。
- 处理过程：作者先给出从小规模试验推断的 q/v 排列，请维护者确认。
- 有效处理：输入 Pinocchio 广义速度前，把浮动基线速度和角速度表示到 base/body frame；q 的 base translation 仍在 parent/world frame。
- 结果：维护者明确确认作者给出的 q/v 约定正确。
- 限制：线程只确认 FreeFlyer q/v 的基本表达；后续关于 ccrba、centroidal momentum、JointModelSphericalZYX 和 ABA 的追问未获回答。；没有给出从具体估计器或仿真器坐标系到 body frame 的转换代码。
- 独立核验引用：[maintainer_confirmation · 维护者确认 base translation 在 parent/world 表达，而 velocity 在 body frame 表达](https://github.com/stack-of-tasks/pinocchio/issues/1137#issuecomment-608520990)
- 适用边界：适用于原帖 Pinocchio FreeFlyer 基本 q/v 输入；其他 root joint、centroidal API 和仿真器状态需单独核对。

### Pinocchio 浮动基广义加速度的局部坐标约定

- `problem_id`：`problem.joint_mapping_frames_conventions.pinocchio_freeflyer_acceleration_frame_1656`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio ABA 返回的浮动基广义加速度按局部坐标表达**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原作者把输出定义写为 a=\[base-frame linear acceleration, base-frame angular acceleration, joint accelerations\]，维护者明确确认正确。因此不能直接把 aba 输出前六维当作 world-frame base acceleration。线程没有给 local-to-world acceleration 变换，也没有澄清 classical 与 spatial acceleration 的差异；涉及这些量时必须继续依据目标 API 定义核对。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1656，问题定义与维护者确认 issuecomment-1134709342
- 原帖/精确回复：[Pinocchio ABA 返回的浮动基广义加速度按局部坐标表达](https://github.com/stack-of-tasks/pinocchio/issues/1656#issuecomment-1134709342)
- 平台/作者：GitHub Issues / FenglongSong
- 关键术语：关节体算法（articulated-body algorithm, ABA）；广义加速度（generalized acceleration）；局部关节坐标系（local joint frame）；空间加速度（spatial acceleration）
- 环境：2022 年 Pinocchio floating-base dynamics；具体版本和机器人未说明。
- 症状：用户已知 v 的浮动基分量在 local joint frame，但不确定 a 是否采用相同表达。
- 诊断：把 aba 输出解释为配置流形切空间中的广义加速度，并核对根关节局部坐标约定。
- 原因：将广义加速度误认为 world-frame 的普通二阶位置导数。
- 处理过程：作者列出 a=\[local base linear acceleration, local base angular acceleration, joint accelerations\] 请维护者确认。
- 有效处理：按 base local frame 解释 aba 输出的前六维；需要 world-frame 量时再做与目标定义匹配的显式变换。
- 结果：维护者明确确认作者的局部坐标解释正确。
- 限制：线程没有给出 local-to-world acceleration 转换，也没有讨论 spatial acceleration、classical acceleration 与 d(v)/dt 的差别。；具体 root joint 类型和软件版本未说明。
- 独立核验引用：[maintainer_confirmation · 维护者确认 aba 广义加速度按作者所列 base local frame 定义](https://github.com/stack-of-tasks/pinocchio/issues/1656#issuecomment-1134709342)
- 适用边界：适用于原帖 Pinocchio floating-base aba() 输出解释；不能外推到未说明的 classical acceleration 接口。

### Pinocchio 复合根关节的非线性项一致性问题

- `problem_id`：`problem.joint_mapping_frames_conventions.pinocchio_jointmodelcomposite_nle_2053`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 3 preview 的 JointModelComposite 下 C v 加 g 与 nle 不一致**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突。
- 解答状态：`unresolved`
- 候选解答：作者用 Translation+SphericalZYX 的 JointModelComposite、完整 URDF 和固定 q/v 复现了不一致；维护者明确说原因是当时尚未完整支持 JointModelComposite，并表示计划修复。线程没有修复 PR、版本或复测，Issue 仍 open，所以当前只能把它作为该 preview 环境的已确认限制和排查入口，不能宣称升级或更换接口已经解决。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2053，完整复现见正文；维护者原因确认 issuecomment-1713511072
- 原帖/精确回复：[Pinocchio 3 preview 的 JointModelComposite 下 C v 加 g 与 nle 不一致](https://github.com/stack-of-tasks/pinocchio/issues/2053#issuecomment-1713511072)
- 平台/作者：GitHub Issues / matheecs
- 关键术语：复合关节模型（composite joint model）；科里奥利矩阵（Coriolis matrix）；广义重力（generalized gravity）；非线性效应（nonlinear effects, NLE）
- 环境：Ubuntu 22.04 Intel x86-64；pinocchio3-preview；作者提供完整 Python code、URDF 和输出。
- 症状：同一 q、v 下 data.nle 与 data.C@v_home+data.g 的多个分量出现可见差异。
- 诊断：用最小 URDF 和固定 q/v 同时调用 computeCoriolisMatrix、nonLinearEffects、computeGeneralizedGravity 并逐分量比较。
- 原因：维护者确认当时没有完整支持 JointModelComposite。
- 处理过程：作者提供可运行的最小代码和完整模型；维护者承认支持缺口并表示会尝试修复。
- 结果：根因范围被维护者指向 JointModelComposite 支持不完整，但线程没有修复结果。
- 限制：Issue 截至核对时仍为 open，未链接修复 PR/commit、修复版本或回归测试。；不能据此推断当前稳定版仍有相同问题，也不能把改用其他 root joint 写成已验证修复。
- 独立核验引用：[issue · 作者提供完整 Python 复现、URDF、环境和不一致输出](https://github.com/stack-of-tasks/pinocchio/issues/2053)；[maintainer_confirmation · 维护者把原因指向 JointModelComposite 尚未完整支持](https://github.com/stack-of-tasks/pinocchio/issues/2053#issuecomment-1713511072)
- 适用边界：严格限于原帖 Ubuntu 22.04 x86-64、pinocchio3-preview 和所给 JointModelComposite；其他版本需要重新运行相同一致性检查。

## model_asset_and_urdf_usd (`model_asset_and_urdf_usd`)

### Pinocchio Python 如何把指定关节固定在参考配置，并在需要显示时同步缩减几何模型？

- `problem_id`：`problem.model_asset_and_urdf_usd.bd0fa4cb8c9f23df`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio Python 可按参考配置锁定关节，并按需同时缩减几何模型**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：使用 pinocchio.buildReducedModel，而不是未限定命名空间的 buildReducedModel。待锁对象应通过 model.getJointId 获取 Joint ID；第三个参数 reference_configuration 用来计算锁定关节的放置。只需要运动学/动力学模型时调用 model 重载；还要显示时传入 visual_model，并接收缩减后的 model 与 visual_model。原帖用户确认命名空间修正并分享了工作片段，但其具体参考向量没有经过线程内独立验证。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1232，维护者 API 说明 issuecomment-639461045、命名空间说明 issuecomment-640721560、用户工作片段 issuecomment-641755486
- 原帖/精确回复：[Pinocchio Python 可按参考配置锁定关节，并按需同时缩减几何模型](https://github.com/stack-of-tasks/pinocchio/issues/1232#issuecomment-641755486)
- 平台/作者：GitHub Issues / julesser
- 关键术语：缩减模型（reduced model）；参考配置（reference configuration）；关节索引（joint index）；几何模型（GeometryModel）
- 环境：robotpkg-py36-pinocchio；Python 3.6 路径；RH5 浮动基人形 URDF；RobotWrapper.BuildFromURDF。
- 症状：直接调用 buildReducedModel 报 NameError；早期草稿用 getFrameId 收集待锁关节，且不清楚参考配置和几何模型重载。
- 诊断：确认函数在 pinocchio 命名空间；用 existJointName/getJointId 获取 Joint ID；参考配置必须用于计算锁定关节位姿；需要显示时检查 visual_model 是否同步缩减。
- 原因：未使用 pinocchio.buildReducedModel 命名空间；混淆 Frame ID 与 Joint ID；未区分只缩减运动学模型和同时缩减几何模型的重载。
- 处理过程：维护者贴出 Python docstring；用户按官方 C++ 示例改写 Python 代码并继续修正命名空间和 Joint ID。
- 有效处理：调用 pin.buildReducedModel(model, joint_ids, reference_configuration)；需要显示时调用带 geometry_model 的重载并接收 model、geometry_model 两个返回值。
- 结果：用户确认命名空间修正正确，并分享其 working Python 片段；两位维护者建议把示例贡献到正式文档。
- 限制：用户片段的浮动基前 7 个参考配置全部写为 0，线程没有讨论该四元数是否合法，也没有给出测试输出；不应把整段数值原样视为通用模板。
- 独立核验引用：[official_documentation · 维护者在原线程引用 Python 绑定 docstring 和两个重载](https://github.com/stack-of-tasks/pinocchio/issues/1232#issuecomment-639461045)；[maintainer_confirmation · 维护者确认函数位于 pinocchio 命名空间](https://github.com/stack-of-tasks/pinocchio/issues/1232#issuecomment-640721560)；[issue · 用户分享其 working Python 片段并区分可视化几何重载](https://github.com/stack-of-tasks/pinocchio/issues/1232#issuecomment-641755486)
- 适用边界：适用于线程所示 Python 绑定和 RobotWrapper 浮动基模型；目标版本的函数签名仍应通过本地 help/docstring 核对。

### Pinocchio 解析 continuous 关节后为什么 nq=2、nv=1，配置和速度应怎样理解？

- `problem_id`：`problem.model_asset_and_urdf_usd.438e2524f327caf6`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 连续转动关节用 cosθ、sinθ 表示配置，因此 nq=2 而 nv=1**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：这是预期设计。项目 contributor 明确说明 continuous 关节的配置使用 SO(2) 复数表示，即 cos(theta)、sin(theta)，所以配置维数 nq 为 2；关节速度仍是单一 theta_dot，所以 nv 为 1。它与球关节用四元数表示配置、但切空间维数更小的思路相同。构造状态和索引时应分别使用模型给出的 nq 与 nv。
- 证据状态：`issue_candidate`
- 来源定位：Issue #794，项目 contributor 回复 issuecomment-490049010 与 issuecomment-490050573
- 原帖/精确回复：[Pinocchio 连续转动关节用 cosθ、sinθ 表示配置，因此 nq=2 而 nv=1](https://github.com/stack-of-tasks/pinocchio/issues/794#issuecomment-490050573)
- 平台/作者：GitHub Issues / mkatliar
- 关键术语：连续关节（continuous joint）；配置空间（configuration space）；切空间（tangent space）；二维特殊正交群（two-dimensional special orthogonal group, SO2）
- 环境：最小 C++/URDF 示例；Pinocchio 2019 年线程；具体发布版本未说明。
- 症状：单个 continuous 关节得到 model.nq==2，原测试预期 nq==1 因而断言失败。
- 诊断：分别检查 model.nq、model.nv 和关节模型类型；不要用 URDF 非固定关节数量直接推断配置向量长度。
- 原因：Pinocchio 用 cos(theta)、sin(theta) 的 SO(2) 表示承载无界角度配置，而不是直接存一个 theta。
- 处理过程：提问者将 continuous 改为 revolute 对照；项目 contributor 解释两种配置表示和共同的单一速度维度。
- 有效处理：这不是需要修复的 bug；按关节模型的 nq/nv 布局构造配置与速度，连续角配置写成合法的 cos(theta)、sin(theta)。
- 结果：提问者确认已经理解；维护者准备把说明补入关节文档。
- 限制：原线程只解释表示法，没有给出如何把上下限映射到切空间；限位问题需单独处理。
- 独立核验引用：[maintainer_confirmation · 项目 contributor 解释 continuous 的 cos/sin 配置与单一 theta_dot 速度](https://github.com/stack-of-tasks/pinocchio/issues/794#issuecomment-490050573)；[issue · 提问者确认解释清楚](https://github.com/stack-of-tasks/pinocchio/issues/794#issuecomment-490090729)
- 适用边界：适用于 Pinocchio 从 URDF continuous 关节构造的无界转动关节模型；有界 revolute 关节仍使用单一角配置。

### Pinocchio 固定基 MJCF 的 contact model 在 Python 中为空

- `problem_id`：`problem.model_asset_and_urdf_usd.pinocchio_fixed_mjcf_contacts_2854`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 3.9 固定基 MJCF 的 Python 快捷接口会漏返回 contact models**

- 独立等级：**值得参考** — 问题现象有另一位项目成员独立复现，Pinocchio 4 修复由维护者声明；缺少升级后复测与本轮补丁核验，因此列为值得参考。
- 解答状态：`resolved`
- 候选解答：原帖用同一 MJCF 对照出固定基 0 个、FreeFlyer 1 个 contact model，另一位项目成员又在 Nix 环境复现了相同输出。维护者最终写明该问题已在 Pinocchio 4 修复并链接 PR #2855。因此可把升级 Pinocchio 4 作为线程内已确认的处理方向；但由于原帖没有贴升级复测，也没有给出 3.x 补丁，升级后仍应对返回数量和实际约束做最小测试。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2854，独立复现 issuecomment-3996776812；维护者修复说明 issuecomment-4288817479
- 原帖/精确回复：[Pinocchio 3.9 固定基 MJCF 的 Python 快捷接口会漏返回 contact models](https://github.com/stack-of-tasks/pinocchio/issues/2854#issuecomment-4288817479)
- 平台/作者：GitHub Issues / OscarMrZ
- 关键术语：接触模型（contact model）；固定基（fixed base）；自由浮动基（FreeFlyer）；语言绑定（Python bindings）
- 环境：Ubuntu 22.04；uv/pip；pin 3.9.0；另有 Nix/nixpkgs Python Pinocchio 独立复现。
- 症状：同一 MJCF 中，固定基调用输出 contact models=0，FreeFlyer 调用输出 contact models=1。
- 诊断：用同一文件分别执行无 root_joint 和显式 JointModelFreeFlyer 两条加载路径，直接比较返回 contact model 数量。
- 原因：Issue 正文指出 Python shortcuts.py 的条件检查及无 root_joint/root_joint_name 时缺少返回 contact models 的绑定路径；维护者没有在评论中进一步解释内部机制。
- 处理过程：项目成员用 Nix 环境和原最小脚本独立复现；维护者检查后指向 Pinocchio 4 与 PR #2855。
- 有效处理：维护者明确说明升级到 Pinocchio 4 后该问题已修复。
- 结果：原 Issue 被标记为 Pinocchio 4 已修复；线程内没有升级后输出，也没有 3.x workaround。
- 限制：未读取 PR #2855 的补丁细节，不能据此描述具体代码修改；升级前仍应对固定基返回列表做显式断言。
- 独立核验引用：[independent_reproduction · 另一位项目成员用 Nix 运行原脚本，得到固定基 0、FreeFlyer 1](https://github.com/stack-of-tasks/pinocchio/issues/2854#issuecomment-3996776812)；[maintainer_confirmation · 维护者说明已在 Pinocchio 4 修复并链接 PR #2855](https://github.com/stack-of-tasks/pinocchio/issues/2854#issuecomment-4288817479)；[pull_request · 维护者从 Issue 链接的 PR 评论；本轮未读取补丁 diff](https://github.com/stack-of-tasks/pinocchio/pull/2855#issuecomment-4236363128)
- 适用边界：适用于 pin 3.9.0 的 Python buildModelsFromMJCF 固定基路径；Pinocchio 4 的具体最低版本和回归行为需在目标环境核对。

### Unitree H1_2 从 Isaac Gym 迁移到 Isaac Lab 的模型与训练检查项

- `problem_id`：`problem.model_asset_and_urdf_usd.h1_2_isaaclab_migration_2324`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：H1_2 从 Isaac Gym 迁移到 Isaac Lab 时要同时检查迭代次数、碰撞集合和 acceleration reward**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：实践者先用官方脚本把 H1_2 URDF 转为 USD并替换 H1 环境模型，随后报告三项处理：因关节增加、模型更大，把一个未指明名称的 iterative-solution 数量从 4 提到 400以避免异常运动；把全部上身关节加入与地面的碰撞检测；发现 acceleration reward 比例过大，并建议在 TensorBoard 逐项观察 reward。该用户称基本实现了行走，但没有给字段名、配置、版本或曲线，因此这些只能作为迁移检查清单，不能照抄 400 或 reward 比例。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2324，维护者可行性说明 issuecomment-2813752561；实践者迁移结果 issuecomment-2896934209
- 原帖/精确回复：[H1_2 从 Isaac Gym 迁移到 Isaac Lab 时要同时检查迭代次数、碰撞集合和 acceleration reward](https://github.com/isaac-sim/IsaacLab/issues/2324#issuecomment-2896934209)
- 平台/作者：GitHub Issues / GitHub 用户（原候选未保留用户名）
- 关键术语：模型迁移（model migration）；关节顺序（joint order）；碰撞检测（collision detection）；加速度奖励（acceleration reward）
- 环境：Unitree RL Gym/Isaac Gym 到 Isaac Lab；用户称使用官方 URDF→USD 转换脚本；具体 Isaac Lab、Isaac Sim、GPU 和训练配置未说明。
- 症状：H1_2 关节更多、模型更大时出现异常模型运动。；头部和身体关节与地面的碰撞没有按预期进入检测。；调试时 acceleration reward 比例过大。
- 诊断：替换模型后核对新增关节、求解迭代配置和训练中各 reward term 的 TensorBoard 数值。；显式检查上身各 link 是否进入与地面的 collision detection/termination 集合。
- 原因：实践者把异常运动与模型增大后迭代次数不足联系起来。；碰撞检测集合没有覆盖全部上身关节；acceleration reward 权重相对过大。
- 处理过程：用官方脚本把 H1_2 URDF 转为 USD并替换 H1 环境模型；将未指明配置项的迭代次数从 4 提到 400；把所有上身关节加入碰撞检测；观察 TensorBoard reward。
- 有效处理：上述实践者报告该组合基本实现行走，并分别缓解异常运动与碰撞检测问题。
- 结果：实践者称基本实现 walking function；另一用户表示建议有帮助，但原作者没有复测回复。
- 限制：“iterative solutions”没有对应到具体 Isaac Lab/PhysX 配置字段，不能直接把 400 写进任意配置。；没有公开训练时长、成功率、reward 最终比例、代码或版本，无法确认跨环境复现。；维护者只确认迁移可行和欢迎贡献，没有核验实践者的具体参数。
- 安全提示：实机前必须重新核对 H1_2 的 joint order、limit、collision body 与 actuator mapping；原线程只报告仿真 walking。
- 独立核验引用：[maintainer_confirmation · 维护者确认迁移可行、计划支持并欢迎贡献，但未给具体参数](https://github.com/isaac-sim/IsaacLab/issues/2324#issuecomment-2813752561)；[issue · 实践者报告 URDF→USD、迭代次数、碰撞集合和 acceleration reward 的实际处理及基本行走结果](https://github.com/isaac-sim/IsaacLab/issues/2324#issuecomment-2896934209)
- 适用边界：适用于从 H1 配置派生 H1_2 的 Isaac Lab 仿真迁移排查；具体 solver 字段和 reward 权重必须结合目标版本验证。

## realtime_control_latency (`realtime_control_latency`)

### ros2_control 实时循环中栈与堆分配的审计边界

- `problem_id`：`problem.realtime_control_latency.ros2_control_stack_vs_heap_allocation_668`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ros2_control 实时循环中栈分配与堆分配的区别**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原线程的核心区分是：栈上分配通常只是可确定的指针调整，并不因为出现局部变量就一定有问题；默认堆分配则不具有内在确定性。要审计对象内部的 std::string、container/resize、logging 和 std::make_shared。具体处理方向是在实时环前按已知上界预分配，或使用 TLSF 类确定分配器并同时验证初始化路径。该线程没有证明整个代码库已清理完毕，因此只能作为审计方法，不能当作实时验收结果。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #668 正文的 write()/update() 例子；issuecomment-1062676446 的栈/堆、TLSF、logging 与 make_shared 分析；issuecomment-1064190493 的项目成员确认；issuecomment-1109814018 的预分配选择
- 原帖/精确回复：[ros2_control 实时循环中栈分配与堆分配的区别](https://github.com/ros-controls/ros2_control/issues/668)
- 平台/作者：GitHub Issues / AndyZe
- 关键术语：实时循环（real-time loop）；栈分配（stack allocation）；堆分配（heap allocation）；确定分配器（deterministic allocator）；预分配（pre-allocation）；最坏情况执行时间（worst-case execution time, WCET）
- 环境：原帖引用 ros2_control commit 6b495ef86889cbfdc1ee22ac77efa2ff589727ee 的 actuator.cpp，并引用 ros2_controllers commit b9ccf04aa95203e37077f297ddcf9f933ef464fa 的 joint_trajectory_controller.cpp。
- 症状：update() 中声明三个 JointTrajectoryPoint，随后根据 joint_names_.size() 调用 resize_joint_trajectory_point。；同一线程还指出确定性路径中存在日志和 std::make_shared。
- 诊断：对每个局部对象审计其构造、resize、string/container 成员和智能指针，而不是仅搜索局部变量声明。；单独审计 logging 与 std::make_shared 是否进入必须确定的 read/update/write 路径。；若使用确定分配器，还要确认对象初始化本身也是确定的。
- 原因：将“声明局部变量”与“从堆动态分配”等同，会错过两者的确定性差异。；实际风险来自对象内部容器扩容、默认堆分配、日志和共享指针构造等执行时不可预测操作。
- 处理过程：线程讨论了提前预分配足够大的缓冲区，以及使用 TLSF 确定分配器。；对 joint_trajectory_controller 的具体选择是以 joint_names_.size() 作为命令长度上界，在实时循环前预分配。
- 结果：项目成员认可代码库中一些位置需要清理，但该 Issue 没有给出完成全库审计或已合并修复的证据。；Issue 在 2025 年由 stale bot 关闭，关闭原因是长期无活动，不是技术整改验收。
- 限制：栈上分配通常是 O(1) 的说明不等于任意类的构造都无堆分配；必须逐类审计。；TLSF 只解决分配器确定性的一部分，原回复明确提醒初始化逻辑也必须确定。；线程没有提供延迟直方图、最坏情况执行时间或硬实时验收数据。
- 安全提示：真机 WBC 不应因为“已预分配”就默认满足硬实时；还需在目标负载、调度和日志配置下测量最坏延迟。
- 独立核验引用：[issue · 原作者给出 update() 中声明并 resize 三个消息对象的具体代码](https://github.com/ros-controls/ros2_control/issues/668#issuecomment-1062314553)；[issue · 详细区分栈与堆、指出 TLSF 和初始化边界，并补充 logging/make_shared 风险](https://github.com/ros-controls/ros2_control/issues/668#issuecomment-1062676446)；[maintainer_confirmation · 项目成员确认代码库中一些位置需要清理](https://github.com/ros-controls/ros2_control/issues/668#issuecomment-1064190493)；[issue · 原作者决定以 joint_names_.size() 为上界预分配](https://github.com/ros-controls/ros2_control/issues/668#issuecomment-1109814018)；[issue · stale bot 明确记录 Issue 因 45 天无活动而关闭，不是修复验收](https://github.com/ros-controls/ros2_control/issues/668#issuecomment-3044884623)
- 适用边界：适用于 ros2_control 及其他需要确定性的 WBC read/update/write 循环；原线程对应 2022 年代码快照，当前版本需重新审计。

### ros2_control 诊断互斥锁的实际保护对象

- `problem_id`：`problem.realtime_control_latency.ros2_control_diagnostic_controller_list_mutex_851`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ros2_control 诊断互斥锁保护的是控制器列表而非控制器执行**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：按项目成员对当时实现的解释，该 mutex 固定的是存储控制器的列表，使非实时回调读取时列表不发生变化；它禁止同时加载新控制器，而加载本身不属于实时路径。因此不能从注释“lock controllers”直接推断 update 执行被锁。不过原线程没有延迟基准，目标版本仍应用调用路径审计与周期测量验证。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #851 正文的 mutex 代码；issuecomment-1306113645 的调用路径解释；issuecomment-1306115705 的作者确认；issuecomment-1306670347 的列表而非控制器本身澄清
- 原帖/精确回复：[ros2_control 诊断互斥锁保护的是控制器列表而非控制器执行](https://github.com/ros-controls/ros2_control/issues/851)
- 平台/作者：GitHub Issues / AndyZe
- 关键术语：互斥锁（mutex）；递归互斥锁（recursive mutex）；控制器列表（controller list）；非实时回调（non-real-time callback）；锁竞争（lock contention）
- 环境：原帖对应 2022-11-07 合入的 ros2_control PR #820 和当时 master 分支的 controller_manager 实现；未指定 ROS 2 发行版。
- 症状：代码注释写着 lock controllers，并对 controllers_lock_ 创建 std::lock_guard<std::recursive_mutex>，从字面看像是在诊断回调中锁住控制器。
- 诊断：沿 controllers_lock_ 查看所有读写点，确认它保护的是列表结构、控制器对象还是 update() 执行。；区分非实时的 load controller 操作与实时控制器 update 路径。
- 原因：注释“lock controllers”过于简略，容易把“锁定存储列表”误解为“锁定控制器执行”。
- 处理过程：项目成员引用 controller_manager 的加载路径，说明锁持有期间禁止的是加载新控制器。；作者在看到调用路径解释后回复表示问题已清楚。
- 有效处理：不需要因该处代码将诊断功能整体删除；应先按保护对象和调用路径核对实际锁竞争。
- 结果：原作者接受解释，Issue 以 completed 关闭；项目成员在关闭后补充它锁的是控制器存储列表，不是控制器本身。
- 限制：线程只解释锁的语义与调用路径，没有给出诊断回调下的延迟测量或最坏阻塞时间。；该结论对应 2022 年实现；后续版本必须重新检查锁的使用位置。
- 安全提示：对真机硬实时 WBC，调用路径分析只能排除误读；仍要在最坏诊断负载下测量控制周期抖动。
- 独立核验引用：[pull_request · 原帖指向引入该诊断锁代码的 PR](https://github.com/ros-controls/ros2_control/pull/820)；[maintainer_confirmation · 项目成员说明锁用于读取时保持控制器列表不变，只禁止非实时的新控制器加载](https://github.com/ros-controls/ros2_control/issues/851#issuecomment-1306113645)；[issue · 原作者确认该解释消除疑问](https://github.com/ros-controls/ros2_control/issues/851#issuecomment-1306115705)；[maintainer_confirmation · 项目成员再次明确：锁的是存储控制器的列表，不是控制器本身](https://github.com/ros-controls/ros2_control/issues/851#issuecomment-1306670347)
- 适用边界：适用于 ros2_control PR #820 合入后、2022 年当时 controller_manager/diagnostic_updater 的锁语义；其他版本需重新追踪调用路径。

### ros2_control 仿真时间下的更新率错配

- `problem_id`：`problem.realtime_control_latency.ros2_control_sim_time_update_rate_859`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ros2_control 使用仿真时间后更新频率异常**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原线程证实将循环改为 steady_clock 可恢复墙钟 100 Hz，且原作者在多种控制器上使用；但他同时明确这不会随仿真 real-time factor 缩放，所以不是通用解。项目成员倾向让 Gazebo 一类仿真器专用插件/节点在物理更新中驱动 controller update，而不是让通用 ros2_control_node 猜测不同仿真器的 /clock 语义。当前应先明确要求的是墙钟率还是仿真时间率，再选对应集成；该线程未给出已合并的通用修复。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #859 正文的 100 Hz→2.5 kHz 复现；issuecomment-1328320634 和 -1340082821 的 steady clock 测试与边界；-1759199046/-1768649502 的跨版本复现；-1768887521/-2306470198 的仿真器专用节点建议
- 原帖/精确回复：[ros2_control 使用仿真时间后更新频率异常](https://github.com/ros-controls/ros2_control/issues/859)
- 平台/作者：GitHub Issues / joshjowen
- 关键术语：仿真时间（simulation time）；稳定时钟（steady clock）；实时因子（real-time factor, RTF）；更新率（update rate）；物理步（physics step）；时间基（time base）
- 环境：原复现：Ubuntu 22.04，ROS 2 Humble，仿真器发布 /clock，update_rate=100 Hz，use_sim_time=true。；2023-10 另有使用者分别在 Humble 和 ros-rolling-ros2-control 报告同样问题。
- 症状：原作者用 ros2 topic hz /joint_states 测到约 2.5 kHz，而配置值是 100 Hz。；使用 steady_clock 能将墙钟率固定为 100 Hz，但仿真 real-time factor=0.5 时，这等价于相对仿真时间 200 Hz。
- 诊断：同时记录 update_rate 配置、/joint_states 墙钟频率、/clock 发布行为和仿真 real-time factor，不要只看一个 topic hz 数字。；先决定所需语义：控制率是按墙钟固定，还是应随仿真时间和每个物理 step 推进。；检查仿真器是否已有 gazebo_ros2_control 一类在仿真物理更新内调用 controller update 的专用插件。
- 原因：原线程确认 ros2_control_node 的循环时钟与 use_sim_time 组合会产生错误更新率，但线程没有得出可适用所有仿真器的单一时钟实现。；项目成员指出不同仿真器可能使用 /clock 或其他 API，因此在通用 ros2_control_node 中推断仿真进度很难保持通用。
- 处理过程：原作者改用 std::chrono::steady_clock，并报告 joint_trajectory_controller、forward_command_controller 和自定义控制器按墙钟正常工作。；另一名使用者建议让仿真时间从系统时间起步并在启动 ros2_control_node 前先发布 /clock，但本人明确认为这个方案依赖启动顺序。；2024 年有使用者报告 rclcpp::Rate 对 use_sim_time 有效，但其随后给出的代码明确标注为 ChatGPT 生成版，原始试验代码已不在手边。
- 结果：项目成员给出的主要设计方向是由各仿真器专用 simulator_ros2_control 插件或节点按物理时间推进控制器，例如 Gazebo 的插件。；Issue 虽然于 2024-11 以 completed 关闭，但线程未链接一个已合并、通用于 ros2_control_node+use_sim_time 的修复。；被标注为 related 的 PR #802 仅处理 catch-up 行为，且未合并，不能当作 #859 已修复的证据。
- 限制：steady_clock 只解决墙钟周期，原作者明确它不会随仿真 real-time factor 缩放。；将仿真时间对齐系统时间的建议依赖启动顺序，回复者自己也认为并非所有环境可用。；rclcpp::Rate 的回复只有单一使用者经验，展示代码不是当时的原始测试代码，不能升级为通用解答。；真实硬件不应使用 use_sim_time；项目成员指出仿真停止时时间可始终为 0。
- 安全提示：WBC 系统必须在设计上明确控制周期使用的时间基，不要在真机使用仿真时间，也不要在未核对 real-time factor 时将墙钟 100 Hz 误当作仿真时间 100 Hz。
- 独立核验引用：[maintainer_confirmation · 项目成员认可 steady clock 方向，同时警告真实硬件不应使用 use_sim_time](https://github.com/ros-controls/ros2_control/issues/859#issuecomment-1328320634)；[issue · 原作者记录多种控制器可用，并明确 steady clock 不随仿真 real-time factor 缩放](https://github.com/ros-controls/ros2_control/issues/859#issuecomment-1340082821)；[independent_reproduction · 另一使用者在 Humble 和 Rolling 上复现](https://github.com/ros-controls/ros2_control/issues/859#issuecomment-1759199046)；[independent_reproduction · 第二名使用者在 Humble/Rolling 报告同样问题，并说明启动顺序临时方案的局限](https://github.com/ros-controls/ros2_control/issues/859#issuecomment-1768649502)；[maintainer_confirmation · 项目成员建议由各仿真器专用插件/节点处理 controller update](https://github.com/ros-controls/ros2_control/issues/859#issuecomment-1768887521)；[maintainer_confirmation · 项目成员明确通用 ros2_control_node+use_sim_time 并不好用，需要另一个与 clock 同步的节点](https://github.com/ros-controls/ros2_control/issues/859#issuecomment-2306470198)；[pull_request · 线程标注为 related，但 PR 未合并且补丁处理 catch-up，不是 #859 已修复证据](https://github.com/ros-controls/ros2_control/pull/802)；[issue · rclcpp::Rate 回复明确展示代码为 ChatGPT 版，原始试验代码不在手边，因此未作为通用修复](https://github.com/ros-controls/ros2_control/issues/859#issuecomment-2432444432)
- 适用边界：适用于仿真器发布 /clock，同时用通用 ros2_control_node 和 use_sim_time=true 的 Humble/Rolling 类环境；真机不应套用该时钟组合。

### ros2_control 加载控制器时因硬件 I/O 卡住而超时

- `problem_id`：`problem.realtime_control_latency.ros2_control_load_controller_timeout_hardware_io_2049`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ros2_control 的 load_controller 超时可由硬件 I/O 未正常返回触发**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：维护者先要求运行官方 example_2 并对照配置；作者确认 demo 可加载后，又用通用模拟系统（GenericSystem）替换自定义硬件，控制器同样恢复，因而把问题缩小到硬件 I/O。最终作者确认打开了错误串口。同时应单独核对 --param-file 中的 controller key；该 key 错写是 demo 试验中的另一问题，不要与原始根因混为一谈。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #2049，维护者 demo 建议 issuecomment-2657282641，GenericSystem 对照 issuecomment-2658038858，串口根因 issuecomment-2658104086，独立 MCU 案例 issuecomment-3101243782
- 原帖/精确回复：[ros2_control 的 load_controller 超时可由硬件 I/O 未正常返回触发](https://github.com/ros-controls/ros2_control/issues/2049#issuecomment-2658104086)
- 平台/作者：GitHub Issues / Fufs
- 关键术语：控制器管理器（controller manager）；通用模拟系统（GenericSystem）；硬件接口（hardware interface）；服务超时（service timeout）
- 环境：Ubuntu 24.04 LTS；ROS 2 Jazzy；apt 安装的 controller_manager 4.25.0；自定义 DriveBaseSystem 串口硬件接口。
- 症状：/controller_manager/load_controller 在 service list 中存在，但 joint_state_broadcaster 的 load_controller 连续三次 10 s 没有结果；list_controllers 同样超时。；gz_ros2_control 下的控制器可正常加载，原生自定义硬件路径失败。
- 诊断：按维护者建议先运行 ros2_control demo example_2，并与自己的 launch/YAML 对照。；用 GenericSystem 替换自定义硬件；如果控制器恢复加载，把排查缩小到硬件 I/O。；另行核对 --param-file 内的 controller key 是否与 launch 传入的 controller name 一致，然后核对串口和 MCU 对 read/write 的响应。
- 原因：原作者的根因是打开错误串口；GenericSystem 对照将问题从 controller 配置缩小到硬件路径。；另一名用户的类似现象来自 Arduino/ESP32 固件没有回应 Read/Write 数值；这是同类硬件 I/O 完成问题，但不是同一个具体根因。
- 处理过程：作者运行并改写 example_2，修正试验中错写的 diff_drive_controller 参数 key，确认 demo 可加载。；在原包中加入 GenericSystem 硬件模拟，控制器恢复加载。；原作者检查硬件后发现打开了错误串口。
- 有效处理：对原帖环境，改为正确的串口。对另一用户的类似现象，上传能正常响应 read/write 的正确 MCU CPP 固件。
- 结果：原作者明确确认是硬件问题和错误串口；维护者回复确认作者已找到原因。；另一名用户报告换成正确固件后控制器正常执行。
- 限制：原作者在 demo 中另外发现的 --param-file key 错写只是试验配置错误，不是原始超时的根因。；日志中的 FIFO 实时调度警告没有被原线程证明为 load_controller 超时根因。；不是每个 load_controller 超时都是串口或 MCU；必须先用 demo 和 mock hardware 做分层对照。
- 安全提示：实机上不应为让 controller 加载成功而跳过硬件读写健康检查；应在激活力矩控制前验证串口设备身份和反馈更新。
- 独立核验引用：[maintainer_confirmation · 维护者要求运行官方 example_2 并对照自定义配置](https://github.com/ros-controls/ros2_control/issues/2049#issuecomment-2657282641)；[issue · 原作者用 GenericSystem 替换硬件后控制器可加载，将问题定位到硬件路径](https://github.com/ros-controls/ros2_control/issues/2049#issuecomment-2658038858)；[issue · 原作者确认根因是打开错误串口](https://github.com/ros-controls/ros2_control/issues/2049#issuecomment-2658104086)；[issue · 独立的类似症状而非同一根因：另一名用户的 Arduino/ESP32 固件未响应 read/write，换成正确 CPP 后恢复](https://github.com/ros-controls/ros2_control/issues/2049#issuecomment-3101243782)
- 适用边界：原帖环境为 Ubuntu 24.04/ROS 2 Jazzy/controller_manager 4.25.0 的自定义串口 SystemInterface；其他中间件或控制器需重新验证分层结果。

### mc_rtc 实时控制循环出现计算时间尖峰

- `problem_id`：`problem.realtime_control_latency.mc_rtc_spikes_92`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：mc_rtc 五毫秒控制循环出现计算时间尖峰时的三项排查**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：项目成员建议同时核对三项：把 mc_rtc 的 LogPolicy 设为 threaded；确保 lipm_walking controller、lipm_walking_controller 及全部依赖以 Release 或 RelWithDebInfo 构建；关闭 CPU powersaving。作者应用三项后确认尖峰和总体耗时都明显下降。项目成员还说明 state 启动时常伴随 task/state allocation，因此仍可能出现尖峰；他们只在 deadline miss 很少发生时由系统容忍，没有宣称这是硬实时修复。
- 证据状态：`issue_candidate`
- 来源定位：Issue #92，项目成员三项诊断 issuecomment-730088491；作者复测 issuecomment-731432191
- 原帖/精确回复：[mc_rtc 五毫秒控制循环出现计算时间尖峰时的三项排查](https://github.com/jrl-umi3218/mc_rtc/issues/92#issuecomment-731432191)
- 平台/作者：GitHub Issues / Taherifar
- 关键术语：实时抖动（real-time jitter）；控制截止时间（control deadline）；线程化日志策略（threaded logging policy）；发布构建（Release build）
- 环境：2020 年 mc_rtc 与 LIPM controller；ROS；实体机器人；5 ms sampling time；CPU 和软件版本未说明。
- 症状：perf 记录出现偶发尖峰，计算时间可超过 5 ms deadline 并达到约 10 ms。
- 诊断：检查尖峰是否与新 state 启动时的 task/state 内存分配同时发生。；核对 LogPolicy、控制器及所有依赖的构建类型和 CPU 节能状态。
- 原因：默认 non-threaded 日志策略可能引入明显尖峰。；控制器或任一依赖没有以优化构建，以及 CPU powersaving，都会放大耗时；状态切换分配本身也可能产生尖峰。
- 处理过程：作者把 LogPolicy 设为 threaded，把相关控制器及依赖按 Release/RelWithDebInfo 核对，并关闭 CPU powersaving。
- 有效处理：使用 threaded LogPolicy；确保 lipm_walking controller 和 lipm_walking_controller 的全部依赖采用 Release 或 RelWithDebInfo；关闭 CPU 节能。
- 结果：作者确认三项调整对减少尖峰和整体耗时都有很大效果。
- 限制：线程没有分别量化三项措施的独立贡献，也没有给出调整后的最坏执行时间。；项目成员只说明其系统可容忍很少发生的 deadline miss；这不是硬实时或所有机器人都安全的保证。；状态开始时的 task/state allocation 尖峰仍被认为需要未来版本继续改进。
- 安全提示：部署到实体机器人前仍应测量最坏执行时间和 deadline miss 频率，并由目标系统的安全机制处理超时。
- 独立核验引用：[maintainer_confirmation · 项目成员说明状态分配尖峰并给出 LogPolicy、构建类型和 CPU 节能三项检查](https://github.com/jrl-umi3218/mc_rtc/issues/92#issuecomment-730088491)；[issue · 原作者确认应用三项后尖峰和总耗时显著降低](https://github.com/jrl-umi3218/mc_rtc/issues/92#issuecomment-731432191)
- 适用边界：适用于原帖 2020 年 mc_rtc/LIPM、ROS、5 ms 实体机器人控制循环；其他版本和控制器需重新测量。

### TSID 的 HQP 求解远慢于配置控制周期

- `problem_id`：`problem.realtime_control_latency.tsid_eiquadprog_release_222`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：TSID 的 HQP 循环从二十七毫秒恢复到两毫秒：检查 eiquadprog 的构建类型**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：作者已把 TSID 本体设为 Release，但贴出的 eiquadprog 安装命令只有 cmake ..。协作者据此指出 eiquadprog 没有显式使用 CMAKE_BUILD_TYPE=RELEASE，维护者也确认这很可能是缺失点。作者改为 cmake .. -DCMAKE_BUILD_TYPE=RELEASE 并重建后，确认单循环回到 0.002 s，完整示例少于 10 s。因此应逐个核对求解器及依赖的构建类型，而不能只检查 TSID 主库。
- 证据状态：`issue_candidate`
- 来源定位：Issue #222，协作者定位 issuecomment-1958893254；维护者确认 issuecomment-1959212460；作者复测 issuecomment-1959689788
- 原帖/精确回复：[TSID 的 HQP 循环从二十七毫秒恢复到两毫秒：检查 eiquadprog 的构建类型](https://github.com/stack-of-tasks/tsid/issues/222#issuecomment-1959689788)
- 平台/作者：GitHub Issues / hushmandesmaeili
- 关键术语：层级二次规划（hierarchical quadratic programming, HQP）；求解周期（solve cycle）；发布构建（Release build）；采样周期（sampling period）
- 环境：2024 年 TSID 源码构建与 Python 3.10 路径；Intel Xeon E3-1225 v5 @ 3.30 GHz；Pinocchio/hpp-fcl 由 robotpkg 安装；eiquadprog 最初用 cmake .. 构建。
- 症状：compute sample 约 0.00003 s、HQP setup 约 0.00020 s、HQP solve 约 0.026 s，单循环约 0.027 s，明显超过 conf.dt=0.002 s。；一个 CPU core 持续 100%，完整运行约 107–120 s，而同伴机器少于 10 s。
- 诊断：先按 compute sample、HQP setup、HQP solve 和 whole loop 分段计时，确认主要瓶颈在 HQP solve。；逐项检查 TSID 及其依赖的 CMake build type，而不是只确认 TSID 主库为 Release。；从作者贴出的安装命令发现 eiquadprog 只执行 cmake ..，没有显式 Release。
- 原因：eiquadprog 没有以 Release 模式编译；维护者称依赖缺少 Release 在其代码上通常可能带来约二十倍耗时增加。
- 处理过程：协作者建议把 eiquadprog 配置命令改为 cmake .. -DCMAKE_BUILD_TYPE=RELEASE，作者重新构建后复测。
- 有效处理：以 CMAKE_BUILD_TYPE=RELEASE 重新配置并构建 eiquadprog。
- 结果：作者确认单循环恢复到期望的 0.002 s，完整运行少于 10 s。
- 限制：维护者的 1 kHz TALOS 数据是另一台 Intel i7 2.8 GHz 系统的项目经验，不是原作者机器的基准。；线程没有提供修改前后同一机器的完整统计分布，也没有证明所有 TSID 应用都能达到 0.5–1 kHz。；site-packages/dist-packages 的布局建议与本次 HQP 性能根因无关。
- 独立核验引用：[maintainer_confirmation · 项目协作者从安装命令定位到 eiquadprog 未显式采用 Release](https://github.com/stack-of-tasks/tsid/issues/222#issuecomment-1958893254)；[maintainer_confirmation · 项目成员确认这很可能是缺失点](https://github.com/stack-of-tasks/tsid/issues/222#issuecomment-1959212460)；[issue · 原作者确认改为 Release 后循环为 0.002 s、完整运行少于 10 s](https://github.com/stack-of-tasks/tsid/issues/222#issuecomment-1959689788)
- 适用边界：适用于原帖 TSID Exercise 2、eiquadprog 源码构建和所述 Intel Xeon/Python 3.10 环境；其他 HQP solver 或二进制包需要分别定位。

## retargeting_dataset_quality (`retargeting_dataset_quality`)

### 重定向动作回放看似正常，但 Whole Body Tracking 训练一开始就反复终止、mean episode length 卡在 1，先检查什么？

- `problem_id`：`problem.retargeting_dataset_quality.fc4d7943210bfc6b`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：重定向动作的训练帧率与预测帧率不一致导致 episode 长度停在 1**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原帖提问者的实际原因是修改了帧率与时序参数，导致学习无法进行；其结论是训练帧率（training frame rate）必须与预测帧率（prediction frame rate）相同。排查时应把参考动作采样、训练环境步进和策略预测频率逐项对齐。该线程没有公开具体参数值和修复后指标，所以这是一条已由原作者确认、但仍需按目标版本核对的经验。
- 证据状态：`issue_candidate`
- 来源定位：Issue #44，提问者自答 issuecomment-3515636113
- 原帖/精确回复：[重定向动作的训练帧率与预测帧率不一致导致 episode 长度停在 1](https://github.com/HybridRobotics/whole_body_tracking/issues/44#issuecomment-3515636113)
- 平台/作者：GitHub Issues / LuminousLark
- 关键术语：训练帧率（training frame rate）；预测帧率（prediction frame rate）；平均回合长度（mean episode length）；动作重定向（motion retargeting）
- 环境：HybridRobotics/whole_body_tracking；Unitree 重定向 LAFAN1 dance2_subject1.csv；4096 个 G1 环境；训练约 12 小时；具体提交和软件版本未说明。
- 症状：Mean episode length 为 1.00；error_body_pos=0.6723；error_joint_pos=0.3092；error_anchor_pos=0.3256；error_anchor_rot=0.6611；anchor_pos 与 ee_body_pos 终止项大量触发。
- 诊断：在确认重定向 npz 的可视回放没有明显几何错位后，继续核对训练、预测和参考动作的帧率及时序参数。
- 原因：提问者明确确认自己修改了帧率与时序相关参数，使学习过程无法推进。
- 处理过程：提问者恢复训练帧率与预测帧率的一致性，并在原线程说明问题已解决。
- 有效处理：让训练帧率（training frame rate）与预测帧率（prediction frame rate）保持一致。
- 结果：提问者将 Issue 关闭为 completed 并明确写明问题已解决；原帖未提供修复后的 episode length 或误差数值。
- 限制：原帖没有给出被修改的具体参数名、原值/修正值、代码版本及修复后的量化曲线；不能把所有 episode length=1 的问题都归因于帧率。
- 独立核验引用：[maintainer_confirmation · 提问者明确确认原因、处理原则并说明问题已解决](https://github.com/HybridRobotics/whole_body_tracking/issues/44#issuecomment-3515636113)
- 适用边界：适用于使用离线重定向动作训练时序敏感的全身跟踪策略，尤其是参考动作、环境和策略频率可分别配置的实现。

### human2humanoid 的 grad_fit_h1_shape.py 报 left_ankle_link is not in list，如何定位并使用已修补版本？

- `problem_id`：`problem.retargeting_dataset_quality.0e3f7e8e66777726`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：旧版 grad_fit_h1_shape 的 H1 关节名表与 ankle link 选择不一致**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：先比较 h1_joint_pick 与 h1_joint_names_augment。原帖旧版在选择 left_ankle_link 时，基础表仍使用 ankle_pitch/ankle_roll 名称，因此 index 必然失败。维护者关闭线程前发布的 retargeting update 提交 0c6fd6f 把表改成包含 left_ankle_link/right_ankle_link 的 19 项 H1 映射。对 H1 可更新到该提交；对自定义机器人应同步修改关节名、旋转轴和自由度顺序，不能只追加一个字符串掩盖维度不一致。
- 证据状态：`issue_candidate`
- 来源定位：Issue #3 报错；collaborator 回复 issuecomment-2516366430；提交 0c6fd6f 的 grad_fit_h1_shape.py diff
- 原帖/精确回复：[旧版 grad_fit_h1_shape 的 H1 关节名表与 ankle link 选择不一致](https://github.com/LeCAR-Lab/human2humanoid/issues/3#issuecomment-2516366430)
- 平台/作者：GitHub Issues / zhanggang11863976
- 关键术语：关节名映射（joint-name mapping）；动作重定向（motion retargeting）；关键点索引（keypoint index）；自由度顺序（DOF ordering）
- 环境：LeCAR-Lab/human2humanoid；2024-10-04 原帖所用旧版重定向脚本；修补提交 0c6fd6f2a7c0a3974cc2856db1eabb72896b88cd。
- 症状：grad_fit_h1_shape.py 第 65 行构造 h1_joint_pick_idx 时出现 ValueError: 'left_ankle_link' is not in list。
- 诊断：对照 h1_joint_pick 和 h1_joint_names_augment，检查选择项中的 left_ankle_link/right_ankle_link 是否实际存在于 H1 关节名表。
- 原因：旧脚本的 H1 表列出 left_ankle_pitch_link/left_ankle_roll_link 等名称，而关键点选择使用 left_ankle_link，名称集合不一致。
- 处理过程：维护者在修补前建议先用仓库提供的 retargeted .pkl 做临时调试；随后发布 retargeting update。
- 有效处理：使用提交 0c6fd6f 或之后的对应代码；该提交把 H1 关节名表改为包含 left_ankle_link/right_ankle_link 的 19 项映射。
- 结果：collaborator 在原线程确认最新版已修补并关闭 Issue；源码 diff 精确修改了报错涉及的关节名表。
- 限制：该提交同时重写了较多 legacy retargeting 代码；自定义机器人不能只复制 H1 的 19 项表，仍需按自己的 XML/URDF 建立一致映射。
- 独立核验引用：[source_code · scripts/data_process/grad_fit_h1_shape.py 将旧 27 项名称表替换为包含 left_ankle_link/right_ankle_link 的 19 项表](https://github.com/LeCAR-Lab/human2humanoid/commit/0c6fd6f2a7c0a3974cc2856db1eabb72896b88cd)；[maintainer_confirmation · collaborator 确认最新版已修补并关闭 Issue](https://github.com/LeCAR-Lab/human2humanoid/issues/3#issuecomment-2516366430)
- 适用边界：直接适用于 0c6fd6f 之前的 H1 legacy retargeting 脚本；自定义机器人只可借用一致性检查方法。

### H1_ROTATION_AXIS 是 19 轴而 dof_pos 是 27 维时，应该怎样修复而不掩盖映射错误？

- `problem_id`：`problem.retargeting_dataset_quality.17ef28bd6a6bd866`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：旧版 grad_fit_h1_shape 把 19 轴 H1_ROTATION_AXIS 与 27 维 dof_pos 相乘**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：该仓库已修补的 H1 路径把 dof_pos 初始化从 27 改为 19，并同步把关节名表整理为 19 项，使每个自由度与旋转轴逐项一致。应使用提交 0c6fd6f 或之后的对应实现，并检查自己的模型自由度数；对自定义机器人不能无条件改成 19，而要让 DOF 向量、ROTATION_AXIS 和关节顺序三者一致。
- 证据状态：`issue_candidate`
- 来源定位：Issue #4；collaborator 回复 issuecomment-2516365741；提交 0c6fd6f 的 27→19 diff
- 原帖/精确回复：[旧版 grad_fit_h1_shape 把 19 轴 H1_ROTATION_AXIS 与 27 维 dof_pos 相乘](https://github.com/LeCAR-Lab/human2humanoid/issues/4#issuecomment-2516365741)
- 平台/作者：GitHub Issues / zhanggang11863976
- 关键术语：旋转轴表（rotation-axis table）；自由度向量（DOF vector）；维度不匹配（dimension mismatch）；动作重定向（motion retargeting）
- 环境：LeCAR-Lab/human2humanoid；2024-10-05 原帖所用旧版脚本；修补提交 0c6fd6f2a7c0a3974cc2856db1eabb72896b88cd。
- 症状：RuntimeError: The size of tensor a (19) must match the size of tensor b (27) at non-singleton dimension 1。
- 诊断：同时核对 H1_ROTATION_AXIS 的轴数、dof_pos 最后一维自由度数和 h1_joint_names 的顺序，而不是只在 torch.cat 外层补零。
- 原因：旧脚本的 H1_ROTATION_AXIS 为 19 轴，但 dof_pos 初始化为 27 维。
- 处理过程：社区用户链接了临时修改，提问者回复 I think it works；维护者随后发布正式仓库更新。
- 有效处理：提交 0c6fd6f 把 grad_fit_h1_shape.py 的 dof_pos 从 torch.zeros((1,27)) 改为 torch.zeros((1,19))，并同步为 19 项 H1 关节表。
- 结果：collaborator 确认最新版已修补并关闭 Issue；提交 diff 精确覆盖报错行。
- 限制：19 是该 H1 模型和该脚本的维度，不是任意自定义机器人都应使用的常数；修改维度时必须同步关节顺序和旋转轴。
- 独立核验引用：[source_code · grad_fit_h1_shape.py 把 dof_pos 从 (1,27) 改为 (1,19)，并同步 19 项关节名表](https://github.com/LeCAR-Lab/human2humanoid/commit/0c6fd6f2a7c0a3974cc2856db1eabb72896b88cd)；[maintainer_confirmation · collaborator 确认最新版已修补并关闭 Issue](https://github.com/LeCAR-Lab/human2humanoid/issues/4#issuecomment-2516365741)
- 适用边界：直接适用于 0c6fd6f 之前的 Unitree H1 legacy retargeting 脚本；其他机器人只适用维度一致性原则。

### 自定义人形机器人重定向出现一侧正常、另一侧关键点整体错位时，如何检查轴符号和关节顺序？

- `problem_id`：`problem.retargeting_dataset_quality.6b3161828feff3fd`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：自定义机器人重定向单侧错位：负轴符号与 XML 关节顺序同时不一致**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原帖作者最终确认有两个同时存在的问题：URDF 的负方向关节轴需要在对应自由度位置给 dof_pos 乘负号；NECK_Y 的导入位置又打乱了右臂关节顺序，因此还要调整 MuJoCo XML 的 worldbody 顺序，并让 ROTATION_AXIS 按完全相同顺序排列。只改一个轴的正负号不足以修复索引错位。该结论由原作者在其 30 关节机器人上确认，迁移到其他模型时需重新打印实际 DOF 顺序验证。
- 证据状态：`issue_candidate`
- 来源定位：Issue #71，提问者自答 issuecomment-3149818647
- 原帖/精确回复：[自定义机器人重定向单侧错位：负轴符号与 XML 关节顺序同时不一致](https://github.com/LeCAR-Lab/human2humanoid/issues/71#issuecomment-3149818647)
- 平台/作者：GitHub Issues / Hanna-Li
- 关键术语：关节轴符号（joint-axis sign）；自由度顺序（DOF ordering）；旋转轴表（ROTATION_AXIS）；正向运动学（forward kinematics）
- 环境：LeCAR-Lab/human2humanoid；stable_punch.pkl；30 关节自定义机器人；vis_motion.py；MuJoCo XML/URDF；具体提交和版本未说明。
- 症状：左臂和左腿能匹配红色关键点，右侧身体不能匹配；修改单个 axis 的 -1/1 后一度没有变化。
- 诊断：逐关节比较 URDF 轴符号与运行时 ROTATION_AXIS；打印导入后的关节顺序，确认 NECK_Y 是否插入右臂 DOF 之前并造成索引错位。
- 原因：URDF 中负方向关节轴未在 dof_pos 中补偿符号；NECK_Y 在导入顺序中位于右臂关节之前，使右侧关节向量与 ROTATION_AXIS 顺序错位。
- 处理过程：提问者先直接修改 axis 的 -1/1，但结果没有变化；随后同时处理 dof_pos 符号矩阵和关节顺序。
- 有效处理：为 URDF 中负轴关节建立符号矩阵，对相应 dof_pos 乘 -1；在 MuJoCo XML worldbody 中调整 NECK_Y 与右臂关节的相对顺序，并按相同顺序修改 torch_humanoid_batch.py 的 ROTATION_AXIS。
- 结果：提问者在原线程明确写明问题解决，并列出上述两个原因和处理。
- 限制：这是单一自定义机器人的作者自测；不同导入器是否按名称排序、树结构还是 XML 顺序生成 DOF 索引，需要在目标工具链实测。
- 安全提示：错误轴符号或关节顺序会产生方向相反的关节命令；进入实机前应以小幅单关节命令逐轴核对。
- 图片分析：原帖以红色关键点描述左右侧差异，但根因与修复由提问者文字自答明确给出；未从未读取的截图补充额外结论。
- 独立核验引用：[maintainer_confirmation · 提问者明确报告问题解决并列出两项原因与处理](https://github.com/LeCAR-Lab/human2humanoid/issues/71#issuecomment-3149818647)
- 适用边界：适用于从 URDF/MuJoCo XML 自动生成关节索引、并用独立 ROTATION_AXIS 表解释动作的自定义 humanoid 重定向。

### 重定向脚本调用前向运动学（FK），为什么仍可称为逆运动学（IK）？

- `problem_id`：`problem.retargeting_dataset_quality.24902336e5ae23ba`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Human2Humanoid 重定向代码看似 FK 而论文称 IK**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：项目贡献者明确说明，该项目的 IK 是“基于 FK 的优化”：优化器调整机器人关节变量，FK 负责计算当前关节对应的身体/关节位置，再用这些位置与目标之间的误差驱动优化。因此代码中出现 FK 模型不等于只做正向计算。
- 证据状态：`issue_candidate`
- 来源定位：Issue #25，贡献者回复 issuecomment-2518575224
- 原帖/精确回复：[Human2Humanoid 重定向代码看似 FK 而论文称 IK](https://github.com/LeCAR-Lab/human2humanoid/issues/25#issuecomment-2518575224)
- 平台/作者：GitHub Issues / Maxwell-Zhao
- 关键术语：逆运动学（inverse kinematics, IK）；前向运动学（forward kinematics, FK）；优化式重定向（optimization-based retargeting）
- 环境：LeCAR-Lab/human2humanoid；grad_fit_h1_shape.py；Unitree H1。
- 症状：代码审阅时只看到 FK 模型，没有显式闭式 IK 调用。
- 诊断：区分用于计算位姿误差的 FK 与外层优化求解关节变量的 IK。
- 原因：把优化式 IK 中的 FK 误差计算当成纯 FK 流程。
- 处理过程：提问者贴出脚本截图；项目贡献者解释实现形式。
- 有效处理：按基于 FK 的优化式 IK 理解该脚本。
- 结果：贡献者回答后关闭 Issue。
- 限制：回复没有展开目标函数、约束和优化器细节；具体实现仍需阅读对应代码。
- 图片分析：帖子截图只用于指出脚本中的 FK 模型；结论来自贡献者文字回复，不依赖截图推断。
- 独立核验引用：[maintainer_confirmation · 项目贡献者确认 IK 由基于 FK 的优化实现](https://github.com/LeCAR-Lab/human2humanoid/issues/25#issuecomment-2518575224)
- 适用边界：适用于 human2humanoid 的重定向脚本；其他项目是否采用同一形式需查其实现。

## simulator_physics_numerics (`simulator_physics_numerics`)

### MJX 第一步就 NaN，而同一模型在原生 MuJoCo 稳定，应该怎样证明不是普通调参问题？

- `problem_id`：`problem.simulator_physics_numerics.d0d1022c8147bb5b`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MJX 单腿最小模型首步 NaN、原生 MuJoCo 稳定的差分复现**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索。
- 解答状态：`unresolved`
- 候选解答：用同一 XML、同一 qpos/qvel/ctrl 初值并排运行 mjx.forward→mjx.step 与 mj_forward→mj_step，逐步打印 NaN；再对 float64、积分器、timestep、执行器/传动和根关节做单变量消融。如果这些变化都不影响 MJX 首步 NaN、native 仍稳定，就形成后端差异的高质量最小复现，但在维护者定位前不能宣称根因。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2932 setup、observations、minimal XML 与 reproduction script
- 原帖/精确回复：[MJX 单腿最小模型首步 NaN、原生 MuJoCo 稳定的差分复现](https://github.com/google-deepmind/mujoco/issues/2932)
- 平台/作者：GitHub Issues / Dcyaprogrammer
- 关键术语：最小可复现示例（minimal reproducible example）；差分测试（differential test）；数值发散（numerical divergence）
- 环境：macOS darwin 24.3.0；Python 3.12；MuJoCo 3.3.7；bundled MJX；JAX CPU build。
- 症状：mjx.forward 无 NaN；第一次 mjx.step 的 qpos/qvel 出现 NaN；原生 mj_step 连续 5 步稳定。
- 诊断：同一 XML/初始状态并排运行 MJX 与 native MuJoCo。；分别检查 forward 与 step 后的 qpos/qvel。；对精度、积分器、步长、执行器、传动和固定基做消融。
- 原因：MJX 对该约束/传动组合的数值实现或支持差异；具体根因尚未由维护者确认。
- 处理过程：启用 JAX float64。；测试 Euler/RK4 和 0.005/0.002/0.001 s。；替换执行器/传动。；把 freejoint 根改为 weld。
- 结果：所有消融仍在 MJX 首步 NaN，而 native MuJoCo 稳定；Issue 仍 Open。
- 限制：尚无维护者根因和修复；最小模型包含 tendon/约束组合，不能推断所有 MJX 腿式模型都会失败。
- 安全提示：任何包含 NaN 的 policy/状态必须在进入执行器接口前被 watchdog 拦截。
- 适用边界：MuJoCo 3.3.7/MJX 对应环境及类似约束/传动模型。

### MuJoCo 接触后只在 implicit/implicitfast 快速发散，原帖最终定位和修复是什么？

- `problem_id`：`problem.simulator_physics_numerics.b01c692a8b2777d3`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo implicit/implicitfast 在退化惯量接触约束下快速发散**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：维护者先用原 MRE 确认切换 Euler 或 RK4 后现象消失，随后官方提交把根因记录为约束中的退化刚体逆权重（degenerate body inverse weights）。commit 1cda1e7 为退化的平移/旋转权重加入互相回退，并增加连续 1000 步不出现 BADQACC 的回归测试。未包含该提交的版本可用 Euler/RK4 作为帖子确认的绕行方案。
- 证据状态：`issue_candidate`
- 来源定位：Issue #2472 评论 issuecomment-2703086771；fix commit 1cda1e7
- 原帖/精确回复：[MuJoCo implicit/implicitfast 在退化惯量接触约束下快速发散](https://github.com/google-deepmind/mujoco/issues/2472#issuecomment-2703086771)
- 平台/作者：GitHub Issues / jjyyxx
- 关键术语：隐式积分器（implicit integrator）；退化逆权重（degenerate inverse weights）；回归测试（regression test）
- 环境：MuJoCo 3.3.0；Python/C；Linux；timestep=0.001；implicitfast；elliptic cone；最小 XML。
- 症状：接触发生后接触力激增并快速数值发散。
- 诊断：同一 MRE 对比 Euler、RK4、implicit 与 implicitfast。；检查 timestep、摩擦锥、无摩擦和 joint damping 等消融。
- 原因：维护者最终提交把根因描述为约束中的退化 body inverse weights。
- 处理过程：提问者测试极小 timestep、pyramid friction cone、无摩擦和 RK4。；维护者复现并确认 Euler/RK4 可避开 implicit 系列问题。
- 有效处理：官方 commit 1cda1e7 在平移/旋转 inverse weight 一项退化为零时使用另一项回退，并加入回归测试。
- 结果：修复提交明确 Fixes #2472；测试连续 1000 步确认无 BADQACC 警告；Issue 关闭。
- 限制：临时切换 Euler/RK4 与正式修复不是同一保证；使用者需确认所装版本是否包含该提交。
- 独立核验引用：[source_code · 官方修复退化 body inverse weights，并加入 1000 步 DegenerateInertia 回归测试](https://github.com/google-deepmind/mujoco/commit/1cda1e7a8c2094fd0a87507d0c75bc2f109588d1)
- 适用边界：MuJoCo 3.3.0 起受影响的相关 implicit/implicitfast 约束组合；应确认安装版本含修复提交。

## training_reward_curriculum (`training_reward_curriculum`)

### 起身策略通过抖动刷奖励却不真正站起，如何调整？

- `problem_id`：`problem.training_reward_curriculum.63c4121b1413b7d3`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：人形基础动作奖励函数的局部最优与分阶段调参**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先把任务拆成高度提升、直立姿态和稳定保持三个阶段；初期让高度进展占主导，站起后逐步提高姿态误差、关节速度和平滑性约束，并明确允许的足部接触。不要直接照搬示例权重，应记录每项奖励曲线确认是否被单项劫持。
- 证据状态：`community_candidate`
- 来源定位：第 2 节起身阶段设计及第 6 节调试表
- 原帖/精确回复：[人形基础动作奖励函数的局部最优与分阶段调参](https://zhuanlan.zhihu.com/p/1894420366153216587)
- 平台/作者：Zhihu / 星穷碧落人归尽
- 关键术语：奖励塑形（reward shaping）；局部最优（local optimum）；课程学习（curriculum learning）
- 环境：Gym 类人形强化学习环境；起身、行走、跳跃基础动作；具体机器人和代码版本未给出。
- 症状：机器人抖动不稳或停在局部最优。；速度跟踪不足。；着陆后姿态失稳。；稀疏奖励导致收敛慢。
- 诊断：按主目标、辅助目标、惩罚项拆开奖励，并观察高度、姿态、关节速度、足端接触和落地阶段。
- 原因：关节速度惩罚过重。；速度奖励曲线过平。；落地阶段奖励不足。；奖励信号过于稀疏。
- 处理过程：起身先提高高度奖励，再增加姿态和平滑性约束。；速度跟踪改用更陡或线性的误差奖励。；跳跃增加落地姿态和冲击惩罚。；添加高度变化等中间奖励并分阶段提高难度。
- 结果：正文给出症状—原因—调参方向表，但没有公开独立复现实验或量化前后对比。
- 限制：示例权重和阈值不可直接迁移到不同机器人；代码片段偏伪代码，需核对量纲、符号和接触定义。
- 安全提示：进入真机前先在仿真中检查力矩、动作变化率、接触冲击与关节限位，再采用吊架、限力和急停。
- 图片分析：正文关键证据主要是公式、伪代码和症状对策表；页面图片没有提供可核验的训练曲线，因此未把图片当作效果证据。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_comments
- 适用边界：适用于学习式起身策略；具体权重需按机器人尺度、执行器和接触模型重调。

### 长序列动作奖励稀疏、训练收敛慢，如何建立调试顺序？

- `problem_id`：`problem.training_reward_curriculum.abc4fd5ba17bfca1`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：人形基础动作奖励函数的局部最优与分阶段调参**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先只保留能完成基本动作的主目标，再加入高度变化、相位进展等密集的中间反馈，最后逐项加入能效、对称性和安全惩罚；每次只改一组权重并记录分项奖励。这样能区分任务不会做，还是被辅助惩罚压制。
- 证据状态：`community_candidate`
- 来源定位：第 5 节通用设计原则及第 6 节调试表
- 原帖/精确回复：[人形基础动作奖励函数的局部最优与分阶段调参](https://zhuanlan.zhihu.com/p/1894420366153216587)
- 平台/作者：Zhihu / 星穷碧落人归尽
- 关键术语：稀疏奖励（sparse reward）；密集奖励（dense reward）；消融实验（ablation）
- 环境：Gym 类人形强化学习环境；起身、行走、跳跃基础动作；具体机器人和代码版本未给出。
- 症状：机器人抖动不稳或停在局部最优。；速度跟踪不足。；着陆后姿态失稳。；稀疏奖励导致收敛慢。
- 诊断：按主目标、辅助目标、惩罚项拆开奖励，并观察高度、姿态、关节速度、足端接触和落地阶段。
- 原因：关节速度惩罚过重。；速度奖励曲线过平。；落地阶段奖励不足。；奖励信号过于稀疏。
- 处理过程：起身先提高高度奖励，再增加姿态和平滑性约束。；速度跟踪改用更陡或线性的误差奖励。；跳跃增加落地姿态和冲击惩罚。；添加高度变化等中间奖励并分阶段提高难度。
- 结果：正文给出症状—原因—调参方向表，但没有公开独立复现实验或量化前后对比。
- 限制：示例权重和阈值不可直接迁移到不同机器人；代码片段偏伪代码，需核对量纲、符号和接触定义。
- 安全提示：进入真机前先在仿真中检查力矩、动作变化率、接触冲击与关节限位，再采用吊架、限力和急停。
- 图片分析：正文关键证据主要是公式、伪代码和症状对策表；页面图片没有提供可核验的训练曲线，因此未把图片当作效果证据。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_comments
- 适用边界：适用于起身、跳跃和其他多阶段全身动作。

### 行走策略一直达不到目标速度，先检查哪一类奖励设计？

- `problem_id`：`problem.training_reward_curriculum.c51edad122fe0ae8`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：人形基础动作奖励函数的局部最优与分阶段调参**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：先画出速度误差到奖励的映射。如果目标附近曲线太平，策略感受不到继续加速的收益，可改用线性项或更窄的指数核；同时检查能耗、姿态和扭矩惩罚是否压过速度奖励。修改后要同时看速度、能耗和摔倒率，避免用更大冲击换速度。
- 证据状态：`community_candidate`
- 来源定位：第 3 节速度跟踪与第 6 节调试表
- 原帖/精确回复：[人形基础动作奖励函数的局部最优与分阶段调参](https://zhuanlan.zhihu.com/p/1894420366153216587)
- 平台/作者：Zhihu / 星穷碧落人归尽
- 关键术语：速度跟踪（velocity tracking）；指数核（exponential kernel）；能量惩罚（energy penalty）
- 环境：Gym 类人形强化学习环境；起身、行走、跳跃基础动作；具体机器人和代码版本未给出。
- 症状：机器人抖动不稳或停在局部最优。；速度跟踪不足。；着陆后姿态失稳。；稀疏奖励导致收敛慢。
- 诊断：按主目标、辅助目标、惩罚项拆开奖励，并观察高度、姿态、关节速度、足端接触和落地阶段。
- 原因：关节速度惩罚过重。；速度奖励曲线过平。；落地阶段奖励不足。；奖励信号过于稀疏。
- 处理过程：起身先提高高度奖励，再增加姿态和平滑性约束。；速度跟踪改用更陡或线性的误差奖励。；跳跃增加落地姿态和冲击惩罚。；添加高度变化等中间奖励并分阶段提高难度。
- 结果：正文给出症状—原因—调参方向表，但没有公开独立复现实验或量化前后对比。
- 限制：示例权重和阈值不可直接迁移到不同机器人；代码片段偏伪代码，需核对量纲、符号和接触定义。
- 安全提示：进入真机前先在仿真中检查力矩、动作变化率、接触冲击与关节限位，再采用吊架、限力和急停。
- 图片分析：正文关键证据主要是公式、伪代码和症状对策表；页面图片没有提供可核验的训练曲线，因此未把图片当作效果证据。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_comments
- 适用边界：适用于基于期望速度训练的 locomotion policy。

### 跳跃策略能起跳但落地后站不稳，奖励应怎样补齐？

- `problem_id`：`problem.training_reward_curriculum.dab5d979fb13ea73`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：人形基础动作奖励函数的局部最优与分阶段调参**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：不要只奖励最大高度；显式划分蓄力、飞行和落地阶段，在落地接触触发后加入身体姿态误差、膝关节缓冲轨迹和冲击力惩罚，并给成功稳定保持一个终止或完成奖励。帖子给的是设计方向，没有量化复现，必须重新标定接触阈值。
- 证据状态：`community_candidate`
- 来源定位：第 4 节跳跃与落地缓冲控制
- 原帖/精确回复：[人形基础动作奖励函数的局部最优与分阶段调参](https://zhuanlan.zhihu.com/p/1894420366153216587)
- 平台/作者：Zhihu / 星穷碧落人归尽
- 关键术语：阶段奖励（phase-conditioned reward）；落地冲击（landing impact）；接触检测（contact detection）
- 环境：Gym 类人形强化学习环境；起身、行走、跳跃基础动作；具体机器人和代码版本未给出。
- 症状：机器人抖动不稳或停在局部最优。；速度跟踪不足。；着陆后姿态失稳。；稀疏奖励导致收敛慢。
- 诊断：按主目标、辅助目标、惩罚项拆开奖励，并观察高度、姿态、关节速度、足端接触和落地阶段。
- 原因：关节速度惩罚过重。；速度奖励曲线过平。；落地阶段奖励不足。；奖励信号过于稀疏。
- 处理过程：起身先提高高度奖励，再增加姿态和平滑性约束。；速度跟踪改用更陡或线性的误差奖励。；跳跃增加落地姿态和冲击惩罚。；添加高度变化等中间奖励并分阶段提高难度。
- 结果：正文给出症状—原因—调参方向表，但没有公开独立复现实验或量化前后对比。
- 限制：示例权重和阈值不可直接迁移到不同机器人；代码片段偏伪代码，需核对量纲、符号和接触定义。
- 安全提示：进入真机前先在仿真中检查力矩、动作变化率、接触冲击与关节限位，再采用吊架、限力和急停。
- 图片分析：正文关键证据主要是公式、伪代码和症状对策表；页面图片没有提供可核验的训练曲线，因此未把图片当作效果证据。
- 采集完整性：`partial_visible`；可见回复 0；展开 0 次；回复深度 0/10；停止原因：no_visible_comments
- 适用边界：适用于有可靠接触检测和落地姿态观测的跳跃任务。

### 粗糙地形 base_height_l2 奖励看似正常却不提供有效梯度，如何发现公式相消？

- `problem_id`：`problem.training_reward_curriculum.eb2c2cec61dda84b`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：粗糙地形 base_height_l2 奖励因传感器原点相消而退化**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：把代码代入符号表达式：若 sensor.data.pos_w\[:,2\] 实际等于 root_link_pos_w\[:,2\]，则 root_height-(target_height+sensor_origin_height) 会相消成 -target_height，奖励成为常数。应使用射线命中的地形高度或定义明确的局部参考，并用不同地形/机身高度的单元测试确认奖励会变化。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1698 lines 166—205；关联 PR #1727 仍为 Open
- 原帖/精确回复：[粗糙地形 base_height_l2 奖励因传感器原点相消而退化](https://github.com/isaac-sim/IsaacLab/issues/1698)
- 平台/作者：GitHub Issues / fan-ziqi
- 关键术语：高度奖励（base-height reward）；射线投射器（RayCaster）；常数奖励（constant reward）
- 环境：Isaac Lab rewards.py b5078de；rough terrain；RayCaster sensor。
- 症状：奖励代数化简后只剩 target_height 的常数平方，无法表达离地高度误差。
- 诊断：展开 adjusted_target_height 公式，核对 sensor.data.pos_w 是传感器原点还是射线命中地形高度。
- 原因：把传感器原点世界坐标误当作地形参考高度。
- 处理过程：Issue 建议改用中心点实际参考地形高度；关联 PR 尝试处理传感器无效值。
- 结果：Issue 已关闭，但关联 PR #1727 当前页面仍为 Open，未找到已合并替代修复。
- 限制：不能把关闭状态等同于已发布修复；需要核对当前分支 rewards.py。
- 安全提示：更改奖励后重新训练并检查策略行为，不能把旧 checkpoint 直接当作修复验证。
- 独立核验引用：[pull_request · 关联修复 PR 当前仍为 Open；作为处理方向，不作为已发布修复证明](https://github.com/isaac-sim/IsaacLab/pull/1727)
- 适用边界：适用于使用 RayCaster 修正粗糙地形目标高度的 Isaac Lab 版本。

### 设置 TerrainGeneratorCfg(curriculum=True) 后训练仍未按难度递进，应该检查哪一层？

- `problem_id`：`problem.training_reward_curriculum.d08d86d9883750a2`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：只设置 TerrainGeneratorCfg.curriculum 不等于训练任务已接入地形课程**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原帖作者的有效处理是迁移到管理器式工作流（manager-based workflow），并在 RL 配置中定义课程配置（CurriculumCfg）。TerrainGeneratorCfg 的 curriculum 负责地形生成布局，但任务侧还要有课程项驱动环境在难度行之间更新。作者确认 IsaacLab v2.2.0 的示例代码可工作；其他版本应对照对应分支的配置路径。
- 证据状态：`issue_candidate`
- 来源定位：Issue #1492 自答 issuecomment-2531772317；补充 issuecomment-3395768759
- 原帖/精确回复：[只设置 TerrainGeneratorCfg.curriculum 不等于训练任务已接入地形课程](https://github.com/isaac-sim/IsaacLab/issues/1492#issuecomment-3395768759)
- 平台/作者：GitHub Issues / H-Hisamichi
- 关键术语：地形生成器（terrain generator）；课程配置（CurriculumCfg）；管理器式工作流（manager-based workflow）；难度等级（terrain level）
- 环境：Isaac Lab 地形生成器；原帖自定义 15×25 地形网格；后续确认 IsaacLab v2.2.0 manager-based 示例。
- 症状：RL 刚开始时渲染中已经存在困难地形，与期望的从平地/轻微台阶逐步训练不一致。
- 诊断：除 TerrainGeneratorCfg.curriculum 外，检查 manager-based RL 配置中是否实际定义 CurriculumCfg，以及任务是否注册了地形等级更新项。
- 原因：原帖的解决说明表明旧工作流没有按 manager-based 示例接入 CurriculumCfg。
- 处理过程：迁移到 manager-based workflow，并确认 RL 配置代码定义 CurriculumCfg。
- 有效处理：按 IsaacLab v2.2.0 的 manager-based locomotion 示例定义 CurriculumCfg，而不只设置 terrain generator 的 curriculum 标志。
- 结果：提问者在原线程明确报告迁移后问题解决，并在后续追问中再次给出 v2.2.0 示例定位。
- 限制：原帖没有展示迁移前后地形等级日志或课程项代码；不同 Isaac Lab 版本的配置类路径可能变化。
- 图片分析：原帖有训练初期地形截图，但本卡结论来自作者迁移后的文字确认和精确示例链接，不从截图判断实际难度等级。
- 独立核验引用：[maintainer_confirmation · 提问者明确报告迁移 manager-based 后问题解决](https://github.com/isaac-sim/IsaacLab/issues/1492#issuecomment-2531772317)；[source_code · 提问者补充引用的 v2.2.0 CurriculumCfg 示例](https://github.com/isaac-sim/IsaacLab/blob/f52aa9802780e897c184684d1cbc2025fafcef4a/source/isaaclab_tasks/isaaclab_tasks/manager_based/locomotion/velocity/velocity_env_cfg.py#L278)
- 适用边界：明确对应 IsaacLab v2.2.0 manager-based locomotion 示例；其他版本需核对 CurriculumCfg API。

### Isaac Lab 奖励权重归零后单项 step reward 残留

- `problem_id`：`problem.training_reward_curriculum.isaaclab_zero_weight_step_reward_stale_2391`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 奖励权重归零后单项 step reward 残留旧值**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：原帖定位到 RewardManager.compute 的零权重分支直接 continue，没有清空 _step_reward 对应列，因此可视化和日志读到过期值。已合并 PR #2392 在 continue 前执行 self._step_reward\[:, term_idx\] = 0.0，并使用 enumerate 获得索引。这不是总奖励错误：原帖明确说 _reward_buf 一直正确。PR 没有新增回归测试，目标版本仍应复测 0 → 非 0 → 0 路径。
- 证据状态：`issue_candidate`
- 来源定位：Isaac Lab #2391 正文复现和影响边界；版本确认 issuecomment-2836796927；已合并 PR #2392 及合并提交 f1ba9c3
- 原帖/精确回复：[Isaac Lab 奖励权重归零后单项 step reward 残留旧值](https://github.com/isaac-sim/IsaacLab/issues/2391)
- 平台/作者：GitHub Issues / Bikram Pandit
- 关键术语：单步奖励（step reward）；奖励课程（reward curriculum）；过期值（stale value）；实时可视化（live visualization）
- 环境：Isaac Lab 2.1.0，commit 2e6946afb9b26f6949d4b1fd0a00e9f4ef733fcc；Isaac Sim 4.5；Ubuntu 22.04；RTX 3060；CUDA 12.4；GPU driver 550.120。
- 症状：权重在 0 → 非 0 → 0 后，_reward_buf 继续正确，但 _step_reward\[:, idx\] 保留前一次的非零值。；ManagerLiveVisualizer 和依赖 _step_reward 的日志显示过期单项奖励。
- 诊断：按原帖步骤记录同一项在 0 → 非 0 → 0 三个阶段的 weight、_step_reward 与 _reward_buf，区分单项监控缓冲和总奖励。；检查 RewardManager.compute 的 zero-weight continue 分支是否在跳过前清空对应列。
- 原因：旧实现遇到 weight == 0.0 直接 continue，没有覆盖之前写入 _step_reward 的单项值。
- 处理过程：原帖给出了权重往返切换的伪代码复现。；PR #2392 先引入 term_idx 并在零权重分支清零，后续提交改用 enumerate 避免在循环中搜索名称索引。
- 有效处理：使用已合并 PR #2392 的逻辑：遇到零权重时先执行 self._step_reward\[:, term_idx\] = 0.0，再 continue。
- 结果：PR #2392 于 2025-05-09 合并到主分支，合并提交为 f1ba9c3a30b0cef04d04dfba789f996360cd4f1c。
- 限制：该修复只矫正单项 _step_reward 的可视化/日志值；原帖明确说明总奖励 _reward_buf 本来就正确。；PR #2392 的检查清单明确未添加证明修复有效的测试；应在目标版本重跑原帖的权重切换用例。
- 安全提示：调试过程中不要仅依赖单项可视化判定策略实际收到的总奖励。
- 独立核验引用：[pull_request · PR 在零权重分支清空对应 _step_reward，已合并；检查清单未新增测试](https://github.com/isaac-sim/IsaacLab/pull/2392)；[source_code · PR #2392 合并提交](https://github.com/isaac-sim/IsaacLab/commit/f1ba9c3a30b0cef04d04dfba789f996360cd4f1c)；[issue · 原作者补充确认 Isaac Lab/Isaac Sim 版本](https://github.com/isaac-sim/IsaacLab/issues/2391#issuecomment-2836796927)
- 适用边界：适用于使用 Isaac Lab RewardManager，且运行期动态将同一奖励项权重从非零改回 0 的情况；原环境为 Isaac Lab 2.1.0/Isaac Sim 4.5。

### RSL-RL PPO 报 Normal 分布 std 小于零时，原线程给出了什么可核对线索？

- `problem_id`：`problem.training_reward_curriculum.b2e89c8dbb053f7d`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：PPO 训练中 Normal 分布标准差变为负值**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索；尚未形成可核对的复现记录。
- 解答状态：`unresolved`
- 候选解答：线程只提供两条待验证线索：一名复现者称修改奖励权重后能缓解但仍偶发；另一名用户建议在训练代码中裁剪策略的 sigma。原帖没有证明奖励权重导致负标准差，也没有证明裁剪后的训练质量，因此两项都只能作为复现实验入口。
- 证据状态：`issue_candidate`
- 来源定位：Issue #33 正文栈；issuecomment-3471368600 与 issuecomment-3471370672
- 原帖/精确回复：[PPO 训练中 Normal 分布标准差变为负值](https://github.com/HybridRobotics/whole_body_tracking/issues/33#issuecomment-3471368600)
- 平台/作者：GitHub Issues / dbdxnuliba
- 关键术语：标准差（standard deviation）；策略分布（policy distribution）；数值裁剪（clipping）
- 环境：whole_body_tracking；Isaac Lab Python 3.10 环境；RSL-RL PPO；具体 commit 未说明。
- 症状：RuntimeError: normal expects all elements of std >= 0.0。
- 诊断：堆栈定位到 actor_critic.py 的 distribution.sample。
- 处理过程：一名用户改变奖励权重后问题减少但仍偶发。；另一名用户建议在训练代码中裁剪 sigma。
- 结果：改变奖励权重的用户明确说问题仍会发生；sigma 裁剪建议没有后续验证。
- 限制：没有维护者回复、复现配置、补丁或最终闭环；不能断言奖励权重是根因。
- 适用边界：适用于出现同一 RSL-RL Normal scale/std 异常的训练；版本和策略参数需单独记录。
