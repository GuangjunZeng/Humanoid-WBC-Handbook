# LATENT open-source project: the released tennis tracker and the unreleased-system boundary

[中文版](../latent.md)

Reviewed snapshot: [GalaxyGeneralRobotics/LATENT@`a931da5a70320ba3f07d38debcf71458a005530d`](https://github.com/GalaxyGeneralRobotics/LATENT/tree/a931da5a70320ba3f07d38debcf71458a005530d), 678 stars at the 2026-08-12 snapshot. No verifiable project-wide license was present at the repository root; G1 assets retain separate terms and require an independent check before use. Stars support discovery only. They are not evidence of tennis success, release completeness, or hardware safety.

## Why it is included

The LATENT paper describes a full chain of tracker pretraining, online DAgger distillation, a latent action model, and a high-level tennis policy. The pinned repository README draws a narrower boundary: the released material is motion-tracking code and a small tennis-motion subset. Online distillation, the pretrained latent model, LAB task learning, the high-level policy, and high-level sim-to-real design remain unchecked TODO items.

That difference between the paper system and the reproducible repository is precisely why an independent project page matters. This review makes fine-grained claims only about the inspected tracker, motion preprocessing, evaluation, and ONNX export paths. It does not infer unreleased implementation from the paper.

## Problem addressed

Human tennis motion is not a deployable robot trajectory. References need frequency alignment, recomputed angular, linear, and joint velocity, a smooth transition from the default pose, and explicit treatment of differences between the human wrist and the G1 racket mechanism. A tracker must then preserve whole-body behavior under 50 Hz control and 500 Hz simulation steps.

The released subset can study how imperfect human motion becomes tracker data and a low-level policy. It cannot reproduce the paper's central high-level mechanism: conditional latent priors and bounded residual action that adapt timing and location to the incoming ball.

## Architecture and data flow

The public route is `retargeted NPZ motion → resampling, velocity recomputation, and optional smooth transition → G1TrackingTennis environment → PPO tracker → Brax checkpoint → ONNX export → MuJoCo playback`. Configuration specifies `ctrl_dt=0.02`, `sim_dt=0.002`, rewards, termination, noise, and handling of excluded joints.

`G1TrackingTennisEnv` interprets policy output as offsets from reference joint positions for active actuators. Excluded joints such as parts of the right-wrist mechanism receive separately maintained targets. This prevents the tracker from blindly copying a human wrist trajectory that is incompatible with the racket embodiment. It does not model ball flight, strike targets, or the high-level tennis decision process.

## Code map

- [`g1_tracking_tennis_task_config` and `G1TrackingTennisEnv`](https://github.com/GalaxyGeneralRobotics/LATENT/blob/a931da5a70320ba3f07d38debcf71458a005530d/latent_mj/envs/g1_tracking/train/g1_env_tracking_tennis.py) define timing, reward, termination, observations, action offsets, and the excluded-joint contract.
- [`PlayG1TrackingTennisEnv.step`](https://github.com/GalaxyGeneralRobotics/LATENT/blob/a931da5a70320ba3f07d38debcf71458a005530d/latent_mj/envs/g1_tracking/play/play_g1_env_tracking_tennis.py) aligns reference motion, active-actuator targets, and excluded-joint targets during playback.
- [`preprocess_motion.py`](https://github.com/GalaxyGeneralRobotics/LATENT/blob/a931da5a70320ba3f07d38debcf71458a005530d/scripts/process_motion/preprocess_motion.py) calls environment preprocessing for batches, frequency alignment, and optional start/end smoothing.
- [The release TODO in the official README](https://github.com/GalaxyGeneralRobotics/LATENT/blob/a931da5a70320ba3f07d38debcf71458a005530d/README.md) is primary evidence that DAgger, the latent model, high-level training, and high-level sim-to-real design are not present in this snapshot.

## Minimal reproduction path

Pin the commit, Python 3.12.9, JAX, MuJoCo, Brax, the G1 assets, motion subset, and seeds. Copy the original NPZ files before preprocessing because the README warns that preprocessing overwrites input. Compare sample rate, angular, linear, and joint velocities, smooth transitions, and foot contact before and after conversion.

Train `G1TrackingTennis` with a small environment count. Log body, joint, and foot tracking, torque, action-rate, limit, collision, and termination reward components. Export one checkpoint and compare Brax with MuJoCo/ONNX tensors frame by frame for at least the first 100 steps. The acceptance statement should say that the tracker was reproduced; it must not claim reproduction of LAB or a ball-striking policy.

## Capability boundaries

The defining boundary is a public subset. The README marks the tracker and a small motion subset as released while full data, complete pretrained trackers, DAgger distillation, the latent action model, high-level tennis training, and sim-to-real designs remain pending. High-level results in paper figures and tables cannot serve as repository-reproduction acceptance.

The official overview also reports more than fifty motion-capture cameras, a 19-by-15-meter venue, and roughly RMB 350,000 in rental cost for real experiments. Running an open tracker command and reproducing the paper's end-to-end system are therefore different engineering claims.

## Engineering assessment and risks

The reusable contribution is explicit preprocessing of imperfect reference motion and isolation of wrist degrees of freedom that should not be copied to the racket embodiment. The main misuse is assuming that the repository name means the LAB core is public. Automated coverage should preserve both the reviewed commit and the release-TODO snapshot.

Hardware tennis combines a fast racket, a projectile, and large whole-body motion. Even tracker-only tests require an unoccupied exclusion zone, mechanical racket retention, hard joint, torque, and velocity limits, fall protection, an independent emergency stop, and a dedicated safety operator. Unreleased high-level control must not be guessed from prose and placed on hardware.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/GalaxyGeneralRobotics/LATENT/tree/a931da5a70320ba3f07d38debcf71458a005530d)
- [Released tracker scope and open TODOs](https://github.com/GalaxyGeneralRobotics/LATENT/blob/a931da5a70320ba3f07d38debcf71458a005530d/README.md)
- [English paper deep read](../../en/latent-2603.12686.md)
