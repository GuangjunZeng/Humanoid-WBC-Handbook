# 训练数据与动作重定向

本板块回答“怎样把人体动作变成可训练、可执行、可审计的机器人参考数据”。下面两篇深读锚点分别覆盖离线运动学重定向与无机器人示范采集；扩展目录继续补齐经典方法与开源工作。边界止于参考数据/目标生成，不把下游策略成功归因给数据接口本身。

- [Retargeting Matters / GMR](../retargeting-matters-2510.02252v1.md)：关键体匹配、非均匀缩放、两阶段 IK 与下游可跟踪性评估。
- [HuMI](../humi-2602.06643v2.md)：传感夹爪与五点追踪、在线 IK 反馈、分层扩散策略和低层跟踪。

建议联读问题：几何误差、接触穿透与关节跳变如何进入训练数据验收？任务空间物体几何为何不能随人体比例缩放？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：16 篇，其中深度解读 7 篇，有可核验官方代码 15 篇。
- 必要覆盖角色：领域锚点（field anchor）、开源实现（open source）、机器人数据质量（robot data quality）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](../deepmimic-1804.02717.md) | 2018 | 领域锚点（field anchor）、开源实现（open source） | [官方代码](https://github.com/xbpeng/DeepMimic) | 参考动作跟踪与任务目标联合训练的经典起点，对后续高动态动作学习影响深远。 |
| 深度解读 | [AMASS: Archive of Motion Capture as Surface Shapes](../amass-1904.03278.md) | 2019 | 领域锚点（field anchor）、开源实现（open source） | [官方代码](https://github.com/nghorbani/amass) | 将多个人体动作库统一到 SMPL/SMPL-H 表示，是今日大规模人形跟踪的数据起点。 |
| 深度解读 | [Perpetual Humanoid Control for Real-time Simulated Avatars](../phc-2305.06456.md) | 2023 | 领域锚点（field anchor）、开源实现（open source）、恢复（recovery） | [官方代码](https://github.com/ZhengyiLuo/PHC) | 用渐进容量分配扩展到万级动作，并把失败状态恢复纳入同一物理控制器。 |
| 深度解读 | [World-Grounded Human Motion Recovery via Gravity-View Coordinates](../gvhmr-2409.06662.md) | 2024 | 机器人数据质量（robot data quality）、开源实现（open source） | [官方代码](https://github.com/zju3dv/GVHMR) | 从单目视频恢复世界坐标中的人体运动与相机轨迹，为机器人重定向提供带重力和全局位移的一致输入。 |
| 深度解读 | [Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking](../retargeting-matters-2510.02252v1.md) | 2025 | 机器人数据质量（robot data quality）、开源实现（open source） | [官方代码](https://github.com/YanjieZe/GMR) | 用下游跟踪成功率直接检验重定向伪影，并提供通用开源实现。 |
| 深度解读 | [Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations](../humi-2602.06643v2.md) | 2026 | 机器人数据质量（robot data quality）、稀疏命令（sparse command） | [公开计划，待核验](https://humanoid-manipulation-interface.github.io/) | 代表无机器人示教、人在环可行性反馈与分层全身跟踪的数据路线。 |
| 深度解读 | [PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged and Humanoid Robots](../prime-2605.17681.md) | 2026 | 机器人数据质量（robot data quality）、优化控制（optimization）、开源实现（open source） | [官方代码](https://github.com/well-robotics/PRIME) | 物理一致的惯性与运动估计直接关系到 WBC 状态反馈、落地冲击和恢复判断，补齐感知—控制接口。 |
| 待深读 | [WHAM: Reconstructing World-grounded Humans with Accurate 3D Motion](https://arxiv.org/abs/2312.07531) | 2023 | 领域锚点（field anchor）、机器人数据质量（robot data quality）、开源实现（open source） | [官方代码](https://github.com/yohanshin/WHAM) | 以世界坐标、人体动力学先验和视频运动线索恢复长序列，是视频动作资产进入重定向流水线的重要代表作。 |
| 待深读 | [TRAM: Global Trajectory and Motion of 3D Humans from in-the-wild Videos](https://arxiv.org/abs/2403.17346) | 2024 | 机器人数据质量（robot data quality）、开源实现（open source） | [官方代码](https://github.com/yufu-wang/tram) | 联合相机运动估计与人体重建，补足野外视频转机器人动作时最容易缺失的全局轨迹。 |
| 待深读 | [OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction](https://arxiv.org/abs/2509.26633) | 2025 | 机器人数据质量（robot data quality）、任务交互（task interaction）、开源实现（open source） | [官方代码](https://github.com/amazon-far/holosoma) | 重定向时显式保持人与物、人与场景的交互约束，直接面向全身移动操作训练数据的可执行性。 |
| 待深读 | [PHUMA: Physically-Grounded Humanoid Locomotion Dataset](https://arxiv.org/abs/2510.26236) | 2025 | 机器人数据质量（robot data quality）、开源实现（open source） | [官方代码](https://github.com/DAVIAN-Robotics/PHUMA) | 把大规模人类视频动作转换为带关节、接触和脚滑约束的可跟踪人形数据。 |
| 待深读 | [TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System](https://arxiv.org/abs/2511.02832) | 2025 | 稀疏命令（sparse command）、开源实现（open source）、机器人数据质量（robot data quality） | [官方代码](https://github.com/amazon-far/TWIST2) | 用便携 VR 和低成本机器人颈部取代昂贵 MoCap，面向可规模化数据采集。 |
| 待深读 | [A Kung Fu Athlete Bot That Can Do It All Day: Highly Dynamic, Balance-Challenging Motion Dataset and Autonomous Fall-Resilient Tracking](https://arxiv.org/abs/2602.13656v1) | 2026 | 机器人数据质量（robot data quality）、任务交互（task interaction）、实机证据（hardware evidence）、恢复（recovery）、开源实现（open source） | [官方代码](https://github.com/NPCLEI/KungFuAthleteBot) | 把高动态动作数据、平衡挑战跟踪与自主跌倒恢复放在同一真机系统中，适合跨三个既有 topic 对照。 |
| 待深读 | [GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://arxiv.org/abs/2606.05160) | 2026 | 机器人数据质量（robot data quality）、任务交互（task interaction）、开源实现（open source） | [官方代码](https://github.com/NVlabs/GRAIL) | 结合三维资产与视频先验生成可交互全身动作，代表从互联网数据到仿真可训练轨迹的工程路线。 |
| 待深读 | [HoloMotion-1 Technical Report](https://arxiv.org/abs/2605.15336) | 2026 | 多模式（multi-mode）、实机证据（hardware evidence）、机器人数据质量（robot data quality）、开源实现（open source） | [官方代码](https://github.com/HorizonRobotics/HoloMotion) | 以统一数据与控制栈连接动作资产、全身跟踪和可部署技能，适合作为大型开源系统的架构案例。 |
| 待深读 | [Make Tracking Easy: Neural Motion Retargeting for Humanoid Whole-body Control](https://arxiv.org/abs/2603.22201) | 2026 | 机器人数据质量（robot data quality）、学习控制（learning）、开源实现（open source） | [官方代码](https://github.com/NJU3DV-HumanoidGroup/MakeTrackingEasy) | 把神经动作重定向与后续全身跟踪协同考虑，针对传统逐帧优化产生的难跟踪轨迹。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->

<!-- BEGIN GENERATED PROJECT CATALOG -->
## 高质量开源项目

项目与论文使用不同证据链。stars 只作为按需发现门槛，不参与技术可信度排序；“已审代码”项目已固定 commit 并提供完整中英文独立页，“待审代码”只保留官方仓库与当前快照，不冒充完成解读。

- 当前收录：9 个项目，其中已审代码 5 个、无对应论文的独立项目 2 个。
- stars 快照：2026-08-12T00:00:00+08:00；后续只在用户要求更新时刷新。

| 状态 | 项目 | 关系 | stars | 许可证 | 为什么收录 |
|---|---|---|---:|---|---|
| 已审代码 | [HoloSoma](../projects/holosoma.md) | 论文官方实现 | 1582 | Apache-2.0 | 在同一官方框架中覆盖人形 locomotion、全身跟踪、多仿真后端、FastSAC 与 OmniRetarget 相关路径。 |
| 已审代码 | [PHC](../projects/phc.md) | 论文官方实现 | 1275 | NOASSERTION | 大规模动作跟踪、容量扩展与失败恢复的经典物理人形控制实现。 |
| 已审代码 | [SOMA Retargeter](../projects/soma-retargeter.md) | 独立项目（无对应论文） | 526 | Apache-2.0 | 基于 Newton 与 Warp 的 BVH 到人形运动重定向库，适合独立检查数据接口和批处理实现。 |
| 已审代码 | [KungFuAthleteBot](../projects/kungfu-athlete-bot.md) | 论文官方实现 | 259 | MIT | 公开功夫动作数据、GMR 重定向、强化学习训练、跌倒恢复与 G1 部署链，适合项目级复核。 |
| 已审代码 | [trackerLab](../projects/trackerlab.md) | 独立项目（无对应论文） | 243 | MIT | 以 Isaac Lab 统一重定向、轨迹跟踪与技能控制，适合作为跨本体 Tracker 对照平台。 |
| 待审代码 | [GMR](https://github.com/YanjieZe/GMR) | 论文官方实现 | 2581 | MIT | 跨多种人形本体的实时 CPU 动作重定向基线，配置、几何约束与结果可直接复核。 |
| 待审代码 | [GVHMR](https://github.com/zju3dv/GVHMR) | 论文官方实现 | 1840 | NOASSERTION | 从移动相机视频恢复世界坐标人体运动，是机器人重定向前的数据入口代表。 |
| 待审代码 | [HoloMotion](https://github.com/HorizonRobotics/HoloMotion) | 论文官方实现 | 621 | Apache-2.0 | 把人体模型、重定向、动作库、跟踪模型、评测和 G1 部署放在同一官方工程中。 |
| 待审代码 | [GRAIL](https://github.com/NVlabs/GRAIL) | 论文官方实现 | 466 | NOASSERTION | 从三维资产和视频先验生成移动操作轨迹，补齐交互数据合成与物理筛选路线。 |

项目解读规则见 [开源项目独立解读规范](../../../docs/project-interpretation.md)。候选发现不会自动收录，且不在后台定时运行。
<!-- END GENERATED PROJECT CATALOG -->
