# humanoid-control：OCS2 NMPC、状态估计与加权/分层 WBC 的完整接口

[English version](en/humanoid-control.md)

审阅快照：[pocketxjl/humanoid-control@`3b5ffec98d29827730194b0dbf2f119fb7b265ca`](https://github.com/pocketxjl/humanoid-control/tree/3b5ffec98d29827730194b0dbf2f119fb7b265ca) · 412 stars（2026-08-12 快照）· MIT。star 是发现门槛，不是正确性或硬件安全等级；项目借鉴 OCS2/legged-control，但没有一篇论文覆盖本仓库全部实现。

## 为什么收录

该仓库把 NMPC、MRT、状态估计、步态切换、加权/层级 WBC、PD 输出和 MuJoCo/ROS 控制节点连接起来，并在 README 中公开状态、输入、QP 变量和运行频率。它是现有 loco-manipulation WBC 与 locomotion topic 中少见的可读模型式整链项目。

收录不代表实现已达到工业实时性或实机验证。仓库展示主要是 MuJoCo，README 还提醒必须至少用 `RelWithDebInfo` 构建以满足速度。它适合追踪 OCS2 NMPC 参考如何进入 500 Hz WBC，而不是直接复制参数到新机器人。

## 它解决什么问题

双足需要规划接触力和质心运动，同时满足浮动基动力学、摩擦锥、支撑足不动、摆动足轨迹和力矩限制。OCS2 的 SQP NMPC 负责有限时域，WBC 在当前时刻将优化状态/输入转换为关节加速度、接触力和力矩。线性 Kalman filter 用支撑足运动学约束估计躯干位置与速度。

这种层次把慢规划与快执行分开，但要求 NMPC 的质心模型、MRT 插值、WBC 任务和 PD 目标使用一致的广义坐标。支撑足判错或状态估计漂移会同时污染规划初值和 WBC 约束；简单调大 WBC 权重不能修复上游状态错误。

## 架构与数据流

路径为 `MuJoCo/ROS sensors → StateEstimateBase → OCS2 HumanoidInterface/SQP MPC → MRT policy interpolation → WeightedWbc 或 HierarchicalWbc → desired q/v/torque → PD/controller`。步态调度切换左右脚接触，摆动足 z 轨迹使用三次样条，MPC 以质心动量、基座和关节状态作为状态，以接触力和关节速度作为输入。

WBC QP 的变量包括基座/关节加速度、四个接触点力与关节力矩。浮动基动力学、力矩限位与摩擦锥作为约束，基座、摆动脚与期望接触力作为 cost。仓库同时提供 weighted 与 hierarchical 两种实现，适合检查软权重冲突与严格优先级的差异。

## 代码定位

- [`HumanoidSqpMpcNode.cpp`](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/humanoid_dummy/src/HumanoidSqpMpcNode.cpp) 启动 OCS2 SQP MPC，是规划侧最小独立入口。
- [`HumanoidInterface`](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/humanoid_interface/src/HumanoidInterface.cpp) 组装模型、代价、约束、初值和 MPC 设置。
- [`WeightedWbc`](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/humanoid_wbc/src/WeightedWbc.cpp) 将任务矩阵变成一个加权 QP。
- [`HierarchicalWbc`](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/humanoid_wbc/src/HierarchicalWbc.cpp) 实现逐层优先级求解，可与 weighted 路线对照。
- [`StateEstimateBase`](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/humanoid_estimation/src/StateEstimateBase.cpp) 负责支撑足相关状态更新。

## 最小复现路径

按 README 只构建 OCS2 的必要包，固定 OCS2、Pinocchio、hpp-fcl、qpOASES、ROS 与本仓库 commit，并使用 `RelWithDebInfo`。先启动 OCS2 dummy node 验证 NMPC 独立求解，再运行 cheat estimator 控制器，最后切换正常状态估计器；这样可把规划/WBC 问题与估计问题分开。

记录 NMPC 100 Hz、MRT/WBC/估计 500 Hz 和 PD >1 kHz 是否实际满足；保存每周期求解状态、迭代和耗时、QP 约束残差、摩擦裕量、接触力、关节力矩、估计协方差、脚滑与终止原因。对 weighted/hierarchical 使用同一参考与初态比较，而不是同时换权重、步态和模型。

## 能力边界

当前模型自由度、四个足底接触点与 cost/constraint 选择都是具体设计，不是所有 humanoid 的默认答案。线性估计器信任支撑足，遇脚滑、软地面或错误接触状态时会偏置。README 公式与代码需要以固定 commit 互相核对，不能只按说明推断运行语义。

仓库没有给出广泛真机统计、复杂地形、手臂操作或碰撞避障结果。MuJoCo 成功不证明传感器噪声、执行器带宽、总线延迟和结构柔顺条件下稳定。外部 OCS2 大型依赖也增加版本漂移与构建风险。

## 工程判断与风险

项目最适合教育与可审计基线：它把 NMPC 状态/输入和 WBC QP 变量写得清楚，并允许隔离估计器。长期使用应增加实时监控、求解器降级、接触异常检测、reference freshness、配置 manifest 与自动回归。QP 不可行时必须有明确安全动作，而不是继续使用陈旧输出。

真机需要机器人专用质量/惯量、接触几何、执行器和传感器标定；严格限制位置、速度、力矩和接触冲击，并在支撑/吊装、低增益、低速、急停条件下逐层启动。正常 estimator 必须先在回放中通过。本页不提供任何可直接上机参数。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/pocketxjl/humanoid-control/tree/3b5ffec98d29827730194b0dbf2f119fb7b265ca)
- [主控制器实现](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/humanoid_controllers/src/humanoidController.cpp)
- [MIT 许可证](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/LICENSE)
