# KungFuAthleteBot：高动态武术数据、跟踪与跌倒恢复的公开链路

[English version](en/kungfu-athlete-bot.md)

审阅快照：[NPCLEI/KungFuAthleteBot@`1e3f207013245a5a0db75e6f70e1cdf762e28e9c`](https://github.com/NPCLEI/KungFuAthleteBot/tree/1e3f207013245a5a0db75e6f70e1cdf762e28e9c) · 259 stars（2026-08-12 快照）· MIT。对应论文：[A Kung Fu Athlete Bot That Can Do It All Day, arXiv:2602.13656v1](https://arxiv.org/abs/2602.13656v1)。star 只用于发现，不是数据质量、控制可信度或硬件安全等级。

## 为什么收录

候选初筛把仓库列为无论文项目，但官方首页与 arXiv 已给出论文，因此修正为官方论文代码。它在体育、恢复安全和训练数据三个既有 topic 之间形成少见的完整链路：职业运动视频、GVHMR 人体运动恢复、GMR 重定向、人工筛选/高度调整、G1 跟踪、跌倒恢复与部署。

独立项目页用于核对当前数据与代码状态。README 同时出现早期 848 条和后续 992 条统计，说明数据在迭代；训练代码又在论文后增加 FastSAC 路线。所有数字必须绑定 commit、数据 release 和 subset，不能混为一个固定 benchmark。

## 它解决什么问题

常见人体动作集以步行和日常动作为主，难以覆盖快速质心转移、旋转、腾空和跌倒边界。KungFuAthlete 从训练视频提取高动态运动，并把 ground/jump 分开。论文进一步让一个策略联合学习跟踪和跌倒恢复，避免策略一旦离开参考邻域就没有恢复行为。

数据链每一步都可能引入系统误差：视频估计会漂移或遮挡，GMR 会产生脚滑和高度不一致，人工筛选带主观性，训练又可能把参考伪影当目标。项目公开中间 SMPL-H 与机器人 qpos，给了重新重定向和质量审计的机会。

## 架构与数据流

数据路径是 `athlete video → scene segmentation → GVHMR → SMPL-H → GMR → G1 qpos → manual selection/post-processing → gravity-based height adjustment → NPZ`。训练路径基于 Unitree RL Mjlab，分三阶段：先粗跟踪并获得基础恢复，再提高跟踪精度，最后强化鲁棒性；可选 FastSAC 与默认 PPO 做训练效率对照。

跌倒恢复不是独立状态机，而是由动作采样、异常初态与 LKE 等机制让同一策略覆盖失稳状态。这个思路减少切换边界，但也可能让恢复与高精度跟踪争夺策略容量。FastSAC 的早期 wall-clock 优势和 PPO 的最终回报需要一起读，不能只保留最大加速比。

## 代码定位

- [`gvhmr_to_qpos.py`](https://github.com/NPCLEI/KungFuAthleteBot/blob/1e3f207013245a5a0db75e6f70e1cdf762e28e9c/retarget/scripts/gvhmr_to_qpos.py) 连接视频人体恢复结果与 GMR 机器人 qpos。
- [`adjust_robot_height_by_gravity.py`](https://github.com/NPCLEI/KungFuAthleteBot/blob/1e3f207013245a5a0db75e6f70e1cdf762e28e9c/retarget/scripts/adjust_robot_height_by_gravity.py) 对机器人轨迹做地面/高度后处理，是检查穿地与接触伪影的关键位置。
- [三阶段 G1 task 配置](https://github.com/NPCLEI/KungFuAthleteBot/blob/1e3f207013245a5a0db75e6f70e1cdf762e28e9c/unitree_rl_mjlab/src/tasks/tracking/config/g1/env_cfgs.py) 定义阶段间奖励、采样与鲁棒性差异。
- [`MotionCommand`](https://github.com/NPCLEI/KungFuAthleteBot/blob/1e3f207013245a5a0db75e6f70e1cdf762e28e9c/unitree_rl_mjlab/src/tasks/tracking/mdp/commands.py) 维护动作参考、采样与恢复相关状态。
- [`FastSAC`](https://github.com/NPCLEI/KungFuAthleteBot/blob/1e3f207013245a5a0db75e6f70e1cdf762e28e9c/unitree_rl_mjlab/holosoma_min/agents/fast_sac/fast_sac.py) 是后续加入的可选 off-policy 训练实现，不能反写为论文 v1 唯一算法。

## 最小复现路径

先固定论文 v1、仓库 commit、数据 release 与 ground/jump subset。任选一段公开视频对应样本，逐步保存 GVHMR、SMPL-H、GMR qpos、高度调整与 NPZ；检查 FPS、根四元数、关节顺序、脚底高度、速度/加速度峰值、自碰撞和阶段哈希。不要一开始批量跑全部数据。

训练从 ground 中较平稳动作开始，用小环境验证三个 stage 的配置差异，再扩展到 1307 动作和 jump subset。PPO/FastSAC 对照必须固定 GPU、环境数、seed、任务、停止标准和日志；报告 time-to-threshold、最终回报、跟踪误差、跌倒率、恢复成功率、冲击/饱和与失败视频。

## 能力边界

数据来源是公开训练视频，动作估计并非地面真值；人工筛选与后处理无法保证每帧正确。武器类别只包含身体运动，不含精细手或武器操作。jump subset README 已明确警告处在机器人性能上限附近，且部分样本仍可能有瑕疵。

论文与仓库数字随数据版本变化，必须绑定 release。单动作或 1307 checkpoint 的成功不能推广到 992 条动作。FastSAC benchmark 是特定 16 小时窗口和阶段设置的仓库结果，尚不足以证明所有任务更快或最终性能更高。

## 工程判断与风险

最有价值的是保留人体与机器人中间数据，使高动态数据问题可追溯；最危险的是把视觉上炫目的动作直接当成可部署参考。建议先为每段动作生成自动质量报告，ground 与 jump 使用不同限值，失败样本进入隔离队列而不是删除。

高动态真机实验必须由具备资质团队在保护场地执行，使用吊装/防坠、软垫、隔离区、远程急停、低增益和逐级动作包络；监控电机力矩、温度、冲击和结构负载。后空翻、腾空等动作不能按 README 直接复现。本页不提供上机授权或安全参数。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/NPCLEI/KungFuAthleteBot/tree/1e3f207013245a5a0db75e6f70e1cdf762e28e9c)
- [arXiv:2602.13656v1](https://arxiv.org/abs/2602.13656v1)
- [MIT 许可证](https://github.com/NPCLEI/KungFuAthleteBot/blob/1e3f207013245a5a0db75e6f70e1cdf762e28e9c/LICENSE)
