# KungFuAthleteBot: an open chain from high-dynamic martial-arts data to tracking and recovery

[中文版](../kungfu-athlete-bot.md)

Reviewed snapshot: [NPCLEI/KungFuAthleteBot@`1e3f207013245a5a0db75e6f70e1cdf762e28e9c`](https://github.com/NPCLEI/KungFuAthleteBot/tree/1e3f207013245a5a0db75e6f70e1cdf762e28e9c), 259 stars at the 2026-08-12 snapshot, MIT. Corresponding paper: [A Kung Fu Athlete Bot That Can Do It All Day, arXiv:2602.13656v1](https://arxiv.org/abs/2602.13656v1). Stars are discovery metadata, not data-quality, control-confidence, or hardware-safety ratings.

## Why it is included

Initial screening classified the repository as project-only, but the official page and arXiv now provide a paper, so the relationship is corrected to official paper code. It forms an unusually visible chain across sports, recovery/safety, and training data: athlete video, GVHMR human-motion recovery, GMR retargeting, manual filtering and height adjustment, G1 tracking, fall recovery, and deployment.

A project page is needed to track current data and code status. The README contains an earlier 848-sample statement and a later 992-sample table, showing that the dataset evolves. FastSAC was also added after the initial paper path. Every count and result must therefore identify commit, data release, and subset.

## Problem addressed

Common human-motion datasets emphasize walking and daily activity and poorly cover rapid center-of-mass shifts, rotation, aerial phases, and failure boundaries. KungFuAthlete extracts high-dynamic motion and separates ground and jump subsets. The paper jointly trains tracking and fall recovery so a policy has behavior beyond the nominal reference neighborhood.

Each data stage can introduce systematic error: video pose estimation drifts or suffers occlusion, GMR can create foot slip or height error, manual filtering is subjective, and policy learning can imitate artifacts. Publishing intermediate SMPL-H and robot qpos creates an opportunity for independent retargeting and quality auditing.

## Architecture and data flow

The data path is `athlete video → scene segmentation → GVHMR → SMPL-H → GMR → G1 qpos → manual selection/post-processing → gravity-based height adjustment → NPZ`. The Unitree RL Mjlab training path uses three stages: coarse tracking with basic recovery, higher tracking precision, and improved robustness. FastSAC is an optional alternative to PPO.

Recovery is not presented solely as a separate state machine. Motion sampling, abnormal initial states, and LKE-related mechanisms expose one policy to unstable states. This reduces an explicit switching boundary but may create capacity competition between precise tracking and recovery. FastSAC’s early wall-clock gains must be read together with PPO’s later reward behavior.

## Code map

- [`gvhmr_to_qpos.py`](https://github.com/NPCLEI/KungFuAthleteBot/blob/1e3f207013245a5a0db75e6f70e1cdf762e28e9c/retarget/scripts/gvhmr_to_qpos.py) connects recovered human motion to GMR robot qpos.
- [`adjust_robot_height_by_gravity.py`](https://github.com/NPCLEI/KungFuAthleteBot/blob/1e3f207013245a5a0db75e6f70e1cdf762e28e9c/retarget/scripts/adjust_robot_height_by_gravity.py) performs ground/height post-processing and is a key place to inspect penetration artifacts.
- [Three-stage G1 configuration](https://github.com/NPCLEI/KungFuAthleteBot/blob/1e3f207013245a5a0db75e6f70e1cdf762e28e9c/unitree_rl_mjlab/src/tasks/tracking/config/g1/env_cfgs.py) expresses stage-specific reward, sampling, and robustness changes.
- [`MotionCommand`](https://github.com/NPCLEI/KungFuAthleteBot/blob/1e3f207013245a5a0db75e6f70e1cdf762e28e9c/unitree_rl_mjlab/src/tasks/tracking/mdp/commands.py) maintains reference motion, sampling, and recovery-related state.
- [`FastSAC`](https://github.com/NPCLEI/KungFuAthleteBot/blob/1e3f207013245a5a0db75e6f70e1cdf762e28e9c/unitree_rl_mjlab/holosoma_min/agents/fast_sac/fast_sac.py) is a later optional off-policy implementation and must not be projected backward as the only paper-v1 algorithm.

## Minimal reproduction path

Pin paper v1, repository commit, data release, and ground or jump subset. For one sample, retain GVHMR output, SMPL-H, GMR qpos, height-adjusted qpos, and NPZ. Check frame rate, root quaternion, joint order, foot height, velocity and acceleration peaks, self-collision, and hashes. Do not begin with an uninspected full-dataset conversion.

Start training with a stable ground motion and small environment count, verifying the actual differences among the three stages. Expand to the 1307 motion and jump subset only afterward. PPO/FastSAC comparisons must fix GPU, environments, seed, task, stopping rule, and logging. Report time-to-threshold, final reward, tracking error, falls, recovery, impacts, saturation, and failed videos.

## Capability boundaries

Public training video is not motion-capture ground truth, and manual processing cannot guarantee every frame. Weapon categories contain body motion without detailed hand or weapon control. The README explicitly warns that jump motions approach hardware limits and may retain imperfections.

Paper and repository counts change with data versions. Success on one motion or checkpoint cannot be generalized to every sample. The FastSAC result is a repository benchmark under a specific 16-hour window and stage; it does not prove universal training speed or higher final performance.

## Engineering assessment and risks

The strongest property is retention of intermediate human and robot data, making high-dynamic artifacts traceable. The central danger is treating visually impressive motion as a deployable reference. Generate a per-motion quality report, use different limits for ground and jump subsets, and quarantine failures rather than hiding them.

High-dynamic hardware work requires a qualified team, protected site, fall arrest or suspension, padding, exclusion zone, remote emergency stop, conservative gains, and gradually expanded motion envelopes, with torque, temperature, impact, and structural load monitoring. Aerial and flipping motions must never be attempted by copying README commands. This page provides neither authorization nor safety parameters.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/NPCLEI/KungFuAthleteBot/tree/1e3f207013245a5a0db75e6f70e1cdf762e28e9c)
- [arXiv:2602.13656v1](https://arxiv.org/abs/2602.13656v1)
- [MIT license](https://github.com/NPCLEI/KungFuAthleteBot/blob/1e3f207013245a5a0db75e6f70e1cdf762e28e9c/LICENSE)
