# SOMA Retargeter: an auditable BVH-to-G1 retargeting pipeline

[中文版](../soma-retargeter.md)

Reviewed snapshot: [NVIDIA/soma-retargeter@`b3ef2708d84bfd1314ddb52d0db6c9c211df1f57`](https://github.com/NVIDIA/soma-retargeter/tree/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57), 526 stars at the 2026-08-12 snapshot, Apache-2.0. Stars are only a discovery signal; they are not technical confidence or a hardware-safety rating.

## Why it is included

SOMA Retargeter has no directly corresponding paper, yet it exposes a part of humanoid data engineering that is often hidden in one-off scripts. It accepts BVH motion on the SOMA skeleton, applies proportional mapping, multi-objective inverse kinematics (IK), foot stabilization, and joint-limit clamping, and emits CSV motion for the 29-DoF Unitree G1. This makes it useful in the training-data and retargeting topic because a reader can inspect how each stage changes the trajectory.

The repository includes sample pairs, a visual viewer, and a headless batch path. Those features make interface and continuity checks possible, but they do not establish scientific superiority over other retargeters. No controlled downstream tracking comparison is provided. The review therefore treats the repository as inspectable engineering evidence, not as a paper-level claim.

## Problem addressed

Human and robot skeletons differ in link proportions, joint axes, degrees of freedom, and reachable sets. Copying pose parameters directly creates limit violations, floating feet, or inconsistent world displacement. A per-frame IK solver may converge while introducing temporal jumps that poison the reference consumed by a learned tracker. SOMA Retargeter organizes loading, scaling, solving, stabilization, limiting, visualization, and export as one reproducible pipeline.

Foot stabilization and joint-limit clamping address two visible failure modes, but both terms must be interpreted narrowly. Stabilizing a foot target is not the same as satisfying contact dynamics, and a position inside a joint limit does not imply acceptable velocity, acceleration, torque, or temperature. These modules are data checks upstream of control, not a whole-body controller by themselves.

## Architecture and data flow

The main flow is `BVH → AnimationBuffer → human/robot scale mapping → batched Newton/Warp IK → FeetStabilizer → JointLimitClamper → G1 CSV`. The converter application drives both interactive and headless processing, with JSON configuration selecting paths and retargeting parameters. Source and target states are advanced together in the viewer, which helps expose single-frame misalignment and temporal discontinuities.

Newton and NVIDIA Warp provide the computational substrate for parallel IK. The foot stabilizer constructs batched lower-limb objectives, while the clamper enforces model coordinate bounds at the end of the path. The ordering is meaningful, but it still cannot guarantee no foot slip, self-collision, or dynamic feasibility. Those properties require separate tests and, for dynamics, a simulator or hardware model.

## Code map

- [`Viewer.batched_retargeting` and `Viewer.retarget_motion`](https://github.com/NVIDIA/soma-retargeter/blob/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57/app/bvh_to_csv_converter.py) connect single-motion and folder processing to the shared pipeline.
- [`FeetStabilizer.solve`](https://github.com/NVIDIA/soma-retargeter/blob/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57/soma_retargeter/pipelines/feet_stabilizer.py) reveals how targets, batched state, and lower-limb IK are managed.
- [`JointLimitClamper.apply`](https://github.com/NVIDIA/soma-retargeter/blob/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57/soma_retargeter/pipelines/joint_limit_clamper.py) applies the model’s per-coordinate lower and upper bounds.
- [`IKSmoothJointFilter`](https://github.com/NVIDIA/soma-retargeter/blob/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57/soma_retargeter/pipelines/ik_objectives.py) shows that the optimization includes a smoothing objective rather than endpoint error alone.

## Minimal reproduction path

Pin the reviewed commit, fetch Git LFS assets, and use Python 3.12 with a supported NVIDIA driver. Run one included BVH through `python app/bvh_to_csv_converter.py --config assets/default_bvh_to_csv_converter_config.json --viewer gl`, save the CSV, and then process the same input with `--viewer null`. The interactive and headless outputs should agree in frame count, sample rate, and numeric content.

Record the input and configuration hashes, output frame rate, per-joint position and first-difference maxima, foot minimum height, horizontal slip during intended contact, self-collision events, and limit violations. Then replay the CSV in an independent simulator with conservative gains to verify coordinate conventions, joint order, and timing. Successful file generation alone is not acceptance.

## Capability boundaries

At the reviewed commit, the documented source is SOMA BVH and the documented robot target is the 29-DoF G1. Planned targets must not be reported as implemented support. The stack also depends on a compatible GPU, Newton, Warp, driver versions, and LFS assets, and the repository does not provide a controlled throughput benchmark across machines.

The output is kinematic. It has no contact-force solution, actuator delay model, torque guarantee, or stability margin. Ecosystem references to SOMA or SEED show intended use, not quality certification for every sequence. Users must separately determine whether licenses and data terms cover their chosen inputs and outputs.

## Engineering assessment and risks

The strongest feature is decomposition: loading, scaling, IK, stabilization, and clamping can be tested independently. The main evidence gap is the absence of controlled downstream tracking and real-robot safety evaluation. A production data gate should add temporal continuity, collision, foot-slip, initial-state reachability, and rollout tests, while retaining failed samples for diagnosis.

Any hardware playback requires independent simulation, robot-specific joint mapping, velocity/acceleration/torque limits, low-speed and low-gain commissioning, support or suspension where appropriate, and an operational emergency stop. This review provides no deployment-ready gains or limits. Repository demonstrations are not a safety case.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/NVIDIA/soma-retargeter/tree/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57)
- [Apache-2.0 license](https://github.com/NVIDIA/soma-retargeter/blob/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57/LICENSE)
- [Default converter configuration](https://github.com/NVIDIA/soma-retargeter/blob/b3ef2708d84bfd1314ddb52d0db6c9c211df1f57/assets/default_bvh_to_csv_converter_config.json)
