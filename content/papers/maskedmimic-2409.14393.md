# MaskedMimic：把多种控制接口统一为“补全缺失动作”

[English version](en/maskedmimic-2409.14393.md)

来源：[arXiv:2409.14393](https://arxiv.org/abs/2409.14393) · [ACM DOI](https://doi.org/10.1145/3687951) · [固定提交官方代码](https://github.com/NVlabs/ProtoMotions/tree/5241478e35a7dcf5d1455dac2df0486d5e7f440a)

解读范围：完整 21 页论文、参考文献和补充材料，以及 ProtoMotions 3 固定提交中的稀疏条件控制、VAE 学生和实验配置。论文对象是 69-DoF 物理仿真 SMPL 角色，不是人形机器人真机。

> 一句话总结：MaskedMimic 先用强化学习得到看见完整未来动作的教师，再用结构化随机遮挡和在线蒸馏训练只看部分目标的条件 VAE，使同一物理策略能接受关键帧、稀疏关节、文字和物体等不同约束；它证明了统一接口在仿真角色上的可行性，但没有给出机器人实机或安全关键部署证据。

术语导航：动作补全（motion inpainting）从部分约束恢复完整动作；任意关节任意时刻（any-joint-any-time）允许不同关节在不同未来时刻出现；部分目标（partial goal）、完整目标（full goal）、结构化遮挡（structured masking）、在线数据聚合（DAgger）、条件变分自编码器（conditional VAE, C-VAE）、可学习先验（learned prior）、残差后验（residual posterior）、目标工程（goal-engineering）和情节固定噪声（episodic latent noise）共同决定模型能否在约束不足时仍生成连贯行为。

## 工程痛点

传统物理角色控制器通常按接口分家：全身动作跟踪、头手 VR 跟踪、摇杆转向、文字动作和坐椅交互各训一个策略。新任务不仅要重新设计奖励，还要重新收集适合该奖励的数据；多个策略之间的状态、动作和相位也未必能平滑切换。项目规模增大后，真正昂贵的不是再加一个网络，而是维护一组彼此不兼容的控制合同。

MaskedMimic 把这些接口重新表述成同一道题：用户只描述完整动作的一部分，控制器负责在物理环境中补全其余部分。它像让动画师只在若干时间点钉住手、头或骨盆，系统在这些“图钉”之间自动补出满足动力学的全身运动；文字和物体则是另外两类图钉，而不是必须另训策略的新任务名。

部分约束天然是一对多问题。只要求右手两秒后到达某点，并未规定迈哪只脚、是否弯腰、手臂走哪条路径。若用普通回归把所有可行解取平均，结果可能既不自然也无法保持平衡。论文因此需要一个分布模型，而不是只预测唯一动作。

另一个难点是训练时的“信息泄漏”。若每一帧随机显示不同关节，模型跨几帧就能拼出接近完整动作，训练问题会比真实 VR 丢传感器、长时关键帧或纯文字控制容易得多。Mask 的时序结构不是数据增强小技巧，而是决定训练任务是否真的欠约束。

## 核心洞察

第一层洞察是先分离“会不会执行完整动作”和“能不能从部分描述猜对动作”。完整约束控制器 `πFC` 通过强化学习学习在接触、地形和物体存在时把运动学参考变成 PD 目标；部分约束控制器 `πPC` 不再重新学一套任务奖励，而是模仿教师在同一状态下会执行的动作。这样，物理执行能力与接口补全能力有了可分别检查的训练阶段。

第二层洞察是用 DAgger 而不是离线行为克隆。学生在自己的策略下进入状态分布，教师再对这些状态标注动作，Equation 2/8 的分布因此由学生 rollout 产生。可以把它类比成驾校教练不只给学生看标准路线录像，而是让学生自己开、偏离后再告诉他当前该怎么修正；这减少了部署时小误差滚成失控状态的 covariate shift（协变量偏移）。

第三层洞察是把“看得见什么”显式编码为 token mask。位置与旋转约束分别有掩码，未来时刻也带时间；文本、物体、地形、历史和当前姿态使用各自编码器。Transformer prior 只注意当前存在的条件，因此接口变化等价于 token 集合变化，不必更换策略结构。

第四层洞察是让训练期 encoder 看见完整目标，并把其均值建模成 prior 均值的残差。Equation 6–8 中，prior 只见部分目标，encoder 见完整未来，decoder 把 latent 变成动作；KL 项逐步收紧两者。训练结束后丢弃 encoder，只从 prior 取样。残差结构像老师在学生草稿上只写“还差多少”，而不是独立写另一份答案，使可部署 prior 更容易接近特权分布。

从工程接口看，遮挡不只是把输入清零，还必须同时告诉模型哪些信息原本不存在。否则零坐标可能被误解成“目标就在坐标原点”，缺失条件与真实数值会混为一谈。论文把数值、目标时刻和可见标记一起传入，因而上层可以明确表达“此处不约束”，而不必伪造一个占位目标。

## 方法主线

Stage 1 在 AMASS、HumanML3D 和 SAMP 聚合数据上训练完整约束教师。角色是中性 SMPL 体形、69 DoF；附录给出 358 维状态和 69 维 PD 目标动作。状态包含根高度/旋转、局部关节旋转与速度以及手脚位置；教师同时观察完整未来姿态、地形高度图和适用时的物体。奖励由全局关节位置/旋转、根高度、速度、角速度和能量项组成，论文明确不使用 residual force 或 residual control。

训练场景分成平地、包含楼梯/斜坡/粗糙表面的不规则地形和物体 playground。平地关节误差超过 0.25 m 早停，复杂地形阈值放宽到 0.5 m；困难动作按平地失败率提高采样概率，避免把本来就不适合上楼梯的空翻当成地形训练失败。

Stage 2 把教师蒸馏到 MaskedMimic。部分目标来自完整参考 `gfull` 经随机遮挡 `M` 得到 `gpartial`。可条件关节是左右脚踝、骨盆、头和左右手；位置与旋转可以独立出现。模型还接收当前姿态、16×16 且间隔 10 cm 的地形高度图，以及过去 40 个时刻中每隔 8 步抽取的一帧，共 5 帧历史。

论文使用 11 个未来姿态：前 10 个是连续近未来，第 11 个是随机远期目标。近未来 mask 以 98% 概率延续前一模式、2% 概率重采样；1% 概率产生 1–9 帧完全空白时间段，若存在文字、物体或远期目标则间隔乘 4。每个 episode 中物体有 20% 概率隐藏，文本有 80% 概率隐藏，远期姿态有 20% 概率出现。这个设计强迫模型同时遇到固定稀疏传感器、动作中间补帧和只有高层语义的情况。

prior 是 4 层、4 头、512 latent width、1024 feed-forward width 的 Transformer，输出 64 维高斯 latent；encoder/decoder 各是三层 1024 MLP。训练时 encoder 的后验均值等于 prior 均值加残差，KL 系数从 `0.0001` 线性升到 `0.01`。同一 episode 内重参数化噪声 `ε` 固定，避免每步随机采样把动作风格抖成白噪声。

论文在 Isaac Gym 中用 16,384 个并行环境、4 张 A100 训练约两周；教师/学生约 300/100 亿步。控制器 30 Hz，仿真 120 Hz。如此规模意味着“统一”减少的是任务专用模型和奖励工程，并不表示训练成本低。

## 关键图解

![Figure 3：完整教师、遮挡蒸馏与部分约束推理](assets/maskedmimic-2409.14393/figure-3-framework-05.jpg)

Figure 3 要按三条数据路径读。上层用完整目标和环境训练 `πFC`；中层让学生执行、教师给动作标签，再把目标遮成 `gpartial`；下层部署时只剩用户约束、环境和 `πPC`。这张图支持“任务接口统一”，却不说明学生可以脱离教师训练，也不说明任意约束都可行。

![Figure 5：learned prior、残差 encoder 与 decoder](assets/maskedmimic-2409.14393/figure-5-vae-08.jpg)

Figure 5 与 Equation 6–8 是机制核心。prior 只见可部署信息，encoder 额外见完整参考并给残差，decoder 接收当前状态和 latent 输出动作；推理时 encoder 被移除。若把 encoder 也带到部署端，复现得到的是特权 full-motion tracker，不是论文声称的 motion inpainting。

![Figure 6 / Table 1–2：全身与 VR 稀疏跟踪](assets/maskedmimic-2409.14393/figure-6-table-1-2-11.jpg)

Table 1 的 AMASS test 上，完整教师成功率 99.9%、MPJPE 31.3 mm，MaskedMimic 为 99.2%/35.1 mm，PULSE 为 97.1%/54.1 mm。Table 2 的平地 VR test 中，MaskedMimic 为 98.1%/58.1 mm，PULSE 为 93.4%/88.6 mm，ASE 和 CALM 的成功率分别为 37.6% 与 10.1%。这些数值说明统一学生没有因接口泛化完全丢掉跟踪能力；基线部分来自既有报告，不能当作所有方法在同一新代码栈中的重新训练。

![Figure 8 / Table 6：未见物体与结构消融](assets/maskedmimic-2409.14393/figure-8-table-6-14.jpg)

Table 6 在 5,000 个随机 episode 的未见坐具任务中报告完整模型 96.9% 成功、10.5 cm 误差；无历史为 94.9%，无 VAE 为 93.2%，无 residual prior 降到 21.1%，无 structured masking 则为 0%、274.4 cm。这是全文最能隔离机制的结果：决定跨接口泛化的不是仅仅扩大网络，而是让训练遮挡模式与真实欠约束持续时间匹配。

## 最有说服力的实验

最强证据是 Table 2、Table 4 和 Table 6 的组合。Table 2 测没有专门为 VR tracking 训练的统一模型，Table 4 把同一模型放到随机不规则地形，Table 6 再用组件消融解释为什么物体任务能工作。只看 Figure 1 的多任务拼图会得到“功能很多”的印象；三组表格共同回答的是“是否同一模型、是否跨环境、哪些设计不可删”。

Table 4 的 test 结果是：MaskedMimic 在不规则地形全身跟踪为 95.4%/62.9 mm，VR 为 93.6%/69.4 mm。它支持对训练分布内程序化地形的稳健性，不支持真实地形、感知噪声或机器人足地接触的迁移结论。

Table 5 的目标工程任务各评 5,000 个 episode：不规则地形 path-following 成功 96.3%、位置误差 12.5 cm，steering 成功 93.8%、速度误差 8.4 cm/s，reach 成功 87.3%、误差 21.7 cm。任务由人工有限状态机切换约束完成，因此结果证明“goal interface 可编程”，并不等同于策略自己完成了长时任务规划。

## 论文—代码映射

| 论文机制 | 固定提交符号 | 可核验范围 |
|---|---|---|
| 未来时刻与关节 mask | [`MaskedMimicControl._shift_and_sample_body_masks` / `_sample_body_masks`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/envs/control/masked_mimic_control.py) | 维护未来目标、位置/旋转可见性并按时序重复或重采样 |
| 部分目标上下文 | [`MaskedMimicControl.populate_context`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/envs/control/masked_mimic_control.py) | 在固定未来时刻查询 reference pose，并连同 masks/time offsets 写入环境上下文 |
| prior—residual encoder—decoder | [`MaskedMimicModel.forward`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/agents/supervised/masked_mimic_model.py) | prior 采样部署 latent，encoder 均值作为残差形成 privileged latent，两条路径共用 decoder |
| 推理与 KL | [`forward_inference` / `kl_loss` / `_kld_coefficient`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/agents/supervised/masked_mimic_model.py) | 推理移除 encoder，并显式计算高斯 KL 与课程系数 |
| 当前实验组合 | [`examples/experiments/masked_mimic/transformer.py`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/examples/experiments/masked_mimic/transformer.py) | 绑定 observation components、64 维 VAE 和 Transformer/MLP 模块 |

固定提交是 2025–2026 年重构后的 ProtoMotions 3，不是 2024 论文原始训练树。当前入口默认 5 个未来目标、mask 重复概率 0.8、KL schedule 500–2000 epoch，而论文是 11 个未来目标、98% 重复、3000 epoch 后用 6000 epoch 升 KL；公开入口也未显示论文完整的 XCLIP 文本与坐具 bounding-box 条件链。因此代码能够核验稀疏姿态补全和 VAE 机制，但不能直接复现 Table 1–6 的完整多模态系统。

## 局限与安全边界

作者明确列出三类局限。第一，生成动作会抖动，backflip 和 breakdance 等困难动作仍不能完整覆盖；第二，不规则地形上的脚步更多是把平地动作顺应到地面，而不是显式规划避开崎岖区域；第三，复杂场景仍需人工 goal-engineering，长指令如“走四步再举手”受短历史限制，动态物体、工具和多角色交互尚未解决。

独立判断还要加四条。所有定量结果来自单一仿真 SMPL 角色和 Isaac Gym；没有电机饱和、通信时延、状态估计漂移和真机跌倒统计。AMASS/HumanML3D/SAMP 的动作与文本覆盖决定 prior 的可行域，任意新文字并不等于可执行技能。以 prior 均值评测提高了稳定指标，却隐藏了随机取样的失败尾部。最后，5,000 episode 是仿真规模，不是跨场景、跨 seed、跨形体的完整安全证明。

MaskedMimic 的“物理合理”只表示动作通过论文仿真动力学执行，不等于符合机器人接触、力矩、速度、温度和自碰撞限制。将其迁移到人形机器人时，必须先有经验证的低层 tracker、姿态估计、接触监督、关节/力矩限幅、碰撞区、独立急停和安全停止状态；文字或关键帧不能直接绕过这些层发布到执行器。

## 可执行但有边界的结论

可复用的核心是“完整动作教师 + 结构化遮挡 + 学生分布 DAgger + learned-prior C-VAE”。它适合把多个稀疏控制接口收敛到同一个训练合同，特别适合关键帧补全、VR 头手输入和上层路径约束。真正要迁移的是表示和验收方法，不是直接复制论文的 SMPL 网络或奖励权重。

若目标是机器人 WBC，可先在统一低层 tracker 之上把 mask 作为 reference interface：每个约束明确关节、位置/旋转、目标时刻、容差与过期策略；未知区域由生成层补全，低层仍独立检查可达性和稳定性。这样，生成模型提出候选动作，安全控制器决定能否执行。

## 复现与验收清单

第一步固定论文与实现版本，分别记录 2024 论文配置和 ProtoMotions 3 当前配置。不要把 `num_masked_future_steps=5` 当成论文的 11，也不要把 `repeat_mask_probability=0.8` 写成 98%。至少做一组严格论文参数重建和一组当前代码默认值实验，结果分栏报告。

第二步先验收教师。按 AMASS train/test 分割报告成功率、MPJPE、早停原因和每类动作失败，不在教师尚不能稳定跟踪时训练学生。困难动作优先采样要只用平地失败率，避免把不可在楼梯上执行的动作错误标成需要加强的地形技能。

第三步单独验证 mask 采样器。对 10 个近未来和 1 个远期目标统计位置/旋转可见率、连续 mask run length、time-gap 分布、全隐藏比例，以及文本/物体存在时 gap ×4 是否成立。用固定种子构造 Figure 5 token mask，确保被遮 token 不能进入 attention。

第四步检查 DAgger 的数据归属：rollout 必须来自学生，动作标签来自冻结教师；日志要记录学生状态、完整目标、部分目标、教师动作和学生动作。只在教师轨迹上做离线回归会低估部署分布漂移，不能声称复现 Equation 2/8。

第五步复现 Table 1–4 时同时报告 success 和 error。成功阈值、平均误差、只对成功轨迹计算还是全轨迹计算都要写清；VR 既要报告观测关节 MPOJPE，也要报告不可见全身 MPJPE。对从其他论文引用的 PULSE/ASE/CALM 数值，注明是原报告还是在同一代码栈重训。

第六步复现 Table 6 的四个消融，并增加多个随机 seed。`no history`、`no VAE`、`no residual prior` 和 `no structured masking` 必须保持训练步数、数据和网络容量尽量一致。若无 structured masking 仍成功，应先检查每帧随机 mask 是否通过历史泄漏了完整动作。

第七步评估欠约束输出的分布，而不只跑 prior mean。对同一稀疏目标多次采样，报告成功率分位数、动作多样性、足滑、能量、抖动、自碰撞和失败模式；固定 episode 噪声与逐帧重采样分别对照。多样性增加却失败尾部变重时，部署要使用可行性筛选而不是任取样本。

第八步把 goal-engineering 与策略能力分开。公开每个任务的有限状态机、切换阈值、目标 horizon 和容差，特别是 path-following 中“离路径超过 0.4 m 时只给 0.8 s 远目标”的规则。若不公开这些外部逻辑，就无法判断成功来自模型还是手工状态机。

第九步在任何机器人试验前建立仿真到真机的独立安全门：用机器人真实 URDF、执行器和时延模型重定向动作；逐步扩大速度与关节范围；先悬吊/保护架，再软地面；每次试验保留急停人员、日志和停止条件。论文没有真机证据，因此不能从 Figure 1 的角色动画推导可直接上机。

> **金句**：统一控制器的关键不是“一个网络会所有任务”，而是把每种任务都改写成可审计的部分动作合同，再让生成层补全、让物理层否决。
