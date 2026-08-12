# Unitree RL Mjlab：用 MuJoCo/MJLab 复核轻量训练与部署

[English version](en/unitree-rl-mjlab.md)

审阅快照：[unitreerobotics/unitree_rl_mjlab@`1425b15f73bd4095f0df53709d7c389c3eb9e790`](https://github.com/unitreerobotics/unitree_rl_mjlab/tree/1425b15f73bd4095f0df53709d7c389c3eb9e790) · 578 stars（2026-08-12 快照）· Apache-2.0。star 是发现信号，不是仿真精度、策略质量或真机安全置信度；当前没有一篇与整个仓库完全对应的论文。

## 为什么收录

Unitree RL Mjlab 是官方组织提供的另一条工程路线：保留类似 Isaac Lab 的 manager-based API，但以 MuJoCo/MuJoCo-Warp 为物理后端。它支持多种 Unitree 本体、速度跟踪、G1 动作模仿、ONNX 导出和 SDK2 部署，因此可以与 Unitree RL Lab 做受控的后端对照，而不是默认某个模拟器更接近真机。

它属于地形运动与通用跟踪两个既有 topic。独立页的价值是解释“轻量”具体落在哪些接口，以及训练、play、sim2sim 与实机是否共享配置。高 star 和官方身份不替代接触模型、执行器模型与真机统计的实证检查。

## 它解决什么问题

Omniverse/PhysX 栈功能完整但安装和计算成本较高；研究者希望用更轻的 MuJoCo 路径快速训练、回放和检查部署。Mjlab 将场景、命令、观测、奖励、终止和 runner 组织为清晰配置，并把多环境训练与 Unitree C++ 控制程序串联起来。

它也提供动作模仿：CSV 被重采样为 NPZ，`MotionCommand` 根据时间生成参考，训练任务追踪关节与刚体状态。这里最重要的工程问题不是能否跑起 PPO，而是 CSV→NPZ、模拟器状态、ONNX 输入和 C++ observation 是否保持同一顺序、单位与坐标系。

## 架构与数据流

速度路径是 `MJCF 资产 → VelocityEnvCfg → 命令/观测/奖励/课程 → RSL-RL runner → ONNX`；跟踪路径是 `CSV → csv_to_npz.py → MotionLoader/MotionCommand → TrackingEnvCfg → policy`。play 脚本在 MuJoCo 中复现 checkpoint，部署目录读取 ONNX 与 YAML 并通过 unitree_sdk2 发送关节命令。

仓库支持许多机器人常量和 XML，但每个任务配置仍需显式绑定关节、执行器与 observation。MuJoCo-Warp 提高并行能力不等于与 CPU MuJoCo 数值完全相同；GPU kernel、时间步、接触求解与渲染设置都应被版本化。

## 代码定位

- [`MotionLoader` 与 `MotionCommand`](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/src/tasks/tracking/mdp/commands.py) 读取动作并生成跟踪参考、时间索引和重采样状态。
- [`TrackingEnvCfg`](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/src/tasks/tracking/tracking_env_cfg.py) 汇总跟踪任务的 manager 项与模拟参数。
- [速度奖励与课程](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/src/tasks/velocity/mdp/rewards.py) 是检查速度命令、步态和正则项具体含义的入口。
- [`scripts/train.py`](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/scripts/train.py) 解析 task、分布式参数、日志目录和 runner，决定配置怎样进入训练。
- [`State_Mimic.cpp`](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/deploy/robots/g1/src/State_Mimic.cpp) 是 G1 模仿策略在部署端的状态实现。

## 最小复现路径

固定 Python、mjlab、MuJoCo/MuJoCo-Warp、RSL-RL 与仓库 commit。先运行 `python scripts/train.py Unitree-G1-Flat --env.scene.num-envs=64` 做 smoke test，保存实际解析后的配置。然后用自带 G1 CSV 转成 NPZ，检查输入/输出 FPS、根四元数顺序、关节名和一阶差分，再以少量环境启动 tracking。

验收需要同一 checkpoint 在 `scripts/play.py`、集成的 unitree_mujoco 和部署控制程序中逐级复现。保存每层 observation/action 数组并做逐字段比较；报告速度跟踪误差、根高度、姿态、脚滑、终止原因、NaN/饱和以及墙钟训练时间。若与 Isaac Lab 对照，只能改变后端，不能同时改变奖励和机器人模型。

## 能力边界

README 列出 Go2、A2、AS2、G1、R1、H1_2、H2，不等于每个本体的速度、跟踪与真机路径同等成熟。示例预训练策略也不能证明用户自训策略安全。MJCF 资产与用户真实机器人参数可能不同，尤其是惯量、阻尼、摩擦和碰撞几何。

GPU MuJoCo-Warp 的高并行吞吐不自动保证确定性或物理一致性。外部依赖和 API 仍在快速变化，命令行与任务名需绑定 commit。实机流程要求进入 debug mode 并直接连接控制器，必须视为独立高风险步骤。

## 工程判断与风险

这个仓库最有用的方式不是替代所有 Isaac Lab 工作，而是提供第二个官方后端来隔离模拟器依赖。若同一控制契约在两个后端都通过、但真机失败，排查可以进一步聚焦执行器、状态估计、通信和硬件；若两后端已分歧，应先解决模型与离散化差异。

真机前必须完成 sim2sim、输入输出一致性、动作限幅、控制周期和超时检查；悬空或支撑进入 debug mode，保持物理急停、低增益、低速与小范围命令，监控力矩、温度和通信。本页不认可直接复制 README 步骤即上机，也不提供安全参数。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/unitreerobotics/unitree_rl_mjlab/tree/1425b15f73bd4095f0df53709d7c389c3eb9e790)
- [G1 资产常量](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/src/assets/robots/unitree_g1/g1_constants.py)
- [G1 部署配置](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/deploy/robots/g1/config/config.yaml)
