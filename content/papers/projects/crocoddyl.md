# Crocoddyl：多接触机器人最优控制与 FDDP 工程库

[English version](en/crocoddyl.md)

审阅快照：[loco-3d/crocoddyl@`46974c3c49ed956e41f8f95a329cf8537af7550b`](https://github.com/loco-3d/crocoddyl/tree/46974c3c49ed956e41f8f95a329cf8537af7550b) · 1274 stars（2026-08-12 快照）· BSD-3-Clause。star 代表项目的影响力与发现价值，不是优化收敛、实时 deadline 或真机安全的担保。

## 为什么收录

Crocoddyl 是多接触 optimal control（最优控制）与 Differential Dynamic Programming（DDP，差分动态规划）的主流开源实现。它基于 Pinocchio 的刚体动力学与解析导数，将流形状态、action model、cost、contact/impulse 和 shooting solver 组成可扩展库。

对 WBC 读者而言，Crocoddyl 不是替代低层全身控制器的单一模块，而是生成多接触轨迹、做 MPC 滚动优化或检查 warm start 的工具。项目页重点是现代库的模型—导数—求解契约，论文页另行限定 2019 FDDP 实验。

## 它解决什么问题

传统 shooting DDP 需要从完全动力学可行的状态—控制轨迹开始。对跳跃、走路和接触切换，初值往往有 dynamics gaps（动力学缺陷）；先强制闭合可能让 rollout 进入差的 basin。

FDDP 在 forward pass 中显式保留和收缩 gaps，并在 expected improvement 中计入它们，使差 warm start 也能逐步趋于可行。Crocoddyl 把这套 solver 与 contact forward dynamics、impulse action、已知接触序列和自定义 cost 结合，降低重复实现导数的风险。

## 架构与数据流

主路径为 `state/action/contact models + costs → ShootingProblem → calc/calcDiff → SolverFDDP backward pass → gap-aware forward rollout → line-search acceptance → optimized state/control trajectory`。动作模型必须同时提供动力学/代价和导数，否则 solver 性能与收敛解释都不可靠。

接触 gait 示例会预先给定支撑序列，并在切换点使用 impulse model。这是“已知接触模式下优化轨迹”，不是自动发现脚步或不确定接触计划。

## 代码定位

- [`SolverFDDP`](https://github.com/loco-3d/crocoddyl/blob/46974c3c49ed956e41f8f95a329cf8537af7550b/include/crocoddyl/core/solvers/fddp.hxx) 的 `computeDirection`、`backwardPass`、`forwardPass` 和 `expectedImprovement` 实现 gap-aware 方向、rollout 和接受准则。
- [`contact-fwddyn.hxx`](https://github.com/loco-3d/crocoddyl/blob/46974c3c49ed956e41f8f95a329cf8537af7550b/include/crocoddyl/multibody/actions/contact-fwddyn.hxx) 实现多体接触前向动力学和导数契约。
- [`biped_gaits_fwddyn.py`](https://github.com/loco-3d/crocoddyl/blob/46974c3c49ed956e41f8f95a329cf8537af7550b/examples/biped_gaits_fwddyn.py) 展示双足 contact/impulse action models、足步 cost 和 shooting problem 的组装。
- [`shooting.cpp`](https://github.com/loco-3d/crocoddyl/blob/46974c3c49ed956e41f8f95a329cf8537af7550b/bindings/python/crocoddyl/core/shooting.cpp) 的 Python binding 层体现 problem 对象与 calc/calcDiff 的公开契约。

## 最小复现路径

锁定 commit、Pinocchio、编译器、BLAS、线程数、CPU 和机器人模型。先跑一个短时域无接触问题，用有限差分或现有测试验证 `calcDiff`。然后跑 biped gait，每迭代保存 cost、gap norm、step length、regularization、接受状态和 wall time。

使用三组 warm start：准静态插值、错误落脚和明显速度不连续。固定接触序列与 cost，比较 DDP/FDDP 的收敛率、最终 cost、最大 gap 和尾延迟。再增加摩擦、力矩、关节与自碰撞检查，而不只复制无约束吞吐。

## 能力边界

原 FDDP 论文的主要实验为研究 solver 忽略摩擦锥和 torque limits。当前 Crocoddyl 库有更广泛的 model/cost/solver 能力，但不能用当前 API 的存在回写原论文已做真机安全验证。

求解器通常需要用户提供接触序列、cost 和初值。收敛到低 cost 不代表轨迹不滑脚、不自碰撞、满足执行器限制或对模型误差鲁棒，这些都需显式建模与验收。

库的可扩展性也带来对照风险：两个实验即使都调用 `SolverFDDP`，也可能使用不同状态流形、积分方式、正则化、接触刚度或停止准则。所以性能比较必须同时固定 problem construction 和 solver options，不能只报一个类名。

## 工程判断与风险

最值得复用的是清晰的 action-model 导数契约与 gap-aware shooting；最大风险是将“毫秒级迭代”当作硬实时保证。应报告端到端求解时间分布和最坏 deadline miss，并对导数错误、秩损失和病态做故障注入。

对 MPC 还应将建模、导数、后向遍历、前向线搜索和消息传输分别计时，记录 P50/P95/P99 和超时时的备用动作。平均时间足够快，不能替代对最坏周期和降级路径的验证。

在真机 MPC/WBC 中使用时，需要最大迭代/时间预算、不可行与超时降级、上一轨迹健康检查、独立反馈控制器和急停。离线轨迹也必须通过摩擦、力矩、速度、冲击和自碰撞门禁。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/loco-3d/crocoddyl/tree/46974c3c49ed956e41f8f95a329cf8537af7550b)
- [FDDP 核心实现](https://github.com/loco-3d/crocoddyl/blob/46974c3c49ed956e41f8f95a329cf8537af7550b/include/crocoddyl/core/solvers/fddp.hxx)
- [对应论文的中文深读](../crocoddyl-1909.04947.md)
