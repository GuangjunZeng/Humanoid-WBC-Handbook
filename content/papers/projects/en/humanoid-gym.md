# Humanoid-Gym: an Isaac Gym, MuJoCo, and XBot deployment baseline

[中文版](../humanoid-gym.md)

Reviewed snapshot: [roboterax/humanoid-gym@`ae46e201c85a2b17e7f2cea59a441dae7ea88a8f`](https://github.com/roboterax/humanoid-gym/tree/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f), 2,062 stars at the 2026-08-12 snapshot, BSD-3-Clause with inherited legged_gym, rsl_rl, and asset notices. Stars do not prove zero-shot sim-to-real success on every robot or terrain.

## Why it is included

Humanoid-Gym is a high-star classic in open humanoid locomotion. Derived from legged_gym and rsl_rl, it joins XBot-S/XBot-L Isaac Gym PPO training, observation history, domain randomization, rewards, termination, policy export, MuJoCo sim-to-sim, and hardware interfaces.

Its distinguishing value is using a second physics engine as a low-cost failure screen before hardware. This can catch observation and action ordering, PD decimation, model parameters, and termination mismatches. Passing sim-to-sim is still not equivalent to passing hardware acceptance.

## Problem addressed

Humanoid locomotion policies are sensitive to control frequency, history stacks, previous actions, attitude representations, foot contact, and PD gains. If export and deployment fail to preserve training defaults, a policy may work in one engine and immediately destabilize in another.

Humanoid-Gym makes 15 actor-history frames, three critic-history frames, policy/PD decimation, reward scales, randomization, and safety scales explicit in XBot configuration. These are auditable contracts, not parameters to copy blindly to a different embodiment.

## Architecture and data flow

The flow is `velocity command + proprioception/history → actor policy → target joint action → decimated PD control → Isaac Gym rollout → PPO update → export → MuJoCo sim-to-sim → XBot deployment`. The critic can use privileged state; the actor must remain restricted to deployable observations.

`LeggedRobot.step` executes several 1 ms physics steps per policy action. Policy frequency, PD frequency, and delay must be reported separately. The history buffer is stateful deployment logic; exporting only a neural network while changing buffer initialization or order is not equivalent to training.

## Code map

- [`XBotLCfg`](https://github.com/roboterax/humanoid-gym/blob/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f/humanoid/envs/xbot_l/xbot_l_config.py) defines `frame_stack`, `c_frame_stack`, `control.decimation`, rewards, randomization, and safety scales.
- [`LeggedRobot.step`](https://github.com/roboterax/humanoid-gym/blob/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f/humanoid/envs/base/legged_robot.py) executes decimated control, maintains history, and passes actions to simulation.
- [`LeggedRobot.check_termination`](https://github.com/roboterax/humanoid-gym/blob/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f/humanoid/envs/base/legged_robot.py) maps non-foot contact and other failures to resets; its meaning must align with MuJoCo and hardware fault categories.
- [MuJoCo deployment code](https://github.com/roboterax/humanoid-gym/blob/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f/deploy/deploy_mujoco/deploy_mujoco.py) is the second-engine entry point for checking observation, action, PD, and model mapping.

## Minimal reproduction path

Pin the commit, Isaac Gym, rsl_rl, CUDA, XBot assets, and one pretrained checkpoint. Replay a fixed initial state and velocity command in Isaac Gym. Export every observation slice, history frame, action, PD target, reward term, and termination reason.

Initialize MuJoCo with the same root pose, joints, previous action, and history. Compare the first 100, first 1,000, and full rollout for joint, root, and contact divergence. Inject mass, friction, delay, and sensor-noise changes and record the first source of divergence.

## Capability boundaries

The paper demonstrates XBot-S and XBot-L hardware but lacks large repeated success, fall, emergency-stop, and cross-engine-to-hardware correlation statistics. “Zero-shot” is bounded to its workflow and demonstrated hardware, not one-click transfer to arbitrary robots.

MuJoCo is a failure-screening layer, not a hardware substitute. Both engines can share the same incorrect URDF, torque limits, or actuator model, so agreement may simply reproduce the same error.

## Engineering assessment and risks

The reusable pattern is the training-to-second-engine-to-hardware gate. The main hazard is treating the second gate as certification. Classify failures as observation/action contract, engine physics, training-engine overfit, actuator/sensor mismatch, or out-of-distribution commands.

Hardware needs manufacturer limits, start-pose checks, communication timeouts, non-foot-contact and attitude protection, support or suspension, and a physical emergency stop. Paper gains and safety scales belong to its robot and cannot be copied directly elsewhere.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/roboterax/humanoid-gym/tree/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f)
- [XBot-L training contract](https://github.com/roboterax/humanoid-gym/blob/ae46e201c85a2b17e7f2cea59a441dae7ea88a8f/humanoid/envs/xbot_l/xbot_l_config.py)
- [English companion-paper deep read](../../en/humanoid-gym-2404.05695v2.md)
