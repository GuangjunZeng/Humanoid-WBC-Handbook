# SOMA Retargeter：可审计的 BVH→G1 运动重定向流水线

[English version](en/soma-retargeter.md)

审阅快照：[NVIDIA/soma-retargeter@`b3ef2708d84bfd1314ddb52d0db6c9c211df1f57`](https://github.com/NVIDIA/soma-retargeter/tree/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57) · 526 stars（2026-08-12 快照）· Apache-2.0。star 只用于发现候选，不代表技术可信度或实机安全等级。

## 为什么收录

SOMA Retargeter 没有用一篇对应论文包装结论，但它把动作数据工程里常被藏在脚本中的环节做成了相对清楚的库：输入 SOMA 骨架的 BVH，经过比例缩放、多目标逆运动学（multi-objective inverse kinematics, IK）、足部稳定和关节限位，输出 Unitree G1 29-DoF CSV。它适合训练数据与重定向 topic，因为读者可以追踪每一步如何改写轨迹，而不是只看最终视频。

本页把仓库当前实现与科学结论分开。项目自带 10 组样例和无界面批处理入口，足以检查接口和数值连续性；但仓库没有给出跨方法受控实验，也没有证明输出轨迹在动力学上可执行。高 star 说明社区关注度，不把它升级为论文证据。

## 它解决什么问题

人体骨架与机器人在连杆长度、关节轴、自由度和可达空间上不同。直接复制姿态会产生关节越限、脚底漂移和世界坐标错位；逐帧 IK 即使能收敛，也可能在时间上跳变。这个项目的工程目标是把“读取、对齐、求解、稳定、限幅、导出”串成可批处理的数据入口，并让 GUI 与 headless 模式使用同一条流水线。

它特别处理两类容易污染下游 tracker 的问题。其一是脚在应接触地面时上下浮动；其二是求解器给出的关节坐标超出模型边界。这里的足部稳定（feet stabilization）与关节限位钳制（joint-limit clamping）是数据门禁，不是动力学控制器，也不能替代碰撞、速度和力矩检查。

## 架构与数据流

主路径是 `BVH → AnimationBuffer → 人体/机器人比例映射 → Newton/Warp 批量 IK → FeetStabilizer → JointLimitClamper → G1 CSV`。`app/bvh_to_csv_converter.py` 同时组织交互查看器和目录批处理；配置文件决定导入目录、目标本体、缩放与足部参数。源动画和机器人状态在播放器中并排更新，因此单帧错位与时间连续性可以直接目检。

核心求解建立在 Newton 与 NVIDIA Warp 上，适合把多帧或多环境并行处理。`FeetStabilizer` 使用两骨骼 IK 和配置化目标修正下肢，`JointLimitClamper` 则在每个自由度上执行最后边界约束。顺序很重要：若先硬裁剪再稳定脚，末端目标可能被再次破坏；但当前顺序仍不能保证脚底无滑移或无自碰撞。

## 代码定位

- [`Viewer.batched_retargeting` 与 `Viewer.retarget_motion`](https://github.com/NVIDIA/soma-retargeter/blob/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57/app/bvh_to_csv_converter.py) 是批处理与单段处理的入口，决定输入输出如何进入同一流水线。
- [`FeetStabilizer.solve`](https://github.com/NVIDIA/soma-retargeter/blob/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57/soma_retargeter/pipelines/feet_stabilizer.py) 构造和求解足部目标，暴露了状态复位与批量环境语义。
- [`JointLimitClamper.apply`](https://github.com/NVIDIA/soma-retargeter/blob/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57/soma_retargeter/pipelines/joint_limit_clamper.py) 把模型的自由度上下限落实到输出关节坐标。
- [`IKSmoothJointFilter`](https://github.com/NVIDIA/soma-retargeter/blob/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57/soma_retargeter/pipelines/ik_objectives.py) 说明求解目标不仅追末端，还包含关节平滑项。

## 最小复现路径

在 Python 3.12、NVIDIA 驱动 545+ 和 Git LFS 完整下载资产的环境中固定上述 commit，使用仓库默认配置先运行一个自带 BVH：`python app/bvh_to_csv_converter.py --config assets/default_bvh_to_csv_converter_config.json --viewer gl`。保存 CSV 后，再以 `--viewer null` 对同一目录批处理，比较交互与 headless 输出哈希和帧数。

验收至少记录：输入 BVH 与配置哈希、输出 FPS/帧数、关节位置和一阶差分峰值、脚底最低高度、接触阶段水平滑移、自碰撞以及越限计数。只看“成功导出”不够；再把 CSV 在独立仿真器中以低增益回放，确认坐标系、关节顺序与时间步一致，然后才允许进入策略训练。

## 能力边界

审阅 commit 明确支持 SOMA 输入骨架与 G1 29-DoF 输出，其他输入骨架和机器人只是规划方向，不能从模块化接口推断为已支持。GPU、Newton/Warp、驱动和 LFS 资产形成较重的环境依赖；批处理吞吐量也没有在仓库中给出可复核基准。

输出是运动学轨迹，不包含接触力、力矩、执行器延迟或稳定裕度。足部稳定不等于物理接触一致，关节位置在限位内也不等于速度、加速度与电流可接受。SEED 数据集中的使用案例是生态关联，不是本项目对全部数据的质量担保。

## 工程判断与风险

这个项目最有价值的地方是可把重定向分解为若干可测步骤，适合作为数据管线基线；最薄弱的地方是缺乏受控的下游跟踪对照和真机安全评测。实际采用时应增加跨帧连续性、自碰撞、脚滑和初始姿态可达性门禁，并保存失败样本，而不是只导出漂亮动作。

任何真机回放都必须经过独立仿真、速度/加速度/力矩限制、低增益和低速调试、支撑或吊装、急停与机器人专用关节映射审查。本页不提供可直接上机的参数；仓库演示也不构成硬件安全证明。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/NVIDIA/soma-retargeter/tree/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57)
- [Apache-2.0 许可证](https://github.com/NVIDIA/soma-retargeter/blob/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57/LICENSE)
- [默认转换配置](https://github.com/NVIDIA/soma-retargeter/blob/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57/assets/default_bvh_to_csv_converter_config.json)
