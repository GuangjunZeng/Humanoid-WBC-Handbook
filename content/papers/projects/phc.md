# PHC：大规模物理人形动作跟踪与失败恢复实现

[English version](en/phc.md)

审阅快照：[ZhengyiLuo/PHC@`846988d433ce1f341e85ac6fbd2cd51911bb3341`](https://github.com/ZhengyiLuo/PHC/tree/846988d433ce1f341e85ac6fbd2cd51911bb3341) · 1275 stars（2026-08-12 快照）· 仓库含 LICENSE，但使用前还需逐项核对 SMPL/SMPL-X、AMASS、机器人资产与模型条款。star 不是复现简单、动作全覆盖或真机安全的证据。

## 为什么收录

PHC（Perpetual Humanoid Control）是大规模 physics-based motion tracking（物理动作跟踪）的经典开源实现。它将 AMASS 动作处理、SMPL/SMPL-X 人形、参考状态、模仿奖励、PMCP/PNN/MCP 网络、hard-sequence curriculum 和 fall-state recovery 放在同一仓库。

项目在 2024–2025 继续加入 PHC+、offline dataset、G1/H1 配置和 Isaac Lab 推理示例，所以当前代码能力明显超过 2023 论文快照。独立项目页用来区分“原论文结论”和“当前仓库入口”，避免用后来的 README 成绩回写原始实验。

## 它解决什么问题

单一动作跟踪策略容易做，万级动作、噪声参考和偏离状态同时覆盖就会出现 capacity、catastrophic forgetting（灾难性遗忘）和失败数据不平衡。PHC 通过 progressive multiplicative control policy（PMCP）对难动作逐步分配新容量，并把恢复作为可组合 primitive。

工程上最难的不只是 network。动作帧率、root frame、关节映射、初始状态采样、终止门槛与“far from reference”定义会决定哪些样本被当作失败。仓库将这些选项暴露在 task 和 Hydra config 中，但 README 也承认完整 PHC 训练需要很多手工阶段。

## 架构与数据流

主路径是 `AMASS/SMPL motion → preprocessing/retargeting → MotionLib reference → HumanoidIm observations and rewards → PNN primitives → hard-sequence fitting → MCP composition → fall-state recovery`。`run_hydra.py` 组合 robot、env、learning、control、domain randomization 和 simulator 配置。

`HumanoidIm` 在每帧采样参考并计算根、关节、刚体位姿和速度误差。`HumanoidImGetup` 额外维护 fall/recovery episode 状态。PNN/MCP 负责容量扩展与 primitive 组合。单 primitive 可以有高跟踪率，但 README 明确说它没有完整的 failure-state recovery 能力。

## 代码定位

- [`HumanoidIm`](https://github.com/ZhengyiLuo/PHC/blob/846988d433ce1f341e85ac6fbd2cd51911bb3341/phc/env/tasks/humanoid_im.py) 是参考动作跟踪任务；同文件的 `compute_imitation_reward` 和 `_compute_reset` 是奖励/终止边界的直接证据。
- [`HumanoidImGetup`](https://github.com/ZhengyiLuo/PHC/blob/846988d433ce1f341e85ac6fbd2cd51911bb3341/phc/env/tasks/humanoid_im_getup.py) 通过 `_reset_fall_episode` 和 `_compute_reset` 管理随机倒地、恢复窗口和重置。
- [`HumanoidImMCP`](https://github.com/ZhengyiLuo/PHC/blob/846988d433ce1f341e85ac6fbd2cd51911bb3341/phc/env/tasks/humanoid_im_mcp.py) 将已训 primitive 组合到 MCP task；[`amp_network_pnn_builder.py`](https://github.com/ZhengyiLuo/PHC/blob/846988d433ce1f341e85ac6fbd2cd51911bb3341/phc/learning/amp_network_pnn_builder.py) 是渐进网络构建入口。
- [G1 PHC env config](https://github.com/ZhengyiLuo/PHC/blob/846988d433ce1f341e85ac6fbd2cd51911bb3341/phc/data/cfg/env/env_im_g1_phc.yaml) 将人形 avatar 方法接到机器人配置，但配置存在不等于论文已做 G1 真机验证。

## 最小复现路径

首先锁定 commit、Isaac Gym/CUDA/Python、SMPL 资产和动作许可，用 README 的 minimal viable evaluation 与 sample motion 跑通预训策略。记录 motion key、fps、观测版本、误差分项、终止原因和 recovery/fall flag，而不只记录一个 success rate。

训练时先用单 primitive 和小动作集验证数据契约，再执行 PNN 的多阶段 fitting/forward 流程。每次增加 primitive 时保存 hard-sequence 列表与旧动作回归。最后单独测试 fall-only、far-only 和两者组合，避免跟踪平均分遮住恢复失败。

## 能力边界

PHC 原论文的实验对象是 simulated avatars，不是真实人形机器人。仓库后来增加 G1/H1 和 Isaac Lab 路径，不能改变原论文证据边界。README 中的 98.9%、100% 等当前数字还对应清理后的 AMASS 与特定评估配置，不是任意输入成功率。

完整 PMCP 训练并非单命令自动化，README 直接说明需要多次修改配置和训练阶段。复现者应把手工选择记录为实验参数，否则不同运行之间无法真正对比。

## 工程判断与风险

最值得复用的是将难动作识别、容量扩展和恢复数据显式放进训练状态机。最大风险是用当前 README 的综合成绩取代锁定论文版本，或将动画 avatar 的 recovery 误读为机器人自保护跌倒。

若将 G1/H1 配置用于硬件，需要独立的 actuator model、action scaling、observation ordering、时延、关节/力矩限幅、自碰撞、接触冲击、通信超时和急停安全案。先做 sim2sim 与吊装低增益测试，本页不提供上机参数。

评估还应保留失败动作、恢复用时和重置原因，避免只发布成功样例。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/ZhengyiLuo/PHC/tree/846988d433ce1f341e85ac6fbd2cd51911bb3341)
- [官方评估与训练说明](https://github.com/ZhengyiLuo/PHC/blob/846988d433ce1f341e85ac6fbd2cd51911bb3341/README.MD)
- [对应论文的中文深读](../phc-2305.06456.md)
