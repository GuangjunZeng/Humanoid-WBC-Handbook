# LATENT 开源工程：已发布的网球跟踪子管线与未发布的能力边界

[English version](en/latent.md)

审阅快照：[GalaxyGeneralRobotics/LATENT@`a931da5a70320ba3f07d38debcf71458a005530d`](https://github.com/GalaxyGeneralRobotics/LATENT/tree/a931da5a70320ba3f07d38debcf71458a005530d) · 678 stars（2026-08-12 快照）· 根目录未见可验证的项目级许可证，G1 资产保留自身条款，使用前需独立核对。star 只用于发现，不代表网球成功率、公开完整性或真机安全信心。

## 为什么收录

LATENT 论文设计了 tracker pre-training、DAgger online distillation、latent action model 和 high-level tennis policy 的完整高动态技能链。但固定 commit 的 README TODO 明确显示，当前已发布的是 motion tracking 代码和少量网球动作；在线蒸馏、latent prior、LAB 任务学习和高层 sim-to-real 设计仍在未完成项中。

这个项目值得独立一页，正是因为“论文有完整系统”与“当前开源仓库能复现什么”存在重要差异。本页只对已审阅的 tracker、动作预处理、评测和 ONNX 导出路径作细粒度判断。

## 它解决什么问题

网球动捕不是直接可部署的机器人轨迹。参考运动需要重采样、重算速度、平滑从默认姿态进入首帧，同时处理人与 G1 在右腕、球拍和关节限位上的差异。跟踪策略还要在 50 Hz 控制、500 Hz 物理步进与接触中保持全身稳定。

当前开源部分可以用来研究“不完美人体动作如何变成跟踪数据和低层策略”，但不能回答论文的核心高层问题：如何用 conditional latent prior 和 bounded residual 学会对来球的时空修正。

## 架构与数据流

已发布链路是 `retargeted NPZ motion → frequency alignment / velocity recomputation / smooth transition → G1TrackingTennis environment → PPO tracker → Brax checkpoint → ONNX export → MuJoCo playback`。训练 config 定义 `ctrl_dt=0.02`、`sim_dt=0.002`、奖励、终止、噪声与被排除关节的处理。

`G1TrackingTennisEnv` 将动作解释为相对参考关节的偏移，对活跃执行器生成 motor targets，同时为被排除的右腕等关节维护独立目标。这一设计能防止 tracker 强行复制不适合机器人球拍机构的人体腕部轨迹，但它不包含球飞行、击球目标或高层决策。

## 代码定位

- [`g1_tracking_tennis_task_config` 与 `G1TrackingTennisEnv`](https://github.com/GalaxyGeneralRobotics/LATENT/blob/a931da5a70320ba3f07d38debcf71458a005530d/latent_mj/envs/g1_tracking/train/g1_env_tracking_tennis.py) 定义时序、奖励、终止、观测、动作偏移和关节排除契约。
- [`PlayG1TrackingTennisEnv.step`](https://github.com/GalaxyGeneralRobotics/LATENT/blob/a931da5a70320ba3f07d38debcf71458a005530d/latent_mj/envs/g1_tracking/play/play_g1_env_tracking_tennis.py) 对照参考轨迹、活跃执行器和 excluded-joint targets，是检查 ONNX 回放契约的入口。
- [`preprocess_motion.py`](https://github.com/GalaxyGeneralRobotics/LATENT/blob/a931da5a70320ba3f07d38debcf71458a005530d/scripts/process_motion/preprocess_motion.py) 调用环境的 `preprocess_trajectory`，完成分批、频率对齐和可选起止平滑。
- [README 的发布 TODO](https://github.com/GalaxyGeneralRobotics/LATENT/blob/a931da5a70320ba3f07d38debcf71458a005530d/README.md) 是判定 DAgger、latent model、high-level policy 和 sim-to-real 尚未开放的一手依据。

## 最小复现路径

固定 commit、Python 3.12.9、JAX/MuJoCo/Brax、G1 资产、动作子集和 seed。先复制原始 NPZ，因为 README 说预处理会覆盖源文件。检查重采样前后帧率、角/线/关节速度、首尾平滑和脚底接触是否一致。

使用少量环境训练 `G1TrackingTennis`，逐项输出身体/关节/脚部跟踪、力矩、动作变化、限位、碰撞和 termination 奖励。再对同一 checkpoint 做 Brax 与 MuJoCo/ONNX 前 100 帧逐张量对账。最终只声称已复现 tracker，不声称已复现 LAB 或网球击球策略。

## 能力边界

当前仓库的最重要边界是“公开子集”。README 已勾选 tracker 和少量动作，却未勾选全量数据、全部预训练 tracker、DAgger 在线蒸馏、latent action model、高层网球策略和 sim-to-real 设计。因此论文 Figure/Table 中的高层效果不能作为仓库复现验收。

官方说明还披露真机实验使用 50+ 个动捕相机、19×15 m 场地和约 35 万元租赁成本。这意味着开源 tracker 命令可运行与论文端到端系统可复现是两个不同命题。

## 工程判断与风险

最值得复用的是对不完美参考动作做显式预处理，并将不适合人形执行的右腕自由度从 tracker 动作中隔离。最需避免的是看到仓库名称后就默认 LAB 核心已开源；自动化索引应同时保存 reviewed commit 和 TODO 快照。

真机网球涉及高速球拍、飞行球与大幅度身体动作。即使只测 tracker，也要使用无人禁入区、球拍机械固定、关节/力矩/速度硬限幅、吊装或防倒、独立急停与专职安全员。未开源的高层控制不应由读者根据论文描述猜写后直接上机。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/GalaxyGeneralRobotics/LATENT/tree/a931da5a70320ba3f07d38debcf71458a005530d)
- [已发布 tracker 范围与 TODO](https://github.com/GalaxyGeneralRobotics/LATENT/blob/a931da5a70320ba3f07d38debcf71458a005530d/README.md)
- [对应论文的中文深读](../latent-2603.12686.md)
