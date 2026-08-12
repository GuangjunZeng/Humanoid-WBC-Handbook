# 体育与高动态技能

本板块把“高动态”拆成两类难点：训练仿真与真实动力学偏差，以及视觉/击打任务的多阶段课程。论文展示值不是硬件动作许可，所有跳跃、踢击、挥拍均须独立热、电流和跌倒风险审查。

- [ASAP](../asap-2502.01143v3.md)：用真实轨迹学习 delta action，对齐训练仿真后微调主策略。
- [Humanoid Whole-Body Badminton](../humanoid-badminton-2511.11218v3.md)：足步、挥拍和任务精调的三级训练，以及 46 次实机比较。

建议联读问题：残差模型在什么版本/工况下失效？任务预测收益应怎样用实机重复次数而不是展示视频衡量？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：7 篇，其中深度解读 4 篇，有可核验官方代码 3 篇。
- 必要覆盖角色：领域锚点（field anchor）、开源实现（open source）、仿真到现实（sim-to-real）、任务交互（task interaction）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](../deepmimic-1804.02717v3.md) | 2018 | 领域锚点（field anchor）、开源实现（open source） | [官方代码](https://github.com/xbpeng/DeepMimic) | 参考动作跟踪与任务目标联合训练的经典起点，对后续高动态动作学习影响深远。 |
| 深度解读 | [Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning](../agile-soccer-2304.13653v2.md) | 2023 | 领域锚点（field anchor）、仿真到现实（sim-to-real）、恢复（recovery） | 未发现官方公开代码 | 小型人形真实 1v1 足球的代表性工作，统一了行走、踢球、策略与快速起身。 |
| 深度解读 | [ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills](../asap-2502.01143v3.md) | 2025 | 仿真到现实（sim-to-real）、开源实现（open source）、实机证据（hardware evidence） | [官方代码](https://github.com/LeCAR-Lab/ASAP) | 用实机轨迹学习 delta action 对齐训练动力学，并公开报告硬件损坏代价。 |
| 深度解读 | [Humanoid Whole-Body Badminton via Multi-Stage Reinforcement Learning](../humanoid-badminton-2511.11218v3.md) | 2025 | 任务交互（task interaction）、实机证据（hardware evidence） | 未发现官方公开代码 | 用足步、挥拍和任务精调三阶段学习时序敏感的真实羽毛球击打。 |
| 待深读 | [KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills](https://arxiv.org/abs/2506.12851) | 2025 | 开源实现（open source）、仿真到现实（sim-to-real）、任务交互（task interaction） | [官方代码](https://github.com/TeleHuman/PBHC) | 面向武术类高动态动作的多阶段运动处理、自适应跟踪与真机开源基线。 |
| 待深读 | [Learning Human-Like Badminton Skills for Humanoid Robots](https://arxiv.org/abs/2602.08370) | 2026 | 任务交互（task interaction）、仿真到现实（sim-to-real） | 待核验 | 用从模仿到交互的渐进训练和流形扩展学习多种拟人击球技能。 |
| 待深读 | [Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework](https://arxiv.org/abs/2602.05310) | 2026 | 任务交互（task interaction）、仿真到现实（sim-to-real） | 待核验 | 用动作技能、感知动作融合和物理迁移三阶段学习 Unitree G1 足球。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->
