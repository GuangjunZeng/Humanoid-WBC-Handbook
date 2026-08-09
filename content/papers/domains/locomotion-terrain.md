# 行走与复杂地形

本板块比较两个互补工程路径：可直接复现的零样本 sim-to-real 行走基线，以及用轨迹预训练 Transformer 提高复杂地形学习效率。成功率必须与地形分布、传感假设和测试分母一起阅读。

- [Humanoid-Gym](../humanoid-gym-2404.05695v2.md)：历史本体观测、特权 critic、仿真校准与双尺寸机器人部署。
- [Learning Humanoid Locomotion over Challenging Terrain / HT-2](../challenging-terrain-2410.03654v1.md)：轨迹预训练、缺失动作掩码与六类刚性地形 PPO 微调。

建议联读问题：sim-to-sim 应是怎样的发布门禁？预训练轨迹分布与目标地形不匹配时，收益会在哪里消失？
