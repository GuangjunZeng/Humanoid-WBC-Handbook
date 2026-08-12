# GMR: real-time motion retargeting across humanoid embodiments

[中文版](../gmr.md)

Reviewed snapshot: [YanjieZe/GMR@`bb1bbe40774794fceb2a7c579a3464a28e68c844`](https://github.com/YanjieZe/GMR/tree/bb1bbe40774794fceb2a7c579a3464a28e68c844), 2,581 stars at the 2026-08-12 snapshot, MIT. This commit post-dates the paper and includes later robot and format extensions. Stars are a discovery signal, not proof of dynamic feasibility or hardware safety.

## Why it is included

General Motion Retargeting (GMR) is a high-star upstream data component for WBC training. It uses Mink differential inverse kinematics to map BVH, SMPL, and other human motions to G1, H1, and additional embodiments through configured key bodies, local scales, task weights, and two optimization stages.

Robot mappings live in reviewable JSON rather than one opaque script. That makes GMR a useful neutral starting point for comparing the same human motion across robots. It does not mean every configuration has received equal experimental validation.

## Problem addressed

Humans and robots differ in segment proportions, degrees of freedom, limits, and foot geometry. Copying joint angles creates end-effector error, self-collision, or unreachable poses. Aligning only hands and feet can lose torso orientation and contact meaning.

GMR first applies non-uniform scaling to local human-body positions, then solves two groups of differential-IK tasks. The first stage fixes primary structure and root behavior; the second refines end effectors and orientation. Each stage stops at an improvement threshold or iteration cap, trading a bounded compute budget for real-time throughput.

## Architecture and data flow

The core flow is `human parser → global body transforms → per-body local scaling → task1 differential IK → task2 refinement → ground offset → robot qpos trajectory`. Configuration binds human and robot bodies, scales, position/orientation weights, and task stages.

The output is a geometrically matched joint trajectory, not a dynamically feasible controller. Ground offset can avoid obvious penetration, but it does not enforce support polygons, friction cones, torque limits, or whole-body collision constraints.

## Code map

- [`GeneralMotionRetargeting.scale_human_data`](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/motion_retarget.py) converts key bodies to root-relative positions, applies local scaling, and restores global root translation.
- [`GeneralMotionRetargeting.retarget`](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/motion_retarget.py) runs `tasks1` and `tasks2` with improvement and iteration stopping conditions.
- [The LAFAN1-to-G1 configuration](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/ik_configs/bvh_lafan1_to_g1.json) binds bodies, weights, and upper/lower-body scales for both stages.
- [`offset_human_data_to_ground` and `apply_ground_offset`](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/motion_retarget.py) handle vertical offsets and must not be confused with contact dynamics.

## Minimal reproduction path

Pin the commit, Mink, MuJoCo, robot model, and human parser. Start with a short LAFAN1 walk. Save original transforms, scaled transforms, residuals and iteration counts for each stage, ground offset, and final qpos. Repeat with the same configuration and verify deterministic output.

Then add squatting, kneeling, rapid limb motion, and turning. Report body position and orientation error, joint-limit violations, foot slip, self-collision, and velocity/acceleration peaks. Only trajectories passing geometric checks should enter physics tracking and inverse-dynamics validation.

## Capability boundaries

GMR is not a human-motion reconstruction model; video needs an upstream system such as GVHMR or WHAM. It is also not a tracking policy or WBC. It optimizes selected geometry tasks without solving contact forces, actuator torque, or full self-collision constraints every frame.

The reviewed commit contains post-paper extensions. Its capability list is not evidence that the original paper benchmarked every current robot. Each new configuration needs versioned model hashes, mappings, weights, scales, and a failure set.

## Engineering assessment and risks

The most reusable design is the versionable embodiment map. The main risk is equating an attractive replay with executability. Rate every motion again using physics-tracking success, inverse-dynamics residual, and contact consistency, and preserve failure reasons.

Never send retargeted qpos directly to hardware. Check joint position, velocity, acceleration, torque, and self-collision; then run physics tracking, sim-to-sim, and supported low-gain tests. Limits must come from the target robot, not human motion data.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/YanjieZe/GMR/tree/bb1bbe40774794fceb2a7c579a3464a28e68c844)
- [Core retargeting implementation](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/motion_retarget.py)
- [English companion-paper deep read](../../en/retargeting-matters-2510.02252v1.md)
