# 高减速比位置接口上的力矩控制：HRP-2 辨识、估计与逆动力学闭环

[English version](en/torque-control-high-ratio-gearboxes-2016.md)

来源：[HAL: hal-01136936](https://hal.science/hal-01136936) · [作者公开 PDF](https://homepages.laas.fr/ostasse/hugo/publication/journals/delprete-ijhr-2015/delprete-ijhr-2015.pdf) · [固定提交的 TSID 官方代码](https://github.com/stack-of-tasks/tsid/tree/eae96180ed8d289bc2c634f9d0857020ebfa6d90)

解读范围：完整 32 页论文、辨识推导、HRP-2 右腿六关节运动/受力实验与 TSID 任务空间逆动力学实现。论文的电机辨识脚本未随 TSID 一并公开，因此代码映射只覆盖上层 inverse-dynamics/HQP 部分，不伪造一一对应。

> 一句话总结：论文用腕/踝六维力传感器、IMU、编码器和刚体动力学估计关节力矩，再辨识“位置误差—力矩”的速度符号相关分段线性模型，把逆模型前馈与估计力矩反馈叠加；HRP-2 单腿楼梯轨迹在相同增益下误差更小、四分之一增益仍接近原位置控制，并能跟踪脚端正弦力，但结果依赖 F/T 传感器且只验证一条腿。

术语导航：高减速比齿轮箱（high-ratio gearbox）、关节力矩估计（joint-torque estimation）、六维力/力矩传感器（six-axis force/torque sensor, F/T sensor）、Savitzky–Golay 滤波（Savitzky–Golay filter）、逆执行器模型（inverse actuator model）、非对称惩罚辨识（asymmetric-penalty identification）、任务空间逆动力学（Task-Space Inverse Dynamics, TSID）与层级二次规划（Hierarchical Quadratic Programming, HQP）。

## 工程痛点

许多老式或高减速比 humanoid 只暴露关节位置命令，不能直接控制电流，也没有每个关节的力矩传感器。WBC 虽能算出期望关节力矩，接口却只接受位置误差。直接把力矩除以一个假设刚度换成位置偏置，忽略摩擦、低层死区、速度符号和内部控制器，容易跟踪差甚至不稳定。

可以把它理解成隔着一名未知驾驶员控制汽车：上层只能说“方向盘再向左一点”，不能直接给轮胎力；必须先用车辆响应辨识驾驶员怎样把指令变成力。另一个类比是称重：论文不是在每个关节放秤，而是从脚腕的总力、身体运动和动力学沿链条反推每个关节承担多少；任何模型或加速度误差都会进入这个估计。

## 核心洞察

HRP-2 有编码器、躯干 IMU 和腕/踝 F/T 传感器。作者用 Savitzky–Golay 从关节位置估计速度/加速度，补偿末端自身重力和惯性得到外力，再沿 floating-base dynamics 计算关节力矩。这里“without joint-torque sensors”不等于 without force sensors；四个六维 F/T 是估计可观测性的关键。

初始线性电机模型在数据上失败。位置误差与力矩关系有低层死区，并随关节速度正负切换。作者因此为正/负速度各拟合三段 affine 模型，辨识时使用非对称惩罚：过度补偿摩擦可能造成正反馈，代价高于不足补偿。最终控制输入是期望力矩经过逆模型得到的 feedforward position offset，加上估计力矩误差反馈。

## 方法主线

Equation 1 从 floating-base 方程把力矩写成 q、v、加速度与接触力的函数。关节微分滤波是有延迟的，基座角速度/加速度来自 IMU 与运动学；论文明确讨论传感器噪声、惯性参数和编码器离散误差。辨识保持关节静止并施加外力，不需高频激励，这是忽略齿轮弹性与电机电气极点换来的工程简化。

控制律把 inverse dynamics 期望力矩、摩擦前馈、位置反馈和力反馈组合成位置命令增量。上层 inverse dynamics 可加入脚端力任务，因此同一位置接口既做运动跟踪也做接触力跟踪。简化模型并非物理真值，而是稳定、易辨识且在当前频带有效的经验接口模型。

## 关键图解

![Figure 1：分段执行器模型](assets/torque-control-high-ratio-gearboxes-2016/figure-1-actuator-model.jpg)

Figure 1 显示膝关节的力矩—位置误差不是单线性，速度符号分组后才形成可拟合分支；非对称模型尽量避免蓝线给出比样本更激进的补偿。它是整篇论文最直接的“接口并非理想弹簧”证据。

![Figure 2 / Table 1：实验与参数](assets/torque-control-high-ratio-gearboxes-2016/figure-2-table-1-setup.jpg)

Figure 2 区分悬挂单腿运动实验与双足站立脚端力实验，Table 1 给出六个右腿关节辨识参数。悬挂减少未知接触，但也意味着运动结果不能代表全身行走接触切换。

![Figure 4：运动跟踪](assets/torque-control-high-ratio-gearboxes-2016/table-2-3-figure-4-motion.jpg)

Figure 4 对髋 roll 与踝 pitch 比较原位置控制、同增益力矩控制 K6=1、四分之一增益 K6=0.25。相同增益时误差显著下降，较低增益仍接近原控制，支持 feedforward 分担了反馈负担。

![Figure 5：脚端受力](assets/torque-control-high-ratio-gearboxes-2016/figure-5-force.jpg)

Figure 5 跟踪右脚 z 向正弦力。作者提高 force gain 直到观察到不稳定后取较低值，说明增益边界通过实机试验得到，而非理论保证；固定砖块接触也比真实地面切换简单。

## 最有说服力的实验

最强证据是运动跟踪的公平增益比较。论文不仅显示同增益误差更小，还把 torque controller 增益降到原来的 25%，误差仍相近；这比只给一个“最好调参”曲线更能证明模型前馈的贡献。Figure 6 进一步分解控制量，运动中摩擦前馈最大，受力中期望力矩前馈最大。

力跟踪实验说明位置接口上的 torque loop 能服务 contact task，但只在右脚、刚性固定物和有限频率下验证。它支持 proof of concept，不支持高速冲击、软地面、双脚切换或全身操作接触的稳定性结论。

## 论文—代码映射

固定 TSID 提交 `eae96180ed8d289bc2c634f9d0857020ebfa6d90` 中，`tsid::formulations::InverseDynamicsFormulationAccForce::computeProblemData` 组装运动任务、接触和动力学约束；`addMotionTask` 与 `addRigidContact` 对应论文上层任务/接触求解接口。`tsid::tasks::TaskSE3Equality::compute` 生成末端六维任务，`TaskActuationBounds::compute` 提供执行器边界。

需要明确：TSID 仓库是同一研究路线的上层开源库，并不包含论文 HRP-2 低层闭源位置控制器，也未发现完整分段电机辨识和六维传感器力矩估计脚本。因此复现者必须自行实现 estimator、piecewise inverse model 与 position-offset loop；不能只运行 TSID demo 就声称复现 Figure 4–5。

## 局限与工程判断

作者明确指出：分段模型来自主观观察，仍缺少未辨识项；估计和辨识有改善空间；当前模型只用于控制，未来可用于预测状态以补偿滤波延迟；可尝试 disturbance observer。论文也承认简化模型忽略齿轮弹性和电机极点，只在实验频带内证明合理。

独立工程局限包括：只测 HRP-2 右腿六关节；需要腕/踝 F/T、IMU 和较可信惯性参数；没有全身行走、接触切换、长时温漂和齿轮磨损统计；内部位置控制器闭源，固件改变会使辨识失效；悬挂轨迹和固定砖块不覆盖实际地面冲击。

硬件安全上，非对称辨识只是降低过补偿风险，不构成稳定性证明。开环逆模型、反馈增益和滤波延迟必须逐关节从低能量验证；F/T 饱和、IMU 异常、接触突变或 estimator 残差过大时应退回安全位置模式。高减速比机构可能积累弹性能量，不能用低频成功外推碰撞。

## 可执行但有边界的结论

这篇论文提供了“只有位置接口时如何接上 torque-level WBC”的工程桥梁：先确认可观测传感器，离线辨识实际低层映射，再用保守前馈加估计反馈。价值不在把位置控制伪装成理想力矩源，而在显式建模这个非理想接口并测量其边界。

对现代 G1/H1，若已有原生 torque/current 接口和关节力矩估计，应优先使用厂家可验证通道；若只能位置控制，可借鉴方法，但要重新辨识每个关节、温度、负载与速度分支。TSID 负责上层任务求解，actuator adapter 负责把期望力矩安全翻译到底层，二者应模块化隔离。

## 复现与验收清单

固定 HRP-2/目标机器人固件、齿比、采样频率、编码器、IMU、F/T 标定、惯性参数、Savitzky–Golay 窗口、分段阈值、非对称权重、反馈增益、参考轨迹和 TSID commit。复现 Figure 1、4、5 与 Tables 1–3，公开 estimator delay 和残差。

辨识数据应覆盖正/负速度、不同负载与温度，分训练/验证，检查单调性、连续性和过补偿比例。控制验收依次为离线回放、单关节悬挂、六关节悬挂、静态接触、低频力跟踪，再到多接触；每步有位置、速度、力矩估计、F/T、功率和急停门限。

运行时监控期望/估计力矩差、模型分支切换、滤波 age、F/T saturation 和 HQP feasibility。固件、润滑、减速器或 payload 改变后自动使辨识过期。把上层 TSID 输出与 actuator adapter 日志同时保存，才能区分任务求解错误和低层翻译错误。

## 进一步工程审计

这套接口像给每个关节安装一个“软件变速箱”：上层输出物理力矩，adapter 负责按当前速度分支、温度和估计反馈翻译成位置偏置。软件变速箱的输入输出、饱和、斜率和版本必须独立测试；若把它散落在 WBC 代码里，任何任务权重修改都可能掩盖低层模型错误。

分段模型在阈值附近可能抖动。速度估计含噪时 sign 会快速翻转，控制器在正负分支间跳变。实现应设置零速滞回、连续插值或状态机，并记录每秒分支切换数。静态摩擦区域尤其不能只用 sign(qdot) 决定，必要时保持上一个可信分支并限制位置增量变化率。

力矩估计还需要独立的静态和动态基线。静态多姿态下检查 gravity residual，缓慢运动检查速度/加速度项，高频运动检查滤波延迟；外力已知时比较 F/T propagation。若 estimator bias 与 actuator model 一起拟合，训练数据上会互相抵消，换姿态或负载后同时失效。

F/T 传感器位置决定可观测范围。末端传感器只能直接测到穿过该截面的外载，身体其他未建模接触会破坏反推；全身 WBC 中手扶墙、膝触地或躯干碰撞时必须更新接触集合。未知接触出现时暂停 force task 或降低增益，比让 estimator 强行解释成电机力矩更安全。

TSID 求解成功也不代表底层命令可实现。应在 HQP 后增加 adapter-aware feasibility：将候选力矩通过 inverse model 转成位置偏置，检查关节位置/速度、offset rate、预计电流和 branch validity。超限时向上层报告约束，而不是静默 clip；静默裁剪会破坏任务优先级并产生难以解释的接触误差。

温度和磨损应纳入重新辨识触发。摩擦随减速器温度、润滑和长期磨损变化，冷机参数可能在热机过度补偿。可以用低风险校准动作周期性估计 residual trend，一旦超过阈值使模型降级或过期。这样比等到力跟踪振荡再人工排查更可维护。

Handbook 对“无力矩接口如何做 WBC”的回答应明确分层：上层 TSID 生成一致的 task/contact torque，中层 estimator 提供可观测反馈，底层 adapter 翻译接口，安全层处理饱和和未知接触。缺少任一层，都不能用论文的 proof of concept 为系统背书。

验收报告还应给出频率范围。静态辨识和低频正弦受力通过，只说明该频带内模型可用；参考频率提高时，滤波相位、未建模弹性和内部电机动态会逐渐主导。逐级扫频时一旦相位裕度、估计残差或位置偏置超过门限，就把更高频率标成不支持，而不是继续加反馈增益追求曲线重合。

所有辨识结果应带采集日期、温度和硬件序列号，避免把另一台机器人或旧状态参数误装到当前关节。

> **工程判断**：“无关节力矩传感器”并非“无受力测量”；方法成立依赖末端 F/T、动力学估计和保守辨识，证明的是位置接口可被改造成有限频带的力矩控制通道。
