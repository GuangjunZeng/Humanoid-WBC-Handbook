# 15 分钟人形行走：FastSAC/FastTD3 的离策略配方与时间边界

[English version](en/fast-humanoid-locomotion-2512.01996.md)

来源：[arXiv:2512.01996](https://arxiv.org/abs/2512.01996) · [固定提交的论文配方代码 Holosoma](https://github.com/amazon-far/holosoma/tree/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3) · [固定提交的 FastTD3 算法仓库](https://github.com/younggyoseo/FastTD3/tree/229ed59bbf43ea2f7a2d5d90d1076314839944d7)

解读范围：完整 12 页论文、所有消融与实机展示，以及 Holosoma 中 FastSAC、G1 locomotion reward/curriculum 和官方 FastTD3 算法实现。标题中的“15 分钟”只按论文的单 RTX 4090 locomotion 条件解释。

> 一句话总结：作者把 replay、多次梯度更新、LayerNorm、平均双 Q、C51 critic、低探索噪声和简洁 reward 组合成 FastSAC/FastTD3，在单张 RTX 4090 上 15 分钟训练 G1/T1 平地、粗糙地形和抗推行走；全身动作跟踪则使用 4×L40S 和更长时间，论文没有给出大规模真机成功率，所以不能把标题推广为“任意 WBC 15 分钟训练完成”。

术语导航：离策略强化学习（off-policy reinforcement learning）、经验回放（experience replay）、软演员评论家（Soft Actor-Critic, SAC）、延迟双评论家（Twin Delayed DDPG, TD3）、分布式评论家（distributional critic）、类别分布价值（C51）、层归一化（Layer Normalization, LayerNorm）、目标熵（target entropy）与域随机化（domain randomization）。

## 工程痛点

人形 RL 通常使用 PPO，因为大规模并行仿真能快速生成新数据，on-policy 实现稳定。代价是同一 transition 只使用很少次数，墙钟速度受 rollout 与更新平衡限制。把 SAC/TD3 直接移植到高维 humanoid 又常因 replay 分布、critic 过估计、探索过强和大 batch 优化不稳而失败。

可以把 off-policy replay 理解为一间循环使用试题的训练馆：PPO 做完一套题就换新题，FastSAC 会从题库反复抽取难题，但若题库陈旧或评分器偏置也会学坏。另一个类比是赛车调校：单独换更大引擎不够，轮胎、变速、制动和悬挂要一起匹配；论文的速度来自一组互相依赖的 critic、optimizer、noise、reward 与 simulator 配方，不是某个神奇超参数。

## 核心洞察

FastSAC/FastTD3 在大量并行环境外增加 replay buffer 和每步多次更新。critic 不用 clipped double Q 的最小值，而取两个 Q 的平均；LayerNorm 稳定高维观测；C51 分布式 critic 比标量或论文测试的 quantile 版本更有效。locomotion 用折扣 γ=0.97，全身 tracking 用 0.99，说明有效 horizon 随任务难度变化。

FastSAC 把 tanh 前标准差上限设为 1，初始温度 α=0.001，并自动调节；locomotion 目标熵为 0，tracking 为 −|A|/2。FastTD3 混合 0.01–0.05 的低高斯噪声。优化使用 Adam/AdamW 风格 3e−4 学习率、0.001 weight decay、β2=0.95。论文强调 reward 少于十项，并用 curriculum、左右对称和非足接触终止。

## 方法主线

locomotion reward 覆盖线速度、yaw、足高、默认姿态、足方向、交叉足、alive、躯干和动作率。粗糙地形与强推力通过课程逐步加难，域随机化覆盖物理参数。训练曲线以墙钟时间而非 environment steps 为横轴，能直接回答开发者“等待多久得到可用策略”，但强依赖 RTX 4090、环境数和 simulator throughput。

全身 tracking 复用同一算法配方，却使用 4 张 L40S、16,384 环境，训练舞蹈、拳击和抗推等动作。作者展示零样本 sim-to-real，并称舞蹈连续运行超过两分钟。该部分证明算法不限于速度跟踪，却不属于单卡 15 分钟结论。

## 关键图解

![Figure 1：结果范围](assets/fast-humanoid-locomotion-2512.01996/figure-1-summary.jpg)

Figure 1 同时展示 locomotion 与 whole-body tracking，最容易让读者把时间混在一起。应先区分单 4090 行走和多 L40S 跟踪，再看实机图片属于定性部署还是重复统计。

![Figure 2：配方消融](assets/fast-humanoid-locomotion-2512.01996/figure-2-recipe-ablation.jpg)

Figure 2 检查 clipped/average Q、非平地 replay、LayerNorm、折扣和熵。它说明“off-policy 不适合 humanoid”不是固定结论；critic 与探索配错时才会快速发散或停滞。

![Figure 3：15 分钟行走](assets/fast-humanoid-locomotion-2512.01996/figure-3-locomotion.jpg)

Figure 3 在单张 RTX 4090 比较 G1/T1、平面/粗糙地形和 strong push。FastSAC/TD3 多数条件在 5–12 分钟明显超过 PPO，15 分钟达到较高速度跟踪回报；图注明确 push 间隔与 episode 长度，是复现标题的必要条件。

![Figure 5–6：全身跟踪](assets/fast-humanoid-locomotion-2512.01996/figure-5-6-tracking.jpg)

Figure 5–6 展示多 GPU tracking 曲线和实机舞蹈、拳击、抗推。它支持“配方可扩展到高维动作”，但没有每个动作多少次成功、跌倒率或峰值力矩，不能当作工业可靠性表。

## 最有说服力的实验

最强实验是 Figure 2 消融与 Figure 3 墙钟曲线。前者解释为什么常规 SAC/TD3 失败，后者在相同单卡条件下与 PPO 比较真正的训练时间。两者组合比只报告最终 return 更能指导工程：先锁定 simulator 吞吐和更新比，再逐项核对 critic、normalization、discount 和 exploration。

论文的实机全身动作是重要能力证据，但证据等级较低：主要是示例与视频，未给多 seed、不同机器人、长期温度和失效分布。对使用者而言，训练曲线可以复现算法效率，实机上线仍需另一套安全与重复性验收。

## 论文—代码映射

论文明确把当前 recipe 指向 Holosoma。固定提交 `6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3` 中，`src/holosoma/holosoma/agents/fast_sac/fast_sac_agent.py::FastSACAgent` 的 `_update_main`、`_update_pol`、`learn` 实现 replay 更新、C51 target、温度与 actor 优化；`config_values/loco/g1/reward.py` 和 `managers/reward/terms/locomotion.py` 实现 G1 reward。

同仓库 `config_values/loco/g1/curriculum.py`、`randomization.py` 与 `termination.py` 对应 terrain/push 课程、域随机化和非足接触终止。早期官方 `FastTD3` 固定提交 `229ed59bbf43ea2f7a2d5d90d1076314839944d7` 提供算法抽象与实验入口；复现本论文数字应优先 Holosoma，而不是误把两个仓库的默认配置当成完全等价。

## 局限与工程判断

作者没有单独列出完整 limitations，但明确把更多任务、更多 off-policy 改进和更广比较留作未来工作。论文文字也清楚区分单 GPU locomotion 与多 GPU whole-body tracking；Figure 3 的 15 分钟绑定 RTX 4090、特定并行环境、20 秒 episode 和 push 频率。

独立工程局限包括：return 曲线不是硬件成功率，实机没有报告重复试验、故障分类、峰值电流/力矩和热状态；算法效率与 simulator/GPU、混合精度、buffer 和 update-to-data ratio 强耦合；replay 可能在 curriculum 改变后保留旧分布；简单 reward 在新平台不一定保留安全足态。

硬件安全上，快速训练不应压缩验证时间。每次 policy checkpoint 都要先做 action scale、observation scale、关节顺序、PD、延迟和限幅检查；粗糙地形和 push 试验需吊绳、软垫、急停与跌倒保护。任何“15 分钟后直接上机”的流程都超出论文证据。

## 可执行但有边界的结论

论文最值得复用的是墙钟导向的完整 recipe：在相同 GPU 和 simulator 下记录 samples/s、updates/s、buffer age、critic loss 和 return，逐项消融而不是只比较 steps。若 FastSAC 更快但 P95 critic 或动作抖动不稳定，应优先修复稳定性，而非继续增加环境数。

团队可以把 15 分钟设为开发回归基准：固定 G1/T1 任务和 seed，在软件变更后检查到达目标 return 的时间。它不是产品能力承诺。全身 tracking 应建立独立预算、硬件指标与验收页，避免标题吞掉真实计算成本。

## 复现与验收清单

固定 RTX 4090/L40S 型号、驱动、PyTorch、simulator、环境数、physics/control Hz、buffer、batch、update ratio、C51 atoms/support、Q 聚合、LayerNorm、γ、噪声、α、reward、curriculum、randomization、seed 与两份 commit。复现 Figure 2、3、5 的墙钟曲线并公开置信区间。

记录训练前 15 分钟每分钟 samples、updates、GPU 利用率、显存、buffer 新鲜度、Q 分布、entropy 与 policy action range。对 clipped/average Q、scalar/C51、LayerNorm、γ、target entropy、weight decay 和 β2 做单变量消融；换 GPU 时同时报告等样本和等时间结果。

实机先用导出模型一致性测试和 MuJoCo sim-to-sim，再做悬挂、原地、低速、平地、弱推、粗糙地形。每阶段记录成功、partial、跌倒、急停、足滑、峰值力矩/电流、温升和连续运行时间。只有训练速度与部署安全两条独立流水线都通过，才能称为可用工程方案。

## 进一步工程审计

离策略训练首先要审计更新比。环境数增加后，rollout 速度和 gradient update 速度不会同步增长；若每秒新样本远多于更新，replay 失去复用优势，若更新过多又会对旧分布过拟合。日志中应同时记录环境步、梯度步、样本平均被使用次数和从写入到采样的年龄分布，而不是只看全局 step。

课程变化会让 replay 混合不同任务分布。例如从平地进入粗糙地形、从弱推进入强推后，旧 buffer 仍含大量简单样本，可能减慢适应或稳定 critic。可以比较全量 replay、按难度分层采样与阶段性衰减，并报告各层占比。不能为追求 15 分钟任意清空 buffer，因为那会改变论文配方，应把差异写清。

平均双 Q 的优势也要观察尾部。取最小值偏保守，平均值提高学习速度，但当一个 critic 在危险动作上严重过估计时，平均仍会抬高目标。工程监控应按 reward、terrain 和 termination 类型画两个 Q 的差、分布 support 饱和与真实 return，而不仅是均值 loss。部署候选可以额外用 conservative evaluator 筛除高分歧状态。

C51 support 若设置过窄，value 会堆在边界；过宽则分辨率不足。换 reward scale、episode 长度或任务后必须重新检查 atom occupancy，不能照搬原值。LayerNorm 同样依赖观测拼接契约：新加一组未经缩放的 terrain 或 command 特征可能改变网络动态，即使 nominal observation normalization 仍正常。

训练速度基准应区分冷启动和稳定运行。首次编译 kernel、加载 terrain、分配 replay 和导出模型都可能占据短任务的大比例。建议报告从进程启动到可部署 checkpoint、从第一步到目标 return 两种时间，并固定是否包含 evaluation。否则不同团队都宣称“15 分钟”，实际测量窗口并不一致。

实机观测/动作契约是最常见的失败来源。训练和部署必须自动比较关节名及顺序、默认姿态、action scale、observation scale、gravity frame、控制频率和模型 hash。任何字段不一致直接拒绝加载。快速算法会更快生成大量 checkpoint，更需要机器可检查的 contract，而不是依靠操作者肉眼确认。

长时运行测试不可由短训练曲线替代。舞蹈超过两分钟是良好信号，但行走应在不同电量、温度、地面摩擦和重复推力下记录数十分钟的 drift、过热和跌倒。若训练只需十几分钟而硬件验收需要数小时，这是正常且必要的工程比例，不能为保持宣传对称压缩后者。

因此在 Handbook 搜索“为什么 FastSAC 很快但真机不稳”时，答案应先指向 replay age、Q 分歧、scale/顺序、PD/延迟和硬件 envelope，再讨论学习率。配方解决的是样本复用与优化稳定性，无法自动修复部署接口错误。

还需要把“学得快”和“收敛可靠”分开统计。同一设置如果一半随机种子五分钟达到目标，另一半完全失败，最佳曲线仍很漂亮，却不适合作为日常开发基线。应报告到达门槛时间的中位数、最慢分位、失败比例和最终波动，并预先规定超时如何处理。若只挑成功种子，训练时间结论会系统性偏乐观。

奖励项虽少，尺度耦合仍可能改变行为。速度奖励提高后，策略可能通过更大步幅获得回报，同时增加落地冲击；动作变化惩罚过强又可能在被推时来不及恢复。每次修改应同时画速度误差、足滑、非足接触、力矩、动作变化和存活，而不是只比较总回报。总回报相同的两个策略，安全性质可能完全不同。

终止条件也影响学习速度。非足部接触立即结束会快速告诉策略“不要跌倒”，但会让经验回放缺少跌倒后的状态，也可能把短暂手扶地等可恢复行为一律排除。若目标任务需要恢复或多接触，应建立单独课程和策略，不要简单放宽原终止后仍沿用十五分钟结论。任务定义改变时，训练基准也随之改变。

地形课程应检查机器人究竟学会了地形适应，还是记住了生成器规律。把高度场种子、尺度和障碍频率分成训练、验证与完全不同生成方式的外推集；若验证回报高但换生成器立即跌倒，说明快速训练主要拟合了课程。实机选择地面时也要量化粗糙度、摩擦和坡度，避免“粗糙地形”只是一张定性照片。

推力扰动应记录方向、大小、持续时间、施加部位和相位。相同速度增量在双支撑与单支撑的难度不同，随机平均会掩盖薄弱相位。可按步态相位绘制恢复率和最大偏移，优先补最危险区间。实机推力必须用可重复装置或明确测量，人工推一下的视频不能和仿真强推曲线直接对应。

模型导出是另一条常见断点。训练框架中的观测归一化、历史缓冲、动作裁剪和随机模块在导出时可能遗漏；应对同一录制观测逐步比较训练模型、导出模型和实机运行时输出，要求数值误差在门限内。若导出后才发现动作不同，继续调真机比例会把软件错误伪装成仿真现实差距。

硬件回归要与训练回归解耦。日常代码提交可以在固定仿真任务上用十几分钟检查学习速度，但不是每次都上机；只有通过数值契约、外推地形、扰动和安全审计的候选才进入受控实机。这样既保留快速迭代优势，又不会让大量未经筛选的策略消耗机器人寿命。

当算法迁移到另一种机器人时，第一轮目标不应仍是十五分钟。先用较长预算确认动作范围、奖励、观测和动力学合理，再逐项恢复快速配方并测量哪里获得加速。若一开始就追时间，团队容易通过缩短任务、放松指标或选择简单地形“复现”标题，却没有获得同等能力。

最终，一个可信的快速训练页面应同时展示计算条件、能力范围、重复性和部署门槛。读者搜索到它时能明确知道：哪部分确实在单卡短时间完成，哪部分需要多卡和更久，哪些实机结果只有展示，哪些步骤绝不能因为训练快而跳过。这种边界说明比单一速度数字更能减少工程误用。

持续维护时还应保存一条不随新算法变化的参考流水线。仿真器、驱动或训练框架升级后，先用旧提交和旧模型重跑，确认吞吐、回报与导出一致，再比较新算法。若基础环境已经变快或变慢，把全部差异归因于学习方法会得出错误结论。训练报告要同时记录软件版本、机器负载和测量起止点，并保留原始曲线，方便之后复核。

快速基准也要防止为了成绩缩小问题。减少随机化、缩短回合、降低目标速度或只保留平地都能让门槛更早达到，却改变了能力。任何任务契约变化都应生成新基准名称，不能继续沿用原来的十五分钟标签。只有条件可比较，墙钟数字才有意义。

> **工程判断**：15 分钟是一个严格限定的 locomotion 墙钟基准；真正可迁移的成果是配方与测量方法，不是把所有 humanoid WBC 都压成同一个时间口号。
