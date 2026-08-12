# 移动操作与末端 WBC

本板块讨论行走、躯干和双臂任务的耦合。FALCON 用上下身双策略与力矩感知外力课程，ULC 用一个统一策略、逐阶段课程和残差手臂动作；两者不能在未验证的实机接触力包络外互相替代。

- [FALCON](../falcon-2505.06776v2.md)：末端 Jacobian/力矩余量、三维外力课程与双策略协同。
- [ULC](../ulc-2507.06905v2.md)：29 维统一动作、顺序技能激活、五次插值和负载/延迟随机化。

建议联读问题：何时应拆分上下身优化，何时应共享单策略？末端扰动、腕部负载和 CoM 目标怎样落入同一安全约束？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：15 篇，其中深度解读 5 篇，有可核验官方代码 12 篇。
- 必要覆盖角色：经典控制（classical control）、优化控制（optimization）、开源实现（open source）、学习控制（learning）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [A Whole-Body Control Framework for Humanoids](../sentis-wbc-2006.md) | 2006 | 经典控制（classical control）、领域锚点（field anchor） | 未发现官方公开代码 | 层级操作空间全身控制的经典文献，定义了多任务优先级与动力学一致的基本语言。 |
| 深度解读 | [Implementing Torque Control with High-Ratio Gear Boxes and without Joint-Torque Sensors](../hrp2-torque-control-hal-01136936.md) | 2016 | 优化控制（optimization）、开源实现（open source）、经典控制（classical control） | [官方代码](https://github.com/stack-of-tasks/tsid) | TSID 的工程实现锚点，说明高减速比、无关节力矩传感时如何落地任务空间逆动力学。 |
| 深度解读 | [Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control](../crocoddyl-1909.04947.md) | 2019 | 优化控制（optimization）、经典控制（classical control）、开源实现（open source） | [官方代码](https://github.com/loco-3d/crocoddyl) | 多接触最优控制与微分动态规划的高质量开源框架，是学习方法之外理解 WBC 优化栈的重要经典锚点。 |
| 深度解读 | [FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation](../falcon-2505.06776v2.md) | 2025 | 学习控制（learning）、开源实现（open source）、实机证据（hardware evidence） | [官方代码](https://github.com/LeCAR-Lab/FALCON) | 用双策略分解与力矩可行外力课程学习受力移动操作。 |
| 深度解读 | [ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation](../ulc-2507.06905v2.md) | 2025 | 学习控制（learning）、机器人部署（robot deployment） | 未发现官方公开代码 | 用顺序技能、残差手臂动作和延迟/载荷随机化训练单一细粒度策略。 |
| 待深读 | [Expressive Whole-Body Control for Humanoid Robots](https://arxiv.org/abs/2402.16796) | 2024 | 多模式（multi-mode）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/chengxuxin/expressive-humanoid) | 以稀疏指令实现上肢表达与下肢稳定协同，是全身遥操和交互控制的早期代表性真机路线。 |
| 待深读 | [Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning](https://arxiv.org/abs/2504.14305) | 2025 | 多模式（multi-mode）、任务交互（task interaction）、开源实现（open source） | [官方代码](https://github.com/TeleHuman/ALMI-Open) | 联合对抗式步态与动作模仿，展示一套策略同时覆盖移动、跟踪和上肢任务的路线。 |
| 待深读 | [HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit](https://arxiv.org/abs/2502.13013) | 2025 | 学习控制（learning）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/InternRobotics/OpenHomie) | 同构外骨骼驾驶舱与移动操作策略联合设计，并完整开源硬件和训练资源。 |
| 待深读 | [OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction](https://arxiv.org/abs/2509.26633) | 2025 | 机器人数据质量（robot data quality）、任务交互（task interaction）、开源实现（open source） | [官方代码](https://github.com/amazon-far/holosoma) | 重定向时显式保持人与物、人与场景的交互约束，直接面向全身移动操作训练数据的可执行性。 |
| 待深读 | [SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending](https://arxiv.org/abs/2506.09366) | 2025 | 任务交互（task interaction）、潜技能（latent skill）、开源实现（open source） | [官方代码](https://github.com/Humanoid-SkillBlender/SkillBlender) | 通过技能混合组合全身移动操作行为，体现可复用技能比单一端到端策略更易扩展的技术路线。 |
| 待深读 | [ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation](https://arxiv.org/abs/2502.00893) | 2025 | 机器人部署（robot deployment）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/hshi74/toddlerbot) | 完整开源软硬件平台把低成本人形、学习控制与移动操作放进同一可复现实验载体。 |
| 待深读 | [Whole-Body Model-Predictive Control of Legged Robots with MuJoCo](https://arxiv.org/abs/2503.04613) | 2025 | 优化控制（optimization）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://johnzhang3.github.io/mujoco_ilqr/) | 用 MuJoCo 动力学和有限差分 iLQR 给出容易复现的真实全身 MPC 基线。 |
| 待深读 | [AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning](https://arxiv.org/abs/2603.20147v1) | 2026 | 机器人部署（robot deployment）、仿真到现实（sim-to-real）、任务交互（task interaction）、恢复（recovery）、开源实现（open source） | [官方代码](https://github.com/nvidia-isaac/WBC-AGILE) | 覆盖数据、训练、部署与恢复的完整移动操作工作流，适合用来核对单点算法在系统工程中的位置。 |
| 待深读 | [GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://arxiv.org/abs/2606.05160) | 2026 | 机器人数据质量（robot data quality）、任务交互（task interaction）、开源实现（open source） | [官方代码](https://github.com/NVlabs/GRAIL) | 结合三维资产与视频先验生成可交互全身动作，代表从互联网数据到仿真可训练轨迹的工程路线。 |
| 待深读 | [Safety-Critical Whole-Body Control for Humanoid Robots via Input-to-State Safe Control Barrier Functions](https://arxiv.org/abs/2605.25546) | 2026 | 经典控制（classical control）、保护性跌倒（protective fall）、优化控制（optimization） | 未发现官方公开代码 | 以输入到状态安全控制屏障函数约束全身控制，为社区中常见的经验性安全调参提供形式化对照。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->
