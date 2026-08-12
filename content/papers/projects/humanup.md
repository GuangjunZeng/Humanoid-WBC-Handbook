# HumanUP：“先发现、再追踪”的人形起身训练工程

[English version](en/humanup.md)

审阅快照：[RunpeiDong/HumanUP@`7516e0f27e6f4d1e7365cf64ea577a78247bd8cb`](https://github.com/RunpeiDong/HumanUP/tree/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb) · 231 stars（2026-08-12 快照）· Apache-2.0。star 只是发现高信号仓库的索引，不是起身成功率、跌倒伤害或真机安全等级。

## 为什么收录

HumanUP 是起身恢复领域中少有的完整工程链：Stage I discovery policy（发现策略）允许策略在简化碰撞和较弱正则下找到快速起身轨迹，Stage II tracking policy（跟踪策略）再用关节、能量、动作变化和接触相关约束学习更可部署的行为。

项目页关心代码中两阶段如何交接、课程怎样改变任务分布，以及哪些惩罚只是训练代理指标。论文的实验结论和图表边界由独立深读页负责，不因仓库高 star 或演示视频而扩大。

## 它解决什么问题

直接用密集动作惩罚训练起身，往往会限制探索；只优化站起高度，又可能学到冲击大、关节极限多或依赖特定初始姿态的捷径。HumanUP 把“找到任务可行轨迹”和“把轨迹变成可控跟踪行为”分开，降低这两个目标在同一奖励中互相拉扯的风险。

但是“可跟踪”不等于“任意跌倒后安全恢复”。起身还受地面材料、机器人碰撞几何、电机温度、电池状态、外部负载和跌倒姿态影响。项目代码提供研究基线，没有替用硬件故障诊断和功能安全控制层。

## 架构与数据流

主链是 `fixed supine/prone initialization → discovery rollout → standing/regularization curricula → discovered reference trajectory → interpolation → tracking policy → bounded joint targets`。俯卧和仰卧由不同策略或中间轨迹处理，不应将单一初始姿态的结果当作全姿态恢复能力。

discovery 环境根据起身进度改变站立采样概率和正则强度；tracking 环境读入发现轨迹并插值，同时优化关节误差、基座姿态、力矩、加速度、动作变化和关节边界。复现时必须记录“参考轨迹版本”，否则 Stage II 成绩无法与 Stage I 来源对齐。

## 代码定位

- [`G1WaistRollHumanUP`](https://github.com/RunpeiDong/HumanUP/blob/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb/simulation/legged_gym/legged_gym/envs/g1waistroll/g1waistroll_up.py) 实现 discovery 环境，其 `_update_standing_prob_curriculum`、`_update_regularization_scale_curriculum` 和 `_reward_*` 定义任务/正则课程。
- [`G1WaistRollHumanUPCfg`](https://github.com/RunpeiDong/HumanUP/blob/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb/simulation/legged_gym/legged_gym/envs/g1waistroll/g1waistroll_up_config.py) 固定观测、动作、奖励尺度、随机化和 PPO 超参数的实验契约。
- [`G1WaistRollTrack`](https://github.com/RunpeiDong/HumanUP/blob/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb/simulation/legged_gym/legged_gym/envs/g1rolltrack/g1waistroll_track.py) 加载/插值发现轨迹，并实现 `_reward_tracking_dof_error`、基座姿态与力矩/能量/边界正则。
- [`G1WaistRollTrackCfg`](https://github.com/RunpeiDong/HumanUP/blob/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb/simulation/legged_gym/legged_gym/envs/g1rolltrack/g1waistroll_track_config.py) 是比较 Stage I 与 Stage II 环境差异的入口。

## 最小复现路径

固定 commit、Isaac Gym/CUDA、G1 URDF 与碰撞体、初始姿态集、terrain、randomization 和 seed。先使用少量并行环境训练仰卧 discovery，逐 episode 保存根高度、姿态、接触、最大力矩、站立概率、正则尺度与终止原因。用多 seed 确认不是单条偶然轨迹。

再将固定 discovery 轨迹交给 tracking，对比单阶段、无 Stage II、简化碰撞、无 posture randomization 和 hard symmetry。报告成功率时同时报告姿态覆盖、时间、峰值力矩/功率、接触冲击、脚/膝滑动和失败分类。

## 能力边界

论文与代码支持特定 G1 模型和姿态分布下的起身研究，不支持“任意跌倒、任意地面、任意负载都能恢复”。奖励中的力矩、关节限位和能量惩罚是软约束，不等于执行器硬限幅或保护回路。

公开仓库主要是训练与仿真工程。即使策略在仿真中不终止，也可能在真机上出现电流过限、过热、重复冲击损伤或通信中断。这些风险必须由独立监控层处理。

## 工程判断与风险

最值得复用的是“先放松探索，再带约束跟踪”的分阶段设计；最容易误用的是把 tracking reward 中的惩罚当作安全证明。应建立轨迹、配置和 checkpoint 三者一起版本化的验收表，任何一者改变都重跑整套门禁。

真机必须先做无动力碰撞检查和低力矩支撑/吊装测试，再逐步增加动作速度与初始姿态。需要独立急停、电流/温度与姿态超限、软性落地区、禁入区和专职安全员；策略超时或状态不可信时必须进入明确的保护动作。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/RunpeiDong/HumanUP/tree/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb)
- [官方训练与部署说明](https://github.com/RunpeiDong/HumanUP/blob/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb/README.md)
- [对应论文的中文深读](../humanup-2502.12152.md)
