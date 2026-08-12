# 行走与复杂地形

本板块比较两个互补工程路径：可直接复现的零样本 sim-to-real 行走基线，以及用轨迹预训练 Transformer 提高复杂地形学习效率。成功率必须与地形分布、传感假设和测试分母一起阅读。

- [Humanoid-Gym](../humanoid-gym-2404.05695v2.md)：历史本体观测、特权 critic、仿真校准与双尺寸机器人部署。
- [Learning Humanoid Locomotion over Challenging Terrain / HT-2](../challenging-terrain-2410.03654v1.md)：轨迹预训练、缺失动作掩码与六类刚性地形 PPO 微调。

建议联读问题：sim-to-sim 应是怎样的发布门禁？预训练轨迹分布与目标地形不匹配时，收益会在哪里消失？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：9 篇，其中深度解读 4 篇，有可核验官方代码 6 篇。
- 必要覆盖角色：经典控制（classical control）、学习基线（learning anchor）、开源实现（open source）、地形（terrain）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [Biped Walking Pattern Generation by Using Preview Control of Zero-Moment Point](../zmp-preview-kajita-2003.md) | 2003 | 经典控制（classical control）、领域锚点（field anchor） | 未发现官方公开代码 | ZMP 预览控制的经典工作，是理解现代学习步态与模型控制分工的必要基线。 |
| 深度解读 | [Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition](../periodic-gaits-2011.01387v2.md) | 2020 | 学习基线（learning anchor）、开源实现（open source） | [官方代码](https://github.com/osudrl/apex) | 在 Cassie 上将周期奖励组合为多步态真实迁移，是双足深度强化学习的早期可复现锚点。 |
| 深度解读 | [Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer](../humanoid-gym-2404.05695v2.md) | 2024 | 开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/roboterax/humanoid-gym) | 开源 Isaac Gym 训练、MuJoCo sim-to-sim 和双尺寸真机部署的工程基线。 |
| 深度解读 | [Learning Humanoid Locomotion over Challenging Terrain](../challenging-terrain-2410.03654v1.md) | 2024 | 地形（terrain）、机器人部署（robot deployment） | 未发现官方公开代码 | 用平地序列预训练 Transformer 再 PPO 微调，验证盲走 Digit 的复杂地形样本效率。 |
| 待深读 | [Humanoid Locomotion as Next Token Prediction](https://arxiv.org/abs/2402.19469) | 2024 | 学习基线（learning anchor）、机器人部署（robot deployment） | 未发现官方公开代码 | 把真实 Digit 行走建模为下一 token 预测，代表离线序列模型进入人形运动控制。 |
| 待深读 | [Booster Gym: An End-to-End Reinforcement Learning Framework for Humanoid Robot Locomotion](https://arxiv.org/abs/2506.15132) | 2025 | 开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/BoosterRobotics/booster_gym) | 从训练、域随机化到 Booster T1 部署的端到端开源人形行走框架。 |
| 待深读 | [Learning Sim-to-Real Humanoid Locomotion in 15 Minutes](https://arxiv.org/abs/2512.01996) | 2025 | 开源实现（open source）、学习基线（learning anchor）、机器人部署（robot deployment） | [官方代码](https://github.com/younggyoseo/FastTD3) | 用大规模并行离策略 RL 将 G1/T1 实机行走训练缩短到分钟级。 |
| 待深读 | [PHUMA: Physically-Grounded Humanoid Locomotion Dataset](https://arxiv.org/abs/2510.26236) | 2025 | 机器人数据质量（robot data quality）、开源实现（open source） | [官方代码](https://github.com/DAVIAN-Robotics/PHUMA) | 把大规模人类视频动作转换为带关节、接触和脚滑约束的可跟踪人形数据。 |
| 待深读 | [Whole-Body Model-Predictive Control of Legged Robots with MuJoCo](https://arxiv.org/abs/2503.04613) | 2025 | 优化控制（optimization）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://johnzhang3.github.io/mujoco_ilqr/) | 用 MuJoCo 动力学和有限差分 iLQR 给出容易复现的真实全身 MPC 基线。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->
