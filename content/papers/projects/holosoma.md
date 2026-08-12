# HoloSoma：人形强化学习的多后端训练框架

[English version](en/holosoma.md)

审阅快照：[amazon-far/holosoma@`6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3`](https://github.com/amazon-far/holosoma/tree/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3) · 1582 stars（2026-08-12 快照）· Apache-2.0。star 只用于发现高信号仓库，不是技术正确性、真机成功率或安全信心。

## 为什么收录

HoloSoma 把 locomotion（行走）、whole-body tracking（全身跟踪）、PPO、FastSAC、多仿真后端与推理部署放在同一工程边界中。它是《Learning Sim-to-Real Humanoid Locomotion in 15 Minutes》当前配方的官方实现，也承载 OmniRetarget 等相关工作，所以项目页关心“代码现在怎么组织”，而论文页另行限定实验结论。

本页直接审阅固定 commit 中的 core training tree。仓库 README 声明支持 Isaac Gym、Isaac Sim、MJWarp 和 MuJoCo，但“同一仓库有多后端”不代表数值语义完全等价，也不代表一个 checkpoint 可无验证跨后端和真机使用。

## 它解决什么问题

人形 RL 常被分散的环境封装、奖励、课程、终止、replay buffer 和推理接口卡住。实验结果可能看似是算法差异，实际来自 action scaling、observation order、随机化或 done mask 不一致。HoloSoma 通过配置值、manager 和 agent 层把这些契约显式化。

FastSAC 路线又解决一个更窄的问题：如何在大量并行环境中保留 off-policy（离策略）的样本复用，同时不让 replay 更新成为墙钟时间瓶颈。这是“15 分钟”工程数字背后的主路径，但该数字只能按论文的单卡 locomotion 设置理解。

## 架构与数据流

主链可写成 `task config → simulator/vectorized env → observation/action contract → replay buffer → FastSAC updates → policy checkpoint`。`config_values/loco/g1/` 定义 G1 的 action、command、observation、reward、randomization、curriculum 和 termination；manager 层把各 term 组合为环境时序。

agent 从并行 rollout 收集 transition，放入 replay，再进行 critic、distributional target、actor 和 entropy-temperature 更新。这条链上任一 shape、尺度或 terminal flag 错位都可以让训练“运行但学错”，因此比较 PPO/FastSAC 前应先比对环境契约。

## 代码定位

- [`FastSACAgent`](https://github.com/amazon-far/holosoma/blob/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3/src/holosoma/holosoma/agents/fast_sac/fast_sac_agent.py) 是核心训练状态机；`_update_main`、`_update_pol` 和 `learn` 分别负责 value/distributional target、policy/temperature 与总体迭代。
- [G1 locomotion reward 配置](https://github.com/amazon-far/holosoma/blob/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3/src/holosoma/holosoma/config_values/loco/g1/reward.py) 是查找奖励权重和 term 绑定的首要入口。
- [locomotion reward terms](https://github.com/amazon-far/holosoma/blob/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3/src/holosoma/holosoma/managers/reward/terms/locomotion.py) 提供奖励实际计算，可用来核对坐标系、求和维度与指数尺度。
- [`CurriculumManager`](https://github.com/amazon-far/holosoma/blob/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3/src/holosoma/holosoma/managers/curriculum/manager.py) 和 [termination manager](https://github.com/amazon-far/holosoma/blob/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3/src/holosoma/holosoma/managers/termination/manager.py) 决定难度如何变化以及哪些状态真正结束 episode。

## 最小复现路径

不要先追求真机。固定 commit、Python/CUDA/仿真器版本、G1 资产和一个 seed，使用少量环境跑通 README 中的 FastSAC G1 locomotion 命令。先保存 observation 名称与 shape、action 限幅、reward 分项、termination 原因、replay 大小和 update-to-data ratio。

第二步才将环境数扩大，报告多 seed 的 wall-clock、sample count、return、跟踪误差、足端滑移、动作饱和与终止分布。若比较 PPO，必须固定任务契约和总环境交互量，同时分开报告样本效率和墙钟效率。

## 能力边界

仓库是研究框架，不是已完成功能安全认证的机器人产品。它支持多后端，但 contact、solver、latency 和 sensor noise 的差异仍需独立验收。它有 sim-to-real 管线，但不能由此推导默认配置对任何 G1/T1 均安全。

该 commit 的官方 README 同时覆盖训练、重定向与部署概览；本页只对直接审阅的 core training 代码做细粒度映射。其他组件的“存在”不等于已对所有路径做本页级别的复现核验。

## 工程判断与风险

最值得复用的是把 reward、curriculum 和 termination 变成可审计 manager 的设计；最容易误用的是只复制训练命令而忽略版本、资产与本体标定。训练成功的 checkpoint 必须先通过独立 sim2sim、延迟/丢包注入、观测顺序单元测试与限幅检查。

真机上机需要厂商限位、力矩/速度饱和、姿态与接触保护、通信超时、物理急停、支撑/吊装和分级放宽。不应因为论文有真机视频或 star 较高就跳过本机安全案。

所有异常都应记录具体配置与终止原因，便于追溯和回归。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/amazon-far/holosoma/tree/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3)
- [训练命令与支持范围](https://github.com/amazon-far/holosoma/blob/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3/README.md)
- [对应论文的中文深读](../fast-humanoid-locomotion-2512.01996.md)
