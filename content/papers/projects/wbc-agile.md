# WBC-AGILE：面向人形 RL 的环境验证—训练—评估—部署闭环

[English version](en/wbc-agile.md)

审阅快照：[nvidia-isaac/WBC-AGILE@`7259792cf10803aab814d101134d493d24c8f22f`](https://github.com/nvidia-isaac/WBC-AGILE/tree/7259792cf10803aab814d101134d493d24c8f22f) · 313 stars（2026-08-12 快照）· 大部分代码 Apache-2.0，RSL-RL 部分 BSD-3-Clause。对应论文：[AGILE, arXiv:2603.20147v1](https://arxiv.org/abs/2603.20147v1)。star 只是发现信号，不是可信度或安全认证。

## 为什么收录

候选初筛把它当作无论文项目，但官方仓库与 arXiv 已发布 AGILE 论文，本轮修正为官方论文代码。项目仍值得独立页，因为贡献重心是工程工作流：交互式验证、可复现训练、统一评估、descriptor 驱动部署和 sim2mujoco 回归，而不仅是一种策略网络。

它覆盖移动操作 WBC 与通用跟踪 topic，并包含站起、速度/高度跟踪、舞蹈和遥操作等任务。论文声称在 G1 与 Booster T1 上验证五类技能；项目页只说明代码如何组织证据，具体成功率与实验边界需在论文深读页结合图表核验。

## 它解决什么问题

人形 RL 代码常能在训练视频中工作，却缺少环境 sanity check、固定情景回归、随机 rollout 统计和可移植部署描述。策略一旦换本体或动作维度，observation、action、关节、归一化和部署端读取容易错位。AGILE 把策略生命周期拆成可检查阶段，并用 YAML descriptor 显式描述接口。

另一个问题是只在训练模拟器评估。AGILE 提供 sim2mujoco watcher 与统一指标，让 checkpoint 到达真机前经过第二物理后端。这个设计只能发现部分模拟器依赖，不能证明 sim-to-real；它的价值是尽早暴露错误并保存回归结果。

## 架构与数据流

主路径为 `task YAML/Python config → interactive play 验证 → scripts/train.py → checkpoint → scripts/eval.py 场景/随机评测 → IO descriptor 导出 → sim2mujoco → robot/task descriptor 部署`。teacher-student 路线先用 privileged observations 训练 teacher，再蒸馏 deployable student；两者的输入边界必须分别记录。

数据记录模块可把 observation/action 写入 HDF5，并转换为 GR00T 格式，形成上层模型与 WBC policy 的接口。它说明项目不只关心 locomotion，也关心任务条件控制；但录制与转换工具存在并不代表任意 VLA 输出都满足低层安全约束。

## 代码定位

- [`scripts/train.py`](https://github.com/nvidia-isaac/WBC-AGILE/blob/7259792cf10803aab814d101134d493d24c8f22f/scripts/train.py) 是配置、任务与 RSL-RL 训练的主入口。
- [`scripts/eval.py`](https://github.com/nvidia-isaac/WBC-AGILE/blob/7259792cf10803aab814d101134d493d24c8f22f/scripts/eval.py) 执行 checkpoint 加载、情景覆盖和统一评估。
- [`sim2mujoco_watcher.py`](https://github.com/nvidia-isaac/WBC-AGILE/blob/7259792cf10803aab814d101134d493d24c8f22f/scripts/sim2mujoco_watcher.py) 监控 checkpoint 并报告跌倒率、存活时间和速度跟踪误差。
- [`ActionProcessor`](https://github.com/nvidia-isaac/WBC-AGILE/blob/7259792cf10803aab814d101134d493d24c8f22f/agile/sim2mujoco/actions.py) 将 descriptor 中的动作项变成关节命令，是模拟器间接口的关键边界。
- [`HDF5DataRecorder`](https://github.com/nvidia-isaac/WBC-AGILE/blob/7259792cf10803aab814d101134d493d24c8f22f/scripts/data_recording/data_recorder.py) 负责多环境 episode 的 observation/action 记录。

## 最小复现路径

固定 Isaac Lab 2.3.2、Isaac Sim 5.1、资产和本页 commit。先用 `scripts/play.py` 的零动作、随机动作或正弦动作验证关节方向、限位和 reset；再以 README 的 `Velocity-T1-v0` 小环境训练。保存解析后的 env/agent 配置、seed、依赖 commit 与 checkpoint manifest。

运行 `scripts/eval.py` 的固定情景和随机 rollout，保存逐 episode 终止原因；导出 IO descriptor 后进入 `scripts/sim2mujoco_eval.py` 或 watcher，检查观察字段、归一化、action 处理与关节名是否一致。只有两套仿真都通过预定义阈值，才进入受控硬件 commissioning。

## 能力边界

工作流可移植性不等于策略跨本体零修改。每个本体仍需资产、执行器、奖励、descriptor 和部署适配。论文所列五类技能是特定配置的验证范围，不意味着仓库中的所有 task 或上层 GR00T 接口均有同等真机证据。

MuJoCo 评估与 Isaac Lab 共享部分描述符，但接触、执行器和传感器模型仍可能同时偏离真实硬件。teacher 的 privileged observation 不能泄漏到 student 部署输入；数据录制还需检查图像、状态、时间戳和任务文本是否同步。

## 工程判断与风险

AGILE 的最大价值是把回归评估提升为一等公民：checkpoint 不应凭一个视频发布，而应带固定场景、随机 rollout、sim2sim 和 IO contract 结果。项目采用单文件 task config 有利审计，但公共函数或底层依赖改变仍可能影响多个 task，需 CI 绑定完整依赖快照。

硬件上必须有 descriptor schema 校验、关节和单位核对、动作限幅、超时回退、急停、低增益/低速测试以及支撑或吊装。上层模型生成的任务或 action 不能绕过低层 safety layer。论文和视频不是安全认证，本页也不提供部署参数。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/nvidia-isaac/WBC-AGILE/tree/7259792cf10803aab814d101134d493d24c8f22f)
- [arXiv:2603.20147v1](https://arxiv.org/abs/2603.20147v1)
- [仓库许可证说明](https://github.com/nvidia-isaac/WBC-AGILE/blob/7259792cf10803aab814d101134d493d24c8f22f/LICENCE)
