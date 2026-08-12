# legged_gym：人形强化学习仓库广泛继承的 Isaac Gym 环境基座

[English version](en/legged-gym.md)

审阅快照：[leggedrobotics/legged_gym@`8fa29acc6fd1910c3d9659eef6310bdd301cde0a`](https://github.com/leggedrobotics/legged_gym/tree/8fa29acc6fd1910c3d9659eef6310bdd301cde0a) · 3079 stars（2026-08-12 快照）· BSD-3-Clause，内置机器人资产和依赖保留各自许可。star 只用于发现工程影响力，不是人形适配完成度、sim-to-real 成功率或硬件安全证明。

## 为什么收录

legged_gym 是大量腿式与人形 RL 项目的代码祖先。它将 Isaac Gym 并行环境、动作到 PD/执行器网络的转换、observation、reward、termination、terrain/command curriculum、域随机化和 policy export 放进可继承基类。Human2humanoid、Humanoid-Gym 等后续工程延续了其许多契约。

当前固定快照的官方任务主要是 ANYmal、A1 和 Cassie，不是完成的现代人形训练仓库。本页把它作为 infrastructure（基础设施）审阅，说清人形仓库“继承了什么”，不把四足实验写成人形结论。

## 它解决什么问题

高并行 locomotion RL 的主要复现障碍并不只是 PPO，而是每个 environment step 内的时序和尺度：policy action 经多次 physics step 执行，观测在哪一刻刷新，timeout 是否作为 terminal，reward scale 是否乘 dt，以及随机摩擦/质量/推扰的采样时机。

legged_gym 把这些放在 `LeggedRobot.step`、`post_physics_step`、config 嵌套类和自动 reward discovery 中。这些抽象降低新本体接入成本，但也使默认值容易被无意继承；对人形而言，躯干、手臂、自碰撞和非足接触都需重新定义。

## 架构与数据流

主链是 `task registry + robot config → vectorized Isaac Gym environments → observations/commands → external rsl_rl PPO → action clipping → decimated PD or actuator-network torques → physics → termination/reward/reset → rollout`。任务类继承 `LeggedRobot`，config 类继承 `LeggedRobotCfg/LeggedRobotCfgPPO`，注册表绑定名称与环境/训练配置。

`step` 在一次 policy action 内循环 `control.decimation` 次，每次计算力矩并推进仿真；`post_physics_step` 再检查终止、计算 reward、reset 和 observation。`_prepare_reward_function` 按 config 中非零 scale 动态绑定 `_reward_<name>`，因此名称拼写和继承覆盖都是可以让训练“正常运行但目标变了”的高风险点。

## 代码定位

- [`LeggedRobot.step` 与 `post_physics_step`](https://github.com/leggedrobotics/legged_gym/blob/8fa29acc6fd1910c3d9659eef6310bdd301cde0a/legged_gym/envs/base/legged_robot.py) 定义 action clipping、decimation、力矩、物理、reward、termination、reset 和 observation 的顺序。
- [`LeggedRobotCfg`](https://github.com/leggedrobotics/legged_gym/blob/8fa29acc6fd1910c3d9659eef6310bdd301cde0a/legged_gym/envs/base/legged_robot_config.py) 定义观测/特权观测、控制、asset、randomization、reward 和 PPO 默认契约。
- [`_prepare_reward_function` 与 curriculum`](https://github.com/leggedrobotics/legged_gym/blob/8fa29acc6fd1910c3d9659eef6310bdd301cde0a/legged_gym/envs/base/legged_robot.py) 将非零 scale 映射到奖励函数，并实现地形/指令课程。
- [`task_registry`](https://github.com/leggedrobotics/legged_gym/blob/8fa29acc6fd1910c3d9659eef6310bdd301cde0a/legged_gym/utils/task_registry.py) 连接任务名、环境 config、PPO config、创建与恢复训练。
- [`export_policy_as_jit`](https://github.com/leggedrobotics/legged_gym/blob/8fa29acc6fd1910c3d9659eef6310bdd301cde0a/legged_gym/utils/helpers.py) 显示前馈/循环策略导出与隐状态 reset 契约。

## 最小复现路径

按快照固定 Python 3.8、PyTorch 1.10/CUDA 11.3、Isaac Gym Preview 3、rsl_rl v1.0.2、commit 和机器人资产。先用官方 `anymal_c_flat` 验证环境契约，记录 observation/action shape、physics/policy dt、每项 reward、termination、摩擦/质量/推扰样本和 terrain level。

接入人形时新建环境和 config，不改写共享基类的默认值。显式列出关节顺序、默认姿态、PD/力矩、feet 和 termination body 名、接触传感方法、特权观测与 actor 观测。先对比单环境逐步输出，再扩大到数千环境。

## 能力边界

官方 README 已说明项目随 Isaac Gym 向 Isaac Sim 迁移后只有有限更新，新应用建议使用 Isaac Lab。因此该 commit 是复现历史工作和理解继承契约的锚点，不是新项目的默认选型建议。

官方 Known Issues 还指出 GPU triangle-mesh terrain 上 `net_contact_force_tensor` 不可靠，需用合理布置的 force sensor 绕过。这对依赖接触终止、脚空时间或足滑指标的人形任务是直接边界，不能忽略。

## 工程判断与风险

最值得复用的是环境与 config 的继承结构、奖励动态绑定和时序集中实现；最大风险是后续仓库只复制基类却没有重新审计默认观测、contact 和 termination。任何 fork 都应保留与这个 commit 的契约 diff，不只记录算法超参数。

真机部署不属于该环境代码的安全保证。需要独立关节/力矩/速度限幅、观测顺序和尺度测试、通信超时、非足接触保护、姿态超限、吊装/支撑和物理急停。应先在第二引擎重放完整 observation/action 契约，再进入低能量硬件验收。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/leggedrobotics/legged_gym/tree/8fa29acc6fd1910c3d9659eef6310bdd301cde0a)
- [架构、迁移公告与 Known Issues](https://github.com/leggedrobotics/legged_gym/blob/8fa29acc6fd1910c3d9659eef6310bdd301cde0a/README.md)
- [对应论文的中文深读](../learning-walk-2109.11978.md)
