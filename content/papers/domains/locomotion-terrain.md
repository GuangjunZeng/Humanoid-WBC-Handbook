# 行走与复杂地形

本板块比较两个互补工程路径：可直接复现的零样本 sim-to-real 行走基线，以及用轨迹预训练 Transformer 提高复杂地形学习效率。成功率必须与地形分布、传感假设和测试分母一起阅读。

- [Humanoid-Gym](../humanoid-gym-2404.05695v2.md)：历史本体观测、特权 critic、仿真校准与双尺寸机器人部署。
- [Learning Humanoid Locomotion over Challenging Terrain / HT-2](../challenging-terrain-2410.03654v1.md)：轨迹预训练、缺失动作掩码与六类刚性地形 PPO 微调。

建议联读问题：sim-to-sim 应是怎样的发布门禁？预训练轨迹分布与目标地形不匹配时，收益会在哪里消失？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：20 篇，其中深度解读 8 篇，有可核验官方代码 17 篇。
- 必要覆盖角色：经典控制（classical control）、学习基线（learning anchor）、开源实现（open source）、地形（terrain）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [Biped Walking Pattern Generation by Using Preview Control of Zero-Moment Point](../zmp-preview-kajita-2003.md) | 2003 | 经典控制（classical control）、领域锚点（field anchor） | 未发现官方公开代码 | ZMP 预览控制的经典工作，是理解现代学习步态与模型控制分工的必要基线。 |
| 深度解读 | [Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control](../crocoddyl-1909.04947.md) | 2019 | 优化控制（optimization）、经典控制（classical control）、开源实现（open source） | [官方代码](https://github.com/loco-3d/crocoddyl) | 多接触最优控制与微分动态规划的高质量开源框架，是学习方法之外理解 WBC 优化栈的重要经典锚点。 |
| 深度解读 | [Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition](../periodic-gaits-2011.01387v2.md) | 2020 | 学习基线（learning anchor）、开源实现（open source） | [官方代码](https://github.com/osudrl/apex) | 在 Cassie 上将周期奖励组合为多步态真实迁移，是双足深度强化学习的早期可复现锚点。 |
| 深度解读 | [Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](../learning-walk-2109.11978.md) | 2021 | 学习基线（learning anchor）、仿真到现实（sim-to-real）、开源实现（open source） | [官方代码](https://github.com/leggedrobotics/legged_gym) | 大规模并行强化学习训练腿式运动的经典工程基线，legged_gym 也成为大量人形项目的基础设施。 |
| 深度解读 | [Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer](../humanoid-gym-2404.05695v2.md) | 2024 | 开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/roboterax/humanoid-gym) | 开源 Isaac Gym 训练、MuJoCo sim-to-sim 和双尺寸真机部署的工程基线。 |
| 深度解读 | [Learning Humanoid Locomotion over Challenging Terrain](../challenging-terrain-2410.03654v1.md) | 2024 | 地形（terrain）、机器人部署（robot deployment） | 未发现官方公开代码 | 用平地序列预训练 Transformer 再 PPO 微调，验证盲走 Digit 的复杂地形样本效率。 |
| 深度解读 | [Learning Sim-to-Real Humanoid Locomotion in 15 Minutes](../fast-humanoid-locomotion-2512.01996.md) | 2025 | 开源实现（open source）、学习基线（learning anchor）、机器人部署（robot deployment） | [官方代码](https://github.com/amazon-far/holosoma) | 用大规模并行离策略 RL 将 G1/T1 实机行走训练缩短到分钟级。 |
| 深度解读 | [Learning Athletic Humanoid Tennis Skills from Imperfect Human Motion Data](../latent-2603.12686.md) | 2026 | 任务交互（task interaction）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/GalaxyGeneralRobotics/LATENT) | 从不完美人体动作学习网球中的移动、击球和时序协同，官方来源也纠正了聚合清单的错误 arXiv 映射。 |
| 待深读 | [Universal Humanoid Motion Representations for Physics-Based Control](https://arxiv.org/abs/2310.04582) | 2023 | 领域锚点（field anchor）、潜技能（latent skill）、多模式（multi-mode）、开源实现（open source） | [官方代码](https://github.com/ZhengyiLuo/PULSE) | PULSE 从大规模非结构化动作学习通用潜在表示，并用于跟踪、地形穿越和下游任务，是动作先验路线的代表作。 |
| 待深读 | [Humanoid Locomotion as Next Token Prediction](https://arxiv.org/abs/2402.19469) | 2024 | 学习基线（learning anchor）、机器人部署（robot deployment） | 未发现官方公开代码 | 把真实 Digit 行走建模为下一 token 预测，代表离线序列模型进入人形运动控制。 |
| 待深读 | [Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning](https://arxiv.org/abs/2504.14305) | 2025 | 多模式（multi-mode）、任务交互（task interaction）、开源实现（open source） | [官方代码](https://github.com/TeleHuman/ALMI-Open) | 联合对抗式步态与动作模仿，展示一套策略同时覆盖移动、跟踪和上肢任务的路线。 |
| 待深读 | [Booster Gym: An End-to-End Reinforcement Learning Framework for Humanoid Robot Locomotion](https://arxiv.org/abs/2506.15132) | 2025 | 开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/BoosterRobotics/booster_gym) | 从训练、域随机化到 Booster T1 部署的端到端开源人形行走框架。 |
| 待深读 | [MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains](https://arxiv.org/abs/2506.08840) | 2025 | 地形（terrain）、多模式（multi-mode）、开源实现（open source） | [官方代码](https://github.com/TeleHuman/MoRE) | 用残差专家混合在复杂地形上保持类人步态，连接动作风格、多模式策略与地形适应。 |
| 待深读 | [PHUMA: Physically-Grounded Humanoid Locomotion Dataset](https://arxiv.org/abs/2510.26236) | 2025 | 机器人数据质量（robot data quality）、开源实现（open source） | [官方代码](https://github.com/DAVIAN-Robotics/PHUMA) | 把大规模人类视频动作转换为带关节、接触和脚滑约束的可跟踪人形数据。 |
| 待深读 | [ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation](https://arxiv.org/abs/2502.00893) | 2025 | 机器人部署（robot deployment）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/hshi74/toddlerbot) | 完整开源软硬件平台把低成本人形、学习控制与移动操作放进同一可复现实验载体。 |
| 待深读 | [Towards Bridging the Gap: Systematic Sim-to-Real Transfer for Diverse Legged Robots](https://arxiv.org/abs/2509.06342) | 2025 | 仿真到现实（sim-to-real）、机器人部署（robot deployment）、开源实现（open source） | [官方代码](https://github.com/leggedrobotics/pace-sim2real) | 系统拆解腿式机器人仿真到真实迁移误差，适合作为人形部署参数、延迟和建模偏差的工程参照。 |
| 待深读 | [Whole-Body Model-Predictive Control of Legged Robots with MuJoCo](https://arxiv.org/abs/2503.04613) | 2025 | 优化控制（optimization）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://johnzhang3.github.io/mujoco_ilqr/) | 用 MuJoCo 动力学和有限差分 iLQR 给出容易复现的真实全身 MPC 基线。 |
| 待深读 | [AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning](https://arxiv.org/abs/2603.20147v1) | 2026 | 机器人部署（robot deployment）、仿真到现实（sim-to-real）、任务交互（task interaction）、恢复（recovery）、开源实现（open source） | [官方代码](https://github.com/nvidia-isaac/WBC-AGILE) | 覆盖数据、训练、部署与恢复的完整移动操作工作流，适合用来核对单点算法在系统工程中的位置。 |
| 待深读 | [Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids](https://arxiv.org/abs/2601.07718) | 2026 | 地形（terrain）、实机证据（hardware evidence）、仿真到现实（sim-to-real）、开源实现（open source） | [官方代码](https://github.com/project-instinct/InstinctLab) | 将感知、复杂地形跑酷与可扩展训练基础设施整合，补充实验室平地基准之外的系统证据。 |
| 待深读 | [HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control](https://arxiv.org/abs/2602.03205) | 2026 | 任务交互（task interaction）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/TeleHuman/humanoid_skateboarding) | 针对滑板接触动力学构建物理感知全身控制，官方来源纠正了聚合清单中指向代数论文的错误编号。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->
