# HoloSoma: a multi-backend training framework for humanoid reinforcement learning

[中文版](../holosoma.md)

Reviewed snapshot: [amazon-far/holosoma@`6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3`](https://github.com/amazon-far/holosoma/tree/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3), 1,582 stars at the 2026-08-12 snapshot, Apache-2.0. Stars are used to discover high-signal repositories; they are not evidence of technical correctness, hardware success rate, or safety.

## Why it is included

HoloSoma puts locomotion, whole-body tracking, PPO, FastSAC, multiple simulation backends, and an inference/deployment boundary in one project. It is the current official recipe for *Learning Sim-to-Real Humanoid Locomotion in 15 Minutes* and also hosts work related to OmniRetarget. The project review asks what the current code actually provides, while the separate paper reviews bound experimental claims.

This page directly inspected the core training tree at the pinned commit. The official README lists Isaac Gym, Isaac Sim, MJWarp, and MuJoCo support. Multiple backends in one repository do not imply numerically identical semantics, and they do not prove that one checkpoint can move across backends or onto hardware without validation.

## Problem addressed

Humanoid RL systems often fail at the seams between environment wrappers, rewards, curricula, terminations, replay, and inference. A result that appears to be an algorithmic difference may actually come from action scaling, observation order, randomization, or a different done mask. HoloSoma makes many of those contracts explicit through configuration values, managers, and agents.

FastSAC addresses a narrower problem: retaining off-policy sample reuse in massively parallel environments without letting replay updates dominate wall-clock time. That is the engineering route behind the fifteen-minute result. The number remains specific to the paper's single-GPU locomotion setup and must not be generalized to every whole-body task.

## Architecture and data flow

The core flow is `task configuration → vectorized simulator environment → observation/action contract → replay buffer → FastSAC updates → policy checkpoint`. The `config_values/loco/g1/` package specifies G1 actions, commands, observations, rewards, randomization, curriculum, and termination. Managers combine individual terms into environment timing.

The agent collects transitions from parallel rollouts, stores them in replay, then updates critics and distributional targets before actor and entropy-temperature steps. A wrong shape, scale, or terminal flag can produce a run that optimizes the wrong task. PPO-versus-FastSAC comparisons therefore require an identical environment contract before comparing learning curves.

## Code map

- [`FastSACAgent`](https://github.com/amazon-far/holosoma/blob/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3/src/holosoma/holosoma/agents/fast_sac/fast_sac_agent.py) owns the main training state machine. `_update_main`, `_update_pol`, and `learn` expose value/distributional targets, policy/temperature updates, and the overall loop.
- [G1 locomotion reward configuration](https://github.com/amazon-far/holosoma/blob/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3/src/holosoma/holosoma/config_values/loco/g1/reward.py) is the first place to audit weights and term bindings.
- [Locomotion reward terms](https://github.com/amazon-far/holosoma/blob/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3/src/holosoma/holosoma/managers/reward/terms/locomotion.py) contain the actual computations needed to verify frames, reductions, and exponential scales.
- [`CurriculumManager`](https://github.com/amazon-far/holosoma/blob/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3/src/holosoma/holosoma/managers/curriculum/manager.py) and the [termination manager](https://github.com/amazon-far/holosoma/blob/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3/src/holosoma/holosoma/managers/termination/manager.py) determine how difficulty changes and which states end an episode.

## Minimal reproduction path

Do not start on hardware. Pin the commit, Python/CUDA/simulator versions, G1 assets, and one seed. Run the README FastSAC G1 locomotion command with a small environment count. Record observation names and shapes, action limits, each reward component, termination causes, replay size, and update-to-data ratio before scaling training.

Next increase the environment count and report wall-clock time, sample count, return, tracking error, foot slip, action saturation, and termination distribution across multiple seeds. A PPO comparison must hold the task contract and total environment interactions fixed, and report sample efficiency separately from wall-clock efficiency.

## Capability boundaries

This is a research framework, not a functionally certified robot product. Multiple backends still differ in contact, solvers, latency, and sensor-noise assumptions. A sim-to-real pipeline does not prove that default settings are safe for every G1 or T1.

The official repository overview includes training, retargeting, and deployment components. This page makes fine-grained claims only about the directly inspected core training tree. The existence of another component is not equivalent to a reproduction audit of every path.

## Engineering assessment and risks

The most reusable design is the auditable separation of rewards, curricula, and terminations. The common failure mode is copying a command while losing version, asset, embodiment, or calibration assumptions. Every trained checkpoint needs independent sim-to-sim, delay and packet-loss injection, observation-order tests, and limit checks.

Hardware use requires manufacturer limits, torque and velocity saturation, posture and contact protection, communication timeouts, a physical emergency stop, support or suspension, and staged relaxation. Neither a hardware video nor a high star count justifies skipping a robot-specific safety case.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/amazon-far/holosoma/tree/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3)
- [Official supported-scope and training commands](https://github.com/amazon-far/holosoma/blob/6e146b0af5d7cd8a39b8bb2ed05b977cf70445d3/README.md)
- [English paper deep read](../../en/fast-humanoid-locomotion-2512.01996.md)
