# MultiModalWBC / M3imic：把异构动作参考对齐到一个全身控制器

[English version](en/multimodalwbc.md)

审阅快照：[Renforce-Dynamics/MultiModalWBC@`1628d0e3c0e05b9e2ec95c141568bd8c3f480e51`](https://github.com/Renforce-Dynamics/MultiModalWBC/tree/1628d0e3c0e05b9e2ec95c141568bd8c3f480e51) · 189 stars（2026-08-12 快照）· 核心仓库 BSD-3-Clause，捆绑组件与资产沿用各自条款。对应论文为 [M3imic, arXiv:2606.04829v1](https://arxiv.org/abs/2606.04829v1)。star 只用于发现，不代表论文结论可信度或真机安全。

## 为什么收录

仓库最初被候选列表视为“纯项目”，但官方 README 与 arXiv 一手页已经明确给出 M3imic 论文，所以本轮将关系修正为 `official_paper_code`。仍保留项目独立页，是因为代码层可以回答论文摘要不能回答的问题：三种模态如何进入 observation、数据怎样统一加载、不同任务配置如何共用环境、策略又如何导出。

它覆盖通用跟踪与运动生成两个既有 topic。代表性不在于模态名称多，而在于试图用一个策略处理机器人关节轨迹、SMPL-X 人体姿态和 SE(3) 关键点。论文声称不为每种模态重新训练即可 sim-to-real；项目页只核对公开实现结构，不替代后续完整论文图表解读。

## 它解决什么问题

机器人关节角是密集、与本体强绑定的参考；人体姿态和末端 SE(3) 轨迹更稀疏，且关节定义不同。把它们直接拼成一个向量会让网络同时承担坐标对齐、缺失信息和控制学习。M3imic 的工程思路是为不同参考构造专门数据与 observation 入口，再在共享策略空间内训练。

这种统一的主要收益是接口一致与数据复用，但“共享”不等于模态完全等价。稀疏关键点可能无法确定肘部或腰部冗余姿态；SMPL-X 数据还带有人体骨架与机器人形态差异。因此实验中的成功率必须与模态、数据集、终止阈值和具体任务一起解释。

## 架构与数据流

工程路径可写为 `异构数据预处理 → Motion_Dataset/Unify_Motion_Dataset → Motion_Dataloader → command term → 模态专用 observations → Tracking/GAEMimic 环境配置 → RSL-RL runner → ONNX export`。`tracking_env_cfg.py` 把 command、policy/critic observations、奖励、随机化、终止和 curriculum 组合在一个 Isaac Lab manager-based 环境中。

`GAEMimic_TrackingEnvCfg` 继承多动作跟踪配置，变化集中在统一数据与模态 observation；这使对照更容易，但也意味着基类配置的改动会同时影响多种实验。延迟执行器模块为命令加入延迟缓冲，属于 sim-to-real 建模的一部分；它不能自动覆盖真机通信抖动、摩擦或结构柔顺性。

## 代码定位

- [`Unify_Motion_Dataset`](https://github.com/Renforce-Dynamics/MultiModalWBC/blob/1628d0e3c0e05b9e2ec95c141568bd8c3f480e51/source/whole_body_control/whole_body_control/utils/motion_dataset.py) 定义机器人动作、SMPL-X 与关键点数据怎样落入统一样本。
- [`Unify_Motion_Dataloader`](https://github.com/Renforce-Dynamics/MultiModalWBC/blob/1628d0e3c0e05b9e2ec95c141568bd8c3f480e51/source/whole_body_control/whole_body_control/utils/motion_dataloader.py) 预载并拼接多段动作，暴露跨模态 buffer 字段。
- [`motion_smplx_pose_body` 与 `motion_keypoints_se3`](https://github.com/Renforce-Dynamics/MultiModalWBC/blob/1628d0e3c0e05b9e2ec95c141568bd8c3f480e51/source/whole_body_control/whole_body_control/tasks/tracking/mdp/observations.py) 是人体姿态与 SE(3) 关键点进入策略的直接位置。
- [`GAEMimic_TrackingEnvCfg`](https://github.com/Renforce-Dynamics/MultiModalWBC/blob/1628d0e3c0e05b9e2ec95c141568bd8c3f480e51/source/whole_body_control/whole_body_control/tasks/tracking/tracking_env_cfg.py) 汇总多模态 command、observation 和环境设置。
- [`_Onnx_GAEMimic_PolicyExporter`](https://github.com/Renforce-Dynamics/MultiModalWBC/blob/1628d0e3c0e05b9e2ec95c141568bd8c3f480e51/source/whole_body_control/whole_body_control/utils/exporter.py) 展示三种推理入口如何导出到 ONNX。

## 最小复现路径

固定 Isaac Lab `90b79bb2d44feb8d833f260f2bf37da3487180ba` 与本页 commit，安装 `source/whole_body_control`，下载官方预处理数据并记录文件哈希。先运行环境列表，再以小环境数分别加载 robot、human、keypoint 样本，打印每个 observation 字段的形状、坐标系与归一化统计；确认后才运行 README 的 `MultiTracking-Flat-G1-v0` 训练。

最小对照应固定网络、随机种子、训练步数和随机化，只切换参考模态；分别报告训练内、未见动作和 sim2sim 的成功率、根/刚体/末端误差、终止原因与动作饱和率。导出 ONNX 后，对同一输入比较 PyTorch 与 ONNX 输出，再做有明确延迟与噪声设置的回放。

## 能力边界

审阅代码主要面向 Unitree G1，架构可扩展不等于其他本体已有可复核结果。官方摘要的 98.42% 峰值成功率来自特定未见测试集与仿真定义，不能写成任意模态或真机任务的通用成功率。README 的真机视频提供存在性证据，不给出全部失败分布。

数据集托管在外部平台，复现受数据版本、许可证和下载可用性影响。仓库 vendor 了 RSL-RL 并依赖 Isaac Lab，需分别记录版本和许可证。项目目前 TODO 仍包括 mjlab 版本与更多模态，不能当作现有能力。

## 工程判断与风险

最值得复用的是模态专用输入与共享环境配置的分层，而不是简单追求“一个策略全包”。工程上应为每种模态保留独立的缺失值、坐标系、频率和质量门禁，并在策略内部外都记录当前模态，便于失败追踪。多模态平均分可能掩盖某一模态长期失败。

真机部署必须校验 ONNX 元数据、关节顺序、输入频率、延迟缓冲、动作缩放和 PD/力矩限制；先 sim2sim、再吊装或支撑下低增益测试，并保持急停。稀疏末端命令可能诱导未约束身体部分采取危险姿态，需要碰撞、关节限位和姿态安全层。本页不提供可直接上机的参数。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/Renforce-Dynamics/MultiModalWBC/tree/1628d0e3c0e05b9e2ec95c141568bd8c3f480e51)
- [arXiv:2606.04829v1](https://arxiv.org/abs/2606.04829v1)
- [环境安装文档](https://github.com/Renforce-Dynamics/MultiModalWBC/blob/1628d0e3c0e05b9e2ec95c141568bd8c3f480e51/docs/env_setup.md)
