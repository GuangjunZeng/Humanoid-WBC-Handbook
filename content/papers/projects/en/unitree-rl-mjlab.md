# Unitree RL Mjlab: lightweight MuJoCo/MJLab training and deployment validation

[中文版](../unitree-rl-mjlab.md)

Reviewed snapshot: [unitreerobotics/unitree_rl_mjlab@`1425b15f73bd4095f0df53709d7c389c3eb9e790`](https://github.com/unitreerobotics/unitree_rl_mjlab/tree/1425b15f73bd4095f0df53709d7c389c3eb9e790), 578 stars at the 2026-08-12 snapshot, Apache-2.0. Stars are discovery metadata, not confidence in simulator fidelity, policy quality, or hardware safety. No single paper corresponds to the whole repository.

## Why it is included

Unitree RL Mjlab is an official alternative engineering path. It preserves an Isaac Lab-like manager API while using MuJoCo and MuJoCo-Warp as the physics backend. It exposes multiple Unitree embodiments, velocity tracking, G1 imitation, ONNX export, and SDK2 deployment. This makes it valuable for controlled backend comparison with Unitree RL Lab rather than assuming one simulator is more realistic.

It belongs to locomotion and universal tracking. The project page clarifies where the “lightweight” path changes the stack and whether training, play, sim-to-sim, and hardware use the same contracts. Official ownership and stars do not replace contact, actuator, or real-world evaluation.

## Problem addressed

The Omniverse/PhysX stack is capable but can be expensive to install and run. Researchers may want a lighter MuJoCo route for rapid training, replay, and deployment checks. Mjlab organizes scenes, commands, observations, rewards, termination, and runners through explicit configurations and connects parallel learning to the Unitree C++ controller.

Motion imitation adds another conversion boundary. CSV is resampled into NPZ, `MotionCommand` advances a reference in time, and the task tracks joint and body state. The crucial engineering question is not whether PPO starts, but whether CSV, simulator state, ONNX input, and C++ observation preserve identical order, units, and frames.

## Architecture and data flow

The velocity path is `MJCF asset → VelocityEnvCfg → command/observation/reward/curriculum → RSL-RL runner → ONNX`. The tracking path is `CSV → csv_to_npz.py → MotionLoader/MotionCommand → TrackingEnvCfg → policy`. The play script reproduces checkpoints in MuJoCo, while deployment reads ONNX and YAML and sends joint commands through unitree_sdk2.

Many robot constants and XML assets are present, but each task still binds joints, actuators, and observations explicitly. MuJoCo-Warp increases parallel throughput; it does not guarantee numerical identity with CPU MuJoCo. GPU kernels, time step, contact solving, and rendering choices need versioned records.

## Code map

- [`MotionLoader` and `MotionCommand`](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/src/tasks/tracking/mdp/commands.py) load motion and generate references, temporal indices, and resampling state.
- [`TrackingEnvCfg`](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/src/tasks/tracking/tracking_env_cfg.py) composes tracking managers and simulation parameters.
- [Velocity rewards](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/src/tasks/velocity/mdp/rewards.py) expose the exact meaning of command tracking, gait, and regularization terms.
- [`scripts/train.py`](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/scripts/train.py) resolves tasks, distributed settings, logging, and the runner used for training.
- [`State_Mimic.cpp`](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/deploy/robots/g1/src/State_Mimic.cpp) is the G1 imitation runtime state in deployment.

## Minimal reproduction path

Pin Python, mjlab, MuJoCo/MuJoCo-Warp, RSL-RL, and the repository commit. Run `python scripts/train.py Unitree-G1-Flat --env.scene.num-envs=64` as a smoke test and save the fully resolved configuration. Convert the included G1 CSV to NPZ, verify input/output frame rate, root quaternion order, joint names, and first differences, and then start tracking with a small environment count.

Reproduce one checkpoint through `scripts/play.py`, integrated unitree_mujoco, and the deployment controller. Capture observations and actions at every layer for field-by-field comparison. Report velocity error, root height and orientation, foot slip, termination causes, NaN or saturation, and wall-clock training. A backend comparison must hold rewards, robot model, seed, and training budget fixed.

## Capability boundaries

The README lists Go2, A2, AS2, G1, R1, H1_2, and H2, but velocity, tracking, and hardware maturity are not necessarily equal for every robot. Example policies do not make newly trained policies safe. MJCF parameters may differ from a physical unit, particularly inertia, damping, friction, and collision geometry.

High parallel throughput does not establish determinism or physical equivalence. Dependencies and APIs evolve quickly, so commands and task names must be tied to commits. The hardware instructions enter debug mode and directly connect a control program, which is a separate high-risk operation rather than a normal continuation of training.

## Engineering assessment and risks

The strongest use is as a second official backend that isolates simulator dependence. If one control contract passes both backends but fails on hardware, investigation can focus on actuators, estimation, communication, and hardware. If the backends already disagree, resolve model and discretization differences before adding domain randomization or changing the policy.

Hardware use requires sim-to-sim, input/output equivalence, action limits, period and timeout tests, supported or suspended entry into debug mode, a physical emergency stop, conservative gains, speeds, and commands, plus torque and temperature monitoring. This page does not endorse copying README steps directly onto hardware and provides no safety parameters.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/unitreerobotics/unitree_rl_mjlab/tree/1425b15f73bd4095f0df53709d7c389c3eb9e790)
- [G1 asset constants](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/src/assets/robots/unitree_g1/g1_constants.py)
- [G1 deployment configuration](https://github.com/unitreerobotics/unitree_rl_mjlab/blob/1425b15f73bd4095f0df53709d7c389c3eb9e790/deploy/robots/g1/config/config.yaml)
