# 移动操作与末端 WBC

本板块讨论行走、躯干和双臂任务的耦合。FALCON 用上下身双策略与力矩感知外力课程，ULC 用一个统一策略、逐阶段课程和残差手臂动作；两者不能在未验证的实机接触力包络外互相替代。

- [FALCON](../falcon-2505.06776v2.md)：末端 Jacobian/力矩余量、三维外力课程与双策略协同。
- [ULC](../ulc-2507.06905v2.md)：29 维统一动作、顺序技能激活、五次插值和负载/延迟随机化。

建议联读问题：何时应拆分上下身优化，何时应共享单策略？末端扰动、腕部负载和 CoM 目标怎样落入同一安全约束？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：6 篇，其中深度解读 4 篇，有可核验官方代码 4 篇。
- 必要覆盖角色：经典控制（classical control）、优化控制（optimization）、开源实现（open source）、学习控制（learning）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [A Whole-Body Control Framework for Humanoids](../sentis-wbc-2006.md) | 2006 | 经典控制（classical control）、领域锚点（field anchor） | 未发现官方公开代码 | 层级操作空间全身控制的经典文献，定义了多任务优先级与动力学一致的基本语言。 |
| 深度解读 | [Implementing Torque Control with High-Ratio Gear Boxes and without Joint-Torque Sensors](../hrp2-torque-control-hal-01136936.md) | 2016 | 优化控制（optimization）、开源实现（open source）、经典控制（classical control） | [官方代码](https://github.com/stack-of-tasks/tsid) | TSID 的工程实现锚点，说明高减速比、无关节力矩传感时如何落地任务空间逆动力学。 |
| 深度解读 | [FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation](../falcon-2505.06776v2.md) | 2025 | 学习控制（learning）、开源实现（open source）、实机证据（hardware evidence） | [官方代码](https://github.com/LeCAR-Lab/FALCON) | 用双策略分解与力矩可行外力课程学习受力移动操作。 |
| 深度解读 | [ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation](../ulc-2507.06905v2.md) | 2025 | 学习控制（learning）、机器人部署（robot deployment） | 未发现官方公开代码 | 用顺序技能、残差手臂动作和延迟/载荷随机化训练单一细粒度策略。 |
| 待深读 | [HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit](https://arxiv.org/abs/2502.13013) | 2025 | 学习控制（learning）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/InternRobotics/OpenHomie) | 同构外骨骼驾驶舱与移动操作策略联合设计，并完整开源硬件和训练资源。 |
| 待深读 | [Whole-Body Model-Predictive Control of Legged Robots with MuJoCo](https://arxiv.org/abs/2503.04613) | 2025 | 优化控制（optimization）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://johnzhang3.github.io/mujoco_ilqr/) | 用 MuJoCo 动力学和有限差分 iLQR 给出容易复现的真实全身 MPC 基线。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->
