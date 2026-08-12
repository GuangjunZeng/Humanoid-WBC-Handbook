# 通用跟踪与遥操作

本板块关注从稠密或稀疏人体命令到全身关节目标的在线控制。下面两篇深读锚点共同采用教师—学生蒸馏与历史状态，但一个强调头手稀疏遥操作，另一个强调运行时多种控制模式；扩展目录则补齐经典基线和官方开源工作。

- [OmniH2O](../omnih2o-2406.08858v1.md)：头/手目标、历史观测、DAgger 和实机遥操作证据。
- [HOVER](../hover-2410.21229v2.md)：统一命令向量、模式/稀疏掩码与多模式全身控制。

建议联读问题：何时历史能替代显式全局线速度？运行时模式切换怎样设置 ODD、延迟与失败回退？

<!-- BEGIN GENERATED PAPER CATALOG -->
## 扩展论文目录

下表由 [`catalog.json`](../catalog.json) 生成。“深度解读”已通过中文全文分析与关键图质量门；“待深读”已经过主记录、去重、经典性/开源性与板块缺口审查，但不冒充完整解读。

- 当前收录：22 篇，其中深度解读 7 篇，有可核验官方代码 20 篇。
- 必要覆盖角色：领域锚点（field anchor）、开源实现（open source）、稀疏命令（sparse command）、多模式（multi-mode）。

