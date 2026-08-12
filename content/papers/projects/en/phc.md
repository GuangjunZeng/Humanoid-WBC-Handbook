# PHC: large-scale physics-based humanoid tracking and failure recovery

[中文版](../phc.md)

Reviewed snapshot: [ZhengyiLuo/PHC@`846988d433ce1f341e85ac6fbd2cd51911bb3341`](https://github.com/ZhengyiLuo/PHC/tree/846988d433ce1f341e85ac6fbd2cd51911bb3341), 1,275 stars at the 2026-08-12 snapshot. The repository contains a license, but SMPL/SMPL-X, AMASS, robot assets, data, and models require their own terms review. Stars do not prove easy reproduction, universal motion coverage, or hardware safety.

## Why it is included

Perpetual Humanoid Control (PHC) is a classic open implementation of large-scale physics-based motion tracking. It combines AMASS processing, SMPL/SMPL-X characters, reference states, imitation rewards, PMCP/PNN/MCP networks, a hard-sequence curriculum, and fall-state recovery in one repository.

The project continued to add PHC+, offline datasets, G1/H1 configurations, and an Isaac Lab inference example during 2024-2025, so current repository capability exceeds the 2023 paper snapshot. A separate project page distinguishes original paper claims from current engineering entry points and avoids rewriting the paper with later README numbers.

## Problem addressed

A controller for one reference clip is comparatively easy. Tens of thousands of motions, noisy references, and off-reference states create capacity, catastrophic-forgetting, and failure-data imbalance problems. PHC's progressive multiplicative control policy allocates new capacity to hard sequences and makes recovery a composable primitive.

The network is not the only difficulty. Motion FPS, root frame, joint mapping, initial-state sampling, termination thresholds, and the definition of “far from reference” decide which samples become failures. Tasks and Hydra configuration expose many of these decisions, while the README candidly states that full PHC training still requires many manual stages.

## Architecture and data flow

The main route is `AMASS/SMPL motion → preprocessing/retargeting → MotionLib reference → HumanoidIm observations and rewards → PNN primitives → hard-sequence fitting → MCP composition → fall-state recovery`. `run_hydra.py` combines robot, environment, learning, control, domain-randomization, and simulator settings.

`HumanoidIm` samples references and computes root, joint, rigid-body pose, and velocity errors. `HumanoidImGetup` adds fall/recovery episode state. PNN/MCP handles capacity expansion and primitive composition. A single primitive can track well, but the official README explicitly says it does not provide the full failure-state-recovery capability.

## Code map

- [`HumanoidIm`](https://github.com/ZhengyiLuo/PHC/blob/846988d433ce1f341e85ac6fbd2cd51911bb3341/phc/env/tasks/humanoid_im.py) is the reference-tracking task. `compute_imitation_reward` and `_compute_reset` in the same file expose reward and termination boundaries.
- [`HumanoidImGetup`](https://github.com/ZhengyiLuo/PHC/blob/846988d433ce1f341e85ac6fbd2cd51911bb3341/phc/env/tasks/humanoid_im_getup.py) uses `_reset_fall_episode` and `_compute_reset` to manage randomized falls, recovery windows, and resets.
- [`HumanoidImMCP`](https://github.com/ZhengyiLuo/PHC/blob/846988d433ce1f341e85ac6fbd2cd51911bb3341/phc/env/tasks/humanoid_im_mcp.py) composes trained primitives, while [`amp_network_pnn_builder.py`](https://github.com/ZhengyiLuo/PHC/blob/846988d433ce1f341e85ac6fbd2cd51911bb3341/phc/learning/amp_network_pnn_builder.py) constructs progressive networks.
- [The G1 PHC environment configuration](https://github.com/ZhengyiLuo/PHC/blob/846988d433ce1f341e85ac6fbd2cd51911bb3341/phc/data/cfg/env/env_im_g1_phc.yaml) connects the avatar method to a robot configuration. Its presence is not evidence that the 2023 paper performed a G1 hardware experiment.

## Minimal reproduction path

Pin the commit, Isaac Gym/CUDA/Python, SMPL assets, and motion licenses. Run the README's minimal viable evaluation on a sample motion and pretrained policy. Record motion keys, FPS, observation version, error components, termination causes, and fall/recovery flags instead of reporting only one success rate.

For training, validate the data contract with one primitive and a small motion set before the multi-stage PNN fitting and forward progression. Save the hard-sequence list and regression results on old clips every time capacity grows. Evaluate fall-only, far-only, and combined recovery separately so an average tracking score cannot hide recovery failure.

## Capability boundaries

The original PHC paper studies simulated avatars, not physical humanoid robots. Later G1/H1 and Isaac Lab paths do not change that evidence boundary. README values such as 98.9% or 100% refer to cleaned AMASS and specific current evaluation configurations, not arbitrary-input success rates.

Full PMCP training is not a single automated command. The official README says it requires repeated configuration changes and training phases. Reproduction should record every manual selection as an experimental parameter, otherwise two runs are not genuinely comparable.

## Engineering assessment and risks

The most reusable design is the explicit training state machine for hard-motion discovery, capacity expansion, and recovery data. The main interpretation risk is replacing a locked paper result with current README aggregate numbers, or reading avatar recovery as protective falling for a physical robot.

Hardware use of G1/H1 configurations requires an independent actuator model, action scaling, observation-order checks, latency analysis, joint and torque limits, self-collision protection, impact limits, communication timeouts, and an emergency stop. Use sim-to-sim and supported low-gain tests first. This page supplies no hardware parameters.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/ZhengyiLuo/PHC/tree/846988d433ce1f341e85ac6fbd2cd51911bb3341)
- [Official evaluation and training guide](https://github.com/ZhengyiLuo/PHC/blob/846988d433ce1f341e85ac6fbd2cd51911bb3341/README.MD)
- [English PHC paper deep read](../../en/phc-2305.06456.md)
