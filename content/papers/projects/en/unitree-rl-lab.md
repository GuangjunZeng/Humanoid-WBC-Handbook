# Unitree RL Lab: the official Isaac Lab-to-G1 deployment chain

[中文版](../unitree-rl-lab.md)

Reviewed snapshot: [unitreerobotics/unitree_rl_lab@`4960b84732b0c2ec593dccbfe963fda1bcd7b1e3`](https://github.com/unitreerobotics/unitree_rl_lab/tree/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3), 1,272 stars at the 2026-08-12 snapshot, Apache-2.0. Stars determine discovery priority only, not algorithmic confidence. The repository is not organized around one corresponding research paper.

## Why it is included

This official Unitree repository exposes reinforcement-learning environments for Go2, H1, and the 29-DoF G1, together with policy export, MuJoCo sim-to-sim, and C++ deployment interfaces. It covers the portion often missing from paper repositories: how an observation/action contract becomes ONNX and then enters an SDK2 control process.

It is relevant to locomotion and universal tracking because it contains velocity tracking and motion imitation. Official ownership and high stars justify early inspection, but they do not guarantee compatibility with every firmware version, robot batch, or site. This page reviews one pinned source snapshot rather than endorsing a default policy for hardware.

## Problem addressed

Humanoid RL reproduction often fails because assets, actuator models, observation order, action scaling, control periods, or deployment preprocessing differ, not because PPO equations changed. Unitree RL Lab places robot assets, Isaac Lab tasks, RSL-RL training, ONNX export, and SDK2 runtime code together so those contracts can be compared directly.

Velocity and mimic tasks share a manager-based framework but use different references and rewards. Mimic advances a motion in time and compares robot state to rigid-body and joint references. Velocity control responds to commands and terrain-oriented objectives. A common deployment executable does not make their failure modes or safety envelopes identical.

## Architecture and data flow

The training flow is `USD/URDF asset → RobotEnvCfg → Commands/Observations/Actions/Rewards/Events/Terminations → RSL-RL → checkpoint/ONNX`. In mimic tasks, `MotionLoader` reads a clip and `MotionCommand` maintains time, reference state, and adaptive sampling. Reward terms compare root, body, orientation, and velocity quantities.

The deployment flow is `ONNX plus deploy.yaml → State_RLBase/State_Mimic → observation assembly and normalization → policy inference → joint command → unitree_sdk2`. An FSM moves through passive or fixed-stand states before policy control. Running the same communication path against MuJoCo catches mapping and runtime errors, but cannot reproduce every actuator, battery, network, and floor condition.

## Code map

- [`MotionLoader` and `MotionCommand`](https://github.com/unitreerobotics/unitree_rl_lab/blob/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3/source/unitree_rl_lab/unitree_rl_lab/tasks/mimic/mdp/commands.py) manage motion data, reference state, time, and adaptive resampling.
- [Mimic reward terms](https://github.com/unitreerobotics/unitree_rl_lab/blob/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3/source/unitree_rl_lab/unitree_rl_lab/tasks/mimic/mdp/rewards.py) implement root, relative-body, orientation, and velocity errors.
- [`RobotEnvCfg`](https://github.com/unitreerobotics/unitree_rl_lab/blob/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3/source/unitree_rl_lab/unitree_rl_lab/tasks/mimic/robots/g1_29dof/gangnanm_style/tracking_env_cfg.py) composes G1 scene, action, observation, randomization, reward, and termination settings.
- [`State_Mimic.cpp`](https://github.com/unitreerobotics/unitree_rl_lab/blob/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3/deploy/robots/g1/src/State_Mimic.cpp) is the concrete runtime state through which the G1 mimic policy enters the deployment FSM.

## Minimal reproduction path

Pin Isaac Sim 5.1, Isaac Lab 2.3, and this repository commit. Download and hash the Unitree models, list tasks, and run a small-environment smoke test for `Unitree-G1-29dof-Velocity`. Log observation and action fields, units, decimation, and joint names. Preserve the full training configuration, seed, dependency commits, and ONNX export log.

Use staged acceptance: `Isaac Lab play → unitree_mujoco plus g1_ctrl → hardware`. Sim-to-sim must use the exact `deploy.yaml` and ONNX intended for the robot. Compare every observation field and one-step action between Python and C++, then test step commands, latency, and invalid inputs to verify FSM fallback, limits, and emergency-stop behavior.

## Capability boundaries

Listed robots and task names do not imply equal policy quality or hardware validation for every combination. GIFs are qualitative evidence and do not provide common success metrics or failure distributions. Models are external, and URDF versus USD import can change joints, inertias, and collision geometry.

Official organization ownership does not prove that a commit matches a user’s firmware. Deployment requires disabling the onboard controller, a high-risk state change. Network interface, Domain ID, elastic-hand setting, gamepad, and robot configuration must all be verified. Bundled ONNX Runtime and other third-party binaries also need license and platform review.

## Engineering assessment and risks

The repository is strongest as an official interface-alignment baseline: use it to verify Unitree assets, SDK2, joint order, and deployment FSM before comparing a research policy. Technical confidence must come from repeated runs under fixed configuration, not from the number of task names. Each checkpoint should have a machine-readable manifest binding task, asset, observation contract, action scale, commits, and firmware.

Before hardware use, commission in a supported or suspended configuration and verify passive, damping, stand, and policy states. Use conservative gains, speeds, and command envelopes with a physical emergency stop. Monitor position, velocity, torque, temperature, and communication timeout. Mapping or scaling errors can immediately create high-speed commands. This review supplies no deployment-ready parameters.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/unitreerobotics/unitree_rl_lab/tree/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3)
- [G1 deployment configuration](https://github.com/unitreerobotics/unitree_rl_lab/blob/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3/deploy/robots/g1/config/config.yaml)
- [Apache-2.0 license](https://github.com/unitreerobotics/unitree_rl_lab/blob/4960b84732b0c2ec593dccbfe963fda1bcd7b1e3/LICENSE)
