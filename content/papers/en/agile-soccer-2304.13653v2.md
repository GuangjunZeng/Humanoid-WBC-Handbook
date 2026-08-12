# Agile Soccer: composing recovery, locomotion, kicking, and opposition into one small-humanoid policy

[中文版](../agile-soccer-2304.13653v2.md)

Sources: [arXiv:2304.13653v2](https://arxiv.org/abs/2304.13653) · [Science Robotics DOI](https://doi.org/10.1126/scirobotics.adi8022) · [authors' quantitative data](https://doi.org/10.5281/zenodo.10793725)

Review scope: all 38 pages of the authors' version, including the main paper, 101 references, and Supplementary Materials. No uniquely verifiable official training repository is public. The Zenodo release contains quantitative figure and table data rather than the controller stack, so this review defines a paper-level reproduction contract without inventing source-level mappings.

> In one sentence: the work trains soccer and get-up skills separately, then combines them through adaptive multi-teacher regularization, a bounded pool of historical opponents, and targeted sim-to-real randomization, producing zero-shot real-robot 1v1 behavior on a 20-joint Robotis OP3; the evidence supports a small, protected, externally observed system, not an onboard-vision, full-size, or open human-shared deployment.

Key terms are Distributional Maximum a Posteriori Policy Optimization (DMPO，分布式最大后验策略优化), skill distillation（技能蒸馏）, adaptive teacher regularization（自适应教师正则）, self-play（自博弈）, opponent pool（历史对手池）, domain randomization（域随机化）, zero-shot sim-to-real（零样本仿真到现实）, motion capture (MoCap，动作捕捉), joint-position target action（关节位置目标动作）, set-piece experiment（受控定位球实验）, and operational design domain (ODD，适用设计域).

## Engineering problem

Robot soccer is not solved by calling a walking controller, a get-up routine, and a kick routine in sequence. The robot can lose balance while turning, shorten its steps near an opponent, recover while the ball is still moving, and switch behavior within a 25 ms nominal control period. A hand-built state machine can join a few nominal clips, but covering continuous contacts, velocities, and opponent configurations quickly becomes unmanageable.

Training one policy from a sparse goal reward is also insufficient. The paper reports that an unregularized agent found a rolling-on-the-ground local optimum that occasionally struck the ball. Adding forward and ball-directed shaping made it stand, but still did not reliably score. This is like asking a person who has not learned to stand to discover football only from match results: the terminal signal cannot distinguish useful early attempts.

The second problem is transfer on inexpensive hardware. The 51 cm, 3.5 kg OP3 has 20 XM430 servos, and backlash, zero offsets, battery state, missed cycles, and repeated impacts change its behavior over time. The authors explicitly report loosening hips, encoder miscalibration, and regular maintenance. “Zero-shot” therefore does not mean that simulation is exact; a fast position loop, randomized errors, perturbation training, mechanical protection, and maintenance jointly absorb mismatch.

The third problem is non-stationary competition. Pure self-play against the current policy can cycle and forget older responses. Fixed weak opponents do not provide a progressively harder curriculum. The system must solve exploration, skill composition, opponent selection, and hardware robustness together rather than relying on a larger neural network alone.

## Core insight

The first insight is to separate skill acquisition from match integration. Stage 1 trains one policy to score against an untrained opponent and another to get up by following three key poses sampled from scripted front and back recovery trajectories. Stage 2 initializes equally from front-down, back-down, and standing configurations, then trains one student with task return plus state-dependent regularization toward the appropriate teacher.

Teacher regularization is designed to disappear. The upright student is pulled toward the soccer teacher and the fallen student toward the recovery teacher. When corresponding Q thresholds are crossed, the regularization weight falls toward zero. The teachers are like an instructor's dual controls: they make early exploration survivable, but must release the student once the task is learned, or the result remains a switch between old skills rather than a policy that discovers new combinations.

The second insight is a deliberately bounded opponent pool. Opponents are sampled from untrained behavior and policy snapshots saved during the first quarter of training. Early snapshots provide a natural progression, while limiting the pool avoids filling it with many late, similar, or immediately overwhelming opponents. Figure 7 shows that sampling all snapshots was unstable and that training against fixed opponents plateaued earlier on the evaluation set.

The third insight is to transfer through position targets, not direct current control. The paper says zero-shot direct-current control failed. The 40 Hz policy outputs 20 position targets, smoothed by `u_t = 0.8 u_{t-1} + 0.2 a_t`; a torque PD loop in simulation or voltage-style PID on hardware tracks them. This inner loop behaves like a suspension layer: it cannot remove modelling error, but prevents the policy from having to reproduce every high-frequency actuator detail.

## Method

The MuJoCo/DeepMind Control Suite field is 5 m by 4 m with 0.8 m goals. The actor receives five-step stacks of joint positions, linear acceleration, angular velocity, gravity direction, and filtered previous action. Externally measured game state adds robot velocity and relative positions and velocities of ball, opponent, and goals. This is neither a proprioception-only controller nor a complete onboard-vision football system.

DMPO uses a feed-forward Gaussian actor and a categorical distributional critic. Supplementary Table S4 specifies critic layers `(400, 400, 400, 300)`, 51 atoms on `[-150, 150]`, five-step returns, and discount 0.99. The actor uses `(256, 256, 128)` layers and samples 20 actions per state. Replay capacity is `10^6`, batch size 256, trajectory segments 48, and both network learning rates are `10^-4`. These values constrain a reproduction, but absent code they do not settle normalization, termination ordering, or distributed sampling details.

Stage-1 soccer episodes terminate on a fall, leaving the field, entering a penalty area, an opponent goal, or 50 seconds. Supplementary Table S3 gives scoring weight 1000 plus dense forward-velocity, ball-directed velocity, interference, upright, and knee-torque terms. The recovery teacher does not track a full scripted trajectory. It switches among three poses from each front/back script, with an exponentially distributed mean target duration of 1.5 seconds, leaving multiple dynamical paths to each pose.

Stage 2 linearly combines task return and teacher losses. The critic additionally receives an integer opponent identity, while the deployed actor does not. That particular privileged input is deployment-free; the external MoCap game state is not and remains a major system dependency.

Servo identification produces approximate damping 1.084 Nm/(rad/s), armature 0.045 kg m², friction 0.03, maximum torque 4.1 Nm, and position gain 21.1 N/rad. Randomization covers friction 0.5–1, joint offsets ±2.9 degrees, IMU orientation 2 degrees, position 5 mm, an extra torso mass up to 0.5 kg, and observation delay 10–50 ms. Training also injects external disturbances every 1–3 seconds for 0.05–0.15 seconds. The paper labels their amplitude 5–15 Nm; a reproduction should preserve that stated unit and audit the environment definition rather than silently reinterpret it.

Fourteen OptiTrack PrimeX 22 cameras feed game state through VRPN/ROS. The robots receive torso bumpers, printed forearms, hip-load modifications, a marker vest, and rubber-tile flooring. Knee-load, upright, and action-range rewards complement these measures. They reduce experimental damage but are not certified safety barriers.

## How to read the key figures

![Figure 2: two-stage skill learning, distillation, and self-play](../assets/agile-soccer-2304.13653v2/figure-2-training-pipeline-03.jpg)

Figure 2 separates the two Stage-1 replay/DMPO loops from the unified Stage-2 student. The KL arrows explain how teacher behavior reaches the student; “earlier snapshots” explains how match difficulty evolves. The diagram supports the division of labor, not the claim that its thresholds or snapshot fraction transfer unchanged to another robot.

![Table 1: hardware behavior, scripted baseline, and sim-to-real gap](../assets/agile-soccer-2304.13653v2/table-1-hardware-05.jpg)

Table 1 reports 0.57 m/s walking, 2.85 rad/s turning, 0.93 s recovery, and 2.02 m/s standing-kick speed on real hardware, versus 0.20, 0.71, 2.52, and 2.07 for scripted baselines. A 2.5 m run-up raises the learned kick to 2.77 m/s. The widely quoted 181%, 302%, 63%, and 34% are relative to these specific scripts and protocols; they are not universal gains over classical control or evidence for a larger humanoid.

![Figure 5: controlled set-piece trajectories and footwork](../assets/agile-soccer-2304.13653v2/figure-5-behavior-08.jpg)

Figure 5 overlays ten trajectories for get-up-and-shoot, interception, opponent avoidance, and adaptive footwork. A turn-and-kick example uses ten footsteps to turn, travel roughly 2 m, turn again, kick, and rebalance. These panels demonstrate context-conditioned trajectories. With roughly ten trials per adversarial set piece, they do not establish general tactical understanding.

![Figure 7: ablations of opponent selection, teacher regularization, and shaping](../assets/agile-soccer-2304.13653v2/figure-7-ablation-19.jpg)

Figure 7 is the strongest mechanism evidence: five seeds per method are periodically evaluated against six fixed opponents for 100 matches each, with 95% confidence intervals. The full method finishes highest; all-snapshot self-play is unstable; fixed-opponent training plateaus; and removing both teacher regularization and reward shaping yields ground-rolling behavior. The combined ablation does not isolate the contribution of teacher loss from shaping.

![Figure S3 / Table S5: learning curves and compute cost](../assets/agile-soccer-2304.13653v2/figure-s3-table-s5-compute-34.jpg)

Supplementary Figure S3 and Table S5 expose the cost hidden by demonstrations. Recovery uses 2.4×10^8 steps, 70 simulated days, and 14 wall-clock hours; soccer uses 2.0×10^9 steps, 580 simulated days, and 158 hours; full 1v1 uses 9.0×10^8 steps, 262 simulated days, and 68 hours. Distributed execution compresses about 912 simulated days into 240 hours, but hardware specifications for the compute cluster are not reported, so this is not a personal-GPU budget.

## Strongest experiment

The strongest hardware transfer test is the matched 50-simulation plus 50-real get-up-and-shoot set piece. The policy stood and touched the ball in every real trial, scored 29/50 (58%) on hardware versus 35/50 (70%) in simulation, and first touched the ball at 4.7 versus 4.6 seconds on average. Explicit denominators and a reported gap make this more informative than a continuous-match montage.

Table 1 adds ten trials per behavior for the learned and scripted systems, including standard errors. Its turning protocol matters: the learned controller fell in three of 13 attempts before ten upright samples were retained, whereas the scripted controller completed ten consecutive upright trials. The 302% speed advantage must therefore be read with the rerun rule. The run-up kick also lacks an equivalent scripted comparison and supports energy-building behavior, not a matched 34% controller comparison by itself.

Figure 7 provides the stronger training-mechanism evidence because it combines five seeds, six opponents, and 100 matches per opponent at each evaluation. The two evidence blocks answer different questions: Figure 7 tests whether the recipe reliably produces stronger simulated policies; the 50+50 set piece and Table 1 test whether one resulting policy transfers to this OP3 setup. Neither alone proves a general humanoid-football method.

The supplementary vision policy is a smaller exploratory result. Static NeRF backgrounds are combined with MuJoCo renders of dynamic objects and ball appearance randomization. It scores 10/10 in a simulated penalty set piece, then 6/10 on hardware with three post hits. The critic still receives state information during training, and the policy architecture comes from NeRF2Real. Ten hardware shots cannot upgrade the main MoCap evidence into a reliable onboard-vision claim.

## Paper-to-implementation status

There is no public code or uniquely verifiable official training repository for the environment, DMPO learner, or deployment controller at this locked version. The official Zenodo release contains data behind quantitative figures and tables. Robotis OP3 software, MuJoCo, and dm_control are ingredients, not the paper implementation, so there are no two fixed-commit code symbols that can honestly be mapped to the method.

A reproduction can use Supplementary Tables S1–S5 as a contract, but similarity in final scores does not establish bitwise or symbol-level equivalence. If author-owned code appears later, provenance, paper linkage, license, and a 40-character commit must be checked before changing the status. A similarly named third-party football environment must not fill this evidence gap.

## Limitations and safety boundary

The authors explicitly identify extensive domain knowledge in rewards, handcrafted recovery key poses and skill choices, simulation-only training, testing on only a small robot, fragile/occluded MoCap ball tracking, frequently missed 25 ms deadlines, idealized actuators, battery sensitivity with practical 5–10 minute operation, maintenance for loose hips and encoder drift, unstable self-play, and extensive reward-weight tuning.

The authors also state that programmed joint limits do not eliminate self-collision. Knee-torque and upright rewards are preferences, not hard constraints. Bumpers, modified arms, soft flooring, and maintenance reduce damage. The paper's language about safe movement is an experimental observation, not a functional-safety certification, and aggregate counts of impacts, falls, and replaced hardware are not reported.

Our independent engineering boundary is a narrow ODD: a 5×4 m mapped field, two identical 51 cm OP3 robots, fourteen external cameras, known goals, simplified 1v1 rules, soft flooring, and expert maintenance. Mass, inertia, and fall energy scale nonlinearly. Rolling recovery and fast edge-of-foot turns that are tolerable on this platform cannot be copied to an adult-size humanoid.

A second independent boundary is perception. The actor receives relative opponent and ball state. Onboard vision adds occlusion, ego-motion, clock drift, recognition latency, and uncertainty. The 6/10 supplementary vision set piece does not cover active opposition, camera motion during falls, or sustained play.

A third independent boundary is causal attribution. Figure 7 removes teacher regularization and shaping together, while Figure S4 ablates only velocity rewards. A reproduction using PPO, SAC, or a newer simulator should preserve component-level and failure-mode comparisons; matching total return does not reproduce the proposed mechanism.

## Bounded engineering takeaway

The transferable idea is not merely “use RL for soccer.” It is a four-part contract: train the minimum skills needed to escape exploration dead zones; use state-dependent teacher regularization that exits when the student becomes competent; train against a controlled historical opponent curriculum; and expose joint offsets, delays, friction, payload, and disturbances around a position-target interface. Each contract needs a separate ablation and failure ledger.

For a WBC program, the paper is especially valuable as a recovery-with-task-continuity anchor. Recovery should not be an isolated demonstration: the system must stand and resume sensing and task progress. Conversely, the task policy must enter a low-energy recoverable mode after a fall. That principle transfers to inspection or carrying, while teacher selection, terminations, and safety supervision must be rebuilt for the new task.

Before hardware, separate the learned policy, fast joint loop, and independent safety layer. Robot-specific checks must bound joint position, velocity, torque/current, temperature, and attitude. Communication or MoCap timeout must enter a deterministic low-energy state. A harness where compatible, soft ground, a tested emergency stop, and a safety operator remain required during staged acceptance. Paper values are experimental records, not commands or certified limits.

## Reproduction and acceptance checklist

First, freeze the environment contract: OP3 collision geometry, field and ball parameters, 40 Hz actor, inner loop, action filter, every observation frame, and clocks. Log termination reasons separately for fall, bounds, penalty area, opponent goal, and timeout. Total return alone can hide a ground-rolling exploit.

Second, reproduce the recovery and soccer teachers independently. Recovery acceptance should include front/back starts, pose-switch randomization, time to the 36 cm shoulder threshold, failures, and peak actions. Soccer acceptance should report scores, touches, falls, and exploration toward the ball. Do not distill from an unstable teacher.

Third, log every adaptive-regularization variable: upright/fallen gate, both Q thresholds, KL weights, decay, and teacher disagreement. Compare permanent teacher loss, fixed annealing, adaptive release, and no teacher to show that new combinations come from student optimization rather than permanent teacher control.

Fourth, freeze opponent sampling and reproduce untrained, first-quarter history, all-history, and fixed-opponent pools. Use at least five seeds, six fixed evaluation opponents, and 100 games per opponent, retaining 95% intervals and cyclic failures. Define the “first quarter” by environment steps, not file order.

Fifth, split sim-to-real into identification, randomization, and external-disturbance ablations. The paper's negative result—without randomization and perturbations the real robot fell every one or two steps and could not score—is essential. Remove delay, offset, friction, payload, and perturbation separately to link each intervention to a failure mode.

Sixth, reproduce the exact Table 1 protocols and disclose reruns. Measure walking from seconds 2–7, turning from ±45 to ±135 degrees, recovery at the 36 cm shoulder threshold, and kick speed from distance travelled during 0.2 seconds after first contact. Falls remain in the denominator.

Seventh, run the same initialization grid for 50 simulated and 50 physical get-up-and-shoot trials. Report standing, first touch, scoring, touch-time distribution, and all failures. Stratify by battery voltage, servo temperature, hip looseness, and zero calibration to test whether the reported 58% depends on freshly maintained hardware.

Eighth, replace MoCap with vision only after offline comparison of MoCap truth, visual estimates, and actual policy inputs. Progress through stationary balls, rolling balls, opponent occlusion, and fall-induced camera motion. Document privileged critic state, NeRF backgrounds, and offline replay; do not pool the 6/10 vision result with the 50-trial MoCap evaluation.

Ninth, define independent stop conditions for repeated deadline misses, MoCap/IMU loss, attitude violation, excessive temperature/current, a person entering the protected zone, leaving the soft field, or loose hardware. Inspect battery and mechanical zero every 5–10 minute window. Record falls, impact locations, emergency stops, and replaced parts—not only successful goals.

> **Takeaway**: distillation and curriculum compose skills into one policy; an audited position loop, randomization envelope, and independent stop boundary are what make a hardware trial defensible.
