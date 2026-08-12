# Humanoid-Gym：Isaac Gym 训练、MuJoCo 回放与 XBot 部署基线

[English version](en/humanoid-gym.md)

审阅快照：[roboterax/humanoid-gym@`ae46e201c85a2b17e7f2cea59a441dae7ea88a8f`](https://github.com/roboterax/humanoid-gym/tree/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f) · 2062 stars（2026-08-12 快照）· BSD-3-Clause，并继承 legged_gym/rsl_rl 及机器人资产的相关通知。star 不是 zero-shot sim-to-real 在所有本体和地形上成功的证据。

## 为什么收录

Humanoid-Gym 是人形 locomotion 开源生态的高星经典基线。它从 legged_gym/rsl_rl 发展而来，把 XBot-S/XBot-L 的 Isaac Gym PPO 训练、observation history、domain randomization、reward、termination、policy export、MuJoCo sim2sim 和真机接口放在一条工程链。

它的差异化价值不是“又一个 PPO”，而是将第二物理引擎放在真机之前作为低成本失败筛查。该流程可以发现 observation/action order、PD decimation、模型参数和终止条件错位，但 sim2sim 通过不等于硬件通过。

## 它解决什么问题

人形行走策略对控制频率、history stack、上一动作、姿态表示、脚部接触和 PD gain 很敏感。训练引擎里的默认值若没有在导出和部署中原样保留，策略可在一个物理引擎正常，到另一个引擎立即失稳。

Humanoid-Gym 通过 XBot 专用 config 把 15 帧 actor history、3 帧 critic history、策略/PD decimation、reward scale、domain randomization 和 safety scale 显式化。这些是可审计契约，不是可盲目复制到其他本体的参数。

## 架构与数据流

主路径为 `velocity command + proprioception/history → actor policy → target joint action → decimated PD control → Isaac Gym rollout → PPO update → exported policy → MuJoCo sim2sim → XBot deployment`。critic 可以读更多特权信息，actor 必须严格限制为部署可用状态。

`LeggedRobot.step` 在一个 policy action 内执行多个 1 ms physics step，因而 policy 频率、PD 频率和控制延迟必须分开记录。history buffer 是有状态的部署组件；只导出网络而忽略 buffer 初始化和更新顺序，会导致模型与训练不等价。

## 代码定位

- [`XBotLCfg`](https://github.com/roboterax/humanoid-gym/blob/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f/humanoid/envs/xbot_l/xbot_l_config.py) 中的 `frame_stack/c_frame_stack`、`control.decimation`、`rewards.scales`、`domain_rand` 和 `safety` 定义 XBot-L 核心契约。
- [`LeggedRobot.step`](https://github.com/roboterax/humanoid-gym/blob/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f/humanoid/envs/base/legged_robot.py) 执行 decimated control，维护历史，并将 action 交给仿真。
- [`LeggedRobot.check_termination`](https://github.com/roboterax/humanoid-gym/blob/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f/humanoid/envs/base/legged_robot.py) 把非足接触和其他失败变成 reset，其语义需与 MuJoCo/真机故障分类对齐。
- [MuJoCo deployment configuration](https://github.com/roboterax/humanoid-gym/blob/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f/deploy/deploy_mujoco/deploy_mujoco.py) 是审查导出 observation、action、PD 与 model mapping 的第二引擎入口。

## 最小复现路径

锁定 commit、Isaac Gym、rsl_rl、CUDA、XBot 资产和一个预训 checkpoint。先在 Isaac Gym 使用固定初始状态和速度指令回放，导出每个 observation slice、history frame、action、PD target、reward term 和 termination reason。

然后在 MuJoCo 使用同一初始根姿态、关节、上一动作和 history，比较前 100、1000 与整段 rollout 的关节/根/接触差异。增加模型质量、摩擦、延迟和 sensor noise 扰动，记录第一个分歧源。

## 能力边界

对应论文给出 XBot-S/XBot-L 真机演示，但缺少大规模重复成功率、跌倒/急停率和跨引擎与真机失败的相关统计。因此“zero-shot”只能按该工程流程与所展示硬件理解，不是任意机器人的一键迁移。

MuJoCo sim2sim 是失败筛查层，不是真机替代品。两个引擎可以共享同样错误的 URDF、力矩限制或 actuator model，因而“两边一致”可能只说明错误被复制。

第二引擎对比应保留可追溯的初始状态和第一个分歧时刻，而不只比较最终是否跌倒。如果分歧首先出现在观测或 PD 目标，应先修复接口契约；若首先出现在接触力和摩擦状态，才进入引擎参数与模型差异的定量定位。这种逐帧对账比盲目调整随机化范围更容易找到根因。

## 工程判断与风险

最值得复用的是训练—第二引擎—真机的分层门禁；最需防范的是认为第二引擎通过即安全。应将每个失败分为观测/动作契约、引擎物理、策略过拟合、执行器/传感器和 OOD 指令。

实验报告还应列出训练、MuJoCo 和真机三端的关节顺序、观测尺度、动作限幅、控制周期与历史初始化对照表。这些字段中任何一个错位，都可以在不修改网络参数的情况下完全改变闭环行为。

真机需要厂商限幅、起始姿态检查、通信超时、非足接触保护、姿态超限、支撑/吊装和物理急停。附录增益和 safety scale 只属于论文本体，不可直接复制到其他硬件。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/roboterax/humanoid-gym/tree/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f)
- [XBot-L 训练契约](https://github.com/roboterax/humanoid-gym/blob/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f/humanoid/envs/xbot_l/xbot_l_config.py)
- [对应论文的中文深读](../humanoid-gym-2404.05695v2.md)
