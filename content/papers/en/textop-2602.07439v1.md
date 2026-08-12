# TextOp: Turning an Editable Text Stream into Continuous Humanoid Motion

[中文版](../textop-2602.07439v1.md)

Sources: [arXiv:2602.07439v1](https://arxiv.org/abs/2602.07439v1) · [version-pinned official code](https://github.com/TeleHuman/TextOp/tree/ef6555fb174c9b5c44945a62c7ffc77b5ddbbf22)

Review scope: the complete 20-page paper and appendix, plus the official code at the pinned commit.

> In one sentence: TextOp repeatedly generates short G1-skeleton motion chunks from current text and recent motion history, while a separately trained tracker closes the physical loop on a mixture of MoCap and generated references.

Key terms are streaming text control (流式文字控制), motion chunk (动作块), diffusion Transformer (扩散 Transformer), classifier-free guidance (CFG，分类器免引导), autoregressive history (自回归历史), robot-skeleton representation (机器人骨架表示), distribution augmentation (分布增强), and hierarchical decoupling (上下层解耦).

## Engineering problem

Conventional text-to-motion accepts one sentence and generates a complete human clip. If a robot executing that clip receives “now wave,” regenerating an entire sequence loses the current phase, while splicing clips creates root, support-foot, and joint-velocity discontinuities. Text-conditioned generation is not yet continuous hardware control.

TextOp behaves like an actor taking live direction: each generation covers only a short future but must remember the current performance. Recent robot-skeleton frames preserve physical phase while text embedding can change. This separates what the user wants from where the robot currently is.

Generated human motion is also outside the distribution of many trackers. Even after GMR retargeting, transition frequency and artifacts differ from MoCap. Mixing generated references into tracker training is an interface adaptation rather than a guarantee of universal generalization.

## Core insight

Text updates do not reset generation state. The semantic condition changes, while recent robot motion remains the autoregressive anchor. Short chunks bound the effect of each edit and allow the low-level controller to continue operating during high-level generation.

Generating directly in a robot-skeleton representation removes a second post-generation retargeting distribution shift. It still does not make references physically feasible; the 50 Hz closed-loop tracker is what converts reference motion into joint targets on hardware.

Generated-data augmentation has a tradeoff. Tables IV–V show mixed MoCap/generated training helps on the generator's distribution, while MoCap-only can generalize better to unseen SnapMoGen. This is an important negative result against the assumption that more generated data monotonically improves all distributions.

## Method: input → processing → output

BABEL/AMASS is retargeted and filtered to G1, producing 83,478 motion-text pairs. A Transformer VAE encodes future motion; CLIP encodes text; a diffusion Transformer uses five denoising steps and CFG=5 to generate a latent, conditioned on recent robot motion. The high level runs at 6.25 Hz on an external workstation.

A PPO tracker runs at 50 Hz on the 29-DoF G1 onboard computer and tracks reference chunks. Its training mixture contains MoCap and generated motions. On text edit, only the text embedding is updated; the next chunk continues from latest history and no low-level reset is required.

There are at least three separate clocks: user text events, high-level chunk generation, and low-level tracking. Denoising steps are numerical iterations inside one generation call, not control cycles.

## How to read the key figures

![Figures 2–3: streaming generation, aligned data, and low-level tracking](../assets/textop-2602.07439v1/figure-2-streaming.jpg)

Figures 2–3 separate the three clocks and data representations. Chunk lookahead prevents high-level compute jitter from directly becoming joint jitter, while the tracker maintains physical feedback between publications. The figure does not show environment geometry or a planner that judges textual safety.

![Tables I–II: 30-second hardware streams and latency decomposition](../assets/textop-2602.07439v1/table-1-2-hardware.jpg)

Table I reports 30-second streaming trials: 16/20 for random combinations, 10/10 for repeating punch and guitar/violin, and 8/10 for wave. Table II separates text encoding 7.64 ms, generation 29.63 ms, and tracking 2.15 ms from perceived type-to-response latency of 0.73±0.10 s across ten human observations. The latter is interaction latency, not a low-level control-loop delay.

![Tables III–IV: representation and tracker distribution](../assets/textop-2602.07439v1/table-3-4-representation.jpg)

Table III compares robot-skeleton representation with DART+retargeting and other representations; the direct representation wins most clip/transition metrics, while DART is stronger on selected transition smoothness. Tables IV–V reveal the training-distribution tradeoff: mixed data improves generated references, but MoCap-only can be best on an unseen generator.

## Strongest experiment

Tables I–II are the strongest closed-loop evidence because they provide trial denominators and a timing decomposition. Random combination success of 16/20 shows switching remains harder than stable cyclic behaviors, while the latency table indicates where interaction delay occurs.

Thirty seconds is not a long-duration guarantee. Autoregressive root or phase drift may emerge over minutes, and cyclic actions can hide accumulated errors. Reproduction should add multi-minute streams, frequent semantic reversals, and a commanded return to a stable stationary state.

## Paper-to-code mapping

- `ClassifierFreeWrapper` and `generate_next_motion` combine conditional/unconditional diffusion with text embedding and motion history to output a new chunk.
- `DenoiserTransformer.forward` and `mask_cond` embed diffusion time, CLIP text, history, and noisy latent motion.
- `MotionDAR._gen_motion` and `_update_text_embedding` preserve tail history while updating text without resetting execution.
- `MotionDAR.loop` and `_publish_motion_block` schedule lookahead chunks and publish them through ROS to the tracker.

The [pinned official repository](https://github.com/TeleHuman/TextOp/tree/ef6555fb174c9b5c44945a62c7ffc77b5ddbbf22) is MIT licensed, but its README says the latest code and dataset are not yet updated. File-level evidence must not be assumed to reproduce every paper-v1 table exactly.

## Limitations and safety boundary

The authors explicitly state that TextOp lacks environment geometry and cannot adapt motions to obstacles, terrain, or dynamic objects. Independent limits are CLIP/BABEL vocabulary coverage, private supplemental data, autoregressive drift, small streaming trial counts, qualitative push robustness, ambiguous or dangerous text, and no formal text-level safety planner.

“Turn quickly” omits direction, angle, free space, and stopping condition. A likely semantic completion can still be physically unsafe. Text semantics, tracker feasibility, and environmental safety must be independent acceptance axes.

Hardware deployment needs an allowed-command compiler, amplitude/speed/space/deadline limits, environment sensing, collision and joint supervision, timeouts, a safe-stop state, and emergency stop. Language must never bypass those layers.

## Bounded engineering takeaway

Reuse streaming short-chunk generation plus a separately validated tracker and distribution-aware tracker training. Evaluate cyclic motion, related semantic switches, support-conflicting switches, long autoregression, and unseen generators. Report semantic match, tracking termination, and safety rejection separately.

## Reproduction and acceptance checklist

Record counts and removals through raw BABEL/AMASS, text labels, GMR retargeting, quality filtering, and final pairs. Timestamp text submission, embedding update, denoising, block publication, tracker receipt, and first visible response; report tail latency, queue depth, expiry, and loss. Test walk→fast-walk, walk→wave, and forward→backward switches for root, support, velocity, semantics, and termination. Compare MoCap-only, generated-only, and mixed trackers under equal sample and training budgets on MoCap, seen-generator, and unseen-generator sets. Unknown, ambiguous, negated, or spatially constrained text must produce uncertainty or rejection rather than a plausible but unsafe motion.
