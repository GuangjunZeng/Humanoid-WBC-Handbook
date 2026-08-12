# human2humanoid：H2O 与 OmniH2O 的人体到人形跟踪仓库

[English version](en/human2humanoid.md)

审阅快照：[LeCAR-Lab/human2humanoid@`750f1fa052641f0fde43669d50cb4e407dabe6c8`](https://github.com/LeCAR-Lab/human2humanoid/tree/750f1fa052641f0fde43669d50cb4e407dabe6c8) · 1050 stars（2026-08-12 快照）· 主项目标注 CC BY-NC 4.0，依赖、动作、模型与机器人资产仍需核对各自条款。star 不是遥操时延、稳定性或真机安全信心。

## 为什么收录

human2humanoid 同时承载 H2O 和 OmniH2O 的训练代码。H2O 聚焦从 RGB 人体姿态到 H1 全身跟踪，OmniH2O 将命令缩减为头和双手三点，用 privileged teacher 与 DAgger 学习不显式依赖全局线速度的历史学生策略。

这个仓库的价值是把 motion data、H1 task config、PPO/DAgger runner 和教师标注放在一条可追踪代码链上。但 H2O 和 OmniH2O 的观测契约和证据边界不同，不能用同一仓库就将两篇论文的主张互换。

## 它解决什么问题

实时全身遥操需要将人体参考、机器人本体感知和延迟不确定性合并为一个固定 observation vector。全局线速度在仿真中容易得到，在真机却依赖外部 MoCap、VIO 或估计器；如果训练契约将其隐式当作真值，部署会突然失效。

H2O 使用 sim-to-data 过滤将重定向动作先交给 privileged imitator，去掉难执行样本。OmniH2O 再让教师用特权状态产生 action labels，学生从 25 帧本体感知和上一动作历史中弥补被移除的速度信息。

## 架构与数据流

H2O 路径可概括为 `human pose → retargeted robot motion → privileged simulator filter → PPO full-body tracking → H1 policy`。OmniH2O 路径为 `head/hand goals + privileged state → teacher action → rollout labels → DAgger student with 25-step history → sparse-command policy`。

`LeggedRobot.step` 是两条路径的时序交汇点：它执行 action、维护历史、计算 teacher action 并将标注放入 info。runner 再把 rollout 数据交给 PPO 的 imitation optimization。若 history order、观测归一化或 teacher/student action scale 不一致，DAgger 损失仍可下降却学到错误控制契约。

## 代码定位

- [`H1TeleopCfg`](https://github.com/LeCAR-Lab/human2humanoid/blob/750f1fa052641f0fde43669d50cb4e407dabe6c8/legged_gym/legged_gym/envs/h1/h1_teleop_config.py) 定义 H2O/OmniH2O 的 actor/privileged observation、19 维动作、控制延迟、增益与质量/质心/推扰随机化。
- [`LeggedRobot.load_expert` 和 `step`](https://github.com/LeCAR-Lab/human2humanoid/blob/750f1fa052641f0fde43669d50cb4e407dabe6c8/legged_gym/legged_gym/envs/base/legged_robot.py) 加载教师、在学生访问的状态上产生 action label，并维护含/不含线速度的历史对照。
- [`OnPolicyRunner.learn`](https://github.com/LeCAR-Lab/human2humanoid/blob/750f1fa052641f0fde43669d50cb4e407dabe6c8/rsl_rl/rsl_rl/runners/on_policy_runner.py) 组织 rollout 和 teacher label；[`PPO._optimize_kin`](https://github.com/LeCAR-Lab/human2humanoid/blob/750f1fa052641f0fde43669d50cb4e407dabe6c8/rsl_rl/rsl_rl/algorithms/ppo.py) 优化学生与教师的动作差。
- [`compute_observations`](https://github.com/LeCAR-Lab/human2humanoid/blob/750f1fa052641f0fde43669d50cb4e407dabe6c8/legged_gym/legged_gym/envs/base/legged_robot.py) 与 teleop reward 函数是核对关节、本体、关键点参考及上一动作顺序的入口。

## 最小复现路径

首先固定 commit、Isaac Gym/CUDA、H1 资产、motion file 和观测变体。用小环境数加载预训 teacher/student，逐项打印 actor、privileged、history、target keypoint 和 action tensor 的名称、shape、均值与尺度。

对 OmniH2O，使用同一组 20 条站立动作复现论文对照，同时额外增加转身、快速手部、身体遮挡和延迟注入。报告跟踪误差、失败类型、history ablation 和多 seed，不应只看演示视频。

## 能力边界

H2O 的“RGB-only”是人体命令入口的描述，论文真机机器人线速度仍来自外部 MoCap。OmniH2O 在其 H1、19-DoF、50 Hz 设置中表明历史策略可不显式输入全局线速度，不能外推为所有机器人或动态动作都不需要速度估计。

仓库中不同 config 保留线速度、历史和特权信息变体。复现者若不报告确切 config，就无法判断成绩来自哪种观测契约。

此外，仓库把人体关键点误差、机器人状态奖励与控制正则项同时组合。因此迁移到新本体时，必须重新核对关键点索引、骨架尺度、默认关节角和奖励归一化；仅替换 URDF 并不构成有效复现。

## 工程判断与风险

最值得复用的是将 teacher action 与 student history 放在同一 rollout 语义中，并对线速度依赖做显式变体。最需防范的是训练时漏入 privileged observation，或导出后改变 history/action order 却不做契约测试。

真机遥操还需要人体输入失联、姿态跳变、延迟、关节/力矩/速度限制、自碰撞、接触冲击和物理急停安全案。先做固定指令、低速、支撑或吊装测试，再扩展人体命令范围。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/LeCAR-Lab/human2humanoid/tree/750f1fa052641f0fde43669d50cb4e407dabe6c8)
- [教师、历史与观测实现](https://github.com/LeCAR-Lab/human2humanoid/blob/750f1fa052641f0fde43669d50cb4e407dabe6c8/legged_gym/legged_gym/envs/base/legged_robot.py)
- [OmniH2O 中文深读](../omnih2o-2406.08858v1.md) · [H2O 中文深读](../human2humanoid-2403.04436.md)
