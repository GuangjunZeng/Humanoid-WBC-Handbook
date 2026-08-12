# Meta Motivo: Zero-Shot Behavioral Foundation Models from Action-Free Motion

[中文版](../meta-motivo-2504.11054.md)

Sources: [arXiv:2504.11054](https://arxiv.org/abs/2504.11054) · [pinned official code](https://github.com/facebookresearch/metamotivo/tree/ff8dcc55cf58f766d365ab0be23a021a7e34d53d)

Review scope: the complete fifty-five-page paper, appendices, and references, plus official FB-CPR agent, forward-backward inference, and HumEnv wrapper.

> In one sentence: Meta Motivo's FB-CPR combines action-free AMASS motion with online interaction so rewards, goal states, or reference motions can define tasks at test time, but all evidence is on a MuJoCo SMPL humanoid rather than robot hardware.

Key terms include behavioral foundation model (行为基础模型), forward-backward representation (FB，前向—后向表示), successor measure (连续占用测度), conditional policy regularization (CPR，条件策略正则化), action-free motion data (无动作标注动作数据), zero-shot inference (零样本推断), and occupancy distribution (占用分布).

## Engineering problem

Conventional reinforcement learning retrains for every reward, target, or motion clip. A behavioral foundation model instead aims to encode broad interaction experience into a policy whose latent task can be inferred at test time.

Motion capture is abundant but lacks actions for the simulated body. Behavior cloning cannot infer the controls that generated a trajectory, while online RL alone struggles to cover human motion. It resembles having extensive game footage without muscle commands: the system must learn what human states look like from video and how to reach them through interaction.

The paper also unifies reward, goal-state, and trajectory interfaces. The question is whether one latent successor representation supports all three, not merely whether one network checkpoint has three wrappers.

## Core insight

Forward-backward representation approximates a policy's successor measure by a low-rank inner product. `F(s,a,z)` describes future occupancy under latent `z`, while `B(s)` embeds states as a basis. Reward-weighted backward features produce a task latent without retraining.

FB controllability alone does not ensure human-like behavior. CPR adds a latent-conditioned discriminator estimating a motion-data-to-policy occupancy ratio. Critic and actor combine FB and discriminator returns. It acts like a movement coach added to a navigator: task destination remains flexible, while visited states stay near the human-motion distribution.

Training mixes latent sources: approximately 60% expert-motion encoding, 20% online goals, and 20% uniform samples. The model uses a 256-dimensional latent and about 30 million environment steps. Scaling to roughly 288M parameters brings modest gains, suggesting data and objectives matter beyond capacity.

## Method: input → processing → output

The environment is a MuJoCo SMPL body with roughly 358 state dimensions and 69 action dimensions, simulated at 450 Hz and controlled at 30 Hz. AMASS contributes 8,902 training motions, about 29 hours, and 990 test motions, about three hours, without simulator actions.

ERFB encodes expert motion; online goals and uniform latent samples add coverage. The FB critic learns low-rank future occupancy and the actor maximizes its value. A `z`-conditioned discriminator supplies CPR regularization. Equations 7–11 describe the joint objective.

At test time, reward inference aggregates `B(s)` with reward values, goal inference uses the target state's backward feature, and tracking inference constructs commands from a reference sequence. Policy weights are not updated.

“Zero-shot” means no gradient training for the new task. Reward inference still needs evaluable reward samples, tracking needs a reference, and goal reaching needs a target state. Interface cost should be reported with capability.

## How to read the key figures

![Figure 2: FB-CPR objective](../assets/meta-motivo-2504.11054/figure-2-fbcpr.jpg)

Figure 2 and Equations 7–11 show FB dynamics and the conditional discriminator updating the actor. Motion data contain no action; occupancy regularization comes from motion, while controllability comes from online interaction.

![Table 1: three zero-shot task families](../assets/meta-motivo-2504.11054/table-1-main-results.jpg)

Table 1 reports normalized reward 0.61, goal proximity 0.69 and success 0.48, tracking EMD 0.80, and test success 0.88 for FB-CPR. It does not win every metric against retrained single-task top lines; its claim is substantial performance without task-specific retraining.

![Figure 3: human evaluation](../assets/meta-motivo-2504.11054/figure-3-human-eval.jpg)

Fifty evaluators prefer FB-CPR as more human-like than task-specific TD3 in about 83% of reward cases and 69% of goal cases. Human judgment supplements reward but is sensitive to video selection and cannot measure dynamics safety.

![Figure 4: objective and scaling ablations](../assets/meta-motivo-2504.11054/figure-4-ablations.jpg)

Figure 4 studies discriminator conditioning, FB objectives, data, capacity, and online training. CPR must be understood with FB controllability, and larger models alone give limited improvement.

## Strongest experiment

Table 1 is strongest because one protocol covers reward maximization, goal reaching, and motion tracking while distinguishing retrained top lines from unsupervised baselines. Test-motion tracking remains high and goals and rewards require no policy update.

All results remain in a simulated SMPL body. There are no robot actuators, state estimator, contact sensor, latency, or hardware trials. Compute also differs: oracle MPPI takes roughly thirty minutes for a 300-step episode, while FB-CPR inference and rollout take on the order of seconds.

## Paper-to-code mapping

At commit `ff8dcc55cf58f766d365ab0be23a021a7e34d53d`, `metamotivo/fb_cpr/agent.py::FBcprAgent` implements `sample_mixed_z`, `encode_expert`, `update_discriminator`, and actor/critic updates.

`metamotivo/fb/model.py` provides `reward_inference`, `goal_inference`, and `tracking_inference`. `metamotivo/wrappers/humenvbench.py` adapts HumEnv. Reproduction must pin AMASS processing, SMPL assets, MuJoCo, and tasks; checkpoints do not reconstruct the data-license chain.

## Limitations and safety boundary

The authors explicitly identify theoretical gaps, weak ground motion and fall/get-up behavior, occasional unnatural behavior, proprioception-only input, no navigation or object interaction, expensive motion capture, and no language interface.

Independent limitations include the large gap between SMPL actuation and robot motors, action-free data that cannot constrain real energy or force, human preference that may ignore foot sliding, unsafe out-of-distribution reward latents, and success thresholds unrelated to hardware error limits.

Robot migration requires retargeting and a low-level dynamics tracker. The high-level latent should produce bounded goals or references, not direct motor action. Joint, torque, contact, collision, fall recovery, and external emergency stop remain separate requirements.

## Bounded engineering takeaway

Meta Motivo turns reward, goal, and tracking into inference over one behavioral representation and uses action-free motion to regularize style. It is an important anchor for motion generation and high-level intent.

It is not a ready humanoid WBC. Morphology adaptation, low-level tracking, and safety filtering must be added and every task family revalidated. Simulated zero-shot behavior is not hardware zero-shot control.

## Reproduction and acceptance checklist

Pin AMASS licensing and file lists, splits, SMPL assets, HumEnv, MuJoCo, commit, and seeds. Verify 8,902/990 motions and filtering. Reproduce reward, goal, and tracking with input-construction time, rollout time, thresholds, and failures.

Ablate the 60/20/20 latent mixture, discriminator conditioning, online data, and capacity. For robot transfer, first report retarget feasible yield, slip, collision, torque, and tracking in simulation. Then stage bounded goals on hardware from static to slow tracking and complex motion, reporting falls, stops, saturation, and unnatural behavior.
