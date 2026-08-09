# TextOp：把可随时修改的文字流变成连续人形运动

来源：[arXiv:2602.07439v1](https://arxiv.org/abs/2602.07439v1) · [固定提交官方代码](https://github.com/TeleHuman/TextOp/tree/ef6555fb174c9b5c44945a62c7ffc77b5ddbbf22)

解读范围：完整 20 页正文与附录。

## 方法主线

TextOp 的高层不是一次生成整段动作，而是每次用最近机器人骨架运动和当前文字生成短 horizon：BABEL/AMASS 先由 GMR 重定向并过滤到 G1，构成 83,478 个片段—文本对；Transformer VAE 编码未来运动，文本经 CLIP，扩散 Transformer 用 5 步去噪和 CFG=5 生成潜变量，再结合历史解码未来机器人关节/根运动。高层 6.25 Hz 在外部工作站运行。

低层 PPO 跟踪生成参考，50 Hz 在 29-DoF G1 机载计算机运行；训练数据同时含 MoCap 与生成运动，以降低生成器—跟踪器分布差。用户修改文字时只更新文本 embedding，后续块继续从最新历史自回归生成，因此无需中断控制器。

## 关键证据

- Figure 2/3：文字流—自回归生成—低层跟踪，以及文本/SMPL/机器人运动的时间对齐数据。
- Table I：30 秒实机流式命令中，随机组合 16/20 成功；循环 punch 与 guitar/violin 10/10，wave 8/10。失败标准是不能完成或触发安全终止，不等于语义完美。
- Table II：文本编码 7.64 ms、生成 29.63 ms、跟踪 2.15 ms；从键入到观察到机器人响应为 0.73±0.10 s（10 次人工感知测量）。
- Table III：机器人骨架表示在大多数片段/转换指标优于 DART+Retarget、BeyondMimic 表示、HumanML3D 和 RobotMDM；DART 重定向在部分转换平滑指标更好。
- Table IV/V：混合 MoCap+生成数据的 tracker 在生成分布上全局误差低于仅 MoCap；但未见 SnapMoGen 上仅 MoCap 反而泛化最好，说明生成增强有分布权衡。
- Appendix Table VI-X：2 帧历史、8 帧未来、5 diffusion steps、431/557 维跟踪观测和 200/50 Hz 仿真/策略频率。

最强证据是 Table I+II：真实 30 秒连续试验有明确分母，并把计算延迟与人感响应分开。它支持“可交互”，但 0.73 s 不是控制回路延迟，也不保证任意文字能生成安全动作。

## 论文—代码映射

| 组件 | 固定提交符号 | 对应关系 |
|---|---|---|
| CFG 去噪 | `ClassifierFreeWrapper`、`generate_next_motion` | 组合有/无文本条件扩散，输入文本 embedding 与历史，输出下一运动块 |
| 文本/历史条件 | `DenoiserTransformer.forward` / `mask_cond` | 嵌入扩散时刻、CLIP 文本、历史运动与噪声潜变量 |
| 在线生成 | `MotionDAR._gen_motion` / `_update_text_embedding` | 生成后保留尾部历史；键盘更新文字 embedding 而不重置整个执行链 |
| 发布节奏 | `MotionDAR.loop` / `_publish_motion_block` | 预生成未来块并通过 ROS 消息交给下层跟踪 |

官方仓库为 MIT，但 README 明确说“latest code and dataset are not yet updated”；固定提交是可查实现，不应假设与论文 v1 所有表格完全一致。

## 局限与安全边界

作者明确指出 TextOp 不感知环境几何，无法针对障碍、地形或动态物体改动作，未来需环境感知与交互规划。独立判断：CLIP/BABEL 词汇与私有少量数据限制开放文本；连续自回归可能积累漂移；随机组合 20 次仍属小样本；手动推扰只有定性展示；用户文字可能语义含糊或危险，系统没有文本级安全规划证明。

适合复用的是“流式短块生成 + 独立鲁棒 tracker + 生成分布增强”的架构。上线必须给命令白名单/拒绝逻辑、空间与速度限制、环境感知和低层安全监督，且把生成延迟、交互延迟、跟踪延迟分别监测。
