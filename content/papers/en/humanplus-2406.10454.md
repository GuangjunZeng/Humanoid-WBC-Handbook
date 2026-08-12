# HumanPlus: From Human Shadowing to Egocentric Imitation

[中文版](../humanplus-2406.10454.md)

Sources: [arXiv:2406.10454](https://arxiv.org/abs/2406.10454) · [pinned official code](https://github.com/MarkFzp/humanplus/tree/ff7148903303ac2951857cf0b7df686d77323917)

Review scope: the full seventeen-page paper and appendix plus official HST, HIT, H1 environment, and hardware paths. Evidence for live shadowing, teleoperation efficiency, robustness, and autonomous imitation is kept separate.

> In one sentence: HumanPlus uses an eight-frame Humanoid Shadowing Transformer at 50 Hz to output nineteen body-joint targets, records egocentric demonstrations with head cameras, and trains a fifty-step Humanoid Imitation Transformer; it reports a six-person user study and ten hardware trials per task, while fixed camera occlusion, fixed retargeting, and a sitting-policy bypass remain explicit boundaries.

Key terms include humanoid shadowing (人形影子跟踪), whole-body teleoperation (全身遥操), motion retargeting (动作重定向), proprioception (本体感知), action chunking (动作块), future visual feature prediction (未来视觉特征预测), egocentric vision (第一视角视觉), simulation-to-reality (仿真到现实), and imitation learning (模仿学习).

## Engineering problem

VR teleoperation provides accurate hand commands but can constrain the operator and omit lower-body motion. Monocular human pose lets an operator walk, squat, and manipulate naturally, but latency, occlusion, and morphology mismatch can destabilize H1. Even if live shadowing works, autonomous learning still requires synchronized first-person images, robot state, and executed actions.

HumanPlus can be viewed as an actor, a stunt double, and a student. The human supplies intent, HST makes the robot double reproduce it while recording embodied data, and HIT learns to act from the recording. A second analogy is live translation: WHAM and HaMeR translate the human body into robot targets, while HST uses history to resolve ambiguity. A joint omitted by the fixed dictionary cannot be recovered by the downstream controller.

## Method

The customized Unitree H1 has thirty-three DoF: nineteen body joints, two wrists, and twelve finger joints, with two RGB cameras on the head. HST controls the nineteen body joints. Its observation includes roll/pitch, base angular velocity, joint state, last action, and target pose over eight frames. The policy runs at 50 Hz over a 1,000 Hz PD loop and is trained from about forty hours and eleven thousand AMASS motions with domain randomization.

One RGB camera estimates the human online: WHAM body pose runs around 25 Hz and HaMeR hands around 10 fps on an RTX 4090. Retargeting uses manually specified Euler-angle correspondences, including reduced finger mappings. For sitting, the authors bypass HST and send target poses directly to PD because rich contact was difficult to learn in simulation. This is an engineering workaround, not a unified-policy result.

### Input → processing → output

HST is a decoder-only Transformer mapping recent proprioception and target poses to joint setpoints. History helps bridge brief occlusion and target motion. Rewards cover target planar and yaw velocity, joint pose, roll/pitch, energy, foot contact, foot slip, and survival. Randomization spans base and hand payload, center of mass, motor strength, friction, and 20–40 ms control delay.

During data collection the robot follows a nearby operator, and two head cameras record the task. HIT consumes proprioception and stereo egocentric features and predicts a fifty-step action chunk. An auxiliary future-feature loss makes the current representation predict later visual features. Deployment runs at 25 Hz, using twenty-five to forty demonstrations for each task.

## Key figures

![Figure 1: full stack](../assets/humanplus-2406.10454/figure-1-full-stack.jpg)

Figure 1 connects shadowing, robot-centric data collection, and autonomous imitation. The illustrated warehouse, shoe, and cloth tasks show scope, while their repeated success belongs in Table 5.

![Figure 3: estimation and retargeting](../assets/humanplus-2406.10454/figure-3-retargeting.jpg)

Figure 3 separates body and hand estimators before fixed mapping to H1. A reproduction should log body and hand update age independently, because different rates and occlusion create stale mixed targets.

![Figure 4: HST and HIT](../assets/humanplus-2406.10454/figure-4-models.jpg)

Figure 4 shows HST history-to-setpoint control and HIT image/proprioception queries, action chunks, and future-feature prediction. Table 1–2 on the same page expose the reward and randomization contract behind the architecture.

![Table 3: user study](../assets/humanplus-2406.10454/table-3-user-study.jpg)

Table 3 averages six participants, two tasks, three measured trials, and prior practice. HumanPlus is the only comparator with whole-body movement and is faster, but operators remain nearby; the result does not cover remote networks or untrained use.

![Table 4–5: robustness and task trials](../assets/humanplus-2406.10454/table-4-5-hardware.jpg)

Table 4 reports directional disturbance thresholds of 32/44/70/100 N versus 24/36/40/40 N for default H1, with roughly 1.2 s versus 15 s recovery. Table 5 reports 90%–100% on most tasks but 60% for shoe-on-then-walk. Each result uses ten trials, so a displayed 100% is not a long-run failure bound.

## Decisive evidence

The strongest evidence is the combined user, robustness, and imitation evaluation. Six users support usability beyond one expert; disturbance tests isolate the low-level controller; repeated autonomous trials show whether collected data train an independent policy. The combination still assumes a short, fixed environment and a nearby human safety operator.

The 60% shoe-and-walk result is particularly diagnostic. It couples crouching, hand-foot coordination, stand-up, and locomotion. Fixed head cameras may lose the hands, morphology limits reachable poses, and contact error compounds between phases. Its failures indicate whether the next investment belongs in camera coverage, data collection, or control.

## Paper-to-implementation mapping

At commit `ff7148903303ac2951857cf0b7df686d77323917`, `HST/rsl_rl/rsl_rl/modules/actor_critic_transformer.py::ActorCriticTransformer` and `Transformer.forward` implement the history-to-action policy. `HST/legged_gym/legged_gym/envs/h1/h1.py::H1` provides `_init_target_jt`, `update_target_jt`, `_compute_torques`, and `_reward_target_jt` for target timing, delay, PD, and tracking.

`HIT/detr/models/detr_vae.py::DETRVAE_Decoder.forward` creates action queries and separates future camera features when `feature_loss` is enabled. `HIT/policy.py::ACTPolicy` organizes action-chunk learning, while `hardware/hardware_whole_body.py` exposes robot execution. Code presence does not make default settings safe for another H1 revision.

## Limits and evidence boundary

The authors explicitly identify the one-DoF ankle and five-DoF arms as reachability limits, loss of hands from fixed head cameras, fixed retargeting that omits joints, occlusion failures, and a focus on manipulation plus limited locomotion. Long-range navigation needs more data and better velocity estimation.

Independent limitations include asynchronous 25 Hz body, 10 fps hand, and 50 Hz policy targets without a published end-to-end timestamp acceptance test. Sitting bypasses the learned controller. Comparator training is not perfectly symmetric. Ten trials do not characterize confidence, recovery, or thermal state, and nearby operation does not test remote delay or loss.

Shadowing needs independent speed, torque, power, slip, and collision limits. Stale pose, occlusion, or loss of the person should trigger hold or low-energy behavior. Sitting and rising are contact-rich actions requiring geometry, contact checks, and emergency stop; a joint target inside numerical limits is not sufficient evidence of safety.

## Bounded engineering takeaway

HumanPlus is valuable because the data-collection interface and autonomous learner share the same embodied viewpoint and action space. A team can first use HST as an embodied data recorder, with strict synchronization and visibility metrics, before expanding autonomous task coverage.

Treat shadowing, sitting bypass, hand mapping, and visual imitation as separately degradable services. Preserve the original terms and code symbols so a reader can move from a reported engineering problem directly to the responsible module.

## Reproduction checklist

Pin hardware revision, DoF map, camera calibration, WHAM/HaMeR models, AMASS split, eight-frame context, 50/1,000 Hz rates, randomization, demonstration count, chunk length, and commit. Reproduce Table 3–5 with participant, practice, completion, failure, and video records.

Use one monotonic clock for body, hand, image, and joint streams; report mean, P95, and maximum age. Inject occlusion, dropouts, target jumps, and delay, and validate hold, abort, and recovery. Project unreachable Euler targets explicitly against joint, velocity, and collision constraints.

Stage hardware from suspended joints to standing, slow walking, squat, sitting, and manipulation with energy limits. Log success, intervention, damage, slip, camera hand loss, retries, and controller transitions. Expand unattended operation only after cross-user, lighting, placement, and thermal-duration gates pass.

> **Engineering judgment:** HumanPlus turns natural whole-body demonstration into robot-view data, but fixed cameras, fixed mappings, and asynchronous estimation make it first a bounded collection system—not a universal teleoperation guarantee.
