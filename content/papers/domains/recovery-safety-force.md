# 起身恢复、跌倒与受力安全

本板块是硬件高风险区。HoST 面向多接触姿态的无示范起身，FRASA 面向小型人形的对称矢状面起身与扰动恢复。所有结论都受机器人型号、接触面、姿态、能量和保护设施约束。

- [HoST](../host-2502.08378v2.md)：多 critic、拉力探索课程、动作幅度课程与平滑约束。
- [FRASA](../frasa-2410.08655v3.md)：五自由度对称 CrossQ/SAC、随机跌倒初始化与摆锤抗扰试验。

建议联读问题：如何区分“能站起来”和“机械上可长期接受”？碰撞感知、急停、跌倒保护与分阶段测试应如何成为发布门禁？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：16 篇，其中深度解读 8 篇，有可核验官方代码 11 篇。
- 必要覆盖角色：恢复（recovery）、保护性跌倒（protective fall）、开源实现（open source）、实机证据（hardware evidence）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning](../agile-soccer-2304.13653v2.md) | 2023 | 领域锚点（field anchor）、仿真到现实（sim-to-real）、恢复（recovery） | 未发现官方公开代码 | 小型人形真实 1v1 足球的代表性工作，统一了行走、踢球、策略与快速起身。 |
| 深度解读 | [Perpetual Humanoid Control for Real-time Simulated Avatars](../phc-2305.06456.md) | 2023 | 领域锚点（field anchor）、开源实现（open source）、恢复（recovery） | [官方代码](https://github.com/ZhengyiLuo/PHC) | 用渐进容量分配扩展到万级动作，并把失败状态恢复纳入同一物理控制器。 |
| 深度解读 | [FRASA: An End-to-End Reinforcement Learning Agent for Fall Recovery and Stand Up of Humanoid Robots](../frasa-2410.08655v3.md) | 2024 | 恢复（recovery）、开源实现（open source）、实机证据（hardware evidence） | [官方代码](https://github.com/Rhoban/frasa) | 在小型真实人形上用统一策略处理抗扰、倒地恢复和快速起身。 |
| 深度解读 | [FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation](../falcon-2505.06776v2.md) | 2025 | 学习控制（learning）、开源实现（open source）、实机证据（hardware evidence） | [官方代码](https://github.com/LeCAR-Lab/FALCON) | 用双策略分解与力矩可行外力课程学习受力移动操作。 |
| 深度解读 | [Learning Getting-Up Policies for Real-World Humanoid Robots](../humanup-2502.12152.md) | 2025 | 恢复（recovery）、开源实现（open source）、实机证据（hardware evidence） | [官方代码](https://github.com/RunpeiDong/HumanUP) | HumanUP 先放开约束发现起身轨迹，再细化为平滑、低速、可迁移的真机策略。 |
| 深度解读 | [Learning Humanoid Standing-up Control across Diverse Postures](../host-2502.08378v2.md) | 2025 | 恢复（recovery）、开源实现（open source）、实机证据（hardware evidence） | [官方代码](https://github.com/OpenRobotLab/HoST) | 从多姿态无示范探索起身，以多 critic、探索课程和平滑约束实现 G1 迁移。 |
| 深度解读 | [SafeFall: Learning Protective Control for Humanoid Robots](../safefall-2511.18509v1.md) | 2025 | 保护性跌倒（protective fall）、实机证据（hardware evidence） | 待核验 | 用跌倒预测器触发伤害缓解策略，显式保护头、手等脆弱部件。 |
| 深度解读 | [PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged and Humanoid Robots](../prime-2605.17681.md) | 2026 | 机器人数据质量（robot data quality）、优化控制（optimization）、开源实现（open source） | [官方代码](https://github.com/well-robotics/PRIME) | 物理一致的惯性与运动估计直接关系到 WBC 状态反馈、落地冲击和恢复判断，补齐感知—控制接口。 |
| 待深读 | [Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning](https://arxiv.org/abs/2512.01336) | 2025 | 保护性跌倒（protective fall）、实机证据（hardware evidence） | 待核验 | 直接以冲击伤害为目标学习适合刚性人形结构的自保护跌倒行为。 |
| 待深读 | [Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints](https://arxiv.org/abs/2510.18002) | 2025 | 任务交互（task interaction）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/InternRobotics/Humanoid-Goalkeeper) | 以位置条件任务约束学习守门动作，官方来源纠正了聚合清单中指向网络入侵论文的错误编号。 |
| 待深读 | [Towards Bridging the Gap: Systematic Sim-to-Real Transfer for Diverse Legged Robots](https://arxiv.org/abs/2509.06342) | 2025 | 仿真到现实（sim-to-real）、机器人部署（robot deployment）、开源实现（open source） | [官方代码](https://github.com/leggedrobotics/pace-sim2real) | 系统拆解腿式机器人仿真到真实迁移误差，适合作为人形部署参数、延迟和建模偏差的工程参照。 |
| 待深读 | [Unified Humanoid Fall-Safety Policy from a Few Demonstrations](https://arxiv.org/abs/2511.07407) | 2025 | 保护性跌倒（protective fall）、恢复（recovery）、实机证据（hardware evidence） | 待核验 | 将防倒、冲击缓解和起身恢复放入一个少示范统一策略。 |
| 待深读 | [A Kung Fu Athlete Bot That Can Do It All Day: Highly Dynamic, Balance-Challenging Motion Dataset and Autonomous Fall-Resilient Tracking](https://arxiv.org/abs/2602.13656v1) | 2026 | 机器人数据质量（robot data quality）、任务交互（task interaction）、实机证据（hardware evidence）、恢复（recovery）、开源实现（open source） | [官方代码](https://github.com/NPCLEI/KungFuAthleteBot) | 把高动态动作数据、平衡挑战跟踪与自主跌倒恢复放在同一真机系统中，适合跨三个既有 topic 对照。 |
| 待深读 | [AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning](https://arxiv.org/abs/2603.20147v1) | 2026 | 机器人部署（robot deployment）、仿真到现实（sim-to-real）、任务交互（task interaction）、恢复（recovery）、开源实现（open source） | [官方代码](https://github.com/nvidia-isaac/WBC-AGILE) | 覆盖数据、训练、部署与恢复的完整移动操作工作流，适合用来核对单点算法在系统工程中的位置。 |
| 待深读 | [Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids](https://arxiv.org/abs/2601.07718) | 2026 | 地形（terrain）、实机证据（hardware evidence）、仿真到现实（sim-to-real）、开源实现（open source） | [官方代码](https://github.com/project-instinct/InstinctLab) | 将感知、复杂地形跑酷与可扩展训练基础设施整合，补充实验室平地基准之外的系统证据。 |
| 待深读 | [Safety-Critical Whole-Body Control for Humanoid Robots via Input-to-State Safe Control Barrier Functions](https://arxiv.org/abs/2605.25546) | 2026 | 经典控制（classical control）、保护性跌倒（protective fall）、优化控制（optimization） | 未发现官方公开代码 | 以输入到状态安全控制屏障函数约束全身控制，为社区中常见的经验性安全调参提供形式化对照。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->
