# OpenLoong Dynamics Control：可读的 MPC + 优先级 WBC 人形控制链

[English version](en/openloong-dyn-control.md)

审阅快照：[loongOpen/OpenLoong-Dyn-Control@`4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e`](https://github.com/loongOpen/OpenLoong-Dyn-Control/tree/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e) · 350 stars（2026-08-12 快照）· Apache-2.0。star 仅用于发现，不是控制正确性或真机安全置信度；仓库以软件引用为主，没有一篇完全对应全部实现的论文。

## 为什么收录

OpenLoong 公开了一条经典模型式人形控制链：状态估计（state estimation）、步态调度（gait scheduling）、足步规划（foot placement）、模型预测控制（model predictive control, MPC）、优先级全身控制（priority-based whole-body control, WBC）和关节命令。相较黑盒策略仓库，它便于读者从数据总线追踪期望量、约束和输出。

它同时归入 locomotion 与 loco-manipulation WBC 两个既有 topic。收录重点是模型式 WBC 的可读工程锚点，而不是宣称当前实现是最先进方案。官方 README 说明 Qinglong 真机实现了行走和盲踩障碍，但公开仓库主要复现路径仍是 MuJoCo。

## 它解决什么问题

动态行走需要低频规划未来接触与力、高频满足全身动力学和任务优先级，并用更高频关节伺服落实命令。若把所有层塞进一个 QP，时域规划与瞬时约束会混杂；若完全分开，又可能出现 MPC 期望力与 WBC 可实现力不一致。OpenLoong 用 DataBus 连接各模块，明确读—算—写顺序。

MPC 根据简化质心模型生成期望状态和接触力；WBC 在当前时刻按任务优先级求广义加速度与力矩；足步、步态和状态估计提供相位与反馈。这样的分层允许逐模块调试，同时引入跨频率、坐标系和状态延迟问题。

## 架构与数据流

主循环是 `MuJoCo sensors → StateEst/PinoKinDyn → GaitScheduler + FootPlacement → MPC → WBC_priority → joint PVT command → MuJoCo`。`walk_mpc_wbc.cpp` 组织不同频率模块，DataBus 承载根状态、足端、期望轨迹、接触状态与控制输出。README 给出的典型频率是 MPC 100 Hz、MRT/WBC/估计 500 Hz、PD 超过 1 kHz。

WBC 使用分层任务和 QP，README 示例将冗余关节、静态接触、躯干姿态/高度、水平位置、摆动腿和手部跟踪排序。优先级顺序改变会重分配可行空间；它不是装饰性配置。MPC、WBC、关节伺服之间还必须使用一致的接触与符号约定。

## 代码定位

- [`demo/walk_mpc_wbc.cpp`](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/demo/walk_mpc_wbc.cpp) 展示状态估计、步态、MPC、WBC 与关节命令怎样在主循环按频率连接。
- [`MPC`](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/algorithm/mpc.cpp) 构造滚动时域优化并输出接触相关控制量。
- [`WBC_priority`](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/algorithm/wbc_priority.cpp) 实现任务优先级与全身动力学求解。
- [`PriorityTasks`](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/algorithm/priority_tasks.cpp) 是检查每层任务矩阵、PD 目标与堆叠方式的位置。
- [`StateEst`](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/algorithm/StateEst.cpp) 处理基座状态反馈，是控制链能否闭环的前提。

## 最小复现路径

固定 Ubuntu/compiler、仓库 commit 与捆绑依赖版本，先构建并运行 `walk_wbc`，再运行 `walk_mpc_wbc`。保存机器人模型、关节控制 JSON、MPC 权重、WBC 任务顺序、步态周期和仿真时间步。用同一初始状态分别运行至少十次，记录是否确定性一致。

验收不以“走起来”为终点：记录 MPC/WBC 求解时间和状态、QP 不可行次数、接触力与摩擦锥裕量、足底滑移、质心/躯干误差、关节力矩/速度饱和与模块 deadline miss。再用 README changelog 中曾修复的传感器 ID、MPC 矩阵维度和优先级计算问题构造回归测试。

## 能力边界

公开示例围绕 Qinglong 模型、平地/盲踩障碍与跳跃，不等于通用双足或移动操作系统。捆绑的 MuJoCo、Pinocchio 等依赖可能与上游版本不同；模型替换教程能指导迁移，但不能自动生成正确惯量、接触点、任务维度和增益。

README 的真机陈述是项目方报告，没有公开统一的失败率、扰动范围或硬件日志。状态估计、接触切换和被动踝等条件对稳定性敏感。仿真默认参数也不能直接迁移到电机、减速器与柔顺结构不同的机器人。

## 工程判断与风险

项目最有价值的是模块可读与经典 WBC 调试入口，尤其适合学习“规划参考如何进入瞬时 QP”。生产使用应加入求解器状态监控、不可行降级、接触一致性检查、实时 deadline、单元/维度断言和参数 manifest。历史 bug 已说明矩阵维度与传感器索引足以改变行为。

真机部署需要机器人专用动力学与执行器标定、严格的力矩/速度/位置限制、状态估计验证、接触检测、支撑或吊装、低速低增益 commissioning 与物理急停。QP 有解也不表示动作安全；本页不提供直接上机参数。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/loongOpen/OpenLoong-Dyn-Control/tree/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e)
- [模型替换教程](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/Tutorial.md)
- [Apache-2.0 许可证](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/LICENSE)
