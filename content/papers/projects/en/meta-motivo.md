# Meta Motivo: zero-shot behavioral foundation model code for a virtual humanoid

[中文版](../meta-motivo.md)

Reviewed snapshot: [facebookresearch/metamotivo@`ff8dcc55cf58f766d365ab0be23a021a7e34d53d`](https://github.com/facebookresearch/metamotivo/tree/ff8dcc55cf58f766d365ab0be23a021a7e34d53d), 778 stars at the 2026-08-12 snapshot, CC-BY-NC-4.0. Corresponding paper: [Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models, arXiv:2504.11054](https://arxiv.org/abs/2504.11054). Stars are discovery metadata, not scientific confidence or hardware-safety rating.

## Why it is included

Meta Motivo was initially classified as project-only, but the official citation and arXiv record identify its paper, so the catalog now marks it as official paper code. It represents a motion-generation route different from a per-motion tracker: it learns a forward-backward representation for the SMPL humanoid in HumEnv and conditions one policy on reward, goal, or tracking contexts.

A project page remains necessary because the repository exposes pretrained models, buffers, benchmark wrappers, and later FB-CPR training code. Readers must distinguish the paper method, inference supported by a particular release, and training code added later. This is not a Unitree-style hardware WBC and must not be reported as one merely because it controls a humanoid.

## Problem addressed

Task-specific RL retrains a policy whenever the reward or motion goal changes. Unsupervised zero-shot RL instead pretrains a conditional policy and adapts it through a latent context. Pure coverage objectives may visit many states without producing human-like behavior. Meta Motivo regularizes forward-backward representation learning with observation-only motion data so the policy’s behavioral support is better aligned with useful humanoid motion.

At runtime, a user infers latent `z` from a buffer and task definition, then calls `model.act(observation, z)`. Reward inference, goal inference, and tracking inference create context differently. Calling each a prompt should not hide its data, compute, and evaluation protocol.

## Architecture and data flow

The visible path is `HumEnv observation-only buffer → forward/backward encoders plus conditional policy → FB-CPR training → checkpoint → reward/goal/tracking context inference → model.act → HumEnv`. Separate `fb` and `fb_cpr` packages expose the base and regularized variants, and Hugging Face helpers load published models.

The benchmark wrapper adapts the model to HumEnv reward, goal, and tracking evaluations. Reward context can use many buffer samples, while tracking context is inferred from a next-observation trajectory. These protocols measure virtual-character state control. They contain no robot joint limits, actuator model, estimator, or sim-to-real layer.

## Code map

- [`metamotivo/fb_cpr/agent.py`](https://github.com/facebookresearch/metamotivo/blob/ff8dcc55cf58f766d365ab0be23a021a7e34d53d/metamotivo/fb_cpr/agent.py) organizes FB-CPR updates, contexts, and policy training.
- [`metamotivo/fb_cpr/model.py`](https://github.com/facebookresearch/metamotivo/blob/ff8dcc55cf58f766d365ab0be23a021a7e34d53d/metamotivo/fb_cpr/model.py) defines deployment-facing model components and the action interface.
- [`RewardWrapper`, `GoalWrapper`, and `TrackingWrapper`](https://github.com/facebookresearch/metamotivo/blob/ff8dcc55cf58f766d365ab0be23a021a7e34d53d/metamotivo/wrappers/humenvbench.py) connect latent inference to HumEnv benchmarks.
- [`ZBuffer`](https://github.com/facebookresearch/metamotivo/blob/ff8dcc55cf58f766d365ab0be23a021a7e34d53d/metamotivo/misc/zbuffer.py) manages latent/context samples used during search and reuse.
- [`FBcprModel.from_pretrained`](https://github.com/facebookresearch/metamotivo/blob/ff8dcc55cf58f766d365ab0be23a021a7e34d53d/metamotivo/fb_cpr/huggingface.py) is the compatibility boundary between a published model and repository code.

## Minimal reproduction path

Pin HumEnv, model release, inference buffer, repository commit, and seed. Load `facebook/metamotivo-S-1` on CPU, feed one fixed observation and latent, and retain the action as a smoke-test vector. Reproduce reward, goal, and tracking wrappers separately; do not combine their results under one zero-shot score.

Record context sample count, worker count, inference time, tasks, initial-state distribution, and episodes. Report mean, variance, failed tasks, and context-inference cost. Training reproduction must state whether it uses the later FB-CPR release or the original paper snapshot and retain data licenses and checkpoint hashes.

## Capability boundaries

The evaluated system is the HumEnv/SMPL virtual humanoid. It has no real-robot morphology retargeting, contact sensing, state estimation, joint-torque interface, or communication latency. Zero-shot means no downstream gradient training; it does not mean zero buffer, task definition, or context inference.

CC-BY-NC-4.0 is non-commercial and cannot be treated as a permissive software license. Models, data, and dependencies may have additional terms. Benchmark task coverage cannot be extrapolated to real terrain, manipulation, or high-dynamic sports.

## Engineering assessment and risks

Meta Motivo is a useful anchor for general behavioral representation and potentially an upper-level motion proposal system. Connecting it to a robot requires explicit retargeting, dynamic-feasibility checks, collision and contact constraints, a low-level controller, and new latency/frequency validation. Latent controllability does not prove every interpolated context has stable semantics.

HumEnv rendering is not hardware evidence. Real-robot experiments require a separate tracker or WBC, limits, conservative gains, support or suspension, an emergency stop, and per-motion review. High stars and the “foundation model” label do not replace a safety case. This page provides no deployment parameters.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/facebookresearch/metamotivo/tree/ff8dcc55cf58f766d365ab0be23a021a7e34d53d)
- [arXiv:2504.11054](https://arxiv.org/abs/2504.11054)
- [CC-BY-NC-4.0 license](https://github.com/facebookresearch/metamotivo/blob/ff8dcc55cf58f766d365ab0be23a021a7e34d53d/LICENSE)
