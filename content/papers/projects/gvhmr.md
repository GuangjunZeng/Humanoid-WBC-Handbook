# GVHMR：从移动相机视频恢复世界坐标人体运动的数据入口

[English version](en/gvhmr.md)

审阅快照：[zju3dv/GVHMR@`6ec3ca39336c50492c0fae65fba2fb831fc7d866`](https://github.com/zju3dv/GVHMR/tree/6ec3ca39336c50492c0fae65fba2fb831fc7d866) · 1840 stars（2026-08-12 快照）· 自定义非商业研究许可，修改版需开源，商业使用需联系权利人。star 只是发现信号，不是世界轨迹精度、机器人可执行性或真机安全信心。

## 为什么收录

GVHMR 是 WBC 动作数据上游的代表工程：它从单目视频推理 SMPL 人体姿态、尺度、根朝向和世界平移，并用 gravity-view coordinates（重力—视角坐标）分离摄像机旋转与人体全局运动。对从网络视频或现场相机构造人形训练动作的团队，它是比“手工抽几个二维关键点”更完整的输入层。

独立项目页不重复论文表格，而是说清整条视频预处理、视觉里程计、网络、坐标解码与后处理如何组成。这很重要，因为网络前向只占全链路一部分，不能用单模块速度代替端到端吞吐。

## 它解决什么问题

移动摄像机下，画面中的人体位移是人在动与相机在动的混合。只在相机坐标回归姿态，可以得到局部看起来正确、但长序列朝向漂移或根轨迹不可用的结果。GVHMR 把二维关键点、图像特征、相机角速度与全图相机参数合并，在重力对齐表示中预测并再组成世界运动。

但它输出的仍是人体 SMPL 运动，不是机器人 qpos，更不是满足接触、摩擦、自碰撞和力矩限制的控制命令。要进入 WBC，还必须通过动作重定向、接触修正、动力学跟踪和物理验收。

## 架构与数据流

主链可写为 `video → person tracking / 2D pose / image feature → camera motion or static-camera flag → GVHMR temporal network → encoded body/root/camera quantities → world-coordinate decoding → static-joint and IK postprocess → SMPL motion`。演示脚本允许静态相机跳过 VO，动态相机则依赖 DPVO 或后续 SimpleVO 路径。

`NetworkEncoderRoPE` 将 17 个带可见性的二维关键点、CLIFF camera、camera angular velocity 和可选图像特征投影到时序 token，再输出身体、相机和静态可信度。`EnDecoder` 和 `hmr_global.py` 负责标准化表示与世界坐标转换；静态关节后处理是可选改良，不应与原始网络输出混在一个指标中。

## 代码定位

- [`Pipeline.forward`](https://github.com/zju3dv/GVHMR/blob/6ec3ca39336c50492c0fae65fba2fb831fc7d866/hmr4d/model/gvhmr/pipeline/gvhmr_pipeline.py) 组合观测编码、时序网络、身体/根解码与可选后处理，是整体契约入口。
- [`NetworkEncoderRoPE.forward`](https://github.com/zju3dv/GVHMR/blob/6ec3ca39336c50492c0fae65fba2fb831fc7d866/hmr4d/network/gvhmr/relative_transformer.py) 处理关键点可见性、相机条件、图像特征和长序列注意力窗。
- [`get_R_c2gv` 与局部速度 rollout](https://github.com/zju3dv/GVHMR/blob/6ec3ca39336c50492c0fae65fba2fb831fc7d866/hmr4d/utils/geo/hmr_global.py) 明确重力—视角坐标和全局平移的组成。
- [`DemoPL.predict`](https://github.com/zju3dv/GVHMR/blob/6ec3ca39336c50492c0fae65fba2fb831fc7d866/hmr4d/model/gvhmr/gvhmr_pl_demo.py) 将预处理数据送入 pipeline，并显式传递 `static_cam`。

## 最小复现路径

固定 commit、checkpoint、SMPL 模型、检测/姿态/特征模型、VO 后端、焦距和视频解码版本。先用官方 tennis 视频分别跑静态相机和动态相机路径，保存人框、二维关键点、图像特征、相机轨迹、SMPL 参数和后处理前后结果。

然后选用 RICH/EMDB 的官方评测入口，分开报告局部姿态、全局朝向、根轨迹和脚滑相关指标。吞吐要同时给出整条预处理时间与网络时间。输入 WBC 前，对参考动作做失联、遮挡、快速摄像机旋转和低焦距故障注入。

## 能力边界

GVHMR 不保证绝对公制尺度、无漂移世界轨迹或正确接触标签。遮挡、镜面、动态背景、运动模糊、焦距误设与 VO 失效都可能让长序列坐标失真。开源许可为非商业研究限定，不能当作宽松开源许可。

对人形控制而言，这是人体运动估计器，不是 retargeter、motion filter 或 policy。即使输出动画看起来流畅，也不证明关节可达、脚底不滑、质心稳定或力矩可行。

## 工程判断与风险

最值得复用的是把重力方向与相机视角组成明确坐标契约，并为静态相机和动态相机提供不同入口。最容易误用的是只保存最终 SMPL 文件，丢掉二维检测、相机轨迹和后处理标志，导致后续脚滑时无法追回误差来源。

从 GVHMR 到真机必须有三道门：输入质量与坐标审计；机器人重定向、接触/自碰撞/关节界限审计；仿真跟踪、动力学与安全限幅审计。只有视频可视化不得直接生成硬件命令。

## 一手来源

- [固定 commit 的官方仓库](https://github.com/zju3dv/GVHMR/tree/6ec3ca39336c50492c0fae65fba2fb831fc7d866)
- [官方许可边界](https://github.com/zju3dv/GVHMR/blob/6ec3ca39336c50492c0fae65fba2fb831fc7d866/LICENSE)
- [对应论文的中文深读](../gvhmr-2409.06662.md)
