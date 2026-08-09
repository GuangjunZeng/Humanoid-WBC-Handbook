# Humanoid-Gym：把训练、跨仿真校准与实机部署做成最小开源闭环

来源：[arXiv:2404.05695v2](https://arxiv.org/abs/2404.05695v2) · [固定提交的官方代码](https://github.com/roboterax/humanoid-gym/tree/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f)

解读范围：完整 6 页正文和附录。

## 问题与主线

这篇论文的贡献更接近工程基线而非新算法：用 Isaac Gym 大规模训练 PPO，把同一策略先放进经实机摆动曲线校准的 MuJoCo，再零样本部署到两种尺寸的 RobotEra XBot。输入是速度命令、周期时钟、关节位置/速度、机身角速度/欧拉角和上一动作的 15 帧堆叠；训练 critic 另看摩擦、质量、基座线速度、接触和推力等特权状态。输出是 12 个关节目标位置，策略 100 Hz，PD 1000 Hz。

奖励把速度、周期接触、参考关节、姿态/高度、能耗、二阶动作平滑和大接触力组合为加权和。随机化覆盖观测噪声、0–10 ms 延迟、摩擦、载荷和电机强度。MuJoCo 校准用实机正弦关节响应和相图检查模拟动态，而不是把第二仿真器当成实机真值。

## 关键定位与证据

- Figure 2：Isaac Gym 训练 → MuJoCo 跨引擎检查 → 实机部署的完整流水线。
- Table I：单帧 47 维部署观测与 73 维特权状态的边界；Appendix Table II 指定 15/3 帧堆叠。
- Figure 3/4：校准后 MuJoCo 的关节正弦轨迹和相图更接近实机，提供的是定性曲线证据。
- Appendix Table III：噪声、延迟、摩擦、电机强度和载荷随机化范围。
- Appendix Table IV：`exp(-w||e||²)` 型跟踪奖励与动作平滑、能耗、接触力惩罚。

最有价值的证据是同一框架在 1.2 m XBot-S 和 1.65 m XBot-L 上都实现零样本部署，说明接口与工程流程不只绑定一个尺寸。但论文没有成功率、里程、跌倒率或跨仿真预测性相关系数；“rigorously tested”不能等同于可统计复现。

## 论文—代码映射

| 组件 | 固定提交符号 | 对应关系 |
|---|---|---|
| 观测历史与特权历史 | `XBotLCfg.env.frame_stack/c_frame_stack`、`LeggedRobot.obs_history/critic_history` | 固定 15 帧 actor 与 3 帧 critic 堆叠 |
| 100 Hz/1000 Hz 控制 | `XBotLCfg.control.decimation`、`XBotLCfg.sim.dt`、`LeggedRobot.step` | 每 10 个 1 ms 物理步更新一次策略动作 |
| 奖励与随机化 | `XBotLCfg.rewards.scales`、`XBotLCfg.domain_rand` | 把论文附录机制落实为 XBot-L 专用配置 |
| 安全边界 | `XBotLCfg.safety`、`LeggedRobot.check_termination` | 含位置/速度/力矩缩放与非足部接触终止，但不是完整实机安全系统 |

仓库标注 BSD-3-Clause，并继承 legged_gym/rsl_rl 相关版权。本文只链接和解释，不复制代码或参数集。

## 边界与工程判断

论文没有独立局限章节。其主要不足是定量评测缺失、机器人均来自同一厂商、MuJoCo 校准只展示少量关节轨迹、训练配置与论文附录存在迭代差异。正弦响应接近不代表碰撞、摩擦突变、落脚冲击等动态都接近；sim-to-sim 只能作为失败筛查层，不能替代硬件验证。

可复用结论是：把跨引擎回放放在仿真训练与实机之间，并用真实关节响应校准第二引擎，能形成低成本工程门禁。复现时应补充固定场景成功率、跌倒率、速度误差、接触峰值和跨引擎/实机相关性。附录中的增益、随机化和限值只属于论文机器人，不能直接下发到其他硬件。
