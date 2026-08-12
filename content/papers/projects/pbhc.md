# PBHC / KungfuBot：从人体动作到 G1 高动态跟踪的开源链路

[English version](en/pbhc.md)

审阅快照：[TeleHuman/PBHC@`ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0`](https://github.com/TeleHuman/PBHC/tree/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0) · 1052 stars（2026-08-12 快照）· CC BY-NC 4.0，仓库明确限制商业用途。star 只是发现门槛，不是高动态动作在其他机器人上的成功率或安全保证。

## 为什么收录

PBHC 是 KungfuBot 的官方实现，也包含后续 general motion tracking 路径。它的价值不只是几段功夫演示，而是把 motion source、SMPL 统一、物理筛选、Mink/PHC retargeting、动作校正、Isaac Gym 训练、轨迹分析和 MuJoCo sim2sim 放在一个仓库。

这条链路比“下载动作然后 PPO”更真实：高动态技能的主要成本往往在数据可行性、接触时序、起止姿态和真机切入条件。项目页因此突出数据契约和可执行的中间检查，而不把最终视频当作全链条证据。

## 它解决什么问题

视频或 mocap 里的人体动作可能有重建飘移、穿地、不可达关节、错误接触和不适合 G1 的速度/惯量。直接重定向会让 RL 对不可行参考进行折中，最后很难分辨失败来自数据还是控制器。

PBHC 先过滤和校正动作，再重定向到机器人，然后用自适应跟踪奖励训练。adaptive sigma 让各跟踪项的容忍度随误差统计调整，减少一组固定尺度对不同技能全部通用的假设。

## 架构与数据流

数据流为 `video/LAFAN/AMASS → SMPL motion → optional physics filter → Mink or PHC retarget → contact/height correction → robot-motion visualization and interpolation → Isaac Gym policy training → rollout metrics → ONNX/MuJoCo sim2sim → robot-specific adapter`。每一步都应留存帧率、坐标系、关节顺序和接触 mask。

仓库区分 single-motion tracking 和 general tracking。前者用于 KungfuBot 的特定动作；后者包含 teacher/student observation 配置。README 还提供 benchmark mode，其 actor 有 privileged information 且没有 domain randomization，仓库自身已明确它不可部署，不应将 benchmark 成绩当成 sim-to-real 成绩。

## 代码定位

- [`MotionFilter`](https://github.com/TeleHuman/PBHC/blob/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0/smpl_retarget/motion_filter/utils/motion_filter.py) 将人体 mesh/物理指标变成可选的动作筛选。
- [`correct_motion`](https://github.com/TeleHuman/PBHC/blob/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0/smpl_retarget/mink_retarget/convert_fit_motion.py) 使用 contact mask 和 vertices 修正高度；[`retarget_fit_motion`](https://github.com/TeleHuman/PBHC/blob/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0/smpl_retarget/mink_retarget/retargeting/mink_retarget.py) 是 G1 Mink 重定向主路径。
- [`GeneralTracking._update_adaptive_sigma`](https://github.com/TeleHuman/PBHC/blob/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0/humanoidverse/envs/motion_tracking/general_tracking.py) 更新跟踪尺度，同文件的 `_reward_teleop_body_position_extend`、`_reward_teleop_joint_position` 等将不同误差送入奖励。
- [`humanoidverse/README.md`](https://github.com/TeleHuman/PBHC/blob/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0/humanoidverse/README.md) 固定了训练、benchmark、评估、ONNX 与 MuJoCo 路径，并明确写出真机前的限位检查。

## 最小复现路径

先用仓库提供的 horse-stance sample 和 pretrained checkpoint 复现 evaluation，不要直接训新动作。记录 motion schema、fps、joint order、contact mask、policy observation shape 和 sample/ratio evaluation 指标。再导出 ONNX，用 MuJoCo 验证一致的起止姿态和终止条件。

对新动作，先单独可视化 SMPL、重定向和 correction 结果，再用 128 环境调试，最后扩到 README 中的 4096 环境与 50000 iterations。比较 fixed sigma/adaptive sigma、有无 filter/correction，报告跟踪误差、完整率、力矩、平滑性、接触错位和多 seed。

## 能力边界

PBHC 不是一个自主感知和技能规划系统。KungfuBot 论文的每个动作主要对应独立策略，而真机定量重复试验主要集中在太极。仓库新增 general tracking 支持不等于论文已为所有动作和环境给出相同硬件证据。

仓库整体采用 CC BY-NC 4.0，README 还明确禁止用于宣传商业产品的 demo。依赖的 PHC、MaskedMimic、IPMAN 等仍有各自条款，不能用顶层 LICENSE 替代逐项审查。

## 工程判断与风险

这个项目最值得复用的是“先数据质量，再策略训练”的分层调试方式。最容易误用的是将人眼觉得漂亮的重定向回放当作动力学可行性，或将 benchmark oracle 当作可部署 policy。应保留数据阶段的失败标签，否则策略会吞掉上游错误。

高动态真机必须有支撑/吊装、足够缓冲空间、物理急停、关节位置/速度/加速度/力矩限制、接触冲击和通信超时保护。先做 sim2sim 和慢放低增益，不应从视频效果倒推真机参数。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/TeleHuman/PBHC/tree/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0)
- [SMPL 重定向说明](https://github.com/TeleHuman/PBHC/blob/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0/smpl_retarget/README.md)
- [对应论文的中文深读](../kungfubot-2506.12851.md)
