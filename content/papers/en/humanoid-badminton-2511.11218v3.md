# Humanoid Badminton: Three-Stage Whole-Body RL from Footwork to Task Refinement

[中文版](../humanoid-badminton-2511.11218v3.md)

Sources: [arXiv:2511.11218v3](https://arxiv.org/abs/2511.11218v3) · [official project page](https://humanoid-badminton.github.io/)

Review scope: the complete 15-page paper and appendix. The official page did not provide an auditable author code repository, so no third-party implementation is presented as official.

> In one sentence: Humanoid Badminton moves one 21-DoF policy through stable footwork, sparse contact discovery, and task-effect refinement, then compares explicit EKF interception targets with history-based implicit prediction on hardware.

Key terms are curriculum reinforcement learning (课程强化学习), sparse hit reward (稀疏击球奖励), racket-face orientation (拍面姿态), interception prediction (交点预测), Extended Kalman Filter (EKF，扩展卡尔曼滤波), prediction-free policy (无预测策略), motion capture (MoCap，动作捕捉), and human-robot shared space (人机共域).

## Engineering problem

Badminton compresses foot placement, trunk stabilization, and a narrow racket interception window into about one second. Rewarding only “the shuttle crossed the net” gives almost no early signal. Keeping dense pose and proximity rewards forever can produce an aesthetically plausible swing that does not send the shuttle to a useful target.

The three-stage curriculum works like teaching driving: learn stable start/stop first, then steering and observation, and only later evaluate full traffic behavior. Making every requirement strict on the first lesson does not create a more complete skill; it creates competing gradients.

Sensing adds another tradeoff. An EKF supplies time-to-hit, interception position, and desired racket orientation but depends on MoCap and an aerodynamic model. A prediction-free policy consumes current ball position and five-frame history, simplifying the interface while hiding time estimation inside the actor.

## Core insight

The final stage deliberately removes most style and process rewards. Stages S1 and S2 are scaffolds that let the policy cross exploration gaps; S3 removes part of the scaffold so outgoing shuttle outcome controls final optimization. This is not simply “adding more rewards at every stage.”

The sensing comparison keeps actions and rewards consistent and changes the ball representation, making differences easier to attribute to interception estimation. “Prediction-free” is a naming convenience, not a literal absence of prediction: history lets the network infer speed and arrival time.

The deployment choice is itself evidence. Despite competitive simulation means, the prediction-free policy has worse real launch success and virtual-target error, so the authors use the EKF policy for human rallies. An end-to-end label is not a reason to discard measured safety margin.

## Method: input → processing → output

A 1.28 m, 21-DoF humanoid uses the same observation and action interface across three reward stages. S1 learns stationary and moving footwork with stable posture. S2 adds sparse contact, racket position, and orientation rewards to discover swings. S3 removes most style/proximity terms and refines the final hit outcome.

The actor receives 87-dimensional proprioceptive and task input plus history; the critic additionally sees clean state. It outputs 21 target joint positions at 50 Hz for a 500 Hz PD loop. The target-aware version samples about 20k pre-generated shuttle trajectories with hit time, interception, and racket orientation. On hardware, 210 Hz MoCap and EKF produce the same semantics. The alternative sees current shuttle position and five frames of history. Neither policy uses force or tactile sensing.

## How to read the key figures

![Figure 2: three-stage training and MoCap/EKF deployment](../assets/humanoid-badminton-2511.11218v3/figure-2-training.jpg)

Figure 2 connects simulated target generation, staged rewards, and the real MoCap/EKF path. The generated and online pipelines deliver nominally identical target semantics but not identical latency and noise. It supports interface reuse, not distribution equality.

![Figures 3–4: simulated rally and target-aware/prediction-free control](../assets/humanoid-badminton-2511.11218v3/figure-3-4-control.jpg)

Figure 3's 21-hit two-robot rally is a best trajectory, not an average rally length. Figure 4 shows the form of the sensing comparison. These capability images must be interpreted beside full denominators rather than treated as typical performance.

![Figures 5–6: hardware swing error and launcher success](../assets/humanoid-badminton-2511.11218v3/table-5-hardware.jpg)

Figures 5–6 provide symmetric denominators: 71 virtual-target swings for each policy and 46 launcher trials each. Mean target error is 2.46 cm for EKF versus 6.71 cm prediction-free. Launcher success is 42/46 (91.3%) versus 33/46 (71.7%); peak outgoing speed is 19.1 versus 18.1 m/s and mean speed 11.1 versus 8.2 m/s.

## Strongest experiment

The 46+46 controlled launcher trial is strongest because incoming conditions are repeatable and denominators match. It shows that prediction-free control works but is not equivalent: a 19.6-point success gap and larger target error are deployment-relevant. The authors' negative choice not to use it in human rally is valuable engineering evidence.

A launcher is not a human opponent. It has less variable speed, deception, and human path intrusion. Reproduction should stratify speed, direction, landing point, estimator uncertainty, and reachability, including the policy's ability to refuse an unreachable shuttle.

## Paper-to-implementation status

As of 2026-08-10 the paper and official project page exposed paper and video, but no unique official code repository, commit, or license. Three-stage transitions, shuttle simulation, EKF, rewards, and hardware protection cannot be audited as source symbols.

Any reproduction must label those components as independently implemented. Matching success rates cannot establish identical mechanisms or safety boundaries.

## Limitations and safety boundary

Author-stated limits are MoCap dependence; one dominant forehand style with no backhand, lunge, or jump smash; a narrow interception band; insufficient long rallies; lower precision/success for the prediction-free policy; and missing high-level landing-target decisions.

Independent limits include human-rally evidence without a complete denominator, more repeatable launcher inputs than human shots, venue effects, aerodynamic and shuttle-flip mismatch, and latency/EKF/action errors that may add in the same direction. Mean error hides rare early/late high-energy swings, so tail error and racket-head energy are necessary.

This is a high-speed shared-space system. A 91.3% return rate is not permission for close human interaction. Reproduction must start with simulation, dummy balls, low-speed launching, a restricted interception zone, independent emergency stop, netting, a safety operator, and a separate spatial supervisor that can reject swings.

## Bounded engineering takeaway

Use stable footwork and intermediate racket targets to cross sparse exploration, then remove process rewards that obstruct task optimization. Compare sensing interfaces under identical action, reward, and launcher distributions, and preserve negative deployment decisions. Treat rejection of unreachable shots as a safety success, not merely a missed task.

## Reproduction and acceptance checklist

Freeze shuttle dynamics, contact, trajectory library, interception range, and stage rewards. Save stage snapshots and replay prior capabilities after every transition. Log MoCap measurements, EKF state, interception prediction, actor input, racket timing, support state, and safety overrides. Progress from virtual fixed targets to machine launches stratified by speed/direction/landing point, then to human-free rally. Report contact, net crossing, valid landing, continuation, falls, emergency stops, refusals, tail timing error, and post-test mechanical inspection. A spatial safety layer must bound people, racket swept volume, speed, and stopping distance independently of the learned policy.
