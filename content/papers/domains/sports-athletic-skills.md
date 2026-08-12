# 体育与高动态技能

本板块把“高动态”拆成两类难点：训练仿真与真实动力学偏差，以及视觉/击打任务的多阶段课程。论文展示值不是硬件动作许可，所有跳跃、踢击、挥拍均须独立热、电流和跌倒风险审查。

- [ASAP](../asap-2502.01143v3.md)：用真实轨迹学习 delta action，对齐训练仿真后微调主策略。
- [Humanoid Whole-Body Badminton](../humanoid-badminton-2511.11218v3.md)：足步、挥拍和任务精调的三级训练，以及 46 次实机比较。

建议联读问题：残差模型在什么版本/工况下失效？任务预测收益应怎样用实机重复次数而不是展示视频衡量？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：11 篇，其中深度解读 6 篇，有可核验官方代码 7 篇。
- 必要覆盖角色：领域锚点（field anchor）、开源实现（open source）、仿真到现实（sim-to-real）、任务交互（task interaction）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](../deepmimic-1804.02717v3.md) | 2018 | 领域锚点（field anchor）、开源实现（open source） | [官方代码](https://github.com/xbpeng/DeepMimic) | 参考动作跟踪与任务目标联合训练的经典起点，对后续高动态动作学习影响深远。 |
| 深度解读 | [Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning](../agile-soccer-2304.13653v2.md) | 2023 | 领域锚点（field anchor）、仿真到现实（sim-to-real）、恢复（recovery） | 未发现官方公开代码 | 小型人形真实 1v1 足球的代表性工作，统一了行走、踢球、策略与快速起身。 |
| 深度解读 | [ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills](../asap-2502.01143v3.md) | 2025 | 仿真到现实（sim-to-real）、开源实现（open source）、实机证据（hardware evidence） | [官方代码](https://github.com/LeCAR-Lab/ASAP) | 用实机轨迹学习 delta action 对齐训练动力学，并公开报告硬件损坏代价。 |
| 深度解读 | [Humanoid Whole-Body Badminton via Multi-Stage Reinforcement Learning](../humanoid-badminton-2511.11218v3.md) | 2025 | 任务交互（task interaction）、实机证据（hardware evidence） | 未发现官方公开代码 | 用足步、挥拍和任务精调三阶段学习时序敏感的真实羽毛球击打。 |
| 深度解读 | [KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills](../kungfubot-2506.12851.md) | 2025 | 开源实现（open source）、仿真到现实（sim-to-real）、任务交互（task interaction） | [官方代码](https://github.com/TeleHuman/PBHC) | 面向武术类高动态动作的多阶段运动处理、自适应跟踪与真机开源基线。 |
| 深度解读 | [Learning Athletic Humanoid Tennis Skills from Imperfect Human Motion Data](../latent-2603.12686.md) | 2026 | 任务交互（task interaction）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/GalaxyGeneralRobotics/LATENT) | 从不完美人体动作学习网球中的移动、击球和时序协同，官方来源也纠正了聚合清单的错误 arXiv 映射。 |
| 待深读 | [Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints](https://arxiv.org/abs/2510.18002) | 2025 | 任务交互（task interaction）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/InternRobotics/Humanoid-Goalkeeper) | 以位置条件任务约束学习守门动作，官方来源纠正了聚合清单中指向网络入侵论文的错误编号。 |
| 待深读 | [A Kung Fu Athlete Bot That Can Do It All Day: Highly Dynamic, Balance-Challenging Motion Dataset and Autonomous Fall-Resilient Tracking](https://arxiv.org/abs/2602.13656v1) | 2026 | 机器人数据质量（robot data quality）、任务交互（task interaction）、实机证据（hardware evidence）、恢复（recovery）、开源实现（open source） | [官方代码](https://github.com/NPCLEI/KungFuAthleteBot) | 把高动态动作数据、平衡挑战跟踪与自主跌倒恢复放在同一真机系统中，适合跨三个既有 topic 对照。 |
| 待深读 | [HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control](https://arxiv.org/abs/2602.03205) | 2026 | 任务交互（task interaction）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/TeleHuman/humanoid_skateboarding) | 针对滑板接触动力学构建物理感知全身控制，官方来源纠正了聚合清单中指向代数论文的错误编号。 |
| 待深读 | [Learning Human-Like Badminton Skills for Humanoid Robots](https://arxiv.org/abs/2602.08370) | 2026 | 任务交互（task interaction）、仿真到现实（sim-to-real） | 待核验 | 用从模仿到交互的渐进训练和流形扩展学习多种拟人击球技能。 |
| 待深读 | [Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework](https://arxiv.org/abs/2602.05310) | 2026 | 任务交互（task interaction）、仿真到现实（sim-to-real） | 待核验 | 用动作技能、感知动作融合和物理迁移三阶段学习 Unitree G1 足球。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->
