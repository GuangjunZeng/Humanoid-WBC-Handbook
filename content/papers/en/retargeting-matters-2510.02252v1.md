# Retargeting Matters: Robot Retargeting Is an Upstream Dynamics Constraint

[中文版](../retargeting-matters-2510.02252v1.md)

Source: [arXiv:2510.02252v1](https://arxiv.org/abs/2510.02252v1). The implementation notes refer to the pinned official GMR code linked by the Chinese evidence page.

> **Bottom line:** GMR treats retargeting as a constrained optimization problem over robot links, scale, root motion, and kinematic limits. A visually plausible human-to-robot mapping can still inject foot slip, unreachable poses, or unstable targets that a tracking policy cannot repair.

## Engineering problem
Human and humanoid proportions, joint axes, degrees of freedom, and end-effector semantics differ. Copying joint angles or matching only selected keypoints leaves systematic artifacts in root height, contact, and limb reach, which later appear as an RL problem even though they originated in the data layer.

## Method
The method defines robot-specific link correspondences and solves a weighted kinematic objective after scale and coordinate normalization. The useful engineering idea is not one universal set of weights; it is making every mapping, offset, scale, limit, and objective explicit and testable before policy training.

## Key figures
![Figure 2: end-to-end retargeting pipeline](../assets/retargeting-matters-2510.02252v1/figure-2-pipeline.jpg)
Figure 2 separates human representation, robot correspondence, optimization, and exported motion.
![Tables 1-2: downstream tracking comparisons](../assets/retargeting-matters-2510.02252v1/table-1-2-tracking.jpg)
The tables show that upstream retargeting choices measurably change downstream tracking rather than merely changing visual style.
![Figure 3 and Table 3: artifact analysis](../assets/retargeting-matters-2510.02252v1/figure-3-table-3-artifacts.jpg)
The artifact views make foot placement and morphology mismatch auditable instead of hiding them inside a total reward.

## Decisive evidence
The strongest evidence is the same-policy comparison under different retargeting pipelines: tracking quality changes even when the controller is held fixed. That supports the causal claim that data geometry is part of controller performance.

## Paper-to-implementation mapping
The pinned GMR repository exposes the motion-retargeting class, robot configuration files, correspondence tables, and optimization path. Reproduction should point to those concrete artifacts and save the resolved robot configuration with every generated trajectory.

## Limits and evidence boundary
Kinematic feasibility is not dynamic feasibility. Contact timing, collision, torque, thermal limits, and state-estimation robustness still require simulation and closed-loop checks. Results on supported robot configurations do not make arbitrary morphologies zero-configuration.

## Bounded engineering takeaway
Promote retargeting to a versioned subsystem with its own acceptance tests. Reject or repair motions before RL when root discontinuities, persistent foot slip, joint-limit saturation, or link-collision checks fail.

## Reproduction checklist
Lock source motion, robot URDF/MJCF, link map, scale, coordinate transforms, objective weights, solver tolerances, and output rate. Report per-link error, root and foot trajectories, contact artifacts, joint-limit margin, downstream tracking success, and failure examples.
