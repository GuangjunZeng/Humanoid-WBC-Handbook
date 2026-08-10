# 起身恢复、跌倒与受力安全

本板块是硬件高风险区。HoST 面向多接触姿态的无示范起身，FRASA 面向小型人形的对称矢状面起身与扰动恢复。所有结论都受机器人型号、接触面、姿态、能量和保护设施约束。

- [HoST](../host-2502.08378v2.md)：多 critic、拉力探索课程、动作幅度课程与平滑约束。
- [FRASA](../frasa-2410.08655v3.md)：五自由度对称 CrossQ/SAC、随机跌倒初始化与摆锤抗扰试验。

建议联读问题：如何区分“能站起来”和“机械上可长期接受”？碰撞感知、急停、跌倒保护与分阶段测试应如何成为发布门禁？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：9 篇，其中深度解读 3 篇，有可核验官方代码 5 篇。
- 必要覆盖角色：恢复（recovery）、保护性跌倒（protective fall）、开源实现（open source）、实机证据（hardware evidence）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [FRASA: An End-to-End Reinforcement Learning Agent for Fall Recovery and Stand Up of Humanoid Robots](../frasa-2410.08655v3.md) | 2024 | 恢复（recovery）、开源实现（open source）、实机证据（hardware evidence） | [官方代码](https://github.com/Rhoban/frasa) | 在小型真实人形上用统一策略处理抗扰、倒地恢复和快速起身。 |
| 深度解读 | [FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation](../falcon-2505.06776v2.md) | 2025 | 学习控制（learning）、开源实现（open source）、实机证据（hardware evidence） | [官方代码](https://github.com/LeCAR-Lab/FALCON) | 用双策略分解与力矩可行外力课程学习受力移动操作。 |
| 深度解读 | [Learning Humanoid Standing-up Control across Diverse Postures](../host-2502.08378v2.md) | 2025 | 恢复（recovery）、开源实现（open source）、实机证据（hardware evidence） | [官方代码](https://github.com/OpenRobotLab/HoST) | 从多姿态无示范探索起身，以多 critic、探索课程和平滑约束实现 G1 迁移。 |
| 待深读 | [Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning](https://arxiv.org/abs/2304.13653) | 2023 | 领域锚点（field anchor）、仿真到现实（sim-to-real）、恢复（recovery） | 未发现官方公开代码 | 小型人形真实 1v1 足球的代表性工作，统一了行走、踢球、策略与快速起身。 |
| 待深读 | [Perpetual Humanoid Control for Real-time Simulated Avatars](https://arxiv.org/abs/2305.06456) | 2023 | 领域锚点（field anchor）、开源实现（open source）、恢复（recovery） | [官方代码](https://github.com/ZhengyiLuo/PHC) | 用渐进容量分配扩展到万级动作，并把失败状态恢复纳入同一物理控制器。 |
| 待深读 | [Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning](https://arxiv.org/abs/2512.01336) | 2025 | 保护性跌倒（protective fall）、实机证据（hardware evidence） | 待核验 | 直接以冲击伤害为目标学习适合刚性人形结构的自保护跌倒行为。 |
| 待深读 | [Learning Getting-Up Policies for Real-World Humanoid Robots](https://arxiv.org/abs/2502.12152) | 2025 | 恢复（recovery）、开源实现（open source）、实机证据（hardware evidence） | [官方代码](https://github.com/RunpeiDong/HumanUP) | HumanUP 先放开约束发现起身轨迹，再细化为平滑、低速、可迁移的真机策略。 |
| 待深读 | [SafeFall: Learning Protective Control for Humanoid Robots](https://arxiv.org/abs/2511.18509) | 2025 | 保护性跌倒（protective fall）、实机证据（hardware evidence） | 待核验 | 用跌倒预测器触发伤害缓解策略，显式保护头、手等脆弱部件。 |
| 待深读 | [Unified Humanoid Fall-Safety Policy from a Few Demonstrations](https://arxiv.org/abs/2511.07407) | 2025 | 保护性跌倒（protective fall）、恢复（recovery）、实机证据（hardware evidence） | 待核验 | 将防倒、冲击缓解和起身恢复放入一个少示范统一策略。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->
