# Human2Humanoid (H2O): Real-Time H1 Teleoperation Depends on Feasible Data

[中文版](../human2humanoid-2403.04436.md)

Sources: [arXiv:2403.04436](https://arxiv.org/abs/2403.04436) · [pinned official code](https://github.com/LeCAR-Lab/human2humanoid/tree/750f1fa052641f0fde43669d50cb4e407dabe6c8)

Review scope: the complete ten-page paper and official H1 observation, tracking reward, domain-randomization, termination, and PPO implementation. This is the original H2O, distinct from OmniH2O.

> In one sentence: H2O retargets AMASS to H1, uses a privileged imitator to reject dynamically infeasible motions, and trains a robust 138-dimensional deployable policy; “RGB-only” describes the human command, while robot linear velocity still comes from external motion capture.

Key terms include human-to-humanoid teleoperation (人体到人形遥操), motion retargeting (动作重定向), sim-to-data (仿真到数据), privileged motion imitator (特权模仿器), embodiment feasibility (实施体可行性), keypoint goals (关键点目标), domain randomization (域随机化), and sim-to-real transfer (仿真到现实迁移).

## Engineering problem

A camera can estimate human pose, but a robot cannot necessarily execute it. Human and H1 proportions, axes, degrees of freedom, feet, torque, and bandwidth differ. Copying SMPL angles causes endpoint error, penetration, sitting, and dynamically impossible targets. The first bottleneck is motion feasibility, not network latency.

Manual review does not scale to ten thousand clips. H2O treats a privileged simulation policy as a customs checkpoint: clips that it can track enter the deployable dataset, while repeated failures are rejected. This is “sim-to-data”—physics execution cleans kinematic data.

Deployment must use less information than privileged training. Removing global state can destroy reachability reasoning, while retaining hard-to-estimate linear velocity creates hidden infrastructure. The observation contract therefore matters as much as the policy architecture.

## Core insight

H2O first fits an SMPL shape closer to H1 proportions, then minimizes twelve corresponding joint positions. Endpoint geometry is more useful than copying angles. Heuristics remove obvious unsafe sitting motions, but geometry alone cannot determine dynamic feasibility.

A privileged imitator then tracks roughly 10,000 retargeted sequences and retains about 8,500. The process resembles compilation: the retargeted motion is source code, and only motions that run under robot dynamics enter final training. Failures reveal embodiment boundaries rather than disposable noise.

The deployable policy has 138 state dimensions, including proprioception, targets/differences/velocities for eight extended keypoints, and the previous action, and outputs nineteen PD targets. Randomization spans friction, mass, center of mass, gains, 20–60 ms control delay, and periodic pushes.

## Method: input → processing → output

HybrIK estimates 3D human pose from approximately 30 Hz video. The robot policy runs around 50 Hz and the low-level sensor/PD chain around 200 Hz. Human keypoints become robot-space goals, while current joints, velocity, gravity, goal difference, and history produce nineteen joint targets.

Reward covers selected joint position and velocity, eight body keypoint positions, rotation, linear and angular velocity, with penalties for torque, acceleration, action rate, slip, collision, and limits. Termination by height, gravity, and reference distance also defines whether a motion survives sim-to-data.

The real setup uses a 1080p webcam and HybrIK, but the paper explicitly obtains robot linear velocity from a 50 Hz external MoCap system. Other proprioception comes from H1 at about 200 Hz. The accurate claim is monocular human command, not an entirely infrastructure-free control loop.

## How to read the key figures

![Figure 1: real-time whole-body tasks](../assets/human2humanoid-2403.04436/figure-1-real-time-teleop.jpg)

Figure 1 shows punching, side-step kicking, pushing a stroller, and box handling. The robot reorganizes lower-body motion for balance rather than copying each human frame. These are capability demonstrations, not repeated success statistics.

![Figure 4: the full H2O pipeline](../assets/human2humanoid-2403.04436/figure-4-pipeline.jpg)

Figure 4 is the central systems result: shape fit and retargeting, privileged filtering, robust sim-to-real imitation, then camera deployment. Removing the left side asks one policy to solve data cleaning and control simultaneously.

![Table III–IV: sim-to-data and scale](../assets/human2humanoid-2403.04436/table-3-4-sim2data.jpg)

Table III reports 85.5% for the privileged upper bound, 53.2% for a 90-dimensional reduced state, 67.9% without sim-to-data, and 72.5% for full H2O on uncleaned held-out motions. Global MPJPE is 166.7 mm and root-relative MPJPE 91.7 mm. Table IV rises from 52.0% at 0.1% of data to 72.5% at full scale.

![Figure 5–7: hardware motion and disturbance](../assets/human2humanoid-2403.04436/figure-5-7-hardware.jpg)

Figure 5–6 shows kicking, walking, and back jumping, and Figure 7 shows balance under a kick. They support real-time feasibility but provide no per-skill repetition count, failure rate, or latency distribution.

## Strongest experiment

Table III is stronger than the demo video. A reduced deployable state loses substantial success, while full state without sim-to-data also trails the complete method. This separates the effects of observation design and dynamics-based data cleaning.

The data-scale ablation shows useful sharing but long-tail difficulty. Simulation percentages do not establish hardware reliability because the paper lacks multiple-seed intervals and repeated real-world success rates.

## Paper-to-code mapping

At commit `750f1fa052641f0fde43669d50cb4e407dabe6c8`, `legged_gym/envs/h1/h1_teleop_config.py::H1TeleopCfg` defines 138 actor observations, 214 privileged observations, nineteen actions, and friction, link-mass, CoM, gain, delay, and push randomization.

`legged_gym/envs/base/legged_robot.py::compute_observations` assembles joints, body state, extended keypoint goals, and previous action. `_reward_teleop_body_position_extend`, `check_termination`, and `reset_idx` implement tracking and filtering. Observation variants such as `v-teleop-extend-max-nolinvel` make linear-velocity dependence an explicit engineering choice.

## Limitations and safety boundary

The authors explicitly identify representation, embodiment, and sim-to-real gaps. Larger state improves fidelity but hurts sample efficiency; weak regularization fails transfer while excessive regularization blocks learning. Camera latency and pose error are unavoidable, feedback is mostly visual, and lower-body fidelity is limited by morphology.

Independent limitations include external MoCap for robot velocity, missing systematic camera failure injection, absent repeated hardware statistics, and selection bias: the privileged imitator may reject motions that another controller could learn.

Human keypoint commands require speed, workspace, collision, and posture-health checks. Dropped or discontinuous video should freeze or transition to a safe behavior. Hardware needs tethering, mats, emergency stop, limits, current and thermal monitoring, and a trained safety operator.

## Bounded engineering takeaway

The reusable contribution is a three-stage funnel: geometric retargeting removes obvious errors, a privileged policy checks dynamic executability, and a deployable policy learns the accepted set under structured randomization. Each layer should report retention and rejection reasons.

Moving to another robot requires new correspondences, shape fit, ranges, termination, actuator modeling, randomization, and a rebuilt sim-to-data set. The reported 72.5% is not a platform-independent constant.

## Reproduction and acceptance checklist

Pin AMASS subset, retargeting version, H1 asset, Isaac Gym, commit, and seeds. Record counts through raw, retargeted, privileged-trackable, and deployable stages by motion class. Unit-test every slice, frame, unit, and normalization in the 138-dimensional observation.

Reproduce Table III and IV with multiple seeds and report MPJPE, falls, slip, limit and torque saturation. Inject keypoint loss, jumps, latency, and robot-velocity drift. Replace external velocity progressively with an onboard estimator and test degradation separately.

Stage hardware from static gestures through weight shifts, slow steps, then dynamics. Repeat each skill and log end-to-end latency, success, stop, torque, slip, and recovery. Camera or localization loss must enter a tested fallback state.

> **Engineering judgment:** H2O's decisive contribution is converting “a human can do it” into “this robot can learn it under its dynamics,” not direct video-to-joint copying.
