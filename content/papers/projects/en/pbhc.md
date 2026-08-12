# PBHC / KungfuBot: an open pipeline from human motion to high-dynamic G1 tracking

[中文版](../pbhc.md)

Reviewed snapshot: [TeleHuman/PBHC@`ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0`](https://github.com/TeleHuman/PBHC/tree/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0), 1,052 stars at the 2026-08-12 snapshot, CC BY-NC 4.0. The repository explicitly restricts commercial use. Stars are a discovery threshold, not a success-rate or safety guarantee for dynamic motions on another robot.

## Why it is included

PBHC is the official KungfuBot implementation and also contains a later general-motion-tracking route. Its value is not limited to martial-arts videos. It joins motion sources, a unified SMPL format, physics filtering, Mink or PHC retargeting, motion correction, Isaac Gym training, trajectory analysis, and MuJoCo sim-to-sim in one repository.

This is more realistic than “download a motion and run PPO.” High-dynamic skill work is often dominated by data feasibility, contact timing, start and end poses, and conditions for safely entering a policy on hardware. The project page therefore emphasizes intermediate contracts rather than treating final videos as evidence for the entire pipeline.

## Problem addressed

Human motion reconstructed from video or captured in mocap may contain drift, ground penetration, unreachable joints, wrong contacts, and speed or inertia that do not fit G1. Direct retargeting forces RL to compromise against an infeasible reference, making it hard to separate a data failure from a controller failure.

PBHC filters and corrects motion, retargets it to the robot, and trains with adaptive tracking rewards. Adaptive sigma changes the tolerance of tracking terms from observed errors instead of assuming one fixed scale works for every skill.

## Architecture and data flow

The flow is `video/LAFAN/AMASS → SMPL motion → optional physics filter → Mink or PHC retargeting → contact/height correction → visualization and interpolation → Isaac Gym policy training → rollout metrics → ONNX/MuJoCo sim-to-sim → robot-specific adapter`. Frame rate, coordinate frames, joint order, and contact masks must be retained at every transition.

The repository distinguishes single-motion tracking from general tracking. The latter includes teacher and student observation configurations. It also documents a benchmark mode that uses privileged actor observations and no domain randomization. The repository explicitly says this mode is not deployable, so its result cannot be presented as sim-to-real performance.

## Code map

- [`MotionFilter`](https://github.com/TeleHuman/PBHC/blob/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0/smpl_retarget/motion_filter/utils/motion_filter.py) converts human-mesh and physical indicators into an optional motion filter.
- [`correct_motion`](https://github.com/TeleHuman/PBHC/blob/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0/smpl_retarget/mink_retarget/convert_fit_motion.py) corrects height using contacts and vertices, while [`retarget_fit_motion`](https://github.com/TeleHuman/PBHC/blob/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0/smpl_retarget/mink_retarget/retargeting/mink_retarget.py) is the main Mink-to-G1 path.
- [`GeneralTracking._update_adaptive_sigma`](https://github.com/TeleHuman/PBHC/blob/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0/humanoidverse/envs/motion_tracking/general_tracking.py) updates tracking scales. The same file computes body and joint tracking rewards.
- [`humanoidverse/README.md`](https://github.com/TeleHuman/PBHC/blob/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0/humanoidverse/README.md) pins the training, benchmark, evaluation, ONNX, and MuJoCo workflows and states pre-hardware limit checks.

## Minimal reproduction path

Start with the provided horse-stance sample and pretrained checkpoint. Reproduce evaluation before training a new motion. Record the motion schema, FPS, joint order, contact mask, policy-observation shape, and both sample and ratio metrics. Export ONNX and verify identical start/end poses and termination conditions in MuJoCo.

For a new motion, visualize the SMPL input, retargeted result, and correction output independently. Debug with 128 environments, then scale toward the README's 4,096 environments and 50,000 iterations. Compare fixed and adaptive sigma, with and without filtering/correction, across tracking error, completion ratio, torque, smoothness, contact mismatch, and multiple seeds.

## Capability boundaries

PBHC is not an autonomous perception and skill-planning system. The original KungfuBot route primarily trains a separate policy per motion, and repeated quantitative hardware trials concentrate on Tai Chi. Later general-tracking support does not retroactively provide equal hardware evidence for every skill or environment.

The repository uses CC BY-NC 4.0 and explicitly prohibits commercial promotional demos. Incorporated PHC, MaskedMimic, IPMAN, assets, and data retain their own terms; the top-level license is not a substitute for dependency-by-dependency review.

## Engineering assessment and risks

The most reusable design is the staged rule “validate data quality before policy optimization.” A common error is treating a visually attractive retargeted replay as proof of dynamic feasibility, or treating the privileged benchmark oracle as a deployable policy. Preserve upstream failure labels so the policy does not hide data defects.

High-dynamic hardware tests require support or suspension, buffer space, a physical emergency stop, position/velocity/acceleration/torque limits, impact protection, and communication-timeout handling. Run sim-to-sim and slow, low-gain stages first. Never infer deployable parameters from a video or from stars.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/TeleHuman/PBHC/tree/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0)
- [Official SMPL retargeting guide](https://github.com/TeleHuman/PBHC/blob/ffac5cded61fe78b39b051f09ac2ed0f6a1ccea0/smpl_retarget/README.md)
- [English KungfuBot paper deep read](../../en/kungfubot-2506.12851.md)