| 状态 | 论文 | 年份 | 收录角色 | 代码 | 为什么收录 |
|---|---|---:|---|---|---|
| 深度解读 | [HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots](../hover-2410.21229v2.md) | 2024 | 多模式（multi-mode）、开源实现（open source） | [官方代码](https://github.com/NVlabs/HOVER) | 用统一命令向量、模式掩码与稀疏掩码训练一个多模式全身控制器。 |
| 深度解读 | [HumanPlus: Humanoid Shadowing and Imitation from Humans](../humanplus-2406.10454.md) | 2024 | 领域锚点（field anchor）、开源实现（open source）、稀疏命令（sparse command） | [官方代码](https://github.com/MarkFzp/humanplus) | 把真人影子模仿、全身数据采集与自主视觉模仿连成完整系统。 |
| 深度解读 | [Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation](../human2humanoid-2403.04436.md) | 2024 | 领域锚点（field anchor）、开源实现（open source） | [官方代码](https://github.com/LeCAR-Lab/human2humanoid) | 早期真实全尺寸人形学习式实时全身遥操锚点，建立 sim-to-data 筛选管线。 |
| 深度解读 | [OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning](../omnih2o-2406.08858v1.md) | 2024 | 稀疏命令（sparse command）、开源实现（open source） | [官方代码](https://github.com/LeCAR-Lab/human2humanoid) | 用头手稀疏命令、历史观测和教师蒸馏实现全身遥操与任务学习。 |
| 深度解读 | [Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models](../meta-motivo-2504.11054.md) | 2025 | 潜技能（latent skill）、领域锚点（field anchor）、开源实现（open source） | [官方代码](https://github.com/facebookresearch/metamotivo) | Meta Motivo 用行为基础模型展示零样本全身控制，是高 Star 无独立页面项目转为论文—代码联合解读的关键案例。 |
| 深度解读 | [Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations](../humi-2602.06643v2.md) | 2026 | 机器人数据质量（robot data quality）、稀疏命令（sparse command） | [公开计划，待核验](https://humanoid-manipulation-interface.github.io/) | 代表无机器人示教、人在环可行性反馈与分层全身跟踪的数据路线。 |
| 深度解读 | [M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking](../m3imic-2606.04829v1.md) | 2026 | 多模式（multi-mode）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/Renforce-Dynamics/MultiModalWBC) | 统一处理多种动作条件与模态输入，是 Renforce Dynamics 开源全身控制路线中最直接的论文锚点。 |
| 待深读 | [Universal Humanoid Motion Representations for Physics-Based Control](https://arxiv.org/abs/2310.04582) | 2023 | 领域锚点（field anchor）、潜技能（latent skill）、多模式（multi-mode）、开源实现（open source） | [官方代码](https://github.com/ZhengyiLuo/PULSE) | PULSE 从大规模非结构化动作学习通用潜在表示，并用于跟踪、地形穿越和下游任务，是动作先验路线的代表作。 |
| 待深读 | [ExBody2: Advanced Expressive Humanoid Whole-Body Control](https://arxiv.org/abs/2412.13196) | 2024 | 多模式（multi-mode）、领域锚点（field anchor） | 未发现官方公开代码 | 将关键点跟踪与根速度控制解耦，并在两种真实人形平台上验证表达性动作。 |
| 待深读 | [Expressive Whole-Body Control for Humanoid Robots](https://arxiv.org/abs/2402.16796) | 2024 | 多模式（multi-mode）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/chengxuxin/expressive-humanoid) | 以稀疏指令实现上肢表达与下肢稳定协同，是全身遥操和交互控制的早期代表性真机路线。 |
| 待深读 | [MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting](https://arxiv.org/abs/2409.14393) | 2024 | 潜技能（latent skill）、开源实现（open source）、多模式（multi-mode） | [官方代码](https://github.com/NVlabs/ProtoMotions) | 把关键帧、文本、场景和稀疏目标统一为掩码动作补全问题。 |
| 待深读 | [Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning](https://arxiv.org/abs/2504.14305) | 2025 | 多模式（multi-mode）、任务交互（task interaction）、开源实现（open source） | [官方代码](https://github.com/TeleHuman/ALMI-Open) | 联合对抗式步态与动作模仿，展示一套策略同时覆盖移动、跟踪和上肢任务的路线。 |
| 待深读 | [BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning](https://arxiv.org/abs/2511.04131) | 2025 | 潜技能（latent skill）、多模式（multi-mode）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/LeCAR-Lab/BFM-Zero) | 无监督预训练可提示行为模型，代表从单任务跟踪走向可组合、可查询动作空间的开放实现。 |
| 待深读 | [GMT: General Motion Tracking for Humanoid Whole-Body Control](https://arxiv.org/abs/2506.14770) | 2025 | 学习控制（learning）、实机证据（hardware evidence）、开源实现（open source） | [官方代码](https://github.com/zixuan417/humanoid-general-motion-tracking) | 面向多样动作的通用全身跟踪器，提供从参考运动到真机控制的可复现训练实现。 |
| 待深读 | [HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit](https://arxiv.org/abs/2502.13013) | 2025 | 学习控制（learning）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/InternRobotics/OpenHomie) | 同构外骨骼驾驶舱与移动操作策略联合设计，并完整开源硬件和训练资源。 |
| 待深读 | [Physics-Based Motion Imitation with Adversarial Differential Discriminators](https://arxiv.org/abs/2505.04961) | 2025 | 学习控制（learning）、开源实现（open source） | [官方代码](https://github.com/xbpeng/MimicKit) | 差分判别器比较动作变化而非只看绝对姿态，为物理动作模仿提供对风格和动态更敏感的目标。 |
| 待深读 | [SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control](https://arxiv.org/abs/2511.07820) | 2025 | 多模式（multi-mode）、开源实现（open source）、机器人部署（robot deployment） | [官方代码](https://github.com/NVlabs/GR00T-WholeBodyControl) | 系统扩展模型、数据和计算，用统一 token 接口连接遥操、视频与 VLA。 |
| 待深读 | [TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System](https://arxiv.org/abs/2511.02832) | 2025 | 稀疏命令（sparse command）、开源实现（open source）、机器人数据质量（robot data quality） | [官方代码](https://github.com/amazon-far/TWIST2) | 用便携 VR 和低成本机器人颈部取代昂贵 MoCap，面向可规模化数据采集。 |
| 待深读 | [TWIST: Teleoperated Whole-Body Imitation System](https://arxiv.org/abs/2505.02833) | 2025 | 稀疏命令（sparse command）、开源实现（open source） | [官方代码](https://github.com/YanjieZe/TWIST) | 以 RL+BC、特权未来帧和真实 MoCap 提高单一网络的响应性全身遥操。 |
| 待深读 | [AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning](https://arxiv.org/abs/2603.20147v1) | 2026 | 机器人部署（robot deployment）、仿真到现实（sim-to-real）、任务交互（task interaction）、恢复（recovery）、开源实现（open source） | [官方代码](https://github.com/nvidia-isaac/WBC-AGILE) | 覆盖数据、训练、部署与恢复的完整移动操作工作流，适合用来核对单点算法在系统工程中的位置。 |
| 待深读 | [HoloMotion-1 Technical Report](https://arxiv.org/abs/2605.15336) | 2026 | 多模式（multi-mode）、实机证据（hardware evidence）、机器人数据质量（robot data quality）、开源实现（open source） | [官方代码](https://github.com/HorizonRobotics/HoloMotion) | 以统一数据与控制栈连接动作资产、全身跟踪和可部署技能，适合作为大型开源系统的架构案例。 |
| 待深读 | [Make Tracking Easy: Neural Motion Retargeting for Humanoid Whole-body Control](https://arxiv.org/abs/2603.22201) | 2026 | 机器人数据质量（robot data quality）、学习控制（learning）、开源实现（open source） | [官方代码](https://github.com/NJU3DV-HumanoidGroup/MakeTrackingEasy) | 把神经动作重定向与后续全身跟踪协同考虑，针对传统逐帧优化产生的难跟踪轨迹。 |

更新不在后台定时运行。当用户明确要求更新该板块时，按 [论文库按需更新流程](../../../docs/on-demand-paper-update.md) 执行。
<!-- END GENERATED PAPER CATALOG -->

<!-- BEGIN GENERATED PROJECT CATALOG -->
## 高质量开源项目

项目与论文使用不同证据链。stars 只作为按需发现门槛，不参与技术可信度排序；“已审代码”项目已固定 commit 并提供完整中英文独立页，“待审代码”只保留官方仓库与当前快照，不冒充完成解读。

- 当前收录：12 个项目，其中已审代码 5 个、无对应论文的独立项目 3 个。
- stars 快照：2026-08-12T00:00:00+08:00；后续只在用户要求更新时刷新。

| 状态 | 项目 | 关系 | stars | 许可证 | 为什么收录 |
|---|---|---|---:|---|---|
| 已审代码 | [Unitree RL Lab](../projects/unitree-rl-lab.md) | 独立项目（无对应论文） | 1272 | Apache-2.0 | Unitree 官方 Isaac Lab 训练、策略导出与机器人部署入口，直接覆盖 H1/G1 工程链。 |
| 已审代码 | [Unitree RL Mjlab](../projects/unitree-rl-mjlab.md) | 独立项目（无对应论文） | 578 | Apache-2.0 | Unitree 官方 MuJoCo/MJLab 轻量训练和验证路线，可与 Omniverse 栈做受控对照。 |
| 已审代码 | [WBC-AGILE](../projects/wbc-agile.md) | 论文官方实现 | 313 | Apache-2.0 (most code) / BSD-3-Clause (RSL-RL portion) | NVIDIA 面向人形移动操作学习的完整工作流，强调训练数据、WBC 基座与任务接口衔接。 |
| 已审代码 | [trackerLab](../projects/trackerlab.md) | 独立项目（无对应论文） | 243 | MIT | 以 Isaac Lab 统一重定向、轨迹跟踪与技能控制，适合作为跨本体 Tracker 对照平台。 |
| 已审代码 | [MultiModalWBC](../projects/multimodalwbc.md) | 论文官方实现 | 189 | BSD-3-Clause (core repository; bundled components and assets retain their own terms) | 把本体状态和多模态人体条件统一为人形跟踪与任务条件控制接口，属于项目型 WBC 基线。 |
| 待审代码 | [MuJoCo](https://github.com/google-deepmind/mujoco) | 基础设施 | 14525 | Apache-2.0 | WBC Sim2Sim、模型控制和轻量训练常用的主流开源物理引擎，接触与执行器语义直接影响结论。 |
| 待审代码 | [Isaac Lab](https://github.com/isaac-sim/IsaacLab) | 基础设施 | 7883 | BSD-3-Clause | 多个人形学习项目共用的官方仿真训练底座，环境、执行器、传感器与并行训练接口可审计。 |
| 待审代码 | [GR00T Whole-Body Control](https://github.com/NVlabs/GR00T-WholeBodyControl) | 论文官方实现 | 3248 | NOASSERTION | NVIDIA 的通用人形 WBC 平台，覆盖 SONIC、解耦控制与上层模型调用接口。 |
| 待审代码 | [ProtoMotions](https://github.com/NVlabs/ProtoMotions) | 论文官方实现 | 2286 | Apache-2.0 | 统一多种物理角色与人形动作学习方法，能在同一框架比较条件掩码、潜技能和跟踪任务。 |
| 待审代码 | [MimicKit](https://github.com/xbpeng/MimicKit) | 基础设施 | 2224 | Apache-2.0 | 在同一轻量框架复现多种动作模仿和运动先验方法，便于控制变量比较而非跨仓库拼接。 |
| 待审代码 | [human2humanoid](https://github.com/LeCAR-Lab/human2humanoid) | 论文官方实现 | 1050 | NOASSERTION | H2O 与 OmniH2O 的官方训练和部署代码，把人体输入、跟踪策略与真机接口连成闭环。 |
| 待审代码 | [HoloMotion](https://github.com/HorizonRobotics/HoloMotion) | 论文官方实现 | 621 | Apache-2.0 | 把人体模型、重定向、动作库、跟踪模型、评测和 G1 部署放在同一官方工程中。 |

项目解读规则见 [开源项目独立解读规范](../../../docs/project-interpretation.md)。候选发现不会自动收录，且不在后台定时运行。
<!-- END GENERATED PROJECT CATALOG -->
