# WBC 社交平台工程问题查询手册

> 生成时间：2026-08-11T15:09:42+08:00。所有已发现经验均按问题聚合并完整展示；等级仅说明核验基础，不会自动升级为正式 `EngineeringClaim`。

## 等级与使用

- `可信度很高`：问题闭环、环境明确、无冲突，并有正式资料交叉核验或独立复现；依赖图片时图片已完成分析。
- `值得参考`：环境、症状、处理和结果形成完整工程记录，但尚缺正式交叉核验或独立复现。
- `需要实际验证`：单一经验、信息缺项、尚未复现、图片尚待分析，或结论仍有冲突。
- 点赞、浏览、收藏和作者粉丝数不参与等级判定。
- 无论原帖是中文还是英文，整理均以中文为主；关键术语采用 `中文（English, ABBR）`。
- `community_candidate`、`issue_candidate` 与 `partial_visible` 分别表示来源类型和采集可见范围，不替代可信度或解答状态。
- 更新按需触发：查询前沿、搜索调度、可信度、解答状态和正式结论是五个互不替代的概念。

## 总览

- 已审阅来源：258
- 工程问题：298；工程经验：311
- 经验等级：可信度很高 56 / 值得参考 194 / 需要实际验证 61
- 解答状态：resolved 138 / partial 131 / unresolved 28 / conflicting 14
- Scope 覆盖：32/32

| 工程范围 | `scope_id` | X | 知乎 | 小红书 | GitHub Issues | 问题 | 经验 | 需实际验证 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 开放式 WBC 工程经验 | `open_ended_wbc_field_notes` | 1 | 1 | 1 | 0 | 5 | 5 | 1 |
| 安装、依赖与版本兼容 | `environment_setup_dependencies` | 1 | 3 | 1 | 2 | 10 | 12 | 4 |
| 仿真器与工具链 | `simulation_toolchain` | 1 | 0 | 1 | 11 | 13 | 14 | 4 |
| 训练不稳定与崩溃 | `training_instability` | 1 | 0 | 1 | 0 | 2 | 2 | 0 |
| 奖励、课程与随机化 | `reward_curriculum_randomization` | 1 | 1 | 0 | 3 | 7 | 7 | 1 |
| 性能、显存与并行仿真 | `compute_performance_memory` | 0 | 1 | 1 | 3 | 6 | 6 | 3 |
| 动作重定向与数据质量 | `retargeting_and_dataset` | 2 | 1 | 0 | 0 | 3 | 3 | 0 |
| 跟踪与遥操 | `tracking_and_teleoperation` | 1 | 1 | 1 | 0 | 3 | 3 | 2 |
| 状态估计、标定与时间同步 | `state_estimation_calibration` | 1 | 1 | 0 | 9 | 13 | 13 | 2 |
| 通信、时延与实时性 | `communication_and_realtime` | 0 | 1 | 1 | 3 | 6 | 6 | 1 |
| sim-to-sim 与 sim-to-real | `sim_to_sim_and_sim_to_real` | 2 | 1 | 1 | 7 | 16 | 16 | 3 |
| 足式运动、接触与地形 | `locomotion_contact_terrain` | 1 | 0 | 0 | 7 | 8 | 8 | 3 |
| IK/QP/MPC/WBC 优化问题 | `optimization_ik_qp_mpc` | 1 | 2 | 1 | 54 | 62 | 67 | 9 |
| 力控、接触操作与载荷 | `force_control_manipulation` | 1 | 1 | 1 | 3 | 9 | 9 | 3 |
| 电机、减速器、温升与磨损 | `hardware_actuator_thermal` | 1 | 0 | 1 | 6 | 8 | 10 | 3 |
| 部署、固件与 SDK | `deployment_firmware_sdk` | 2 | 1 | 0 | 0 | 6 | 6 | 0 |
| 安全、跌倒、冲击与起身 | `safety_fall_recovery` | 2 | 0 | 1 | 2 | 5 | 5 | 3 |
| 传感器与感知接口 | `sensing_and_perception` | 1 | 0 | 1 | 2 | 4 | 4 | 1 |
| 复现、日志、评估与调试方法 | `reproducibility_and_debugging` | 1 | 0 | 0 | 3 | 5 | 5 | 0 |
| 机械集成、负载与配重 | `mechanical_payload_integration` | 0 | 1 | 0 | 1 | 2 | 2 | 0 |
| communication_realtime_control | `communication_realtime_control` | 0 | 2 | 0 | 0 | 5 | 5 | 5 |
| contact_force_friction | `contact_force_friction` | 0 | 0 | 0 | 17 | 20 | 20 | 5 |
| debugging_logging_reproducibility | `debugging_logging_reproducibility` | 0 | 0 | 0 | 2 | 2 | 2 | 1 |
| dynamics_mass_inertia_actuation | `dynamics_mass_inertia_actuation` | 0 | 0 | 0 | 3 | 3 | 3 | 0 |
| dynamics_model_validation | `dynamics_model_validation` | 0 | 0 | 0 | 1 | 1 | 1 | 0 |
| hardware_actuator_thermal_power | `hardware_actuator_thermal_power` | 0 | 0 | 0 | 8 | 8 | 8 | 1 |
| joint_mapping_frames_conventions | `joint_mapping_frames_conventions` | 0 | 0 | 0 | 13 | 14 | 17 | 3 |
| model_asset_and_urdf_usd | `model_asset_and_urdf_usd` | 0 | 0 | 0 | 11 | 11 | 11 | 0 |
| realtime_control_latency | `realtime_control_latency` | 0 | 0 | 0 | 18 | 20 | 20 | 1 |
| retargeting_dataset_quality | `retargeting_dataset_quality` | 0 | 0 | 0 | 7 | 8 | 8 | 0 |
| simulator_physics_numerics | `simulator_physics_numerics` | 0 | 0 | 0 | 2 | 2 | 2 | 1 |
| training_reward_curriculum | `training_reward_curriculum` | 0 | 1 | 0 | 7 | 11 | 11 | 1 |

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

### OCS2 零速度接触约束长时间积分造成世界地面参考漂移

- `problem_id`：`problem.simulation_toolchain.ocs2_zero_velocity_contact_z_drift_24`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OCS2 legged robot 示例长时间积分后目标轨迹沿 z 方向漂移**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：项目贡献者的线程内解释是：dummy simulation 与 MPC 使用相同模型，并用零速度接触约束（zero-velocity contact constraint）维持接触；长时间积分会累计漂移。命令仍在世界坐标系（world frame）发布，但内部对地面的认知已经沿 z 方向漂移，所以绿色轨迹看起来升高。线程只提到未来加入正式 terrain notion，没有给出当时可复测的补丁。
- 证据状态：`issue_candidate`
- 来源定位：OCS2 #24：贡献者评论 963489354 解释零速度接触约束与 world-frame ground drift；原作者评论 963824521 致谢
- 原帖/精确回复：[OCS2 legged robot 示例长时间积分后目标轨迹沿 z 方向漂移](https://github.com/leggedrobotics/ocs2/issues/24#issuecomment-963489354)
- 平台/作者：GitHub Issues / edward9503
- 关键术语：零速度接触约束（zero-velocity contact constraint）；世界坐标系（world frame）；积分漂移（integration drift）；地形参考（terrain notion）
- 环境：Ubuntu 20.04、Eigen 3.3.7、OCS2 legged robot example；可以完整 catkin build；未给 OCS2 commit。
- 症状：多次让机器人向前和向后移动后，绿色 desired body trajectory 沿 z 方向上漂。；发帖人同时说明机器人运动仍显得正确、合理。
- 诊断：对比目标轨迹的 world-frame 高度与内部接触/地面参考，判断是显示与世界参考漂移还是机器人动力学本身失稳。；检查长时间积分中的零速度接触约束是否累计漂移，而不是先归因于 Eigen 版本。
- 原因：项目贡献者解释，零速度接触约束在长时间积分中会产生漂移；命令仍按 world frame 发布，但内部地面概念已经沿 z 漂移。
- 处理过程：原帖只报告环境、图片和视频，没有给出修改后的复测步骤。
- 结果：贡献者说明扩展 formulation 正在加入正式世界地形概念，并计划贯穿优化、仿真和命令侧；原线程没有发布补丁或复测结果。
- 限制：该线程解释了原因但没有验证可立即采用的修复，因此不能把 Issue 的 closed 状态等同于实现已修好。；静态图能看到绿色轨迹位于机器人上方；视频附件未成功取帧，本卡不对视频中的运动速度或时间作推断。
- 安全提示：长时间仿真或实机执行前，应监控接触面高度与世界参考漂移；不能只凭可视化中机器人仍在运动就认为参考一致。
- 图片分析：原帖 PNG 已核验：RViz 中四足机器人上方有一条绿色近水平线，发帖人用黑色手绘轮廓圈出该目标轨迹；画面没有高度刻度、时间或单位，只能支持“目标轨迹明显位于机器人/地面上方”的症状。；原帖 MP4 已打开，但浏览器播放器未成功提供可核验的视频帧；本卡不据此描述运动过程，原因与限制仅来自原帖文字及贡献者回复。
- 独立核验引用：[maintainer_confirmation · 项目贡献者解释零速度约束导致长时间漂移以及 world-frame 命令与内部地面参考失配](https://github.com/leggedrobotics/ocs2/issues/24#issuecomment-963489354)
- 适用边界：适用于该 OCS2 legged robot dummy simulation 的长时间积分现象；不同仿真器、接触模型或新版地形 formulation 需重新核对。

### Isaac Lab Fabric 下 actuator gain 的 UI 显示与运行时生效状态不一致

- `problem_id`：`problem.simulation_toolchain.isaaclab_fabric_actuator_gain_runtime_vs_ui_4320`
- 问题综合等级：**需要实际验证** — 不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab GPU/Fabric 下 UI 不显示 actuator gain 与运行时是否生效不能混为一谈**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突。
- 解答状态：`conflicting`
- 候选解答：不能仅凭 UI 判断。项目维护者明确说明 GPU simulation/Fabric 会抑制 USD read/write，所以运行时属性和 transform 不会在 UI 中显示；需要观察 UI 时可用 --device cpu env.sim.use_fabric=false 调试。但线程对运行时是否实际生效没有闭环：后续回复称自定义 gain 会生效，原作者最后却说自己已经使用同样的 ImplicitActuatorCfg 仍不工作。因此应把 UI 可见性和 runtime gain 分开验证，不能把任一方的陈述当作最终修复。
- 证据状态：`issue_candidate`
- 来源定位：Isaac Lab #4320 评论 3707421315 解释 GPU/Fabric UI 行为；评论 3725503782 声称 gain 生效；评论 3914083197 原作者说明相同配置仍不工作
- 原帖/精确回复：[Isaac Lab GPU/Fabric 下 UI 不显示 actuator gain 与运行时是否生效不能混为一谈](https://github.com/isaac-sim/IsaacLab/issues/4320#issuecomment-3707421315)
- 平台/作者：GitHub Issues / junshi356rl
- 关键术语：隐式执行器配置（ImplicitActuatorCfg）；关节刚度（joint stiffness）；关节阻尼（joint damping）；运行时状态（runtime state）；通用场景描述（Universal Scene Description, USD）
- 环境：Isaac Lab、Isaac Sim 5.1、Python 3.11、Ubuntu 24.04.3、RTX 5080、driver 580.95.05；manager-based PPO template，UR-with-gripper USD；原帖未给 Isaac Lab commit。
- 症状：配置 finger_joint stiffness=280、damping=28 后，Isaac Sim UI 仍显示 USD 文件中的原值。；原作者怀疑参数未应用，因为 joint-velocity penalty 明显增大。；在获得同一 ImplicitActuatorCfg 示例后，原作者最后仍回复该配置没有工作。
- 诊断：先把 UI/USD 可见性与 PhysX/Fabric 运行时值分开：GPU Fabric 下 UI 不显示修改是项目方明确说明的已知行为。；需要查看 USD 侧调试值时，按维护者建议使用 CPU 且关闭 Fabric；运行时是否生效则应另做受控动态响应或底层 buffer 对照。
- 原因：UI 不更新的原因由维护者解释为 GPU simulation 为提速抑制 USD read/write。；实际 stiffness/damping 是否生效没有闭环：回复者称会生效，但原作者用相同配置后仍称不工作。
- 处理过程：维护者建议以 --device cpu env.sim.use_fabric=false 运行，便于在 UI 中查看运行时修改。；后续回复者再次给出 ImplicitActuatorCfg 的 arm/gripper 配置；原作者说明自己原帖已经使用同类配置且无效。
- 结果：线程只解释了 GPU/Fabric 下 UI 不反映修改的机制；没有证明原作者环境中的 gripper stiffness/damping 已在运行时生效，也没有关联 PR 或最终修复。
- 限制：CPU+关闭 Fabric 是显示/调试建议，原作者没有报告执行结果，不能写成已经修复 actuator gain。；线程没有读取 PhysX runtime buffer、阶跃响应、关节轨迹或独立力矩对照；仅凭 UI 和 penalty 变化不能判断实际 gain。；Issue 虽关闭，但最后一条技术回复仍是原作者称相同配置没有工作，关闭状态不能替代闭环证据。
- 安全提示：把策略或控制器迁移到实机前，应通过受控小幅响应识别等效 stiffness/damping，并限制力矩、速度和位置；不能依据 UI 单值直接标定。
- 独立核验引用：[conflict · 回复者声称 Fabric 默认开启时自定义 stiffness/damping 会生效](https://github.com/isaac-sim/IsaacLab/issues/4320#issuecomment-3725503782)；[conflict · 原作者明确说明自己已使用同样的 ImplicitActuatorCfg，但仍不工作](https://github.com/isaac-sim/IsaacLab/issues/4320#issuecomment-3914083197)
- 适用边界：适用于 Isaac Sim 5.1/Isaac Lab GPU simulation 中 ImplicitActuatorCfg 与 Fabric/USD UI 的诊断；实际 gain 需在目标 commit 和资产上独立测量。

### Pinocchio continuous joint 配置未归一化导致 ABA 加速度异常

- `problem_id`：`problem.simulation_toolchain.pinocchio_continuous_joint_configuration_normalization_1534`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio continuous joint 构型未归一化会使 ABA 加速度对照失真**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：维护者指出原代码忘记归一化配置。该模型使用 continuous joint，q 以 \[cos(theta), sin(theta)\] 参数化，因此应在 ABA 前执行 q=pin.normalize(model,q)，并注意 normalize 返回新值，必须重新赋给 q。线程没有给出修正后的加速度输出，也没有回到完整 walking 模型复测，所以只能把这条作为已确认的输入修正，不能声称完整摆动腿问题已经闭环。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1534 评论 934651753 给出 normalize 脚本；评论 973980396 解释 continuous joint 参数化；评论 974012875 强调接收返回值
- 原帖/精确回复：[Pinocchio continuous joint 构型未归一化会使 ABA 加速度对照失真](https://github.com/stack-of-tasks/pinocchio/issues/1534#issuecomment-934651753)
- 平台/作者：GitHub Issues / Kongx231
- 关键术语：连续关节（continuous joint）；配置流形（configuration manifold）；构型归一化（configuration normalization）；关节加速度（joint acceleration）；关节空间前向动力学算法（Articulated-Body Algorithm, ABA）
- 环境：pinocchio3-preview、Python、附件 single_pendulum.urdf；原帖未给 OS、具体 commit 或编译选项。
- 症状：单摆长度 2、质量 1、惯量 1、重力 9.81、质心距转轴 1，在 pi/2 零速度初始化时，原作者预期约 -4.905，却从 ABA 得到约 -7.7。；更大 walking 模型中，原作者先观察到 swing-leg joint accelerations 偏大且与其他 solver 不一致。
- 诊断：检查 URDF joint 类型和 model.nq/model.nv；continuous joint 不能按单个标量角度直接填配置。；在调用 ABA/constraintDynamics 前对 q 使用 pin.normalize(model,q)，并保留返回值。
- 原因：维护者指出原始 q 未归一化；该 continuous joint 的配置使用 \[cos(theta), sin(theta)\] 参数化。
- 处理过程：原作者先从 walking constraintDynamics 简化到单摆 ABA 最小复现，并附 Python 代码与 URDF。；维护者给出包含 q=pin.normalize(model,q) 的完整脚本片段。
- 有效处理：以 q=pin.normalize(model,q) 接收归一化返回值后再调用 pin.aba；不要只调用 normalize 而丢弃返回值。
- 结果：维护者将异常定位为未归一化配置，并解释 continuous joint 的 \[cos(theta), sin(theta)\] 参数化；原作者没有发布修正后数值。
- 限制：线程没有原作者归一化后的 -4.905 对照，也没有回到完整 walking/constraintDynamics 模型复测，因此完整摆动腿问题仍需单独验证。；本卡不能把所有过大加速度都归因于配置归一化；惯量、单位、外力和约束也需独立核对。；附件代码/URDF 没有在当前环境重新运行。
- 安全提示：动力学输入进入实机 WBC 前应检查配置流形有效性和有限值；异常大加速度不得直接转成力矩下发。
- 独立核验引用：[maintainer_confirmation · 维护者说明该 continuous joint 用 q=\[cos(theta),sin(theta)\] 参数化](https://github.com/stack-of-tasks/pinocchio/issues/1534#issuecomment-973980396)；[issue · 项目成员纠正为 q=pin.normalize(model,q)，必须保存返回值](https://github.com/stack-of-tasks/pinocchio/issues/1534#issuecomment-974012875)
- 适用边界：适用于 Pinocchio continuous joint 的配置向量及其 ABA/constraintDynamics 调用；完整机器人仍需检查其他动力学输入。

### MJX contact pair mesh 的凸包缺失修复

- `problem_id`：`problem.simulation_toolchain.mjx_contact_pair_mesh_hull_2777`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MJX put_model 遇到仅通过 contact pair 碰撞的 mesh 时需要凸包修复**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：先确认该 mesh 的 contype/conaffinity 为 0、碰撞只由 contact/pair 指定；若符合，使用包含提交 3434f5d 的 MuJoCo 版本。该提交在编译期先解析 pairs，把 pair 中的 mesh 标记为需要 convex hull，并加入 ConvexHullForPairCollisionMeshes 回归测试。原作者未报告升级复测，但维护者诊断、作者模型确认、正式源码修复和测试形成了完整证据链。
- 证据状态：`issue_candidate`
- 来源定位：MuJoCo #2777 维护者诊断 3133421618、作者模型确认 3134769229；commit 3434f5d
- 原帖/精确回复：[MJX put_model 遇到仅通过 contact pair 碰撞的 mesh 时需要凸包修复](https://github.com/google-deepmind/mujoco/issues/2777#issuecomment-3133421618)
- 平台/作者：GitHub Issues / VincentFEI
- 关键术语：接触对（contact pair）；凸包（convex hull）；网格图地址（mesh_graphadr）；回归测试（regression test）
- 环境：MuJoCo/MJX 3.3.4；Python API；Ubuntu 24.04；原模型通过 contact/pair 让 contype=0、conaffinity=0 的 mesh 参与碰撞。
- 症状：mjx.put_model 报 mesh.py convex 错误；相关 mesh_graphadr 为 -1；把 mesh 替换为 box 后不报错。
- 诊断：检查异常 mesh 是否 contype/conaffinity 都为 0，却只在 contact/pair 中参与碰撞。；检查安装版本是否包含提交 3434f5d 或 changelog 中对应修复。
- 原因：正式提交说明：只通过 contact pair 碰撞的 mesh 没有被标记计算 convex hull。
- 处理过程：维护者把问题与原模型的 contact pair 对齐；作者确认原模型确有 pair。
- 有效处理：使用包含 MuJoCo 提交 3434f5d9c774bf56d3cf4dd26d0beca8d9c509f1 的版本；该修复会在 convex-hull 检查前编译 pairs，并把 pair 中 mesh 标记为需要 hull。
- 结果：修复提交加入专门的 pair-collision mesh 回归测试并写入 changelog；原作者未在评论中报告升级后复测。
- 限制：原帖最小复现被维护者指出与真实 bug 不一致；适用前必须确认真实模型确有 contact pair。；不能把该修复外推到所有 mesh.py convex 错误。
- 安全提示：升级后应对脚底接触数量、法向和摩擦行为做回归，不能只以 put_model 不报错作为动力学验收。
- 独立核验引用：[source_code · 正式提交修改 user_model.cc、加入 pair mesh convex-hull 回归测试并更新 changelog](https://github.com/google-deepmind/mujoco/commit/3434f5d9c774bf56d3cf4dd26d0beca8d9c509f1)
- 适用边界：适用于 MuJoCo/MJX 3.3.4 及缺少该提交的版本，并且 mesh 仅通过 contact pair 参与碰撞。

### MuJoCo sysid modifier factory 隐式返回 None

- `problem_id`：`problem.simulation_toolchain.mujoco_sysid_modifier_none_3286`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo sysid 零迭代先检查 modifier factory 是否真的返回 callable**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：该例不是 LuGre 参数通路失效，而是 Python factory 的 return modifier 缩进在 inner function 内，outer factory 隐式返回 None。sysid.Parameter 收到 None 后不调用 modifier，candidate 值没有进入 spec，残差不变，有限差分梯度自然为零。修法是让 outer factory 返回 modifier；inner modifier 只修改 spec。维护者还单独检查了 biasprm\[3\]/\[4\] 的 spec→model→LuGre ODE 通路。
- 证据状态：`issue_candidate`
- 来源定位：MuJoCo #3286 维护者诊断与修正代码 4546762188，库方结论 4549965819
- 原帖/精确回复：[MuJoCo sysid 零迭代先检查 modifier factory 是否真的返回 callable](https://github.com/google-deepmind/mujoco/issues/3286#issuecomment-4546762188)
- 平台/作者：GitHub Issues / ndhoang02-source
- 关键术语：参数修改器（parameter modifier）；工厂函数（factory function）；有限差分梯度（finite-difference gradient）；刷毛微分方程（LuGre bristle ODE）
- 环境：MuJoCo 3.8.0 Python；Ubuntu 22.04 x86_64；最小单关节 dcmotor/LuGre 模型。
- 症状：optimizer 0 iterations、finite-difference gradient 为 0；HTML report 中 initial 与 nominal torque 相同；identified 参数停在 initial。
- 诊断：确认传给 sysid.Parameter(modifier=...) 的对象是 callable，而不是 None。；在优化前手动改变 param，检查 spec、compile 后 model 和 residual 是否随之变化。
- 原因：两个 factory 的 return modifier 缩进在 inner modifier 内，outer factory 隐式返回 None。
- 处理过程：维护者展开 Python 作用域与缩进，检查 Parameter.apply_modifier 的 falsy no-op 路径。；维护者单独验证 biasprm\[3\] 写入 spec 后能进入 model，且 biasprm\[3\]/\[4\] 被 LuGre ODE 读取。
- 有效处理：把 return modifier 移到 outer factory 作用域；inner modifier 只更新 spec 参数。
- 结果：维护者将问题标为 resolved，并明确不做库侧修改，因为属于用户代码错误。
- 限制：原作者没有在评论中贴出修正后的优化数值；结论依据维护者代码诊断与参数通路检查。；其他零梯度问题仍可能来自尺度、可辨识性或残差设计，不能一概归因于缩进。
- 安全提示：将识别参数用于真实执行器前，应保留边界约束并用独立轨迹验证，不要仅凭优化器退出状态接受参数。
- 独立核验引用：[maintainer_confirmation · 维护者确认属于 user error、问题 resolved，不做库侧修改](https://github.com/google-deepmind/mujoco/issues/3286#issuecomment-4549965819)
- 适用边界：精确适用于 MuJoCo 3.8.0 sysid 参数 modifier factory 返回 None 的情形；其他零梯度需重新诊断。

### 核对永久外力的 world/body frame 缓存

- `problem_id`：`problem.simulation_toolchain.isaaclab_permanent_global_wrench_4580`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 永久 world-frame 外力会随 body frame 转向**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原作者沿固定 commit 的调用链说明：force 在 reset 时按当时姿态从 world frame 投影到 local frame，随后缓存 vector 每步以 `is_global=False` 应用；body frame 改变后没有重新投影，所以世界方向漂移甚至翻转。这个根因路径得到维护者正面回应。#4604 尝试 mixed representation，但仍处于 open，维护者指出它可能破坏 permanent local force 随 body rotation 的语义，作者也认可，因此不能当作已验证 fix。当前应先用旋转 180° 的最小测试同时检查永久 global 与 local force，再等待或实现能分别保持两种 frame 语义的修复。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #4580 详细调用链 3871986934、维护者回应 3889639271；开放 PR #4604 的未解决评审
- 原帖/精确回复：[Isaac Lab 永久 world-frame 外力会随 body frame 转向](https://github.com/isaac-sim/IsaacLab/issues/4580#issuecomment-3871986934)
- 平台/作者：GitHub Issues / LoreMoretti
- 关键术语：永久外力（permanent force）；世界坐标系（world frame）；机体坐标系（body frame）；混合表示（mixed representation）
- 环境：IsaacLab v2.3.2、commit 37ddf626871758333d6ed89cf64ad702aef127d0、Ubuntu 24.04、RTX 5090、CUDA 13.0、driver 580.126.09；原帖 Isaac Sim 版本字段未实际填写。
- 症状：世界系 `\[0,0,-10\]` 力在 body 绕 x 轴转 180° 后变成相反的世界方向；只影响 permanent wrench composer。
- 诊断：跟踪 reset 时 world-to-local 投影、`composed_forces_b` 缓存和后续 `is_global=False` 的 apply 调用，检查是否每步重投影。
- 原因：永久 world force 只在 reset 姿态下投影到 local frame，之后缓存的旧 local vector 被套到不断变化的新 body frame。
- 处理过程：作者提交 PR #4604，尝试使用 world orientation/link-origin 的 mixed representation；维护者随后指出 permanent local force tracking rotations 仍可能错误。
- 有效处理：当前没有合并且经维护者接受的修复；#4604 不能作为完成方案。
- 结果：维护者认可详细复现并计划修复；#4604 仍 open，作者对维护者指出的问题回复 `you're right`。
- 限制：Issue 的 Isaac Sim version 是模板占位文字，不能视为确切 5.0。；线程没有发布最终 workaround；若要恢复 v2.3.1 语义，应在目标版本自行做旋转 body 的方向不变量测试。
- 安全提示：外力用于真机或安全评估前，必须记录 force 表达 frame、application point 与每步实际 world wrench，避免方向翻转。
- 独立核验引用：[source_code · 原作者逐段绑定 commit 37ddf626 的 reset 投影、缓存与 apply 调用](https://github.com/isaac-sim/IsaacLab/issues/4580#issuecomment-3871986934)；[conflict · 维护者指出 proposed mixed representation 的 permanent local-force rotation 仍有问题](https://github.com/isaac-sim/IsaacLab/pull/4604#issuecomment-3908653234)
- 适用边界：适用于 v2.3.2 composable wrench permanent composer；其他版本需运行 global/local 两组旋转不变量测试。

### 选择支持 hfield 射线检测的 MuJoCo 后端

- `problem_id`：`problem.simulation_toolchain.mjx_hfield_ray_backend_2155`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MJX 不计划补齐 hfield ray，项目指向 MuJoCo Warp**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：按 MuJoCo 维护者在该线程的最终决定，不应把当前方案建立在 MJX 即将补齐此功能的假设上：该能力不计划加入 MJX。维护者明确指向 MuJoCo Warp 的 `ray`，其官方 API 文档包含 height fields。工程上应把它作为候选后端重新评估，但原帖没有证明两条后端在性能、数值或接口上完全等价。
- 证据状态：`issue_candidate`
- 来源定位：MuJoCo #2155 维护者最终回复 4707886038
- 原帖/精确回复：[MJX 不计划补齐 hfield ray，项目指向 MuJoCo Warp](https://github.com/google-deepmind/mujoco/issues/2155#issuecomment-4707886038)
- 平台/作者：GitHub Issues / nico-bohlinger
- 关键术语：高度场（height field, hfield）；射线检测（ray casting）；测距传感器（rangefinder）；计算后端（compute backend）
- 环境：原始请求针对 MJX 的 `mjx.ray` 与 hfield geom；线程未固定 MuJoCo 版本。
- 症状：`mjx.ray` 当时没有 hfield geom 实现，无法直接为 hfield locomotion terrain 生成所需射线结果。
- 诊断：先确认目标后端是 MJX 还是 MuJoCo Warp，再核对所需 geom 类型是否在该后端 `ray` API 中受支持。
- 原因：这是维护者确认的功能边界，不是原帖已经定位出的运行时故障。
- 处理过程：原帖提出把 CPU `mj_rayHfield` 移植到 MJX；后续贡献者询问是否可以实现。
- 有效处理：若需求是 hfield ray casting，按维护者指向评估 MuJoCo Warp `ray`；线程没有声称 MJX 与 MuJoCo Warp 可无成本互换。
- 结果：维护者明确 MJX 不计划此功能，并把 Issue 关闭；官方 MuJoCo Warp `ray` 文档列出 height fields。
- 限制：该结论只回答项目公开计划与后端能力选择，不比较两个后端的性能、数值一致性或完整迁移成本。
- 安全提示：把地形感知输入用于真机 WBC 前，还需独立验证量程、遮挡、坐标系和时延。
- 独立核验引用：[official_documentation · MuJoCo Warp ray API：维护者直接链接的 height-field ray casting 文档](https://mujoco.readthedocs.io/en/latest/mjwarp/api.html#mujoco_warp.ray)
- 适用边界：适用于需要 hfield ray casting、正在 MJX 与 MuJoCo Warp 间选型的项目；具体版本与迁移代价需另行验证。

### 修复 DART slip-compliance sentinel 告警回归

- `problem_id`：`problem.simulation_toolchain.gazebo_dart_slip_sentinel_3289`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Gazebo Ionic slip compliance -1 告警风暴由 DART 6.16.5 回归引起**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：如果环境与原帖一致，先不要批量修改模型。DART 的 `-1.0` 是“使用全局默认值”的哨兵值（sentinel value）；6.16.5 的校验回归把它错误地报警。DART PR #2493 已合并修复，并把发布记录指向 6.16.6；原作者通过 Homebrew 升级到 DART 6.16.6 后确认告警消失。只有参数不是这个 sentinel、而是 NaN/Inf 或自定义异常值时，才应继续检查模型数据。
- 证据状态：`issue_candidate`
- 来源定位：Gazebo #3289 作者复测 3818259239；合并 DART PR #2493
- 原帖/精确回复：[Gazebo Ionic slip compliance -1 告警风暴由 DART 6.16.5 回归引起](https://github.com/gazebosim/gz-sim/issues/3289#issuecomment-3818259239)
- 平台/作者：GitHub Issues / michael-p
- 关键术语：滑移柔度（slip compliance）；哨兵值（sentinel value）；接触约束（contact constraint）；回归缺陷（regression）
- 环境：macOS Homebrew；Gazebo Ionic 9.5.0；DART 6.16.5 触发，作者升级到 DART 6.16.6 后复测。
- 症状：控制台约每秒 100 行相同警告；Fuel 中大量模型受影响；`-v 0` 无效。；维护者报告 Homebrew CI 日志从小于 4 MB 增长到 1.5 GB 以上。
- 诊断：先检查 DART 版本；确认日志参数值恰为 sentinel `-1`，而不是 NaN/Inf 或显式非法配置。
- 原因：已合并 PR 确认：DART 6.16.5 的新校验把表示“use global default”的负值 sentinel 错误地当作非法 slip compliance。
- 处理过程：显式在 SDF 写 `slip1=0`、`slip2=0` 可让单模型安静，但不能解决大量 Fuel 模型；`-v 0` 无效。
- 有效处理：升级到包含 DART PR #2493 的 6.16.6；补丁对负值 sentinel 静默返回默认值，仅对 NaN/Inf 保留警告。
- 结果：PR 合并且相关修改行有测试覆盖；原作者确认升级 DART 6.16.6 后告警消失。
- 限制：该修复针对恰为负值 sentinel 的回归；若输入是 NaN/Inf 或自定义非预期值，仍应检查 SDF 和数值来源。
- 安全提示：不要通过全局丢弃 Gazebo stderr 来掩盖日志；先区分已知 sentinel 回归和真实接触参数错误。
- 独立核验引用：[pull_request · 已合并 PR c827858：区分负值 sentinel 与 NaN/Inf，并增加单元测试](https://github.com/dartsim/dart/pull/2493)
- 适用边界：适用于 Gazebo Ionic 9.5.0 / DART 6.16.5 的 `-1` sentinel 告警回归；其他错误值需另查。

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

### 验证 MJX 每环境 hfield 路由是否真实生效

- `problem_id`：`problem.reward_curriculum_randomization.mjx_batched_hfield_dataid_3258`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MJX-Warp 当前不能用 batched geom_dataid 路由每环境 hfield**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：该线程对应的公开实现不能这样使用。原帖给出的转换代码会把多维 `geom_dataid` 折叠为第一行；维护者也明确 batched `geom_dataid` 当前不计划加入 MJX，并指出 JIT 静态分析下的 collision driver 可能需要重构。作者只提到本地 monkey patch，没有发布补丁或结果，所以不能把它当作可复用解法。
- 证据状态：`issue_candidate`
- 来源定位：MuJoCo #3258 维护者关闭说明 4741236754
- 原帖/精确回复：[MJX-Warp 当前不能用 batched geom_dataid 路由每环境 hfield](https://github.com/google-deepmind/mujoco/issues/3258#issuecomment-4741236754)
- 平台/作者：GitHub Issues / nico-bohlinger
- 关键术语：批量几何数据标识（batched geom_dataid）；每环境路由（per-world routing）；即时编译（Just-In-Time compilation, JIT）；地形随机化（terrain randomization）
- 环境：`mujoco.mjx` 且 `impl=warp`；原帖基于 2026-05 的公开实现说明，未给发布版号。
- 症状：多维 `geom_dataid` 在 `_put_model_warp` 中被折叠到第一行，随后所有 world 收到相同映射。
- 诊断：检查转换路径中 `geom_dataid` 的形状是否在进入 Warp 前被压成一维，并实际记录各 world 使用的 data id。
- 原因：维护者说明，MJX collision driver 为 JIT 静态分析把 `geom_dataid` 当作 NumPy array；支持动态批量字段可能需要重构。
- 处理过程：作者说自己做过本地 monkey patch，但没有公开结果、补丁或复测数据；因此不把它登记为有效修复。
- 有效处理：线程没有已合并修复；当前只能把该能力视为未受支持，并在选用替代架构或自建 PR 前做最小验证。
- 结果：Issue 因功能不在计划中而关闭；维护者允许提交足够小且干净的 PR，但没有承诺接收。
- 限制：底层 MuJoCo Warp 的二维字段能力不等于 MJX 前端已暴露该能力；原帖也没有验证任意 monkey patch 的正确性。
- 安全提示：训练前应抽样打印每环境地形 ID 或几何统计，避免域随机化（domain randomization）静默失效。
- 独立核验引用：[maintainer_confirmation · 维护者说明不在计划内及 collision driver/JIT 静态分析约束](https://github.com/google-deepmind/mujoco/issues/3258#issuecomment-4741236754)
- 适用边界：适用于该线程所述 MJX-Warp 转换路径；后续版本若合入新实现需重新检查。

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

### Pinocchio 的 ABA、computeMinverse 与 Cholesky 路径选择

- `problem_id`：`problem.compute_performance_memory.pinocchio_forward_dynamics_minverse_selection_1215`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 前向动力学与质量矩阵逆的计算路径应按已计算量和乘法形式选择**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：维护者给出的通用规则是：已有质量矩阵时复用 Cholesky；已执行 ABA 时优先考虑 computeMinverse；只需 M^-1 乘向量时用 Cholesky solve，避免显式形成完整逆；需要矩阵-矩阵运算时才更可能需要完整 M^-1；通用 Eigen inverse 不能利用腿式机器人运动树稀疏性。可是原作者的接触 Jacobian 完整矩阵特例没有闭环：维护者链接的 contact-dynamics.hxx 使用 Cholesky，原作者指出与前述建议不一致后没有获得解释。因此应把这些规则作为候选起点，并在目标矩阵运算上 benchmark。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1215 评论 630212062 给出通用决策规则；评论 630280866 指向 contact-dynamics.hxx；评论 631426324 指出特例未解释的矛盾，之后无技术回复
- 原帖/精确回复：[Pinocchio 前向动力学与质量矩阵逆的计算路径应按已计算量和乘法形式选择](https://github.com/stack-of-tasks/pinocchio/issues/1215#issuecomment-630212062)
- 平台/作者：GitHub Issues / andreadelprete
- 关键术语：关节空间前向动力学算法（Articulated-Body Algorithm, ABA）；复合刚体算法（Composite Rigid Body Algorithm, CRBA）；质量矩阵逆（inverse mass matrix）；乔列斯基分解（Cholesky decomposition）；运动树稀疏性（kinematic-tree sparsity）
- 环境：2020 年 Pinocchio C++ API；原帖给出典型 nv=18、3k=12 的接触 Jacobian 规模，但没有软件版本、硬件、编译器或实测时延。
- 症状：同一库提供多条前向动力学和质量矩阵逆路径，调用者不确定是否需要逐应用 benchmark。；原作者需要构造含接触 Jacobian 和 M^-1 的完整矩阵并进一步计算 matrix exponential。
- 诊断：先区分所需结果是完整 M^-1、M^-1 乘向量，还是接触投影/矩阵-矩阵运算。；记录当前计算图是否已经得到 M 或已执行 ABA，再选择可以复用中间量的算法。；腿式运动树可利用稀疏性；不要默认把 CRBA 结果交给通用 Eigen inverse。
- 处理过程：维护者按已有 M、已有 ABA、向量乘法和完整矩阵四种情况给出选择建议。；对于原作者的接触矩阵特例，维护者只链接了 contact-dynamics.hxx，没有解释其中 Cholesky 与此前建议的关系。
- 结果：通用选择规则得到维护者明确说明；原作者的接触矩阵特例没有最终算法选择、benchmark 或复测结果。
- 限制：不能从该线程断言 computeMinverse 对所有接触矩阵运算都最快；维护者指向的实现使用 Cholesky，而最后追问未回答。；线程没有给绝对时延、机器人拓扑对照或当前 Pinocchio 版本 benchmark；算法实现和复杂度可能已演进。；原帖写作 J*Minv*J，未给完整维度表达；本卡不自行补写是否应有转置。
- 安全提示：实时 WBC 上线前应在目标模型、编译选项和矩阵形状上测量最坏时延；平均更快不等于满足硬实时截止时间。
- 独立核验引用：[issue · 原作者指出接触矩阵实现使用 Cholesky，与已调用 ABA 后优先 computeMinverse 的建议关系未被解释](https://github.com/stack-of-tasks/pinocchio/issues/1215#issuecomment-631426324)；[source_code · 维护者为接触矩阵特例直接给出的固定源码位置](https://github.com/stack-of-tasks/pinocchio/blob/ada5b11e5881e3fbc28e3bac717075ed8fa6855c/src/algorithm/contact-dynamics.hxx#L39)
- 适用边界：适用于 Pinocchio 中 ABA/CRBA/质量矩阵逆及接触矩阵运算的方案预选；最终路径需按当前版本、目标机器人和乘法形式实测。

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

### OCS2 observation feedback 低通滤波能稳定步行但引入相位延迟

- `problem_id`：`problem.state_estimation_calibration.ocs2_observation_lowpass_delay_27`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OCS2 与 RaiSim/WBC 闭环中姿态约定错误及观测低通滤波的边界**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：只能视为该线程环境中的阶段性工程方案。原作者报告低通滤波让 MPC 的 base pose/twist 参考更平滑，并使当前四足步行闭环稳定；项目贡献者同时明确指出，滤波会加入人工 phase shift/delay，可能妨碍更动态运动。帖子没有滤波器参数或动态动作复测，所以应用到目标机器人前必须实测延迟与稳定裕度。
- 证据状态：`issue_candidate`
- 来源定位：OCS2 #27：原作者评论 999336345 报告低通滤波后可行走；贡献者评论 999452836 警告动态动作的 phase shift/delay
- 原帖/精确回复：[OCS2 与 RaiSim/WBC 闭环中姿态约定错误及观测低通滤波的边界](https://github.com/leggedrobotics/ocs2/issues/27#issuecomment-999452836)
- 平台/作者：GitHub Issues / edward9503
- 关键术语：低通滤波（low-pass filter）；相位偏移（phase shift）；时延（delay）；稳定裕度（stability margin）
- 环境：ANYmal C、RaiSim、自研 WBC 1 kHz、mrtDesiredFrequency 1 kHz、mpcDesiredFrequency=-1（作者机器实际约 250 Hz）；未给 OCS2 commit。
- 症状：以 1 kHz 更新 observation_ 时，机器人起初站立不动，随后漂移。；把 observation_ 更新降到 1 Hz 后，RViz 机器人位置跳变，RaiSim 侧再次不稳定。；作者尝试多组 MRT/MPC/observation 更新频率仍不稳定。
- 诊断：先核对 MPC 与仿真/WBC 两侧的姿态约定和 quaternion 到 Euler ZYX 的转换。；分离 MPC feedforward 与 WBC 对 base pose/twist 的附加反馈，检查是否把 MPC 已有反馈重复叠加。；不要仅靠改变 observation 更新频率判断根因；同时检查参考状态/输入的连续性和坐标变换。
- 原因：原作者最终确认存在 quaternion 到 Euler ZYX 的微小计算错误。；贡献者指出，WBC 中额外的 base pose/twist error feedback 可能与 MPC 自身的测量状态反馈叠加并使闭环失稳。
- 处理过程：作者在 1 kHz 和 1 Hz 以及其他 MRT/MPC/observation 频率组合间尝试，均未直接解决。；作者修正 quaternion-to-Euler ZYX 计算后，四足能够行走。；作者把全状态和输入反馈给 MPC，在 WBC 初测中只跟踪 base pose 与腿关节角，并对真实 observation feedback 加低通滤波。
- 有效处理：修正 quaternion 到 Euler ZYX 的姿态转换错误；这是原作者明确确认有效的修复。；低通滤波 observation feedback 在作者当前步行测试中使 MPC 参考更平滑并稳定了闭环，但仅是该环境的工程做法。
- 结果：原作者明确回复修正姿态转换后 quadruped can walk。；原作者报告低通滤波后的 current walkable WBC 可稳定行走；贡献者认可当前结果，同时警告动态动作中的相位延迟风险。
- 限制：帖子没有公开姿态转换代码、滤波器类型、截止频率或延迟量，不能复制一个通用滤波参数。；贡献者建议仅跟踪 MPC desired base acceleration，但原作者只表示将尝试，线程没有给出该方案的复测结果。；低通滤波结果只覆盖作者当时的步行测试，未覆盖更动态运动。
- 安全提示：实机接入前应离线验证姿态约定、单位和符号；任何新增滤波必须测量相位延迟，并在低速/悬空或安全支撑条件下逐步闭环。
- 图片分析：第一段 GIF 已在多个时刻核验：画面左右分别是 RViz 和 RaiSim，左侧机器人出现明显多姿态重影，右侧机器人姿态与左侧参考不一致；没有时间戳、数值或坐标说明，不能从图中量化漂移。；第二段 GIF 已在多个时刻核验：两帧中左侧 RViz 足端轨迹/机器人姿态和右侧 RaiSim 机器人姿态发生明显跳变；它支持帖子描述的可视不同步/不稳定症状，但不单独证明更新频率或姿态转换是根因。
- 独立核验引用：[issue · 原作者报告 observation feedback 低通滤波后当前闭环可稳定行走](https://github.com/leggedrobotics/ocs2/issues/27#issuecomment-999336345)；[maintainer_confirmation · 项目贡献者提醒滤波引入 phase shift/delay，可能影响更动态运动](https://github.com/leggedrobotics/ocs2/issues/27#issuecomment-999452836)
- 适用边界：仅覆盖原帖 ANYmal C/RaiSim/OCS2/自研 WBC 的当时步行测试；更动态动作与不同滤波参数必须重新验证。

### OCS2/RaiSim/WBC 状态回灌因 quaternion-to-Euler ZYX 转换错误而失稳

- `problem_id`：`problem.state_estimation_calibration.ocs2_quaternion_euler_zyx_feedback_27`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OCS2 与 RaiSim/WBC 闭环中姿态约定错误及观测低通滤波的边界**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：贡献者先建议核对两侧 orientation convention；原作者随后确认 quaternion 到 Euler ZYX 的一个微小计算错误，修正后四足能够行走。线程同时提醒，MPC 已用测量状态闭环时，WBC 对 base pose/twist 的额外强反馈可能重复叠加；但原作者没有在该线程验证“只跟踪 desired base acceleration”这一建议，因此它只能作为后续排查项。
- 证据状态：`issue_candidate`
- 来源定位：OCS2 #27：贡献者评论 998091116 建议核对姿态约定；原作者评论 999336345 确认 quaternion→Euler ZYX 修复后可行走
- 原帖/精确回复：[OCS2 与 RaiSim/WBC 闭环中姿态约定错误及观测低通滤波的边界](https://github.com/leggedrobotics/ocs2/issues/27#issuecomment-999336345)
- 平台/作者：GitHub Issues / edward9503
- 关键术语：姿态约定（orientation convention）；四元数（quaternion）；欧拉角 ZYX（Euler ZYX）；测量状态回灌（measured-state feedback）
- 环境：ANYmal C、RaiSim、自研 WBC 1 kHz、mrtDesiredFrequency 1 kHz、mpcDesiredFrequency=-1（作者机器实际约 250 Hz）；未给 OCS2 commit。
- 症状：以 1 kHz 更新 observation_ 时，机器人起初站立不动，随后漂移。；把 observation_ 更新降到 1 Hz 后，RViz 机器人位置跳变，RaiSim 侧再次不稳定。；作者尝试多组 MRT/MPC/observation 更新频率仍不稳定。
- 诊断：先核对 MPC 与仿真/WBC 两侧的姿态约定和 quaternion 到 Euler ZYX 的转换。；分离 MPC feedforward 与 WBC 对 base pose/twist 的附加反馈，检查是否把 MPC 已有反馈重复叠加。；不要仅靠改变 observation 更新频率判断根因；同时检查参考状态/输入的连续性和坐标变换。
- 原因：原作者最终确认存在 quaternion 到 Euler ZYX 的微小计算错误。；贡献者指出，WBC 中额外的 base pose/twist error feedback 可能与 MPC 自身的测量状态反馈叠加并使闭环失稳。
- 处理过程：作者在 1 kHz 和 1 Hz 以及其他 MRT/MPC/observation 频率组合间尝试，均未直接解决。；作者修正 quaternion-to-Euler ZYX 计算后，四足能够行走。；作者把全状态和输入反馈给 MPC，在 WBC 初测中只跟踪 base pose 与腿关节角，并对真实 observation feedback 加低通滤波。
- 有效处理：修正 quaternion 到 Euler ZYX 的姿态转换错误；这是原作者明确确认有效的修复。；低通滤波 observation feedback 在作者当前步行测试中使 MPC 参考更平滑并稳定了闭环，但仅是该环境的工程做法。
- 结果：原作者明确回复修正姿态转换后 quadruped can walk。；原作者报告低通滤波后的 current walkable WBC 可稳定行走；贡献者认可当前结果，同时警告动态动作中的相位延迟风险。
- 限制：帖子没有公开姿态转换代码、滤波器类型、截止频率或延迟量，不能复制一个通用滤波参数。；贡献者建议仅跟踪 MPC desired base acceleration，但原作者只表示将尝试，线程没有给出该方案的复测结果。；低通滤波结果只覆盖作者当时的步行测试，未覆盖更动态运动。
- 安全提示：实机接入前应离线验证姿态约定、单位和符号；任何新增滤波必须测量相位延迟，并在低速/悬空或安全支撑条件下逐步闭环。
- 图片分析：第一段 GIF 已在多个时刻核验：画面左右分别是 RViz 和 RaiSim，左侧机器人出现明显多姿态重影，右侧机器人姿态与左侧参考不一致；没有时间戳、数值或坐标说明，不能从图中量化漂移。；第二段 GIF 已在多个时刻核验：两帧中左侧 RViz 足端轨迹/机器人姿态和右侧 RaiSim 机器人姿态发生明显跳变；它支持帖子描述的可视不同步/不稳定症状，但不单独证明更新频率或姿态转换是根因。
- 独立核验引用：[maintainer_confirmation · 项目贡献者确认 measured-state feedback 方向正确，并建议核对 orientation convention](https://github.com/leggedrobotics/ocs2/issues/27#issuecomment-998091116)；[issue · 原作者确认修正 quaternion 到 Euler ZYX 计算后四足可以行走](https://github.com/leggedrobotics/ocs2/issues/27#issuecomment-999336345)
- 适用边界：适用于 OCS2 MPC、RaiSim 和自研 WBC 之间传递浮基姿态的接口；具体状态布局、旋转顺序和单位必须按目标代码核对。

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

### OmniH2O 实时稀疏关键点输入不重复离线全身重定向

- `problem_id`：`problem.state_estimation_calibration.omnih2o_sparse_keypoints_no_online_retarget_13`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OmniH2O 实时稀疏遥操直接使用人体关键点，不走离线全身动作重定向**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：项目作者说明不需要。实机部署直接使用视觉系统输出的人体全局关键点位置，因为策略跟踪的是稀疏输入（sparse inputs），不是完整全身动作（whole-body motions）；离线 SMPL→H1 gradient retargeting 属于训练数据准备路径。原线程没有公开关键点到机器人/Isaac Gym 坐标的具体矩阵变换，因此坐标标定仍需另行验证。
- 证据状态：`issue_candidate`
- 来源定位：human2humanoid #13：作者评论 2426760408/2426762777 给出传感路径，2426906228/2426908658 确认直接 keypoint 与 sparse-input 原因
- 原帖/精确回复：[OmniH2O 实时稀疏遥操直接使用人体关键点，不走离线全身动作重定向](https://github.com/LeCAR-Lab/human2humanoid/issues/13#issuecomment-2426906228)
- 平台/作者：GitHub Issues / FinnJob
- 关键术语：稀疏输入（sparse inputs）；全局关键点位置（global keypoint positions）；动作重定向（motion retargeting）；坐标标定（coordinate calibration）
- 环境：human2humanoid/OmniH2O 部署语境；Apple Vision Pro 或 RGB camera + HybrIK；原帖未给软件 commit、频率和相机标定参数。
- 症状：使用者看到训练数据预处理会把 SMPL motion 通过 gradient descent 转成 H1 reference，因此不知道实时视觉输入如何满足同一接口。
- 诊断：先区分策略任务定义：offline whole-body motion tracking 与 online sparse keypoint tracking 不是同一输入路径。；确认实时策略实际消费哪些全局 keypoint positions，而不是默认重建完整 AMASS/SMPL motion。
- 原因：把用于全身训练数据准备的离线 SMPL→H1 retargeting 流程误认为实时 sparse-input 部署的必经步骤。
- 处理过程：原作者先询问如何实时取得 processed AMASS-like joint data，项目作者澄清其部署不需要该全身 reference。
- 有效处理：按项目作者说明，从 Vision Pro 或 RGB+HybrIK 获取人体全局关键点位置，作为 sparse tracking reference 直接输入部署路径，不在实时环重复完整动作重定向。
- 结果：提问者回复已理解 sparse-input 与 whole-body retargeting 的区别。
- 限制：线程没有回答 RGB/HybrIK 坐标到 Isaac Gym/机器人世界坐标的具体矩阵变换、尺度、原点或时间同步。；没有公开实时部署代码、输入张量布局或延迟测量，不能仅凭此卡复现实机系统。
- 安全提示：实机使用前仍需单独验证坐标系、尺度、时间戳、异常关键点过滤和速度/位置限幅。
- 独立核验引用：[maintainer_confirmation · 项目作者说明使用 Vision Pro 与 RGB+HybrIK 获取人体全局位置](https://github.com/LeCAR-Lab/human2humanoid/issues/13#issuecomment-2426760408)；[maintainer_confirmation · 项目作者解释无需全身重定向的原因是策略跟踪 sparse inputs](https://github.com/LeCAR-Lab/human2humanoid/issues/13#issuecomment-2426908658)；[issue · 原作者关于 RGB/Isaac Gym matrix transform 的追问未获项目回答，构成明确未覆盖边界](https://github.com/LeCAR-Lab/human2humanoid/issues/13#issuecomment-2446010339)
- 适用边界：适用于 human2humanoid/OmniH2O 的 sparse tracking 部署设计；坐标变换和具体输入格式未在原线程公开。

### Pinocchio Translation+SphericalZYX 根关节的基座速度使用 WORLD frame

- `problem_id`：`problem.state_estimation_calibration.pinocchio_translation_sphericalzyx_velocity_world_2177`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Translation+SphericalZYX 复合根关节的广义基座速度按 WORLD frame 表达**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原作者在多组配置和项目贡献者提供的 floating-base velocity viewer 基础上测试后确认，该 Translation+SphericalZYX 复合根关节的 floating-base velocity 表达在 WORLD frame。这个结论不能套用到 FreeFlyer：FreeFlyer 的 LOCAL 速度约定属于不同 joint model。线程没有贴完整扩展脚本和数值输出，因此升级版本后仍应复测。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #2177 评论 2007410825 链接 PR #2143/固定 viewer；评论 2008762724 原作者给出测试结论
- 原帖/精确回复：[Translation+SphericalZYX 复合根关节的广义基座速度按 WORLD frame 表达](https://github.com/stack-of-tasks/pinocchio/issues/2177#issuecomment-2008762724)
- 平台/作者：GitHub Issues / thuuzi
- 关键术语：广义速度（generalized velocity）；复合根关节（composite root joint）；世界坐标系（world frame）；局部坐标系（local frame）；局部原点世界对齐坐标系（local-world-aligned frame）
- 环境：Pinocchio C++、自定义 URDF、JointModelComposite(Translation+SphericalZYX)；线程引用 commit 080720a 的官方 Python viewer，未给发布版本或 OS。
- 症状：在 LOCAL_WORLD_ALIGNED frame 获取末端 Jacobian 时，基座线速度对应的 top-left 3×3 对随机配置始终为单位阵。
- 诊断：不要把 FreeFlyer 的 LOCAL velocity 约定自动套到其他复合根关节。；用官方 floating-base velocity viewer 扩展到目标 root joint，并在不同 base orientation 下观察世界/局部速度箭头或 Jacobian 块。
- 原因：不同根关节模型定义了不同的广义速度参数化；原作者测试确认 Translation+SphericalZYX 组合使用 WORLD-frame base velocity。
- 处理过程：原作者随机测试多组配置并检查 Jacobian 基座块。；项目贡献者提供官方 floating-base velocity viewer；原作者扩展后报告测试结论。
- 有效处理：按 JointModelTranslation+JointModelSphericalZYX 的 WORLD-frame velocity 约定解释状态和 Jacobian，不复用 FreeFlyer 的 LOCAL-frame 假设。
- 结果：原作者测试后明确确认该复合根关节的 floating-base velocity 在 WORLD frame。
- 限制：线程没有贴扩展后的脚本、配置向量或数值输出；不同 Pinocchio 版本应再次运行 viewer/数值对照。；结论只针对 JointModelTranslation+JointModelSphericalZYX 组合，不外推任意 JointModelComposite。；FreeFlyer 的 LOCAL 约定仍是另一种 joint model 的语义，两者不能互相覆盖。
- 安全提示：将基座速度送入实机 WBC 前，应对旋转基座做 frame 单元测试；错误 frame 可同时污染速度反馈、动量和接触约束。
- 独立核验引用：[source_code · 项目贡献者提供、由原作者扩展用于该 root-joint 组合的官方可视化脚本](https://github.com/stack-of-tasks/pinocchio/blob/080720adb012468ad4ff2956383199a6877608c7/examples/floating-base-velocity-viewer.py)；[issue · 原作者测试后明确报告 WORLD-frame 结论](https://github.com/stack-of-tasks/pinocchio/issues/2177#issuecomment-2008762724)
- 适用边界：适用于 JointModelComposite 中依次加入 JointModelTranslation 与 JointModelSphericalZYX 的根关节模型；其他 root joint 需单独核对。

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

### rmw_zenoh 下 controller_manager 服务调用拖慢实时环

- `problem_id`：`problem.communication_and_realtime.ros2_control_zenoh_service_overrun_2808`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ros2_control 高频服务调用卡顿在该案例中由 rmw_zenoh 切换 RMW 消除**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：在该 Jazzy/4.38.0/UR 环境中，作者用 A/B 确认把 RMW_IMPLEMENTATION 从 rmw_zenoh_cpp 切到 rmw_fastrtps_cpp 后现象消失；其在 Zenoh 0.2.8 deb 和 0.2.9 固定提交上都复现。可把切换 RMW 作为隔离手段，但 Zenoh 为何在服务/发布路径引入延迟没有定位，Cyclone DDS 也未在帖中给出实测。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #2808 评论 3541490499、3541707255；维护者未复现见 3541065379/3541219103
- 原帖/精确回复：[ros2_control 高频服务调用卡顿在该案例中由 rmw_zenoh 切换 RMW 消除](https://github.com/ros-controls/ros2_control/issues/2808#issuecomment-3541707255)
- 平台/作者：GitHub Issues / rafa-martin
- 关键术语：机器人操作系统中间件实现（ROS middleware implementation, RMW）；控制环超时（control-loop overrun）；实时数据交换（Real-Time Data Exchange, RTDE）；服务调用（service call）
- 环境：Ubuntu 24.04；kernel 6.8.1-1037-realtime PREEMPT_RT；ROS 2 Jazzy；ros-jazzy-controller-manager 4.38.0-1noble.20251008.000820；rmw_zenoh 0.2.8 deb 与 0.2.9 commit 858f7b5；Intel i7-11700。
- 症状：list_controllers 单次/每秒调用会令 update 约 3.16 ms、总周期约 3.33 ms，错过 500 Hz deadline。；频繁时 UR RTDE Data Pipeline overflow 并断连。
- 诊断：固定 ros2_control/controller_manager 版本，只切换 RMW_IMPLEMENTATION 做 A/B。；对比服务调用前、中、后的 controller_manager.total_time；维护者同版本本地未复现，提示不是单纯 controller_manager 版本问题。
- 原因：作者确认现象随 rmw_zenoh 出现，换 Fast DDS 后消失；Zenoh 内部具体锁与机制没有继续定位。
- 处理过程：作者提供服务调用、rqt、系统负载证据；维护者测量 mutex 区域仅约 20 us。；作者从 rmw_zenoh 切到 rmw_fastrtps，并在两个 Zenoh 版本上复现。
- 有效处理：在该环境临时从 rmw_zenoh 切换到 Fast DDS；作者也计划使用 Cyclone DDS。
- 结果：作者 100% confirmed 仅切换 RMW 即消除现象；根因未深入，Issue 后因 stale 关闭。
- 限制：不能据此断言所有 rmw_zenoh 版本或所有服务调用都有该问题。；Cyclone DDS 在该线程没有给出实际测试数据，只是作者计划。；Issue 的 stale 关闭不等于 Zenoh 根因修复。
- 安全提示：RMW 切换应在实验台验证 QoS、服务语义和控制周期，再恢复真机高速运行。
- 独立核验引用：[issue · 维护者同版本测量 mutex 区域约 20 us 且无法复现，支持继续隔离环境差异](https://github.com/ros-controls/ros2_control/issues/2808#issuecomment-3541219103)
- 适用边界：Ubuntu 24.04 PREEMPT_RT、ROS 2 Jazzy、controller_manager 4.38.0、UR 500 Hz 与 rmw_zenoh 0.2.8/0.2.9。

### ROS 2 Humble joint_trajectory_controller 的版本化时延差异

- `problem_id`：`problem.communication_and_realtime.ros2_humble_jtc_jitter_808`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ROS 2 Humble 控制循环抖动要区分打印开销与发行版控制器实现**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：先移除实时循环里的 print 干扰，并把时延分段到 read/controller update/write。该作者定位到 joint_trajectory_controller 后，对比发现 apt 的 Humble 包偶发 2000–3000 us，而当时从 master 构建的源码版偶发小于 500 us，机器人抖动明显降低；维护者确认近期改进尚未同步到 Humble。由于帖子没有给 master commit，实际使用时应固定源码提交并重新做最坏时延测试，而不是直接追随 master。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #808 测量警告 1242789008，作者对照 1248844616/1248848453，维护者确认 1264354371
- 原帖/精确回复：[ROS 2 Humble 控制循环抖动要区分打印开销与发行版控制器实现](https://github.com/ros-controls/ros2_control/issues/808#issuecomment-1264354371)
- 平台/作者：GitHub Issues / yeyanlei
- 关键术语：控制循环抖动（control-loop jitter）；抢占实时内核（PREEMPT_RT kernel）；最坏执行时间（worst-case execution time, WCET）；发行版回移（release backport）
- 环境：Ubuntu 22.04；ROS 2 Humble；Linux 5.15.55-rt48 PREEMPT_RT；FIFO priority 90；1 ms loop；joint_trajectory_controller、hand controller、joint_state_broadcaster。
- 症状：measured_period 偶发 2–6 ms；作者定位 controller_manager update 内 joint_trajectory_controller 延迟。
- 诊断：不要在每个实时循环中使用 std::cout/print 作为唯一测量方法，先移除或改成预分配缓冲的低扰动 trace。；分别测 read、controller update、write，并记录具体 controller 和配置。；对比发行版二进制与固定源码提交，而不是只比较模糊的 master。
- 原因：维护者确认当时近期性能改进尚未同步到 Humble；线程未给具体 commit。
- 处理过程：作者把 apt 安装的 joint_trajectory_controller 与当时 master 源码构建做时延对照。
- 有效处理：作者改用源码版 joint_trajectory_controller 后，报告执行时间从偶发 2000–3000 us 降到偶发小于 500 us，机器人抖动明显降低。
- 结果：维护者确认改进未同步到 Humble并关闭问题；没有精确补丁或长期统计。
- 限制：master 是移动目标，必须记录实际 commit；不能把 500 us 视为所有硬件的保证。；循环内 print 本身会扰动测量，原线程数字只能作为该环境对照。
- 安全提示：实时控制器升级后必须在目标负载下做周期分布、最坏时延和 deadline miss 回归，再连接高功率执行器。
- 独立核验引用：[maintainer_confirmation · 维护者确认近期改进尚未同步到 Humble，并因作者已解决而关闭](https://github.com/ros-controls/ros2_control/issues/808#issuecomment-1264354371)
- 适用边界：适用于 2022 年 ROS 2 Humble/PREEMPT_RT 的该控制器版本差异；当前发行版需重新对照。

### ros2_control hardware component 级 rw_rate

- `problem_id`：`problem.communication_and_realtime.ros2_control_component_rw_rate_649`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ros2_control 多速率要区分组件级 rw_rate 与单组件内部信号节流**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：有。合并的 PR #1570 为每个 ros2_control hardware component 增加 rw_rate，并更新 different update rates 官方文档、解析/调度实现和测试。文档示例让 system、actuator、sensor 分别运行 500/200/250 Hz；未设置时跟随 controller_manager，配置频率高于 controller_manager 时也只按 controller_manager 频率运行。使用前仍要核对目标 ROS 2 发行版是否包含该合并提交。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #649 维护者指向 PR #1570 的评论 2245933173；merged PR #1570 文档、实现和测试
- 原帖/精确回复：[ros2_control 多速率要区分组件级 rw_rate 与单组件内部信号节流](https://github.com/ros-controls/ros2_control/issues/649#issuecomment-2245933173)
- 平台/作者：GitHub Issues / bijoua29
- 关键术语：硬件组件（hardware component）；读写频率（read/write rate, rw_rate）；控制器管理器（controller manager）；异步硬件（asynchronous hardware）
- 环境：ros2_control rolling/master 时期；PR #1570 已合并；具体 ROS 2 发行版需查看 backport。
- 症状：固定高频 read/write 会让低频状态占用带宽，引发重试、丢包和额外时延。
- 诊断：先判断不同频率信号是否能拆为不同 ros2_control hardware components。；区分 controller update rate、hardware component rw_rate 与单 component 内部每个 state 的实际采样率。；为复用旧值的 state 暴露时间戳或陈旧度，避免控制器把缓存值当新样本。
- 处理过程：PR #1570 实现每个 hardware component 的 rw_rate，并更新官方不同更新率文档。；维护者建议同 component 内用 counter/internal filtering 跳过低频电压读取，或拆分 components。
- 有效处理：跨 component：在 ros2_control 标签配置 rw_rate；高于 controller_manager rate 时实际被 controller_manager rate 限制。；同 component：在硬件 read 内按计数器/过滤规则低频更新目标 state，跳过周期保留上次值；或重构为独立 component。
- 结果：组件级 rw_rate 已合并并有文档/测试；按 controller 请求 state 子集的细粒度接口仍未在该线程实现。
- 限制：PR #1570 当时参数名和语义对应其合并版本；不同 ROS 2 发行版需核对是否已回移。；同 component 的 counter 方案是维护者建议，线程没有贴出调用者的部署复测。
- 安全提示：低频状态复用旧值时，应携带时间戳/validity 并设置超时；温度、电压或故障状态过期不能静默用于安全决策。
- 独立核验引用：[pull_request · 已合并 PR 增加 rw_rate、官方 userdoc、release note、实现与多频率测试](https://github.com/ros-controls/ros2_control/pull/1570)
- 适用边界：适用于包含 ros-controls/ros2_control PR #1570 的版本；发行版包是否回移需单独确认。

### 单个 ros2_control hardware component 内信号的多速率读取

- `problem_id`：`problem.communication_and_realtime.ros2_control_single_component_signal_rates_649`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ros2_control 多速率要区分组件级 rw_rate 与单组件内部信号节流**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该线程没有实现按 state interface 或 controller 请求子集的调度。维护者给出的现有做法是：若能拆分就建不同 components；否则在 hardware read 内用 counter/internal filtering 只按低频更新电压等状态，跳过的周期继续保留上次值。维护者明确说明 controller 高频读取时会复用缓存 state。因为调用者仍把自动子集调度视为增强诉求，这个方案应标为工程实现建议，而不是框架已提供的逐 interface 调度。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #649 缓存语义 2246159316，单组件 counter/拆分建议 2246220069，调用者说明增强仍未实现 2246280084
- 原帖/精确回复：[ros2_control 多速率要区分组件级 rw_rate 与单组件内部信号节流](https://github.com/ros-controls/ros2_control/issues/649#issuecomment-2246220069)
- 平台/作者：GitHub Issues / bijoua29
- 关键术语：状态接口（state interface）；内部节流（internal filtering/throttling）；缓存状态（cached state）；数据陈旧度（data staleness）
- 环境：ros2_control rolling/master 时期；PR #1570 已合并；具体 ROS 2 发行版需查看 backport。
- 症状：固定高频 read/write 会让低频状态占用带宽，引发重试、丢包和额外时延。
- 诊断：先判断不同频率信号是否能拆为不同 ros2_control hardware components。；区分 controller update rate、hardware component rw_rate 与单 component 内部每个 state 的实际采样率。；为复用旧值的 state 暴露时间戳或陈旧度，避免控制器把缓存值当新样本。
- 处理过程：PR #1570 实现每个 hardware component 的 rw_rate，并更新官方不同更新率文档。；维护者建议同 component 内用 counter/internal filtering 跳过低频电压读取，或拆分 components。
- 有效处理：跨 component：在 ros2_control 标签配置 rw_rate；高于 controller_manager rate 时实际被 controller_manager rate 限制。；同 component：在硬件 read 内按计数器/过滤规则低频更新目标 state，跳过周期保留上次值；或重构为独立 component。
- 结果：组件级 rw_rate 已合并并有文档/测试；按 controller 请求 state 子集的细粒度接口仍未在该线程实现。
- 限制：PR #1570 当时参数名和语义对应其合并版本；不同 ROS 2 发行版需核对是否已回移。；同 component 的 counter 方案是维护者建议，线程没有贴出调用者的部署复测。
- 安全提示：低频状态复用旧值时，应携带时间戳/validity 并设置超时；温度、电压或故障状态过期不能静默用于安全决策。
- 独立核验引用：[maintainer_confirmation · 维护者说明低频 hardware 更新之间 controller 会复用同一 state 值](https://github.com/ros-controls/ros2_control/issues/649#issuecomment-2246159316)
- 适用边界：适用于同一 hardware component 内混合高低频状态；需自行实现缓存、时间戳和超时语义。

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

### Isaac Lab ONNX 输出与 ActionTerm 后处理的边界

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.isaaclab_onnx_actionterm_postprocess_2636`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 导出 ONNX 后不要假定 ActionTerm 的 scale 与 clipping 已打包**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：原帖回复建议把两层处理拆开核对：ActionTerm 的 scale、clipping 等后处理通常需要在实机侧复现；RSL-RL agent 配置内的 clipping 则可能已经进入导出模型。由于回复带有不确定措辞且没有复测，可靠做法不是直接照搬乘法，而是对同一 observation 比较训练环境 actuator 前的最终 action 与 ONNX 加部署后处理的逐元素结果。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #2636 唯一评论 2954156235
- 原帖/精确回复：[Isaac Lab 导出 ONNX 后不要假定 ActionTerm 的 scale 与 clipping 已打包](https://github.com/isaac-sim/IsaacLab/issues/2636#issuecomment-2954156235)
- 平台/作者：GitHub Issues / lde-RL
- 关键术语：动作缩放（action scaling）；动作裁剪（action clipping）；动作项（ActionTerm）；模型后处理（post-processing）
- 环境：Isaac Lab + RSL-RL + ONNX sim-to-real；原帖未给软件版本、机器人或导出脚本提交。
- 症状：ONNX 输出超过 \[-1,1\]，例如 1.5 或 -2.0；部署者不确定是否还要乘 action_scale。
- 诊断：分别列出 RSL-RL agent 配置中的处理与 Isaac Lab ActionTerm 中的 scale/clipping，不要把两层混为一层。；用同一 observation 对比训练环境中送入 actuator 前的最终 action 与 ONNX+部署后处理结果。
- 原因：回复者认为 ActionTerm 后处理可能不在 ONNX 中，而 agent 配置内的 clipping 可能在导出图内。
- 处理过程：回复建议在实机侧复现 ActionTerm 后处理，并单独核对 agent 配置是否已包含 clipping。
- 结果：得到排查分层，但没有作者复测、导出图检查或目标机器人结果。
- 限制：回复使用了 I think/might，不能视为所有版本和导出器的确定契约。；不能仅凭 ONNX 输出越界判断 scale 已应用或未应用。
- 安全提示：首次上机前离线逐元素对齐 action，并加硬件侧限幅、急停和低增益测试。
- 独立核验引用：[issue · 回复区分 ActionTerm 后处理与 agent 配置内处理，但没有复测](https://github.com/isaac-sim/IsaacLab/issues/2636#issuecomment-2954156235)
- 适用边界：Isaac Lab + RSL-RL 的 ONNX 部署排查入口；版本、导出脚本和 ActionTerm 类型未知，必须实测。

### GO1 actuator net 替换为 PD 后的作者实机结果

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.go1_actuator_pd_retrain_386`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Unitree GO1 策略上机前要同时核对关节顺序与 actuator 模型**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：作者把 GO1 actuator net 换成 PD model 并重新训练后，报告真实 GO1 不再突然踢腿、抖动到功率保护，并能在 velocity_commands 全零时站立。这是作者环境中的有效 workaround；由于同一线程还发现 motor order 不一致，且没有消融实验，不能把 actuator net 写成已证实的唯一根因，也不能直接复用未公开的 PD 参数。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #386 作者实机复测评论 2094062434
- 原帖/精确回复：[Unitree GO1 策略上机前要同时核对关节顺序与 actuator 模型](https://github.com/isaac-sim/IsaacLab/issues/386#issuecomment-2094062434)
- 平台/作者：GitHub Issues / Pansamic
- 关键术语：执行器网络（actuator network）；比例—微分模型（proportional-derivative model, PD model）；功率保护（power protection）；消融实验（ablation test）
- 环境：2024-04 的 Orbit/Isaac Lab unitree-go1-flat policy；真实 Unitree GO1；ONNX Runtime C++；原帖未给精确提交、SDK 或固件版本。
- 症状：零 velocity_commands 下，真实 GO1 腿部突然踢动、抖动并进入 power protection。
- 诊断：在训练环境打印 asset.joint_names 或 asset_cfg.joint_names，并与实机 SDK、legged-gym 和部署端 observation/action 数组逐项对齐。；若使用高度扫描，另外核对 Isaac Sim/Orbit 的 XY 与旧管线的 YX 排列。；把关节顺序修正与 actuator model 替换分开做 A/B 复测，避免把两个变化混成一个根因。
- 原因：作者确认 legged-gym 与 Orbit 的 motor order 实际不同。；作者怀疑 GO1 actuator net，但线程没有证明它是唯一根因。
- 处理过程：维护者给出打印 joint order 的代码并说明 BFS/DFS 与 height-scan 排列差异。；作者把 actuator net 换为 PD model 后重新训练。
- 有效处理：作者特定环境中，改用 PD model 重新训练后，真实 GO1 不再踢动、抖动到功率保护，并可在零速度命令下站立。
- 结果：实机症状消失；但 joint order 修正和 actuator model 替换没有单独消融，唯一根因未闭环。
- 限制：不能由该线程断言所有 GO1 actuator net 都有问题。；没有给出 PD stiffness/damping、动作限幅、策略提交或实机 SDK 版本。；height-scan 只是一项维护者提示，原作者没有报告它是否参与该策略。
- 安全提示：涉及实机突然踢腿和功率保护；重新上机必须使用吊架/保护绳、低增益、动作与力矩限幅、急停和人员隔离。
- 独立核验引用：[issue · 作者说明替换为 PD、重新训练后的真实 GO1 结果，同时使用 suspect 而非已证明措辞](https://github.com/isaac-sim/IsaacLab/issues/386#issuecomment-2094062434)
- 适用边界：只适用于该作者的 Orbit/GO1 策略链；PD 增益、限幅、SDK 与模型版本缺失，其他机器人必须重新训练和低风险复测。

### GO1 策略部署的关节与扫描顺序对齐

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.go1_policy_joint_order_386`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Unitree GO1 策略上机前要同时核对关节顺序与 actuator 模型**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原帖给出的可核对步骤是：在训练环境打印 asset.joint_names 或 asset_cfg.joint_names，再与 legged-gym、实机 SDK 和部署端数组逐项对齐；Isaac Gym/legged-gym 与 Isaac Sim/Orbit 还可能有 DFS/BFS 顺序差异，若策略包含 height scan，还要核对 XY/YX 排列。作者最终确认 legged-gym 与 Orbit 的 motor order 实际不同，但没有单独报告只修正顺序后的实机结果，因此这是一条必须执行的接口检查，而不是已隔离的唯一修复。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #386 评论 2082831221、2092587921 与作者确认 2094062434
- 原帖/精确回复：[Unitree GO1 策略上机前要同时核对关节顺序与 actuator 模型](https://github.com/isaac-sim/IsaacLab/issues/386#issuecomment-2094062434)
- 平台/作者：GitHub Issues / Pansamic
- 关键术语：关节顺序（joint ordering）；深度/广度优先遍历（depth-first/breadth-first parsing, DFS/BFS）；高度扫描（height scan）；观测—动作映射（observation-action mapping）
- 环境：2024-04 的 Orbit/Isaac Lab unitree-go1-flat policy；真实 Unitree GO1；ONNX Runtime C++；原帖未给精确提交、SDK 或固件版本。
- 症状：零 velocity_commands 下，真实 GO1 腿部突然踢动、抖动并进入 power protection。
- 诊断：在训练环境打印 asset.joint_names 或 asset_cfg.joint_names，并与实机 SDK、legged-gym 和部署端 observation/action 数组逐项对齐。；若使用高度扫描，另外核对 Isaac Sim/Orbit 的 XY 与旧管线的 YX 排列。；把关节顺序修正与 actuator model 替换分开做 A/B 复测，避免把两个变化混成一个根因。
- 原因：作者确认 legged-gym 与 Orbit 的 motor order 实际不同。；作者怀疑 GO1 actuator net，但线程没有证明它是唯一根因。
- 处理过程：维护者给出打印 joint order 的代码并说明 BFS/DFS 与 height-scan 排列差异。；作者把 actuator net 换为 PD model 后重新训练。
- 有效处理：作者特定环境中，改用 PD model 重新训练后，真实 GO1 不再踢动、抖动到功率保护，并可在零速度命令下站立。
- 结果：实机症状消失；但 joint order 修正和 actuator model 替换没有单独消融，唯一根因未闭环。
- 限制：不能由该线程断言所有 GO1 actuator net 都有问题。；没有给出 PD stiffness/damping、动作限幅、策略提交或实机 SDK 版本。；height-scan 只是一项维护者提示，原作者没有报告它是否参与该策略。
- 安全提示：涉及实机突然踢腿和功率保护；重新上机必须使用吊架/保护绳、低增益、动作与力矩限幅、急停和人员隔离。
- 独立核验引用：[maintainer_confirmation · 维护者给出打印实际 joint order 的代码并提示 Isaac Sim 与 Isaac Gym 顺序不同](https://github.com/isaac-sim/IsaacLab/issues/386#issuecomment-2082831221)
- 适用边界：适用于 legged-gym/Isaac Gym 策略向 Isaac Sim/Orbit 或真实 GO1 迁移；具体顺序必须以目标版本打印结果为准。

### 区分 Newton gain buffer 与实际双控制器

- `problem_id`：`problem.sim_to_sim_and_sim_to_real.newton_explicit_gain_mode_5806`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Newton 显式 actuator gains 写回不一定等于双控制器生效**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：不能直接判定。线程中两位独立排查者都确认写入顺序会把配置 stiffness/damping 写回 simulator-bound buffer，并都得到将其重定向到 actuator-data buffer 的 proposed patch；但 stock Go2 实测同时显示 `mjw_model.nu==0`、全部 joints 为 EFFORT mode，因此该资产上的 nonzero gains 没有对应 MJWarp actuator，不能解释约 0.118 rad 的 rest-pose 差异。只有 USD authored nonzero drive gains 使关节导入为 position/velocity mode、solver 实际创建 actuator 时，旧写入才可能形成双控制器。应联合检查 USD gains、target mode、`nu` 和 live torque；当前 patch 尚未合并。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #5806 原帖源码链与 proposed patch；独立确认/Go2 测量 4871459996
- 原帖/精确回复：[Newton 显式 actuator gains 写回不一定等于双控制器生效](https://github.com/isaac-sim/IsaacLab/issues/5806#issuecomment-4871459996)
- 平台/作者：GitHub Issues / ecstayalive
- 关键术语：显式执行器（explicit actuator）；目标模式（target mode）；零拷贝绑定（zero-copy binding）；静止姿态（rest pose）
- 环境：Isaac Lab 3.0.0 a4a7602f、isaaclab_newton 0.5.9、Newton 1.0.0、warp 1.12.0、mujoco-warp 3.5.0.2；独立测量 driver 570.211.01/CUDA 12.8；原帖 Ubuntu 24.04、Isaac Sim 6.0。
- 症状：同一 stock Go2 cfg 下 `data.joint_stiffness` 为 Newton 25.0、PhysX 0.0；zero-action hold 的 rest-pose 差约 0.118 rad。
- 诊断：同时检查写入顺序、`data.joint_stiffness`、USD authored drive gains、`JointTargetMode` 和 `mjw_model.nu`，不要只看 gain buffer。
- 原因：写入顺序确实让 explicit actuator 的配置 gains 回到 simulator-bound buffer；但其是否产生控制作用取决于导入 mode 和 MJWarp 是否实际创建 actuator。；独立回复认为 stock Go2 的剩余 rest-pose 差更像 solver/contact difference，但该部分只是其判断，未被维护者确认。
- 处理过程：原作者与独立回复者分别提出把两个 kernel outputs 改写到 `_actuator_stiffness/_actuator_damping`；独立回复额外转储 PhysX/Newton parsed model、mode 和 `nu`。
- 有效处理：当前没有合并修复。诊断时先按 asset 分成 authored-zero 与 authored-nonzero drive gains，再检查 `nu`/target mode；两行 buffer redirect 仍是 proposed patch，必须对两类资产做 regression test 后才能采用。
- 结果：独立回复确认写入链和 proposed redirect；stock Go2 上 gains 为 inert，因而否定了用该 bug 解释其 rest-pose 差异。
- 限制：Issue 仍开放，没有维护者技术结论或合并 PR；原帖所用资产的 USD drive gains 没有在回复中核对。；独立仓库与原始 JSON dumps 是外部工程记录，本轮未把其中未贴在线程的数字扩写为正式结论。
- 安全提示：后端对照应限制 effort、记录 mode/targets/actual torque，并在真机部署前单独验证硬件驱动不会叠加位置环。
- 独立核验引用：[independent_reproduction · 独立重走写入链并转储 stock Go2 live model；`nu==0` 限定双控制器结论](https://github.com/isaac-sim/IsaacLab/issues/5806#issuecomment-4871459996)
- 适用边界：适用于 Isaac Lab 3.0.0/Newton 0.5.9 附近的 explicit actuator 初始化；其他版本必须重走 binding 与 solver mode。

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

### OCS2 RaiSim 生成地形与平地位置误差增益冲突导致静止失稳

- `problem_id`：`problem.locomotion_contact_terrain.ocs2_raisim_terrain_position_gain_56`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OCS2 RaiSim 示例因平地位置误差假设与生成地形不一致而失稳**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：贡献者指出根因不是简化模型、关节 Kp/Kd 或缺少 WBC，而是 EE 的 ZeroVelocityConstraint.positionErrorGain 假设平地，与 generated terrain 冲突。平地使用者应设 generateTerrain=false；确实需要粗糙地形时应设 positionErrorGain=0.0。原作者复测后回复 Works like a charm，但没有说明具体选择哪一条。
- 证据状态：`issue_candidate`
- 来源定位：OCS2 #56：贡献者评论 1304459256 给出两种配置；原作者评论 1304836921 确认有效
- 原帖/精确回复：[OCS2 RaiSim 示例因平地位置误差假设与生成地形不一致而失稳](https://github.com/leggedrobotics/ocs2/issues/56#issuecomment-1304836921)
- 平台/作者：GitHub Issues / Kate88L
- 关键术语：零速度约束（ZeroVelocityConstraint）；位置误差增益（position error gain）；生成地形（generated terrain）；粗糙地形（rough terrain）
- 环境：OCS2 legged_robot_raisim 示例并启用 generated terrain；原帖未给 OCS2 commit、RaiSim 版本或机器人参数。
- 症状：仿真启动后机器人姿态立即改变，CoM 略向 x 移动，前腿接触力改变机身姿态并轻微振荡。；无 gait command、无 trajectory command，右后腿仍会逐渐浮起，随后计算崩溃。；第二位用户在同一线程报告相同问题。
- 诊断：检查是否同时开启 generateTerrain 且 ZeroVelocityConstraint 的 positionErrorGain 仍按平地假设工作。；在调整 Kp/Kd 或另写 WBC 前，先用线程给出的两种互斥配置验证地形假设。
- 原因：项目贡献者明确指出，EE ZeroVelocityConstraint 的 positionErrorGain 当前假设地形平坦，与 generated terrain 不一致。
- 处理过程：第二位复现者询问是否需要调整 joint Kp/Kd、RaiSim 参数或实现 WBC；贡献者明确回答这些都不是必要修复。；原作者按贡献者给出的配置方案修改后复测。
- 有效处理：若只需平地，把 raisim.info 中 generateTerrain 设为 false。；若需要粗糙地形，把 task.info 中 ZeroVelocityConstraint 的 positionErrorGain 设为 0.0。
- 结果：原作者回复 Works like a charm，并感谢快速答复。
- 限制：线程没有说明原作者最终采用两种方案中的哪一种，也没有公开修改后日志。；配置链接指向当时 main 分支行号；目标版本的文件位置和参数名需要重新核对。；positionErrorGain=0.0 是该粗糙地形示例的线程建议，不能直接推广为所有足端位置误差反馈都应关闭。
- 安全提示：实机或高保真仿真中修改接触位置反馈前，应限制力矩/速度并验证足端穿透、滑移和地形估计误差。
- 图片分析：原帖 PNG 已核验：RViz 画面中机器人呈现多个姿态重影，右后足有一处明显抬起，足端附近可见绿色力箭头；图中无时间、单位或配置值，只支持“静止状态姿态漂移/抬腿”的症状。；第二位用户的 GIF 已在两个时刻核验：彩色网格地形上机器人姿态发生明显变化并伴随重影；它支持独立用户遇到相似失稳，但不能从画面确定 positionErrorGain 数值。
- 独立核验引用：[issue · 第二位用户报告相同问题并提供复现 GIF](https://github.com/leggedrobotics/ocs2/issues/56#issuecomment-1302022974)；[maintainer_confirmation · 项目贡献者明确原因并给出 flat/rough terrain 两种配置](https://github.com/leggedrobotics/ocs2/issues/56#issuecomment-1304459256)；[source_code · 贡献者引用的 generateTerrain 配置位置](https://github.com/leggedrobotics/ocs2/blob/main/ocs2_raisim/ocs2_legged_robot_raisim/config/raisim.info#L11)；[source_code · 贡献者引用的 positionErrorGain 配置位置](https://github.com/leggedrobotics/ocs2/blob/main/ocs2_robotic_examples/ocs2_legged_robot/config/mpc/task.info#L12)；[issue · 原作者确认配置方案有效](https://github.com/leggedrobotics/ocs2/issues/56#issuecomment-1304836921)
- 适用边界：适用于线程所述 OCS2 legged_robot_raisim generated-terrain 配置；新版参数路径和真实地形估计方案需另行确认。

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

### MuJoCo 非方形 heightfield 的 rangefinder 索引错误

- `problem_id`：`problem.locomotion_contact_terrain.mujoco_nonsquare_hfield_raycast_2765`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo 3.3.4 非方形 hfield 的 rangefinder 错测由 raycast 索引修复**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：先保持 hfield 几何尺寸不变，用 64x32、32x64 与方形分辨率做 A/B；该线程对应的源码修复是提交 7b9f5bd。提交将 hfield 边缘数据的行跨度从 nrow 改为 ncol，并新增 4x3 非方形 hfield 回归测试。应升级到包含该提交的版本，并用自己的地图分辨率复测。
- 证据状态：`issue_candidate`
- 来源定位：MuJoCo #2765 评论 3151492060；修复提交 7b9f5bdae72480bdbc3b7fd4bef73e6a0925d96e
- 原帖/精确回复：[MuJoCo 3.3.4 非方形 hfield 的 rangefinder 错测由 raycast 索引修复](https://github.com/google-deepmind/mujoco/issues/2765#issuecomment-3151492060)
- 平台/作者：GitHub Issues / giorgionicola
- 关键术语：高度场（height field, hfield）；测距传感器（rangefinder）；射线检测（ray casting）；回归测试（regression test）
- 环境：MuJoCo 3.3.4；Python API；Ubuntu 24；hfield 64x32、32x64 与 32x32 对照。
- 症状：几何尺寸不变时，非方形分辨率的 rangefinder 会错误命中 hfield 边缘；方形 32x32 给出预期结果。
- 诊断：固定 hfield 几何尺寸，只交换 nrow/ncol 分辨率进行 A/B 对照。；运行原帖最小代码并检查不同分辨率的 rangefinder 读数。
- 原因：修复提交显示 hfield 边缘高度数据索引误用了 nrow，非方形时应按 ncol 做行跨度。
- 处理过程：作者提供可运行最小代码和三种分辨率对照；维护者合入源码修复与非方形回归测试。
- 有效处理：采用包含提交 7b9f5bdae72480bdbc3b7fd4bef73e6a0925d96e 的 MuJoCo 版本，或核对等价 mj_rayHfield 索引修复。
- 结果：维护者确认已修复；提交增加 4x3 hfield 的四个 rangefinder 期望值测试。
- 限制：原作者没有在评论中报告升级后复测；闭环依据是维护者确认、修复提交和回归测试。；不能将此修复外推到其他传感器或 mesh raycast。
- 安全提示：升级前后用目标地图分辨率回放感知测试，避免把错误地形距离直接用于实机落足。
- 独立核验引用：[source_code · Fixes #2765；修正 mj_rayHfield 非方形索引并加入 RayHfield 测试](https://github.com/google-deepmind/mujoco/commit/7b9f5bdae72480bdbc3b7fd4bef73e6a0925d96e)
- 适用边界：MuJoCo 3.3.4 的 hfield rangefinder/raycast 非方形分辨率问题；其他 raycast 类型需分别验证。

### MuJoCo rigid flex 凹碰撞的适用范围

- `problem_id`：`problem.locomotion_contact_terrain.mujoco_rigid_flex_concave_limits_3330`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo rigid flex 可做凹碰撞，但复杂穿透场景有性能与崩溃边界**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原作者确认 rigid=true 的 flexcomp 在简单模型中确实能产生凹碰撞；但复杂模型性能降到 40 FPS/5 FPS，穿透静态物体时出现大量接触、arena memory full 和 findEdges 错误。把 nconmax 提高到 30000 只消除了内存警告，findEdges 错误和 simulate.exe 退出仍存在。因此 rigid flex 可作为简化模型方案，但帖子没有证明它能替代复杂焊接工件的 Coal 集成。
- 证据状态：`issue_candidate`
- 来源定位：MuJoCo #3330 rigid flex 建议 4688939402；作者简单成功 4690882257；复杂限制 4704015555、4714020235、4714129335
- 原帖/精确回复：[MuJoCo rigid flex 可做凹碰撞，但复杂穿透场景有性能与崩溃边界](https://github.com/google-deepmind/mujoco/issues/3330#issuecomment-4714020235)
- 平台/作者：GitHub Issues / G-Yong
- 关键术语：刚性柔性体（rigid flex）；凹碰撞（concave collision）；接触竞技场内存（contact arena memory）；静态穿透（static penetration）
- 环境：2026-06 的 MuJoCo Issue；Windows simulate.exe 被评论提及；精确 MuJoCo 版本、CPU/GPU 和 mesh 规模未给。
- 症状：普通 convex hull 对空腔误报碰撞；简单 rigid flex 可用。；复杂 rigid flex 降至 40 FPS 或 5 FPS；穿透静态地面时 ncon=22287、arena memory full，随后 findEdges: no tree found 并退出。
- 诊断：先用简化 mesh 验证 rigid flex 的凹碰撞。；记录 ncon、arena memory、FPS，并单独测试静态穿透。；增大 nconmax 后区分内存警告是否消失，以及 findEdges 错误是否仍独立存在。
- 处理过程：使用 rigid=true 的 flexcomp 和 contact 配置。；把 size nconmax 提高到 30000。
- 有效处理：简单模型中 rigid flex 实现了作者需要的凹碰撞。
- 结果：提高 nconmax 只消除了 arena memory full 警告，没有消除 findEdges 错误和进程退出；复杂场景性能仍不足，作者继续依赖 Coal。
- 限制：rigid flex 不是该复杂焊接场景的完整替代方案。；线程没有维护者给出的 findEdges 修复或可用版本。；视频和截图未用于本卡结论，所有结果来自作者文字。
- 安全提示：将非凸碰撞用于运动规划前，应把穿透、接触数上限、实时因子和进程异常纳入自动回归，避免仿真崩溃中断安全检查。
- 独立核验引用：[issue · 作者给出复杂模型的接触数、错误文本和性能结果](https://github.com/google-deepmind/mujoco/issues/3330#issuecomment-4704015555)
- 适用边界：适用于评估复杂 mesh 的 rigid flex 凹碰撞；精确版本和模型规模未知，必须在目标模型复测。

### 核对 MJX plane-capsule fallback 的接触切向基

- `problem_id`：`problem.locomotion_contact_terrain.mjx_plane_capsule_tangent_fallback_2774`
- 问题综合等级：**需要实际验证** — 不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MJX plane-capsule 切向基 fallback 的数值差异仍待维护者确认**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突。
- 解答状态：`conflicting`
- 候选解答：目前不能。线程中的详细最小例子确实纠正了早期对 `normalize_with_norm` 返回值的理解，并展示了 fallback 可能生成非正交 frame、且差异集中在 pyramidal friction 的证据；但维护者只是重新打开 Issue 并表示将检查，尚未确认根因或合并修复。可把 frozen-state、contact frame、cone type 和 `qacc_warmstart=0` 的对比流程用于复现，不能把作者提议的 `math.orthogonals` 替换写成通用有效修复。
- 证据状态：`issue_candidate`
- 来源定位：MuJoCo #2774 详细纠正与复现实验 5082490175；维护者重新打开 5104526098
- 原帖/精确回复：[MJX plane-capsule 切向基 fallback 的数值差异仍待维护者确认](https://github.com/google-deepmind/mujoco/issues/2774#issuecomment-5082490175)
- 平台/作者：GitHub Issues / GJBoth
- 关键术语：接触坐标系（contact frame）；正交归一基（orthonormal basis）；金字塔摩擦锥（pyramidal friction cone）；预热加速度（qacc warm-start）
- 环境：详细跟进固定到 MuJoCo commit 6882095；一个 plane、一个 free capsule、一个显式 contact pair；CPU double 与 jitted MJX float64，同一 frozen state、fresh data、`qacc_warmstart=0`。
- 症状：跟进报告 `b_norm=0.4407495` 时 fallback 触发；给定 `n=\[0.3,0.4,0.8660254\]` 会选 `b=\[0,1,0\]`，从而 `n·b=0.4`。；同一 common-world point Jacobian 约差 `5.82e-18`，但 active contact tangent 不同；pyramidal friction 下 force 与 `qacc` 差异明显，`condim=1` 和 isotropic elliptic 基本一致。
- 诊断：冻结同一状态、清空 warmstart，分别比较 common-world Jacobian、contact frame、friction cone 类型、constraint force 与 `qacc`；不要只比较接触点位置。
- 原因：跟进作者指出 fallback 复用了 `math.orthogonals` 的轴选择，但缺少后续投影和重新归一化；维护者尚未正式确认该根因。
- 处理过程：作者提出在很小容差下使用 `math.orthogonals(n)\[0\]`，并报告替换选择后 parity 恢复；尚无维护者审核或合并补丁。
- 有效处理：当前没有可登记的正式修复；只能把该替换作为待验证实验，不应直接升级生产或训练基线。
- 结果：Issue 从关闭状态重新打开；维护者表示会检查，线程截至采集时没有进一步结论。
- 限制：现有数据来自一个最小 frozen-state 例子；尚未证明对所有 plane-capsule 姿态、cone 类型和 MuJoCo 版本都成立。
- 安全提示：若 WBC 依赖摩擦方向或接触力阈值，应在目标版本对 CPU/MJX 接触 frame 和 cone 配置做回归测试。
- 独立核验引用：[conflict · 维护者重新打开 Issue，表示将进一步检查；不是技术确认](https://github.com/google-deepmind/mujoco/issues/2774#issuecomment-5104526098)
- 适用边界：仅直接适用于 commit 6882095 和原帖最小 plane-capsule frozen-state 配置；其他版本与接触几何需复现。

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

### Isaac Lab Jacobian 的 link 索引与 body view 排序错位

- `problem_id`：`problem.optimization_ik_qp_mpc.isaaclab_jacobian_link_order_267`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 四足机器人 Jacobian 取错 link 的根因是 body view 与 articulation view 排序不同**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：先确认索引和数据来自同一个 PhysX 视图。原帖用 rigid body view 的 find_bodies 索引读取 root_physx_view.get_jacobians()，但当时 body view 与 articulation view 的 link 排序不同，所以整数 4 并不对应预期足端。维护者合并 e3c40acf，在 Orbit 0.14.0 中令 Articulation.body_names 遵循 PhysX articulation 顺序，并内部重排 body-view 数据。旧版本应按 root_physx_view.shared_metatype.link_names 取索引；新版本应使用统一后的 Articulation/root_physx_view 接口。
- 证据状态：`issue_candidate`
- 来源定位：Isaac Lab #267 评论 1992307071 的双视图顺序对照、评论 1994213116 的作者确认、评论 2000071829 与 commit e3c40acf 的正式修复
- 原帖/精确回复：[Isaac Lab 四足机器人 Jacobian 取错 link 的根因是 body view 与 articulation view 排序不同](https://github.com/isaac-sim/IsaacLab/issues/267#issuecomment-2000071829)
- 平台/作者：GitHub Issues / catachiii
- 关键术语：雅可比矩阵（Jacobian matrix）；刚体视图（Rigid Body View）；关节体视图（Articulation View）；连杆索引（link indexing）；有限差分（finite difference）
- 环境：Isaac Lab/Orbit main；Isaac Sim 2023.1.1；Ubuntu 22.04；RTX 4090；CUDA 12.3；Unitree Go2 与 ANYmal-C。
- 症状：提问者以 jacobian\[0, 4, 0:3, -12:\] 读取自认为是 FL_foot 的条目，矩阵除一列外几乎全零。；同一读取方式在 Go2 与 ANYmal-C 上都出现。
- 诊断：分别打印 body_physx_view.prim_paths 导出的 body 名顺序和 root_physx_view.shared_metatype.link_names，确认索引来源与 Jacobian 来源一致。；ANYmal 示例中 body view 按每条腿链排列，而 articulation view 先列四个 hip、再列 thigh、shank、foot；相同整数索引对应不同 link。
- 原因：find_bodies 使用 rigid body view 的 body_names 返回索引，而 Jacobian 来自 PhysX articulation view；两个视图当时的 link 排序不一致。
- 处理过程：作者按维护者提供的 articulation view link_names 重新解释索引，并确认原索引把数据取错。；维护者合并 commit e3c40acf，把 Articulation.body_names 改为 PhysX articulation 顺序，并在内部处理 articulation-link 到 body-view 的重排。
- 有效处理：旧版本中读取 root_physx_view 数据时必须使用 root_physx_view.shared_metatype.link_names 对应的索引。；升级到包含 e3c40acf 的 Orbit 0.14.0 或后续 Isaac Lab 版本，使用统一后的 Articulation.body_names/root_physx_view 接口，不再混用已弃用的 body_physx_view。
- 结果：作者确认 index messed things up；维护者发布修复提交并说明它覆盖 Jacobian、质量矩阵等 link 数据的索引一致性，Issue completed 关闭。
- 限制：该修复解决的是 link 排序一致性，不代表任意 Jacobian 数值异常都由索引导致。；不同 Isaac Lab 版本的公共属性名称已有变化，排查时应以当前版本 Articulation API 为准。
- 安全提示：WBC 上实机前应把每个 Jacobian 行块与 link 名做自动断言，并用有限差分或已知关节运动做方向检查，避免对错 link 下发控制。
- 独立核验引用：[issue · Go2/ANYmal-C 的最小读取方式、近零矩阵和完整环境](https://github.com/isaac-sim/IsaacLab/issues/267)；[maintainer_confirmation · 维护者列出 body view 与 articulation view 的两套实际 link 顺序](https://github.com/isaac-sim/IsaacLab/issues/267#issuecomment-1992307071)；[source_code · Orbit 0.14.0：统一 Articulation.body_names 排序并内部重排 body-view 数据](https://github.com/isaac-sim/IsaacLab/commit/e3c40acf5e6433c1d88b54a6e9d45bd6d3e73152)
- 适用边界：直接适用于 Isaac Sim 2023.1.1/旧 Orbit 的 Go2 与 ANYmal-C；后续版本仍应确认当前 API 返回顺序后再复用索引。

### Isaac Lab 旋转基座下 IK 的 Jacobian 坐标系不一致

- `problem_id`：`problem.optimization_ik_qp_mpc.isaaclab_rotated_base_ik_frame_911`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 绝对 IK 在旋转基座下漂移是 Jacobian 坐标系未转换**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：先把目标、误差和 Jacobian 的参考坐标系统一。旧 DifferentialInverseKinematicsAction 直接使用 world-frame 几何 Jacobian，却按 root/base-frame 目标求解；作者用基座逆旋转矩阵分别左乘 Jacobian 的线速度和角速度块后，在旋转基座上恢复稳定控制。已合并的 PR #967 将该转换放入 action，并区分 world-frame 与 base-frame Jacobian。绝对目标若来自 world frame，也必须由调用侧或 action 按同一约定转换。
- 证据状态：`issue_candidate`
- 来源定位：Isaac Lab #911 评论 2333206262/2333999077 的修补与形状说明，评论 2523695195 指向已合并 PR #967
- 原帖/精确回复：[Isaac Lab 绝对 IK 在旋转基座下漂移是 Jacobian 坐标系未转换](https://github.com/isaac-sim/IsaacLab/issues/911#issuecomment-2523695195)
- 平台/作者：GitHub Issues / zoctipus
- 关键术语：几何雅可比（geometric Jacobian）；基座坐标系（base frame）；世界坐标系（world frame）；批量矩阵乘法（batched matrix multiplication）；微分逆运动学（Differential Inverse Kinematics, Differential IK）
- 环境：Isaac Lab commit 7452386；Isaac Sim 4.1；Ubuntu 20.04；RTX 4090；CUDA 12.5；Franka IK-Abs 任务。
- 症状：同一常量 base-frame 目标在默认基座下稳定，在基座旋转 90 度后末端持续偏离目标。；初始时位置误差和姿态误差接近零，但控制过程仍漂移。
- 诊断：同时标注 action target、当前末端姿态与 Jacobian 的 frame，不要仅看误差向量初值。；维护者澄清 PhysX Jacobian 本身可合法地位于 world frame；问题在于 DifferentialInverseKinematicsAction 需要与 root/base-frame 目标保持一致。；quat_apply 只接受 N×3 向量，而 Jacobian 块是 N×3×n_Dof；线程中确认应使用 matrix_from_quat 与 torch.bmm。
- 原因：旧实现没有读取 root/base 姿态来转换几何 Jacobian，导致旋转基座时 Jacobian 与目标/误差所在 frame 不一致。
- 处理过程：作者用 inverse(base_quat) 生成 3×3 旋转矩阵，对 Jacobian 的线速度三行和角速度三行分别做批量矩阵乘法，并在旋转 90 度基座上演示稳定遥操作。；贡献者进一步讨论绝对目标若在 world frame 给出，还需先转换为 base frame；线程明确这是接口设计选择，调用侧必须保持约定一致。
- 有效处理：使用包含 PR #967 的版本；该 PR 在 DifferentialInverseKinematicsAction 内把 Jacobian 转到 root frame，并区分 world-frame 与 base-frame Jacobian 属性。；旧版本手工修补时，用基座逆旋转矩阵分别左乘 Jacobian 的线速度块与角速度块，且把绝对目标转换到同一 base/root frame。
- 结果：作者在旋转 90 度的 Franka 基座上展示修补后可稳定遥操作；PR #967 已合并，merge commit 为 762f4e32，Issue completed 关闭。
- 限制：world-frame Jacobian 不是天然错误；只有在控制器误差与命令使用 root/base frame 时才必须转换。；PR #967 描述中的测试 checklist 未勾选新增测试，部署到其他机器人仍应做旋转基座回归测试。
- 安全提示：实机移动操作前至少用两个非零 base 朝向验证同一末端目标，并记录 frame 名；零朝向测试不能暴露此类坐标系错误。
- 独立核验引用：[issue · 旋转/未旋转基座对照、完整复现脚本与环境](https://github.com/isaac-sim/IsaacLab/issues/911)；[maintainer_confirmation · 协作者确认 Jacobian 是 N×3×n_Dof，matrix_from_quat + torch.bmm 路径有效，并澄清 world/root frame 语义](https://github.com/isaac-sim/IsaacLab/issues/911#issuecomment-2333999077)；[pull_request · 2024-12-12 合并；Computes Jacobian in the root frame；Fixes #911](https://github.com/isaac-sim/IsaacLab/pull/967)
- 适用边界：直接适用于 Isaac Lab commit 7452386/Isaac Sim 4.1 的 Franka IK-Abs；其他版本与机器人应核对 action API 当前声明的 frame。

### Pinocchio frame Jacobian 输出矩阵少三行导致结果看似全零

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_frame_jacobian_output_shape_2683`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 3.5 的 computeFrameJacobian 不再替调用方修正 3×nv 输出矩阵**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：先检查调用方输出矩阵。Frame Jacobian 同时包含线速度与角速度，契约是 6×model.nv；原作者只传了 3×nv，非零项恰在第 5、6 行，而 3.5.0 不再替调用方 resize。应在调用前创建并清零 6×nv 矩阵。已合并的 PR #2684 又为 frame/joint Jacobian 增加 6 行和 nv 列的参数检查。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #2683：作者评论 2905781523 定位 3×nv；维护者评论 2906540315 确认 6×nv；PR #2684 合并提交 8af6014
- 原帖/精确回复：[Pinocchio 3.5 的 computeFrameJacobian 不再替调用方修正 3×nv 输出矩阵](https://github.com/stack-of-tasks/pinocchio/issues/2683#issuecomment-2905781523)
- 平台/作者：GitHub Issues / scastro-bdai
- 关键术语：帧雅可比矩阵（frame Jacobian）；空间速度（spatial velocity）；输出矩阵尺寸（output matrix shape）；参数检查（argument-size check）
- 环境：Ubuntu 22.04；Pinocchio 3.4.0 与 3.5.0 对照；C++ Eigen 动态矩阵；原帖提供 URDF 与 Python 复现仓库。
- 症状：C++ 3.5.0 输出全零，3.4.0 与 Python 输出在最后两行存在非零项。；调用结束后的 Jacobian 仍只有 3 行，而 frame Jacobian 的空间维度应为 6。
- 诊断：在调用前打印输出矩阵形状，确认是 6×model.nv，而不是只含线速度的 3×model.nv。；将输出矩阵预置为 6×nv 的零矩阵，再比较 Python/C++ 和版本差异；不要先把问题归因于参考系或算法回归。
- 原因：调用方传入了 3×nv 矩阵；3.4.0 曾隐式 resize，3.5.0 不再这样做，非零角速度行因此没有被写入。
- 处理过程：原作者把问题写成版本回归并对照 Python/C++ 后，重新检查输出尺寸，定位到 3 行预分配。
- 有效处理：始终传入已清零的 6×model.nv 输出矩阵。；PR #2684 在 frame/joint Jacobian 路径加入 J.rows()==6 与 J.cols()==model.nv 的参数检查，使错误尺寸不再静默通过。
- 结果：维护者确认 6×nv 是所有 frame/joint Jacobian 的契约；PR #2684 于 2025-05-26 合并，Issue 以 completed 关闭。
- 限制：该根因只解释输出矩阵尺寸错误；若 6×nv 仍异常，仍需继续核对 frame id、配置 q 和 reference frame。；原帖没有给出把 C++ 矩阵改成 6×nv 后的新数值截图，但作者已明确定位，维护者补丁直接检查同一条件。
- 安全提示：将 Jacobian 维度作为控制启动前断言，避免错误任务空间约束进入实机 QP。
- 独立核验引用：[issue · Python/C++、3.4/3.5 对照，frame、q、输出矩阵与系统环境](https://github.com/stack-of-tasks/pinocchio/issues/2683)；[maintainer_confirmation · 维护者确认所有 frame/joint Jacobian 均须由调用方提供 6×nv 矩阵](https://github.com/stack-of-tasks/pinocchio/issues/2683#issuecomment-2906540315)；[pull_request · 2025-05-26 合并；对 J/dJ 增加 6 行与 model.nv 列检查](https://github.com/stack-of-tasks/pinocchio/pull/2684)；[source_code · PR #2684 merge commit：frames.hxx 与 jacobian.hxx 参数尺寸检查](https://github.com/stack-of-tasks/pinocchio/commit/8af6014f6143022f4645e49fbefce2eb0418a225)
- 适用边界：直接覆盖 Ubuntu 22.04、Pinocchio 3.4/3.5 C++ 调用；其他版本也应遵守 6×nv 的 frame/joint Jacobian 输出契约。

### Pinocchio 固定世界方向外力的 Jacobian 参考系选择

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_fixed_world_force_lwa_1761`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 将固定世界方向的末端力映射到关节力矩时使用 LOCAL_WORLD_ALIGNED Jacobian**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：在作者明确这一目标后，维护者回答使用 LOCAL_WORLD_ALIGNED。线程同时澄清 universe/inertial frame 固定，而 world-aligned coincident point 可随目标 frame 移动。由于作者没有发布 torque 结果或复测，该结论只能作为 reference-frame 选择入口；wrench 排列、作用点、符号和 Jacobian 转置映射仍需在目标模型实际验证。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1761：维护者评论 1264712803 澄清 fixed universe/coincident point；1266647907 回答使用 LOCAL_WORLD_ALIGNED
- 原帖/精确回复：[Pinocchio 将固定世界方向的末端力映射到关节力矩时使用 LOCAL_WORLD_ALIGNED Jacobian](https://github.com/stack-of-tasks/pinocchio/issues/1761#issuecomment-1266647907)
- 平台/作者：GitHub Issues / huihuishen
- 关键术语：局部世界对齐坐标系（LOCAL_WORLD_ALIGNED）；参考坐标系（ReferenceFrame）；末端雅可比矩阵（end-effector Jacobian）；外力到关节力矩映射（force-to-torque mapping）
- 环境：Pinocchio RobotWrapper.BuildFromURDF(..., JointModelFreeFlyer())；末端 frame；原帖未给 Pinocchio 版本和 URDF。
- 症状：作者误以为 WORLD frame 随机器人整体移动，因此无法确定固定世界方向外力应与哪种 Jacobian 配对。
- 诊断：明确外力的坐标轴方向和作用点，再选择 Jacobian reference frame。；区分固定 universe/inertial frame 与位于移动 body/frame 原点的 world-aligned 表达。
- 原因：把 WORLD convention 中随 body 移动的 coincident point 误解为 universe 坐标轴本身移动。
- 处理过程：作者多次澄清目标，最终明确要把固定 frame 描述的 force 转成 torque。
- 有效处理：维护者针对该目标回答使用 LOCAL_WORLD_ALIGNED frame Jacobian。
- 结果：Issue 已关闭，但没有作者的数值结果、代码或修复后确认。
- 限制：线程没有验证 Jacobian 转置公式、力/力矩六维排列、符号或作用点，因此不能从该回答单独保证 torque 数值正确。；没有版本与复现结果，必须在目标模型上用虚功或有限差分等方法另行核对。
- 安全提示：实机施力前必须独立验证 wrench 顺序、frame transform、关节顺序和力矩限幅。
- 独立核验引用：[maintainer_confirmation · 维护者澄清 universe 固定，但 coincident point 随 body 移动](https://github.com/stack-of-tasks/pinocchio/issues/1761#issuecomment-1264712803)；[maintainer_confirmation · 维护者针对固定 frame 外力到 torque 的目标回答使用 LOCAL_WORLD_ALIGNED](https://github.com/stack-of-tasks/pinocchio/issues/1761#issuecomment-1266647907)
- 适用边界：适用于原帖“固定世界方向外力、末端 frame、浮动基机器人”的目标；未验证具体 torque 映射实现。

### Pinocchio 无接触前向动力学误调用 constrained forwardDynamics

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_unconstrained_forward_dynamics_aba_2604`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 无接触前向动力学应调用 aba，forwardDynamics 是约束动力学重载**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：先检查调用的算法语义和 Python overload。原帖是无接触前向动力学，应使用 aba(model,data,q,v,tau)；forwardDynamics 面向带接触/约束的动力学重载，需要 constraint_jacobian 和 constraint_drift。原作者的五参数调用匹配了另一重载，导致 q 被解释成应为 nv 长度的 tau，于是出现 got nq=15 的迷惑报错。原作者改用建议后确认解决。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #2604：贡献者评论 2694376878 解释 aba 与 forwardDynamics overload；原作者 2696551706 确认解决
- 原帖/精确回复：[Pinocchio 无接触前向动力学应调用 aba，forwardDynamics 是约束动力学重载](https://github.com/stack-of-tasks/pinocchio/issues/2604#issuecomment-2694376878)
- 平台/作者：GitHub Issues / qiyuanchn
- 关键术语：关节空间惯量算法（Articulated-Body Algorithm, ABA）；前向动力学（forward dynamics）；约束动力学（constrained dynamics）；函数重载（function overload）
- 环境：Pinocchio Python；iris.urdf；JointModelFreeFlyer；model.nq=15、model.nv=10；无 contacts。
- 症状：调用 pin.forwardDynamics(model,data,q,v,tau) 报 ValueError: wrong argument size: expected 10, got 15，尽管 tau 长度为 10。
- 诊断：使用 help(pinocchio.forwardDynamics) 检查 Python overload 的参数列表。；先判断问题是无接触前向动力学，还是带 constraint_jacobian/constraint_drift 的 contact/constrained dynamics。
- 原因：五参数调用匹配了 constrained forwardDynamics 的另一重载，q 被当成只应为 nv 长度的 tau，因此错误信息显示 got nq=15。
- 处理过程：维护者要求完整 URDF 后，与另一位项目成员复核了模型和 API overload。
- 有效处理：无接触场景改用 pin.aba(model, data, q, v, tau)；需要接触约束时才按 forwardDynamics 文档提供 constraint_jacobian 与 constraint_drift。
- 结果：原作者回复问题已解决。
- 限制：该结论只覆盖原帖无接触场景；存在闭链、刚性接触或其他约束时不能直接丢弃 constraint inputs。；原帖没有给 Pinocchio 版本和最终加速度数值，只确认 API 选择解决尺寸错误。
- 安全提示：实机控制前需确认动力学模型、外力/接触约束与执行器输入定义，不能仅以函数成功返回作为动力学正确性证明。
- 独立核验引用：[maintainer_confirmation · 项目贡献者说明无接触 forward dynamics 应使用 aba，并列出 constrained forwardDynamics overload](https://github.com/stack-of-tasks/pinocchio/issues/2604#issuecomment-2694376878)；[issue · 原作者确认问题解决](https://github.com/stack-of-tasks/pinocchio/issues/2604#issuecomment-2696551706)；[source_code · 维护者在原回复中给出的固定提交 aba 无接触仿真示例](https://github.com/stack-of-tasks/pinocchio/blob/187afafcfe22d7ac16a26241c0b13a76d04d82c1/examples/simulation-inverted-pendulum.py#L97)
- 适用边界：适用于无 contact/constraint 的 Pinocchio FreeFlyer forward dynamics；带约束问题必须使用对应 constrained API。

### Pinocchio 4 获取 frame Jacobian 对 q 的 6×nv×nv Hessian

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_frame_kinematic_hessian_2844`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 4 已提供 frame Jacobian 对关节配置的完整 Hessian 接口**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`resolved`
- 候选解答：Pinocchio 4 已提供 getFrameKinematicHessian。先运行 computeJointKinematicHessians 填充 data，再用 frame_id 和 reference frame 调用 getFrameKinematicHessian；官方头文件的返回值 overload 创建 6×nv×nv tensor，无动态分配 overload 则要求调用方预先清零同尺寸 tensor。原线程没有用户数值复测，因此仍应在目标版本做有限差分校验。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #2844：维护者评论 3846183967 说明 Pinocchio 4 已实现，评论 5103983954 指向源码；固定源码 commit 031ebb1 行 527-539、655-665
- 原帖/精确回复：[Pinocchio 4 已提供 frame Jacobian 对关节配置的完整 Hessian 接口](https://github.com/stack-of-tasks/pinocchio/issues/2844#issuecomment-5103983954)
- 平台/作者：GitHub Issues / Decembereye
- 关键术语：运动学 Hessian（kinematic Hessian）；帧雅可比导数（frame Jacobian derivative）；参考坐标系（reference frame）；三阶张量（third-order tensor）
- 环境：原帖指向 Pinocchio 4；本轮源码核验固定在 devel commit 031ebb13a637babd0705ce030ce9fb2e1e9aae2c。
- 症状：旧用法能调用 getJointKinematicHessian，却找不到对 frame_id 等价的 getFrameKinematicHessian。
- 诊断：先区分需要完整 6×nv×nv dJ/dq，还是只需要 Hessian-vector/wrench contraction；两者最合适的算法不同。；在目标安装版本的 kinematics-derivatives.hpp 中确认 getFrameKinematicHessian overload 与 binding 可用性。
- 原因：该能力在早期 Pinocchio 没有公开 frame 接口，而 Pinocchio 4 才补齐。
- 处理过程：原帖引用旧 #867 中通过 joint Hessian 或重复 time-variation 调用构造结果的历史讨论。
- 有效处理：在 Pinocchio 4 先调用 computeJointKinematicHessians，再调用 getFrameKinematicHessian(model, data, frame_id, reference_frame, tensor)，或使用返回 tensor 的 overload。；无动态分配的 overload 要求调用方先把 6×nv×nv tensor 清零；返回值 overload 会创建同尺寸 tensor。
- 结果：维护者在 2026-07-28 指向已实现的官方函数，Issue 以 completed 关闭；固定 commit 的头文件包含 frame_id overload。
- 限制：原线程没有调用者复测、数值有限差分对照或 Python binding 示例，因此在目标构建上仍应核对可用 overload。；接口返回的是 frame kinematic Hessian；具体 reference frame 与张量索引约定应按同版本文档和有限差分验证。
- 安全提示：二阶导数进入优化器前，应在小扰动下做有限差分方向导数检查，避免张量轴或 reference frame 误用。
- 独立核验引用：[maintainer_confirmation · 维护者说明 frame kinematic Hessian 已在 Pinocchio 4 实现](https://github.com/stack-of-tasks/pinocchio/issues/2844#issuecomment-3846183967)；[source_code · 固定 commit 的 frame_id + output tensor overload，并转发 parentJoint/frame.placement](https://github.com/stack-of-tasks/pinocchio/blob/031ebb13a637babd0705ce030ce9fb2e1e9aae2c/include/pinocchio/algorithm/kinematics-derivatives.hpp#L527-L539)；[source_code · 返回值 overload 创建 6×nv×nv tensor、清零并调用填充版本](https://github.com/stack-of-tasks/pinocchio/blob/031ebb13a637babd0705ce030ce9fb2e1e9aae2c/include/pinocchio/algorithm/kinematics-derivatives.hpp#L655-L665)
- 适用边界：适用于包含 getFrameKinematicHessian 的 Pinocchio 4 C++ 构建；具体 Python 暴露和最低发布版本需在目标环境核验。

### 接触 QP 用 RNEA derivatives 直接计算 Hessian-wrench contraction

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_contact_hessian_wrench_rnea_867`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：接触 QP 只需要 dJᵀ/dq·λ 时可用 Pinocchio RNEA derivatives 避免构造完整 Hessian**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：先确认目标是沿空间 wrench λ 收缩后的 nv×nv 矩阵，而不是完整 dJ/dq。原线程指出，RNEA 的 external-force 项包含 J^Tλ，因此可用 RNEA analytical derivatives 直接求 d(J^Tλ)/dq。Valkyrie nv=32 的原作者确认该方法可用，并报告原始 derivative 调用约 0.035 ms；这些时序只代表其旧环境，不应外推。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #867：评论 526278645 写出 contraction 与 RNEA 关系；评论 530373296 确认可用并给出对照；评论 530407733 补充 raw 调用时序
- 原帖/精确回复：[接触 QP 只需要 dJᵀ/dq·λ 时可用 Pinocchio RNEA derivatives 避免构造完整 Hessian](https://github.com/stack-of-tasks/pinocchio/issues/867#issuecomment-530373296)
- 平台/作者：GitHub Issues / Leph
- 关键术语：递归牛顿-欧拉算法导数（Recursive Newton-Euler Algorithm derivatives, RNEA derivatives）；外部力（external force）；张量收缩（tensor contraction）；有限差分（finite difference）
- 环境：2019 年 Pinocchio/RBDL 对照；Valkyrie humanoid，nv=32；作者仅说明标准 laptop，未给 CPU 与精确 Pinocchio 版本。
- 症状：有限差分完整 Hessian 阻碍约 1 ms 的计算预算；实际目标是对 Hessian 第一维与 contact wrench λ 收缩后得到 nv×nv 矩阵。
- 诊断：先把优化中的真实表达式写成 J(q+dq)^T λ，确认需要的是 d(J^T λ)/dq，而非完整 dJ/dq。；区分张量最后一维的 Hessian-vector product 与原帖沿空间 wrench 维度收缩的 nv×nv 结果。
- 原因：直接构造完整 Hessian 计算了优化器不会使用的大量元素；RNEA 外力项已经包含 J^T λ，其解析导数可直接给出所需收缩。
- 处理过程：作者先用 RBDL 有限差分，并讨论过完整 tensor API 与 nv 次 time-variation 调用。；随后把零重力、零速度/加速度和外力项的 RNEA 导数用于 dJ^T/dq·λ。
- 有效处理：若目标确实是 d(J^T λ)/dq，使用带 external forces 的 RNEA analytical derivatives 直接计算，而不是先构造完整 frame Hessian。
- 结果：作者明确确认 RNEA derivatives 能取得所需 Hessian-wrench product，并报告其本机 Valkyrie 对照时序。
- 限制：0.500/0.060/0.035 ms 是单一作者、旧版本和未注明 CPU 的线程记录，不能作为当前硬件通用 benchmark。；维护者推测标准 laptop 可到 0.015 ms，但作者没有验证该数值，本卡不把它作为结果。；若优化确实需要完整 dJ/dq，应改用 Pinocchio 4 的 frame kinematic Hessian 接口，而不是此 contraction。
- 安全提示：把解析 contraction 与有限差分在随机 q、λ 上做方向导数对照后，再放入实时接触 QP。
- 独立核验引用：[issue · 作者写出 M(i,j)=Σk H(k,i,j)λ(k)，并识别 RNEA derivatives 路径](https://github.com/stack-of-tasks/pinocchio/issues/867#issuecomment-526278645)；[issue · 作者确认带 external forces 的 RNEA derivative 可取得所需 product，并报告对照时序](https://github.com/stack-of-tasks/pinocchio/issues/867#issuecomment-530373296)；[issue · 作者说明 0.060 ms 含 Pinocchio/RBDL 转换，raw RNEA derivatives 约 0.035 ms](https://github.com/stack-of-tasks/pinocchio/issues/867#issuecomment-530407733)
- 适用边界：适用于接触 QP 中 d(J^Tλ)/dq 这一特定 contraction；原帖为 Valkyrie nv=32 和 2019 年 API，当前签名需按目标 Pinocchio 版本核对。

### Crocoddyl TALOS 状态边界代价在初始求解时产生 NaN

- `problem_id`：`problem.optimization_ik_qp_mpc.crocoddyl_talos_state_bounds_nan_1395`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Crocoddyl TALOS whole-body manipulation 的状态边界代价导致 NaN**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：原作者把 NaN 定位到 xBounds 代价中的 ResidualModelState(state, 0*x0, actuation.nu)。维护者的 PR #1403 把它改为 ResidualModelState(state, actuation.nu)，PR 正文明确写明修复 #1395，随后合入 devel 并关闭 Issue。应优先使用包含该 PR 的 notebook；线程没有给出原作者合并后复跑日志，因此不能扩展为所有 Crocoddyl NaN 的通用结论。
- 证据状态：`issue_candidate`
- 来源定位：Crocoddyl #1395：协作者评论 2922474130 复现；原作者评论 2931328830 定位 xBounds；维护者评论 2936325526 指向 PR #1403；合并提交 8e3c143
- 原帖/精确回复：[Crocoddyl TALOS whole-body manipulation 的状态边界代价导致 NaN](https://github.com/loco-3d/crocoddyl/issues/1395#issuecomment-2936325526)
- 平台/作者：GitHub Issues / pran-d
- 关键术语：状态边界惩罚（state limits penalization）；残差模型（residual model）；二次障碍激活（quadratic barrier activation）；全身操作（whole-body manipulation）
- 环境：Ubuntu 24.04.2、Python 3.12.3、Crocoddyl 3.0.1；原作者降级到 Crocoddyl 2.2.0 后仍复现；未给 example_robot_data 版本。
- 症状：whole_body_manipulation.ipynb 不改动运行时 cost 显示 NaN，solver 在第 0 次迭代退出。；移除 differential model 的 contacts 后问题仍在；相同环境和 cost formulation 换 Panda 模型可以求解并到达目标。
- 诊断：先用同一虚拟环境替换机器人模型，区分通用求解器故障与特定多体状态维度/边界故障。；逐项移除或检查 cost；原作者把 NaN 定位到 xBounds 中 ActivationBounds 与 ResidualModelState 的组合。；核对 StateMultibody 的 nq、nv、状态切空间维度以及 residual 期望维度，不要仅按 nq+nv 猜测。
- 原因：原线程把直接原因定位到状态边界惩罚中 ResidualModelState(state, 0*x0, actuation.nu) 的参考状态构造；维护者修复补丁移除了该错误参考参数。
- 处理过程：原作者尝试移除 contacts，问题仍存在。；原作者把 TALOS 换成 Panda 后求解正常，并在 Crocoddyl 3.0.1/2.2.0 间交叉复现。；协作者使用 PR #1396 提供的 Jupyter 入口复现了错误行为。
- 有效处理：采用已合入 PR #1403 的 notebook，或把 xBounds residual 从 ResidualModelState(state, 0*x0, actuation.nu) 改为 ResidualModelState(state, actuation.nu)。
- 结果：PR #1403 明确声明修复 #1395，于 2025-06-04 合入 loco-3d/crocoddyl:devel；Issue 状态为 completed。
- 限制：原作者没有在合并后再次留言确认运行结果；闭环依据是协作者复现、维护者指向修复、PR 明确关联并合入以及 Issue 关闭。；PR #1403 还修改了 contact stabilization、notebook 结构和 README；本卡只把原作者已定位且补丁直接改动的 xBounds residual 作为该 NaN 的线程内修复。；不能从该线程推导任意 StateMultibody 的通用边界切片公式。
- 安全提示：在把优化结果用于实机前，先把初始 cost、residual 维度和有限值检查作为启动门槛；NaN 状态下不得下发控制量。
- 独立核验引用：[independent_reproduction · 项目协作者说明使用 #1396 可以复现该错误行为](https://github.com/loco-3d/crocoddyl/issues/1395#issuecomment-2922474130)；[issue · 原作者给出 xBounds 代码并把 NaN 定位到状态边界代价](https://github.com/loco-3d/crocoddyl/issues/1395#issuecomment-2931328830)；[pull_request · PR 正文明确 Fixes #1395，2025-06-04 合入 devel](https://github.com/loco-3d/crocoddyl/pull/1403)；[source_code · 固定提交把 xBounds 的 ResidualModelState(state, 0*x0, ...) 改为不传错误参考状态的构造](https://github.com/loco-3d/crocoddyl/commit/d2ab9a5510094fb52c5f8212fbbb25d749f56d66)
- 适用边界：适用于旧版 whole_body_manipulation.ipynb 的 TALOS 状态边界代价构造；目标安装必须确认是否已包含 PR #1403。

### Pinocchio 旧 IK 示例的位姿残差与 Jacobian 参考坐标系不一致

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_ik_error_jacobian_frame_mismatch_1959`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 旧 IK 示例把目标坐标系残差与局部 Jacobian 混用**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：原线程确认的错误是：log6(dMi) 残差表达在目标坐标系 d，而 computeFrameJacobian 的 Jacobian 表达在当前末端/关节坐标系 i。已合入 PR #1963 把残差改为 iMd=data.oMi\[JOINT_ID\].actInv(oMdes)，使误差位于当前局部坐标系，并用 Jlog6(iMd.inverse()) 对几何 Jacobian 做位姿任务链式修正。修订后的官方 C++/Python 示例均给出收敛日志。减小 dt 单独没有解决原用户问题；原用户也没有证明自己的 GEN3 Lite 关节限位问题已解决。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1959 评论 1543725756 定位 frame mismatch；评论 1543910510 否定仅减小 dt；评论 1543936952/1546547369 指向修复；PR #1963 已审阅、合并并附收敛日志
- 原帖/精确回复：[Pinocchio 旧 IK 示例把目标坐标系残差与局部 Jacobian 混用](https://github.com/stack-of-tasks/pinocchio/issues/1959#issuecomment-1543725756)
- 平台/作者：GitHub Issues / DawnQiu
- 关键术语：逆运动学（inverse kinematics, IK）；位姿残差（pose residual）；几何雅可比矩阵（geometric Jacobian）；局部坐标系（local frame）；三维特殊欧氏群（special Euclidean group, SE3）
- 环境：Pinocchio C++、用户自有 GEN3Lite.urdf；原帖未给 OS、Pinocchio 版本或 commit。关联 PR #1963 修改官方 C++/Python inverse-kinematics 示例并合入 devel。
- 症状：原用户运行 1000 次迭代仍未达到 1e-4 误差阈值，最终配置包含约 39.27 和 -39.18 rad 的关节值。；原用户明确回复，减小 dt 后仍未达到预期结果。
- 诊断：逐项标注 log6 残差和 computeFrameJacobian 输出所处的 frame，确认两者一致后再调阻尼或步长。；对 SE(3) 位姿任务 Jacobian 核对 Jlog6 链式修正；不要只把几何 Jacobian 直接与 log6 残差组合。
- 原因：贡献者指出，原代码的 log6(dMi) 残差表达在目标 frame d，而 computeFrameJacobian 的 Jacobian 表达在当前 body/frame i；两者坐标系不一致。
- 处理过程：原用户增加迭代次数并调整时间步长，均未解决自己的机械臂结果。；PR #1963 在官方 C++/Python 示例中把残差与 Jacobian 统一到当前关节局部坐标系，并加入 Jlog6 修正。
- 有效处理：按已合入 PR #1963 的方式，以 iMd=data.oMi\[JOINT_ID\].actInv(oMdes) 计算局部残差，并用 Jlog6(iMd.inverse()) 修正任务 Jacobian；Python 示例使用 np.dot 保持 Python 2.7/ROS Melodic 兼容。
- 结果：PR #1963 的 C++ 与 Python 示例日志均显示 Convergence achieved，PR 经项目维护者审阅批准并合入 devel。
- 限制：原用户没有在 GEN3 Lite 模型上发布采用 PR #1963 后的复测结果；本卡确认的是官方示例的 frame/Jlog6 修复，不宣称用户机器人的所有不收敛都已解决。；PR #1963 没有加入关节限位约束；原帖中超出物理限位的现象需要另行使用受约束 IK 或限位处理，不能由本线程推导已经解决。；目标可达性、奇异位形、阻尼和步长仍需针对目标机器人验证。
- 安全提示：把 IK 结果用于实机前必须检查关节位置、速度和碰撞约束；即使数值收敛也不能直接下发越界配置。
- 独立核验引用：[issue · 原用户说明减小 dt 后仍未达到预期，排除把步长单独写成已验证修复](https://github.com/stack-of-tasks/pinocchio/issues/1959#issuecomment-1543910510)；[pull_request · 已合入 PR 把残差统一到当前局部 frame、加入 Jlog6，并附 C++/Python 收敛日志](https://github.com/stack-of-tasks/pinocchio/pull/1963)；[source_code · PR #1963 的合并提交，固定官方 IK 示例修改](https://github.com/stack-of-tasks/pinocchio/commit/4b28322642096f2e7521e978ba535e94de0667b0)
- 适用边界：适用于使用 Pinocchio log6 位姿残差和局部几何 Jacobian 的迭代 IK，尤其是基于旧官方示例的实现；目标机器人仍需单独处理可达性和关节限位。

### Pinocchio 含外力静力矩二阶导数的接口缺口

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_static_torque_second_order_external_force_2092`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 当时没有带外力静力矩二阶导数的现成接口**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：截至原线程时间，项目方明确说二阶导支持尚不完整，没有可直接使用的含 external forces 静力矩二阶导接口；专门利用静态结构可以减少计算，但需要进一步研究和工程实现。原作者最后只表示可能用 CppADCodeGen 自动微分，并未发布实现或结果，所以它只能作为待验证的备选路线。目标版本若更新，必须重新核对 API，不能永久沿用 2023 年结论。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #2092 评论 1822471230 说明二阶导支持不完整；评论 1824887277 说明可实现但需工程投入；评论 1831924121 原作者仅计划 CppADCodeGen
- 原帖/精确回复：[Pinocchio 当时没有带外力静力矩二阶导数的现成接口](https://github.com/stack-of-tasks/pinocchio/issues/2092#issuecomment-1822471230)
- 平台/作者：GitHub Issues / IoannisDadiotis
- 关键术语：广义静力矩（generalized static torque）；二阶导数（second-order derivative）；外力（external force）；逆动力学递归牛顿-欧拉算法（Recursive Newton-Euler Algorithm, RNEA）；自动微分（automatic differentiation, AD）
- 环境：2023-11 的 Pinocchio 公开接口；原帖未给版本、commit、OS、机器人或矩阵规模。
- 症状：computeStaticTorque/computeStaticTorqueDerivatives 没有二阶接口，而 ComputeRNEASecondOrderDerivatives 不接收 external forces。；原作者用 std::chrono 粗测一阶接口时，零速度/零加速度的 ComputeRNEADerivatives 比 computeStaticTorqueDerivatives 慢约 2–3 倍，但未给硬件、重复次数或绝对时延。
- 诊断：先核对目标 Pinocchio 版本的二阶导 API 是否支持 external forces，不要仅凭函数名假定覆盖静力矩场景。；若考虑通用 RNEA 二阶导替代静态专用导数，应单独基准不需要的速度/加速度导数开销。
- 原因：项目贡献者明确表示当时 Pinocchio 的二阶导支持不完整；含外力静力矩的专用二阶导需要研究和工程实现。
- 处理过程：原作者考虑分别求 gravity 与 J(q)^T fext 的二阶导，或把速度和加速度置零后调用 RNEA 二阶导。；原作者最后表示对自己的应用可能使用 CppADCodeGen 自动微分。
- 结果：线程确认当时没有现成的含外力静力矩二阶导路径；维护者邀请协作实现，原作者没有投入底层开发并转向考虑自动微分。
- 限制：CppADCodeGen 只是原作者计划，没有代码、数值正确性、编译时间或运行时结果，不能写成已验证替代方案。；原作者的 2–3 倍时序缺少硬件、版本和统计方法，不能外推为性能结论。；该结论对应 2023-11 的接口状态；新版本必须重新检查 release、文档和函数签名。
- 安全提示：将二阶导数用于接触/力矩优化前，应与有限差分或自动微分方向导数交叉检查，避免遗漏 external-force 项。
- 独立核验引用：[maintainer_confirmation · 维护者说明能力可以实现，但需要时间和工程投入](https://github.com/stack-of-tasks/pinocchio/issues/2092#issuecomment-1824887277)；[issue · 原作者只提出考虑 CppADCodeGen，没有提交实现或验证结果](https://github.com/stack-of-tasks/pinocchio/issues/2092#issuecomment-1831924121)
- 适用边界：适用于核对 2023-11 前后 Pinocchio 的含外力静力矩二阶导能力；当前版本和具体模型必须重新验证。

### Pinocchio 的空间与经典点加速度需要不同的 Jacobian 时间导数

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_classical_spatial_jacobian_time_derivative_2141`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：2（全部列出，不隐藏待验证或冲突来源）

**经验 1：getFrameJacobianTimeVariation 返回空间加速度 Jacobian 的时间导数**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：getFrameJacobianTimeVariation 返回的是空间加速度对应的 dJs/dt。若目标是经典点加速度，维护者在 LOCAL frame 给出的关系是 dJc=dJs+omega×Jl：代码上复制 Js 为 Jc，再对 dJc 的线性前三行加入 pin.skew(v_s.angular)@Jc\[:3,:\]。其完整脚本用 isApprox 断言验证了重构结果。LOCAL_WORLD_ALIGNED 的后续问题没有答案，因此该公式不能从本线程直接外推到该 reference frame。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #2141 评论 1925393733：维护者解释 dJs/dt 与 dJc/dt 差异并给出完整断言脚本；评论 2088271817 说明原始问题已回答；评论 2068201550 的 LWA 追问未获解答
- 原帖/精确回复：[getFrameJacobianTimeVariation 返回空间加速度 Jacobian 的时间导数](https://github.com/stack-of-tasks/pinocchio/issues/2141#issuecomment-1925393733)
- 平台/作者：GitHub Issues / matheecs
- 关键术语：空间加速度（spatial acceleration）；经典点加速度（classical point acceleration）；雅可比时间导数（Jacobian time derivative）；局部坐标系（local frame）；叉乘矩阵（skew-symmetric matrix）
- 环境：Ubuntu 22.04.3 LTS、Pinocchio 3、pin.buildSampleModelManipulator()。
- 症状：原帖示例中经典加速度与直接使用 getFrameJacobianTimeVariation@v 的结果在线性前三维明显不同，角加速度后三维一致。；原作者手工加入 omega 与线性 Jacobian 的叉乘项后，示例数值与 getFrameClassicalAcceleration 一致。
- 诊断：先确认需要的是空间加速度（spatial acceleration）还是经典点加速度（classical point acceleration）。；分别用 getFrameAcceleration 和 getFrameClassicalAcceleration 建立数值对照，并在相同 LOCAL frame 中验证 a_s=J_s*qddot+dJ_s*qdot。
- 原因：维护者明确说明 getFrameJacobianTimeVariation 返回 dJs/dt；把它直接当作经典点加速度的 dJc/dt 会漏掉 omega×Jl 项。
- 处理过程：原作者手工计算叉乘项并得到与经典加速度一致的结果。；维护者提供完整随机 q、v、qddot 脚本，以三个 isApprox 断言核验关系。
- 有效处理：在维护者给出的 LOCAL-frame 范围内，以 Jc=Js，并令 dJc 的线性块加上 skew(omega)@Jc_linear，再用 Jc*qddot+dJc*qdot 重构经典点加速度。
- 结果：维护者脚本通过断言验证经典加速度与空间加速度关系、空间 Jacobian 重构和修正后的经典加速度重构；项目方据此认定原始 Issue 已回答且无需修改 Pinocchio。
- 限制：维护者脚本只明确覆盖 LOCAL frame；LOCAL_WORLD_ALIGNED 下的经典加速度 Jacobian 时间导数追问未获回答，不能从本线程自行推广公式。；关于 Jc=Js.copy() 的后续概念追问也未在该线程回答。；该线程没有给出特定机器人 URDF 的独立复测。
- 安全提示：把 Jdot*qdot 用于加速度或接触约束前，应与同 frame 的运动学加速度接口做数值对照，避免错误补偿进入实机力矩。
- 独立核验引用：[maintainer_confirmation · 项目方确认原始 Issue 已由维护者脚本回答，因此无需 Pinocchio 代码改动](https://github.com/stack-of-tasks/pinocchio/issues/2141#issuecomment-2088271817)；[issue · LOCAL_WORLD_ALIGNED 下的后续追问未得到公式，用于限定本卡适用范围](https://github.com/stack-of-tasks/pinocchio/issues/2141#issuecomment-2068201550)
- 适用边界：适用于 Pinocchio 3、LOCAL frame、以经典点加速度重构 J*qddot+Jdot*qdot 的场景；其他 reference frame 必须重新推导和验证。

**经验 2：任务空间控制只需要 Jdot*qdot 时可直接读取经典加速度漂移项**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：维护者建议先用 forwardKinematics(model,data,q,v,0*v) 把广义加速度置零，再通过 getFrameClassicalAcceleration 直接读取 frame 的经典加速度漂移；原作者确认这就是其公式中所需的 classical Jdot*qdot。它只返回乘积/漂移项，不等于提供完整 Jdot 矩阵。后续用户自写的矩阵公式没有项目方确认，不应混入这一已闭环经验。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1395 评论 779978792 说明零 qddot 后读取 acceleration drift；评论 779991630 原作者确认 getFrameClassicalAcceleration；评论 780094814 维护者确认
- 原帖/精确回复：[任务空间控制只需要 Jdot*qdot 时可直接读取经典加速度漂移项](https://github.com/stack-of-tasks/pinocchio/issues/1395#issuecomment-779991630)
- 平台/作者：GitHub Issues / junhyeokahn
- 关键术语：经典点加速度（classical point acceleration）；空间加速度（spatial acceleration）；雅可比时间导数（Jacobian time derivative）；加速度漂移项（acceleration drift term）；任务空间控制（task-space control）
- 环境：2021 年 Pinocchio API、两自由度机械臂示例；原帖未给版本、OS 或完整代码。
- 症状：getFrameJacobianTimeVariation 返回 spatial acceleration 相关量，而控制器公式 qddot_des=pinv(J)(ac_des-Jdot*qdot) 需要 classical acceleration drift。
- 诊断：先确认控制器实际需要完整 Jdot 还是只需要乘积 Jdot*qdot。；将 qddot 置零运行 forward kinematics，使 frame classical acceleration 对应速度产生的漂移项。
- 原因：问题来自把 spatial Jacobian derivative 与 classical point acceleration 控制公式混用。
- 处理过程：维护者建议 forwardKinematics(model,data,q,v,0*v) 后直接获取 acceleration drift，并指向 TSID 的同类控制器。；原作者确认 getFrameClassicalAcceleration 可直接得到其所需的 classical Jdot*qdot。
- 有效处理：当只需乘积项时，以零 qddot 调用 forwardKinematics，再使用 getFrameClassicalAcceleration 读取 frame 的 classical acceleration drift，避免显式构造 Jdot。
- 结果：原作者确认理解并采用这一思路；维护者确认该方式简单且高效。
- 限制：线程没有给完整函数调用顺序、reference frame 参数或数值输出；目标版本应以最小测试核对。；这一捷径只直接回答 Jdot*qdot，不提供完整 Jdot 矩阵；确实需要矩阵本身时仍需使用相应 API/推导。；后续用户自行写出的 classical dJ 公式没有维护者确认，没有纳入答案。
- 安全提示：把漂移补偿用于实机前，应以数值差分或已知轨迹验证符号、frame 和量纲；错误偏置会直接改变期望关节加速度。
- 独立核验引用：[issue · 独立原线程给出 spatial/classical Jdot 的显式关系和完整断言脚本；本卡聚合为同一稳定问题](https://github.com/stack-of-tasks/pinocchio/issues/2141)；[maintainer_confirmation · 维护者确认直接获取漂移项的方式简单且高效](https://github.com/stack-of-tasks/pinocchio/issues/1395#issuecomment-780094814)
- 适用边界：适用于加速度级任务控制只需要 frame classical Jdot*qdot 漂移项的场景；需要完整 Jdot 或其他 frame 时需单独处理。

### Pinocchio 质心动力学是否包含基座惯量取决于基座是否被建模为可动自由度

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_centroidal_base_mobility_modeling_1252`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 质心动量的表达坐标系与基座建模边界**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：维护者说明，真正固定的机械臂 base 不运动，其 base 惯量不会作为运动基座贡献进入 centroidal dynamics；若机械臂放在由 JointModelPlanar 表达的移动基座上，基座惯量会贡献。由 prismatic cart 与 revolute pendulum 建模的系统也不是传统固定基，而是自由度较少的移动/浮动基系统。线程确认了建模分类，但没有给数值等价测试。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1252 评论 716349153 解释固定 base；评论 716646794 澄清 cart-pendulum；评论 716667472 解释 planar mobile base 的惯量贡献；评论 716704766 确认建模方向
- 原帖/精确回复：[Pinocchio 质心动量的表达坐标系与基座建模边界](https://github.com/stack-of-tasks/pinocchio/issues/1252#issuecomment-716667472)
- 平台/作者：GitHub Issues / rshum19
- 关键术语：固定基座（fixed base）；移动基座（mobile base）；平面关节（planar joint）；欠驱动系统（underactuated system）；基座惯量（base inertia）
- 环境：2020–2022 年 Pinocchio C++ API；原帖未给具体版本、机器人 URDF 或数值测试。
- 症状：调用者不确定 computeCentroidalMomentum 是否对应 Orin、Goswami、Lee 2013 所述的人形质心动量。；调用者进一步不确定没有显式 JointModelFreeFlyer 时，cart-pendulum 或固定机械臂的 base 惯量是否被计入。
- 诊断：记录质心动量 frame 的原点和轴向：原点在 CoM，轴与 world 对齐。；检查模型中的 base 是否具有实际广义坐标；不要把“没有 FreeFlyer”自动等同为固定基。；区分静止固定 base 的惯量与通过 planar/prismatic 自由度运动的 base 惯量。
- 处理过程：维护者直接确认函数定义、表达 frame 和时间导数接口。；原作者以固定机械臂、cart-pendulum 和 JointModelPlanar 移动基座逐步澄清基座建模。
- 有效处理：需要移动基座对系统动量的贡献时，在 URDF/根关节模型中显式建模相应自由度；线程确认 JointModelPlanar 是移动平面基座的可用建模入口。
- 结果：原作者确认 computeCentroidalMomentum 的定义回答了解其问题，并在基座建模讨论后再次表示理解。
- 限制：线程没有给线/角动量向量元素顺序、单位或数值例子；这些应从目标版本 API 文档与测试核对。；维护者对 URDF 中移动关节与 buildModel(..., JointModelPlanar()) 的最后回复很简短，本卡不把它扩写成任意模型都数值等价。；本线程不讨论外力、接触切换或质心动量矩阵导数。
- 安全提示：动量控制用于实机前，应以独立动量/力矩平衡检查 frame、单位和基座自由度，避免错误约束导致大接触力。
- 独立核验引用：[maintainer_confirmation · 项目贡献者澄清 prismatic cart + pendulum 不是固定基，而是自由度较少的移动/浮动基](https://github.com/stack-of-tasks/pinocchio/issues/1252#issuecomment-716646794)；[issue · 原作者在建模讨论后确认理解](https://github.com/stack-of-tasks/pinocchio/issues/1252#issuecomment-716707958)
- 适用边界：适用于以固定、prismatic/planar 或 FreeFlyer 根关节构造 Pinocchio 模型时解释基座对质心动力学的贡献。

### Pinocchio 质心动量的 CoM 原点与 world-aligned 轴约定

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_centroidal_momentum_frame_1252`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 质心动量的表达坐标系与基座建模边界**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：维护者确认，该函数计算刚体树的总质心动量，表达 frame 的原点位于系统质心，坐标轴与 world frame 对齐；后续追问确认线动量也采用相同约定。需要时间导数时调用 computeCentroidalMomentumTimeVariation。原线程没有给向量元素顺序或数值例子，因此实现时仍要核对目标版本文档。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1252 评论 650976642 确认定义、frame 与时间导数接口；评论 651815897 原作者确认；评论 1051564222 确认线动量同样适用
- 原帖/精确回复：[Pinocchio 质心动量的表达坐标系与基座建模边界](https://github.com/stack-of-tasks/pinocchio/issues/1252#issuecomment-650976642)
- 平台/作者：GitHub Issues / rshum19
- 关键术语：质心动量（centroidal momentum）；线动量（linear momentum）；角动量（angular momentum）；质心坐标系（center-of-mass frame）；世界对齐坐标轴（world-aligned axes）
- 环境：2020–2022 年 Pinocchio C++ API；原帖未给具体版本、机器人 URDF 或数值测试。
- 症状：调用者不确定 computeCentroidalMomentum 是否对应 Orin、Goswami、Lee 2013 所述的人形质心动量。；调用者进一步不确定没有显式 JointModelFreeFlyer 时，cart-pendulum 或固定机械臂的 base 惯量是否被计入。
- 诊断：记录质心动量 frame 的原点和轴向：原点在 CoM，轴与 world 对齐。；检查模型中的 base 是否具有实际广义坐标；不要把“没有 FreeFlyer”自动等同为固定基。；区分静止固定 base 的惯量与通过 planar/prismatic 自由度运动的 base 惯量。
- 处理过程：维护者直接确认函数定义、表达 frame 和时间导数接口。；原作者以固定机械臂、cart-pendulum 和 JointModelPlanar 移动基座逐步澄清基座建模。
- 有效处理：需要移动基座对系统动量的贡献时，在 URDF/根关节模型中显式建模相应自由度；线程确认 JointModelPlanar 是移动平面基座的可用建模入口。
- 结果：原作者确认 computeCentroidalMomentum 的定义回答了解其问题，并在基座建模讨论后再次表示理解。
- 限制：线程没有给线/角动量向量元素顺序、单位或数值例子；这些应从目标版本 API 文档与测试核对。；维护者对 URDF 中移动关节与 buildModel(..., JointModelPlanar()) 的最后回复很简短，本卡不把它扩写成任意模型都数值等价。；本线程不讨论外力、接触切换或质心动量矩阵导数。
- 安全提示：动量控制用于实机前，应以独立动量/力矩平衡检查 frame、单位和基座自由度，避免错误约束导致大接触力。
- 独立核验引用：[issue · 原作者确认函数定义回答了其问题](https://github.com/stack-of-tasks/pinocchio/issues/1252#issuecomment-651815897)；[maintainer_confirmation · 维护者确认线动量与角动量使用同一表达 frame 约定](https://github.com/stack-of-tasks/pinocchio/issues/1252#issuecomment-1051564222)
- 适用边界：适用于 Pinocchio computeCentroidalMomentum 与 computeCentroidalMomentumTimeVariation 的 frame 解释；输出排列和单位仍以目标版本为准。

### Pinocchio 质心动量解析导数的 FreeFlyer 平移漏项

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_centroidal_derivative_freeflyer_translation_bug_1473`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 质心动量对 FreeFlyer 平移的解析导数曾漏项**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：原作者先验证只改变 base position 的 q1/q2 得到相同 centroidal momentum，维护者随后确认 q 偏导漏掉一项。已合入 PR #1474 在 CoM 平移后的 dh_dq 与 dhdot_dq 角动量块补上相应项，并把有限差分测试改为直接比较 hg/dhg。应确认目标 Pinocchio 包含合并提交 d780648 或等价补丁；线程没有给第一个修复 release，也没有原作者合并后的新矩阵。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1473 评论 886642671 给出 h1/h2 对照；评论 886658456 维护者确认漏项；PR #1474 已合入并更新实现与测试
- 原帖/精确回复：[Pinocchio 质心动量对 FreeFlyer 平移的解析导数曾漏项](https://github.com/stack-of-tasks/pinocchio/issues/1473#issuecomment-886658456)
- 平台/作者：GitHub Issues / jp-sleiman
- 关键术语：质心动量导数（centroidal momentum derivative）；自由浮动关节（FreeFlyer joint）；解析导数（analytical derivative）；自动微分（automatic differentiation, AD）；有限差分（finite difference）
- 环境：2021 年 Pinocchio computeCentroidalDynamicsDerivatives 与 CppAD 对照；原帖未给版本、OS 或模型文件，修复固定在合并 PR #1474/commit d780648。
- 症状：解析 dh_dq 对 FreeFlyer position 的三列非零，而 CppAD 结果为零。；原作者用 Pinocchio 分别计算仅 base translation 不同的 q1/q2，得到 h1 与 h2 相同。
- 诊断：构造仅改变 FreeFlyer position 的成对配置，先验证 centroidal momentum 本身是否保持不变。；将解析 dh_dq 与自动微分/有限差分对照，并单独检查 base translation 三列。
- 原因：维护者最终确认 q 偏导计算漏掉一项；PR #1474 在把力集合平移到 CoM 后补充与线动量和 CoM 导数相关的角动量偏导项。
- 处理过程：原作者使用 CppAD 对照，并用 q1/q2 只改变 FreeFlyer position 的直接函数值对照排查。；维护者提交 PR #1474，修改两条 centroidal derivatives 路径及有限差分单元测试。
- 有效处理：使用包含 PR #1474 合并提交 d780648 的 Pinocchio，或核对目标版本是否包含等价的 centroidal derivatives 漏项修复。
- 结果：PR #1474 已合入；补丁同时更新 dh_dq/dhdot_dq 计算和 centroidal derivatives 有限差分测试。
- 限制：原作者没有在 PR 合并后发布新的 CppAD 数值矩阵；闭环依据是原作者函数值对照、维护者确认、补丁和测试。；线程没有声明第一个包含修复的正式 release；不能仅按版本号猜测。；本卡只覆盖该 FreeFlyer 平移漏项，不外推所有 centroidal derivative 差异。
- 安全提示：解析导数进入接触/动量优化前，应持续保留自动微分或有限差分回归，避免旧二进制或不同关节模型再次引入梯度错误。
- 独立核验引用：[pull_request · 已合入 PR 明确 Related to #1473，并修改两条 centroidal derivatives 路径和有限差分测试](https://github.com/stack-of-tasks/pinocchio/pull/1474)；[source_code · PR #1474 的固定合并提交](https://github.com/stack-of-tasks/pinocchio/commit/d78064830c8ac0859001dfd47f63169709c079cc)
- 适用边界：适用于旧版 computeCentroidalDynamicsDerivatives 的 FreeFlyer position 偏导；目标安装需核对是否包含 PR #1474。

### Pinocchio Composite Joint 下 CasADi 与解析 RNEA 导数不一致

- `problem_id`：`problem.optimization_ik_qp_mpc.pinocchio_rnea_derivatives_composite_casadi_1872`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio Composite Joint 下 CasADi 与 RNEA 解析导数不一致的支持边界**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：维护者判断原模型使用的 JointModelComposite 当时未正式支持 derivatives，建议改为纯 JointModelFreeFlyer，并用 integrate/difference 在配置流形切空间中定义扰动；同时给出官方 C++ CasADi RNEA derivative 测试作为调用参考。但原作者没有发布换 FreeFlyer 后的对照，最后关于 error-state/Euler/quaternion 优化变量的追问也没有答案。因此这不是已验证修复，只能作为目标版本和 joint model 的排查路径。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1872 评论 1436459057 判断 Composite derivatives 未支持并建议 FreeFlyer/integrate/difference；评论 1436461285 链接固定单元测试；评论 1439410356 的优化变量追问未回答
- 原帖/精确回复：[Pinocchio Composite Joint 下 CasADi 与 RNEA 解析导数不一致的支持边界](https://github.com/stack-of-tasks/pinocchio/issues/1872#issuecomment-1436459057)
- 平台/作者：GitHub Issues / matheecs
- 关键术语：逆动力学导数（inverse-dynamics derivative）；复合关节（Composite Joint）；自由浮动关节（FreeFlyer joint）；配置流形（configuration manifold）；切空间（tangent space）
- 环境：Pinocchio 3 Python、pin.buildSampleModelHumanoidRandom(False)、CasADi SX；原帖未给 OS、CasADi/Pinocchio 精确版本或 commit。
- 症状：解析 dtau_dq 与 CasADi Jacobian 的非根部关节列相同，但浮动基相关列出现明显不同。；原作者担心差异会影响优化。
- 诊断：先检查根关节是否为 JointModelComposite，以及目标算法是否正式支持该 joint model。；对 FreeFlyer 配置使用 integrate/difference 在切空间构造扰动；不要直接假定欧拉角或四元数坐标的普通导数与切空间导数等价。；参考维护者链接的固定 C++ 单元测试建立同一 joint model、同一扰动定义的对照。
- 原因：维护者判断 JointModelComposite 当时尚未支持 derivatives，需要额外工程工作。
- 处理过程：原作者用同一 q、v、a 比较 Pinocchio 解析 dtau_dq 与 CasADi 直接 q-Jacobian。；维护者建议使用纯 FreeFlyer 与 integrate/difference，并链接官方 C++ CasADi derivative 测试。
- 结果：线程没有换成 FreeFlyer 后的数值结果，也没有回答优化变量应怎样具体参数化；Issue 关闭不能证明差异已在原环境消失。
- 限制：维护者的原因判断没有原作者复测或关联修复 PR；只能作为高价值排查方向。；最后关于 error state、Euler angle 和 quaternion 优化变量的追问未回答，本卡不自行给出优化器设计。；链接的单元测试展示官方用法，但没有证明原作者的 Composite Joint 模型已受支持。
- 安全提示：导数进入优化器前应对同一切空间方向做有限差分/自动微分检查；浮动基列不一致时不得直接用于实机力矩优化。
- 独立核验引用：[source_code · 维护者提供的固定 C++ CasADi RNEA derivatives 单元测试；仅用于参考官方扰动/比较方式](https://github.com/stack-of-tasks/pinocchio/blob/0d53f26acdf9a0b5740b88145f624b11d97f40f9/unittest/casadi/rnea-derivatives.cpp#L24-L174)；[issue · 原作者关于优化变量的最后追问没有回答，用于限制本卡结论](https://github.com/stack-of-tasks/pinocchio/issues/1872#issuecomment-1439410356)
- 适用边界：适用于 Pinocchio 3、CasADi RNEA derivatives 与 Composite/FreeFlyer 根关节的对照；当前版本的 Composite 支持状态需重新核对。

### Isaac Lab 的 Jacobian 时间导数 Jdot 能力边界

- `problem_id`：`problem.optimization_ik_qp_mpc.isaaclab_jdot_api_1759`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 没有直接给出 Jacobian 时间导数 Jdot 的接口**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：按 IsaacLab 团队在 2025-02 的原帖回复，当时没有现成 Jdot 能力，需要手工实现。线程没有给出实现细节或复测，因此这是一条版本相关的能力线索：先在目标版本 API 中重新确认，再自行选择并验证解析或数值实现，不能把帖子补写成某一种算法建议。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #1759 唯一评论 2628472796
- 原帖/精确回复：[Isaac Lab 没有直接给出 Jacobian 时间导数 Jdot 的接口](https://github.com/isaac-sim/IsaacLab/issues/1759#issuecomment-2628472796)
- 平台/作者：GitHub Issues / hojae-io
- 关键术语：雅可比时间导数（Jacobian time derivative, Jdot）；任务空间加速度（task-space acceleration）；手工实现（manual implementation）
- 环境：2025-01 的 IsaacLab Issue；原帖未给 Isaac Lab、Isaac Sim、GPU 或机器人版本。
- 症状：实现 v=Jqdot 的时间微分关系时需要 Jdot，但调用者找不到现成接口。
- 诊断：先确认所用 Isaac Lab/Isaac Sim 版本是否新增 Jdot API；原线程只覆盖 2025-01 时点。
- 处理过程：团队成员检查后回复，当时没有该能力，需要手工实现。
- 结果：能力边界得到回答，但手工实现方案、数值稳定性和验收方法均未给出。
- 限制：不能从该线程推导应使用有限差分、解析递推还是自动微分；也不能断言当前最新版仍没有该接口。
- 安全提示：若用数值差分估计 Jdot 或 Jdot*qdot，应在目标控制频率下检查噪声放大和最坏时延。
- 独立核验引用：[maintainer_confirmation · 团队回复当时没有现成 Jdot 能力，需要手工实现](https://github.com/isaac-sim/IsaacLab/issues/1759#issuecomment-2628472796)
- 适用边界：适用于核对 2025 年初 Isaac Lab 的 Jdot API 能力；当前版本和具体实现仍需复核。

### Crocoddyl 飞行相动量的积分器漂移

- `problem_id`：`problem.optimization_ik_qp_mpc.crocoddyl_aerial_momentum_integrator_979`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Crocoddyl 空中相角动量漂移可先对比 Euler 与 RK4 积分器**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：帖子先排除了 contact force，并确认 JMinvJt_damping=0；单纯把 timestep 从 0.005 降到 0.001 改善有限。按维护者建议把 Euler 换为 RK4 后，作者报告 angular momentum 在 aerial phase 保持恒定。维护者将原因归为 numerical integrator 引入的 drift/energy injection。该结果适合作为同配置 A/B 诊断，不代表所有动量漂移都由积分器造成。
- 证据状态：`issue_candidate`
- 来源定位：Crocoddyl #979 维护者建议 887311851、作者复测 888126517、维护者解释 888133549/888232475
- 原帖/精确回复：[Crocoddyl 空中相角动量漂移可先对比 Euler 与 RK4 积分器](https://github.com/loco-3d/crocoddyl/issues/979#issuecomment-888126517)
- 平台/作者：GitHub Issues / zzhou387
- 关键术语：角动量（angular momentum, AM）；飞行相（aerial phase）；数值积分器（numerical integrator）；辛格式（symplectic scheme）
- 环境：Crocoddyl A1 jumping/backflipping optimization；aerial phase 无 contact model、contact forces 已确认始终为零。；原 timestep 0.005，尝试 0.001；JMinvJt_damping 一直为 0；未给 commit/OS。
- 症状：飞行相 angular momentum 不恒定，腿部摆动时更明显。；仅减小 Euler timestep 没有充分改善。
- 诊断：先确认 aerial phase contact forces 为零且没有 contact model。；记录 JMinvJt_damping 与 integrator；在相同 cost/contact 配置下做 Euler/RK4 A/B。
- 原因：两位维护者把漂移归因于 numerical integrator 注入能量，而不是所链接的 Pinocchio issue。
- 处理过程：作者从 Euler 切换到 RK4，同时保持 JMinvJt_damping=0。
- 有效处理：作者特定轨迹中改用 RK4 后 angular momentum 漂移大幅改善，并报告飞行相保持恒定。
- 结果：作者确认问题在其案例中解决；维护者解释 advanced integrator 可降低 drift。
- 限制：没有 commit、机器人参数、RK4 timestep 或数值误差阈值，不能外推为所有飞行相只需换 RK4。；作者贴出的曲线图未用于本卡判断；结果采用其文字复测。；若换积分器仍漂移，还需继续检查 contact leakage、model/inertia 和 cost formulation。
- 安全提示：跳跃轨迹上机前应独立检查动量、接触切换、峰值力矩和落地冲击，不以优化器收敛替代物理一致性验收。
- 独立核验引用：[maintainer_confirmation · Crocoddyl 维护者确认 numerical integrators 会注入能量，并说明 Euler/RK4 的设计约束](https://github.com/loco-3d/crocoddyl/issues/979#issuecomment-888232475)
- 适用边界：适用于 Crocoddyl 飞行相 trajectory optimization 中 contact 已排除且 Euler 积分产生明显漂移的案例。

### Crocoddyl BoxQP 的 Armijo 终止错误

- `problem_id`：`problem.optimization_ik_qp_mpc.crocoddyl_boxqp_armijo_743`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：BoxQP 随机初值多跑迭代先核对 Armijo 条件修复**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：先确认版本包含合并 PR #1067。维护者在 #743 中明确定位到 Armijo condition 错误：它会让求解器找到 solution 后仍执行额外迭代，随机初始化时还不保证收敛；该问题不是 factorization solver 的结论。PR #1067 重算 free-subspace gradient/search direction，并在更新后的 free-gradient infinity norm 上检查收敛。修复后仍应以目标 MPC 问题回归 KKT residual 与迭代上界。
- 证据状态：`issue_candidate`
- 来源定位：Crocoddyl #743 维护者定位 1113252162；PR #1067
- 原帖/精确回复：[BoxQP 随机初值多跑迭代先核对 Armijo 条件修复](https://github.com/loco-3d/crocoddyl/issues/743#issuecomment-1113252162)
- 平台/作者：GitHub Issues / wxmerkt
- 关键术语：阿米霍条件（Armijo condition）；自由子空间梯度（free-subspace gradient）；随机初始化（random initialization）；无用迭代（useless iterations）
- 环境：Crocoddyl 2020–2022 BoxQP 变更讨论；原帖含 Exotica quadcopter side-by-side benchmark，但未给统一硬件/commit。；精确修复为 2022-04 合并 PR #1067。
- 症状：求解器找到 solution 后仍运行 extra iterations。；random initialization 下 convergence 不保证。
- 诊断：先检查目标版本是否包含 PR #1067，再讨论 LLT/LDLT/PivLU 或 line-search schedule。；用固定随机 QP 集记录 iteration count、termination reason 与 KKT/free-gradient norm。
- 原因：维护者明确定位为 Armijo condition 错误，而非 factorization solver。
- 处理过程：线程比较新旧 active set、gradient norm、linear/exponential line search 和多种 factorization。；PR #1067 修正 free-subspace gradient/search direction 与 convergence check，并更新 identity-Hessian regularized test。
- 有效处理：升级到包含 PR #1067 / merge commit d5c387e 的 Crocoddyl 版本。
- 结果：维护者说明修复可避免已找到 solution 后的无用迭代，并恢复随机初始化下该条件的收敛判定；PR 已合并。
- 限制：#743 中关于 factorization 性能的讨论没有形成可普遍采纳的结论，本卡不推荐某一种分解器。；原作者提到的 90%/30% speedup 来自其未合并改动，不能归因于 PR #1067。；不使用原帖性能图作为本卡证据。
- 安全提示：实时 MPC 升级求解器后应对 worst-case iterations、KKT residual、deadline miss 和 fallback 做回归。
- 独立核验引用：[pull_request · 合并 PR d5c387e 修正 BoxQP free-gradient/search direction 与 convergence check，并更新测试](https://github.com/loco-3d/crocoddyl/pull/1067)
- 适用边界：适用于缺少 2022-04 PR #1067 的 Crocoddyl BoxQP/Box(F)DDP 路径，尤其 random initialization 与多余迭代问题。

### OCS2 hard inequality constraint 的实际求解路径

- `problem_id`：`problem.optimization_ik_qp_mpc.ocs2_hard_inequality_path_108`
- 问题综合等级：**需要实际验证** — 不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OCS2 hard inequality constraint 路径的社区解释相互冲突**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突；当前仅形成问题线索；尚未形成可核对的复现记录；适用环境未知。
- 解答状态：`conflicting`
- 候选解答：没有。线程中的解释互相冲突：一条回复称 SQP 用 relaxed barrier，后续源码讨论又认为 hard constraints 可能进入 HPIPM，原回复者随后承认只确认了 equality path、没有找到 inequality path。也没有维护者、版本化最小复现或原作者复测。当前能可靠保留的只有排查方法：在目标 commit 分开测试 state/state-input 与 equality/inequality，逐层打印 constraint value、linearization、QP bounds 和 HPIPM residual；delta/mu 调参不能当作已验证答案。
- 证据状态：`issue_candidate`
- 来源定位：OCS2 #108 社区解释 2346304811、反向源码观察 2413803782、修正 2414510557、同类复现 2721087622
- 原帖/精确回复：[OCS2 hard inequality constraint 路径的社区解释相互冲突](https://github.com/leggedrobotics/ocs2/issues/108#issuecomment-2414510557)
- 平台/作者：GitHub Issues / min-dai
- 关键术语：硬不等式约束（hard inequality constraint）；松弛障碍函数（relaxed barrier function）；内点法（interior-point method, IPM）；约束残差（constraint residual）
- 环境：原帖未给 OCS2 commit、solver config、机器人模型、操作系统或最小复现。；评论源码链接锚定 commit 164c26b 的 SqpSolver/HpipmInterface。
- 症状：hard input inequality constraints 未满足；equality 只有 linear portion 满足。；constraint violation 时 MPC 继续运行且不报告 infeasible。；另一用户把 stateinputConstraint 放入 inequalityConstraintPtr 后也报告无变化。
- 诊断：在目标 commit 追踪 constraint collection、linearization、SqpSolver 到 HpipmInterface 的具体数组，并打印每阶段维度。；构造单状态/单输入最小问题，同时记录原始 constraint value、linear approximation、QP bounds 与 solver residual。；把 state-only、state-input、equality、inequality 四类约束分开测试。
- 原因：评论对 hard inequality 是否使用 relaxed barrier、是否传入 HPIPM 的解释互相矛盾；没有证据足以确定根因。
- 处理过程：社区用户逐行查了 SqpSolver.cpp 和 HpipmInterface.cpp 的 equality path。；有人建议调 relaxed-barrier delta/mu，但随后承认前述 inequality 解释可能错误。
- 结果：没有原作者复测、维护者确认或已合并修复；2025-03 仍有用户询问同类问题。
- 限制：不能把 delta/mu 调参写成已验证解法。；不能从 thread 确认 inequality 根本没有传给 HPIPM；需要绑定目标 commit 做 source trace。；帖子缺少最小复现和版本，适用性未知。
- 安全提示：在 constraint path 未闭环前，不应依赖该约束保护真实机器人；必须增加独立 runtime monitor、command clamp 和安全停机。
- 独立核验引用：[conflict · 首条回复称 inequality 使用 relaxed barrier、无 hard guarantee](https://github.com/leggedrobotics/ocs2/issues/108#issuecomment-2346304811)；[conflict · 后续用户按源码提出 hard constraints 进入 HPIPM 的相反解释](https://github.com/leggedrobotics/ocs2/issues/108#issuecomment-2413803782)
- 适用边界：仅作为 OCS2 SQP/IPM constraint-path 排查入口；因缺少版本和最小复现，不能直接外推。

### 约束 DDP 不能只按 dVexp 跳过 rollout

- `problem_id`：`problem.optimization_ik_qp_mpc.crocoddyl_dvexp_constraints_1104`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Crocoddyl 约束求解中不能因 dVexp 为负跳过 dV**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：该线程最终答案是否定的。维护者在关闭前明确修正早期说法：带 constraints 的 solver 必须在代价改善（optimality）与约束满足（feasibility）之间权衡，单凭 `dVexp<0` 跳过实际 rollout/`dV` 会干扰 step acceptance。用户指定 alpha 列表本身可以配置；根据剩余 MPC 时间自适应测试 alpha 仍是方向，但线程没有提供可复用的公开实现或 benchmark。
- 证据状态：`issue_candidate`
- 来源定位：Crocoddyl #1104 最终维护者更正 1772562615
- 原帖/精确回复：[Crocoddyl 约束求解中不能因 dVexp 为负跳过 dV](https://github.com/loco-3d/crocoddyl/issues/1104#issuecomment-1772562615)
- 平台/作者：GitHub Issues / andreadelprete
- 关键术语：线搜索（line search）；期望改进（expected improvement, dVexp）；最优性（optimality）；可行性（feasibility）
- 环境：Crocoddyl 2022-2023 master/devel 讨论；没有固定 release、机器人或 timing benchmark。
- 症状：forward pass 在部分 MPC 测试中占到约 75%，用户希望减少 line-search rollout。
- 诊断：区分无约束 DDP 的下降判据与 constrained solver 中 cost improvement/constraint satisfaction 的联合 step acceptance。
- 原因：早期优化建议只看 optimality，没有覆盖带约束求解需要同时改善 feasibility 的路径。
- 处理过程：线程讨论跳过 dV、用户可配 alpha、自适应 line search 与并行 tryStep；后续维护者基于约束 solver 进展修正第一点。
- 有效处理：不要在 constrained solver 中仅凭 `dVexp<0` 跳过 `dV`；具体 step acceptance 应以目标版本 solver 实现为准。
- 结果：维护者明确撤销早期 point 1；自适应 alpha 点仍有效但由维护者在更大 solver 改造中处理，线程未提供公开补丁。
- 限制：维护者提到 private branch 的改进尚未在该线程公开，不能据此声称某版本已有 adaptive line search。；没有 forward-pass before/after timing，不能量化建议的性能影响。
- 安全提示：接触、摩擦或执行器约束存在时，任何 line-search shortcut 都必须同时回归 cost、constraint violation 与 deadline miss。
- 独立核验引用：[maintainer_confirmation · 维护者明确撤销早期 shortcut，并解释 constrained optimality/feasibility 权衡](https://github.com/loco-3d/crocoddyl/issues/1104#issuecomment-1772562615)
- 适用边界：适用于包含 feasibility/constraints 权衡的 DDP/FDDP 类 solver；无约束旧 DDP 的具体实现仍需按版本核对。

### TSID 任意 internal passive joints 尚需 formulation 支持

- `problem_id`：`problem.optimization_ik_qp_mpc.tsid_arbitrary_passive_joints_165`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：TSID 两 frame 闭链 contact 已合并但任意 passive joints 仍需分开处理**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原线程不能支持这一结论。作者在 fully-actuated loop 中成功，但把 pantograph 的其他 passive joints 设为 zero torque limit 后出现异常运动。维护者说明当时 TSID 除 floating base 外不能声明任意 passive joints；建议在 `RobotWrapper` 保存 passive-joint 信息，并在 `InverseDynamicsFormulation` 中选取对应 M、h、J rows，加入 torque=0 的 dynamics equality；较不整洁的替代是实现 `TaskActuationEquality`。这些只是明确的实现方向，线程没有合并代码或结果，因此 #218 不能单独视为 pantograph 完整修复。
- 证据状态：`issue_candidate`
- 来源定位：TSID #165 作者失败边界 1181695831、维护者 formulation 建议 1184238644
- 原帖/精确回复：[TSID 两 frame 闭链 contact 已合并但任意 passive joints 仍需分开处理](https://github.com/stack-of-tasks/tsid/issues/165#issuecomment-1184238644)
- 平台/作者：GitHub Issues / egordv
- 关键术语：被动关节（passive joint）；驱动选择矩阵（actuation selector）；逆动力学等式（inverse-dynamics equality）；零力矩约束（zero-torque constraint）
- 环境：TSID devel/master 2022-2024；作者在 fully-actuated humanoid wrists 和 Talos gripper demo 上检查 TwoFrames contact；没有固定 release。
- 症状：TwoFrames contact 在 fully-actuated closed loop 工作；把 pantograph passive joints 伪装成 torque-limit=0 后出现 weird movements。
- 诊断：先区分 loop-closure constraint 与 actuation/passive-joint selector；验证 contact 能否保持相对 frame displacement，再单独检查 passive rows 的 torque=0 equality。
- 原因：原 TSID formulation 只把 floating base 作为 unactuated 部分，不能声明任意 internal passive joints。
- 处理过程：作者实现并验证 TwoFrames contact；维护者建议在 RobotWrapper 记录 passive joints，并在 InverseDynamicsFormulation 中选择对应 M、h、J rows 构造 torque-zero equality。
- 有效处理：刚性闭链使用已合并 PR #218 的 `ContactTwoFramePositions`/`TaskTwoFramesEquality` 路径。；任意 passive joints 的 formulation 修改在原线程没有落地；不要把 zero torque-limit hack 或 #218 单独当成 pantograph 完整解。
- 结果：PR #218 于 2024-02-02 合并；维护者复现 covariant return 的最小代码并接受 PR。；passive-joint selector/equality 方案没有关联实现或复测。
- 限制：#218 demo 证明特定闭链 contact，不证明任意 passive-joint pantograph；后续一位用户在 PAL REEM-C TwoFramesEquality 遇到 segfault，未在线程闭环。；spring-damper 的高刚度数值积分建议来自维护者设计讨论，本轮没有额外生成独立卡。
- 安全提示：闭链与 passive joint 错模会产生虚假约束力或不可执行 torque；真机前应检查 constraint residual、actuation selector、joint torque 与闭链内力。
- 独立核验引用：[maintainer_confirmation · 维护者确认当时无任意 passive-joint 接口，并给出 formulation rows/equality 实现方向](https://github.com/stack-of-tasks/tsid/issues/165#issuecomment-1184238644)
- 适用边界：适用于需要 floating base 之外 internal passive joints 的 TSID 模型；目标版本若已有新接口必须重新核对。

### 用 TwoFrames contact 表达 TSID 刚性闭链

- `problem_id`：`problem.optimization_ik_qp_mpc.tsid_two_frame_closed_chain_165`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：TSID 两 frame 闭链 contact 已合并但任意 passive joints 仍需分开处理**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：维护者明确建议使用 robot links 之间的 contact，而不是高增益 task。作者实现 `TaskTwoFramesEquality` 与 `ContactTwoFramePositions`，先在 fully-actuated 双腕闭链中报告有效，后续 PR #218 合并了实现、Python bindings 与 Talos gripper demo。它约束两 frames 的相对位置，可表达这一类 loop closure；但不自动解决任意 internal passive joints。
- 证据状态：`issue_candidate`
- 来源定位：TSID #165 维护者 contact 建议 1178973756、作者仿真 1181695831；合并 PR #218
- 原帖/精确回复：[TSID 两 frame 闭链 contact 已合并但任意 passive joints 仍需分开处理](https://github.com/stack-of-tasks/tsid/issues/165#issuecomment-1181695831)
- 平台/作者：GitHub Issues / egordv
- 关键术语：闭合运动链（closed kinematic chain）；两坐标系接触（two-frame contact）；相对位姿（relative placement）；全驱动（fully actuated）
- 环境：TSID devel/master 2022-2024；作者在 fully-actuated humanoid wrists 和 Talos gripper demo 上检查 TwoFrames contact；没有固定 release。
- 症状：TwoFrames contact 在 fully-actuated closed loop 工作；把 pantograph passive joints 伪装成 torque-limit=0 后出现 weird movements。
- 诊断：先区分 loop-closure constraint 与 actuation/passive-joint selector；验证 contact 能否保持相对 frame displacement，再单独检查 passive rows 的 torque=0 equality。
- 原因：原 TSID formulation 只把 floating base 作为 unactuated 部分，不能声明任意 internal passive joints。
- 处理过程：作者实现并验证 TwoFrames contact；维护者建议在 RobotWrapper 记录 passive joints，并在 InverseDynamicsFormulation 中选择对应 M、h、J rows 构造 torque-zero equality。
- 有效处理：刚性闭链使用已合并 PR #218 的 `ContactTwoFramePositions`/`TaskTwoFramesEquality` 路径。；任意 passive joints 的 formulation 修改在原线程没有落地；不要把 zero torque-limit hack 或 #218 单独当成 pantograph 完整解。
- 结果：PR #218 于 2024-02-02 合并；维护者复现 covariant return 的最小代码并接受 PR。；passive-joint selector/equality 方案没有关联实现或复测。
- 限制：#218 demo 证明特定闭链 contact，不证明任意 passive-joint pantograph；后续一位用户在 PAL REEM-C TwoFramesEquality 遇到 segfault，未在线程闭环。；spring-damper 的高刚度数值积分建议来自维护者设计讨论，本轮没有额外生成独立卡。
- 安全提示：闭链与 passive joint 错模会产生虚假约束力或不可执行 torque；真机前应检查 constraint residual、actuation selector、joint torque 与闭链内力。
- 独立核验引用：[pull_request · 已合并 TwoFramesEquality/ContactTwoFramePositions、Python bindings 与 Talos gripper closed-chain demo](https://github.com/stack-of-tasks/tsid/pull/218)
- 适用边界：适用于以两个 frame 相对位置约束表达的 rigid closed chain；需按 mask/contact 类型核对目标 joint 几何。

### OCS2 大系统 MPC 的分阶段性能诊断

- `problem_id`：`problem.optimization_ik_qp_mpc.ocs2_large_system_profiling_34`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OCS2 大系统 MPC 先关闭开发期数值检查并分段 profiling**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：维护者建议把开发与性能两种配置分开：`checkNumericalStability=true` 会做昂贵的 eigenvalue checks，开发阶段用于验证数值假设，追求速度的已验证运行应设为 false；同时开启 `displayInfo` 或 `displayShortSummary`，先看 adaptive stepping 的平均步长和 LQ approximation、backward pass 等分阶段时间。原作者随后报告 MPC 能运行，并观察到 low-frequency case 的 equality SSE/rollout merit/cost 爆炸；调整 input cost 后也降低了最昂贵 backward pass 的时间。线程没有最终 timing 或通用 cost gains，因此这是 profiling 流程，不是 39-DoF 实时保证。
- 证据状态：`issue_candidate`
- 来源定位：OCS2 #34 维护者性能建议 1083359506、分段定位 1088544950；作者结果 1119497280
- 原帖/精确回复：[OCS2 大系统 MPC 先关闭开发期数值检查并分段 profiling](https://github.com/leggedrobotics/ocs2/issues/34#issuecomment-1119497280)
- 平台/作者：GitHub Issues / IoannisDadiotis
- 关键术语：数值稳定性检查（numerical-stability check）；特征值检查（eigenvalue check）；反向传播阶段（backward pass）；线性二次近似（Linear-Quadratic approximation, LQ approximation）
- 环境：Centauro 39 actuated DoFs、continuous DDP、SRBD 与 centroidal variants、4 feet contacts；OCS2 2022 代码，未固定 commit。
- 症状：初始界面显示约 2-3 秒求解，并警告 solution time window shorter than MPC delay。；低 MPC frequency static gait 中 equality constraints SSE、rollout merit 与 rollout cost 爆炸；backward pass 最耗时。
- 诊断：性能运行时关闭 `checkNumericalStability` 的 expensive eigenvalue checks；打开 `displayInfo`/`displayShortSummary`，查看 adaptive integrator average stepsize 与各 solver phase timing。；若 backward pass 最慢，检查 problem dimension 与 Riccati stiffness；若 LQ approximation 最慢，分别 benchmark costs、constraints 与 dynamics。
- 原因：开发期 numerical-stability checks 造成额外 eigenvalue 计算；问题 stiffness、cost gains 与 constraint satisfaction 也会增加 steps 或 backward-pass 时间。
- 处理过程：作者调整 input cost，并用 solver printouts 观察 SSE、rollout merit/cost 与 backward-pass 时间。
- 有效处理：把 `checkNumericalStability=false` 作为性能测量配置，而不是删除开发期检查；用 phase timing 后再针对 input cost/constraints/dynamics 做定点优化。
- 结果：作者报告 MPC 已能在 robot-in-place 场景运行，input cost 调整同时帮助降低 backward-pass 时间；没有给最终毫秒数。
- 限制：维护者提到另一个 48-state/24-input 系统低于 10 ms 只是经验量级，不能作为 Centauro 保证。；低频 gait、dummy slowdown ratio 与 target node crash 等后续问题没有完整闭环，本卡不为它们提供推测答案。；线程视频不用于推断 motion quality，只采用作者文字确认。
- 安全提示：关闭数值检查只用于已通过开发验证的性能运行；上线前仍需离线检查 Hessian/derivative、constraint residual 与 deadline monitor。
- 独立核验引用：[maintainer_confirmation · 维护者确认 numerical stability eigenvalue checks 昂贵，并给出 display/profiling flags](https://github.com/leggedrobotics/ocs2/issues/34#issuecomment-1083359506)；[issue · 原作者报告 input cost 调整降低 backward-pass 时间，但未给最终 timing](https://github.com/leggedrobotics/ocs2/issues/34#issuecomment-1119497280)
- 适用边界：适用于 OCS2 DDP/MPC 大系统的开发期与性能期分离；字段名和统计输出需按目标版本核对。

### 校验 qpOASES 跨接口的约束矩阵布局

- `problem_id`：`problem.optimization_ik_qp_mpc.qpoases_matrix_layout_37`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：qpOASES C++ 与 Matlab/Simulink 结果不一致先查 A 的存储顺序**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：先逐元素检查 constraint matrix `A` 的存储顺序。维护者说明 C++ 接口期望行主序（row-major），而 Matlab/Simulink 内部采用列主序（column-major）；`A` 被隐式转置时，求解器拿到的是另一个 QP，常表现为不可行。对称 `H` 可能掩盖布局错误。Simulink 还要按接口要求把 `A` 堆叠为向量。只有确认实际传入矩阵一致后，才继续比较求解选项与数值设置。
- 证据状态：`issue_candidate`
- 来源定位：qpOASES #37 维护者支持记录正文与 resolution 589978265
- 原帖/精确回复：[qpOASES C++ 与 Matlab/Simulink 结果不一致先查 A 的存储顺序](https://github.com/coin-or/qpOASES/issues/37)
- 平台/作者：GitHub Issues / ferreau（Trac 迁移记录）
- 关键术语：行主序（row-major）；列主序（column-major）；约束矩阵（constraint matrix）；不可行二次规划（infeasible quadratic program）
- 环境：qpOASES 3.1.0 的迁移支持记录；C++、Matlab 与 Simulink 接口。
- 症状：C++ 与 Matlab/Simulink 结果不同；隐式转置 `A` 时常表现为不可行。
- 诊断：逐元素打印 C++ 实际接收的 `A`，按 row-major 还原并与 Matlab 中的矩阵比较；Simulink 同时检查向量堆叠顺序。
- 原因：维护者记录的典型原因是 C++ row-major 与 Matlab/Simulink column-major 不匹配，导致 constraint matrix 被隐式转置。
- 处理过程：原记录直接给出接口布局差异和 Simulink 的 `A` 向量化要求。
- 有效处理：按 C++ row-major 正确构造 `A`；在 Simulink 侧按接口规定的顺序堆叠约束矩阵。
- 结果：记录被标记 fixed，但没有附用户的独立复测数据。
- 限制：若实际传入矩阵逐元素一致，仍需继续检查 bounds、scaling、options 和精度；不能把所有接口差异都归因于布局。
- 安全提示：部署前保存一组黄金 QP，逐元素比较各接口输入与 primal/dual/status，避免静默求解了不同问题。
- 独立核验引用：[issue · 维护者在迁移后的 Issue 正文记录 row-major/column-major 边界](https://github.com/coin-or/qpOASES/issues/37)
- 适用边界：直接对应 qpOASES 3.1.0 接口记录；其他版本应以目标接口文档和实际内存数据复核。

### 核对 qpOASES_e 的静态 QP 维度上限

- `problem_id`：`problem.optimization_ik_qp_mpc.qpoases_e_static_dimensions_47`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：qpOASES_e 超过默认静态维度上限会伪装成 infeasible**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：不一定。该维护者记录说明 qpOASES_e 只用静态内存，默认编译上限为 50 个变量和 100 个约束。先把实际 nV/nC 与 `QPOASES_NVMAX`、`QPOASES_NCMAX` 对照；确实越界时修改 `include/qpOASES_e/Constants.h` 并重新编译。原帖没有提供重新编译后的作者复测，因此仍应在目标硬件上同时验证内存占用和求解结果。
- 证据状态：`issue_candidate`
- 来源定位：qpOASES #47 维护者回复 589978605
- 原帖/精确回复：[qpOASES_e 超过默认静态维度上限会伪装成 infeasible](https://github.com/coin-or/qpOASES/issues/47#issuecomment-589978605)
- 平台/作者：GitHub Issues / ferreau（Trac 迁移记录）
- 关键术语：静态内存（static memory）；编译时上限（compile-time limit）；变量维度（variable dimension）；约束维度（constraint dimension）
- 环境：qpOASES_e 3.1.1；原报告在 49 variables / 68 constraints 以内工作，继续增大后失败。
- 症状：初始化返回 infeasible，但 Matlab 其他 solver 能解同一问题；转折点靠近 50 variables。
- 诊断：在分析模型可行性前，先打印编译时 `QPOASES_NVMAX`、`QPOASES_NCMAX` 与实际 nV/nC。
- 原因：维护者确认 qpOASES_e 使用静态内存，默认最大 50 variables、100 constraints。
- 处理过程：原帖用其他 Matlab solver 交叉检查问题可解。
- 有效处理：提高 `include/qpOASES_e/Constants.h` 中两个上限并重新编译全部依赖该头文件的代码。
- 结果：维护者给出明确配置位置并将记录标记 fixed；没有附作者重新编译后的复测。
- 限制：增大静态上限会增加内存占用；超过新上限或仍失败时还需继续检查真实可行性与输入布局。
- 安全提示：嵌入式目标上修改上限前评估 RAM/stack，并在构建时加 nV/nC 静态或启动期断言。
- 独立核验引用：[maintainer_confirmation · 维护者给出默认 50/100 上限、宏名、文件位置和重新编译要求](https://github.com/coin-or/qpOASES/issues/47#issuecomment-589978605)
- 适用边界：直接对应 qpOASES_e 3.1.1 默认配置；发行包或 fork 可能改过宏值，应读实际构建头文件。

### 分离 zero stepsize 与 QP infeasibility 的诊断

- `problem_id`：`problem.optimization_ik_qp_mpc.qpoases_zero_stepsize_diagnostic_48`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：qpOASES zero stepsize 不是单独的故障结论**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：不能。维护者说明偶发 zero step 通常表示冗余约束使 working-set 迭代当下无法前进，并不单独构成故障结论。若最终还报 infeasible，原帖给出的排查顺序是：验证 QP 真实可行性；在不影响安全的离线副本中小幅放宽 bounds/constraints 检查 round-off；核对 `A` 的 row-major 布局。作者没有回报哪一步有效，所以这是一份诊断清单，不是已确认修复。
- 证据状态：`issue_candidate`
- 来源定位：qpOASES #48 维护者诊断回复 589978627；作者仅表示会尝试 589978633
- 原帖/精确回复：[qpOASES zero stepsize 不是单独的故障结论](https://github.com/coin-or/qpOASES/issues/48#issuecomment-589978627)
- 平台/作者：GitHub Issues / tristanc（Trac 迁移记录）
- 关键术语：步长（step size）；同伦路径（homotopy path）；工作集（working set）；舍入误差（round-off error）
- 环境：qpOASES 3.2.0 的迁移支持记录；原帖未提供 QP 数据或系统环境。
- 症状：先打印 zero stepsize warning，随后 premature homotopy termination / infeasible。
- 诊断：先独立验证 QP 可行性；再小幅放宽 variable bounds 与 constraints 排除 round-off；最后逐元素核对 row-major `A`。
- 原因：维护者说偶发 zero step 常与冗余约束和 working-set 线性独立性有关；但该线程没有定位用户具体 infeasible 的唯一根因。
- 处理过程：维护者给出三步排查；作者回复会尝试，但没有发布结果或 QP 数据。
- 有效处理：没有经原作者确认的有效修复；放宽边界和重排矩阵只能在确认具体问题后采用。
- 结果：记录后来标记 fixed，但线程没有技术闭环，因此本卡保持 partial。
- 限制：没有最小复现、参数尺度或作者结果；不能从日志序列推断真实根因。
- 安全提示：实时控制中不要无条件放宽安全约束；若为数值诊断，只在离线副本或受控限幅下试验。
- 独立核验引用：[maintainer_confirmation · 维护者解释 zero step 并给出三步排查；无作者结果确认](https://github.com/coin-or/qpOASES/issues/48#issuecomment-589978627)
- 适用边界：适用于 qpOASES 3.2.0 同类日志的初步排查；具体根因必须用 QP 数据复现。

### 导出失败周期 QP 区分 solver 与上游 Hessian 问题

- `problem_id`：`problem.optimization_ik_qp_mpc.acado_qpoases_hessian_export_50`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ACADO 内嵌 qpOASES Cholesky 失败要先导出具体 QP Hessian**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：按该线程的已复现流程，先切到受支持的 qpOASES_e 版本并保存失败周期的实际 QP，而不是只看 ACADO 的聚合 status。维护者用 `qpOASES_writeIntoFileM` 导出 300×300 Hessian，在 stand-alone qpOASES_e 重放后发现 QP 42/43 正常、QP 44 Hessian 非正定且异常，Cholesky 因而失败；问题被转回 ACADO 构造侧。这个结果只证明该实例，不代表所有 internal error 都由 Hessian 非正定造成。
- 证据状态：`issue_candidate`
- 来源定位：qpOASES #50 维护者复现与 QP 42/43/44 诊断 589978804
- 原帖/精确回复：[ACADO 内嵌 qpOASES Cholesky 失败要先导出具体 QP Hessian](https://github.com/coin-or/qpOASES/issues/50#issuecomment-589978804)
- 平台/作者：GitHub Issues / yutaochen（Trac 迁移记录）
- 关键术语：乔列斯基分解（Cholesky decomposition）；海森矩阵（Hessian matrix）；非正定（non-positive-definite）；独立重放（stand-alone replay）
- 环境：ACADO code generation；最初使用 qpOASES 1.3，随后切换 qpOASES_e 3.1.1；QP 规模 300×300。
- 症状：旧版本显示 error 31（Cholesky decomposition failure）；切新版本后 ACADO 返回 -1 或 -2。
- 诊断：用 `qpOASES_writeIntoFileM(acadoWorkspace.H, 300, 300, ...)` 导出逐周期 Hessian 和 QP 数据，再在 stand-alone qpOASES_e 重放。
- 原因：维护者在收到的数据上复现：QP 44 Hessian 非正定且外观异常，Cholesky 相应失败；判断更可能是 ACADO 构造问题。
- 处理过程：开启 Levenberg-Marquardt regularization；切换到 qpOASES_e 3.1.1；提供 ACADO 导出代码和数据。
- 有效处理：线程没有给出 ACADO 侧最终修复；有效做法是导出失败周期的实际 QP，stand-alone 重放并把异常 Hessian 交给上游生成器定位。
- 结果：维护者独立重放 QP 42/43/44，确认失败随 QP 44 数据而来，qpOASES 侧记录为 wontFix 并建议联系 ACADO。
- 限制：该根因只对应作者提供的 QP 44；其他 Cholesky failure 仍可能来自不同的非正定、数值尺度或数据损坏。
- 安全提示：不要在线上真机仅靠增大 LM regularization 掩盖异常 Hessian；先保存故障周期并离线检查正定性和构造链。
- 独立核验引用：[independent_reproduction · 维护者收到导出代码后独立导出/重放 QP 42、43、44 并定位非正定 Hessian](https://github.com/coin-or/qpOASES/issues/50#issuecomment-589978804)
- 适用边界：直接适用于该 ACADO/qpOASES codegen 实例；方法可迁移，但每个故障周期的根因必须独立重放。

### 每次 qpOASES hotstart 前重置 nWSR 预算

- `problem_id`：`problem.optimization_ik_qp_mpc.qpoases_hotstart_nwsr_reset_83`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：qpOASES hotstart 循环中必须每次重置 nWSR**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：维护者说明 `nWSR` 不是只读上限，而是输入/输出参数：调用后它会带回实际或剩余的 working-set change 信息。若只在 for-loop 外初始化一次，后续调用继承的允许次数会单调减少，最终触发上限错误，并导致下一次提示 previous QP not solved。应在每次 `hotstart` 前重新赋值期望预算，并逐次检查返回码。该结论对应后续多次循环复现，不等于最初“第二次调用即失败”的报告已被完整复现。
- 证据状态：`issue_candidate`
- 来源定位：qpOASES #83 维护者最终解释 762053495
- 原帖/精确回复：[qpOASES hotstart 循环中必须每次重置 nWSR](https://github.com/coin-or/qpOASES/issues/83#issuecomment-762053495)
- 平台/作者：GitHub Issues / lrjcool（Trac 迁移记录）
- 关键术语：热启动（hot start）；输入输出参数（input/output parameter）；工作集重计算（working-set recalculation）；迭代预算（iteration budget）
- 环境：原帖 qpOASES 3.2.1；后续复现 Ubuntu 16.04、qpOASES 3.2.1、Bazel 0.18.1。
- 症状：前两三个 QP 正常，随后出现 maximum number of working set recalculations；再后续提示 previous QP is not solved。
- 诊断：在每次调用前后打印 `nWSR`，确认调用是否把它改写；同时检查错误发生后 solver 状态。
- 原因：维护者确认 `nWSR` 是 input/output parameter，外层只初始化一次会使下一次调用继承较小的剩余值。
- 处理过程：把 `nWSR` 定义或重新赋值放到每次 `hotstart` 的循环体内。
- 有效处理：每个控制周期在调用 `hotstart` 前重新设置期望的最大 `nWSR`；不要把上次输出值直接作为下次预算。
- 结果：另一用户给出 workaround，维护者补充了参数语义和为何会单调减少；原始 Issue 仍 open。
- 限制：最初的第二次调用问题在 trunk 上不可复现；明确闭环的是“多次循环复用 nWSR”这一后续场景。
- 安全提示：实时循环还应检查每次返回码；一旦 previous QP 未 solved，不要继续把旧控制量当成新有效解。
- 独立核验引用：[maintainer_confirmation · 维护者明确 `nWSR` 为 input/output 并要求每次 hotstart 前重置](https://github.com/coin-or/qpOASES/issues/83#issuecomment-762053495)
- 适用边界：适用于 qpOASES 3.2.1 中把 `nWSR` 复用于连续 hotstart 的循环；其他 API 版本需核对参数语义。

### 正确编码 OSQP C 接口的无穷边界

- `problem_id`：`problem.optimization_ik_qp_mpc.osqp_c_infinity_bound_43`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OSQP C 接口的一侧无穷边界必须使用 OSQP_INFTY**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：该线程的直接原因是示例使用了 OSQP 项目未定义的 `INFINITY` 宏。维护者要求改用 `glob_opts.h` 中的 `OSQP_INFTY`，原作者确认替换后不可行问题可以正确处理。工程上还应打印最终传入的 `l/u`，因为不同 OSQP 大版本可能调整公开头文件或常量位置。
- 证据状态：`issue_candidate`
- 来源定位：OSQP #43 维护者回复 364638732；作者确认 364714680
- 原帖/精确回复：[OSQP C 接口的一侧无穷边界必须使用 OSQP_INFTY](https://github.com/osqp/osqp/issues/43#issuecomment-364714680)
- 平台/作者：GitHub Issues / hongkai-dai
- 关键术语：单侧边界（one-sided bound）；无穷常量（infinity constant）；不可行检测（infeasibility detection）；迭代上限（iteration limit）
- 环境：2018 年 OSQP C 示例；原帖基于 `examples/osqp_demo.c` 修改，未给发布版本号。
- 症状：使用 `INFINITY` 时简单不可行 QP 达到迭代上限并持续增加 penalty；把上界改成有限值时能立即检测不可行。
- 诊断：打印实际传入 `l/u` 的数值和类型，确认使用目标 OSQP 版本定义的无穷常量。
- 原因：维护者确认 `INFINITY` 不是 OSQP 项目定义的宏，C 接口应使用 `OSQP_INFTY`。
- 处理过程：将通用 `INFINITY` 替换为 `glob_opts.h` 定义的 `OSQP_INFTY`。
- 有效处理：在该 OSQP C 接口环境中用 `OSQP_INFTY` 表示单侧无穷 bound。
- 结果：原作者明确确认 `OSQP_INFTY` 解决问题。
- 限制：宏所在头文件和内部表示可能随 OSQP 大版本变化；应以目标版本 C API 为准，不把旧路径硬编码为永久接口。
- 安全提示：上线前用一个已知不可行和一个已知可行的边界测试校验 bound 编码，避免控制循环在故障状态耗尽迭代预算。
- 独立核验引用：[maintainer_confirmation · 维护者指定 `OSQP_INFTY`；下一条评论由原作者确认](https://github.com/osqp/osqp/issues/43#issuecomment-364638732)
- 适用边界：直接适用于该线程的 OSQP C 接口；其他版本需核对对应 C API 常量。

### 联合检查 OSQP 的问题尺度与终止容差

- `problem_id`：`problem.optimization_ik_qp_mpc.osqp_conditioning_tolerance_53`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OSQP 与 CVXOPT 解差异先量化条件数和终止容差**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：不能。维护者在作者提交的数据上测得 `cond(P)≈9.86×10^6`，并说明 OSQP 的启发式缩放未必能完全修复病态问题；一阶方法的默认容差也比对照 solver 松。线程中的实验路径是收紧 `eps_abs/eps_rel` 到 `1e-9` 并视需要提高 `max_iter`。作者没有回报最终结果，因此这是一条有数据支撑的诊断经验，不是通用参数答案。
- 证据状态：`issue_candidate`
- 来源定位：OSQP #53 维护者附件诊断与完整代码 375153096
- 原帖/精确回复：[OSQP 与 CVXOPT 解差异先量化条件数和终止容差](https://github.com/osqp/osqp/issues/53#issuecomment-375153096)
- 平台/作者：GitHub Issues / yasseryasaei
- 关键术语：条件数（condition number）；内部缩放（internal scaling）；绝对容差（absolute tolerance）；相对容差（relative tolerance）
- 环境：macOS High Sierra 10.13.3、Python 3.6、OSQP 0.3.0；作者提交了简化数据和 notebook。
- 症状：OSQP 与 CVXOPT/CVXPY-ECOS 的解和目标值显著不同；最初还被描述为循环中非确定失败。
- 诊断：先计算 Hessian/约束的条件数和尺度范围，再比较各 solver 的绝对、相对终止容差，而不是只比较 status。
- 原因：维护者对附件计算得到 `cond(P)=9,860,981.74`，认为病态尺度与 OSQP 默认较松容差共同解释差异。
- 处理过程：维护者给出 `eps_abs=1e-9, eps_rel=1e-9` 的完整代码，并提醒可能需要提高 `max_iter`。
- 有效处理：没有作者确认的最终修复；紧容差和预缩放只能作为目标数据上的验证步骤。
- 结果：维护者在附件上得到更接近的结果；Issue 因一个月无后续关闭。
- 限制：原帖没有报告新迭代数、误差或循环随机失败是否同时消失；不能把 `1e-9` 写成通用 WBC 配置。
- 安全提示：真机控制应同时设置求解时限和残差门槛；不要为了追求跨 solver 数值一致而无界增加迭代。
- 独立核验引用：[maintainer_confirmation · 维护者读取附件、计算条件数并给出可运行紧容差代码](https://github.com/osqp/osqp/issues/53#issuecomment-375153096)
- 适用边界：直接适用于 OSQP 0.3.0 与原帖病态 QP；其他问题应重新计算条件数和实时预算。

### 区分 OSQP 有限迭代收敛与严格可行

- `problem_id`：`problem.optimization_ik_qp_mpc.osqp_finite_feasibility_polish_97`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OSQP/ADMM 有限迭代不保证严格原始可行**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：不能。项目成员明确说明 ADMM 不保证有限步达到严格可行点；OSQP 只按残差容差终止。polishing 成功时会基于猜测的 active set 计算高精度解，但并不保证成功。原作者最终把 primal/dual residual 降到约 `5e-10` 并认为足够，polishing 仍失败。工程上应按应用复算约束残差并设置上层安全门槛，而不是把 `solved` 等同于零残差。
- 证据状态：`issue_candidate`
- 来源定位：OSQP #97 有限步回答 427692913；作者最终结果 427903194
- 原帖/精确回复：[OSQP/ADMM 有限迭代不保证严格原始可行](https://github.com/osqp/osqp/issues/97#issuecomment-427903194)
- 平台/作者：GitHub Issues / qnzhou
- 关键术语：原始可行性（primal feasibility）；交替方向乘子法（Alternating Direction Method of Multipliers, ADMM）；解抛光（solution polishing）；活动集（active set）
- 环境：作者最终测试：209 variables、288 constraints、部分 equality、`P=0` 的 LP；未给 OSQP 发布版。
- 症状：正常求解总有非零 primal residual；polishing 在作者问题上一直不成功。
- 诊断：同时观察 primal/dual residual、polishing status、迭代数和 active-set 是否稳定；不要只读 `solved`。
- 原因：项目成员说明 ADMM 的可行性残差只在极限中趋零；polishing 失败表示 active-set 猜测未成功或问题可能不可行。
- 处理过程：作者极端收紧容差、减小 `rho`、设 `max_iter=1e7` 和 `polish_refine_iter=1e7`；维护者指出后两项设置不合理。
- 有效处理：没有严格有限步保证；按目标误差设置可审计的 primal/dual residual 门槛，polishing 成功时采用其高精度解，失败时保留原解并执行上层安全策略。
- 结果：作者最终得到 primal/dual residual 约 `5e-10`，认为已足够并关闭 Issue；polishing 仍未成功。
- 限制：不能从该 LP 的 `5e-10` 推导所有 WBC 的安全阈值；线程也没有给 active-set method 的统一替换方案。
- 安全提示：对硬件关键约束，应在 solver 外复算 `l≤Ax≤u` 和执行限幅/降级，不把 `solved` 当成零残差证明。
- 独立核验引用：[maintainer_confirmation · 项目成员说明有限步无严格可行保证与 polishing 语义](https://github.com/osqp/osqp/issues/97#issuecomment-427692913)
- 适用边界：适用于 ADMM/OSQP 的有限迭代解读；具体残差阈值必须按 WBC 约束尺度制定。

### 避免用大有限数替代 OSQP 无穷边界

- `problem_id`：`problem.optimization_ik_qp_mpc.osqp_finite_surrogate_infinity_109`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：用 -1000 代替 -inf 会把 OSQP inequality 改成另一个 QP**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：因为这会改变可行域。该线程中维护者验证 OSQP 的不可行证书成立，并发现 quadprog 的 `x` 对 OSQP 输入有 `min(Ax-l)=-219.2470` 的违反。原作者随后确认 inequality lower bound 被写成 `-1000`，而不是 `-inf`/`-OSQP_INFTY`；改成真正无下界后问题解决。比较 solver 前必须先证明两边实际接收的是同一个 `l≤Ax≤u`。
- 证据状态：`issue_candidate`
- 来源定位：OSQP #109 证书核对 442394129；作者根因与修复 442778706
- 原帖/精确回复：[用 -1000 代替 -inf 会把 OSQP inequality 改成另一个 QP](https://github.com/osqp/osqp/issues/109#issuecomment-442778706)
- 平台/作者：GitHub Issues / GiulioRomualdi
- 关键术语：不可行证书（infeasibility certificate）；可行域（feasible region）；有限替代边界（finite surrogate bound）；无穷边界（infinite bound）
- 环境：OSQP 0.4.1 MATLAB interface；64 variables、82 constraints；对照 MATLAB quadprog。
- 症状：OSQP 50 iterations 报 primal infeasible，quadprog 报 constraints satisfied。
- 诊断：验证 OSQP 的 `prim_inf_cert` 条件，并把对照 solver 的 `x` 代回同一 `l≤Ax≤u` 逐项检查。
- 原因：作者最终确认把不存在的下界编码为 `-1000`，而非真正的 `-inf`，两 solver 实际没有被同样约束。
- 处理过程：维护者计算不可行证书并验证 quadprog 解违反 OSQP 下界；作者随后检查建模代码。
- 有效处理：对无下界的 inequality 使用接口支持的 `-inf` 或 C 端 `-OSQP_INFTY`，不要用任意“大负数”代替。
- 结果：原作者明确说明改用 `-inf` 后问题解决。
- 限制：该结论只对应这次建模差异；若两个接口逐元素输入一致，仍需检查缩放、容差和 solver bug。
- 安全提示：发布前保存规范化 QP 数据并让两个接口逐元素校验，避免单位变化后有限 surrogate bound 进入真实可达区间。
- 独立核验引用：[maintainer_confirmation · 维护者核验 infeasibility certificate 并将 quadprog 解代回同一 constraints](https://github.com/osqp/osqp/issues/109#issuecomment-442394129)
- 适用边界：适用于用有限 surrogate 编码无边界的 OSQP/跨 solver 对照；数值范围不同也应重复检查。

### 区分 OSQP 解容差与不可行证书容差

- `problem_id`：`problem.optimization_ik_qp_mpc.osqp_solution_vs_infeasibility_tolerance_125`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OSQP 约束精度不能用 eps_prim_inf 调节**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：不应该。维护者说明 `eps_prim_inf` 控制 primal infeasibility certificate 检查，不控制正常 `solved` 解的残差。对作者提供的 OSQP 0.5.0 数据，把 `eps_abs`、`eps_rel` 调为 `1e-6` 后，约束违反从约 `10^-3` 降到 `10^-12` 量级，同时迭代从 25 增至 125。实际 WBC 必须按自身尺度和周期预算选择容差。
- 证据状态：`issue_candidate`
- 来源定位：OSQP #125 维护者参数解释、附件复跑与结果 479371495
- 原帖/精确回复：[OSQP 约束精度不能用 eps_prim_inf 调节](https://github.com/osqp/osqp/issues/125#issuecomment-479371495)
- 平台/作者：GitHub Issues / avikde
- 关键术语：原始不可行容差（primal infeasibility tolerance）；绝对终止容差（absolute termination tolerance）；相对终止容差（relative termination tolerance）；约束违反（constraint violation）
- 环境：OSQP 0.5.0 Python；46 variables、82 constraints；作者提供 `P/A/q/l/u` 最小数据。
- 症状：默认 `eps_abs=1e-3, eps_rel=1e-4` 时，两个方向 constraint violation 约 `-0.00185/-0.00252`，大于 `1e-4` 控制限。
- 诊断：区分 infeasibility certificate tolerance 与 solved residual termination tolerance；直接复算 `Ax-l`、`u-Ax`。
- 原因：维护者确认参数语义混淆：`eps_prim_inf` 只用于 primal infeasibility 检查。
- 处理过程：维护者对同一附件改为 `eps_abs=eps_rel=1e-6`。
- 有效处理：按问题尺度调小 `eps_abs/eps_rel`，并同时评估增加的迭代与实时预算。
- 结果：维护者实跑从 25 iterations 增至 125，constraint violation 降到约 `1e-12` 或更小。
- 限制：原作者没有另行复测；`1e-6` 只在该数据上被维护者验证，不是所有控制器的默认值。
- 安全提示：控制循环应在应用层复算约束，并把容差、最大迭代和 fallback 一起纳入时限设计。
- 独立核验引用：[official_documentation · 维护者回复直接链接的 OSQP convergence 文档](https://osqp.org/docs/solver/index.html#convergence)；[independent_reproduction · 维护者在作者附件上实跑 `eps_abs=eps_rel=1e-6` 并给出残差](https://github.com/osqp/osqp/issues/125#issuecomment-479371495)
- 适用边界：直接适用于 OSQP 0.5.0 原帖数据；参数语义可参考，目标数值需按版本和尺度复测。

### 固定 OSQP codegen 的 adaptive-rho 更新间隔

- `problem_id`：`problem.optimization_ik_qp_mpc.osqp_codegen_adaptive_rho_interval_205`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OSQP MATLAB 与 codegen 对照应固定 adaptive_rho_interval**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：线程中的对照表明，默认 time-based adaptive `rho` 会因两条执行路径的墙钟时间不同而在不同迭代触发。关闭 adaptive rho 后，两者均在 1225 iterations 结束且残差一致；改用固定 `adaptive_rho_interval=25` 后，作者确认原始和简化问题都恢复一致。工程上应固定更新间隔并同步 generated workspace 的 `max_iter`，而不是把 25 当成所有 QP 的最优参数。
- 证据状态：`issue_candidate`
- 来源定位：OSQP #205 维护者 A/B 533609939；作者确认 534015433
- 原帖/精确回复：[OSQP MATLAB 与 codegen 对照应固定 adaptive_rho_interval](https://github.com/osqp/osqp/issues/205#issuecomment-534015433)
- 平台/作者：GitHub Issues / markosvec
- 关键术语：自适应罚参数（adaptive rho）；固定更新间隔（fixed update interval）；代码生成（code generation）；原始/对偶残差（primal/dual residuals）
- 环境：2019 OSQP MATLAB/codegen；作者提供原始数据、2–3 维简化 QP 和导出代码；未固定 release。
- 症状：MATLAB 约 350 iterations 解出；codegen 在 1000 达上限，解误差虽约 `1e-6`。
- 诊断：先让两条路径使用同一固定 `adaptive_rho_interval`，比较 primal/dual residual 和迭代数；同时核对 generated workspace 的 `max_iter`。
- 原因：维护者实测确认默认 time-based rho update 在两条路径的触发点不同。
- 处理过程：关闭 adaptive rho 时，两 solver 都在 1225 iterations 结束且残差一致；随后使用固定更新间隔。
- 有效处理：把 `adaptive_rho_interval` 设置为非零固定值，例如线程中验证的 25；不要用墙钟触发做可复现对照。
- 结果：原作者确认 `adaptive_rho_interval=25` 对原始与简化问题均有效。
- 限制：25 不是所有 QP 的最优 interval；该卡只确认固定 interval 消除了两路径触发差异。
- 安全提示：生成代码部署前应固定全部 solver settings，并对最坏迭代数和返回码做硬实时验收。
- 独立核验引用：[maintainer_confirmation · 维护者禁用 adaptive rho 后实测两条路径 1225 iterations、残差一致](https://github.com/osqp/osqp/issues/205#issuecomment-533609939)
- 适用边界：适用于 OSQP MATLAB/codegen 的自适应 rho 跨路径复现；其他接口需核对更新策略。

### 审计 OSQP 不可行证书 epsilon 符号的双向边界

- `problem_id`：`problem.optimization_ik_qp_mpc.osqp_infeasibility_epsilon_sign_255_485`
- 问题综合等级：**需要实际验证** — 不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。
- 经验数量：2（全部列出，不隐藏待验证或冲突来源）

**经验 1：OSQP 旧版不可行证书符号修复已合并但后来出现边界争议**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：Issue #255 与合并 PR #256 把旧版 certificate 判据中的负 epsilon 改为正 epsilon，并用独立的 `OSQP_DIVISION_TOL` 判断 certificate 向量非零；文档也对齐最终论文。该变更确实作为 `develop-0.x` 的正式修复合入。由于后来的 #485 报告正 epsilon 在 singleton feasible region 上可能产生反向误判，这张经验只证明历史合并与原 MRE，不证明判据覆盖所有退化边界。
- 证据状态：`issue_candidate`
- 来源定位：OSQP #255 维护者确认 639451057/639472858；合并 PR #256
- 原帖/精确回复：[OSQP 旧版不可行证书符号修复已合并但后来出现边界争议](https://github.com/osqp/osqp/issues/255#issuecomment-639472858)
- 平台/作者：GitHub Issues / bodono
- 关键术语：不可行证书（infeasibility certificate）；原始不可行容差（primal infeasibility tolerance）；严格不等式（strict inequality）；退化可行域（degenerate feasible region）
- 环境：2020 年 `develop-0.x` 分支；Issue 给出 CVXPY 标量 MRE，PR 给出直接 OSQP Python MRE。
- 症状：对任意 `eps_prim_inf` 都能构造一个间隔等于该 epsilon 的不可行标量问题，使旧条件无法给出 certificate。
- 诊断：对照代码、最终论文 Section 3.4 与当前 certificate inequality；保留退化/单点可行域回归集。
- 原因：维护者确认旧代码把 negativity test 写成负 epsilon，且用 `eps_*_inf` 自身判断 certificate 向量非零。
- 处理过程：PR #256 把 primal/dual 条件换成正 epsilon，并用 `OSQP_DIVISION_TOL` 处理零范数；同步文档。
- 有效处理：历史上升级到包含 merge commit `fad7cf2` 的 `develop-0.x` 修复旧版 non-detection；不能据此断言所有退化边界都正确。
- 结果：PR 已批准、合并；作者/维护者给出修复前失败的最小例。
- 限制：PR 没有在可见 diff 中加入专门测试文件；#485 后来报告正 epsilon 对 singleton feasible region 的相反问题，本问题综合等级必须保留冲突。
- 安全提示：升级 solver 后同时测试明确 infeasible、普通 feasible 和 singleton/退化 feasible 三类 QP。
- 独立核验引用：[pull_request · 已批准并合并；merge `fad7cf2`，修改 primal/dual certificate inequality 与文档](https://github.com/osqp/osqp/pull/256)
- 适用边界：直接对应 2020 年 `develop-0.x` 修复；后续版本和 singleton feasible case 必须与 #485 一并验证。

**经验 2：OSQP 正 epsilon 不可行判据在 singleton feasible case 上仍有公开争议**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突；当前仅形成问题线索。
- 解答状态：`conflicting`
- 候选解答：目前不能把它当作通用修复。#485 的数学质疑指出正 epsilon check 可能接受 `lhs=0` 的 certificate，两位用户报告 singleton case，第二位本地改符号后成功；但没有完整公开 MRE或维护者确认。直接改回负号又可能重新引入 #255 已正式修复的“小间隔不可行问题无法终止”。应把两类 QP 放进同一回归集，并在维护者/正式补丁出现前保持 `conflicting`。
- 证据状态：`issue_candidate`
- 来源定位：OSQP #485 原始数学质疑；第二用户 A/B 2533462232；未解决状态 2537174191
- 原帖/精确回复：[OSQP 正 epsilon 不可行判据在 singleton feasible case 上仍有公开争议](https://github.com/osqp/osqp/issues/485#issuecomment-2537174191)
- 平台/作者：GitHub Issues / forrestlaine
- 关键术语：单点可行域（singleton feasible region）；不可行证书（infeasibility certificate）；假阳性（false positive）；回归测试集（regression test suite）
- 环境：Issue 固定到 commit `5dab81d` 的 `src/auxil.c`；第二用户固定到 commit `e5f1e50`；未给完整 QP MRE。
- 症状：两位用户报告 singleton feasible region 被判 primal infeasible；第二位称改 epsilon 符号后找到解。
- 诊断：对退化 QP 同时验证 certificate 的严格数学条件、返回 `v`、已知 singleton 点和不同 epsilon 符号的 A/B。
- 原因：作者认为 `lhs < +eps·||v||` 允许 lhs 为零，可能放宽到错误 certificate；维护者未确认。
- 处理过程：一位作者愿提交 PR 但等待维护者解释；第二位用户本地改符号后报告可求得 singleton 解。
- 有效处理：没有已合并修复；本地改符号只是用户 A/B，且可能重新引入 #255 的 non-detection。
- 结果：截至采集时 Issue open、无人维护者答复；#255 与 #485 形成双向边界冲突。
- 限制：缺少公开完整 MRE、目标 release 和维护者结论；不能建议直接 revert PR #256。
- 安全提示：WBC solver 回归集必须同时包含 singleton feasible 与间隔很小的 infeasible QP；任一类型失败都应阻止升级。
- 独立核验引用：[conflict · PR #256 的正式正 epsilon 修复与本帖建议的反向符号直接冲突](https://github.com/osqp/osqp/pull/256)
- 适用边界：仅作为 singleton/退化可行域的问题线索；任何本地符号修改都必须同时回归 #255 的 infeasible MRE。

### 排查 OSQP 循环求解的迭代尖峰

- `problem_id`：`problem.optimization_ik_qp_mpc.osqp_max_iter_tolerance_scaling_276`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OSQP 周期性 max-iteration 先检查过紧容差和 Hessian 条件数**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：不能。维护者对单独数据用默认 setup 在 75 iterations 解出；作者后来披露线上把 `eps_abs/eps_rel` 设为 `1e-8`。维护者建议对 ADMM 使用约 `1e-4` relative tolerance，作者确认有帮助，并补充还必须缩放 condition number 很大的 `P`。原帖没有验证 warm-start 污染，也没有给修正后的最坏时延，因此只能采用“容差＋尺度”的已确认缓解。
- 证据状态：`issue_candidate`
- 来源定位：OSQP #276 配置 719565150；维护者建议 721814742；作者确认 725366350
- 原帖/精确回复：[OSQP 周期性 max-iteration 先检查过紧容差和 Hessian 条件数](https://github.com/osqp/osqp/issues/276#issuecomment-725366350)
- 平台/作者：GitHub Issues / Ajin2305
- 关键术语：最大迭代（maximum iterations）；热启动（warm start）；问题缩放（problem scaling）；最坏执行时间（worst-case execution time, WCET）
- 环境：2020 OSQP MATLAB 与生成 MEX；实际设置 `eps_abs=eps_rel=1e-8`、`adaptive_rho_interval=25`、`max_iter=20000`。
- 症状：部分周期运行时大幅增加并返回 maximum iterations；单独重放一个数据却 75 iterations 解出。
- 诊断：记录每周期 QP、warm-start state、容差和 `cond(P)`；先对单独数据用默认设置复现，再逐项恢复线上配置。
- 原因：维护者最终把极严 `1e-8` 容差列为主要原因；作者另确认 `P` 条件数巨大并需要缩放。
- 处理过程：放宽 relative tolerance 到约 `1e-4`；缩放问题以处理 `P` 的巨大 condition number。
- 有效处理：作者确认两项都有帮助，但没有发布新状态分布或最坏运行时，因此登记为环境内缓解。
- 结果：作者回复“does help”，同时说明还必须缩放 `P`；Issue 随后关闭。
- 限制：最初关于坏 warm start 的猜测没有被作者确认；没有曲线后的精确尖峰率或实时保证。
- 安全提示：必须设置 solver deadline 和 fallback；容差放宽前先定义允许的约束残差，而不是只优化速度。
- 图片分析：原帖两张图只显示循环运行时间尖峰与 status 2/-2 的出现位置；图中缺少足够轴信息，未用于推断根因。
- 独立核验引用：[maintainer_confirmation · 维护者明确指出 `1e-8` 对 ADMM 极严并建议约 `1e-4`](https://github.com/osqp/osqp/issues/276#issuecomment-721814742)
- 适用边界：适用于原帖极严容差和病态 `P`；其他周期尖峰需保存具体 QP 与 solver state。

### 保持 OSQP 在线矩阵更新的稀疏结构不变

- `problem_id`：`problem.optimization_ik_qp_mpc.osqp_update_sparsity_pattern_376`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OSQP update 只能改已有稀疏结构中的非零值**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：不能。维护者说明 setup 与 update 后的 `P/A` 必须具有相同 sparsity pattern；value-only update 不能从全零结构创建新 nonzeros。MATLAB 线程还要求 `Ax=nonzeros(A)` 按列主序，`Px=nonzeros(triu(P))` 只传对称 `P` 上三角。维护者给出完整工作代码，作者确认问题来自自己的更新方式。
- 证据状态：`issue_candidate`
- 来源定位：OSQP #376 维护者格式 998756951、工作代码 998793473；作者确认 998794367
- 原帖/精确回复：[OSQP update 只能改已有稀疏结构中的非零值](https://github.com/osqp/osqp/issues/376#issuecomment-998794367)
- 平台/作者：GitHub Issues / epsonlq138
- 关键术语：稀疏结构（sparsity pattern）；压缩稀疏列（Compressed Sparse Column, CSC）；上三角（upper triangular）；数值更新（value-only update）
- 环境：OSQP 0.6.2 MATLAB；258 variables、258 constraints。
- 症状：直接 setup 在 275 iterations `solved`；零矩阵 setup 后 update 在 25 iterations 报 dual infeasible。
- 诊断：比较 setup/update 的 CSC sparsity pattern、nonzero 个数和顺序；检查 `P` 是否只传 upper triangle。
- 原因：维护者确认 update 只替换既有 nonzeros；全零 setup 没有为后续 `P/A` 建立结构。
- 处理过程：setup 时先用目标 `P/A` 结构和零 `q/l/u`，update 时传 `nonzeros(triu(P))` 与 `nonzeros(A)`。
- 有效处理：固定可覆盖所有运行模式的 sparsity pattern 后只更新值；如果 pattern 真要变化，重新 setup solver。
- 结果：维护者代码按预期工作；原作者确认是自己的错误。
- 限制：该线程只覆盖 MATLAB 0.6.2 update API；其他语言的索引更新能力需读目标版本接口。
- 安全提示：接触模式变化前后应断言 nonzero pattern hash；模式未覆盖时宁可重新 setup，也不要继续使用旧结构。
- 独立核验引用：[official_documentation · 维护者直接链接的 OSQP MATLAB matrix update 示例](https://osqp.org/docs/examples/update-matrices.html#matlab)
- 适用边界：直接适用于 OSQP 0.6.2 MATLAB update；其他接口需核对是否支持 indexed pattern update。

### 校验 cuOSQP 单精度边界转换

- `problem_id`：`problem.optimization_ik_qp_mpc.cuosqp_float_bound_cast_nan_424`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：cuOSQP 首迭代 NaN 要检查 l/u 的 double→float Inf 转换**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：该线程中矩阵和 CUDA demo 最终都被排除；原作者发现 `l/u` 从 double 转成 float 后含 NaN/Inf，Inf cast 也会让 cuOSQP 输出 NaN。把应用改成全 float 后原始问题解决。因此应在 `osqp_setup` 前检查目标 dtype 中全部 `P/q/A/l/u`，尤其 bounds 的 finite/无穷编码。线程没有解决后续 CPU/GPU 解差异和迭代慢，不能把全 float 当成完整性能修复。
- 证据状态：`issue_candidate`
- 来源定位：OSQP #424 作者最终根因与修复 1153368937
- 原帖/精确回复：[cuOSQP 首迭代 NaN 要检查 l/u 的 double→float Inf 转换](https://github.com/osqp/osqp/issues/424#issuecomment-1153368937)
- 平台/作者：GitHub Issues / gacamilo
- 关键术语：单精度（single precision）；类型转换（type cast）；非数值（Not a Number, NaN）；线性系统零主元（zero pivot）
- 环境：cuOSQP/OSQP C interface，CUDA 11.6，Visual Studio；MPC 目标 100 Hz；未给 release。
- 症状：CPU OSQP 正常，cuOSQP 从第一迭代 objective/solution 即 NaN；官方 CUDA PCG demo 在同一应用中正常。
- 诊断：逐元素比较 CPU/GPU 的 `P/q/A/l/u` 在最终 dtype 中的值、finite 状态和无穷编码；不要只比较源 double 数据。
- 原因：原作者最终确认 `l/u` 的 double→float 转换产生 NaN/Inf，并触发 NaN 输出。
- 处理过程：对比 `P/A`、令 `P=0`、运行 2×2/demo、检查 GPU 配置；最后改成全 float 数据路径。
- 有效处理：在进入 cuOSQP 前使用目标 float 类型构造 bounds，并显式检查 `isfinite`/允许的无穷表示。
- 结果：作者确认全 float 修改解决原始 NaN；但 CPU/GPU 解不同与 cuOSQP 数千迭代仍待继续排查。
- 限制：不能把所有 GPU NaN 都归因于 bounds cast；原帖剩余性能与解差异没有闭环。
- 安全提示：真机前对每周期 QP 全字段做 finite 检查；GPU solver 返回 NaN 时必须拒绝控制量并进入安全 fallback。
- 图片分析：原帖截图只显示 cuOSQP 首迭代出现 NaN；根因来自后续文字复查 `l/u`，未从截图推断。
- 独立核验引用：[maintainer_confirmation · 项目成员给出 C 接口矩阵/首迭代线性求解的诊断边界；作者最终定位 bounds](https://github.com/osqp/osqp/issues/424#issuecomment-1148438546)
- 适用边界：适用于 cuOSQP 单精度数据路径和含无穷 bounds 的 MPC；其他 GPU backend 需核对自身类型。

### 解释并复核 OSQP 非负约束下的负残差

- `problem_id`：`problem.optimization_ik_qp_mpc.osqp_nonnegative_relative_residual_609`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：OSQP 非负约束下的小负值由相对残差尺度决定**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：只能作为有条件的后处理。项目成员说明 OSQP 按 `eps_abs + eps_rel·max(||Ax||,||z||)` 判断 residual，问题尺度达到数千时，小负值仍可能满足相对准则；负元素个数不是终止指标。对独立 `x≥0` 分量向上截到 0 很直观，但如果同一变量还参与一般 `Ax≤b`，clamp 可能制造新的违反。原作者收紧到 `1e-7`、polishing 失败后仍有约 `-1e-4`，所以必须在后处理后复算全部约束。
- 证据状态：`issue_candidate`
- 来源定位：OSQP #609 convergence 解释 1979012199；clamp 边界 1980361325；作者紧容差结果 1980277232
- 原帖/精确回复：[OSQP 非负约束下的小负值由相对残差尺度决定](https://github.com/osqp/osqp/issues/609#issuecomment-1980361325)
- 平台/作者：GitHub Issues / baharehhj
- 关键术语：非负约束（non-negativity constraint）；相对残差（relative residual）；无穷范数（infinity norm）；后处理截断（post-solve clamping）
- 环境：OSQP 0.6.3、OSQP-Eigen C++；721 variables、2370 constraints、470615 nonzeros。
- 症状：`eps_abs=eps_rel=1e-5` 时出现到 `-0.0131` 的分量；`1e-7` 时仍约 100 个负数，最小约 `-1e-4`；polishing unsuccessful。
- 诊断：复算 infinity-norm residual 和 `||Ax||/||z||`，而不是只数负值个数；clamp 后重新检查全部 `l≤Ax≤u`。
- 原因：项目成员按论文 convergence equation 解释：相对项随大尺度 `Ax` 放大允许 residual。
- 处理过程：收紧 `eps_abs/eps_rel`、启用 polishing、与 quadprog 对照、询问将负值截为 0。
- 有效处理：没有保证严格非负的 solver-side 修复；可对独立 `x≥0` 分量 clamp，但必须重新验证其他一般线性约束和目标影响。
- 结果：作者在 `1e-7` 下减小了负值幅度但仍存在；polishing 未成功；线程以解释和 clamp 边界结束。
- 限制：不能把负值数量当成 solver 指标，也不能假设 clamp 后其他 constraints 仍满足。
- 安全提示：法向接触力等硬件关键量应在输出层限幅并复查耦合约束；不通过时触发降级而非继续执行。
- 独立核验引用：[paper · 项目成员直接引用 OSQP paper Section 3.4 / convergence equation](https://web.stanford.edu/~boyd/papers/pdf/osqp.pdf)
- 适用边界：适用于 OSQP 0.6.3 大尺度一般线性约束；严格安全阈值需按 WBC 单位和耦合关系制定。

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

### Crocoddyl 脚面不对齐世界坐标时需显式设置 wrench cone 旋转

- `problem_id`：`problem.force_control_manipulation.crocoddyl_wrench_cone_foot_rotation_880`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Crocoddyl 全身操作中 contact wrench cone 与足部旋转的配置选择**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：维护者只给出一个明确接口提示：wrench cone constructor 的第一个元素/参数定义其 rotation。线程没有给出旋转矩阵方向、参考系约定或复测代码，因此只能作为定位 API 的入口，不能仅凭配图直接构造矩阵。
- 证据状态：`issue_candidate`
- 来源定位：Crocoddyl #880：作者评论 722446675 提供足板图片并提问；维护者评论 771044606 指出 constructor 第一个参数定义旋转
- 原帖/精确回复：[Crocoddyl 全身操作中 contact wrench cone 与足部旋转的配置选择](https://github.com/loco-3d/crocoddyl/issues/880#issuecomment-771044606)
- 平台/作者：GitHub Issues / ddliu365
- 关键术语：旋转矩阵（rotation matrix）；世界坐标系（world frame）；支撑多边形（support polygon）；接触力矩锥（contact wrench cone）
- 环境：Crocoddyl whole_body_manipulation 示例，线程时间为 2020-10 至 2021-02；未给 Crocoddyl 版本或机器人型号。
- 症状：用户无法判断摩擦锥、CoP/ZMP 和 contact wrench cone 三类 cost 在高动态全身操作中的组合关系。；脚板带偏航角时，用户不清楚 wrench cone rotation matrix 如何定义。
- 诊断：按接触模型需要分别检查切向摩擦、CoP 支撑域与 yaw torque 边界，而不是只看到 friction cone 就认为有限足面稳定性完整。；核对 wrench cone 构造函数第一个旋转参数所使用的参考系，并让它与实际脚面方向一致。
- 原因：示例在 contact wrench cone 功能开发前编写，维护者说明这就是示例仍只用 friction cone 的原因，而不是表示 friction cone 已足够。
- 处理过程：作者查阅 contact wrench cone 论文，并向维护者确认其是否同时覆盖 friction、ZMP/CoP 和 yaw torque。；作者提供双脚不对齐世界坐标的图片，追问旋转矩阵。
- 有效处理：需要完整有限足面约束时使用 contact wrench cone，并移除单独的 friction cone 或 CoP cost，避免重复。；脚面不与世界坐标对齐时，通过 wrench cone constructor 的第一个参数指定其旋转。
- 结果：作者回复解释清楚，并表示会在方案工作后更新示例；线程没有后续实现或数值结果。；旋转参数问题只有维护者的一句接口说明，没有作者复测。
- 限制：线程没有给出 contact wrench cone 的具体 API 版本、矩阵方向约定或代码示例。；不能从足板图片直接推导旋转矩阵；必须回到目标版本构造函数和参考系定义。；该讨论来自 2020/2021 年，当前 Crocoddyl API 名称需要再次核对。
- 安全提示：高动态实机操作中应同时监控摩擦裕度、CoP 支撑域和 yaw torque；约束参考系错误可能产生看似可行但不可执行的接触力矩。
- 图片分析：评论 722446675 的图片已核验：左侧是双脚脚板照片，右侧示意图标注 Left foot、Right foot、support polygon、support polygon with margin 和 Δx_zmp，双脚明显不平行；图片支持“脚面不与同一世界方向对齐”的提问，但没有坐标轴或矩阵定义，不能用于推导旋转参数。
- 独立核验引用：[maintainer_confirmation · 维护者说明 wrench cone constructor 的第一个参数定义其旋转](https://github.com/loco-3d/crocoddyl/issues/880#issuecomment-771044606)
- 适用边界：适用于该线程时期 Crocoddyl wrench cone constructor；当前版本的参数类型、旋转方向和 frame convention 必须查源码/文档验证。

### Crocoddyl 全身操作不能只靠 friction cone 或 CoP 约束有限足面接触

- `problem_id`：`problem.force_control_manipulation.crocoddyl_wrench_cone_vs_friction_cop_880`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Crocoddyl 全身操作中 contact wrench cone 与足部旋转的配置选择**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：维护者明确回答：单独 friction constraint 不够，单独 CoP 也不够，需要 contact wrench cone。原作者把 wrench cone 理解为同时包含摩擦、ZMP/CoP 边界以及 yaw torque 边界，维护者确认正确。使用 wrench cone 时应移除单独的 friction cone 或 CoP cost；旧示例未集成它是因为示例早于该功能。
- 证据状态：`issue_candidate`
- 来源定位：Crocoddyl #880：维护者评论 718918420/718918724 给出结论；评论 719454648 确认作者理解并说明 cost 组合；作者 719600191 表示解释清楚
- 原帖/精确回复：[Crocoddyl 全身操作中 contact wrench cone 与足部旋转的配置选择](https://github.com/loco-3d/crocoddyl/issues/880#issuecomment-719454648)
- 平台/作者：GitHub Issues / ddliu365
- 关键术语：接触力矩锥（contact wrench cone）；摩擦锥（friction cone）；压力中心（center of pressure, CoP）；偏航力矩（yaw torque）
- 环境：Crocoddyl whole_body_manipulation 示例，线程时间为 2020-10 至 2021-02；未给 Crocoddyl 版本或机器人型号。
- 症状：用户无法判断摩擦锥、CoP/ZMP 和 contact wrench cone 三类 cost 在高动态全身操作中的组合关系。；脚板带偏航角时，用户不清楚 wrench cone rotation matrix 如何定义。
- 诊断：按接触模型需要分别检查切向摩擦、CoP 支撑域与 yaw torque 边界，而不是只看到 friction cone 就认为有限足面稳定性完整。；核对 wrench cone 构造函数第一个旋转参数所使用的参考系，并让它与实际脚面方向一致。
- 原因：示例在 contact wrench cone 功能开发前编写，维护者说明这就是示例仍只用 friction cone 的原因，而不是表示 friction cone 已足够。
- 处理过程：作者查阅 contact wrench cone 论文，并向维护者确认其是否同时覆盖 friction、ZMP/CoP 和 yaw torque。；作者提供双脚不对齐世界坐标的图片，追问旋转矩阵。
- 有效处理：需要完整有限足面约束时使用 contact wrench cone，并移除单独的 friction cone 或 CoP cost，避免重复。；脚面不与世界坐标对齐时，通过 wrench cone constructor 的第一个参数指定其旋转。
- 结果：作者回复解释清楚，并表示会在方案工作后更新示例；线程没有后续实现或数值结果。；旋转参数问题只有维护者的一句接口说明，没有作者复测。
- 限制：线程没有给出 contact wrench cone 的具体 API 版本、矩阵方向约定或代码示例。；不能从足板图片直接推导旋转矩阵；必须回到目标版本构造函数和参考系定义。；该讨论来自 2020/2021 年，当前 Crocoddyl API 名称需要再次核对。
- 安全提示：高动态实机操作中应同时监控摩擦裕度、CoP 支撑域和 yaw torque；约束参考系错误可能产生看似可行但不可执行的接触力矩。
- 图片分析：评论 722446675 的图片已核验：左侧是双脚脚板照片，右侧示意图标注 Left foot、Right foot、support polygon、support polygon with margin 和 Δx_zmp，双脚明显不平行；图片支持“脚面不与同一世界方向对齐”的提问，但没有坐标轴或矩阵定义，不能用于推导旋转参数。
- 独立核验引用：[maintainer_confirmation · 维护者明确说明 friction constraint 和 CoP 单独都不够，需要 contact wrench cone](https://github.com/loco-3d/crocoddyl/issues/880#issuecomment-718918420)；[maintainer_confirmation · 维护者确认作者对 wrench cone 的理解，并要求移除单独 friction cone 或 CoP cost](https://github.com/loco-3d/crocoddyl/issues/880#issuecomment-719454648)
- 适用边界：适用于有限足面 whole-body manipulation 的接触稳定性建模；当前 Crocoddyl API 和约束维度需按目标版本核对。

### Pinocchio 阻抗控制的末端 wrench 与 LOCAL Jacobian 坐标系对齐

- `problem_id`：`problem.force_control_manipulation.pinocchio_end_effector_wrench_frame_1779`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 阻抗控制中的末端 wrench 必须与 LOCAL Jacobian 使用同一坐标系**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：getFrameJacobian(..., LOCAL) 已考虑 frame 相对 parent joint 的 placement，并把 Jacobian 表达在末端 frame。wrench 若已在同一 LOCAL frame，无需变换；若按原回复的特定约定，它表达在世界原点且轴与世界坐标对齐，可用 data.oMf\[frame_id\].actInv(wrench) 转到末端 LOCAL。原作者确认该回答足够。对于不同作用点或其他库的 wrench 约定，必须重新核对，不能把这一行代码当作无条件通用公式。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1779 评论 1290530047 解释 LOCAL Jacobian 与 frame placement；评论 1290556806 给出 wrench 变换；评论 1290559993 原作者确认
- 原帖/精确回复：[Pinocchio 阻抗控制中的末端 wrench 必须与 LOCAL Jacobian 使用同一坐标系](https://github.com/stack-of-tasks/pinocchio/issues/1779#issuecomment-1290556806)
- 平台/作者：GitHub Issues / Betancourt20
- 关键术语：阻抗控制（impedance control）；力旋量（wrench）；末端执行器（end effector）；局部坐标系（local frame）；雅可比转置映射（Jacobian-transpose mapping）
- 环境：Kinova Jaco、Pinocchio Python；原帖未给 OS、Pinocchio 版本、URDF commit 或控制周期。
- 症状：机械臂会运动，但方向/行为与机器人文档描述不一致；原作者怀疑 force/wrench 位于错误 frame。
- 诊断：确认 getFrameJacobian 的 reference frame，并显式记录 wrench 的表达坐标系和作用点。；不要重复应用 frame-to-parent 偏置；LOCAL Jacobian 已把 frame placement 纳入计算。
- 原因：原实现把 LOCAL Jacobian 与未明确表达 frame 的 wrench 组合，坐标约定没有对齐。
- 处理过程：原作者曾按 MATLAB Robotics System Toolbox 示例尝试 frame 变换，但没有成功。；维护者先澄清 frame placement/Jacobian 语义，再按 wrench 已在 LOCAL 或位于世界原点且 world-aligned 两种情况给出处理。
- 有效处理：wrench 已表达在末端 LOCAL frame 时不变换；若按原线程限定，wrench 位于世界原点且轴与世界坐标对齐，则用 data.oMf\[frame_id\].actInv(wrench) 转到该 frame 的 LOCAL 表达。
- 结果：原作者回复该解释完全足够并同意关闭 Issue。
- 限制：本线程只覆盖维护者明确描述的 wrench 表达和作用点约定；其他作用点、传感器坐标系或库的 wrench action/dual-action 约定不能直接照抄。；线程没有发布修正后的轨迹、力矩曲线或实机稳定性结果。；回复中的变换应与目标 Pinocchio 版本的 Force/SE3 API 约定再次核对。
- 安全提示：在实机启用阻抗/外力控制前，用小幅静态 wrench 检查关节力矩符号、frame 和限幅，并配置急停；错误 frame 可直接反转期望力方向。
- 独立核验引用：[maintainer_confirmation · 维护者说明 LOCAL Jacobian 已纳入 frame placement 并表达在 frame LOCAL](https://github.com/stack-of-tasks/pinocchio/issues/1779#issuecomment-1290530047)；[issue · 原作者确认该回答完全足够](https://github.com/stack-of-tasks/pinocchio/issues/1779#issuecomment-1290559993)
- 适用边界：适用于 Pinocchio Python 中末端 frame LOCAL Jacobian，以及原回复明确描述的世界原点/world-aligned wrench；不同作用点和 API 版本需验证。

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

### Franka JointVelocityAction 的版本化增益配置

- `problem_id`：`problem.hardware_actuator_thermal.franka_joint_velocity_action_2807`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Franka JointVelocityAction 的可用配置依赖 Isaac Lab 版本与执行器参数**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：一位用户在 IsaacLab 1.4.1、IsaacSim 4.2.0 的 PPO reach 任务中使用 stiffness=0、damping=50、effort_limit=1e9，并把 JointVelocityAction 设为 scale=1、use_default_offset=True；他报告可以直接发送速度命令，并建议过快时限制 joint velocity。原作者的 2.1.0/4.5.0 环境没有复测这套配置，维护者也未确认它是框架通用解法；尤其 1e9 仅可视为仿真 workaround，绝不能用于实机限幅。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #2807 社区结果 3018405585 与精确配置 3026762388
- 原帖/精确回复：[Franka JointVelocityAction 的可用配置依赖 Isaac Lab 版本与执行器参数](https://github.com/isaac-sim/IsaacLab/issues/2807#issuecomment-3026762388)
- 平台/作者：GitHub Issues / EntangledQuantum
- 关键术语：关节速度动作（joint velocity action）；隐式执行器（implicit actuator）；重力补偿（gravity compensation）；力矩上限（effort limit）
- 环境：问题环境：Isaac Lab 2.1.0 commit 3d6f55b、Isaac Sim 4.5.0、Ubuntu 24.04.2、NVIDIA A10。；workaround 环境：IsaacLab 1.4.1、IsaacSim 4.2.0、PPO reach task；硬件细节未给。
- 症状：零或非零速度命令下，Franka 关节不稳定且不能按期望跟踪速度。
- 诊断：先记录 Isaac Lab/Isaac Sim 与 robot asset 精确版本，避免跨版本直接复制 actuator 配置。；检查 velocity action 下 implicit actuator 的 stiffness、damping、effort limit 和 joint velocity limit。
- 原因：原帖作者认为 position target 与重力补偿/增益设置共同导致异常；线程没有维护者确认这一因果。
- 处理过程：社区用户在旧版本中使用 stiffness=0、damping=50、effort_limit=1e9、JointVelocityAction scale=1，并建议必要时限制 joint velocity。
- 有效处理：该用户报告用上述配置完成 PPO reach 训练并可直接发送速度命令。
- 结果：社区用户环境中得到可用结果；原作者的 2.1.0/4.5.0 环境没有复测闭环。
- 限制：effort_limit=1e9 是仿真配置，不是实机安全参数。；旧版本的配置不能视为 Isaac Lab 2.1/Isaac Sim 4.5 或 5.0 的通用答案。；视频未用于本卡结论，结果只采用评论中的文字报告。
- 安全提示：禁止把 1e9 effort limit 迁移到实机；实机应使用厂家力矩/速度限制、急停和逐级增益测试。
- 独立核验引用：[issue · 同一用户用文字报告 PPO reach 的速度命令控制结果；本卡不依赖视频](https://github.com/isaac-sim/IsaacLab/issues/2807#issuecomment-3018405585)
- 适用边界：精确对应 IsaacLab 1.4.1/IsaacSim 4.2.0 的仿真 PPO reach；其他版本和实机必须重新验证。

### ros2_control 控制器同时激活的资源冲突早失败

- `problem_id`：`problem.hardware_actuator_thermal.ros2_control_activation_conflict_2758`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ros2_control 同时激活资源冲突控制器应在 mode switch 前失败**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：使用包含合并 PR #2760 的版本。该修复在实际 mode switch 前计算 deactivation 将释放的接口和 activation 将占用的接口；若接口当前仍被其他 controller claim，或本次 activation list 中重复占用，就直接返回 ERROR，不再进入会误停原接口的失败清理。PR 初版经原作者测试仍失败，修订后维护者跑过 UR tests，原作者确认 regression 修复并批准。硬件 prepare_switch 仍应保留自身互斥模式校验，但不应再承担 controller_manager 的资源所有权漏洞。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #2758 维护者确认 3462221412；PR #2760 修订后作者复测 3479240549；merge f8903b3
- 原帖/精确回复：[ros2_control 同时激活资源冲突控制器应在 mode switch 前失败](https://github.com/ros-controls/ros2_control/issues/2758#issuecomment-3471230616)
- 平台/作者：GitHub Issues / urfeex
- 关键术语：命令接口（command interface）；资源冲突（resource conflict）；命令模式切换（command mode switch）；提前失败（fail early）
- 环境：ros2_control 回归位于 PR #2669 之后；作者日志为 UR5e position/velocity modes；问题日期 2025-10；精确 ROS 2 发行版未给。
- 症状：第二个 position controller 激活失败后，perform_command_mode_switch 收到停止 position interfaces；硬件 position_control_active 被清除，随后可能错误允许 velocity controller。
- 诊断：构造两个控制器同时 claim 同一 command interface 的严格切换测试。；确认冲突是否在 non-realtime activation check 阶段返回，而不是进入 hardware perform_command_mode_switch 后才失败。；失败后断言原 active controller 和硬件 mode flag 保持不变。
- 原因：controller_manager 没有在同时 activation list 中提前检测 future command-interface 冲突，失败清理路径又执行了接口停止。
- 处理过程：作者临时在 hardware prepare_switch 中显式拒绝冲突。；PR #2760 增加 current/future claimed interface 检查、失败早返回和控制器冲突测试；根据作者初测失败继续修订并跑 UR 测试。
- 有效处理：采用已合并 PR #2760：在激活前同时考虑 deactivation 释放和 activation 未来占用，已被占用或本批次重复占用时直接返回 ERROR，不继续错误 mode switch。
- 结果：原作者在修订版 PR 上确认 regression 已修复；两位维护者批准，PR 合并。
- 限制：目标发行版是否包含 merge commit f8903b3 需核对。；修复针对 command interface 资源冲突，不替代硬件自身 position/velocity 兼容性校验。
- 安全提示：模式切换回归测试必须验证失败时旧控制器仍保持 active、硬件模式标志不变，并在实机使用低速、急停和隔离区。
- 独立核验引用：[pull_request · 已合并 PR 加入冲突预检查、早返回和双 controller 同接口回归测试；原作者复测通过](https://github.com/ros-controls/ros2_control/pull/2760)
- 适用边界：适用于包含 ros-controls/ros2_control PR #2760/merge commit f8903b3 的 controller_manager；发行版包需核对。

### ImplicitActuator 的 USD 力矩上限回退

- `problem_id`：`problem.hardware_actuator_thermal_power.isaaclab_implicit_actuator_usd_effort_limit_2054`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 隐式执行器未配置力矩上限时曾错误回退到 1e9**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：使用包含 PR #2098 的版本，并核对 actuator cfg、USD drive max_effort、asset.data.joint_effort_limits 与 PhysX 实际值。该 PR 修正 implicit/explicit 判断：implicit actuator 未显式给 limit 时继承 USD joint drive 的 max_effort；1e9 默认只保留给 explicit actuator 的 simulation effort limit。即使升级后也应显式审计 USD 数值，不能把继承行为直接视为实机安全配置。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #2054 复现 2721483228、维护者修复 2737536308；PR #2098
- 原帖/精确回复：[Isaac Lab 隐式执行器未配置力矩上限时曾错误回退到 1e9](https://github.com/isaac-sim/IsaacLab/issues/2054#issuecomment-2737536308)
- 平台/作者：GitHub Issues / Hellod035
- 关键术语：隐式执行器（implicit actuator）；力矩上限（effort limit）；仿真求解器上限（simulation solver limit）；关节 USD 驱动（USD joint drive）
- 环境：Isaac Sim 4.5、Ubuntu 22.04、RTX 4090D、CUDA 12.4、driver 550.144.03、IsaacLab latest（2025-03）。；复现任务包括 Isaac-Velocity-Flat-G1-v0 与 Legged Lab g1_flat。
- 症状：USD asset 显示正确 max force，但 asset.data.joint_effort_limits 为 1e9。
- 诊断：同时检查 actuator cfg 的 effort_limit/effort_limit_sim、USD drive max_effort、asset.data.joint_effort_limits 和 PhysX 实际上限。；区分 implicit actuator 与 explicit actuator 的默认行为。
- 原因：PR #2098 的源码说明：默认逻辑错误地通过 ActuatorBase 类属性判断 implicit/explicit，导致 implicit actuator 也进入 explicit actuator 的 1e9 分支。
- 处理过程：作者分别在官方 G1 与 Legged Lab G1 配置中注释 limit 后复现。；维护者修改默认判断并扩展 limits 单元测试。
- 有效处理：升级到包含 PR #2098 / merge commit d7da02d 的版本；implicit actuator 未配置 limit 时继承 USD max_effort，explicit actuator 的 solver effort 默认仍可保持 1e9。
- 结果：Issue 随 PR #2098 合并关闭；测试覆盖 implicit actuator 使用 USD limit、explicit actuator 1e9 默认和 actuator/simulation limit 分离。
- 限制：修复不等于推荐省略所有限制；不同 asset 的 USD max_effort 仍必须审计。；原帖截图未参与结论，结论来自文字复现、源码 diff 与测试。
- 安全提示：实机 WBC 不得把仿真 1e9 默认当作硬件允许力矩；部署前应显式设置厂家限制并验证最终下发裁剪。
- 图片分析：原帖 699×259 截图已在前轮读取：Isaac Sim 属性面板 Drive > Angular 显示 Type=force、Max Force=88.0、Target Position=0.0、Target Velocity=0.0、Damping=0.0、Stiffness=0.0；Python 侧 1e9 来自正文而非截图。
- 独立核验引用：[issue · 原作者在 Isaac Lab 与 Legged Lab 的 G1 任务中注释显式上限后均复现 1e9](https://github.com/isaac-sim/IsaacLab/issues/2054#issuecomment-2721483228)；[independent_reproduction · 另一使用者独立报告速度上限能读、力矩上限没有从 Isaac Sim 读取](https://github.com/isaac-sim/IsaacLab/issues/2054#issuecomment-2723958505)；[maintainer_confirmation · 维护者确认 PR #2098 为修复并扩展 effort/velocity limit 检查](https://github.com/isaac-sim/IsaacLab/issues/2054#issuecomment-2737536308)；[pull_request · 合并 PR 修复 implicit/explicit 默认判断并加入 effort/velocity limits 测试](https://github.com/isaac-sim/IsaacLab/pull/2098)；[source_code · PR #2098 合并提交](https://github.com/isaac-sim/IsaacLab/commit/d7da02da62b46153da3dc3e54585eea078e0d9cb)
- 适用边界：适用于 2025-03 修复前后 Isaac Lab implicit/explicit actuator limit 迁移；具体 USD 与 cfg 仍需逐 asset 核对。

### GO1 ActuatorNet 的训练与调用频率匹配

- `problem_id`：`problem.hardware_actuator_thermal.go1_actuator_net_rate_2963`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：GO1 ActuatorNet 训练采样率与仿真调用率不一致仍未闭环**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突。
- 解答状态：`unresolved`
- 候选解答：帖子只验证了调用事实，尚未给出修复结论。作者在 ActuatorNetMLP.compute 和 environment step 中加日志，在官方 GO1 rough task 中观察到网络每个 physics step 调用，并报告每个 policy step 共五次。团队没有回答应该每四步调用一次、保持输出，还是用 200Hz 数据重训，也没有实机结果。因此可复用动作是先对目标版本做同样的调用计数并记录 model training dt；具体频率策略仍需在仿真和实机上实际验证。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #2963 作者 instrumentation 3089324868、官方任务命令 3131807994、团队转 Discussion 3193574728
- 原帖/精确回复：[GO1 ActuatorNet 训练采样率与仿真调用率不一致仍未闭环](https://github.com/isaac-sim/IsaacLab/issues/2963#issuecomment-3089324868)
- 平台/作者：GitHub Issues / ammousa
- 关键术语：执行器网络（actuator network）；仿真步（simulation step）；降采样系数（decimation）；采样率不匹配（sampling-rate mismatch）
- 环境：Isaac Lab 官方 managed environment：Isaac-Velocity-Rough-Unitree-Go1-v0；帖子未给精确 commit、Isaac Sim 版本或硬件。；作者报告 policy rate 50Hz、decimation=4、actuator compute 约 200Hz。
- 症状：instrumentation 显示 actuator network 在每个 sim step 推理，而不是只在 policy action 更新时推理。
- 诊断：在 actuator compute 与 environment physics stepping loop 同时记录调用计数和 sim-step counter。；把 policy period、physics dt、decimation、actuator model 训练数据 dt 并列记录。
- 原因：作者认为 ActuatorNetMLP 作为 explicit actuator 在每个 physics step 计算，与 50Hz 训练数据时间尺度不一致；线程没有维护者确认其物理影响。
- 处理过程：作者在 actuator_net.py 与 manager_based_rl_env.py 加 instrumentation，并用官方 GO1 rough locomotion 任务运行。
- 结果：确认了该任务中的调用频率；没有确认降低调用频率、保持输出或以 200Hz 数据重训哪一种方案正确。；没有帖子内的真实 GO1 部署验证。
- 限制：调用次数结论依赖作者当时版本与 post-step/reset 路径；升级后必须重新 instrument。；日志截图未参与结论，卡片只采用作者贴出的 diff、命令和文字计数。；不能从该线程推断当前 Isaac Lab GO1 policy 必然存在 sim-to-real gap。
- 安全提示：在未验证 actuator model 时间尺度前，不应直接把策略用于实机；先在低增益、限幅、保护绳与急停条件下做 system identification 和 rollout 对照。
- 独立核验引用：[issue · 团队仅转入 Discussions 并建议升级，没有给调用率或重训方案的结论](https://github.com/isaac-sim/IsaacLab/issues/2963#issuecomment-3193574728)
- 适用边界：精确对应帖子当时的 managed GO1 rough locomotion task；其他版本和 actuator model 必须重新计数。

### 执行器速度能力与求解器硬限幅分离

- `problem_id`：`problem.hardware_actuator_thermal_power.88761dd27f8b57d1`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：执行器速度能力与 PhysX 硬速度上限必须分开配置**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：在 #1384 对应的 0.34.0 变更链中，velocity_limit 用于 explicit actuator/DCMotor 的模型内部 torque-speed 或 no-load speed 语义；velocity_limit_sim 才是写入 root_physx_view/PhysX 的 joint hard clamp。PR #1654 建立这两个字段，PR #1873 又明确 implicit actuator 不应继续把旧 velocity_limit 自动传播到 solver，要限 PhysX 速度时显式配置 velocity_limit_sim。迁移时应同时打印两层值并回归训练/轨迹，不能把厂家 no-load speed 机械地当 solver hard clamp。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #1384 讨论；PR #1509、#1654、#1873
- 原帖/精确回复：[执行器速度能力与 PhysX 硬速度上限必须分开配置](https://github.com/isaac-sim/IsaacLab/issues/1384#issuecomment-2532105463)
- 平台/作者：GitHub Issues / diegoaldarondo-fauna
- 关键术语：空载转速（no-load speed）；执行器模型上限（actuator-model limit）；求解器硬限幅（solver hard clamp）；仿真速度上限（velocity_limit_sim）
- 环境：原 Issue commit b9a49ca、Isaac Sim 4.0.0–4.2.0、Ubuntu 22.04、RTX 4090、CUDA 12.1。；语义分离在 Isaac Lab extension 0.34.0 / PR #1654 中引入，PR #1873 于 2025-03 进一步回退 implicit actuator 的旧字段传播。
- 症状：早期 explicit actuator 的 velocity_limit 不会写入 root_physx_view，imported joint limit 可静默压过 DCMotor 设置。；把同一个 velocity_limit 同时当 no-load speed 和 solver hard clamp 后，社区用户报告 quadruped training 被破坏或版本间行为变化。
- 诊断：分别打印 actuator.velocity_limit、actuator.velocity_limit_sim 与 root_physx_view.get_dof_max_velocities。；确认 DCMotor torque-speed cutoff 和 physics solver maxJointVelocity 是否需要不同数值。；升级跨越 #1509/#1654/#1873 时做训练曲线与 joint velocity distribution 回归。
- 原因：同一个 velocity_limit 字段曾承担 actuator no-load speed 与 solver hard clamp 两种不同物理语义。
- 处理过程：PR #1509 先把 velocity_limit 写入 PhysX 并加测试。；评审指出外载下 motor 可进入 torque-speed 另一象限，no-load speed 不应直接做 joint hard clamp。；PR #1654 增加 *_limit_sim；PR #1873 对 implicit actuator 恢复显式 *_limit_sim 的要求。
- 有效处理：在该版本变更链中，用 velocity_limit 表达 explicit actuator/DCMotor 模型内部速度能力，用 velocity_limit_sim 表达传播到 PhysX 的硬速度上限；implicit actuator 要设置 solver limit 时显式使用 velocity_limit_sim。
- 结果：#1384 关闭；#1654 和 #1873 均合并。PR #1654 评论中的 quadruped 用户报告分离后可把 actuator limit 恢复为正常值。
- 限制：字段语义继续演进，使用时必须以目标 Isaac Lab 版本文档和源码为准，不能无版本复制。；tight solver limits 可能引入仿真伪影，数值必须通过 trajectory/contact 回归而非只看配置。；不依赖 PR 中训练曲线图片。
- 安全提示：实机速度保护仍应在硬件驱动/安全控制器独立实现；仿真 solver clamp 不是实机 safety limit。
- 独立核验引用：[pull_request · 合并 PR 4c4377d 引入 velocity_limit_sim/effort_limit_sim，分离 actuator 与 solver limits](https://github.com/isaac-sim/IsaacLab/pull/1654)；[pull_request · 合并 PR 3d836ab 回退 implicit actuator 对旧 velocity_limit 的自动传播并要求显式 *_limit_sim](https://github.com/isaac-sim/IsaacLab/pull/1873)
- 适用边界：适用于 Isaac Lab 0.34.0 附近的 actuator limit 迁移；更晚版本必须按同名字段的目标版本实现复核。

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

### Crocoddyl 软着陆代价需区分通用 formulation 与当时 API 能力

- `problem_id`：`problem.safety_fall_recovery.crocoddyl_soft_landing_velocity_acceleration_682`
- 问题综合等级：**需要实际验证** — 不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Crocoddyl 软着陆中加速度与冲击速度代价的 API 边界**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突；尚未形成可核对的复现记录。
- 解答状态：`conflicting`
- 候选解答：线程给出的可执行旧 API 路径是：在 contact dynamics 中用 weighted quadratic state cost 高权重惩罚 torso/joint velocities，或在 impulse dynamics 中使用当时的 crocoddyl::CostModelImpulseCoM 惩罚 CoM impact velocity。另一位维护者同时纠正，formulation 本身并不禁止加速度代价，限制可能只是当时 API。由于没有版本锁定和复测，不能写成“加速度绝对不能惩罚”，应在目标版本核对现成 residual/cost 或自行派生模型。
- 证据状态：`issue_candidate`
- 来源定位：Crocoddyl #682：维护者评论 583300715 建议 velocity/impact velocity；583484115 给出 CostModelImpulseCoM；成员评论 585627084 说明 formulation 可罚 acceleration、可能仅 API 受限
- 原帖/精确回复：[Crocoddyl 软着陆中加速度与冲击速度代价的 API 边界](https://github.com/loco-3d/crocoddyl/issues/682#issuecomment-585627084)
- 平台/作者：GitHub Issues / ddliu365
- 关键术语：软着陆（soft landing）；冲击速度（impact velocity）；冲量动力学（impulse dynamics）；加速度代价（acceleration cost）
- 环境：Crocoddyl devel 分支，线程时间为 2020-02；未给 commit、Python/C++ 版本或机器人型号。
- 症状：用户观察 jumping example 落地不够柔和，希望增加最小化 torso acceleration 的 cost。
- 诊断：区分 formulation 的表达能力与目标版本现成 API：前者允许自定义加速度代价，后者当时提供的是速度/impact velocity 路径。；若使用 impulse dynamics，核对 CostModelImpulseCoM 只针对 CoM impact velocity，而不是完整 torso/whole-body impact velocity。
- 原因：原 jumping example 没有针对作者所需软着陆指标配置足够的落地速度/冲击代价。
- 处理过程：维护者建议 contact dynamics + high velocity penalization，使用 weighted quadratic state cost 高权重惩罚 torso 和 joint velocities。；维护者说明当时 impulse dynamics 可用 crocoddyl::CostModelImpulseCoM。；另一位维护者指出加速度在一般 formulation 中也可以惩罚，可能只是当时 API 没有现成接口。
- 结果：作者表示会继续研究，但没有发布实现或软着陆复测结果。
- 限制：线程中的“不能惩罚加速度”被另一位维护者限定为可能只是当前 API 限制，结论存在表述冲突。；API 名称和能力来自 2020 年 devel 分支，当前版本必须查源码/文档。；线程后半段转入一个无关的 quadrupedal_gaits visualization AttributeError；本卡未把该子话题混入软着陆结论。
- 安全提示：实机落地调参必须同时约束关节速度、接触冲量、力矩和姿态，并从低高度开始；单一代价项不构成冲击安全保证。
- 独立核验引用：[maintainer_confirmation · 维护者给出 contact dynamics + velocity penalty 与 impulse dynamics 两条路径](https://github.com/loco-3d/crocoddyl/issues/682#issuecomment-583300715)；[issue · 维护者给出当时 API 名称 crocoddyl::CostModelImpulseCoM](https://github.com/loco-3d/crocoddyl/issues/682#issuecomment-583484115)；[conflict · 另一位维护者说明 formulation 可以惩罚加速度，可能只是现有 API 限制](https://github.com/loco-3d/crocoddyl/issues/682#issuecomment-585627084)
- 适用边界：仅作为 2020 年 Crocoddyl devel 的设计线索；当前 API、机器人落地模型和 impact/contact dynamics 必须实际验证。

### Isaac Lab Unitree G1 被动倒下与平衡策略缺失

- `problem_id`：`problem.safety_fall_recovery.isaaclab_g1_requires_balance_policy_2654`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Unitree G1 仅加载 articulation 配置不会自动保持站立平衡**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：按 IsaacLab 团队回复，没有 motion 时倒下是预期行为，G1_CFG 不是自动站立控制器。需要接入 locomotion policy 或其他闭环平衡控制；团队建议从 H1 humanoid policy deployment 教程模板开始。原线程没有给 G1 成品策略，因此模板适配与验收仍需自行完成。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #2654 评论 2963360700 与 2967145219
- 原帖/精确回复：[Unitree G1 仅加载 articulation 配置不会自动保持站立平衡](https://github.com/isaac-sim/IsaacLab/issues/2654#issuecomment-2967145219)
- 平台/作者：GitHub Issues / FranRFH
- 关键术语：运动策略（locomotion policy）；平衡控制器（balance controller）；关节体配置（articulation configuration）；被动倒落（passive falling）
- 环境：Isaac Lab 的 G1_CFG、create_scene.py 与 bipeds.py；原帖未给 Isaac Lab/Isaac Sim 精确版本。
- 症状：G1 在场景中无法自行保持站立，bipeds.py 中三台 Unitree 也会倒下。
- 诊断：区分资产/关节配置是否只定义动力学模型，场景中是否实际运行 locomotion 或 balance policy。
- 原因：团队说明没有运动/平衡策略时倒下属于预期行为。
- 处理过程：作者用教程场景与 bipeds.py 复现；团队建议从 H1 humanoid policy deployment 模板加入策略。
- 有效处理：为 G1 接入 locomotion policy 或其他闭环平衡控制器，而不是只加载 G1_CFG。
- 结果：团队两次确认该行为符合预期，当前不作为模型 bug 修复。
- 限制：线程没有提供可直接用于 G1 的策略、训练配置或站立验收结果；H1 模板只是起点。
- 安全提示：实机调试站立策略时应使用吊架/保护绳、限力矩和急停，不能因仿真资产能加载就直接上机。
- 独立核验引用：[maintainer_confirmation · 团队首次说明无 motion 时倒下是预期行为](https://github.com/isaac-sim/IsaacLab/issues/2654#issuecomment-2963360700)
- 适用边界：适用于只加载 G1 articulation/asset 而没有平衡策略的场景；具体版本和策略实现需另行核对。

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

### Isaac Lab 重置 IMU 历史缓存

- `problem_id`：`problem.sensing_and_perception.isaaclab_imu_reset_history_4305`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 环境重置后 IMU 首帧加速度尖峰**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：该线程的最小复现、源码定位与合并 PR #4306 一致：IMU 用相邻速度做数值微分（numerical differentiation），旧 `reset()` 只清输出，没有清前一帧线速度与角速度缓存，因而首帧拿 reset 前速度参与微分。修复是在 `imu.py` 的 `reset(env_ids)` 中同时把 `_prev_lin_vel_w\[env_ids\]` 和 `_prev_ang_vel_w\[env_ids\]` 置零。原作者确认修复后首帧 `lin_acc_b` 为重力、`ang_acc_b` 为零。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #4305 原帖复现与作者确认 3911771595；合并 PR #4306
- 原帖/精确回复：[Isaac Lab 环境重置后 IMU 首帧加速度尖峰](https://github.com/isaac-sim/IsaacLab/issues/4305#issuecomment-3911771595)
- 平台/作者：GitHub Issues / DreaverZhao
- 关键术语：惯性测量单元（Inertial Measurement Unit, IMU）；数值微分（numerical differentiation）；历史缓存（history buffer）；环境重置（environment reset）
- 环境：IsaacLab commit 244483ee、Isaac Sim 5.1.0、Ubuntu 22.04、RTX 4060Ti 16G、CUDA 12.9、driver 580.95.05；Quadcopter Direct、1 env、IMU update_period=0.005。
- 症状：两次示例中，reset 前加速度为几十量级，reset 后首帧 z 分量分别约 325.6 和 262.9，下一帧恢复正常量级。
- 诊断：检查 IMU 数值微分的历史速度缓存是否与环境、传感器一起按 env_ids 清零。
- 原因：原帖与合并补丁共同确认：`reset()` 清了输出加速度，却没有清 `_prev_lin_vel_w` 和 `_prev_ang_vel_w`，首帧微分仍使用 reset 前速度。
- 处理过程：PR #4306 在 IMU reset 中增加两行，按 env_ids 清零前一帧线速度和角速度缓存。
- 有效处理：升级到包含 PR #4306、merge commit 85d85bd 的版本，或等价地在 IMU reset 中同步清零两个历史速度缓存。
- 结果：PR 已合并；原作者确认修复后 reset 首帧 `lin_acc_b` 为重力、`ang_acc_b` 为零。
- 限制：这里只核验 Isaac Lab 该版本的 IMU 实现，不把首帧结果外推为所有真实 IMU 驱动的重置语义。
- 安全提示：如果首帧 IMU 参与真机保护或状态估计，应在目标驱动上额外核对 reset、时间戳与滤波器状态。
- 独立核验引用：[pull_request · 已合并 PR 85d85bd：reset 同步清零 `_prev_lin_vel_w` 与 `_prev_ang_vel_w`](https://github.com/isaac-sim/IsaacLab/pull/4306)
- 适用边界：适用于包含同一历史缓存实现的 Isaac Lab IMU；其他版本或真实传感器需核对自身 reset 语义。

### 验证 Gazebo 动态生成后的 contact sensor 注册

- `problem_id`：`problem.sensing_and_perception.gazebo_dynamic_contact_spawn_order_2223`
- 问题综合等级：**需要实际验证** — 不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Gazebo 动态生成模型的 Contact sensor 插件顺序 workaround 并不通用**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突。
- 解答状态：`conflicting`
- 候选解答：不能当作通用修复。维护者确认执行顺序是关键机制：`UserCommands` 在 `PreUpdate` 创建实体，`Contact` 的 `EachNew` 必须在之后运行。原作者通过调换插件顺序解决了自己的场景；但后续用户给出相同顺序，仿真启动后再 spawn 仍失败。当前应把顺序调整当作待验证 workaround，同时逐次检查 topic、组件创建和数据新鲜度；线程没有最终修复。
- 证据状态：`issue_candidate`
- 来源定位：Gazebo #2223 原作者 workaround 1845594063、维护者机制说明 1850611180、后续反例 2821527232
- 原帖/精确回复：[Gazebo 动态生成模型的 Contact sensor 插件顺序 workaround 并不通用](https://github.com/gazebosim/gz-sim/issues/2223#issuecomment-2821527232)
- 平台/作者：GitHub Issues / yschulz
- 关键术语：动态生成（dynamic spawn）；接触传感器（contact sensor）；更新前阶段（PreUpdate）；系统执行顺序（system execution order）
- 环境：原帖标注 Ubuntu 22.04、Gazebo Harmonic；后续 Unitree 与 Gazebo Classic 迁移用户报告同类问题。
- 症状：world 文件加载模型时有 contact topic；空 world 启动后经 `/world/test_world/create` 生成时没有。
- 诊断：记录 `UserCommands::PreUpdate` 与 `Contact::PreUpdate` 的实际执行顺序，并检查 `EachNew` 是否在实体创建后才运行。
- 原因：维护者复现并说明：服务生成走 `UserCommands::PreUpdate`；若 `Contact::PreUpdate` 的 `EachNew` 先执行，本轮看不到新实体。
- 处理过程：原作者把 SDF 中 `UserCommands` 放在 `Contact` 前，原始场景不再复现；维护者解释这使实体先创建。；后续用户已经使用 `Physics, UserCommands, SceneBroadcaster, Contact...` 的顺序，仿真启动后再生成模型仍失败。
- 有效处理：当前没有对所有动态生成场景都被确认的修复；插件顺序只能作为局部 workaround 试验，并必须检查 topic 和 contact data。
- 结果：原作者场景得到缓解，但后续环境出现反例；维护者提出 Update/PostUpdate/ECM 方向，Issue 截至采集时仍 open。
- 限制：不同 Gazebo 版本、system priority 配置和生成时刻可能改变结果；不能仅凭 SDF 标签顺序断言已修复。
- 安全提示：接触 topic 是保护或状态切换输入时，应在每次 spawn 后设置显式存活与数据新鲜度检查。
- 独立核验引用：[maintainer_confirmation · 维护者说明 UserCommands::PreUpdate 必须先于 Contact::PreUpdate](https://github.com/gazebosim/gz-sim/issues/2223#issuecomment-1850611180)
- 适用边界：原 workaround 在原作者环境有效；对 Harmonic 及仿真启动后任意时刻 spawn 的模型必须逐环境验证。

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

### Isaac Lab 视觉训练的渲染非确定性边界

- `problem_id`：`problem.reproducibility_and_debugging.isaaclab_vision_render_stochastic_3505`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 视觉训练固定 seed 仍可能受随机渲染管线影响**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：在该线程的 Isaac Sim 5.0/5.1 测试中，强制 PyTorch/cuDNN deterministic、设置 PYTHONHASHSEED/CUBLAS_WORKSPACE_CONFIG，以及 antialiasing OFF 或 FXAA 都没有恢复 RGB 任务可复现性。IsaacLab 团队成员随后明确说明当前 rendering pipeline 本质上具有随机性，暂时没有保证 rendered outputs 确定性的好方法。因此这些设置仍可排除其他随机源，但不能当作当前视觉管线的充分修复；评测应改为多次运行的分布和 camera observation 回归。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #3505 作者复测 3315924447/3326940823，双人 AA 复测 3330102174/3331426534，团队结论 3862666319
- 原帖/精确回复：[Isaac Lab 视觉训练固定 seed 仍可能受随机渲染管线影响](https://github.com/isaac-sim/IsaacLab/issues/3505#issuecomment-3862666319)
- 平台/作者：GitHub Issues / twkang43
- 关键术语：可复现性（reproducibility）；确定性算法（deterministic algorithms）；随机渲染管线（stochastic rendering pipeline）；抗锯齿（anti-aliasing, AA/FXAA）
- 环境：初始：Isaac Sim 4.5、IsaacLab commit f20d74c、Ubuntu 22.04、RTX A6000、CUDA 12.9、driver 575.64.03。；复测：Isaac Sim 5.0.0、IsaacLab commit 90dda53；另有用户报告 Sim 5.1。
- 症状：同 seed 的 state-based 任务训练曲线一致，而 RGB 与 RGB-ResNet18 任务多次运行明显分叉。
- 诊断：先用同任务的 state observation 与 RGB observation 做 A/B 对照。；分别验证 PyTorch/cuDNN 确定性、CUBLAS/PYTHONHASHSEED 与渲染 anti-aliasing，而不是把它们混成一个开关。
- 原因：IsaacLab 团队成员说明当前 rendering pipeline 具有随机性，不能保证 rendered outputs 确定。
- 处理过程：升级 Isaac Sim 5.0/IsaacLab 新提交。；开启 torch.use_deterministic_algorithms、禁用 cudnn benchmark、启用 cudnn deterministic、设置 PYTHONHASHSEED 与 CUBLAS_WORKSPACE_CONFIG。；分别尝试 antialiasing OFF 与 FXAA。
- 结果：上述尝试在帖子所列环境中都没有恢复视觉训练的可复现性；团队未给当前管线的修复。
- 限制：该结论针对帖子测试的 Isaac Cartpole RGB 任务和 4.5/5.0/5.1 时期管线，不能外推未来简化 RTX 模式或 Newton tiled camera。；训练曲线图片未用于判定；卡片只采用多位用户和团队的文字结果。
- 安全提示：视觉策略回归应保存 camera observation 校验样本和多 seed 分布，不要把单次训练差异直接归因于算法改动。
- 独立核验引用：[maintainer_confirmation · 团队成员说明当前渲染管线随机，暂不能保证 rendered outputs 确定](https://github.com/isaac-sim/IsaacLab/issues/3505#issuecomment-3862666319)
- 适用边界：适用于帖子覆盖的 Isaac Sim 4.5、5.0、5.1 视觉训练管线；未来渲染模式需重新测试。

### 隔离 Isaac Lab 环境与 PPO 的随机性

- `problem_id`：`problem.reproducibility_and_debugging.isaaclab_env_vs_ppo_904`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 可复现性要区分环境初始化随机性与策略算法随机性**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：帖子中的可复用隔离法是：先通过 env.reset(seed=YOUR_SEED) 确认 seed 真正传入环境，再用 constant actions 或 seeded random actions 运行，不让 PPO 参与；累计环境 tensor 并对 observation 等结果做 hash。该用户在同一硬件上测到 2000 步连续仿真一致，因此把自己案例的剩余差异定位到 PPO 动作生成。此结果没有覆盖其他硬件或 rough terrain 的所有管线，适合作为诊断步骤而不是通用确定性保证。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #904 后续用户隔离实验 2917221442；rough terrain 未闭环报告 2893545806、2908551344
- 原帖/精确回复：[Isaac Lab 可复现性要区分环境初始化随机性与策略算法随机性](https://github.com/isaac-sim/IsaacLab/issues/904#issuecomment-2917221442)
- 平台/作者：GitHub Issues / hojae-io
- 关键术语：固定动作（constant actions）；带种子的随机动作（seeded random actions）；张量哈希（tensor hash）；策略采样（policy sampling）
- 环境：原帖：Isaac Sim 2024.4.1、Ubuntu 22.04、RTX 3090、CUDA 11.2、driver 550；未给精确 IsaacLab commit。；维护者 PR #940 在同一进程做固定步数 observation/reward 一致性测试，并以 ANYmal rough locomotion 做三次训练对照。；后续用户只明确同一硬件连续运行和最多 2000 sim steps，未给完整版本矩阵。
- 症状：同一 seed 的训练 reward curve 不重合。；rough terrain 即使 terrain seed 固定，仍有用户报告前几次迭代 observation/reward 略有差异并逐渐放大。
- 诊断：在环境构造前设置 cfg seed，避免 terrain、PhysX 或内部 buffer 初始化先消耗随机数。；调用 env.reset(seed=YOUR_SEED) 后，先用 constant actions 或 seeded random actions 驱动环境。；累计 observation/reward 等环境 tensor 并做 hash，对比同硬件连续运行；只有环境一致后再检查 PPO action sampling。
- 原因：维护者认为初始化阶段的 terrain generation、PhysX solver 和内部 buffer 等随机操作在旧流程中早于 seed。；后续用户的 2000 步隔离测试把其特定环境的剩余差异定位到 PPO 动作生成。
- 处理过程：原作者把 seed 从环境创建后移到环境创建前。；PR #940 把 seed 设为环境构造器的首个操作，并增加 observation/reward 一致性测试。；后续用户用 env.reset(seed)、固定动作/seeded random actions 与 tensor hash 隔离环境和 PPO。
- 有效处理：使用包含 PR #940 的版本，或确保环境 seed 在环境、terrain 与仿真对象创建前生效。；特定后续案例中，用 env.reset(seed=...) 修复 Hydra args.seed=None 导致 seed 未生效的问题。
- 结果：原作者报告前移 seed 后多次 reward curve 精确重合；维护者测试在同一进程得到相同 observation/reward。；后续用户报告同硬件连续仿真 2000 步环境 tensor 一致，但其 PPO 动作生成仍不确定。；rough terrain 的另两位用户仍有未闭环差异。
- 限制：PR 测试只证明同一进程/特定任务与版本，不保证跨硬件、跨 Isaac Sim 版本或 GPU scheduling 一致。；维护者三次训练图未用于本卡结论；只采用其文字说明与 PR 测试代码。；rough terrain 差异没有维护者闭环，不能声称设置 seed 即保证所有训练曲线重合。
- 安全提示：可复现性结论应绑定硬件、driver、Isaac Sim/IsaacLab commit 与 task config；控制算法比较应报告多 seed 分布。
- 独立核验引用：[issue · 另一 rough-terrain 环境仍报告差异，限定隔离实验的外推范围](https://github.com/isaac-sim/IsaacLab/issues/904#issuecomment-2893545806)
- 适用边界：适用于同硬件连续运行的环境/PPO 随机源隔离；跨硬件、视觉任务和 rough terrain 需要单独验证。

### Isaac Lab 环境构造前设置随机种子

- `problem_id`：`problem.reproducibility_and_debugging.isaaclab_seed_before_env_904`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 可复现性要区分环境初始化随机性与策略算法随机性**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：该线程确认旧流程在环境创建后才设置 seed，而 terrain generation、PhysX 初始化和内部 buffer 可能已经消耗随机数。合并 PR #940 把 cfg seed 放到环境构造器的最前面，并用固定步数测试得到相同 observation 与 reward；原作者也报告前移 seed 后重复训练曲线重合。应使用包含该 PR 的版本或保证 seed 早于环境、terrain 和仿真对象创建。这个修复只闭环了初始化顺序问题，不保证 rough terrain、跨硬件或整个 PPO 训练链都完全确定。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #904 原帖 Resolution；维护者解释 2320250794、测试 2333392825；PR #940
- 原帖/精确回复：[Isaac Lab 可复现性要区分环境初始化随机性与策略算法随机性](https://github.com/isaac-sim/IsaacLab/issues/904#issuecomment-2333392825)
- 平台/作者：GitHub Issues / hojae-io
- 关键术语：随机种子（random seed）；环境构造（environment construction）；确定性（determinism）；观测与奖励（observations and rewards）
- 环境：原帖：Isaac Sim 2024.4.1、Ubuntu 22.04、RTX 3090、CUDA 11.2、driver 550；未给精确 IsaacLab commit。；维护者 PR #940 在同一进程做固定步数 observation/reward 一致性测试，并以 ANYmal rough locomotion 做三次训练对照。；后续用户只明确同一硬件连续运行和最多 2000 sim steps，未给完整版本矩阵。
- 症状：同一 seed 的训练 reward curve 不重合。；rough terrain 即使 terrain seed 固定，仍有用户报告前几次迭代 observation/reward 略有差异并逐渐放大。
- 诊断：在环境构造前设置 cfg seed，避免 terrain、PhysX 或内部 buffer 初始化先消耗随机数。；调用 env.reset(seed=YOUR_SEED) 后，先用 constant actions 或 seeded random actions 驱动环境。；累计 observation/reward 等环境 tensor 并做 hash，对比同硬件连续运行；只有环境一致后再检查 PPO action sampling。
- 原因：维护者认为初始化阶段的 terrain generation、PhysX solver 和内部 buffer 等随机操作在旧流程中早于 seed。；后续用户的 2000 步隔离测试把其特定环境的剩余差异定位到 PPO 动作生成。
- 处理过程：原作者把 seed 从环境创建后移到环境创建前。；PR #940 把 seed 设为环境构造器的首个操作，并增加 observation/reward 一致性测试。；后续用户用 env.reset(seed)、固定动作/seeded random actions 与 tensor hash 隔离环境和 PPO。
- 有效处理：使用包含 PR #940 的版本，或确保环境 seed 在环境、terrain 与仿真对象创建前生效。；特定后续案例中，用 env.reset(seed=...) 修复 Hydra args.seed=None 导致 seed 未生效的问题。
- 结果：原作者报告前移 seed 后多次 reward curve 精确重合；维护者测试在同一进程得到相同 observation/reward。；后续用户报告同硬件连续仿真 2000 步环境 tensor 一致，但其 PPO 动作生成仍不确定。；rough terrain 的另两位用户仍有未闭环差异。
- 限制：PR 测试只证明同一进程/特定任务与版本，不保证跨硬件、跨 Isaac Sim 版本或 GPU scheduling 一致。；维护者三次训练图未用于本卡结论；只采用其文字说明与 PR 测试代码。；rough terrain 差异没有维护者闭环，不能声称设置 seed 即保证所有训练曲线重合。
- 安全提示：可复现性结论应绑定硬件、driver、Isaac Sim/IsaacLab commit 与 task config；控制算法比较应报告多 seed 分布。
- 独立核验引用：[pull_request · 合并 PR ac71354c：环境构造开始即调用 seed，并增加同一进程 observation/reward 确定性测试](https://github.com/isaac-sim/IsaacLab/pull/940)
- 适用边界：适用于缺少 PR #940、或 seed 仍晚于环境构造的 Isaac Lab 管线；精确确定性边界必须在同硬件与固定版本复测。

### SB3 评测复用训练期 VecNormalize 统计

- `problem_id`：`problem.reproducibility_and_debugging.sb3_vecnormalize_checkpoint_2635`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：SB3 play 必须加载训练期 VecNormalize 统计而不是重新学习**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：使用包含 PR #2022 的版本：train.py 在 run directory 保存 model_vecnormalize.pkl；play.py 从所选 checkpoint 的目录加载该文件，并设置 training=False、norm_reward=False，同时读取训练时保存的 params/agent.yaml。若自定义脚本没有这些步骤，就必须把 normalization stats 与 policy checkpoint 一起保存和加载；仅加载 policy 权重不足以复现训练期输入分布。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #2635 完整复现；SB3 维护者确认 3004477599；PR #2022
- 原帖/精确回复：[SB3 play 必须加载训练期 VecNormalize 统计而不是重新学习](https://github.com/isaac-sim/IsaacLab/issues/2635#issuecomment-3004477599)
- 平台/作者：GitHub Issues / JonasFano
- 关键术语：向量归一化（vector normalization, VecNormalize）；运行统计（running statistics）；评测模式（evaluation mode）；检查点（checkpoint）
- 环境：IsaacLab commit 9f1aa4c、Isaac Sim 4.5.0、Ubuntu 22.04.5、RTX 3500 Ada Laptop 12GB、CUDA 12.1、driver 535.230.02。
- 症状：train.py 不保存 normalization statistics；play.py 用 fresh VecNormalize 且继续 training。；evaluation normalization distribution 与训练期不一致，策略表现下降。
- 诊断：检查 run directory 是否有 model_vecnormalize.pkl。；检查 play 是否从目标 checkpoint 同目录加载 stats，并把 training 与 reward normalization 关闭。；检查 play 使用的是训练时保存的 agent.yaml，而不是当前默认配置。
- 原因：训练统计未持久化，评测端重新初始化并更新均值/方差。
- 处理过程：原帖给出任何 SB3 环境都可执行的 normalize_input/normalize_value 复现步骤与建议代码。；PR #2022 同时修改 train.py 与 play.py 的保存/加载路径。
- 有效处理：使用包含 PR #2022 / merge commit ad14a67 的版本；训练结束保存 model_vecnormalize.pkl，评测从 checkpoint 对应目录加载并设置 training=False、norm_reward=False。
- 结果：SB3 维护者明确回复问题应由 PR #2022 修复，Issue 随后关闭；原作者未贴升级后的性能数值。
- 限制：文件名与路径绑定该 PR 的 Isaac Lab 脚本；自定义 runner 需核对自己的 checkpoint layout。；没有作者升级复测，闭环主要来自合并源码修复与维护者确认。
- 安全提示：部署前应把 policy、VecNormalize stats、agent config 和代码 commit 作为同一不可拆分 artifact 校验。
- 独立核验引用：[pull_request · 合并 PR ad14a67 保存/加载 model_vecnormalize.pkl，并在 play 关闭 stats 更新与 reward normalization](https://github.com/isaac-sim/IsaacLab/pull/2022)
- 适用边界：适用于启用 normalize_input 或 normalize_value 的 Isaac Lab SB3 工作流；自定义目录结构需调整路径。

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

### Isaac Lab 静态地面不支持 GPU filtered contact

- `problem_id`：`problem.contact_force_friction.isaaclab_static_ground_filter_1995`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab GPU contact filter 不能过滤普通静态 ground collider**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：这不等于物理引擎没有求解地面接触。项目贡献者明确说限制在静态 collider 的接触检索/过滤 API；普通静态碰撞仍参与物理求解。原版本的可用绕行是把地面建成带 RigidBodyAPI 的运动学刚体（kinematic rigid body），例如用 RigidObjectCfg + 薄 CuboidCfg 并设置 kinematic_enabled=True。原作者给出了工作配置，但线程没有证明底层静态过滤限制已在后续版本消失，因此升级后仍需实测。
- 证据状态：`issue_candidate`
- 来源定位：Isaac Lab #1995 评论 2708680265/2711098361 的维护者限制说明，评论 2877887219 的原作者可用 RigidObjectCfg 配置
- 原帖/精确回复：[Isaac Lab GPU contact filter 不能过滤普通静态 ground collider](https://github.com/isaac-sim/IsaacLab/issues/1995#issuecomment-2877887219)
- 平台/作者：GitHub Issues / bikcrum
- 关键术语：过滤接触（filtered contact）；静态碰撞体（static collider）；运动学刚体（kinematic rigid body）；接触检索接口（contact retrieval API）；刚体接口（Rigid Body API, RigidBodyAPI）
- 环境：Isaac Sim 4.5.0；Isaac Lab 2.0.0；GPU pipeline；/World/ground 为普通静态 collider。
- 症状：控制台警告 GPU contact filter for collider '/World/ground' is not supported。；指定 filter_prim_paths_expr 后不能取得该静态地面的 filtered contact 数据；不使用 filter 时普通接触仍可参与仿真。
- 诊断：区分接触物理求解与接触检索/过滤 API：维护者明确静态 collider 的物理碰撞仍正常，受限的是 filtered contact retrieval。；检查目标 prim 是否只有 collider、没有 RigidBodyAPI；若用 workaround，还要确认 kinematic body 尺寸覆盖所有环境。
- 原因：当时 PhysX GPU 接触检索 API 不支持对不是 rigid body 的静态 collider 做过滤。
- 处理过程：项目贡献者建议给地面 prim 添加 RigidBodyAPI 并启用 kinematic 属性。；原作者用 SceneCfg 中的 RigidObjectCfg/CuboidCfg 建立大尺寸薄地面，设置 RigidBodyPropertiesCfg(kinematic_enabled=True)、collision_props 和摩擦材质。
- 有效处理：在原版本需要 filtered contact 时，把普通 GroundPlane/static collider 改成覆盖工作区的 kinematic rigid body；原作者明确报告该 RigidObjectCfg 方案可用。
- 结果：原作者发布了工作配置；Issue 之后 completed 关闭，但线程没有给出引擎版本修复或证明普通 static collider 过滤已被支持。
- 限制：该绕行方案改变了地面 prim 类型；TerrainImporterCfg、RayCaster 的 mesh_prim_paths 与多环境路径需要分别验证，不能直接照搬。；后续参与者报告过 prim path 与 ray-caster mesh 错误，但那不是原始 filtered-contact 限制的已确认修复；本卡不把这些跟帖推成通用结论。
- 安全提示：不要仅依据 filtered matrix 为零判定机器人离地；应同时用未过滤净接触、姿态/高度与终止逻辑做交叉检查。
- 独立核验引用：[issue · Isaac Sim 4.5.0/Isaac Lab 2.0.0 的配置、警告和空 filtered contact 现象](https://github.com/isaac-sim/IsaacLab/issues/1995)；[maintainer_confirmation · 贡献者确认限制在检索/过滤 API，静态 collider 的物理接触求解不受影响](https://github.com/isaac-sim/IsaacLab/issues/1995#issuecomment-2711098361)；[issue · 原作者报告 RigidObjectCfg + kinematic Cuboid 地面可用并提供代码](https://github.com/isaac-sim/IsaacLab/issues/1995#issuecomment-2877887219)
- 适用边界：直接适用于 Isaac Sim 4.5.0、Isaac Lab 2.0.0 的 GPU filtered contact 与普通 static ground collider；其他版本需核对当前 PhysX 支持。

### MuJoCo 高阻尼位置伺服抓取旋转时的切向滑移与漂移

- `problem_id`：`problem.contact_force_friction.mujoco_grasp_servo_slip_2934`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：MuJoCo 抓取旋转时物体漂移应先量化伺服增益与切向滑移，而不是仅看可视姿态**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：目前只能确认：该复现里接触在滚转开始时已出现约 0.012 m/s 的切向相对速度，高 kv 会显著放大最终漂移；把 kv 从 100 降到 5 时，报告漂移由约 13.6 mm 降到 0.7 mm。应记录 actuator force、qpos/qvel、物体净力、接触切向速度与 efc_vel，并进一步制作纯 XML 最小复现。降低 kv 是缓解与诊断手段，不是已确认根治；维护者尚未给出最终原因，Issue 仍开放。
- 证据状态：`issue_candidate`
- 来源定位：MuJoCo #2934 评论 4183505169 的 kv 扫描/接触级测量，评论 4183566032 与 4183580186 的维护者边界说明
- 原帖/精确回复：[MuJoCo 抓取旋转时物体漂移应先量化伺服增益与切向滑移，而不是仅看可视姿态](https://github.com/google-deepmind/mujoco/issues/2934#issuecomment-4183505169)
- 平台/作者：GitHub Issues / vmstavens
- 关键术语：位置执行器（position actuator）；切向相对速度（tangential relative velocity）；约束空间速度（constraint-space velocity）；伺服阻尼增益（servo damping gain）；最小可复现实例（Minimal Reproducible Example, MRE）
- 环境：Ubuntu 24.04；MuJoCo 3.3.7；CPU；timestep=0.002 s；implicitfast integrator；Newton solver；elliptic cone；Robotiq 2F-85。
- 症状：mocap 控制下物体表现正常，使用 position actuator 驱动笛卡尔六关节时，夹爪旋转会让盒子沿夹指方向滑移。；固定 kp=300 时，社区复现实验报告 kv=5、10、100 的最终相对 y 漂移约为 0.7、1.4、13.6 mm；kv=300 更严重。
- 诊断：分别记录 roll target、qpos、qvel、actuator force、物体净力、接触坐标系切向相对速度和 efc_vel，而不是只对比视频。；线程测量在 t=3.200 s 给出切向相对接触速度约 0.01225 m/s；t=3.202 s 的切向 efc_vel 约 0.0122，说明可见滚转角尚小时已经出现切向运动。；维护者要求把 Python/MjSpec 复现继续缩成纯 XML 最小复现，并明确列出 expected/unexpected，才能隔离 MjSpec 与接触模型。
- 原因：当前有数据支持的解释是 position servo 在目标变化时立即产生力矩，摩擦接触已进入切向滑移；高 kv 明显放大漂移，但原评论明确说它不一定是根因。；维护者尚未完成线程审查；本卡不采纳第三方提出的“非结合残差”等未经项目维护者确认的最终根因。
- 处理过程：作者比较普通 general actuator、MjSpec set_to_position、手工构造 affine position actuator，以及把编译后的世界写成 MJCF 后手工改为 position tag。；社区复现者固定 kp=300 扫描 kv，并记录接触级速度、约束速度与净力时序。
- 有效处理：降低 kv 在该复现实验中显著减小漂移，可作为诊断性缓解，但没有完全消除起始切向运动。；作者报告普通 general actuator 不出现同样现象但不能提供所需位置控制；将编译结果导出为 MJCF 后手工改 position actuator 在其测试中得到期望结果，这些都尚未形成通用修复。
- 结果：线程已把问题从单纯视觉异常推进到可量化的增益扫描与接触切向速度；截至 2026-04-29 Issue 仍 open，维护者仍等待纯 XML 最小复现。
- 限制：没有最终维护者根因、合并修复或版本边界，不能将其写成 MuJoCo 已确认 bug。；第一张时序图已完成本轮视觉核验；第二张接触速度图和原帖视频未作为独立视觉证据，本卡对应数值只引用评论文字。；线程中存在未经项目方确认的理论性诊断，本卡明确不采用。
- 安全提示：接触操作控制器应同时限制伺服增益、监测切向相对速度和物体漂移；可见姿态稳定不等于接触仍处于粘着区。
- 图片分析：原评论第一张四联时序图（kp=300、kv=300）已核验：虚线约在 3.2 s；roll target 开始上升时 actuator force 先瞬时冲到约 0.45，物体 y 向净力出现约 1.9 N 瞬态，而 qpos/qvel 仍很小；随后 prop relative y 持续下降，到约 3.84 s 接近 -19 mm。该图支持“力与漂移起始早于明显可见滚转”，不单独证明最终根因。
- 独立核验引用：[issue · MuJoCo 3.3.7/CPU 的 MjSpec、mocap 与 actuator 对照复现](https://github.com/google-deepmind/mujoco/issues/2934)；[issue · 固定 kp=300 的 kv 扫描、接触切向速度、efc_vel 与净力时序](https://github.com/google-deepmind/mujoco/issues/2934#issuecomment-4183505169)；[maintainer_confirmation · 维护者说明力/加速度先于位置可见并不意外，同时明确其余问题仍需继续审查](https://github.com/google-deepmind/mujoco/issues/2934#issuecomment-4183580186)
- 适用边界：直接适用于 MuJoCo 3.3.7、CPU、2 ms、implicitfast/Newton、Robotiq 2F-85 的该复现；其他接触模型、增益和步长必须重新测量。

### Isaac Lab ContactSensor 的法向力与摩擦力字段不能混用

- `problem_id`：`problem.contact_force_friction.isaaclab_contact_sensor_normal_vs_friction_2074`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab ContactSensor 的 net_forces_w 只含法向力，摩擦力需单独跟踪**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：维护者明确说明 net_forces_w 是世界坐标中的净法向接触力（net normal contact force），并不包含完整摩擦分量。旧版底层 get_friction_data(dt) 需要自行聚合，且原作者试用后仍得到全零。官方合并 PR #3563 后，应启用 track_friction_forces 并读取 friction_forces_w；该字段按 env/body/filter 聚合摩擦力且有官方测试。使用时必须先核对目标版本是否包含该 PR。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #2074：贡献者评论 2737575470 解释字段语义；协作者 2737622128 提醒输出格式；原作者 2741377794 报告旧路径全零；PR #3563 合入正式字段
- 原帖/精确回复：[Isaac Lab ContactSensor 的 net_forces_w 只含法向力，摩擦力需单独跟踪](https://github.com/isaac-sim/IsaacLab/issues/2074#issuecomment-2737575470)
- 平台/作者：GitHub Issues / hojae-io
- 关键术语：净法向接触力（net normal contact force）；摩擦力（friction force）；接触传感器（ContactSensor）；世界坐标系（world frame）
- 环境：Isaac Lab ContactSensor、长细圆柱 foot collision geometry；原帖未给版本；PR #3563 于 2025-12-10 合入官方仓库。
- 症状：原帖张量中接触足的 z 分量约为 667 N/543 N，而 x 仅约 8e-05/6e-05、y 为零。；另一位使用者的曲线图显示仅一个世界轴分量随拖动变化，另外两条曲线保持零。
- 诊断：先确认读取字段语义：net_forces_w 是 world frame 的净法向接触力，不是 normal+friction 的完整合力。；确认目标版本是否已包含 PR #3563，以及是否启用 track_friction_forces、配置非空 filter_prim_paths_expr 和有效 max_contact_data_count_per_prim。
- 原因：读取了只承载法向力的兼容字段 net_forces_w，却期待其中包含切向摩擦力。
- 处理过程：维护者建议旧路径直接调用 contact_physx_view.get_friction_data(dt)，并提醒必须按不同输出格式自行聚合。；原作者按旧路径尝试后报告仍全零，因此该旧路径在其环境中没有形成已验证修复。
- 有效处理：在包含官方 PR #3563 的版本中启用 ContactSensorCfg.track_friction_forces，并读取 ContactSensorData.friction_forces_w；官方实现按 env/body/filter 对摩擦数据求和，并有接触/非接触测试。
- 结果：PR #3563 合入后，Issue 被标记为 completed；PR 测试验证 friction_forces_w 与底层 get_friction_data 聚合结果一致。
- 限制：Issue 早期的 get_friction_data(dt) 建议未在原作者环境成功，不能把它单独当作旧版本通用修复。；两张原图没有 Isaac Lab 版本、摩擦系数、单位和完整实验配置，不能从曲线大小反推出真实摩擦参数。
- 安全提示：用于实机滑移/摩擦锥判定前，应校验坐标系、符号、滤波、采样周期和传感器/模型误差；仿真接触力不是实机足底传感器的替代品。
- 图片分析：评论 2733805649 的曲线图已核验：图例为 X/Y/Z，只有蓝色 X 曲线在约 -3 至 -10 区间变化并有若干尖峰，橙色 Y 与绿色 Z 基本停在零；坐标仅标 Force/Time，没有单位、版本和摩擦参数，因此只能支持“另外两轴为零”的症状，不能证明力值标定。；评论 2752798128 的 MuJoCo 截图已核验：画面显示机器人足部附近多根浅蓝色向上箭头及数值标注，但没有图例、坐标轴或单位；它只表达作者希望获得类似可视化的完整接触力，不能作为 Isaac Lab 修复结果图。
- 独立核验引用：[maintainer_confirmation · 项目贡献者确认 net_forces_w 仅为 world frame 中的净法向接触力](https://github.com/isaac-sim/IsaacLab/issues/2074#issuecomment-2737575470)；[issue · 原作者报告旧版 get_friction_data 路径在其环境仍返回全零](https://github.com/isaac-sim/IsaacLab/issues/2074#issuecomment-2741377794)；[pull_request · 官方合并 PR 增加 track_friction_forces 与 friction_forces_w，并包含聚合测试](https://github.com/isaac-sim/IsaacLab/pull/3563)；[source_code · 固定合并提交：ContactSensor 对 get_friction_data 按 env/body/filter 求和](https://github.com/isaac-sim/IsaacLab/commit/7b16b6794fba6b1c86a38dddb02f998a6fe32ca6)
- 适用边界：适用于 Isaac Lab ContactSensor；显式 friction_forces_w 路径要求目标版本包含合并 PR #3563，并按配置启用摩擦跟踪。

### Isaac Lab GPU tensor pipeline 启用 surface velocity 后接触消失

- `problem_id`：`problem.contact_force_friction.isaaclab_gpu_surface_velocity_6885`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab GPU tensor pipeline 当前不支持 PhysX surface velocity 接触**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：项目维护者明确说明 GPU 当前不支持该 surface-velocity 行为，应使用 CPU。原帖通过四种管线对照和单独关闭 surfaceVelocityEnabled 证明普通 collider 仍能接触，触发条件是 GPU tensor pipeline 加 surface velocity。若必须留在 GPU，原帖只记录了静态 collider 后逐步改写物体水平 root velocity 的近似方案；它不等价于原生接触，不能拿来验证摩擦或接触力。
- 证据状态：`issue_candidate`
- 来源定位：Isaac Lab #6885：正文四配置对照与最小脚本；维护者评论 5196164192 确认 GPU 不支持并要求使用 CPU
- 原帖/精确回复：[Isaac Lab GPU tensor pipeline 当前不支持 PhysX surface velocity 接触](https://github.com/isaac-sim/IsaacLab/issues/6885#issuecomment-5196164192)
- 平台/作者：GitHub Issues / lxl-2404
- 关键术语：表面速度（surface velocity）；张量管线（tensor pipeline）；运动学刚体（kinematic rigid body）；接触穿透（contact tunneling）
- 环境：Isaac Sim 5.0；omni.physx 107.3.26；Ubuntu 22.04.5；RTX 4090；CUDA 13.0；driver 580.173.02；device=cpu/cuda:0 对照。
- 症状：CPU tensor pipeline 中方块停在约 z=0.30 并以皮带速度移动；GPU tensor pipeline 中方块穿过皮带，落到 ground z≈0.0375，水平速度为零。；没有 warning/error；只关闭 surfaceVelocityEnabled 就恢复同一 collider 的普通 GPU 接触。
- 诊断：用同一场景做 CPU/GPU、timeline/tensor pipeline 四格对照，并只切换 surfaceVelocityEnabled，隔离 collider 与 surface velocity 功能。；记录物体 z、水平速度和是否落到 ground，避免仅凭 viewport 判断。
- 原因：项目维护者确认 GPU 当前不支持该 surface-velocity 行为；不是原帖 collider 本身失效。
- 处理过程：原帖同时测试新 PhysxSurfaceVelocityAPI 与官方 ConveyorBeltDemo 使用的 legacy velocity attribute，二者在 GPU tensor pipeline 下表现相同。；关闭 surface velocity 后普通接触恢复。
- 有效处理：需要原生 surface velocity contact 时改用 CPU pipeline。；原帖记录的 GPU 变通是静态 collider 配合每步事件直接覆盖接触物体的水平 root velocity；它只是行为近似，不是 PhysX 接触解。
- 结果：维护者称该行为符合当前支持边界并要求使用 CPU；Issue 以 completed 关闭，但 GPU 原生 surface velocity 仍没有实现。
- 限制：原帖 System Info 中 Isaac Lab commit/version 字段未填写，只明确 Isaac Sim/PhysX、OS、GPU、CUDA 与 driver。；直接写 root velocity 会绕开真实摩擦/冲量响应，不能用于验证接触力或控制稳定性。；线程没有给出 GPU 支持恢复的版本或补丁。
- 安全提示：不要把 GPU 下穿透现象用于调参或训练接触策略；先切 CPU 验证接触功能边界，并把行为近似与物理接触实验分开。
- 独立核验引用：[issue · CPU/GPU 与 timeline/tensor 四格结果、最小脚本、数值位置和关闭 API 对照](https://github.com/isaac-sim/IsaacLab/issues/6885)；[maintainer_confirmation · 项目维护者确认 GPU 当前不支持，应使用 CPU](https://github.com/isaac-sim/IsaacLab/issues/6885#issuecomment-5196164192)
- 适用边界：直接覆盖 Isaac Sim 5.0/PhysX 107.3.26 的 GPU tensor pipeline；Isaac Lab 精确 commit 未填，后续版本需复测。

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

### TSID ContactForce Python binding 缺少 Contact6d 子类构造 overload

- `problem_id`：`problem.contact_force_friction.tsid_contact_force_binding_child_overload_247`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：TSID Python binding 需为 Contact6d 等 ContactBase 子类显式暴露构造函数**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：项目维护者指出该 Boost.Python binding 不会自动完成所需的 child-to-base 识别，应像其他 TSID bindings 一样，为每个支持的 ContactBase 子类显式暴露 constructor overload。原作者为 Contact6d、ContactPoint 和 ContactTwoFramePositions 增加 bp::init 后确认可实例化；该修改只在用户 fork commit eb03d05，尚无上游发布。
- 证据状态：`issue_candidate`
- 来源定位：TSID #247：维护者评论 2568242300 解释子类 overload；作者评论 2575770028 确认可实例化；fork commit eb03d05 包含三类构造函数 patch
- 原帖/精确回复：[TSID Python binding 需为 Contact6d 等 ContactBase 子类显式暴露构造函数](https://github.com/stack-of-tasks/tsid/issues/247#issuecomment-2575770028)
- 平台/作者：GitHub Issues / danielcostanzi18
- 关键术语：语言绑定（Python binding）；构造函数重载（constructor overload）；子类到基类转换（child-to-base conversion）；接触力等式任务（contact-force equality task）
- 环境：TSID 用户 fork；Python binding；UR5 force-task 示例；原帖未给 TSID/Python/Boost 版本和操作系统。
- 症状：TaskContactForceEquality(name, RobotWrapper, dt, Contact6d) 报 ArgumentError，C++ signature 只显示 ContactBase&。
- 诊断：检查 binding visitor 是否只暴露 ContactBase& constructor，而没有为具体 Contact6d child class 添加 bp::init overload。；对照 TSID 其他 binding 中为每个可能 child class 实现独立方法/构造函数的模式。
- 原因：项目维护者指出 Python binding 没有在该构造函数位置自动识别 Contact6d→ContactBase 继承转换。
- 处理过程：原作者最初只暴露接受 ContactBase& 的构造函数，实例化失败。；随后为 Contact6d、ContactPoint、ContactTwoFramePositions 分别增加 bp::init overload。
- 有效处理：在 TaskContactForceEqualityPythonVisitor 中为每个支持的 ContactBase 子类显式添加 constructor overload，并包含相应 contact headers。
- 结果：原作者确认修改后可传 Contact6d 实例化 task；fork commit eb03d05 的 patch 与该说明一致。
- 限制：修改只存在用户 fork，线程没有上游 PR 合并、发布版本或完整 working force-control example。；环境版本未提供，其他 TSID/Boost.Python 版本必须重新编译验证。
- 安全提示：binding 成功只证明对象可构造，不证明 force task 的 reference、约束维度、接触稳定性或实机力限幅正确。
- 独立核验引用：[maintainer_confirmation · 维护者解释需为 ContactBase 的每个 possible child class 实现独立 constructor](https://github.com/stack-of-tasks/tsid/issues/247#issuecomment-2568242300)；[source_code · 用户 fork：增加 Contact6d、ContactPoint、ContactTwoFramePositions bp::init overload 与 headers](https://github.com/danielcostanzi18/tsid/commit/eb03d0528b401c4d511d30ffe4f13c21fa3faece)
- 适用边界：适用于原帖 TSID Python binding fork；因版本和上游合并状态未知，目标构建需实际验证。

### 在 ros2_control 链式控制中应用 FT 传感器偏置

- `problem_id`：`problem.contact_force_friction.ros2_control_ft_offset_chainable_1796`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ForceTorqueSensorBroadcaster 可用参数偏置并导出链式状态接口**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：已合并 PR #1215 将 broadcaster 改为 `ChainableControllerInterface`，新增 `offset.force.{x,y,z}` 与 `offset.torque.{x,y,z}` 参数，在 update 中应用 offset，并导出对应 state interfaces；补丁同时加入 offset 和接口值测试。该能力应按包含 merge commit `4343c7a` 的版本使用。原帖的 Humble 用户没有完成复测，因此不要假定该功能已回移到 Humble。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #1796 项目回复；ros2_controllers PR #1215 merge 4343c7a4632a97f52fc664b5dcdcad258ffb5e2a
- 原帖/精确回复：[ForceTorqueSensorBroadcaster 可用参数偏置并导出链式状态接口](https://github.com/ros-controls/ros2_control/issues/1796#issuecomment-2419697279)
- 平台/作者：GitHub Issues / lcbw
- 关键术语：力矩传感器（force-torque sensor）；偏置校正（offset calibration）；链式控制器（chainable controller）；状态接口（state interface）
- 环境：原帖：ROS 2 Humble、Ubuntu 22.04、UR10e、Polyscope 5.11；正式实现：ros2_controllers master，PR #1215 merge commit 4343c7a。
- 症状：原有 admittance controller 的 exponential filter 不能满足外加 FT offset 和同时读取 offset/non-offset 数据流的需求。
- 诊断：核对目标 ros2_controllers 版本是否包含 PR #1215，并检查 broadcaster 是否导出六轴 state interfaces。
- 原因：旧 `ForceTorqueSensorBroadcaster` 只发布原始 wrench，未提供参数化 offset 和 chained state interfaces。
- 处理过程：PR #1215 增加 `offset.force.*`/`offset.torque.*` 参数、运行期参数刷新、`ChainableControllerInterface` 和 state-interface export。
- 有效处理：在包含 PR #1215 的版本使用 broadcaster offset 参数，并通过导出的 state interfaces 连接下游 controller。
- 结果：PR #1215 已获两位 reviewer 批准并合并；补丁包含 offset 数值和导出接口单元测试。
- 限制：原作者没有在合并后复测；原帖 Humble 环境当时不能构建该 PR，线程没有 backport 结论。；开启两个 broadcaster 形成原始/偏置双流是项目成员建议，原线程没有发布运行结果。
- 安全提示：FT offset 应在无外力或已知载荷条件下标定，并对突变、饱和和 frame_id 做监控；不能用 offset 掩盖传感器过载或坐标系错误。
- 独立核验引用：[pull_request · 已合并实现、两次批准、offset/exported state interface 单元测试，merge commit 4343c7a](https://github.com/ros-controls/ros2_controllers/pull/1215)
- 适用边界：适用于包含 ros2_controllers PR #1215 的版本；Humble/backport 状态需单独核对。

### 排查 RaiSim 网格接触力跳变

- `problem_id`：`problem.contact_force_friction.raisim_mesh_contact_force_spike_322`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：RaiSim 网格接触力跳变只能先做滤波和碰撞几何排查**

- 独立等级：**需要实际验证** — 尚未形成可核对的复现记录。
- 解答状态：`partial`
- 候选解答：原线程只支持一个有限结论：`dt=0.001 s` 和多组 ERP 对原作者没有改善；项目作者建议需要平滑输出时做时间滤波，并指出碰撞几何切换会产生 spike、网格宜采用更大三角形。降低摩擦被其明确说成未测试，作者也没有发布滤波或重建网格后的结果。因此这些只能作为排查顺序，必须在目标控制器上实际验证滤波延迟和峰值。
- 证据状态：`issue_candidate`
- 来源定位：RaiSim #322 dt/ERP 失败 1165374721；滤波/网格建议 1165990145；ERP 解释 1173562853
- 原帖/精确回复：[RaiSim 网格接触力跳变只能先做滤波和碰撞几何排查](https://github.com/raisimTech/raisimLib/issues/322#issuecomment-1165990145)
- 平台/作者：GitHub Issues / edward9503
- 关键术语：接触力尖峰（contact force spike）；误差修正参数（error reduction parameter, ERP）；碰撞网格（collision mesh）；时间滤波（temporal filtering）
- 环境：RaiSim；机械臂 Cartesian-space control；固定 OBJ wall；`dt=0.001 s`；版本未给出。
- 症状：增大推墙深度后，测得 contact force 在零与应有数值之间反复跳变；配图曲线仅用于说明症状。
- 诊断：比较 timestep、ERP、碰撞网格三角形尺度和几何切换位置；对原始与滤波 force 同时记录。
- 原因：项目作者说明碰撞几何发生变化时会出现 spike，并建议使用较大三角形；线程没有给源码级根因或定量验证。
- 处理过程：原作者已试 `dt=0.001 s` 和不同 ERP，均称没有改善。
- 有效处理：项目作者认为时间滤波是获取平滑 force 的最佳办法，并建议较大网格三角形；原作者未复测。
- 结果：没有公开最终改善数据；ERP spring/damper 只得到概念解释。
- 限制：降低摩擦是项目作者未亲自测试的建议，不能登记为有效修复。；滤波会引入相位延迟，线程没有给 cutoff、order 或 WBC 稳定性结果。
- 安全提示：接触力滤波用于真机控制前必须评估相位裕度、峰值保留和碰撞检测延迟；不得仅为曲线平滑而隐藏冲击。
- 独立核验引用：[maintainer_confirmation · 项目作者解释 ERP spring/damper 与 apparent inertia、simulation step 的关系；没有参数范围或结果](https://github.com/raisimTech/raisimLib/issues/322#issuecomment-1173562853)
- 适用边界：适用于该 OBJ wall + Cartesian pushing 场景；没有版本和最终复测。

### 识别 Gazebo/DART 版本造成的 skid-steer 摩擦差异

- `problem_id`：`problem.contact_force_friction.gz_sim_focal_dart_friction_880`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Ubuntu Focal 的系统 DART 版本会改变 Gazebo skid-steer 摩擦表现**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该线程首先核对 `libdart`，原作者环境为 6.9.2-2build4。维护者认为 Focal 系统 DART 的摩擦支持与 Bionic 所用 Gazebo DART fork 不同，并建议用 Bionic、在 Focal 从源码构建该 fork 与 Ignition，或使用 dartsim PPA做版本 A/B。原作者没有公布任何 workaround 结果，所以它是明确的版本诊断入口，不是已验证修复。
- 证据状态：`issue_candidate`
- 来源定位：gz-sim #880 版本确认 868260846；维护者诊断/源码方案 867964701/868823079；PPA 方案 1101662759
- 原帖/精确回复：[Ubuntu Focal 的系统 DART 版本会改变 Gazebo skid-steer 摩擦表现](https://github.com/gazebosim/gz-sim/issues/880#issuecomment-868823079)
- 平台/作者：GitHub Issues / ctampier
- 关键术语：摩擦模型（friction model）；侧滑转向（skid steering）；物理后端（physics backend）；版本固定（version pinning）
- 环境：Ubuntu 20.04 Focal Docker；Ignition Gazebo Fortress binary；系统 DART 6.9.2-2build4；官方 `skid_steer_mecanum.sdf`。
- 症状：命令 linear x=0.5、angular z=0.5 时，机器人多数时间直行，偶尔突然转 90°，而不是近似圆周运动。
- 诊断：记录 `libdart` 精确版本，并用相同 world/command 对比 Bionic Gazebo fork、Focal system DART 或 PPA build。
- 原因：维护者将差异归到 Focal 系统 DART 的摩擦支持；Bionic 使用 Gazebo 自有 fork，支持更好。
- 处理过程：线程建议切换 Bionic、从源码构建 Gazebo DART fork 与 Ignition，或使用 dartsim PPA。
- 有效处理：没有原作者复测；三种路径只能标为维护者给出的 workaround 候选。
- 结果：环境和 DART 版本被确认，未报告 workaround 后的轨迹。
- 限制：未给固定 fork commit、PPA 包版本或转向误差指标；Issue 仍开放。；该结论不适用于 Bullet、ODE 或当前 Gazebo/DART 版本。
- 安全提示：sim-to-real 前应固定 physics engine/package digest，并用横向/角向速度、接触力和滑移率做回归，不能只看 world 文件相同。
- 独立核验引用：[maintainer_confirmation · 维护者明确关联 Focal DART 版本与 Bionic fork 摩擦支持差异](https://github.com/gazebosim/gz-sim/issues/880#issuecomment-867964701)
- 适用边界：直接适用于 Focal + Fortress binary + DART 6.9.2-2build4；其他版本需重新 A/B。

### RobotLab 接触力尖峰尚无通用参数修复

- `problem_id`：`problem.contact_force_friction.robotlab_contact_spike_dt_4366`
- 问题综合等级：**需要实际验证** — 不同来源存在尚未解决的冲突，全部经验继续展示并等待目标环境验证。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：RobotLab 足端接触力尖峰的 dt 经验仍存在冲突**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；来源结论存在未解决冲突；当前仅形成问题线索。
- 解答状态：`conflicting`
- 候选解答：该线程不能支持这样的通用结论。原作者在自己的 G1 配置中对比 `0.001/10` 异常、`0.005/4` 正常，并一度报告 compliance 3e5/3e2 有效；但后来明确不再推荐 compliance 修法。另一用户又在 `0.005/4` 看到机器人飞起和 NaN，直接限制了 dt workaround 的外推范围。当前只有复现与规避线索，没有维护者根因或正式 fix；应把 target asset、contact model、solver settings、dt/decimation、contact force 与 joint acceleration 同步记录后复测。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #4366 原作者撤回 compliance 推荐 4554291445；小复现 4670800756；0.005/4 反例 4817539554
- 原帖/精确回复：[RobotLab 足端接触力尖峰的 dt 经验仍存在冲突](https://github.com/isaac-sim/IsaacLab/issues/4366#issuecomment-4817539554)
- 平台/作者：GitHub Issues / super-dashuaibi
- 关键术语：仿真时间步（simulation timestep）；控制降采样（control decimation）；柔顺接触（compliant contact）；接触力尖峰（contact-force spike）
- 环境：原帖：RobotLab 2.3、Isaac Sim 5.1.0、Ubuntu 22.04、4090D、CUDA 12.8、driver 570；Unitree G1。；后续小复现使用 RobotLab 2.3.0 的 Unitree H1 flat task、32 envs。
- 症状：原作者在 dt=0.001/decimation=10 报告接触力 1.3k～10kN、`joint_acc_l2` 爆炸；另一用户在 dt=0.005/decimation=4 仍见机器人飞起并触发 NaN。
- 诊断：把训练和 play 使用的 dt/decimation 分开核对；同时记录 latest contact forces、joint acceleration 与异常 env_ids。
- 原因：原线程没有得到维护者确认的根因；small dt 只是原作者环境中的相关条件，不是已证明充分原因。
- 处理过程：原作者尝试 `compliant_contact_stiffness=3e5`、`compliant_contact_damping=3e2` 并一度称有效；后来撤回推荐。；原作者提供替换 `rewards.py`/`flat_env_cfg.py` 的小型复现流程。
- 有效处理：没有经线程闭环的通用修复；dt=0.005 只是原作者规避，已被另一环境反例否定为普适答案。
- 结果：Issue 仍开放；无维护者根因、无关联修复 PR，compliance workaround 也被原作者撤回推荐。
- 限制：原帖和评论包含多张曲线/截图，本卡只采用作者在文字中明确报告的数值与结论，没有从像素读取额外量。；不使用 contact/acceleration reward 只能避免训练项触发，不能证明底层接触尖峰消失。
- 安全提示：任何出现飞起、NaN 或数量级异常的配置都不应直接迁移到真机；先以单环境、限幅、异常终止和 solver telemetry 隔离。
- 独立核验引用：[conflict · 原作者撤回 compliance 推荐，并把 dt=0.005 仅作为规避](https://github.com/isaac-sim/IsaacLab/issues/4366#issuecomment-4554291445)；[conflict · 另一用户在 dt=0.005/decimation=4 仍复现飞起与 NaN](https://github.com/isaac-sim/IsaacLab/issues/4366#issuecomment-4817539554)
- 适用边界：仅作为 RobotLab 2.3/Isaac Sim 5.1 附近 G1/H1 接触数值排查入口，不构成通用稳定参数表。

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

### Isaac Lab 浮动基完整质量矩阵的读取接口

- `problem_id`：`problem.dynamics_mass_inertia_actuation.isaaclab_generalized_mass_matrix_2252`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Sim 4.5 浮动基机器人完整质量矩阵应读取 generalized mass matrix**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：团队建议使用 root_physx_view.get_generalized_mass_matrices()。官方 OSC 示例也先读取该矩阵，再用 arm_joint_ids 切成机械臂子矩阵；浮动基 WBC 若要全系统矩阵，不应照抄这一步切片。原线程没有回答完整 gravity 和 Coriolis 项的对应接口，因此这两部分仍需查目标版本 API。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #2252 评论 2783953307；当前官方 OSC 示例 run_osc.py 第 317 行附近
- 原帖/精确回复：[Isaac Sim 4.5 浮动基机器人完整质量矩阵应读取 generalized mass matrix](https://github.com/isaac-sim/IsaacLab/issues/2252#issuecomment-2783953307)
- 平台/作者：GitHub Issues / JinAses
- 关键术语：广义质量矩阵（generalized mass matrix）；浮动基（floating base）；重力补偿项（gravity compensation term）；科氏与离心项（Coriolis and centrifugal term）
- 环境：Isaac Sim 4.5；浮动基四足或人形机器人；原帖未给 Isaac Lab 精确版本。
- 症状：get_mass_matrices、get_coriolis_and_centrifugal_forces、get_generalized_gravity_forces 只出现关节维度，而 Jacobian 包含浮动基自由度。
- 诊断：对照 get_jacobians 与动力学量的最后一维，确认是否包含浮动基自由度。；参照官方 OSC 示例核对 get_generalized_mass_matrices 的返回后是否又被关节索引切片。
- 处理过程：团队建议改用 get_generalized_mass_matrices，并指向 Omni Physics Tensors API 与 OSC 示例。
- 有效处理：在 Isaac Sim 4.5 读取 get_generalized_mass_matrices；需要全系统矩阵时不要像机械臂示例那样只保留 arm_joint_ids。
- 结果：完整质量矩阵入口得到官方回复与示例交叉核对；完整 gravity/Coriolis 入口仍未回答。
- 限制：本卡只确认质量矩阵；不能把同一方法外推为完整重力或科氏项接口。；当前文档可能已演进，其他 Isaac Sim 版本需重新核对 API。
- 安全提示：将矩阵送入 WBC/QP 前应断言维度、自由度顺序和浮动基坐标约定。
- 独立核验引用：[official_documentation · 当前官方 OSC 示例第 317 行读取 get_generalized_mass_matrices 后按 arm_joint_ids 切片](https://isaac-sim.github.io/IsaacLab/main/source/tutorials/05_controllers/run_osc.html#the-code)
- 适用边界：Isaac Sim 4.5 的 PhysX articulation；其他版本需核对 API 名称和矩阵维度。

### Isaac Lab joint drive 与 actuator 增益的覆盖关系

- `problem_id`：`problem.dynamics_mass_inertia_actuation.isaaclab_joint_drive_actuator_gain_path_2369`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 隐式与显式 actuator 对 PhysX joint drive 增益的处理不同**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：在固定提交 3b6d615 的 articulation.py 中，ImplicitActuator 分支把 actuator stiffness/damping 写入模拟器；其他显式 actuator 分支把模拟器 joint stiffness/damping 写为 0，显式 actuator 自己处理增益和力矩。原帖团队总结与该源码一致。调试时应查看目标版本的同一初始化路径，而不是假定 URDF joint_drive 和 actuator gains 会同时生效。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #2369 评论 2912221637 定位源码；评论 2941414534 给出团队总结；固定提交 articulation.py 1360-1390 行
- 原帖/精确回复：[Isaac Lab 隐式与显式 actuator 对 PhysX joint drive 增益的处理不同](https://github.com/isaac-sim/IsaacLab/issues/2369#issuecomment-2941414534)
- 平台/作者：GitHub Issues / KyleM73
- 关键术语：关节驱动（joint drive）；隐式执行器（implicit actuator）；显式执行器（explicit actuator）；刚度/阻尼增益（stiffness/damping gains）
- 环境：IsaacLab 源码固定提交 3b6d615f9aff7435fdafaa75a0d59365500a428c；Issue 未给 Isaac Sim 精确版本。
- 症状：URDF importer 和 actuator 配置都出现 stiffness/damping，调用者不确定是否叠加、覆盖或忽略。
- 诊断：在目标版本 articulation 初始化路径中检查 implicit 与 explicit 分支实际写入模拟器的 stiffness/damping。
- 处理过程：讨论者定位固定源码行；团队给出 joint drive 和 actuator 的角色总结。
- 有效处理：implicit actuator 由配置的 actuator gains 写入 PhysX；explicit actuator 将 PhysX joint stiffness/damping 置零，避免与显式力矩计算干扰。
- 结果：固定提交的源码与团队总结一致，明确了两类 actuator 的增益写入路径。
- 限制：本卡只确认固定提交的运行路径，不外推所有历史/未来版本。；原评论还讨论 None 默认值和调参建议；本卡没有把未逐行核对的附加建议并入结论。
- 安全提示：部署前记录实际写入 simulator 的 stiffness、damping 和 effort limits，避免双重 PD 或意外零增益。
- 独立核验引用：[source_code · ImplicitActuator 写入 gains；explicit 分支将 simulator stiffness/damping 置零](https://github.com/isaac-sim/IsaacLab/blob/3b6d615f9aff7435fdafaa75a0d59365500a428c/source/isaaclab/isaaclab/assets/articulation/articulation.py#L1371)
- 适用边界：精确适用于 IsaacLab 提交 3b6d615 的 articulation 初始化路径；其他版本需对照源码。

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

### Isaac Lab articulation 的 6D 近端关节反作用 wrench 读取接口

- `problem_id`：`problem.hardware_actuator_thermal_power.isaaclab_body_incoming_joint_wrench_2127`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 用 body_incoming_joint_wrench_b 读取每个 body 近端关节的 6D 反作用力矩**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：官方合并 PR #2128 后，应读取 ArticulationData.body_incoming_joint_wrench_b。PR 文档规定其形状为 (num_instances, num_bodies, 6)，表示 parent body 向 child body 施加的 joint reaction wrench，坐标在 parent body frame，并包含 root body 到 world 的条目。它与 isaacsim.core.articulations 的 get_measured_* API 不是同一层接口，也不等同于任意安装位姿的实体 F/T sensor。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #2127：协作者评论 2789530049 说明新字段；PR #2128 合并提交 1393f3b，含静态 10 N/10 Nm 测试
- 原帖/精确回复：[Isaac Lab 用 body_incoming_joint_wrench_b 读取每个 body 近端关节的 6D 反作用力矩](https://github.com/isaac-sim/IsaacLab/issues/2127#issuecomment-2789530049)
- 平台/作者：GitHub Issues / ParlitsisG
- 关键术语：六维力/力矩（Six-Dimensional Force/Torque, 6D F/T）；关节反作用力矩（joint reaction wrench）；父刚体坐标系（parent body frame）；近端关节（proximal joint）
- 环境：Isaac Lab Articulation API；PR #2128 于 2025-05-03 合入官方仓库；原线程没有给 Isaac Sim/Isaac Lab release 版本。
- 症状：不同旧 Issue 混用 isaacsim.core.articulations 与 Isaac Lab Articulation API，导致使用者无法确认哪些 get_measured_* 调用适用于当前版本。
- 诊断：先区分 isaacsim.core.articulations API 与 Isaac Lab ArticulationData API。；核对目标版本是否包含 PR #2128，并确认 wrench 表达在 parent body frame、最后一维为 6。
- 原因：跨 Isaac Sim/Isaac Lab 版本和 API 层复制旧调用，导致方法归属与返回语义混淆。
- 处理过程：Issue 参与者询问 get_measured_joint_forces/efforts；协作者澄清它们属于不同 API，并指向正在加入的 PR #2128。
- 有效处理：在包含 PR #2128 的 Isaac Lab 版本中读取 ArticulationData.body_incoming_joint_wrench_b；它从底层 get_link_incoming_joint_force 取得数据并缓存为每 body 的 6D 张量。
- 结果：官方 PR #2128 已合入，并增加 CPU/CUDA、单/多 articulation 的静态 wrench 数值测试。
- 限制：该字段是 parent-to-child 近端关节 reaction wrench，不等同于任意安装位置的独立 F/T sensor。；线程没有给噪声、带宽、滤波或实机传感器一致性验证。
- 安全提示：用于碰撞/过载保护前需独立验证符号、body 顺序、坐标变换、阈值和更新延迟，不得只依赖仿真 reaction wrench 触发实机安全动作。
- 独立核验引用：[maintainer_confirmation · 项目协作者说明新 API 将提供每个 articulation body 近端关节的 6D F/T measurement](https://github.com/isaac-sim/IsaacLab/issues/2127#issuecomment-2789530049)；[pull_request · 官方合并 PR 定义字段语义、形状和 parent body frame，并增加数值测试](https://github.com/isaac-sim/IsaacLab/pull/2128)；[source_code · 固定合并提交：ArticulationData.body_incoming_joint_wrench_b 与 test_body_incoming_joint_wrench_b_single_joint](https://github.com/isaac-sim/IsaacLab/commit/1393f3b8b2306c61bf7a67a8256036967dd58bde)
- 适用边界：适用于包含 PR #2128 的 Isaac Lab ArticulationData；旧版本和 isaacsim.core.articulations API 需按其自身文档处理。

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

### 区分 Isaac Lab target 与 effort 更新频率

- `problem_id`：`problem.hardware_actuator_thermal_power.isaaclab_actuator_update_rate_3823`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 显式与隐式执行器在 decimation 内的更新语义**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：维护者明确说明：显式执行器（explicit actuator）的 effort 随每次 simulation step 调用 `write_data_to_sim()` 而重新计算；通常保持到下个控制周期的是 actuator target，而不是必然保持同一 effort。隐式执行器（implicit actuator）的 PhysX 内部 PD 也会在每个 sim step 用当前关节状态重算；显式路径会把 PhysX 内部 PD gains 设为零，使显式计算的 effort 作为 pass-through 写入模拟器。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #3823 维护者回复 3446108549
- 原帖/精确回复：[Isaac Lab 显式与隐式执行器在 decimation 内的更新语义](https://github.com/isaac-sim/IsaacLab/issues/3823#issuecomment-3446108549)
- 平台/作者：GitHub Issues / onurulusoy7
- 关键术语：显式执行器（explicit actuator）；隐式执行器（implicit actuator）；控制降采样（decimation）；比例微分控制（Proportional-Derivative control, PD）
- 环境：原帖给出示例：policy 100 Hz、simulation 500 Hz、decimation 5；没有固定 Isaac Lab commit。
- 症状：用户原先把显式路径画成同一力矩在 5 个 sim steps 内保持。
- 诊断：沿 `Articulation.write_data_to_sim()`、`_apply_actuator_model()` 和内部 PhysX PD gains 的写入路径检查调用频率。
- 原因：问题来自把 target update frequency 与 actuator effort compute frequency 混为一谈。
- 处理过程：维护者直接按源码调用路径逐项回答显式与隐式两类 actuator。
- 有效处理：建模时把 target 通常按 control frequency 更新、explicit compute 按每次 sim-step write 调用执行、implicit PhysX PD 按每 sim step 重算三件事分开。
- 结果：维护者确认用户图中的显式力矩恒定假设不正确；隐式 PD 每 sim step 重算的理解正确。
- 限制：回复使用当时 `main` 的源码链接，未固定 commit；自定义环境若不是每个 sim step 调 `write_data_to_sim`，必须按实际调用链核对。
- 安全提示：真机驱动器内部电流环、速度环和 Isaac Lab actuator 不是同一层级，不能直接用此频率关系替代硬件环路说明。
- 独立核验引用：[maintainer_confirmation · 维护者直接说明 explicit/implicit 两条更新路径](https://github.com/isaac-sim/IsaacLab/issues/3823#issuecomment-3446108549)
- 适用边界：适用于该回复所对应的 Isaac Lab 调用链；需以目标版本和自定义 step loop 的真实 `write_data_to_sim` 调用频率复核。

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
- 经验数量：2（全部列出，不隐藏待验证或冲突来源）

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

**经验 2：Pinocchio 浮动基位姿平移在 world 表达而广义速度在 joint local frame 表达**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：不是。维护者说明 placement 的 t 在 antecedent/world frame 表达，但 generalized velocity 遵循 Featherstone 约定，在 joint local frame 表达。若需要以 base 为原点、坐标轴与 world 对齐的表示，可用当前 R 分别旋转线速度和角速度。该结论与既有 #1137 相同，作为同一工程问题的第二个独立原线程聚合。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1357：维护者评论 743988547 给出 placement/velocity frame 约定；原作者 743989277 确认理解
- 原帖/精确回复：[Pinocchio 浮动基位姿平移在 world 表达而广义速度在 joint local frame 表达](https://github.com/stack-of-tasks/pinocchio/issues/1357#issuecomment-743988547)
- 平台/作者：GitHub Issues / mayataka
- 关键术语：广义速度（generalized velocity）；局部关节坐标系（joint local frame）；世界坐标系（world frame）；浮动基（floating base）
- 环境：Pinocchio 浮动基/FreeFlyer 约定；原帖未给版本和机器人 URDF。
- 症状：使用者对 #1122 与 #1137 的示例产生冲突理解，无法确定模拟器间控制器应怎样转换浮动基速度。
- 诊断：把 placement 的 translation 表达和 generalized velocity 的 twist 表达分开核对。；对接其他模拟器时分别检查 base linear velocity、angular velocity 的原点和坐标轴。
- 原因：把 t 在 world/parent frame 表达误解为整个 generalized velocity 也在 world frame 表达。
- 处理过程：作者对照两个旧 Issue 后直接向维护者核对 convention。
- 有效处理：按维护者说明，将 Pinocchio 浮动基广义速度解释为 joint local frame；需要 base 原点、world 轴表达时，用当前旋转 R 旋转线速度和角速度向量。
- 结果：原作者回复已完全理解。
- 限制：线程没有讨论 spatial velocity 的平移作用点变换，也没有给具体版本 API；只覆盖其明确回答的旋转表达转换。
- 安全提示：实机状态接口上线前用已知姿态/速度样例核对轴向、单位和符号，避免速度 frame 错配直接进入控制器。
- 独立核验引用：[maintainer_confirmation · 维护者明确区分 world-frame translation 与 joint-local generalized velocity](https://github.com/stack-of-tasks/pinocchio/issues/1357#issuecomment-743988547)；[issue · 原作者回复已完全理解](https://github.com/stack-of-tasks/pinocchio/issues/1357#issuecomment-743989277)；[issue · 既有独立原线程同样由维护者确认 FreeFlyer q/v frame 约定](https://github.com/stack-of-tasks/pinocchio/issues/1137)
- 适用边界：适用于 Pinocchio 浮动基广义速度的原帖约定；其他模拟器的 twist 原点和 frame 需单独确认。

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

### Pinocchio/Eigen 编译选项不一致导致 URDF buildModel 段错误

- `problem_id`：`problem.model_asset_and_urdf_usd.pinocchio_eigen_compile_flag_abi_mismatch_2046`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 与 OCS2 依赖使用不一致编译选项时 buildModel 段错误**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：维护者先从 aligned_free 回溯判断，同一进程内的库可能使用了不一致的 Eigen 向量化/CPU 编译选项，并建议所有依赖统一用 find_package(pinocchio REQUIRED) 与 pinocchio::pinocchio。作者最终找到一个库单独启用了 -march=native，移除后段错误消失。因此排查重点是跨库 ABI 与编译选项一致性；不能简单把 buildModel 或 URDF 本身判为根因。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #2046：2023-08-31 维护者编译选项/CMake 诊断，2023-09-05 作者报告移除 -march=native 后恢复
- 原帖/精确回复：[Pinocchio 与 OCS2 依赖使用不一致编译选项时 buildModel 段错误](https://github.com/stack-of-tasks/pinocchio/issues/2046)
- 平台/作者：GitHub Issues / Czworldy
- 关键术语：应用二进制接口（Application Binary Interface, ABI）；向量化编译选项（vectorization flags）；导入目标（imported target）；对齐分配器（aligned allocator）；段错误（segmentation fault）
- 环境：Ubuntu Focal；Pinocchio 2.6.20 amd64；OCS2 getPinocchioInterfaceFromUrdfModel；两个间接依赖分别使用 CMake package 与 pkg-config。
- 症状：pinocchio::urdf::buildModel 过程中在 Eigen aligned allocator 的 free 路径崩溃；GDB 回溯进入 JointModelCompositeTpl 析构。；函数在其他示例正常，只有同时链接另一个同样依赖 Pinocchio 的库时出现。
- 诊断：比较所有链接库的编译器、Eigen 向量化选项和 -march 等 CPU 特定选项，而不是只检查 URDF 内容。；比较各库对 Pinocchio 的接入方式；维护者建议统一通过 pinocchio::pinocchio imported target 传播依赖与编译定义。
- 原因：维护者指出不同向量化编译选项会让 Eigen 使用不同的 malloc/free 路径；作者随后发现库 A 单独启用了 -march=native。
- 处理过程：维护者给出非 catkin 与 catkin 两种 CMake 写法，均使用 find_package(pinocchio REQUIRED) 和 target_link_libraries(... pinocchio::pinocchio)。；作者移除仅在其中一个库启用的 -march=native。
- 有效处理：让同一进程内所有 Pinocchio/Eigen 依赖使用兼容且一致的编译选项；原帖中移除单边 -march=native 后段错误消失。；CMake 工程优先统一链接 pinocchio::pinocchio，不再由不同库分别手工拼接 Pinocchio/Eigen include、library 和编译定义。
- 结果：作者明确报告移除库 A 的 -march=native 后 segmentation fault 消失；维护者补充这类混用问题并非 Pinocchio 独有，并将 Issue 关闭为 completed。
- 限制：原帖没有给出统一编译后的完整 CI 或独立复现；不能把所有 buildModel 段错误都归因于 -march=native。；根因是同一进程内编译选项不一致，而不是 -march=native 在所有工程中都应禁用。
- 安全提示：实机 WBC 部署前应在与目标 CPU 一致的构建产物上运行 URDF 加载与动力学冒烟测试，避免 ABI 问题在控制进程启动后才暴露。
- 独立核验引用：[maintainer_confirmation · 2023-08-31 jcarpent 与 nim65s 将 aligned_free 崩溃定位到不同编译选项，并建议统一 pinocchio::pinocchio](https://github.com/stack-of-tasks/pinocchio/issues/2046)；[issue · 2023-09-05 原作者确认库 A 启用了 -march=native，移除后段错误消失](https://github.com/stack-of-tasks/pinocchio/issues/2046)；[source_code · 维护者在原线程引用的官方最小 CMake 示例](https://github.com/stack-of-tasks/pinocchio-minimal/blob/master/CMakeLists.txt)
- 适用边界：直接适用于原帖 Ubuntu Focal/Pinocchio 2.6.20/OCS2 的混合依赖构建；其他版本或平台需先复核实际编译命令与崩溃栈。

### Pinocchio 旧版本漏解析 continuous 类型 mimic joint

- `problem_id`：`problem.model_asset_and_urdf_usd.pinocchio_continuous_mimic_parse_version_2753`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 3.6.0 不会把 continuous 类型 URDF 关节全部解析为 mimic**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：原帖最小复现表明，唯一被识别的是 revolute mimic，四个 continuous mimic 均漏掉。Issue 由 PR #2756 关联关闭，Pinocchio v3.8.0 官方发布说明明确新增“continuous joint 可从 URDF 解析为 mimic”。因此该版本问题应升级到包含 #2756 的 3.8.0 或后续版本，并保持 buildModelFromUrdf(..., mimic=True)；升级后仍需核对实际 mimic 数量。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #2753 的完整 URDF/数组复现；关联 PR #2756；v3.8.0 release 与 CHANGELOG 的 continuous mimic 条目
- 原帖/精确回复：[Pinocchio 3.6.0 不会把 continuous 类型 URDF 关节全部解析为 mimic](https://github.com/stack-of-tasks/pinocchio/issues/2753)
- 平台/作者：GitHub Issues / sea-bass
- 关键术语：从动关节（mimic joint）；连续关节（continuous joint）；统一机器人描述格式解析器（Unified Robot Description Format parser, URDF parser）；关节映射（joint mapping）
- 环境：Ubuntu 24.04；Pinocchio 3.6.0 Python bindings；完整 Kinova-Robotiq URDF。
- 症状：model.mimicked_joints 只返回 \[9\]，model.mimicking_joints 只返回 \[12\]，而 URDF 中预期有 5 组 mimic。；唯一被识别的从动关节类型为 revolute，漏掉的四个类型均为 continuous。
- 诊断：按 URDF joint type 分组核对 mimic 统计，而不是只检查 mimic=True 参数是否传入。；将运行版本与官方 v3.8.0 CHANGELOG 的 continuous mimic parser 支持边界对照。
- 原因：Pinocchio 3.6.0 的 URDF mimic 解析没有覆盖 continuous joint；官方 v3.8.0 变更将该能力作为 #2756 新增。
- 处理过程：原作者提供完整 URDF 和最小 Python 复现，并明确比较 revolute 与 continuous mimic 的结果。
- 有效处理：升级到包含 PR #2756 的 Pinocchio 3.8.0 或后续版本，并继续以 mimic=True 构建模型。
- 结果：Issue 页显示由 #2756 关联关闭；Pinocchio v3.8.0 官方 release 和 CHANGELOG 均列出 continuous joints 可从 URDF 解析为 mimic。
- 限制：官方 release 证明解析能力已加入，但原 Issue 页没有展示作者在 3.8.0 上重新运行后的数组输出。；该修复针对 continuous mimic 的解析；不能据此推断所有 mimic 相关动力学算法在所有版本都完整可用。
- 安全提示：控制夹爪前应比较 URDF 预期 mimic 数、Pinocchio 模型映射和实际驱动自由度，避免向从动关节错误下发独立命令。
- 独立核验引用：[issue · Ubuntu 24.04/Pinocchio 3.6.0 的完整 URDF 与 mimicked_joints/mimicking_joints 输出](https://github.com/stack-of-tasks/pinocchio/issues/2753)；[pull_request · Issue 页关联的关闭 PR #2756](https://github.com/stack-of-tasks/pinocchio/pull/2756)；[official_documentation · v3.8.0 Added：Continuous joints can now be parsed as mimic from a urdf file (#2756)](https://github.com/stack-of-tasks/pinocchio/releases/tag/v3.8.0)；[source_code · 3.8.0 - 2025-09-17 的 #2756 变更条目](https://github.com/stack-of-tasks/pinocchio/blob/devel/CHANGELOG.md)
- 适用边界：直接适用于 Pinocchio 3.6.0 Python bindings 解析 continuous URDF mimic joint；其他版本仍应以发布记录和模型数组核对。

### Pinocchio mimic joint 的版本与算法支持边界

- `problem_id`：`problem.model_asset_and_urdf_usd.pinocchio_mimic_algorithm_support_boundary_1290`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio mimic joint 支持需要按版本和算法核对**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：不能。原线程在 PR #2441 合并前明确提醒并非所有功能可用。Pinocchio v3.5.0 官方发布只明确列出：buildModel 的 mimic 参数（默认 false），以及 forward kinematics、Jacobians/frames、ccrba、RNEA、CRBA、reachable workspace 的 mimic 支持。工程上应传 mimic=True，并按目标版本 release 逐项核对所用算法；continuous mimic 的 URDF 解析还要到 v3.8.0/#2756。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #1290 的维护者版本边界与 #2441 闭环；v3.5.0 release 的算法清单；v3.8.0 continuous mimic 补充
- 原帖/精确回复：[Pinocchio mimic joint 支持需要按版本和算法核对](https://github.com/stack-of-tasks/pinocchio/issues/1290)
- 平台/作者：GitHub Issues / costashatz
- 关键术语：从动关节（mimic joint）；参考关节（referent joint）；逆动力学（inverse dynamics, RNEA）；复合刚体算法（Composite Rigid Body Algorithm, CRBA）；质心刚体算法（centroidal composite rigid body algorithm, ccrba）
- 环境：讨论起于 2020 年旧版本；最终闭环对应 Pinocchio 3.5.0 与 PR #2441。
- 症状：用户无法确认 forward dynamics、FK、IK/Jacobian 等算法是否会自动遵守 referent-mimic 约束。
- 诊断：分别核对 URDF parser 开关、模型中的 mimicking/mimicked 列表，以及目标算法是否出现在对应版本 release 支持清单。
- 原因：历史版本对 mimic joint 的数据结构、解析入口和算法覆盖并非一次性完整交付；维护者也在合并前提醒并非所有功能可用。
- 处理过程：维护者和用户在原线程讨论是否从最终用户状态向量中移除从动自由度，以及 FK/FD/ID 对约束的预期语义。；维护者在 2025 年指向并合并 PR #2441。
- 有效处理：在 Pinocchio 3.5.0 或后续版本使用 buildModel(..., mimic=True) 解析 URDF mimic 字段，并只把 v3.5.0 release 明列的 FK、Jacobian/frame、ccrba、RNEA、CRBA、reachable workspace 视为该版本已声明支持。
- 结果：维护者在 2025-03-03 说明由 #2441 解决并关闭 Issue；v3.5.0 release 列出解析 API、支持算法和新增模型数据字段。
- 限制：原线程在 #2441 合并前明确提醒并非所有 Pinocchio 功能都可用于 mimic；未列入 v3.5.0 release 的算法不能由该线程推断为已支持。；continuous 类型 mimic 的 URDF 解析还需要 v3.8.0 的 #2756，不能只依据 v3.5.0 的通用支持声明。
- 安全提示：进入实机 WBC 前，应对使用到的每个算法做 mimic 约束回归测试，并验证状态/力矩向量维度没有把从动关节当成独立执行器。
- 独立核验引用：[maintainer_confirmation · 2025-02-25 维护者说明 #2441 即将合并且并非所有功能可用；2025-03-03 说明由 #2441 解决](https://github.com/stack-of-tasks/pinocchio/issues/1290)；[pull_request · 原线程用于闭环 mimic 支持的 PR #2441](https://github.com/stack-of-tasks/pinocchio/pull/2441)；[official_documentation · v3.5.0 release 中的 mimic parser 参数与 FK/Jacobian/ccrba/RNEA/CRBA/reachable workspace 支持清单](https://github.com/stack-of-tasks/pinocchio/releases/tag/v3.5.0)；[official_documentation · continuous URDF mimic 解析由 #2756 在 v3.8.0 补充](https://github.com/stack-of-tasks/pinocchio/releases/tag/v3.8.0)
- 适用边界：适用于用 Pinocchio 3.x/4.x 构建带 mimic joint 的 WBC 模型；具体算法仍以目标版本 release 与回归测试为准。

### ROS 2 目标未链接 Pinocchio imported target 导致 Boost 模板上限错误

- `problem_id`：`problem.model_asset_and_urdf_usd.pinocchio_ros2_imported_target_2917`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ROS Jazzy 工程未链接 pinocchio::pinocchio 时触发 Boost variant 模板参数编译错误**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：不要继续靠调整 include 顺序处理。原作者的 CMakeLists 使用 ament_target_dependencies(test pinocchio ...)，没有继承 Pinocchio target 携带的 Boost 编译定义；改为 find_package(pinocchio REQUIRED) 后用 target_link_libraries(test pinocchio::pinocchio)，编译即恢复。维护者确认 imported target 会自动传播四个 Boost MPL/Fusion 上限定义，并将其认定为正确解法。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #2917：维护者评论 4866469692 给出缺失定义，作者评论 4867110493 报告 imported target 修复，维护者评论 4867266136 确认
- 原帖/精确回复：[ROS Jazzy 工程未链接 pinocchio::pinocchio 时触发 Boost variant 模板参数编译错误](https://github.com/stack-of-tasks/pinocchio/issues/2917#issuecomment-4867110493)
- 平台/作者：GitHub Issues / Yazkox
- 关键术语：导入目标（imported target）；编译定义（compile definitions）；模板参数上限（template arity limit）；元编程库（Meta-Programming Library, MPL）
- 环境：Ubuntu 24.04；ROS 2 Jazzy；通过 rosdep/apt 安装 ros-jazzy-pinocchio；Pinocchio 4.0.0；Boost 1.83；colcon、ament_cmake。
- 症状：编译最小 include 程序时，boost::detail::variant::make_variant_list 收到 25 个模板参数，而预处理的 boost::mpl::list 只提供 20 个参数位置。；调整 include 顺序、添加 pinocchio/fwd.hpp 或尝试其他 Pinocchio 头文件都不能消除错误。
- 诊断：检查 CMake 是否真正链接 Pinocchio 导出的 pinocchio::pinocchio target，而不是只把包名交给 ament_target_dependencies 或手工添加 include 路径。；如果不能使用 CMake target，维护者给出的诊断线索是核对 BOOST_FUSION_INVOKE_MAX_ARITY=12、BOOST_MPL_CFG_NO_PREPROCESSED_HEADERS、BOOST_MPL_LIMIT_LIST_SIZE=30、BOOST_MPL_LIMIT_VECTOR_SIZE=30 是否被传播。
- 原因：作者的旧 CMakeLists 使用 ament_target_dependencies(test pinocchio urdfdom_headers)，没有按 Pinocchio 项目方式链接 imported target，因此目标没有继承 Pinocchio 所需的 Boost 编译定义。
- 处理过程：作者把依赖段改为 find_package(pinocchio REQUIRED) 与 target_link_libraries(test pinocchio::pinocchio)，并移除旧的手工 Eigen include/ament 依赖写法。
- 有效处理：在目标上链接 pinocchio::pinocchio，让其自动传播 Pinocchio/Boost 所需的编译定义；原帖作者报告修改后编译恢复。
- 结果：作者明确确认 target_link_libraries 方案可用；维护者说明 imported target 会自动传递上述定义，并确认这就是正确解法；Issue 以 completed 关闭。
- 限制：该记录直接覆盖 ROS Jazzy、Pinocchio 4.0.0 和 Boost 1.83；其他发行版的 Boost 模板错误仍需先比较实际编译命令。；维护者提供了手工 -D 定义作为不用 CMake target 时的备选线索，但原线程实际验证的是 imported target 方案。
- 安全提示：控制软件构建应把 Pinocchio target 的编译定义作为可审计依赖传播，避免各节点手工拼装 include/define 后产生不一致构建。
- 独立核验引用：[issue · 最小 include 复现、Ubuntu 24.04/ROS Jazzy/Pinocchio 4.0.0/Boost 1.83 环境与完整编译错误](https://github.com/stack-of-tasks/pinocchio/issues/2917)；[maintainer_confirmation · 维护者列出 imported target 应传播的四个 Boost 编译定义](https://github.com/stack-of-tasks/pinocchio/issues/2917#issuecomment-4866469692)；[maintainer_confirmation · 维护者确认 pinocchio::pinocchio 是正确解法](https://github.com/stack-of-tasks/pinocchio/issues/2917#issuecomment-4867266136)
- 适用边界：直接适用于 Ubuntu 24.04、ROS 2 Jazzy、Pinocchio 4.0.0、Boost 1.83 的 ament/CMake 工程；其他环境需先核对编译定义是否同样缺失。

### Pinocchio 程序化追加关节时漏乘 fixed-link frame placement

- `problem_id`：`problem.model_asset_and_urdf_usd.pinocchio_fixed_frame_add_joint_2825`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Pinocchio 程序化 addJoint 时不能把固定 link frame 当成运动学树 joint**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：Fixed link 的 frame 不属于 joint kinematic chain；其惯量会合并到承载 joint，变换则折叠进后续 joint placement。程序化追加时，先取目标 body frame，再用 frame.placement * 新关节局部 placement 作为 addJoint 的静态变换；随后用 Identity 把 body frame 挂到新 joint 并附加惯量，或直接 appendBodyToJoint。原作者确认维护者的示例与解释解决了问题。
- 证据状态：`issue_candidate`
- 来源定位：Pinocchio #2825：维护者评论 3641336177 给出 Variant 4，评论 3641830698 解释 fixed frame/joint/inertia 语义，作者评论 3643534486 确认
- 原帖/精确回复：[Pinocchio 程序化 addJoint 时不能把固定 link frame 当成运动学树 joint](https://github.com/stack-of-tasks/pinocchio/issues/2825#issuecomment-3641830698)
- 平台/作者：GitHub Issues / christophfroehlich
- 关键术语：关节静态位姿（joint placement）；固定连杆（fixed link）；运动学树（kinematic chain）；空间惯量（spatial inertia）
- 环境：Ubuntu Jammy；Pinocchio devel commit 7b4ae02283203f37320c70e1098204d177f07ae9；Python 最小复现；FreeFlyer 根关节。
- 症状：URDF 直接解析得到 urdf_joint2 origin=\[1.5,0.1,0.3\]、CoM=\[0,0,0\]；程序化 q_dummy 得到 origin=\[0,0,0\]、CoM=\[0.5,0.1,0.3\]。；继续追加关节时，前序 fixed-link 的位置偏移持续缺失。
- 诊断：分别打印 Model::jointPlacements、Model::inertias、frame placement 与 data.oMi，不要用 link/frame 列表直接推断 joint tree。；用 getBodyId 取得承载 fixed link 的 frame，检查其 placement 是否需要乘入新 joint 的静态 placement。
- 原因：URDF fixed links 不成为独立 joint；其惯量合并到父 joint，变换用于计算后续 jointPlacements。原程序把新 joint 直接挂到 parent joint 的 Identity placement，漏掉 link_2 frame transform。
- 处理过程：原作者分别用 addFrame 与 appendBodyToJoint 构造 q_dummy，两种写法都在 addJoint 阶段漏掉 fixed-link placement。
- 有效处理：读取 link_2 body frame，并把 link2_frame.placement * dummy_placement 作为 addJoint 的 joint placement。；随后把 dummy body frame 以 Identity 挂到新 joint 并附加 inertia；若不需要 frame，可直接 appendBodyToJoint。
- 结果：维护者提供可运行的 Variant 4 和结构解释；原作者回复已理解且解释符合预期，Issue 以 completed 关闭。
- 限制：示例覆盖 fixed-link 折叠和单个新 PZ joint；更复杂的多分支、闭链或 frame 语义仍需逐级核对。；作者确认理解与示例，但线程没有贴出其完整估计器的回归结果。
- 安全提示：模型拼接后应对总质量、CoM、关键 frame placement 和重力力矩做回归，再用于实机控制。
- 独立核验引用：[issue · URDF/程序化三种构造对照、质量/CoM/origin 输出与完整最小脚本](https://github.com/stack-of-tasks/pinocchio/issues/2825)；[maintainer_confirmation · 维护者给出 frame placement 乘入 addJoint 的完整 Variant 4](https://github.com/stack-of-tasks/pinocchio/issues/2825#issuecomment-3641336177)；[issue · 原作者确认已理解且详细解释解决疑惑](https://github.com/stack-of-tasks/pinocchio/issues/2825#issuecomment-3643534486)
- 适用边界：适用于 Pinocchio 程序化组合包含 fixed links 的 URDF 子模型；原帖环境为 Jammy 与 devel commit 7b4ae02。

### 为嵌套 URDF 按 body 构造 ContactSensor view

- `problem_id`：`problem.model_asset_and_urdf_usd.isaaclab_nested_contact_views_5126`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Sim 6.0 嵌套 URDF 导致 ContactSensor view 初始化失败**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：旧实现假定所有 body 都是同一 parent 下的 flat siblings，把 leaf names 拼成一个 alternation；Isaac Sim 6.0 的 link 是递归嵌套的，这个 pattern 无法表达实际路径。合并 #6378（PhysX）和 #6384（OVPhysX）均改为复用解析阶段返回的 per-body path expressions，一条 body 一条 pattern，并增加嵌套层级回归测试。PhysX 路径还必须同步处理 list-pattern 的 body-major raw ordering；公开 ContactSensor `data` 布局保持不变。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #5126 关闭说明 5174104772；合并 PR #6378/#6384
- 原帖/精确回复：[Isaac Sim 6.0 嵌套 URDF 导致 ContactSensor view 初始化失败](https://github.com/isaac-sim/IsaacLab/issues/5126#issuecomment-5174104772)
- 平台/作者：GitHub Issues / dolevfr
- 关键术语：刚体视图（rigid-body view）；接触传感器（ContactSensor）；逐刚体路径表达式（per-body path expression）；刚体主序（body-major ordering）
- 环境：IsaacLab develop 3.0.0、Isaac Sim 6.0.0 pip、Python 3.12、Ubuntu 24.04、Linux 6.17。
- 症状：`create_articulation_view` 能找到全部 53 links，但 flat `create_rigid_body_view` pattern 只找到直接子级或完全失败，并报 pattern did not match。
- 诊断：比较 USD 实际 nested prim paths 与由第一个 body parent 加 leaf names 构造的 view pattern。
- 原因：嵌套 bodies 不共享同一 parent，单个 parent-level alternation 无法表达每个 body 的实际路径。
- 处理过程：PhysX PR #6378 与 OVPhysX PR #6384 均改为从解析结果为每个 body 构造独立 path expression。
- 有效处理：升级到包含 #6378 和 #6384 的版本；不要再用共享 parent 加 flat body names 构造嵌套 URDF 的 ContactSensor patterns。
- 结果：两条 PR 均已合并并获维护者批准；都加入嵌套 hierarchy regression coverage。
- 限制：#6378 的 PhysX list-pattern API 会产生 body-major raw row order，补丁已同步适配内部 consumers，但用户自写 raw-view 索引需单独审计；公开 `data` 仍保持 `(num_envs, num_bodies, ...)`。；#6384 的 fork PR 环境不能在合并前执行 OVPhysX wheelhouse 测试，PR 明确测试将在 upstream/nightly 执行。
- 安全提示：升级后应以 body_names、data shape 和已知 body world positions 做端到端校验，避免传感器能初始化却发生 body/env 索引错位。
- 独立核验引用：[pull_request · 已合并 PhysX per-body patterns、raw ordering 适配与嵌套回归测试](https://github.com/isaac-sim/IsaacLab/pull/6378)；[pull_request · 已合并 OVPhysX per-body binding patterns 与嵌套回归测试](https://github.com/isaac-sim/IsaacLab/pull/6384)
- 适用边界：适用于 Isaac Sim 6.0+ URDF importer 生成的嵌套 rigid-body hierarchy，以及相同层级结构的自定义 USD。

### 让 spawn 属性遍历每个嵌套刚体

- `problem_id`：`problem.model_asset_and_urdf_usd.isaaclab_nested_spawn_props_5918`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab 嵌套 URDF 的 spawn 属性只落到根 link**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：根因是 `apply_nested` 在根 link 首次成功后停止下钻，跳过了嵌套子 links。合并 PR #6377 给 decorator 增加 `stop_on_success`，并让 rigid-body 与 mass property writers 使用 `stop_on_success=False`；默认仍为 true，避免无关 schema 行为变化。验收不能只看 cfg，应遍历全部 rigid bodies，逐项确认 `disableGravity`、`physics:mass` 等目标属性覆盖 N/N。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #5918 原帖 1/N 复现、关闭说明 5174104792；合并 PR #6377
- 原帖/精确回复：[Isaac Lab 嵌套 URDF 的 spawn 属性只落到根 link](https://github.com/isaac-sim/IsaacLab/issues/5918#issuecomment-5174104792)
- 平台/作者：GitHub Issues / AlfredMoore
- 关键术语：嵌套刚体层级（nested rigid-body hierarchy）；生成属性（spawn properties）；遍历早停（traversal early stop）；回归测试（regression test）
- 环境：IsaacLab a4a7602f29 v3.0.0-beta 与 8ef1bf7a8b beta2、Isaac Sim 6.0.0-rc.22、Ubuntu 24.04、RTX 5090、CUDA 13.0、driver 580.159.03。
- 症状：29 links 中只有 1 个得到 `disable_gravity=True`，手端约下垂 0.2 m；contact report API 也是 1/N，子 link ContactSensor 报找不到 reporter API。
- 诊断：遍历 stage，分别统计 RigidBodyAPI、disableGravity 和 PhysxContactReportAPI 的 body 覆盖数。
- 原因：`apply_nested` 默认认为 physics schema 不会嵌套，wrapped function 在根 link 成功后停止遍历 children。
- 处理过程：PR #6377 给 `apply_nested` 增加默认保持兼容的 `stop_on_success`，rigid-body/mass writers 显式设置为 false。
- 有效处理：升级到包含 PR #6377、merge commit 10144da 的版本，并用 stage traversal 验证每个 nested body 的属性。
- 结果：PR 已合并，三层嵌套刚体 regression test 同时断言 `disableGravity` 和 `physics:mass` 在 3/3 links 生效。
- 限制：#6377 只对 rigid-body 与 mass writers 放宽早停；joint、articulation root 和 collision writers 仍保留默认行为。；对曾按旧的部分生效行为调过 baseline 的 nested asset，升级后任务行为可能变化。
- 安全提示：不要只看 cfg；spawn 后应逐 body 审计最终 USD/PhysX 属性，尤其是 gravity、mass、contact report 和 depenetration limits。
- 独立核验引用：[pull_request · 已合并：rigid-body/mass writers 继续遍历 nested links，并新增 3-deep regression test](https://github.com/isaac-sim/IsaacLab/pull/6377)
- 适用边界：适用于 Isaac Sim 6.0 importer 或自定义 USD 的 body-under-body nested hierarchy。

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

### 定位 ros_control 硬实时线程中的系统调用

- `problem_id`：`problem.realtime_control_latency.ros_control_rtai_syscall_diagnostic_6`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：用 RTAI 调度统计定位 ros_control 实时线程中的系统调用**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该线程使用 RTAI 的 `/proc/rtai/scheduler` 观察实时线程是否发生系统调用，再通过逐段注释、重编译和复跑缩小调用点；原作者据此定位到当时的 `ros::Time::now()`。维护者只写了 `Fixed`，没有补丁或版本，因此这是一条旧 RTAI 环境的诊断经验，不能据此断言当前 ROS 版本仍有同一缺陷或已经在哪个版本修复。
- 证据状态：`issue_candidate`
- 来源定位：ros_control #6 排查方法 10748158；维护者无定位的 Fixed 回复 10784634
- 原帖/精确回复：[用 RTAI 调度统计定位 ros_control 实时线程中的系统调用](https://github.com/ros-controls/ros_control/issues/6#issuecomment-10748158)
- 平台/作者：GitHub Issues / advaitjain
- 关键术语：硬实时（hard realtime）；系统调用（system call）；软模式切换（hard-to-soft transition）；调度统计（scheduler statistics）
- 环境：2012 年 ROS 1 ros_control；带 RTAI 的用户态硬实时线程；具体发行版和提交未给出。
- 症状：`ros::Time::now()` 被原作者定位为会产生系统调用，意味着实时线程可能发生 hard-to-soft transition。
- 诊断：在 RTAI 实时线程中运行控制程序，同时执行 `watch cat /proc/rtai/scheduler`；若计数变化，再逐段注释、重编译和复跑以定位来源。
- 原因：原作者直接确认触发点是当时实现中的 `ros::Time::now()`；线程没有进一步解释内部调用链。
- 处理过程：使用 RTAI scheduler 统计检测系统调用，并用代码二分式注释缩小范围。
- 有效处理：原线程没有公开可定位的代码修复，只记录维护者随后回复 `Fixed`。
- 结果：该方法让原作者定位到 `ros::Time::now()`；没有发布修复后的时延数据。
- 限制：方法依赖旧 RTAI 接口，不能直接替代 PREEMPT_RT、Xenomai 或现代 tracing 工具；也没有对应的修复 commit。
- 安全提示：在真机 WBC 上应先离线或在安全工装中检查系统调用和 hard-to-soft transition，避免诊断输出本身扰动实时循环。
- 独立核验引用：[maintainer_confirmation · 维护者只确认项目侧已处理，但没有给出补丁定位](https://github.com/ros-controls/ros_control/issues/6#issuecomment-10784634)
- 适用边界：适用于旧 ROS 1 + RTAI 硬实时排查；其他实时内核应换用对应 tracing/latency 工具。

### 避免 RealtimePublisher 解锁路径触发 futex

- `problem_id`：`problem.realtime_control_latency.ros_control_realtime_publisher_unlock_futex_8`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：RealtimePublisher 解锁时的非实时等待者会破坏实时安全**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：维护者给出的直接原因是：实时线程持有发布锁时，非实时线程已经阻塞等待同一把锁；在这种状态下，实时线程随后执行 unlock 就不再是实时安全操作。原作者通过注释 `unlockAndPublish()` 和 RTAI syscall 号完成 A/B 定位。项目称默认分支已修复，但没有提供 commit 或发布版本，所以只能把该结论用于识别这种锁竞争模式。
- 证据状态：`issue_candidate`
- 来源定位：ros_control #8 syscall 观测 10822469；维护者根因与修复说明 13088686
- 原帖/精确回复：[RealtimePublisher 解锁时的非实时等待者会破坏实时安全](https://github.com/ros-controls/ros_control/issues/8#issuecomment-13088686)
- 平台/作者：GitHub Issues / advaitjain
- 关键术语：实时发布器（realtime publisher）；互斥锁（mutex）；快速用户态互斥锁（futex）；优先级反转（priority inversion）
- 环境：2012 年 ros_control；32 位 RTAI 用户态实时循环；具体提交未给出。
- 症状：调用 `unlockAndPublish()` 时出现 `LXRT CHANGED MODE (SYSCALL)`，syscall 号为 240；注释该调用后不再出现。
- 诊断：重启或重新插入 RTAI 模块后查看 dmesg 中首个 hard-to-soft syscall；原作者确认机器为 32 位，因此 240 对应 futex。
- 原因：维护者确认：实时线程持锁期间，非实时线程开始阻塞等待；此后实时线程 unlock 会进入非实时安全路径。
- 处理过程：对 `unlockAndPublish()` 做 A/B 注释，并结合 RTAI/dmesg 的 syscall 编号确认。
- 有效处理：项目维护者称已在当时默认分支修复该锁竞争路径。
- 结果：根因被维护者明确说明；线程未给修复后 syscall 计数、commit 或 release。
- 限制：结论绑定旧 ros_control/RTAI 实现；不能从该线程推断现代 `realtime_tools` 的内部实现。
- 安全提示：对 WBC 实时发布路径应在目标内核上做锁竞争压力测试，不能只在无订阅者或低负载条件下验收。
- 独立核验引用：[maintainer_confirmation · 维护者明确解释非实时等待者使 unlock 路径失去实时安全](https://github.com/ros-controls/ros_control/issues/8#issuecomment-13088686)
- 适用边界：直接适用于该线程的旧 RealtimePublisher/RTAI 实现；当前版本需重新测量。

### 把控制器切换容器清理移出实时路径

- `problem_id`：`problem.realtime_control_latency.ros_control_switch_vector_clear_10`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：控制器切换列表的 clear 操作应移出实时分支**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原作者在 `please_switch_` 的实时分支发现 vector `clear()`；维护者随后确认把这些调用移动到了非实时路径。该线程没有证明某次 `clear()` 一定发生堆分配，也没有给出 commit，因此可复用原则是审计并隔离实时路径中的容器生命周期操作，而不是把所有同名调用机械判定为故障。
- 证据状态：`issue_candidate`
- 来源定位：ros_control #10 原帖代码审查；维护者回复 13155600
- 原帖/精确回复：[控制器切换列表的 clear 操作应移出实时分支](https://github.com/ros-controls/ros_control/issues/10#issuecomment-13155600)
- 平台/作者：GitHub Issues / advaitjain
- 关键术语：实时路径（realtime path）；控制器切换（controller switching）；动态分配（dynamic allocation）；容器清理（container clearing）
- 环境：2012 年 ros_control `ControlManager.update`；具体分支和发布版本未给出。
- 症状：代码审查发现 `please_switch_` 分支内清空 STL vector，原作者质疑实时安全。
- 诊断：检查实时更新路径中的容器清理、析构和潜在内存管理操作。
- 原因：原线程将实时分支内的 vector `clear()` 视为不应保留的操作。
- 处理过程：把切换列表的 `clear()` 移到非实时切换准备阶段。
- 有效处理：维护者确认默认分支已将 `clear()` 调用移到非实时路径。
- 结果：维护者明确回复修复完成；没有给出 jitter 或分配次数对照。
- 限制：没有 commit、测试或首个修复 release；不能把所有 `clear()` 一概等同为必然分配。
- 安全提示：对实时 WBC 路径应同时做静态审查与运行时分配/系统调用检测，避免只凭 API 名称判断。
- 独立核验引用：[maintainer_confirmation · 维护者确认 clear 调用已移到非实时部分](https://github.com/ros-controls/ros_control/issues/10#issuecomment-13155600)
- 适用边界：适用于旧 ros_control 切换实现和同类实时容器生命周期审查。

### 隔离 ROS 回调与实时控制线程的数据交接

- `problem_id`：`problem.realtime_control_latency.ros_control_callback_queue_rt_buffer_130`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：把 ros_control 的周期循环与 ROS 回调线程明确分离**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：线程建议每个组件使用自己的 `CallbackQueue`，让 `AsyncSpinner` 在非实时线程处理该组件的 ROS API；实时与非实时线程之间用 `realtime_tools::RealtimeBuffer` 等实时安全结构交接数据。回复同时明确两条边界：设置变更不能让实时线程触发系统调用，非实时线程也不应锁住实时线程需要的共享资源。
- 证据状态：`issue_candidate`
- 来源定位：ros_control #130 callback/RealtimeBuffer 回复 52195810
- 原帖/精确回复：[把 ros_control 的周期循环与 ROS 回调线程明确分离](https://github.com/ros-controls/ros_control/issues/130#issuecomment-52195810)
- 平台/作者：GitHub Issues / davetcoleman
- 关键术语：回调队列（callback queue）；异步轮询器（async spinner）；实时缓冲区（realtime buffer）；优先级反转（priority inversion）
- 环境：ROS 1 ros_control；PREEMPT_RT/Xenomai 讨论；Orocos RTT 示例；2013–2018 年线程。
- 症状：直接把 ROS callbacks、services 和控制周期混在同一执行模型中，会留下调度优先级、互斥锁和系统调用边界不明确的问题。
- 诊断：明确标注 configure/read/update/write/callback 各自所在线程，并检查共享数据是否经过实时安全交换结构。
- 原因：非实时 callback 与实时循环共享普通锁，或在实时线程触发设置变更和系统调用，会产生优先级反转与不可预测时延。
- 处理过程：在 RTT `configureHook()` 构造 hardware interface 与 ControllerManager；在 `updateHook()` 执行 `read → update → write`。；为每个组件建立独立 `CallbackQueue`，由非实时线程 spin，并用 `RealtimeBuffer` 交接数据。
- 有效处理：把周期调度交给 RTT/HAL 等实时执行器，同时把 ROS API 回调隔离在非实时线程。
- 结果：线程参与者发布最小 `rtt_ros_control_example`；另一位用户明确称这些讨论帮助其开发 `hal_ros_control`。
- 限制：示例属于旧 ROS 1/RTT；`ros::Time::now()` 在同仓库另有旧实时安全问题，不能直接照抄时间源。；线程没有给统一的 WCET、jitter 或不同内核对照。
- 安全提示：真机 WBC 运行时参数必须经过边界检查和原子/实时安全交接；非实时 callback 不应持有实时线程所需的普通互斥锁。
- 独立核验引用：[maintainer_confirmation · 项目贡献者给出 per-component CallbackQueue、非实时 spinner 与 RealtimeBuffer 边界](https://github.com/ros-controls/ros_control/issues/130#issuecomment-52195810)
- 适用边界：适用于 ROS 1 ros_control 的 callback/控制周期隔离；具体无锁结构需按版本核对。

### 用外部实时执行器驱动 ros_control 周期循环

- `problem_id`：`problem.realtime_control_latency.ros_control_external_rt_read_update_write_130`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：把 ros_control 的周期循环与 ROS 回调线程明确分离**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原线程的最小结构是在 RTT `configureHook()` 中创建 hardware interface 与 `ControllerManager`，在周期 `updateHook()` 中依次执行 `robot->read()`、`controllerMgr->update(time, period)`、`robot->write()`。该模式后来被整理为 `rtt_ros_control_example`，并被另一位参与者用于实现 `hal_ros_control`。它说明的是线程组织方式，不提供现代 ROS 2 或特定硬件的实时保证。
- 证据状态：`issue_candidate`
- 来源定位：ros_control #130 最小循环 52055471；后续例子 54360309；HAL 使用反馈 407977464
- 原帖/精确回复：[把 ros_control 的周期循环与 ROS 回调线程明确分离](https://github.com/ros-controls/ros_control/issues/130#issuecomment-52055471)
- 平台/作者：GitHub Issues / davetcoleman
- 关键术语：读算写循环（read-compute-write loop）；实时执行器（realtime executor）；周期钩子（update hook）；硬件接口（hardware interface）
- 环境：ROS 1 ros_control；PREEMPT_RT/Xenomai 讨论；Orocos RTT 示例；2013–2018 年线程。
- 症状：直接把 ROS callbacks、services 和控制周期混在同一执行模型中，会留下调度优先级、互斥锁和系统调用边界不明确的问题。
- 诊断：明确标注 configure/read/update/write/callback 各自所在线程，并检查共享数据是否经过实时安全交换结构。
- 原因：非实时 callback 与实时循环共享普通锁，或在实时线程触发设置变更和系统调用，会产生优先级反转与不可预测时延。
- 处理过程：在 RTT `configureHook()` 构造 hardware interface 与 ControllerManager；在 `updateHook()` 执行 `read → update → write`。；为每个组件建立独立 `CallbackQueue`，由非实时线程 spin，并用 `RealtimeBuffer` 交接数据。
- 有效处理：把周期调度交给 RTT/HAL 等实时执行器，同时把 ROS API 回调隔离在非实时线程。
- 结果：线程参与者发布最小 `rtt_ros_control_example`；另一位用户明确称这些讨论帮助其开发 `hal_ros_control`。
- 限制：示例属于旧 ROS 1/RTT；`ros::Time::now()` 在同仓库另有旧实时安全问题，不能直接照抄时间源。；线程没有给统一的 WCET、jitter 或不同内核对照。
- 安全提示：真机 WBC 运行时参数必须经过边界检查和原子/实时安全交接；非实时 callback 不应持有实时线程所需的普通互斥锁。
- 独立核验引用：[maintainer_confirmation · 后续参与者说明讨论与示例帮助其实现 hal_ros_control](https://github.com/ros-controls/ros_control/issues/130#issuecomment-407977464)
- 适用边界：适用于旧 ROS 1 ros_control + RTT/HAL 外部实时调度器架构。

### 同步硬件模式与控制器切换时序

- `problem_id`：`problem.realtime_control_latency.ros_control_prepare_do_switch_timing_211`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：控制器模式切换的 prepareSwitch 与 doSwitch 必须分属非实时和实时阶段**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：该线程和已合并 PR #209/#210 将职责分成两层：非实时 callback 中的 `prepareSwitch()` 负责可能耗时的准备与可行性检查；真正提交硬件模式切换的 `doSwitch()` 与 controller start/stop 一起在实时 `update()` 路径发生，并必须非阻塞。这样避免硬件模式在 controller 尚未切换时提前改变。对需多个周期确认的 CANopen 等硬件，线程没有给通用策略，驱动仍必须明确切换期间旧/新命令的处理。
- 证据状态：`issue_candidate`
- 来源定位：ros_control #211 原帖真机复现；PR #209 merge 57c94c0；PR #210 merge 1ae7a0b；ros_canopen 复测 157007428
- 原帖/精确回复：[控制器模式切换的 prepareSwitch 与 doSwitch 必须分属非实时和实时阶段](https://github.com/ros-controls/ros_control/issues/211)
- 平台/作者：GitHub Issues / adolfo-rt
- 关键术语：模式切换（mode switching）；非实时准备（non-realtime preparation）；原子提交（atomic commit）；实时安全（realtime safe）
- 环境：ROS 1 ros_control Indigo/Jade；作者在硬件复现；ros_canopen 参与者报告典型切换需 3–4 个周期，部分硬件 5 个以上。
- 症状：旧实现可能先切硬件模式、后启动新 controller，导致命令落入错误模式或出现未定义行为。
- 诊断：审计 `prepareSwitch/doSwitch/controller start-stop` 的调用线程和实际顺序，并记录硬件模式确认所需周期。
- 原因：`doSwitch()` 错放在只负责调度切换的非实时 ROS callback，而 controller start/stop 实际在实时 update 线程发生。
- 处理过程：PR #209/#210 保存 start/stop list，把 `doSwitch()` 移到实时 `update()`，并用非实时 `prepareSwitch()` 做可阻塞准备。
- 有效处理：采用 `prepareSwitch()` 非实时准备 + `doSwitch()` 实时、非阻塞提交的两阶段接口。
- 结果：PR #209 和 #210 均已合并；#209 修订后测试通过；ros_canopen 参与者确认在 Indigo 变更上按预期工作。
- 限制：这是 ROS 1 Indigo/Jade 历史接口；慢速硬件仍需自行定义切换期间的命令保持、丢弃和同步策略。；线程对是否允许多周期切换有过争论，最终合并方案不等同于任意硬件都能单周期完成物理模式切换。
- 安全提示：真机模式切换应先在吊架/空载和低增益条件验证，监控旧/新命令、硬件 mode acknowledgement 与急停状态；不得在实时 `doSwitch()` 中阻塞等待总线。
- 独立核验引用：[pull_request · Indigo 修复已合并，merge commit 57c94c096796aabe59f10625cf28e839e85f6415](https://github.com/ros-controls/ros_control/pull/209)；[pull_request · Jade 修复已合并，merge commit 1ae7a0b201d1a1aea49a7fa8e6b0fee92b4775fd](https://github.com/ros-controls/ros_control/pull/210)；[independent_reproduction · ros_canopen 参与者确认 Indigo 变更按预期工作](https://github.com/ros-controls/ros_control/pull/210#issuecomment-157007428)
- 适用边界：直接适用于 ROS 1 Indigo/Jade 历史接口；现代 ros2_control 需按当前 lifecycle/switch API 重新核对。

### 建立 1 kHz WBC 的 PREEMPT_RT 延迟基线

- `problem_id`：`problem.realtime_control_latency.ros2_control_preempt_rt_cyclictest_acpi_118`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：用 cyclictest 先建立 PREEMPT_RT 主机抖动基线**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：该线程使用 `cyclictest -a -t -n -p99` 记录每个实时线程的 Min/Avg/Max，并把最大延迟与 1 ms 周期、约 800 µs 计算预算比较。在作者单机上，不含 ACPI 的 Linux 5.4.47 RT 内核 Max 为 30–45 µs，而含 ACPI 时报告 7000–8000 µs。这个结果只能提示先做内核配置 A/B，不能把关闭 ACPI 当作普适修复；线程也没有完成 ros2_control 的端到端实时测试。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #118 目标与 TODO；cyclictest/ACPI 结果 656812972
- 原帖/精确回复：[用 cyclictest 先建立 PREEMPT_RT 主机抖动基线](https://github.com/ros-controls/ros2_control/issues/118#issuecomment-656812972)
- 平台/作者：GitHub Issues / olivier-stasse
- 关键术语：抢占实时内核（PREEMPT_RT）；周期抖动（cycle jitter）；最坏执行时间（worst-case execution time, WCET）；长尾延迟（tail latency）
- 环境：Linux 5.4.47 + RT_PREEMPT；四个 cyclictest 线程；作者自建机器；未给 CPU 型号和持续时长之外的完整负载矩阵。
- 症状：保留 ACPI 的内核在该机出现 7000–8000 µs 最大延迟，远超 1 ms 周期；不编译 ACPI 时记录为 30–45 µs。
- 诊断：运行 `sudo ./cyclictest -a -t -n -p99`，至少记录每线程 Min/Avg/Max，并与控制周期和求解预算比较。
- 原因：原作者把该机的巨大差异与 ACPI 配置相关联；线程没有做跨主机或固件设置消融。
- 处理过程：比较包含/不包含 ACPI 的内核配置，并配置自托管 RT runner。
- 有效处理：该线程没有完成 ros2_control 集成测试；只得到不含 ACPI 配置下更低的单机 cyclictest 基线。
- 结果：不含 ACPI 时四线程 Max 为 30、40、45、40 µs；含 ACPI 时作者报告 7000–8000 µs。
- 限制：单机、旧内核、没有 CPU/BIOS/负载完整信息；关闭 ACPI 可能影响电源、温控和设备功能，不能直接用于生产机器人。；TODO 中的 ros2_control 实时测试和 CI 集成未完成。
- 安全提示：内核配置改动应先验证温控、急停、总线和设备枚举；WBC 上线还需在真实负载下测端到端 WCET，而不是只看 cyclictest。
- 独立核验引用：[issue · 原线程保留未完成的实时测试与 CI 集成 TODO](https://github.com/ros-controls/ros2_control/issues/118)
- 适用边界：适用于建立 PREEMPT_RT 主机基线；数值只属于原线程机器。

### 正确配置 controller_manager 的 memlock 上限

- `problem_id`：`problem.realtime_control_latency.ros2_control_memlock_limit_2020`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：controller_manager 内存锁定不能沿用过小的固定 memlock 上限**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：该线程中，原作者把 memlock 改为 `unlimited` 后警告消失；第二位用户证明简单扩大到 `1024000` 只让节点先启动，随后仍可能 `std::bad_alloc`，改成 unlimited。项目成员确认 unlimited 可用，并把 `lock_memory=false` 作为明确放弃内存锁定时的备选。工程上应核对进程峰值内存和 page fault，而不是复制旧的 102400 或任意十倍值。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #2020 原帖 A/B；第二用户 bad_alloc 2660327112；项目确认 2660331588
- 原帖/精确回复：[controller_manager 内存锁定不能沿用过小的固定 memlock 上限](https://github.com/ros-controls/ros2_control/issues/2020#issuecomment-2660331588)
- 平台/作者：GitHub Issues / KmakD
- 关键术语：内存锁定（memory locking）；锁定上限（memlock limit）；缺页异常（page fault）；内存分配失败（bad allocation）
- 环境：原帖：Ubuntu、ROS 2 Humble、RPi 4、自定义 RT kernel；复现者：Ubuntu 24.04 Jazzy + PREEMPT_RT、ur_robot_driver。
- 症状：102400 限额时报 `Unable to lock the memory`；1024000 可启动但复现者随后遇到 `std::bad_alloc`。
- 诊断：比较当前 shell/process 的 memlock limit、controller_manager `lock_memory` 参数和进程实际虚拟内存需求；不要只看启动瞬间。
- 原因：固定 102400 字节不足以覆盖 controller_manager 需要锁定的内存；十倍固定值对另一环境仍不足。
- 处理过程：原作者把 soft/hard memlock 改为 unlimited；第二位用户先试 1024000，出现 bad_alloc 后改为 unlimited。
- 有效处理：两位参与者采用 unlimited；项目成员确认该设置可用。若明确接受不锁内存，可把 `lock_memory` 设为 false。
- 结果：原作者 unlimited 后警告消失；第二位用户确认固定十倍值不足，项目成员确认其环境 unlimited 正常。
- 限制：`lock_memory=false` 会放弃该内存锁定保证，不是等价实时修复。；线程没有给不同机器人、DDS 和控制器组合所需的最小可审计字节数；unlimited 仍受系统和部署策略约束。
- 安全提示：真机前应在峰值控制器/消息负载下检查 page fault、RSS、OOM 和周期抖动；不要用任意固定倍数替代容量验证。
- 独立核验引用：[maintainer_confirmation · 项目成员确认 unlimited，并说明 lock_memory=false 的语义](https://github.com/ros-controls/ros2_control/issues/2020#issuecomment-2660331588)
- 适用边界：适用于 Humble/Jazzy controller_manager 内存锁定；部署系统的 limits/PAM/container 配置需分别核对。

### 让 Jazzy hardware interface 日志进入 rosout

- `problem_id`：`problem.realtime_control_latency.ros2_control_hardware_child_logger_2113`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Jazzy 硬件组件应使用继承自 ControllerManager 的 get_logger**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：从 Jazzy 起，hardware component 提供继承自 ControllerManager 的 child logger。原作者升级 Jazzy 后把 `rclcpp::get_logger("hardware_interface")` 改为组件的 `get_logger()`，并确认 Foxglove 能看到日志；维护者链接的官方 demo 也使用该写法。该结论不包含 Iron backport，也不代表可以在实时 read/write 循环高频打印。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #2113 维护者版本说明 2735617665；作者复测 2764284744；官方 demo rrbot.cpp
- 原帖/精确回复：[Jazzy 硬件组件应使用继承自 ControllerManager 的 get_logger](https://github.com/ros-controls/ros2_control/issues/2113#issuecomment-2764284744)
- 平台/作者：GitHub Issues / zacharyyamaoka
- 关键术语：子日志器（child logger）；硬件组件（hardware component）；日志聚合（log aggregation）；实时日志限频（realtime log throttling）
- 环境：原始环境 ROS 2 Iron；作者升级到 Jazzy 后验证；自定义 Moteus hardware interface；Foxglove。
- 症状：`RCLCPP_INFO(rclcpp::get_logger("hardware_interface"), ...)` 在终端可见，但 `/rosout`/Foxglove 不显示。
- 诊断：确认 distro 是否提供 hardware component child logger，并比较 standalone logger 与组件 `get_logger()` 的 rosout 行为。
- 原因：Iron 中使用的独立 logger 没有关联到 ControllerManager node 的 rosout publisher；Jazzy 提供 child logger。
- 处理过程：升级到 Jazzy，并把宏参数改为组件 `get_logger()`。
- 有效处理：在 Jazzy hardware component 内使用 `RCLCPP_INFO(get_logger(), ...)`。
- 结果：原作者明确确认日志随后能在 Foxglove 中显示；官方 ros2_control demo 源码给出同一用法。
- 限制：该接口边界从 Jazzy 起成立，Iron 不应直接假定可用；线程没有给 backport。；实时 `read/write` 高频路径中的日志仍可能破坏时序，本卡只回答 logger 归属。
- 安全提示：故障日志应限频，并把实时状态采样与非实时发布分离；不要在高频 WBC 循环用日志代替 watchdog。
- 独立核验引用：[source_code · 维护者直接链接的 Jazzy-era 官方 hardware demo 使用 get_logger()](https://github.com/ros-controls/ros2_control_demos/blob/5bef8b48d66b5e673bf8ef63affa94f1049963ee/example_1/hardware/rrbot.cpp#L45)
- 适用边界：适用于 ROS 2 Jazzy 及含同一 hardware child logger API 的版本。

### 定位 controller_manager 零订阅者时的 statistics 空闲开销

- `problem_id`：`problem.realtime_control_latency.ros2_control_pal_statistics_idle_cpu_3356`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：零订阅者时 pal_statistics worker 仍可能消耗小型主机 CPU**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原作者依次排除 executor、controller、RT update thread 和 RMW，再在 overlay 中禁用两个 registry 的初始化、worker 启动与每周期 async publish；两个热线程消失，进程 CPU 约从 13% 降到 1%。这证明了该环境中的开销定位，但没有维护者确认或上游修复。作者 patch 会完全删除观测 topic，不能当作生产修复；subscriber-count gate 也仍只是建议。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #3356 完整 reproducer、线程排除和 overlay A/B；唯一评论为 stale bot
- 原帖/精确回复：[零订阅者时 pal_statistics worker 仍可能消耗小型主机 CPU](https://github.com/ros-controls/ros2_control/issues/3356)
- 平台/作者：GitHub Issues / techjoec
- 关键术语：空闲开销（idle overhead）；上下文切换（context switch）；内省发布器（introspection publisher）；订阅者门控（subscriber-count gating）
- 环境：ROS 2 Jazzy，ros2_control 4.44.0-1noble；Ubuntu Noble 6.8；Docker x86_64；CycloneDDS 与 Fast DDS；master 2026-05-27 也复现。
- 症状：两个普通优先级 worker 各约 5–7% CPU、约 2000 context switches/s；RT update thread 约 0.1%。
- 诊断：检查 topic subscription count、`ps -T`、线程调度类/CPU/wchan；分别切换 executor、controllers、RMW，再用 overlay 禁用 registry/publish sites 做 A/B。
- 原因：作者的行为 A/B 将开销定位到两个 pal_statistics registry worker 的每周期唤醒/交接路径；没有维护者确认更细的内部根因。
- 处理过程：SingleThreadedExecutor、停用 controllers、DDS 调优均无变化；`#if 0` 禁用两个 registry 和 async publish sites 后热线程消失。
- 有效处理：作者的本地 workaround 会彻底关闭 introspection/statistics topics，不具备上游合入质量；建议的 subscriber-count gate 尚未实现。
- 结果：overlay A/B 后 `ros2_control_node` 从约 13% 降到约 1%，容器总 CPU 从约 22% 降到约 9%。
- 限制：只有原作者复现，Issue 无维护者技术回复或合并 PR；具体 CPU 百分比不能外推到其他主机。；禁用 registry 会失去观测能力，subscriber gate 仍只是作者建议。
- 安全提示：真机若临时关闭 introspection，必须保留独立 watchdog、故障状态和关键安全遥测；CPU 优化不能以丢失安全观测为代价。
- 独立核验引用：[source_code · 原帖固定 Jazzy/master 行号并给出完整 overlay A/B patch；尚无项目方确认](https://github.com/ros-controls/ros2_control/issues/3356)
- 适用边界：适用于该 Jazzy/master + Docker/SBC 类环境的诊断；数值与补丁不可直接外推。

### ros2_control 实时循环被 I2C IMU 读取拖慢

- `problem_id`：`problem.realtime_control_latency.ros2_control_i2c_imu_jitter_1574`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ros2_control 控制循环高抖动与 update period 异常必须拆开排查**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：作者在配置 realtime group limits、尝试 chrt 后仍看到抖动，随后用 A/B 确认是读取 I2C IMU 导致；停读后，即使仅使用 low-latency kernel，循环也很稳定。线程没有给异步化或驱动层最终实现，所以可执行的结论是先把该 I/O 从实时路径隔离并复测，而不是声称某种线程方案已被验证。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #1574 评论 2183981102
- 原帖/精确回复：[ros2_control 控制循环高抖动与 update period 异常必须拆开排查](https://github.com/ros-controls/ros2_control/issues/1574#issuecomment-2183981102)
- 平台/作者：GitHub Issues / Nate711
- 关键术语：控制循环抖动（control-loop jitter）；低延迟内核（low-latency kernel）；实时调度优先级（real-time scheduling priority）；阻塞式 I/O（blocking I/O）
- 环境：Raspberry Pi 5；controller_manager 250 Hz；low-latency kernel；realtime group limits 后续已配置；未给 ROS 2/ros2_control 精确版本。
- 症状：实际时间差在约 1.1-6.9 ms 之间波动，update() 的 period 参数与作者离线时间差不一致。
- 诊断：先移除或隔离 I2C IMU 读取，观察控制周期抖动是否消失。；不要用同一现象替 period 参数定性；在 ros2_control node 同一位置同时打印 current_time、previous_time、measured_period。
- 原因：作者确认大抖动来自 I2C IMU 读取；period 参数异常仍未定位。
- 处理过程：配置 realtime group limits；用 chrt 调整进程及子进程优先级；停用 I2C IMU 读取；维护者建议同点打印时间变量。
- 有效处理：针对循环抖动，移除/隔离该 I2C IMU 读取后作者观察到循环稳定。
- 结果：I2C 引起的抖动已由作者 A/B 确认；update period 参数问题没有闭环。
- 限制：线程没有说明采用异步 I/O、独立线程或具体驱动修复，只确认停读后稳定。；不能把低延迟内核下的结果直接外推到所有硬件和 RT kernel。
- 安全提示：传感器读取不要无界阻塞实时控制线程；应监控 worst-case execution time 和 deadline miss。
- 独立核验引用：[issue · 作者停用 I2C IMU 读取后循环稳定的 A/B 结果](https://github.com/ros-controls/ros2_control/issues/1574#issuecomment-2183981102)
- 适用边界：Raspberry Pi 5、250 Hz、low-latency kernel 且实时路径直接读取 I2C IMU 的场景。

### ros2_control controller update 的 period 参数与实测时间差不一致

- `problem_id`：`problem.realtime_control_latency.ros2_control_update_period_unresolved_1574`
- 问题综合等级：**需要实际验证** — 现有来源主要提供问题线索或待复现经验，建议在目标系统中逐项核对。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ros2_control 控制循环高抖动与 update period 异常必须拆开排查**

- 独立等级：**需要实际验证** — 解答尚未闭环或存在冲突；当前仅形成问题线索；尚未形成可核对的复现记录。
- 解答状态：`unresolved`
- 候选解答：没有。作者在排除 I2C 抖动后仍认为 period 参数不正确；维护者无法在普通 PC 复现，并要求在 ros2_control node 内同时打印 current_time、previous_time、measured_period。线程到此结束，因此只能保留诊断步骤，不能自行给出 period 计算错误的根因或修复。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #1574 评论 2183981102、2183982425、2183984139
- 原帖/精确回复：[ros2_control 控制循环高抖动与 update period 异常必须拆开排查](https://github.com/ros-controls/ros2_control/issues/1574#issuecomment-2183984139)
- 平台/作者：GitHub Issues / Nate711
- 关键术语：控制器周期参数（controller period parameter）；测量周期（measured period）；当前/前一时间戳（current/previous timestamp）
- 环境：Raspberry Pi 5；controller_manager 250 Hz；low-latency kernel；realtime group limits 后续已配置；未给 ROS 2/ros2_control 精确版本。
- 症状：实际时间差在约 1.1-6.9 ms 之间波动，update() 的 period 参数与作者离线时间差不一致。
- 诊断：先移除或隔离 I2C IMU 读取，观察控制周期抖动是否消失。；不要用同一现象替 period 参数定性；在 ros2_control node 同一位置同时打印 current_time、previous_time、measured_period。
- 原因：作者确认大抖动来自 I2C IMU 读取；period 参数异常仍未定位。
- 处理过程：配置 realtime group limits；用 chrt 调整进程及子进程优先级；停用 I2C IMU 读取；维护者建议同点打印时间变量。
- 有效处理：针对循环抖动，移除/隔离该 I2C IMU 读取后作者观察到循环稳定。
- 结果：I2C 引起的抖动已由作者 A/B 确认；update period 参数问题没有闭环。
- 限制：线程没有说明采用异步 I/O、独立线程或具体驱动修复，只确认停读后稳定。；不能把低延迟内核下的结果直接外推到所有硬件和 RT kernel。
- 安全提示：传感器读取不要无界阻塞实时控制线程；应监控 worst-case execution time 和 deadline miss。
- 独立核验引用：[issue · 维护者无法在普通 PC 复现并继续询问时间来源](https://github.com/ros-controls/ros2_control/issues/1574#issuecomment-2183982425)
- 适用边界：Raspberry Pi 5 上的该线程记录；缺少精确 ros2_control 版本且维护者未复现。

### ros2_control 多硬件 rw_rate 抖动导致额外跳周期

- `problem_id`：`problem.realtime_control_latency.ros2_control_rw_rate_skipped_cycles_2089`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ros2_control 多硬件 rw_rate 应按当前执行与跳过后的时间误差择近**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：PR #2091 不再只用固定 0.99 阈值判断是否过频，而是比较现在执行与再跳一个 controller-manager 周期后执行，哪一种对目标 rw_rate 的时间误差更小。作者在多组频率、mock 组件和 UR16e+KR50 真机上测试；真机 read/write 跳过均降到 0.01% 以下。该 PR 已合并。不可整除频率仍会量化，需按目标组合验收。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #2089 评论 2695374172、2698322050；PR #2091；merge commit bfbedd2c1c7487f3c6d424c58a0b6d1c79e161c9
- 原帖/精确回复：[ros2_control 多硬件 rw_rate 应按当前执行与跳过后的时间误差择近](https://github.com/ros-controls/ros2_control/issues/2089#issuecomment-2698322050)
- 平台/作者：GitHub Issues / RobertWilbrandt
- 关键术语：读写频率（read/write rate, rw_rate）；控制管理器更新率（controller-manager update rate）；周期抖动（periodicity jitter）；跳过周期（skipped cycle）
- 环境：Ubuntu 24.04.1 LTS；ROS 2 Jazzy；ros2_control 源码构建；UR16e 500 Hz、KUKA KR50 250 Hz；另有 mock 测试。
- 症状：慢硬件期望约 4 ms 调用，实际频繁跳到约 6 ms，表现为运动 stutter。；约 500 秒 trace 中 write 超过 5 ms 的比例 20.5%，read 为 0.74%。
- 诊断：记录 read/write 周期分布，不只看平均频率。；比较降低固定阈值与基于 timing error 的调度。；覆盖 100/150/250/333 Hz 与 controller_manager 500/1000 Hz。
- 原因：原逻辑只检查调用是否过频；快接口执行抖动会让慢接口落到 0.99 阈值下并额外跳过一个周期。
- 处理过程：0.98 和 0.97 阈值只减少跳过；作者改为比较本周期执行与下周期执行的时间误差。；先 mock、多频率测试，再在 UR16e+KR50 真机测试。
- 有效处理：采用已合并 PR #2091 的 rw_rate timing-error 选择逻辑。
- 结果：真机 trace 中 read/write 跳过均低于 0.01%；PR #2091 获维护者审核、测试覆盖并合并。
- 限制：150 Hz 相对 500/1000 Hz 不能整除时，线程数据显示实际频率会量化到 166.66 或 142.87 Hz；不能承诺任意目标频率精确命中。；作者认为剩余极少跳过可能与无 RT/low-latency kernel 的测试环境有关，但这是其判断，不是独立结论。
- 安全提示：多硬件系统升级调度算法后，应在禁动力或低速模式下检查每个接口的周期分布和 missed cycles。
- 独立核验引用：[pull_request · 合并 PR，含真实硬件结果、单元测试和 merge commit bfbedd2](https://github.com/ros-controls/ros2_control/pull/2091)
- 适用边界：ROS 2 Jazzy、ros2_control 多硬件组件且 rw_rate 低于 controller_manager update_rate 的场景。

### ros2_control RT/non-RT 共享锁的优先级继承改造

- `problem_id`：`problem.realtime_control_latency.ros2_control_pi_recursive_mutex_3145`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：ros2_control 实时路径共享递归锁改用优先级继承 mutex**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：维护者没有采用 atomic flag 搬移发布，而是要求使用 realtime_tools 已有的 priority-inheritance recursive mutex。PR #3197 将 controllers_lock_ 及全部调用点迁移到 realtime_tools::prio_inherit_recursive_mutex，Windows 保留 std::recursive_mutex 回退；PR 经 review 和测试后合并。它解决的是源码层面的优先级反转风险，不应写成已经量化了 jitter 改善。
- 证据状态：`issue_candidate`
- 来源定位：ros2_control #3145 评论 4160585534、4191555039、4200304531；PR #3197；merge commit 308e4aab78958b730d847c0054c69f2cefabd8db
- 原帖/精确回复：[ros2_control 实时路径共享递归锁改用优先级继承 mutex](https://github.com/ros-controls/ros2_control/issues/3145#issuecomment-4200304531)
- 平台/作者：GitHub Issues / shlok-mehndiratta
- 关键术语：优先级反转（priority inversion）；优先级继承互斥锁（priority-inheritance mutex）；实时线程（real-time thread）；递归互斥锁（recursive mutex）
- 环境：ros2_control master commit a03be840 发现问题；PR 在 ROS 2 Rolling 构建验证；POSIX 使用 realtime_tools PI mutex，Windows 回退 std::recursive_mutex。
- 症状：这是源码审计发现的潜在 priority inversion/jitter 风险，线程没有给出机器人上的实测卡顿或 benchmark。
- 诊断：从 SCHED_FIFO update() 追踪 fallback activation 到 publish_activity()，再检查 controllers_lock_ 是否也被 executor/service 路径持有。
- 原因：标准 recursive_mutex 不提供此处需要的优先级继承，低优先级线程持锁时可能阻塞 RT 线程。
- 处理过程：最初 PoC 用 atomic flag 进行 RT→non-RT 触发；维护者选择更小范围的 PI recursive mutex 替换。
- 有效处理：PR #3197 将 controllers_lock_ 迁移为 realtime_tools::prio_inherit_recursive_mutex，并保留 Windows 回退。
- 结果：PR 获两位维护者批准、修改行测试覆盖后合并。
- 限制：合并证明代码方案被接受，不证明原路径曾产生可测 jitter，也不提供性能改善数值。；Windows 回退路径没有 PI mutex，适用性不同。
- 安全提示：锁替换后仍应在 fallback、服务并发和控制器切换压力场景测量最坏延迟。
- 独立核验引用：[pull_request · 已合并 PI recursive mutex 迁移，merge commit 308e4aa，含 review 与测试覆盖](https://github.com/ros-controls/ros2_control/pull/3197)
- 适用边界：ros2_control controller_manager 使用共享 controllers_lock_ 的 POSIX 平台；Windows 为标准 mutex 回退。

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

### H2O 用 privileged teacher 和 0.5m 逐帧阈值过滤重定向动作

- `problem_id`：`problem.retargeting_dataset_quality.h2o_teacher_motion_filter_6`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：H2O 数据清洗用无随机化 privileged teacher 逐帧筛除跟踪距离超过 0.5m 的动作**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：原项目作者给出的流程是：先完成整个 AMASS 的目标机器人重定向；训练不使用 domain randomization 和 penalty reward 的 privileged teacher；逐条评估动作，只要任一 timestep 的 reference motion distance 超过 0.5 m，就过滤整条 motion。作者同时确认公开的 amass_phc_filtered.pkl 是该流程结果。对其他机器人必须重新验证 distance 定义和阈值。
- 证据状态：`issue_candidate`
- 来源定位：human2humanoid #6：项目作者评论 2417970533 给出完整流程与 >0.5m 条件；2418826815 确认公开 filtered 文件
- 原帖/精确回复：[H2O 数据清洗用无随机化 privileged teacher 逐帧筛除跟踪距离超过 0.5m 的动作](https://github.com/LeCAR-Lab/human2humanoid/issues/6#issuecomment-2417970533)
- 平台/作者：GitHub Issues / Perkins729
- 关键术语：特权教师策略（privileged teacher policy）；领域随机化（domain randomization）；动作可行性筛选（motion feasibility filtering）；参考动作距离（reference motion distance）
- 环境：H2O/human2humanoid 数据清洗流程；完整 AMASS retargeting；privileged teacher；原帖未给 commit、训练步数和距离具体定义代码。
- 症状：仅有重定向后的动作文件，无法区分目标机器人可稳定跟踪与不可跟踪的 reference motions。
- 诊断：先保证所有 AMASS motion 已完成目标机器人重定向，再用不含随机化/惩罚的 teacher 做逐动作 rollout。；逐 timestep 计算项目定义的 reference motion distance，并记录首次超过 0.5 m 的动作。
- 原因：动作在几何上完成重定向不代表目标机器人动力学上可跟踪，需要 privileged teacher 作为 feasibility test。
- 处理过程：提问者询问是否直接训练 teacher，并用 teacher 输出得到 amass_phc_filtered.pkl；项目作者确认该方向。
- 有效处理：用无 domain randomization、无 penalty reward 的 privileged teacher 评估全部动作；任一时刻 reference motion distance > 0.5 m 就剔除整条 motion。
- 结果：项目作者确认公开 amass_phc_filtered.pkl 是上述数据处理结果。
- 限制：0.5 m 是 H2O 线程给出的项目判据，不能不经验证直接用于不同机器人、距离定义或动作尺度。；线程没有给出 distance 所包含的 body、聚合方式、teacher 训练预算和失败率。
- 安全提示：对新机器人应保留被过滤动作和失败轨迹用于审计，并重新标定阈值，避免只依据单一距离掩盖跌倒、力矩或接触失败。
- 独立核验引用：[maintainer_confirmation · 项目作者给出 full-AMASS retarget、无随机化/惩罚 teacher 和任一帧 >0.5m 剔除规则](https://github.com/LeCAR-Lab/human2humanoid/issues/6#issuecomment-2417970533)；[maintainer_confirmation · 项目作者确认 amass_phc_filtered.pkl 是上述流程产物](https://github.com/LeCAR-Lab/human2humanoid/issues/6#issuecomment-2418826815)
- 适用边界：直接适用于 H2O 原训练数据清洗；迁移到其他机器人或距离度量时需重新校准。

### PHC 自定义 XML 的无-joint 中间 body 导致 rotations_world/g_rot 索引缺失

- `problem_id`：`problem.retargeting_dataset_quality.phc_body_without_joint_grot_96`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：自定义机器人 PHC 重定向需分别检查 SMPL T-pose 与无 joint body 的 FK 索引**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原作者确认自定义 XML 中有许多 body 完全没有 joint，而且不只是 end effectors；PHC 的 FK population 因而没有为这些索引生成 rotation tensor。其本地 workaround 是给这些 body 添加活动范围极小、近似静止的 joint，使索引被完整填充。该方法没有上游验证且会改变模型拓扑，只能作为需实际复测的预处理经验；更稳妥的实现仍应检查 FK/parser 对 fixed bodies 的支持。
- 证据状态：`issue_candidate`
- 来源定位：PHC #96：评论 2469949721 打印 65 bodies/51 valid indexes；2471993047 原作者自答无-joint body 根因与 near-static joint workaround
- 原帖/精确回复：[自定义机器人 PHC 重定向需分别检查 SMPL T-pose 与无 joint body 的 FK 索引](https://github.com/ZhengyiLuo/PHC/issues/96#issuecomment-2471993047)
- 平台/作者：GitHub Issues / ghost
- 关键术语：前向运动学（forward kinematics, FK）；旋转张量（rotation tensor）；无关节刚体（body without a joint）；近静态关节（near-static joint）
- 环境：human2humanoid grad_fit_shape/grad_fit 与 PHC fit_smpl_shape/fit_smpl_motion；自定义 MJCF/XML 和 robot.yaml；原帖未给 commit、OS 或库版本。
- 症状：错误渲染中机器人明显不对称，一侧手臂下垂、腿和脚交叠；Isaac Gym 对照是双臂水平、双腿分开的 T-pose。；作者报告 shape-fit loss 由 200+ 降至约 40。；J/bodies 长度为 65，但 rotations_world/g_rot 只有 51 个有效索引；某些位置出现 shape=(1,90,0,3,3) 的空 tensor。
- 诊断：用 +vis=True 对照 SMPL 与 robot matched joints，检查 robot.yaml 的 smpl_pose_modifier 是否让 SMPL 与机器人处于同一 T-shape。；逐 body 检查 XML 是否存在非末端 body 完全没有 joint，并比较 body_names、parents、rotations_world/g_rot 的有效索引数量。
- 原因：shape fitting 只改变 betas 和 scale，不能替错误的 SMPL base pose；smpl_pose_modifier 不对齐会让关键点初始姿态错误。；PHC FK 实现假设所遍历 body 能产生对应 rotation entry；自定义 XML 的无-joint 中间 body 打破了该假设。
- 处理过程：作者先确认运行过 shape fitting，并检查 joint_matches；答复者引导检查 smpl_pose_modifier/T-shape。；作者继续打印 rotations_world，定位到 index 37 等位置没有 tensor。
- 有效处理：把 robot.yaml 的 smpl_pose_modifier 调整为与目标机器人一致的 T-shape；若姿态正确再增加 fitting iterations。；原作者的 XML workaround 是给先前完全无 joint 的 body 添加活动范围极小、近似静止的 joint，使 FK 索引完整。
- 结果：修正 pose modifier 后，作者报告可视匹配明显改善且 loss 从 200+ 降到约 40。；原作者随后明确发布无-joint body 的原因与加近静态 joint 的解决方案，并关闭 PHC Issue。
- 限制：改进后的散点图没有图例、单位或逐 joint 数值，不能从颜色猜测哪组是 SMPL/robot，也不能证明 motion-level tracking 已通过。；给 body 添加 near-static movable joint 会改变模型拓扑，可能影响自由度、惯量、控制和导出；线程没有上游认可或动力学回归。；作者后续仍说会继续调整 robot.yaml 降低 loss，约 40 不是通用验收阈值。
- 安全提示：重定向模型修改后必须重新核对 nq/nv、joint order、inertia、limits 和 FK，并把预处理模型与真实控制模型的差异显式记录。
- 图片分析：三张关键图已核验：错误渲染为明显不对称灰色人形，一侧手臂下垂、双腿和脚在下方交叠；Isaac Gym 对照为双臂水平、双腿分开的近 T-pose；修正后散点图中多数红/蓝关键点成对接近。散点图没有图例、单位或误差数值，因此只支持“对齐明显改善”，不用于判定具体 joint 含义或最终 motion 精度。
- 独立核验引用：[issue · 原作者给出 J/bodies=65、g_rot=51 和空 tensor 的具体索引诊断](https://github.com/ZhengyiLuo/PHC/issues/96#issuecomment-2469949721)；[issue · 原作者确认 XML 中无-joint body 是根因，并发布 near-static joint workaround](https://github.com/ZhengyiLuo/PHC/issues/96#issuecomment-2471993047)
- 适用边界：适用于原作者自定义 MJCF/XML 与 PHC FK 实现；任何控制/仿真模型采用前必须重新核对拓扑和动力学。

### PHC shape fitting 只调 betas/scale，SMPL pose modifier 必须先对齐 T-pose

- `problem_id`：`problem.retargeting_dataset_quality.phc_smpl_pose_modifier_tpose_96`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：自定义机器人 PHC 重定向需分别检查 SMPL T-pose 与无 joint body 的 FK 索引**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`resolved`
- 候选解答：检查 robot.yaml 的 smpl_pose_modifier，确保 SMPL 初始姿态与目标机器人同为对齐的 T-shape。线程答复者解释 shape fitting 只优化 betas 和 scale，只改变骨段长度，不能修正错误基础姿态；原作者调整后报告 loss 从 200+ 降到约 40、关键点明显更接近。姿态正确后才考虑增加 fitting iterations。
- 证据状态：`issue_candidate`
- 来源定位：human2humanoid #18 链接 PHC #96；PHC 评论 2469828963 解释 smpl_pose_modifier/T-shape，2469949721 原作者报告 loss 改善
- 原帖/精确回复：[自定义机器人 PHC 重定向需分别检查 SMPL T-pose 与无 joint body 的 FK 索引](https://github.com/ZhengyiLuo/PHC/issues/96#issuecomment-2469828963)
- 平台/作者：GitHub Issues / ghost
- 关键术语：形状参数（shape parameters, betas）；尺度参数（scale parameter）；标准 T 姿态（T-pose）；姿态修饰器（pose modifier）
- 环境：human2humanoid grad_fit_shape/grad_fit 与 PHC fit_smpl_shape/fit_smpl_motion；自定义 MJCF/XML 和 robot.yaml；原帖未给 commit、OS 或库版本。
- 症状：错误渲染中机器人明显不对称，一侧手臂下垂、腿和脚交叠；Isaac Gym 对照是双臂水平、双腿分开的 T-pose。；作者报告 shape-fit loss 由 200+ 降至约 40。；J/bodies 长度为 65，但 rotations_world/g_rot 只有 51 个有效索引；某些位置出现 shape=(1,90,0,3,3) 的空 tensor。
- 诊断：用 +vis=True 对照 SMPL 与 robot matched joints，检查 robot.yaml 的 smpl_pose_modifier 是否让 SMPL 与机器人处于同一 T-shape。；逐 body 检查 XML 是否存在非末端 body 完全没有 joint，并比较 body_names、parents、rotations_world/g_rot 的有效索引数量。
- 原因：shape fitting 只改变 betas 和 scale，不能替错误的 SMPL base pose；smpl_pose_modifier 不对齐会让关键点初始姿态错误。；PHC FK 实现假设所遍历 body 能产生对应 rotation entry；自定义 XML 的无-joint 中间 body 打破了该假设。
- 处理过程：作者先确认运行过 shape fitting，并检查 joint_matches；答复者引导检查 smpl_pose_modifier/T-shape。；作者继续打印 rotations_world，定位到 index 37 等位置没有 tensor。
- 有效处理：把 robot.yaml 的 smpl_pose_modifier 调整为与目标机器人一致的 T-shape；若姿态正确再增加 fitting iterations。；原作者的 XML workaround 是给先前完全无 joint 的 body 添加活动范围极小、近似静止的 joint，使 FK 索引完整。
- 结果：修正 pose modifier 后，作者报告可视匹配明显改善且 loss 从 200+ 降到约 40。；原作者随后明确发布无-joint body 的原因与加近静态 joint 的解决方案，并关闭 PHC Issue。
- 限制：改进后的散点图没有图例、单位或逐 joint 数值，不能从颜色猜测哪组是 SMPL/robot，也不能证明 motion-level tracking 已通过。；给 body 添加 near-static movable joint 会改变模型拓扑，可能影响自由度、惯量、控制和导出；线程没有上游认可或动力学回归。；作者后续仍说会继续调整 robot.yaml 降低 loss，约 40 不是通用验收阈值。
- 安全提示：重定向模型修改后必须重新核对 nq/nv、joint order、inertia、limits 和 FK，并把预处理模型与真实控制模型的差异显式记录。
- 图片分析：三张关键图已核验：错误渲染为明显不对称灰色人形，一侧手臂下垂、双腿和脚在下方交叠；Isaac Gym 对照为双臂水平、双腿分开的近 T-pose；修正后散点图中多数红/蓝关键点成对接近。散点图没有图例、单位或误差数值，因此只支持“对齐明显改善”，不用于判定具体 joint 含义或最终 motion 精度。
- 独立核验引用：[issue · human2humanoid 原作者把 74 links/34 joints 问题链接到其 PHC #96 自答](https://github.com/LeCAR-Lab/human2humanoid/issues/18#issuecomment-2471994042)；[issue · 答复者说明 shape fit 只改 betas/scale，需先保证 smpl_pose_modifier 也是 T-shape](https://github.com/ZhengyiLuo/PHC/issues/96#issuecomment-2469828963)；[issue · 原作者报告修正后 loss 从 200+ 降至约 40，并附关键点对照图](https://github.com/ZhengyiLuo/PHC/issues/96#issuecomment-2469949721)
- 适用边界：适用于 PHC/human2humanoid 自定义机器人 shape fitting；具体 joint_matches 和可接受 loss 需按机器人重新验证。

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

### Isaac Lab actuator gain randomization 的零增量不是当前增益 no-op

- `problem_id`：`problem.training_reward_curriculum.isaaclab_gain_randomization_default_reset_1604`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab actuator gain randomization 加零仍会先恢复 default_joint_stiffness**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：原作者引用的实现会先把 asset.data.default_joint_stiffness 写入 actuator.stiffness，再施加随机操作；所以 add zero 保持的是 default 基线，不一定保持资产当前 actuator gains。作者用有/无事件多次复现 reward 差异，项目贡献者也认可应分离 default values 与 randomization。不过线程没有合并修复或修复后训练结果，因此当前只能把它作为配置审计结论：逐项比较 event 前后 stiffness/damping，不能宣称已有通用修复。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #1604：作者评论 2563243878 引用 events.py 的 default overwrite；贡献者评论 2565844406 认可分离设计
- 原帖/精确回复：[Isaac Lab actuator gain randomization 加零仍会先恢复 default_joint_stiffness](https://github.com/isaac-sim/IsaacLab/issues/1604#issuecomment-2563243878)
- 平台/作者：GitHub Issues / sdfzz
- 关键术语：执行器增益随机化（actuator gain randomization）；默认关节刚度（default joint stiffness）；隐式执行器（ImplicitActuator）；零增量操作（zero-add operation）
- 环境：Isaac Lab manager_based locomotion/velocity/config/g1/flat_env_cfg.py；startup EventTerm；joint_names=.*；原帖未给 commit、GPU、seed。
- 症状：相同 iteration 243，启用 add-zero randomization 的 mean reward 约 -10.49，未启用时约 16.69；作者称多次运行均出现差异。
- 诊断：比较 event 执行前后的 actuator.stiffness/damping、asset.data.default_joint_stiffness/damping 与资产配置值。；不要把 distribution=(0,0)、operation=add 自动视为对当前 actuator gains 的 no-op。
- 原因：原帖引用的 events.py 先从 default_joint_stiffness 重建 stiffness，再调用 randomize；因此零增量保持的是 default 基线，不一定是 asset 当前 actuator 配置。
- 处理过程：作者用有/无 EventTerm 多次对照，并阅读 events.py 定位到先加载 default_joint_stiffness 的代码。；项目贡献者认可 default values 与 randomization 应分离，并指向类似设计提案。
- 有效处理：线程只形成设计建议：将 default 值恢复与 randomization 分开；没有合并修复、可定位正式提交或修复后训练结果，不能写成已验证方案。
- 结果：Issue 保持 open；项目贡献者认可问题方向，但原作者没有发布最终改法或结果。
- 限制：线程没有随机种子和完整训练曲线，16.69/-10.49 只是在指定 iteration 的对照记录。；PR #1416 讨论 reset joint state 的类似设计，并非 actuator gain randomization 的直接合并修复。
- 安全提示：实机前必须核对随机化后的 stiffness/damping 是否落在执行器和低层控制器允许范围，不能仅依据训练 reward。
- 独立核验引用：[issue · 原作者引用 events.py，指出 randomize 前先恢复 default_joint_stiffness](https://github.com/isaac-sim/IsaacLab/issues/1604#issuecomment-2563243878)；[maintainer_confirmation · 项目贡献者认可将 default values 与 randomizations 分离的方向](https://github.com/isaac-sim/IsaacLab/issues/1604#issuecomment-2565844406)；[pull_request · 贡献者所指的类似 reset/default 分离提案；该 PR 未合并且不是 actuator gain 直接修复](https://github.com/isaac-sim/IsaacLab/pull/1416)
- 适用边界：适用于原帖所用 Isaac Lab randomize_actuator_gains 实现；目标版本代码可能变化，必须核对实际 events.py。

### Isaac Lab RSL-RL 大动作反馈导致 value loss 爆炸

- `problem_id`：`problem.training_reward_curriculum.isaaclab_rslrl_action_clipping_nan_1999`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：Isaac Lab RSL-RL 大动作反馈导致 value loss 爆炸时启用 action clipping**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：原线程验证的是在 RSL-RL wrapper 执行动作前启用动作裁剪（action clipping）。官方 PR #2019 说明，未裁剪的大动作既进入环境又成为上一动作观测（last-action observation），可能形成动作与 critic error 互相放大的负反馈；PR 增加 agent_cfg.clip_actions 并在 step 中用 torch.clamp。原作者合并后确认有效。线程没有公开通用裁剪阈值，因此阈值仍需按任务动作定义验证。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #1999：协作者评论 2700385656 指向 PR #2019；原作者评论 2719617210 确认 Works；PR 合并提交 f774425
- 原帖/精确回复：[Isaac Lab RSL-RL 大动作反馈导致 value loss 爆炸时启用 action clipping](https://github.com/isaac-sim/IsaacLab/issues/1999#issuecomment-2719617210)
- 平台/作者：GitHub Issues / alextong1010
- 关键术语：动作裁剪（action clipping）；上一动作观测（last-action observation）；价值函数损失（value function loss）；负反馈回路（negative feedback loop）
- 环境：Isaac Lab 默认 Go2 rough policy、RSL-RL；约 5000–8000 iterations 后失败；原帖日志为 iteration 8391、24576×12 policy loc；未给 Isaac Lab commit 和随机种子。
- 症状：value function loss 变成 inf，随后 torch Normal 的 loc 张量全部为 NaN，训练退出。；失败前 mean episode length 为 1000，terrain curriculum level 约 6.13；这些日志只描述当时状态，不单独证明根因。
- 诊断：检查策略输出是否未经裁剪直接执行，同时又作为 last-action observation 回馈策略。；记录动作幅值、critic loss 和首次出现 inf/NaN 的 iteration，验证是否存在持续放大的大动作。
- 原因：官方 PR #2019 说明，大动作直接执行并作为上一动作观测回馈，会造成 large action→large critic error→更大 sampled action 的负反馈。
- 处理过程：协作者建议合并 PR #2019 后复测。；原作者按建议测试并回复 Works。
- 有效处理：使用合入 PR #2019 后的 RslRlVecEnvWrapper，并通过 agent_cfg.clip_actions 启用动作裁剪；该 PR 在 wrapper step 中于执行环境动作前调用 torch.clamp。
- 结果：原作者确认合并 PR 后有效并关闭 Issue；PR #2019 于 2025-03-13 合入官方仓库。
- 限制：原线程没有给出所用 clip_actions 数值，不能从该帖子推导通用裁剪阈值。；该修复针对 RSL-RL wrapper 的动作反馈路径，不能把所有 PPO/RL NaN 都归因于同一问题。
- 安全提示：动作裁剪是训练与接口防护，不替代实机的关节位置、速度、力矩和急停安全限制。
- 独立核验引用：[issue · 原作者合并测试后回复 Works 并关闭 Issue](https://github.com/isaac-sim/IsaacLab/issues/1999#issuecomment-2719617210)；[pull_request · 官方合并 PR 解释大动作/last-action 负反馈，并增加 clip_actions 配置](https://github.com/isaac-sim/IsaacLab/pull/2019)；[source_code · 固定合并提交：RslRlVecEnvWrapper.step 在 env.step 前对 actions 执行 torch.clamp](https://github.com/isaac-sim/IsaacLab/commit/f774425b4724e3ed0352e241220a6e2b56067106)
- 适用边界：适用于 Isaac Lab RSL-RL wrapper 中策略动作同时执行并作为上一动作观测的训练路径；具体 clip 范围需匹配任务 action space。

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

### penalty curriculum 改变奖励尺度时不能按 mean reward 峰值选 checkpoint

- `problem_id`：`problem.training_reward_curriculum.h2h_penalty_curriculum_checkpoint_17`
- 问题综合等级：**值得参考** — 至少一条经验形成了完整工程记录，但尚未达到正式交叉核验门槛。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：human2humanoid 平均奖励下降可能来自 penalty curriculum，不能据此提前选 checkpoint**

- 独立等级：**值得参考** — 环境、处理步骤和结果已有工程记录，但尚缺正式资料交叉核验或独立复现。
- 解答状态：`partial`
- 候选解答：项目作者说明 OmniH2O 的 penalty curriculum 会根据 episode length 自动增减负奖励系数，因此 mean reward 的尺度会随训练改变，峰值 checkpoint 不一定已收敛。应保持默认 reward/curriculum，继续训练，并在 W&B 同时画 penalty coefficient、episode length、分项奖励和 rollout。线程建议尝试 100000 iterations，但原作者没有披露最终具体修复，所以该数值不能当成通用阈值。
- 证据状态：`issue_candidate`
- 来源定位：human2humanoid #17：作者评论 2455393534 建议默认配置/100000 iterations；2472060877 解释 penalty curriculum；2478802824 原作者称已解决
- 原帖/精确回复：[human2humanoid 平均奖励下降可能来自 penalty curriculum，不能据此提前选 checkpoint](https://github.com/LeCAR-Lab/human2humanoid/issues/17#issuecomment-2472060877)
- 平台/作者：GitHub Issues / zengweishuai
- 关键术语：惩罚课程（penalty curriculum）；平均回合长度（average episode length）；特权策略（privileged policy）；训练检查点（training checkpoint）
- 环境：human2humanoid privileged policy checkpoint 25000/26500，distilled policy checkpoint 18000；默认训练配置语境；原帖未给 commit、GPU 或随机种子。
- 症状：原作者文字描述前进时一条腿跟随 reference、另一条腿落后。；奖励图显示 mean reward 从负值快速升至约 100，在约 1.2M steps 附近达到更高区间，1.5M 后总体下降并在训练末期约为 50。
- 诊断：同时绘制 penalty coefficient/penalty scale、average episode length 与分项奖励，不只看加权后的 mean reward。；确认是否保持项目默认 reward/curriculum，并比较更后期 checkpoint 的实际跟踪和步态。
- 原因：项目作者判断 penalty curriculum 会按 episode length 自动改变负奖励系数；reward 尺度变化后，早期 reward 峰值不等于策略已充分收敛。
- 处理过程：原作者因总奖励在 1M-1.5M 区间后下降，选了 25000/26500 checkpoint。；项目作者建议继续到 100000 iterations、采用默认 reward/curriculum，并查看 penalty coefficient。
- 有效处理：不要仅按 mean reward 峰值挑选；结合 curriculum coefficient、episode length 和实际 rollout 判断收敛，并按原线程建议用默认设置继续训练。
- 结果：原作者在项目作者解释后回复问题已解决；没有公布最终 checkpoint、曲线或具体改动。
- 限制：100000 iterations 是线程中的排查建议，不是所有任务的固定收敛步数。；原作者没有明确说明是继续训练、恢复默认配置还是其他修改解决问题，因此不能把单一动作写成已验证唯一修复。；GIF 只核验了首个可见帧，不能从单帧证明完整的单腿时序落后。
- 安全提示：进入实机前应对多个 checkpoint 做独立 rollout、跌倒率和关节/力矩约束检查，不以训练总奖励单指标选型。
- 图片分析：奖励曲线已核验：mean reward 从约 -100 快速升至约 100，约 1.2M steps 附近进入约 120 的高点，1.5M 后总体下降并震荡，末端约 50；图中没有 penalty coefficient 或 episode length，因此不能单靠该图判定退化。GIF 的首个可见帧显示机器人深蹲、双腿明显弯曲/交叠并叠加稀疏目标点，但本轮未读取完整动画时序，不据此证明哪条腿持续落后。
- 独立核验引用：[maintainer_confirmation · 项目作者说明 penalty coefficient 按 policy episode length 自动增减，并建议绘图检查](https://github.com/LeCAR-Lab/human2humanoid/issues/17#issuecomment-2472060877)；[issue · 原作者确认问题已解决，但没有说明最终采取的具体动作](https://github.com/LeCAR-Lab/human2humanoid/issues/17#issuecomment-2478802824)；[source_code · 固定 commit：average_episode_length 更新与 penalty_scale 按上下阈值增减并 clip](https://github.com/LeCAR-Lab/human2humanoid/blob/fb7ed5f85c4426f7c52cc3f82e43ee4de215bee9/legged_gym/legged_gym/envs/base/legged_robot.py#L2289-L2307)
- 适用边界：适用于启用 human2humanoid/OmniH2O penalty curriculum 的 privileged-policy 训练；其他 reward 定义需核对自身系数更新逻辑。

### 动态权重归零后的分项 reward 残留

- `problem_id`：`problem.training_reward_curriculum.isaaclab_zero_weight_step_reward_stale_2391`
- 问题综合等级：**可信度很高** — 至少一条经验已有正式资料或独立复现支持，且当前没有未解决冲突。
- 经验数量：1（全部列出，不隐藏待验证或冲突来源）

**经验 1：动态 reward 权重归零后要清空 per-term step buffer**

- 独立等级：**可信度很高** — 问题已闭环、环境明确且无冲突，并有正式资料或独立复现的精确引用。
- 解答状态：`resolved`
- 候选解答：先用 0→非零→0 的权重序列确认只有 _step_reward 分项残留，而 _reward_buf 总 reward 正常。使用包含 PR #2392 的版本，或在 RewardManager.compute 的 zero-weight 分支按 term_idx 显式把 _step_reward\[:, term_idx\] 清零后再 continue。该修复只针对 per-term visualization/logging 的 stale value，不应解释成总 reward 算错。
- 证据状态：`issue_candidate`
- 来源定位：IsaacLab #2391 完整复现与环境；PR #2392
- 原帖/精确回复：[动态 reward 权重归零后要清空 per-term step buffer](https://github.com/isaac-sim/IsaacLab/issues/2391)
- 平台/作者：GitHub Issues / bikcrum
- 关键术语：动态奖励权重（dynamic reward weight）；分步奖励缓冲（step reward buffer）；过期值（stale value）；实时可视化器（live visualizer）
- 环境：Isaac Lab 2.1.0 commit 2e6946a、Isaac Sim 4.5、Ubuntu 22.04、RTX 3060、CUDA 12.4、driver 550.120。
- 症状：_step_reward 对应 term 保留先前非零值，live visualizer/logging 显示 stale reward。；总 reward _reward_buf 仍正确。
- 诊断：把 term weight 按 0→非零→0 顺序动态修改，并同时打印 _step_reward\[:, idx\] 与总 reward。
- 原因：zero-weight 分支直接 continue，遗漏清空 per-term step buffer。
- 处理过程：原帖给出最小伪代码和 acceptance criteria；PR #2392 按 term_idx 在 continue 前写 0。
- 有效处理：升级到包含 PR #2392 / merge commit f1ba9c3 的版本，或在 weight==0 分支显式执行 _step_reward\[:, term_idx\]=0.0。
- 结果：Issue 随 PR 合并关闭；修复针对 per-term visualization/logging，不改变原本正确的 total reward。
- 限制：不要把该 bug 误写成总 reward 计算错误。；PR checklist 未声明新增测试；证据来自精确复现和源码修复。
- 安全提示：调 curriculum 时应同时记录权重、per-term contribution 和 total reward，避免只凭 UI 分项判断。
- 独立核验引用：[pull_request · 合并 PR 在 zero-weight 分支清零对应 _step_reward term；检查清单未新增测试](https://github.com/isaac-sim/IsaacLab/pull/2392)；[source_code · PR #2392 合并提交](https://github.com/isaac-sim/IsaacLab/commit/f1ba9c3a30b0cef04d04dfba789f996360cd4f1c)；[issue · 原作者确认 Isaac Lab 2.1.0 / Isaac Sim 4.5 版本](https://github.com/isaac-sim/IsaacLab/issues/2391#issuecomment-2836796927)
- 适用边界：适用于 Isaac Lab 2.1.0 附近、允许运行时动态切换 reward term weight 的 RewardManager。
