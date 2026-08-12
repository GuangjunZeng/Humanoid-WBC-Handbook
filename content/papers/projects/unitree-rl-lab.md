# Unitree RL Lab：官方 Isaac Lab 训练到 G1 部署链

[English version](en/unitree-rl-lab.md)

审阅快照：[unitreerobotics/unitree_rl_lab@`4960b84732b0c2ec593dccbfe963fda1bcd7b1e3`](https://github.com/unitreerobotics/unitree_rl_lab/tree/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3) · 1272 stars（2026-08-12 快照）· Apache-2.0。star 只说明发现优先级，不是算法置信度；该仓库没有以一篇对应论文作为主证据。

## 为什么收录

这是 Unitree 官方组织维护的 Isaac Lab 强化学习环境，公开 Go2、H1 与 G1-29DoF 的训练、策略导出、MuJoCo sim2sim 和 C++ 部署接口。它填补了论文页经常缺失的最后一段：训练任务中的 observation/action 如何变成 ONNX，再怎样进入 SDK2 控制进程。

项目同时属于地形运动和通用跟踪 topic，因为它包含速度跟踪与动作模仿两类任务。官方身份与高 star 使其值得优先审计，但不能证明默认策略适合任意固件、机器人批次或现场环境；本页只对固定 commit 的公开代码作工程解读。

## 它解决什么问题

人形 RL 的复现失败往往不是 PPO 公式不同，而是资产、执行器配置、观测顺序、action scaling、控制周期和部署端预处理没有对齐。Unitree RL Lab 将机器人资产配置、Isaac Lab 任务、RSL-RL 训练、ONNX 导出与 SDK2 运行时放在同一仓库，降低跨项目猜测接口的成本。

速度任务与 mimic 任务共享 manager-based 结构，但参考来源与奖励不同。mimic 路径需要按动作时间采样参考刚体与关节状态；速度路径则围绕命令、地形与步态奖励训练。两者不能只凭同一个 deploy 程序就视为相同安全边界。

## 架构与数据流

训练侧路径为 `USD/URDF 资产 → RobotEnvCfg → Commands/Observations/Actions/Rewards/Events/Terminations → RSL-RL → checkpoint/ONNX`。mimic 中 `MotionLoader` 读取动作，`MotionCommand` 维护当前片段、时间和自适应采样，奖励函数比较机器人与参考的根、刚体姿态和速度。

部署侧路径为 `ONNX + deploy.yaml → State_RLBase/State_Mimic → observation 拼装与归一化 → policy inference → joint command → unitree_sdk2`。FSM 先保持被动或固定站立，再切入策略。MuJoCo 通过相同通信路径做 sim2sim，有助于发现关节映射和部署端代码错误，但不会覆盖真实执行器、电池、网络和地面差异。

## 代码定位

- [`MotionLoader` 与 `MotionCommand`](https://github.com/unitreerobotics/unitree_rl_lab/blob/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3/source/unitree_rl_lab/unitree_rl_lab/tasks/mimic/mdp/commands.py) 管理动作数据、参考状态、时间推进与自适应重采样。
- [mimic 奖励项](https://github.com/unitreerobotics/unitree_rl_lab/blob/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3/source/unitree_rl_lab/unitree_rl_lab/tasks/mimic/mdp/rewards.py) 定义根位置/姿态、刚体相对姿态与速度等跟踪误差。
- [`RobotEnvCfg`](https://github.com/unitreerobotics/unitree_rl_lab/blob/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3/source/unitree_rl_lab/unitree_rl_lab/tasks/mimic/robots/g1_29dof/gangnanm_style/tracking_env_cfg.py) 汇总 G1 场景、动作、观测、随机化、奖励和终止。
- [`State_Mimic.cpp`](https://github.com/unitreerobotics/unitree_rl_lab/blob/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3/deploy/robots/g1/src/State_Mimic.cpp) 是 G1 mimic 策略进入部署 FSM 的具体运行时。

## 最小复现路径

固定 Isaac Sim 5.1、Isaac Lab 2.3 与本页 commit，下载并哈希 Unitree 模型；先列出任务，再用 `Unitree-G1-29dof-Velocity` 运行少量环境 smoke test。记录 observation/action 字段、单位、控制 decimation 和关节名。训练后保存完整配置、seed、依赖 commit 与 ONNX 导出日志。

部署验收按 `Isaac Lab play → unitree_mujoco + g1_ctrl → 真机` 分级。sim2sim 必须使用将要部署的 `deploy.yaml` 和 ONNX，比较 Python 与 C++ 的逐字段 observation 和单步 action；再施加阶跃命令、网络延迟和异常输入，确认 FSM 回退、限幅与急停路径。

## 能力边界

仓库列出的机器人和任务不代表每个组合都有同等训练质量或真机验证。README 的 GIF 是定性展示，缺少统一成功率、误差分布与失败样本。模型文件来自外部仓库，URDF 与 USD 两条资产路径也可能产生质量、关节和碰撞差异。

官方组织身份不等于当前 commit 与用户机器人固件完全匹配。部署要求关闭板载控制程序，属于高风险状态变更；网络接口、Domain ID、弹性手、手柄与机器人配置必须逐项核对。ONNX Runtime 与其他第三方二进制还需要许可证和平台兼容性检查。

## 工程判断与风险

该项目最适合作为“官方接口对齐基线”：用它核对 Unitree 资产、SDK2、关节顺序和部署状态机，再与研究算法比较。技术结论应来自固定配置下的重复实验，而不是把仓库全部 task 名称视为已验证能力。推荐为每个 checkpoint 生成机器可读 manifest，绑定任务、资产、观测、action scale、commit 与固件。

真机前必须悬空或支撑进入调试模式，确保被动、阻尼、站立和策略状态可控；使用低增益、低速、小命令范围和物理急停，监控关节位置、速度、力矩、温度与通信超时。任何映射或尺度不一致都可能造成高速动作，本页不提供直接上机参数。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/unitreerobotics/unitree_rl_lab/tree/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3)
- [G1 部署配置](https://github.com/unitreerobotics/unitree_rl_lab/blob/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3/deploy/robots/g1/config/config.yaml)
- [Apache-2.0 许可证](https://github.com/unitreerobotics/unitree_rl_lab/blob/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3/LICENSE)
