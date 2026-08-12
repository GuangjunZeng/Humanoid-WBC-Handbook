# trackerLab：把重定向、跟踪、技能图和部署接口放到同一工程

[English version](en/trackerlab.md)

审阅快照：[Renforce-Dynamics/trackerLab@`1e5ccc062b445712a0aa7308cfb99edd7296cc88`](https://github.com/Renforce-Dynamics/trackerLab/tree/1e5ccc062b445712a0aa7308cfb99edd7296cc88) · 243 stars（2026-08-12 快照）· MIT。star 是发现门槛，不是技术置信度；仓库首页也明确警告项目已大幅重构而教程尚未同步。

## 为什么收录

trackerLab 没有一篇直接对应论文，却试图把 SMPL/FBX/AMASS 数据重定向、Isaac Lab 轨迹跟踪、有限状态机（finite-state machine, FSM）技能组合与部署侧动作管理连接起来。它不像单一算法仓库，而更像跨本体 tracker 的实验台，因此同时归入训练数据与通用跟踪 topic。

收录的关键不是“功能多”，而是仓库保留了配置、数据流文档和源码边界，允许读者检查关节映射、动作格式、技能切换与部署插值。与此同时，重构提示意味着 README 命令与当前实现不能默认一致；本页固定 commit 并把这种维护风险写进结论。

## 它解决什么问题

动作跟踪工程常由多个不兼容仓库拼接：一个脚本做人到机器人重定向，另一个任务训练策略，第三套代码做 sim2sim，真机侧再手写状态机。坐标、关节顺序、采样率和命令语义很容易在边界丢失。trackerLab 的目标是使用 manager-based 抽象统一这些接口，并用 YAML/JSON 配置适配 G1、H1 和其他本体。

这并不自动消除误差。相反，统一框架的价值在于把误差定位到数据、任务、策略或部署层。若同一 NPZ 在数据查看器正常、在 Isaac Lab 跟踪失败，就应检查奖励与 observation；若仿真正常而部署异常，则应检查关节映射、插值、控制周期和执行器语义。

## 架构与数据流

仓库的实际路径可概括为 `人体动作 → poselib 重定向/对齐 → NPZ 数据与配置 → trackerTask/Isaac Lab 任务 → RSL-RL 训练 → policy/checkpoint → deploylib/sim2simlib → FSM 技能组合`。`source/poselib` 管骨架与重定向，`source/trackerTask` 管任务，`source/deploylib` 管运行时动作状态与插值，脚本目录提供训练、评估和数据查看入口。

技能层不是让一个策略凭空掌握所有行为，而是把动作 ID、状态和切换逻辑放入 `DeployManager`。重定向配置则明确人体/机器人 T-pose、骨架和映射。两个层次都很重要：前者控制何时执行，后者决定参考是什么；把它们混为“通用 WBC”会夸大项目能力。

## 代码定位

- [`RetargetingProcessor`](https://github.com/Renforce-Dynamics/trackerLab/blob/1e5ccc062b445712a0aa7308cfb99edd7296cc88/source/poselib/poselib/retarget/retargeting_processor.py) 负责 T-pose、基础重定向和动作调整，是人体数据进入机器人轨迹的核心边界。
- [`DeployManager.step`](https://github.com/Renforce-Dynamics/trackerLab/blob/1e5ccc062b445712a0aa7308cfb99edd7296cc88/source/deploylib/deploylib/deploy_manager/deploy_manager.py) 管理动作状态、FSM 运动 ID、插值和逐周期输出。
- [`GMR_to_npz.py`](https://github.com/Renforce-Dynamics/trackerLab/blob/1e5ccc062b445712a0aa7308cfb99edd7296cc88/source/deploylib/scripts/data_fk/GMR_to_npz.py) 把外部重定向结果通过机器人前向运动学整理成训练数据。
- [`data_flow.md`](https://github.com/Renforce-Dynamics/trackerLab/blob/1e5ccc062b445712a0aa7308cfb99edd7296cc88/docs/data_flow.md) 是理解目录间接口的官方一手文档，但需结合重构警告核对源码。

## 最小复现路径

不要从真机开始。固定 commit 与 Isaac Lab 版本，先下载明确版本的资产，在数据查看器中加载一条短动作并确认 T-pose、关节名、FPS 与脚底高度。然后只运行一个已注册的跟踪任务，固定随机种子、环境数、配置和 checkpoint；训练后在 Isaac Lab play 中复现，再进入 MuJoCo sim2sim。

验收报告应记录每个边界的张量形状和关节顺序、策略 observation/action 维度、训练和推理控制周期、动作切换前后误差，以及 sim2sim 中根高度、姿态、脚滑和失败率。README 中“无需额外仓库”的说法与资产库、robotlib 等当前依赖需要按实际 commit 复核。

## 能力边界

项目声称支持多种控制模式和本体，但审阅 commit 的示例、配置完整度与教程同步程度并不一致。某个 JSON 文件存在不等于对应机器人已经训练和部署验证；某个视频也不能证明整个技能图的切换稳定性。页面不把演示扩展为通用性能结论。

框架包含第三方和复制模块，许可证、版本与修补必须逐目录审查。大规模重构而文档滞后会使命令、路径或配置失效；因此这里固定的代码定位比主分支 README 更可靠，但也只对该 commit 有效。

## 工程判断与风险

trackerLab 的差异化价值是“接口对齐实验台”，不是提出已验证的新控制算法。适合用来做跨本体数据格式和部署链对照，也适合把跟踪失败按层定位。要用于长期基线，项目仍需要版本化任务清单、最小 CI、配置—checkpoint 对应表和可复核评测。

实机使用前必须在独立仿真完成策略输出限幅、关节映射、控制周期、初始姿态和状态切换测试；使用吊装、急停、低增益与小动作幅度逐步放开。技能图切换可能产生不连续参考，必须有过渡和超时保护。本页不提供安全参数或部署授权。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/Renforce-Dynamics/trackerLab/tree/1e5ccc062b445712a0aa7308cfb99edd7296cc88)
- [项目结构文档](https://github.com/Renforce-Dynamics/trackerLab/blob/1e5ccc062b445712a0aa7308cfb99edd7296cc88/docs/project_structure.md)
- [问题记录](https://github.com/Renforce-Dynamics/trackerLab/blob/1e5ccc062b445712a0aa7308cfb99edd7296cc88/docs/problems.md)
