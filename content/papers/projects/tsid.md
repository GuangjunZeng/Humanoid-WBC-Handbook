# TSID：基于 Pinocchio 的任务空间逆动力学库

[English version](en/tsid.md)

审阅快照：[stack-of-tasks/tsid@`eae96180ed8d289bc2c634f9d0857020ebfa6d90`](https://github.com/stack-of-tasks/tsid/tree/eae96180ed8d289bc2c634f9d0857020ebfa6d90) · 345 stars（2026-08-12 快照）· BSD-2-Clause。star 是发现信号，不是求解正确、实时性或真机安全的证明。

## 为什么收录

TSID（Task Space Inverse Dynamics，任务空间逆动力学）是优化式 Whole-Body Control（WBC，全身控制）的直接开源锚点。它不是只给一个 QP 公式，而是把机器人模型、运动任务、刚性接触、力与执行器边界、层级 QP（HQP）及 Python bindings 连成可调试库。

仓库同时提供 manipulator、humanoid 和 quadruped 练习。它适合回答“任务和接触到底怎么进入求解器”，但不应与完整机器人控制栈混为一谈。状态估计、接触切换计划、执行器辨识、硬件 I/O 和安全监控仍由集成方负责。

## 它解决什么问题

多接触人形控制需要同时处理刚体动力学、支撑力、质心/末端/姿态任务、关节与力矩边界。若每个研究项目都重写 Jacobian、约束拼接和 solver adapter，错误往往隐藏在维度、坐标系或优先级中。

TSID 用 `TaskMotion`、`ContactBase`、`Constraint*` 和 `SolverHQP*` 把这些概念变成类型化对象。用户给出 q/v 和任务参考，formulation 生成层级 QP 数据，solver 返回加速度、接触力和执行器量。这提高了可复用性，但不会自动保证任务集可行。

## 架构与数据流

典型数据流为 `URDF/Pinocchio model + q,v → task/contact compute → InverseDynamicsFormulationAccForce::computeProblemData → HQPData → SolverHQP::solve → accelerations/contact forces/torques`。运动任务可以是 SE(3) 末端、CoM、角动量或关节姿态；不等式负责关节、速度、加速度或执行器边界。

`priorityLevel` 决定任务放入哪一层，weight 只在层内表示折中。这个区别很重要：把安全约束当作低权重 soft task，与把它放到高优先级 inequality，会得到完全不同的失效方式。

## 代码定位

- [`InverseDynamicsFormulationAccForce::computeProblemData`](https://github.com/stack-of-tasks/tsid/blob/eae96180ed8d289bc2c634f9d0857020ebfa6d90/src/formulations/inverse-dynamics-formulation-acc-force.cpp) 更新 Pinocchio 数据，计算任务/接触并组装 HQP；同文件的 `addMotionTask` 和 `addRigidContact` 管理层级条目。
- [`TaskSE3Equality::compute`](https://github.com/stack-of-tasks/tsid/blob/eae96180ed8d289bc2c634f9d0857020ebfa6d90/src/tasks/task-se3-equality.cpp) 把当前与参考 SE(3) 状态转成六维运动约束。
- [`TaskActuationBounds::compute`](https://github.com/stack-of-tasks/tsid/blob/eae96180ed8d289bc2c634f9d0857020ebfa6d90/src/tasks/task-actuation-bounds.cpp) 生成执行器上下界，但边界数值仍必须由机器人专属配置给出。
- [`tsid_biped.py`](https://github.com/stack-of-tasks/tsid/blob/eae96180ed8d289bc2c634f9d0857020ebfa6d90/exercizes/tsid_biped.py) 展示双足接触、CoM、角动量、姿态、足端与关节边界如何被组装。

## 最小复现路径

首先用 Conda 或 robotpkg 安装固定版本的 TSID、Pinocchio 与 solver dependency，在无硬件的 Python manipulator 练习中验证 q/v 维度、task reference、HQP status 和 integration。随后跑 biped balance 示例，每帧记录 solver status、任务残差、约束违反、接触力与求解时间分布。

最小消融是依次加入 posture、SE(3)、CoM、contact 和 actuation bounds，检查哪一项导致不可行或数值恶化。还要人为构造冲突任务，确认系统显式报错或进入设计好的降级，而不是返回一个未检查的控制量。

## 能力边界

TSID 是逆动力学 formulation 与 solver 库，不是 walking MPC、state estimator、contact planner 或 robot driver。它能表达接触和力边界，但 friction coefficient、support polygon、力矩限制和模型参数不会自动正确。

配套论文的“without joint-torque sensors”不能反向读成 TSID 不需任何力感知。该论文的 HRP-2 实验仍使用腕/踝六维力传感器、IMU 和编码器；本仓库也不是那套执行器辨识的完整打包复现。

## 工程判断与风险

最值得复用的是 task/contact/constraint 契约和多 solver adapter；最危险的是只看 solver 返回 `optimal` 就认为输出物理可实现。模型误差、接触切换、秩损失、尺度病态与积分漂移都需在上层监测。

真机必须有硬限位、力矩/功率/速度限制、接触力监测、求解超时与 infeasible 降级、状态估计健康检查和物理急停。在仿真中做冲突注入和超时测试后，再用支撑或吊装进行低速低力分级验证。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/stack-of-tasks/tsid/tree/eae96180ed8d289bc2c634f9d0857020ebfa6d90)
- [官方安装和示例说明](https://github.com/stack-of-tasks/tsid/blob/eae96180ed8d289bc2c634f9d0857020ebfa6d90/README.md)
- [对应论文的中文深读](../torque-control-high-ratio-gearboxes-2016.md)
