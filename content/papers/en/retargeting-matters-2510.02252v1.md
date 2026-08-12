# GMR: Retargeting Is an Upstream Dynamics Constraint, Not a Cleanup Step

[中文版](../retargeting-matters-2510.02252v1.md)

Sources: [arXiv:2510.02252v1](https://arxiv.org/abs/2510.02252v1) · [version-pinned official code](https://github.com/YanjieZe/GMR/tree/bb1bbe40774794fceb2a7c579a3464a28e68c844)

Review scope: the complete nine-page paper, experiments and references, plus the official `GeneralMotionRetargeting` implementation and LAFAN1-to-G1 configuration. This page contains original analysis, source locators, and links rather than copied paper text.

> In one sentence: GMR treats motion retargeting (动作重定向) as a data-quality gate that must reconcile morphology, reachability, continuity, and contacts before a tracking policy is asked to learn the motion.

Key terms include differential inverse kinematics (差分逆运动学), kinematic feasibility (运动学可行性), dynamic feasibility (动力学可行性), motion tracking (动作跟踪), domain randomization (域随机化), sim-to-sim transfer (模拟器间迁移), and operational design domain (ODD，操作设计域). The central distinction is that a geometrically plausible pose sequence is not automatically a physically executable robot reference.

## Engineering problem

Human motion is often converted into robot references as if it were a format conversion: scale the skeleton, solve inverse kinematics, and let reinforcement learning repair the rest. Ground penetration, self-intersection, a one-frame waist jump, or an unreachable starting pose are not ordinary noise, however. They create contradictory objectives: the tracker is rewarded for following an impossible reference while contact, joint, and termination constraints punish the same behavior.

The paper controls for downstream reward engineering by training the same BeyondMimic pipeline on references from PHC, ProtoMotions, GMR, and Unitree's closed data. The evaluation question is therefore not merely which IK solution has the smallest per-frame geometric error. It is whether a physical policy can complete the full clip under noise, delay, and model perturbations while remaining close to the intended motion.

A useful analogy is a railway: the policy is the train and the reference is the track. More locomotive power cannot repair a track that dives through the floor or turns discontinuously in one frame. That is why larger networks, more reward terms, or stronger randomization cannot reliably compensate for broken upstream geometry.

## Core insight

GMR changes the unit of evaluation from per-frame human-to-robot similarity to downstream closed-loop trackability. This creates an experimentally testable link between data construction and control robustness. The paper also separates local morphology scaling from world displacement: limbs need non-uniform scaling to match robot links, while root translation must remain globally consistent or foot contacts are pulled apart by incompatible local scales.

The two-stage IK is best read as an optimization strategy rather than a claim that two stages are universally superior. Stage one anchors key-body orientations and end-effector positions; stage two tightens all key-body position and orientation constraints. Previous-frame initialization and a final ground offset improve continuity, but the output is still a kinematic reference, not a dynamics certificate.

## Method: input → processing → output

Inputs are a BVH/SMPL motion, human height, a robot XML/URDF, semantic human-to-robot body correspondences, and stage-specific position/orientation weights. Local frames are first aligned in a static pose. Human root translation is scaled uniformly, while upper limbs, lower limbs, and selected rigid bodies receive local scales. Differential IK then solves generalized velocity updates under joint bounds, first for the coarse end-effector/orientation problem and then for all key bodies.

Equation 2 writes a non-root target as its root-relative human position multiplied by the local body scale, plus the uniformly scaled root translation. Equation 3 keeps root displacement on one global scale. Equations 4–6 define the two constrained IK stages. The result is a robot root pose and joint-angle sequence that must still pass collision, continuity, contact, and downstream rollout checks.

## How to read the key figures

![Figure 2: the five-step GMR retargeting pipeline](../assets/retargeting-matters-2510.02252v1/figure-2-pipeline.jpg)

Figure 2 should be read left to right as an audit trail: semantic body mapping, local-axis alignment, body-part scaling, coarse IK, and full-body refinement. Each stage corresponds to a distinct failure class, making the pipeline easier to diagnose than an opaque end-to-end optimizer. The figure supports modular inspectability; it does not prove that every output is dynamically feasible.

![Table I-II: downstream tracking success and error](../assets/retargeting-matters-2510.02252v1/table-1-2-tracking.jpg)

Table I and Table II must be paired. Table I reports completion over 21 LAFAN1 motions in IsaacSim without randomization, with randomized 4096-environment evaluation, and in ROS/MuJoCo sim-to-sim trials. Table II shows that surviving a clip does not imply faithful tracking: GMR's mean global rigid-body position error is 104.1 mm, below PHC's 247.8 mm and ProtoMotions' 139.7 mm but above Unitree data's 77.2 mm.

![Figure 3 and Table III: artifacts and start-frame sensitivity](../assets/retargeting-matters-2510.02252v1/figure-3-table-3-artifacts.jpg)

Figure 3 maps low success to visible reference artifacts: up to roughly 60 cm of ground penetration, leg self-intersection, and waist roll/pitch jumps. Table III shows that changing only the reference start frame can substantially change success. Together they support temporal and initialization gates; they do not establish real-hardware safety.

## Strongest experiment

The strongest evidence is the combination of Table I and Figure 3. The paper preserves failed motions and traces failures to specific reference defects while keeping the tracker, motion set, and disturbance protocol comparable. This supports the narrow conclusion that retargeting quality materially affects tracking success and error on Unitree G1 for these 21 non-interactive LAFAN1 clips.

The experiment does not prove that GMR is optimal for every robot, source dataset, object interaction, or general multi-motion tracker. It also contains no randomized hardware comparison. Perceptual similarity in Figure 4 is useful for checking whether a successful policy changed the motion, but it cannot replace feasibility metrics.

## Paper-to-code mapping

- [`GeneralMotionRetargeting.scale_human_data`](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/motion_retarget.py) implements local body scaling while preserving a uniformly scaled root translation, corresponding to Equations 2–3.
- [`GeneralMotionRetargeting.retarget`](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/motion_retarget.py) executes `tasks1` and `tasks2`, with convergence thresholds and bounded iterations corresponding to Equations 4–6.
- [`bvh_lafan1_to_g1.json`](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/ik_configs/bvh_lafan1_to_g1.json) fixes body mappings, stage weights, and upper/lower-body scales for the audited conversion.
- [`offset_human_data_to_ground` and `apply_ground_offset`](https://github.com/YanjieZe/GMR/blob/bb1bbe40774794fceb2a7c579a3464a28e68c844/general_motion_retargeting/motion_retarget.py) translate the sequence using foot height or an external offset; they do not verify contact consistency.

The pinned repository commit postdates paper v1 and contains later robots, formats, and safeguards. Those additions are useful engineering evidence but must not be backdated into the paper's experiments. The repository is MIT licensed; this handbook links to it without redistributing code, configurations, robot models, or motion data.

## Limitations and safety boundary

Author-stated limitations are that evaluation uses LAFAN1 and G1 only, excludes objects, scenes, and multi-person interaction, and can still exhibit optimization jumps requiring weight tuning. The reported comparisons use IsaacSim and ROS/MuJoCo rather than a hardware randomized trial.

Independent engineering limitations include the difference between “not terminated” and correct contact, energy use, or acceptable wear; one-policy-per-motion training does not reproduce capacity competition in a general tracker; and Unitree's closed references are a strong but unauditable baseline. Clip endpoints, joint-velocity continuity, foot height/slip, collision, and initial reachability should become automated gates before training.

This paper provides no transferable joint, velocity, PD-gain, or torque limits. Hardware use requires robot-specific bounds, collision checks, simulation replay, command limiting, emergency stop, and qualified review.

## Bounded engineering takeaway

Before tracker training, reject or repair reference clips with ground/object penetration, self-collision, joint-position or velocity jumps, and unreachable start/end poses. Do not rank data only by IK residual. Combine downstream completion, local/global body error, and perturbed or cross-simulator rollout evidence.

## Reproduction and acceptance checklist

Freeze the input motion version, semantic body map, scale factors, IK weights, joint limits, ground offset, and code commit. For every clip, export position/velocity continuity, foot height and sliding, collision, initial reachability, and downstream rollout statistics, including failed clips. Separate “can be tracked” from “should be tracked”: motion semantics, contact quality, energy, and hardware wear need their own gate.
