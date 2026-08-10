# 训练数据与动作重定向

本板块回答“怎样把人体动作变成可训练、可执行、可审计的机器人参考数据”。下面两篇深读锚点分别覆盖离线运动学重定向与无机器人示范采集；扩展目录继续补齐经典方法与开源工作。边界止于参考数据/目标生成，不把下游策略成功归因给数据接口本身。

- [Retargeting Matters / GMR](../retargeting-matters-2510.02252v1.md)：关键体匹配、非均匀缩放、两阶段 IK 与下游可跟踪性评估。
- [HuMI](../humi-2602.06643v2.md)：传感夹爪与五点追踪、在线 IK 反馈、分层扩散策略和低层跟踪。

建议联读问题：几何误差、接触穿透与关节跳变如何进入训练数据验收？任务空间物体几何为何不能随人体比例缩放？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：7 篇，其中深度解读 2 篇，有可核验官方代码 6 篇。
- 必要覆盖角色：领域锚点（field anchor）、开源实现（open source）、机器人数据质量（robot data quality）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking](../retargeting-matters-2510.02252v1.md) | 2025 | 机器人数据质量（robot data quality）、开源实现（open source） | [官方代码](https://github.com/YanjieZe/GMR) | 用下游跟踪成功率直接检验重定向伪影，并提供通用开源实现。 |
| 深度解读 | [Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations](../humi-2602.06643v2.md) | 2026 | 机器人数据质量（robot data quality）、稀疏命令（sparse command） | [公开计划，待核验](https://humanoid-manipulation-interface.github.io/) | 代表无机器人示教、人在环可行性反馈与分层全身跟踪的数据路线。 |
| 待深读 | [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](https://arxiv.org/abs/1804.02717) | 2018 | 领域锚点（field anchor）、开源实现（open source） | [官方代码](https://github.com/xbpeng/DeepMimic) | 参考动作跟踪与任务目标联合训练的经典起点，对后续高动态动作学习影响深远。 |
| 待深读 | [AMASS: Archive of Motion Capture as Surface Shapes](https://arxiv.org/abs/1904.03278) | 2019 | 领域锚点（field anchor）、开源实现（open source） | [官方代码](https://github.com/nghorbani/amass) | 将多个人体动作库统一到 SMPL/SMPL-H 表示，是今日大规模人形跟踪的数据起点。 |
| 待深读 | [Perpetual Humanoid Control for Real-time Simulated Avatars](https://arxiv.org/abs/2305.06456) | 2023 | 领域锚点（field anchor）、开源实现（open source）、恢复（recovery） | [官方代码](https://github.com/ZhengyiLuo/PHC) | 用渐进容量分配扩展到万级动作，并把失败状态恢复纳入同一物理控制器。 |
| 待深读 | [PHUMA: Physically-Grounded Humanoid Locomotion Dataset](https://arxiv.org/abs/2510.26236) | 2025 | 机器人数据质量（robot data quality）、开源实现（open source） | [官方代码](https://github.com/DAVIAN-Robotics/PHUMA) | 把大规模人类视频动作转换为带关节、接触和脚滑约束的可跟踪人形数据。 |
| 待深读 | [TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System](https://arxiv.org/abs/2511.02832) | 2025 | 稀疏命令（sparse command）、开源实现（open source）、机器人数据质量（robot data quality） | [官方代码](https://github.com/amazon-far/TWIST2) | 用便携 VR 和低成本机器人颈部取代昂贵 MoCap，面向可规模化数据采集。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->
