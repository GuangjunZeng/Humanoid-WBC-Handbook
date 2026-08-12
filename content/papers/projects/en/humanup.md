# HumanUP: a discover-then-track engineering pipeline for humanoid get-up

[中文版](../humanup.md)

Reviewed snapshot: [RunpeiDong/HumanUP@`7516e0f27e6f4d1e7365cf64ea577a78247bd8cb`](https://github.com/RunpeiDong/HumanUP/tree/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb), 231 stars at the 2026-08-12 snapshot, Apache-2.0. Stars are a discovery signal, not a get-up success rate, injury measure, or hardware safety rating.

## Why it is included

HumanUP provides an unusually inspectable recovery pipeline. A Stage I discovery policy searches for a fast get-up trajectory with simplified collisions and weaker regularization. A Stage II tracking policy then learns to follow that trajectory while adding joint, energy, action-change, and contact-related penalties that are closer to deployment needs.

This project review follows the boundary between those stages, the curricula that alter the training distribution, and the terms that remain optimization proxies rather than hard safety constraints. The separate paper review owns experimental interpretation and figure evidence. Neither repository popularity nor demonstration footage expands those claims.

## Problem addressed

Dense action penalties can prevent reinforcement learning from discovering a get-up maneuver. Optimizing only torso height can instead produce a shortcut with large impacts, frequent joint-limit use, or dependence on one initial pose. HumanUP separates finding a task-feasible path from learning a more controlled tracker, reducing conflict between exploration and regularization in one reward.

Trackability is not the same as safe recovery after any fall. Surface material, collision geometry, actuator temperature, battery state, payload, and the exact fall pose still matter. This repository is a research baseline, not a substitute for hardware fault detection or a functionally safe supervisory controller.

## Architecture and data flow

The main flow is `fixed supine/prone initialization → discovery rollout → standing and regularization curricula → discovered trajectory → interpolation → tracking policy → bounded joint targets`. Prone and supine recovery use separate policies or intermediate motion handling. Results from one initial-pose family must not be treated as universal fall recovery.

The discovery environment changes standing-sample probability and regularization strength as learning progresses. The tracking environment loads and interpolates the discovered motion while optimizing joint error, base attitude, torque, acceleration, action rate, and joint-bound terms. The reference trajectory is therefore a versioned input to Stage II, not an incidental file.

## Code map

- [`G1WaistRollHumanUP`](https://github.com/RunpeiDong/HumanUP/blob/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb/simulation/legged_gym/legged_gym/envs/g1waistroll/g1waistroll_up.py) implements discovery. `_update_standing_prob_curriculum`, `_update_regularization_scale_curriculum`, and `_reward_*` expose task and regularization schedules.
- [`G1WaistRollHumanUPCfg`](https://github.com/RunpeiDong/HumanUP/blob/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb/simulation/legged_gym/legged_gym/envs/g1waistroll/g1waistroll_up_config.py) pins observation, action, reward, randomization, and PPO settings for that stage.
- [`G1WaistRollTrack`](https://github.com/RunpeiDong/HumanUP/blob/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb/simulation/legged_gym/legged_gym/envs/g1rolltrack/g1waistroll_track.py) loads and interpolates discovery motion and implements joint tracking, base-attitude, torque, energy, and limit terms.
- [`G1WaistRollTrackCfg`](https://github.com/RunpeiDong/HumanUP/blob/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb/simulation/legged_gym/legged_gym/envs/g1rolltrack/g1waistroll_track_config.py) is the direct entry point for auditing contract changes between discovery and tracking.

## Minimal reproduction path

Pin the commit, Isaac Gym and CUDA versions, G1 URDF and collision geometry, initial-pose set, terrain, randomization, and seeds. Train supine discovery with a small parallel count first. Log root height and attitude, contacts, peak torque, standing probability, regularization scale, and termination reason for every episode. Use multiple seeds before accepting a discovered trajectory.

Freeze and identify that trajectory before passing it to tracking. Reproduce the single-stage, no-Stage-II, simplified-URDF, no-posture-randomization, and hard-symmetry comparisons. Report success together with pose coverage, get-up time, peak torque and power, contact impact, foot or knee slip, and categorized failures.

## Capability boundaries

The evidence covers the reported G1 model and pose distributions, not every fall, surface, or payload. Torque, joint-limit, and energy penalties in a reward are soft constraints. They are not actuator clamps, collision guarantees, or protective relays.

The public project is primarily a simulation and training stack. A policy that avoids simulation termination can still over-current, overheat, accumulate impact damage, or lose communication on hardware. Those conditions require an independent monitor and explicit fallback behavior.

## Engineering assessment and risks

The reusable idea is to relax exploration first and regularize a tracker second. The most dangerous misreading is to treat Stage II reward terms as safety proof. Trajectory, configuration, and checkpoint should be versioned as one acceptance unit, and every change should rerun the same gates.

Hardware evaluation must begin with passive collision checks and low-torque supported or suspended trials before increasing speed and pose coverage. It needs an independent emergency stop, current, temperature, and attitude limits, a padded landing area, an exclusion zone, and a dedicated safety operator. A timeout or untrusted state must enter a defined protective action rather than continue the learned motion.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/RunpeiDong/HumanUP/tree/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb)
- [Official training and deployment overview](https://github.com/RunpeiDong/HumanUP/blob/7516e0f27e6f4d1e7365cf64ea577a78247bd8cb/README.md)
- [English paper deep read](../../en/humanup-2502.12152.md)
