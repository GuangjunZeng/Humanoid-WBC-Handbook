# ProtoMotions 3：统一人形动作学习、仿真与部署的研究框架

[English version](en/protomotions.md)

审阅快照：[NVlabs/ProtoMotions@`5241478e35a7dcf5d1455dac2df0486d5e7f440a`](https://github.com/NVlabs/ProtoMotions/tree/5241478e35a7dcf5d1455dac2df0486d5e7f440a) · 2286 stars（2026-08-12 快照）· Apache-2.0；SMPL/SMPL-H、Unitree、BeyondMimic 与各仿真器等第三方软件、模型和资产仍受各自条款约束。star 只用于发现高影响力项目，不代表算法正确性、复现实验完成度或真机安全置信度。

## 为什么收录

ProtoMotions 不是单一 WBC 算法，而是把动作数据、机器人模型、仿真器、强化学习算法、观测/奖励/终止组件、评测与部署接口放进同一工程骨架。它同时关联 CALM 的可控潜技能（controllable latent skill）与 MaskedMimic 的掩码动作补全（masked motion inpainting），当前 v3 代码又加入通用跟踪、GPC/PEFT、跨仿真器测试和 G1 部署路径，因此适合作为“论文思想怎样落成可组合系统”的代码地图。

项目页只审阅固定 commit 的工程结构，不把仓库当前 README 中的 40+ 小时 AMASS、4/24 张 A100、BONES-SEED 约 142K 动作或零样本实机演示视作本 Handbook 已独立复现的结果。这些数字是作者报告的能力声明；要获得实验级置信度，仍需锁定数据版本、训练配置、硬件、随机种子、checkpoint 和评测脚本再复跑。

## 它解决什么问题

动作控制研究常见的困难并不是“缺一个 PPO”，而是论文之间的数据格式、身体骨架、观测定义、奖励、仿真后端和日志协议都不同。这样既难比较 AMP、ASE、Mimic、MaskedMimic 与潜技能路线，也容易在从 SMPL 数字人切换到 H1_2 或 G1 时把坐标、关节顺序和控制增益悄悄改掉。ProtoMotions 试图用共享环境上下文和显式组件绑定把这些差异暴露出来。

它还试图缩小训练—部署之间的观测实现差异：导出器把可导出的观测计算与策略一起固化进 ONNX，并生成描述输入/输出的 YAML；MuJoCo 测试器只从原始状态构造输入、执行策略、产生 PD 位置目标并步进仿真。这个设计方向有价值，但“导出成功”不等于真机时序、传感器标定、执行器带宽与安全状态机已经一致。

## 架构与数据流

训练主链可概括为 `motion source → retarget / packaged motion → RobotConfig + simulator → EnvContext → control components → observation / reward / termination MdpComponents → agent (PPO / AMP / mimic / supervised latent model) → checkpoint + evaluation`。实验文件不是复制一个巨型环境类，而是选择组件并把每个纯张量函数的参数绑定到 `FieldPath`；运行时从上下文取动态量，静态参数则固定在组件中。

以 steering 示例为例，`SteeringControl` 维护目标方向、速度和朝向；`compute_steering_obs` 把目标转换到机器人局部坐标；`compute_heading_velocity_rew` 组合速度方向与面朝方向奖励；实验配置再将它们作为 `MdpComponent` 接入环境。它像“控制系统接线板”：每根线的来源与去向可检查，比隐含读取全局环境成员更利于替换任务和导出。

MaskedMimic 路线在控制层保存未来时间、可见姿态与身体掩码；模型层则把稀疏观测送入 prior 得到部署可用潜变量分布，训练时另用 privileged encoder 产生残差后验，再由共享 trunk 解码动作。这里的关键边界是：当前 v3 类与 2024 论文思想相关，但代码已经重构，不能用当前类名反推原论文全部表格仍可逐项复现。

部署链是 `checkpoint + experiment config → MockContext / MdpComponent bindings → ONNX policy with observation graph + YAML contract → raw MuJoCo or robot state → quaternion/body-index conversion → policy inference → PD targets → simulator or hardware adapter`。仓库提供的是接口与示例，不是经过第三方功能安全认证的控制栈。

## 代码定位

- [`MdpComponent`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/envs/mdp_component.py) 区分动态 `FieldPath`、静态参数与元数据，并提供 `get_bindings_dict()` 给 ONNX 导出路径使用。
- [`EnvContext` 与各领域 view`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/envs/context_views.py) 定义 current、historical、mimic、masked-mimic、steering 等显式数据契约。
- [`env_config` 的 steering 组合`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/examples/experiments/steering/mlp.py) 展示控制、观测和奖励函数怎样通过上下文路径接线，而非藏进继承链。
- [`compute_heading_velocity_rew`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/envs/rewards/task.py) 是纯张量任务奖励核，可单独检查输入、速度投影和权重组合。
- [`MaskedMimicControl`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/envs/control/masked_mimic_control.py) 管理目标时间、身体/姿态可见掩码与稀疏条件上下文。
- [`MaskedMimicModel`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/agents/supervised/masked_mimic_model.py) 分开部署 prior、训练期 privileged encoder、潜变量采样和共享动作 trunk。
- [`export_tracker`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/deployment/export_bm_tracker_onnx.py) 从组件绑定构造 ONNX 输入，做可选 onnxruntime 对照并生成 YAML sidecar。
- [`run` 与 `build_onnx_inputs`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/deployment/test_tracker_mujoco.py) 明确 MuJoCo 原始状态、四元数顺序、body index、历史缓冲、推理、PD 目标和 decimation 的连接点。

## 最小复现路径

第一阶段只验证框架契约，不直接训练大模型。固定该 commit、Python/CUDA、一个仿真后端和 G1 或 H1_2 资产许可；运行最小 simulator/tutorial，再运行预训练 mimic inference。保存解析后的 `RobotConfig`、身体/关节顺序、仿真步长、控制 decimation、观测维度、动作尺度、PD 增益和 checkpoint 哈希。任何维度或命名不一致都应在进入长训练前失败。

第二阶段用一个小动作子集训练 mimic MLP。先检查 motion 可视化和接触，再用至少三个种子报告学习曲线、成功率、刚体位置/旋转误差、脚滑、跌倒原因和训练吞吐；不能只播放最佳 rollout。若研究 MaskedMimic，再逐级从全身密集条件、稀疏关键帧、局部身体条件到完全隐藏片段做消融，核对 prior-only inference 与训练期 privileged path 没有信息泄漏。

第三阶段才检查部署：导出 ONNX，比较 PyTorch 与 onnxruntime 输出；用同一动作在训练仿真器和 MuJoCo 做 sim-to-sim，对齐四元数、body index、关节正负号、频率、历史帧和 stiffness/damping。实机前必须在吊架或保护架、急停、低增益、限幅、跌倒检测、通信超时和人工监督下逐级放开，并把每个安全事件与对应观测/命令日志保存下来。

## 能力边界

ProtoMotions 是研究框架，不保证不同仿真器的接触模型、摩擦、执行器或积分器等价；sim-to-sim 通过也不能证明 sim-to-real 成功。README 的大规模吞吐依赖高端 GPU、特定数据与配置，不代表普通工作站的资源需求。Isaac Gym、Isaac Lab、Newton、MuJoCo 和 Genesis 的支持成熟度也不相同，仓库甚至把 Genesis 标为未充分测试，不能把“存在适配目录”理解为同级验证。

Apache-2.0 覆盖仓库自身代码，但不自动授予 SMPL/SMPL-H 模型、机器人网格、数据集、预训练权重和仿真器的再分发权。当前代码是 ProtoMotions 3，CALM 与 MaskedMimic 论文对应的是更早实验快照；要复现论文必须跟随论文版本与论文记录，而不是只运行最新 main。

它也不是完整产品级 WBC：没有替用户完成传感器校准、状态估计、真实执行器辨识、热/电流保护、场地风险评估与系统级故障恢复。仓库演示中的零样本 G1 转移是作者证据，不构成对任意硬件、固件或负载的普遍承诺。

## 工程判断与风险

最值得借鉴的是可审计的数据契约：观测、奖励和终止函数尽量保持纯张量计算，运行时变量通过 `FieldPath` 显式绑定，同一绑定又服务于 ONNX 导出。它减少“训练用 Python 隐式观测、部署端手抄另一份 C++ 观测”的漂移风险，但仍需数值回归测试来证明两端一致。

最大的工程风险是把统一框架误当统一基准。算法使用的动作集、机器人、条件信息、网络规模、训练预算和终止规则不一致时，放在同一仓库并不自动形成公平比较。第二个风险是版本混淆：v3 的重构能力不能回写成 CALM 或 MaskedMimic 原论文的实验事实。第三个风险是从漂亮动作直接跳到真机；高速全身动作可能引发自碰撞、支撑丢失、过流和机械损伤。

因此，本页的结论等级是“固定 commit 的架构与接口已检查”，不是“全部算法及 README 性能已复现”。任何用于实机的策略都必须经过独立动作清洗、动力学与接触测试、跨仿真验证以及硬件安全评审。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/NVlabs/ProtoMotions/tree/5241478e35a7dcf5d1455dac2df0486d5e7f440a)
- [固定 commit 的 Apache-2.0 许可](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/LICENSE.md)
- [固定 commit 的第三方资产排除说明](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/pyproject.toml)
- [MaskedMimic 论文主来源](https://arxiv.org/abs/2409.14393)
- [CALM 论文主来源](https://arxiv.org/abs/2305.02195)
