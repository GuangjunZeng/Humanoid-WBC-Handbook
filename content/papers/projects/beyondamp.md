# beyondAMP：把对抗运动先验模块化接入 Isaac Lab 与 MJLab

[English version](en/beyondamp.md)

审阅快照：[Renforce-Dynamics/beyondAMP@`cee88cdc0958c417e316f9452f802e25a71bc289`](https://github.com/Renforce-Dynamics/beyondAMP/tree/cee88cdc0958c417e316f9452f802e25a71bc289) · 281 stars（2026-08-12 快照）· 仓库许可证未能由官方 GitHub 元数据断言，使用前需逐目录核对。star 只用于发现，不是技术置信度或安全结论。

## 为什么收录

beyondAMP 没有把自己包装为一篇新论文，而是把 Adversarial Motion Priors（AMP，对抗运动先验）的数据集、判别器、observation group、环境 wrapper 与 runner 抽成可接入不同本体的组件。它同时提供 Isaac Lab/PhysX 与 MJLab/MuJoCo-Warp 后端，是检查“风格先验究竟贡献了什么”的实用工程基线。

项目属于地形运动、运动生成和恢复安全三个既有 topic，因为 AMP 常与任务奖励共同塑造运动风格，并可能影响异常姿态覆盖。但收录不意味着它已证明恢复能力或优于跟踪方法；仓库演示主要是拳击、犬式和跪行等动作，必须按配置判断任务目标。

## 它解决什么问题

传统 locomotion 奖励需要手工组合速度、姿态、脚步、能耗和动作平滑项，得到的运动仍可能不自然。AMP 用参考动作中的状态转移训练判别器，把“像数据”作为额外奖励。工程难点在于参考 transition 与策略 transition 的时间、关节、归一化和 observation 定义必须一致。

beyondAMP 将这条链从具体机器人任务中分离，使用户可以在现有 Isaac Lab 或 MJLab 环境中增加 `amp` observation group 与 wrapper。模块化降低接入成本，也提高误用风险：如果 AMP 字段错位，判别器仍可能收敛，却奖励完全错误的运动统计。

## 架构与数据流

路径为 `NPZ motion → MotionDataset/WeightedMotionDataset → AMP observation builder → AMPEnvWrapper → policy rollouts + expert transitions → AMPDiscriminator → style reward → AMPOnPolicyRunner`。基础任务仍提供 task reward；判别器并不替代速度命令、接触或安全约束。

Isaac Lab 与 MJLab 分别有 wrapper 与 observation 实现，复用判别器和数据逻辑。软/硬跟踪示例通过不同 observation 与奖励组合改变策略受参考约束程度。对比后端时，应确保 expert transition 的采样率、坐标变换和归一化相同，否则结果差异不能归因于物理引擎。

## 代码定位

- [`AMPDiscriminator`](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/source/beyondAMP/beyondAMP/modules/amp_discriminator.py) 定义判别网络、判别损失和 style reward 的直接实现。
- [`MotionDataset`](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/source/beyondAMP/beyondAMP/motion/motion_dataset.py) 读取参考动作并形成用于判别的 transition。
- [Isaac Lab `AMPEnvWrapper`](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/source/beyondAMP/beyondAMP/isaaclab/rsl_rl/amp_wrapper.py) 把环境 observation、下一状态与 AMP reward 接入 RSL-RL。
- [MJLab `AMPEnvWrapper`](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/source/beyondAMP/beyondAMP/mjlab/rsl_rl/amp_wrapper.py) 是第二后端对应接口。
- [`amp_obs_anchor_group`](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/source/beyondAMP/beyondAMP/obs_groups/amp_obs_anchor.py) 明确 anchor-based AMP 输入的构成。

## 最小复现路径

固定仓库、Isaac Lab/MJLab、RSL-RL 和机器人资产版本。先用仓库 demo 动作运行 `beyondAMP-DemoPunch-G1-BasicAMP` 的小环境 smoke test，打印 expert/policy AMP observation 的字段、shape、均值方差与相邻帧间隔。确认判别器能区分打乱 transition 后，再开始完整训练。

最小消融至少包含 task-only、AMP、soft tracking 和 hard tracking，固定 seed、环境数、训练步数与 task reward。报告 task return、style reward、判别准确率、动作饱和、根姿态、脚滑、终止原因与多个随机种子；再在另一后端复现同一 checkpoint 或同一配置，区分算法与模拟器差异。

## 能力边界

AMP 只使策略分布接近参考数据定义的特征，不保证语义正确、接触合理或硬件安全。若数据含滑脚、穿地或高冲击，判别器会把这些问题也当作风格。README 推荐 GMR/TrackerLab 做预处理，是依赖建议，不构成输入数据质量担保。

仓库没有给出对所有本体、后端和动作的统一 benchmark；示例在特定 G1 配置上运行。MJLab 安装还需要额外步骤，两个后端并非一个命令完全等价。许可证元数据不明确，不能在分发或商业使用时仅凭引用列表判断授权。

## 工程判断与风险

最值得复用的是清晰的 expert transition 契约与双后端 wrapper；最需要防范的是把 style reward 当作“自然”和“安全”的代理。接入新本体时应先做字段级单元测试、时间反转/关节置乱负对照和 reference replay，可视化判别器究竟依赖哪些状态。

真机策略需要额外的碰撞、关节限位、速度/力矩、接触冲击、姿态和通信超时安全层。先独立 sim2sim，再用支撑或吊装、低增益与急停测试。AMP 可能鼓励训练数据中的高动态动作，不能因 reward 上升就放宽硬件限幅。本页不提供上机参数。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/Renforce-Dynamics/beyondAMP/tree/cee88cdc0958c417e316f9452f802e25a71bc289)
- [官方接入教程](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/docs/tutorial.md)
- [MJLab G1 任务配置](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/source/amp_tasks_mjlab/amp_tasks_mjlab/velocity/g1/amp_env_cfg.py)
