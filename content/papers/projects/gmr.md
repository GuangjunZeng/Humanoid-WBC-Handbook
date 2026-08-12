# GMR：面向多种人形本体的实时动作重定向库

[English version](en/gmr.md)

审阅快照：[YanjieZe/GMR@`bb1bbe40774794fceb2a7c579a3464a28e68c844`](https://github.com/YanjieZe/GMR/tree/bb1bbe40774794fceb2a7c579a3464a28e68c844) · 2581 stars（2026-08-12 快照）· MIT。该 commit 晚于论文，包含后续机器人和数据格式扩展；star 只是发现信号，不是重定向动力学可行性或真机安全的证明。

## 为什么收录

GMR（General Motion Retargeting，通用动作重定向）是 WBC 训练数据上游的高星工程基座。它使用 Mink 差分逆运动学（differential IK），将 BVH、SMPL 等人体动作通过配置化关键刚体、局部尺度、任务权重与两阶段优化映射到 G1/H1 等本体。

与只给一个离线脚本的方法相比，GMR 把机器人映射放入 JSON 配置，便于审查不同刚体的位置/姿态权重。这使它适合做“相同人体动作在不同机器人上的中性起点”，但不代表所有配置都已经过同等实验验收。

## 它解决什么问题

人和机器人的肢段比例、关节自由度、关节限位与脚底几何不同。只拷贝关节角会导致末端偏移、自碰撞或姿态不可达；只对齐手脚又可能丢失躯干方向和接触语义。

GMR 先对人体局部位置做非均匀缩放，再在两组任务上分阶段迭代 IK。第一阶段锁定主要结构和根，第二阶段补充末端或方向细节。每阶段以误差改善或最大迭代停止，用显式计算预算换取实时性。

## 架构与数据流

核心数据流是 `human motion parser → global human body transforms → per-body local scaling → task1 differential IK → task2 refinement → ground offset → robot qpos trajectory`。配置文件定义 human body 与 robot body 的映射、尺度、position/orientation weight 和任务阶段。

输出是几何上尽量贴近参考的机器人关节轨迹。它不包含一个保证动力学可行的 controller：地面偏移可以让脚不穿地，但不会自动满足支撑多边形、摩擦锥、力矩与自碰撞。

## 代码定位

- [`GeneralMotionRetargeting.scale_human_data`](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/motion_retarget.py) 将关键刚体转成相对根位置，应用局部尺度后再加回根平移。
- [`GeneralMotionRetargeting.retarget`](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/motion_retarget.py) 依次运行 `tasks1` 和 `tasks2`，并用改善阈值/最大迭代停止。
- [LAFAN1 到 G1 配置](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/ik_configs/bvh_lafan1_to_g1.json) 显式绑定两阶段刚体、权重和上下肢尺度。
- [`offset_human_data_to_ground` / `apply_ground_offset`](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/motion_retarget.py) 处理整体高度偏移，不应与接触力学混同。

## 最小复现路径

锁定 commit、Mink、MuJoCo、机器人模型和人体数据解析版本。从一段短 LAFAN1 走路开始，保存原人体 transform、scaled transform、每阶段 residual、iteration count、ground offset 与最终 qpos。使用同一配置重复运行，确认输出确定。

随后增加深蹲、跪地、手脚快速运动和转身，分别报告刚体位置/旋转误差、关节限位、脚滑、自碰撞、速度/加速度峰值。最后才将通过几何检查的轨迹送入物理跟踪和逆动力学检查。

## 能力边界

GMR 不是动作恢复模型，输入视频需要 GVHMR/WHAM 等上游；它也不是低层 tracking policy 或 WBC。它优化了选定几何任务，没有在每帧求解接触力、力矩或全身自碰撞约束。

该 commit 包含论文后扩展，因此项目能力表不能当作原论文比较已验证所有机型。新配置需单独记录 robot model hash、joint/body map、权重、尺度与失败集。

## 工程判断与风险

最值得复用的是把本体映射和权重变成可版本控制配置；最需防范的是“回放好看即可执行”。应使用物理跟踪成功率、逆动力残差和接触一致性对每个动作二次评级，并保留失败原因。

重定向轨迹不可直接下发实机。先做关节/速度/加速度/力矩/自碰撞检查，再做仿真跟踪、sim2sim、支撑或吊装低增益验证。真机限值必须来自目标硬件，而不是人体数据。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/YanjieZe/GMR/tree/bb1bbe40774794fceb2a7c579a3464a28e68c844)
- [核心重定向实现](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/motion_retarget.py)
- [对应论文的中文深读](../retargeting-matters-2510.02252v1.md)
