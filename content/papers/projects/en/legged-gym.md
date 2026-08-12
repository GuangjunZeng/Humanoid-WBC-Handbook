# legged_gym: the Isaac Gym environment base inherited by many humanoid RL projects

[中文版](../legged-gym.md)

Reviewed snapshot: [leggedrobotics/legged_gym@`8fa29acc6fd1910c3d9659eef6310bdd301cde0a`](https://github.com/leggedrobotics/legged_gym/tree/8fa29acc6fd1910c3d9659eef6310bdd301cde0a), 3,079 stars at the 2026-08-12 snapshot, BSD-3-Clause with separate licenses for bundled robot assets and dependencies. Stars indicate engineering influence, not humanoid adaptation completeness, sim-to-real success, or hardware safety.

## Why it is included

legged_gym is a code ancestor of many legged and humanoid reinforcement-learning projects. It combines vectorized Isaac Gym environments, action-to-PD or actuator-network conversion, observations, rewards, termination, terrain and command curricula, domain randomization, and policy export in inheritable base classes. Later systems including human2humanoid and Humanoid-Gym retain many of these contracts.

The official tasks in this pinned snapshot focus on ANYmal, A1, and Cassie rather than a finished modern humanoid stack. This review treats it as infrastructure. It explains what downstream humanoid repositories inherit without turning quadruped experiments into humanoid evidence.

## Problem addressed

The hard part of massively parallel locomotion RL is not only PPO. It is environment timing and scaling: how many physics steps execute per policy action, when observations refresh, whether timeouts count as terminal, whether reward scales are multiplied by `dt`, and when friction, mass, and push randomization are sampled.

legged_gym centralizes these rules in `LeggedRobot.step`, `post_physics_step`, nested configuration classes, and automatic reward discovery. The abstraction lowers the cost of adding an embodiment, but inherited defaults can silently change an experiment. A humanoid must redefine torso and arm behavior, self-collision, and non-foot contact rather than assume a quadruped contract.

## Architecture and data flow

The route is `task registry and robot configuration → vectorized Isaac Gym environments → observations and commands → external rsl_rl PPO → action clipping → decimated PD or actuator-network torque → physics → termination, reward, and reset → rollout`. Task classes inherit `LeggedRobot`; configuration classes inherit `LeggedRobotCfg` and `LeggedRobotCfgPPO`.

`step` loops over `control.decimation` physics updates for one policy action. `post_physics_step` checks termination, computes rewards, resets states, and then computes observations. `_prepare_reward_function` binds every nonzero config scale to `_reward_<name>`. A naming or inheritance error can therefore create a valid run that optimizes the wrong objective.

## Code map

- [`LeggedRobot.step` and `post_physics_step`](https://github.com/leggedrobotics/legged_gym/blob/8fa29acc6fd1910c3d9659eef6310bdd301cde0a/legged_gym/envs/base/legged_robot.py) define action clipping, decimation, torque, physics, reward, termination, reset, and observation order.
- [`LeggedRobotCfg`](https://github.com/leggedrobotics/legged_gym/blob/8fa29acc6fd1910c3d9659eef6310bdd301cde0a/legged_gym/envs/base/legged_robot_config.py) defines observation and privileged state, control, assets, randomization, rewards, and PPO defaults.
- [`_prepare_reward_function` and curriculum methods](https://github.com/leggedrobotics/legged_gym/blob/8fa29acc6fd1910c3d9659eef6310bdd301cde0a/legged_gym/envs/base/legged_robot.py) map nonzero scales to functions and change terrain or command difficulty.
- [`task_registry`](https://github.com/leggedrobotics/legged_gym/blob/8fa29acc6fd1910c3d9659eef6310bdd301cde0a/legged_gym/utils/task_registry.py) connects names, environment configuration, PPO configuration, creation, and training resumption.
- [`export_policy_as_jit`](https://github.com/leggedrobotics/legged_gym/blob/8fa29acc6fd1910c3d9659eef6310bdd301cde0a/legged_gym/utils/helpers.py) exposes feed-forward and recurrent export plus hidden-state reset.

## Minimal reproduction path

Pin Python 3.8, PyTorch 1.10 and CUDA 11.3, Isaac Gym Preview 3, rsl_rl v1.0.2, the commit, and robot assets. Begin with official `anymal_c_flat` to inspect the base contract. Record observation and action shapes, physics and policy `dt`, each reward term, termination cause, friction, mass, and push samples, and terrain level.

Add a humanoid through a new environment and configuration rather than changing shared defaults. Explicitly list joint order, default pose, PD and torque limits, foot and termination body names, contact sensing, privileged observations, and actor observations. Compare single-environment tensors before scaling to thousands of environments.

## Capability boundaries

The README says that environments migrated from Isaac Gym to Isaac Sim and this repository receives limited support; new applications are directed to Isaac Lab. This commit is therefore an anchor for historical reproduction and inherited contracts, not an automatic recommendation for a new stack.

Its Known Issues warn that `net_contact_force_tensor` is unreliable on GPU triangle-mesh terrain and suggest carefully placed force sensors. This directly affects humanoid termination, foot-air-time, and slip metrics. Ignoring it can corrupt both reward and evaluation.

## Engineering assessment and risks

The reusable elements are environment and configuration inheritance, dynamic reward binding, and centralized timing. The major risk is copying the base class without re-auditing observations, contact, and termination. Every fork should preserve a contract diff against this commit, not merely record PPO hyperparameters.

Hardware safety is outside the environment's guarantees. Deployment needs independent joint, torque, and velocity clamps, observation-order and scaling tests, communication timeouts, non-foot-contact and posture protection, support or suspension, and a physical emergency stop. Replay the full observation and action contract in a second engine before any low-energy hardware acceptance.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/leggedrobotics/legged_gym/tree/8fa29acc6fd1910c3d9659eef6310bdd301cde0a)
- [Architecture, migration notice, and Known Issues](https://github.com/leggedrobotics/legged_gym/blob/8fa29acc6fd1910c3d9659eef6310bdd301cde0a/README.md)
- [English paper deep read](../../en/learning-walk-2109.11978.md)
