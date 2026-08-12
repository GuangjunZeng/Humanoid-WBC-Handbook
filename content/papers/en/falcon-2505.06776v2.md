# FALCON: Dual Policies and a Torque-Feasible Force Curriculum for Humanoid Loco-Manipulation

[中文版](../falcon-2505.06776v2.md)

Sources: [arXiv:2505.06776v2](https://arxiv.org/abs/2505.06776v2) · [version-pinned official code](https://github.com/LeCAR-Lab/FALCON/tree/a967a6d8494f57777cf8d266a644ac8e45833301)

Review scope: the complete 17-page paper and appendix, plus component-level inspection of the official MIT-licensed implementation at the pinned commit.

> In one sentence: FALCON separates upper- and lower-body objectives into two policies that still observe whole-body history, and derives training-force curricula from remaining actuator torque rather than arbitrary force boxes.

Key terms are loco-manipulation (移动操作), dual-policy decomposition (双策略分解), proprioceptive history (本体历史), Jacobian (雅可比矩阵), torque-feasible set (力矩可行域), Dirichlet distribution (迪利克雷分布), curriculum learning (课程学习), and residual disturbance (残差扰动).

## Engineering problem

Loads, doors, and carts transmit hand force through shoulder, waist, support legs, and ground. A lower-body locomotion policy combined with independent upper-body IK/PD can fight over trunk and angular momentum. A single whole-body policy avoids that explicit split but must balance velocity, posture, hand tracking, and force in one reward, where strong standing terms can dominate exploration.

Training force is also not sensibly sampled from an arbitrary uniform box. Small forces teach little; impossible forces keep the robot in failure states from which no action can satisfy both tracking and torque limits. The situation resembles choosing a lifting curriculum: random loads between a gram and a ton do not create useful progressive training.

FALCON targets both problems separately. Reward and critics are divided by upper/lower objectives, while full-body history preserves coordination. The force generator maps Cartesian forces through actuator torque margins before selecting disturbances.

## Core insight

“Separate optimization” does not mean “separate sensing.” Both actors see joint, IMU, and action history for the whole robot, so the upper body observes gait and the lower body observes trunk response to hand loading. Separate critics prevent two goal families from disappearing inside one scalar return.

The second insight is to derive force from actuator space. The relation `Jᵀf` maps end-effector force to joint torque; subtracting gravity-compensation usage estimates remaining margin. This is like checking remaining current on each fuse before allocating load.

The result is a training-distribution generator, not a real-time control barrier. Per-axis bounds and Dirichlet allocation do not represent the full joint feasible polytope, friction cone, impact, backlash, temperature, or continuous thermal rating.

## Method: input → processing → output

The lower-body actor optimizes velocity, standing, root height, and waist targets. The upper-body actor tracks shoulder, elbow, and wrist joint targets. Each has its own critic and rewards; both consume five-step whole-body joint/IMU/action history. Outputs are concatenated into a whole-body joint target and sent to PD control.

During training, critics may observe root linear velocity and end-effector force, while deployment actors need no force sensor. The force curriculum computes per-axis feasible intervals from end-effector Jacobian, gravity torque, and joint torque limits under `-τ_lim ≤ τ_g + Jᵀf ≤ τ_lim`. Dirichlet proportions distribute force across axes, global scale grows through curriculum, and the application point is randomized along the distal wrist chain.

The curriculum approximates static torque feasibility. Contact tasks still require force estimation, object constraints, collision handling, and an explicit failure/exit policy.

## How to read the key figures

![Figure 2: dual actors, shared observations, and concatenated action](../assets/falcon-2505.06776v2/figure-2-dual-agent.jpg)

Figure 2 has two paths: upper-body joint tracking and lower-body locomotion/root tracking. Shared history between them is the coordination channel. The outputs meet at the same trunk and contact dynamics, so the diagram should not be simplified into two independent controllers.

![Tables 1–2: architecture and force-curriculum ablations](../assets/falcon-2505.06776v2/table-1-2-force-curriculum.jpg)

Table 1 compares dual policy, monolithic whole-body RL, and PID on 252 ACCAD targets under no, medium, and large force. At large force, FALCON upper-body error is 0.37 versus PID 0.60 and monolithic RL 0.73, while root-velocity error remains a tradeoff. Table 2 isolates force sampling: torque-aware curriculum gives 0.36 upper-body error under large force versus 0.61 for broadly clipped sampling.

![Table 4: G1 hardware load-walking comparison](../assets/falcon-2505.06776v2/table-4-hardware.jpg)

Table 4 connects simulated disturbance training to a G1 carrying 1.2 kg in each hand at 0.5 m/s. FALCON upper-body error is 0.39 versus 0.81 for monolithic RL and 1.81 for PD. It covers one quantitative load/walking condition; door opening, cart pulling, and box handling remain mostly qualitative and lack complete trial denominators.

## Strongest experiment

Tables 1–2 form the strongest causal chain. The first separates policy structure from PID and monolithic RL; the second separates torque-aware sampling from a broad force box. Both are necessary to support the full claim that objective decomposition and mechanically informed disturbance generation improve learning under the tested commands.

Table 4 is an important hardware anchor but is narrow. A stronger reproduction should include sustained push/pull, sudden sticking or release, one-sided loads, multiple speeds, success/fall counts, torque saturation, current, and temperature.

## Paper-to-code mapping

- `LeggedRobotDecoupledLocomotionStanceHeightWBCForce._calculate_max_ee_forces` reads Jacobians and torque margins to compute left/right-hand axis bounds.
- `_init_force_settings`, `_scale_forces`, and `_update_force_scale_curriculum` implement Dirichlet axis proportions, filtering, clipping, and global force-scale progression.
- `_resample_force_settings` and `_pre_compute_observations_callback` randomize the application location along the hand chain and build applied-force positions.
- `_reward_tracking_upper_body_dofs` and the multi-agent PPO configuration define upper-body tracking and separate policies.

All symbols are in the [pinned official repository](https://github.com/LeCAR-Lab/FALCON/tree/a967a6d8494f57777cf8d266a644ac8e45833301). The commit is later than the first manuscript and old README TODOs do not describe its current tree, so reproduction must follow the pinned files rather than historical announcements.

## Limitations and safety boundary

The Author-stated limitation is that the current interface relies on joint-angle targets and should be extended to Cartesian end-effector tracking; it does not close the loop on desired contact force. Independent limitations are delayed force inference through history, per-axis approximations, omitted impact/thermal/backlash constraints, platform-specific configurations, and only one quantitative hardware load-walking setting.

Concatenated actors still couple through one trunk and support system. Individual actor stability cannot guarantee combined torque and balance feasibility. Hardware requires whole-body torque, support, contact force, current, temperature, and fault monitoring.

Training-force ranges are not hardware permission envelopes. Real door, cart, and payload tasks need independent force/torque limits, contact detection, thermal protection, and emergency exit logic.

## Bounded engineering takeaway

Reuse the idea “sample disturbances from an actuator-informed feasible region, then compare structured and monolithic policies.” Keep no-torque-aware curriculum, monolithic policy, PID, and no-shared-history controls. Report hand tracking and locomotion, support, saturation, energy, and falls together so upper-body gains cannot hide lower-body degradation.

## Reproduction and acceptance checklist

List upper/lower observations, commands, actions, rewards, network budgets, and shared history. Unit-test the force generator on random poses by mapping sampled force back through the Jacobian and measuring final clipping. Preserve theoretical candidate force and actual applied-force histograms by axis, pose, and application point. Evaluate wrist and forearm points, impulses versus sustained force, and combined one-sided load. Hardware progression should move from static symmetric loads to slow locomotion, asymmetric loads, sustained push/pull, and sudden release, with explicit rollback criteria and full current/temperature/contact logs.
