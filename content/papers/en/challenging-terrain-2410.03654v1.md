# HT-2: Learn Basic Walking from Flat-Ground Sequences, Then Fine-Tune for Challenging Terrain

[中文版](../challenging-terrain-2410.03654v1.md)

Sources: [arXiv:2410.03654v1](https://arxiv.org/abs/2410.03654v1) · [official project page](https://humanoid-challenging-terrain.github.io/)

Review scope: the complete 42-page paper and supplementary material. At the review snapshot, the official page provided no auditable author code repository, commit, or license, so no third-party implementation is presented as official.

> In one sentence: HT-2 pretrains a Transformer on heterogeneous flat-ground observation-action sequences, then uses PPO to convert that initialization into a blind proprioceptive Digit policy for difficult terrain.

Key terms are sequence pretraining (序列预训练), masked action token (遮码动作标记), policy fine-tuning (策略微调), sample efficiency (样本效率), proprioception (本体感知), privileged critic (特权评论家), and operational design domain (ODD，操作设计域).

## Engineering problem

Training Digit from scratch on rough terrain spends large interaction budgets rediscovering basic posture and stepping before it can learn contact adaptation. Existing neural controllers, model-based controllers, and human motion already contain flat-ground structure, but their observations and actions are not all identical and some trajectories lack robot action labels.

HT-2 converts heterogeneous sources into observation-action sequences. Missing actions use a learned `[M]` token rather than a numeric zero, separating “unknown” from “the controller commanded zero.” A Transformer learns temporal structure on flat ground, then initializes an RL actor on six procedural rigid-terrain families.

The design is analogous to teaching a learner to stand and walk on a gym floor before spending expensive lessons on rocks. Pretraining does not teach terrain itself; it tries to stop terrain RL from spending its budget on elementary gait discovery.

## Core insight

The first insight is that useful state trajectories need not all provide identical action supervision. Explicit missingness lets human motion and model-controller rollouts contribute temporal structure without pretending their action fields are robot commands.

The second is methodological: sample-efficiency claims need scratch baselines with equal and larger RL budgets. Figure 9 gives scratch up to twice the interaction budget and still observes a gap. Without that control, “faster convergence” could simply mean the pretrained method consumed more total data.

The third is that initialization leaves behavioral bias. Figure 11's more symmetric gait is not only visual style; it indicates that PPO retained part of the flat-ground prior instead of fully rewriting it. This can be beneficial, but any inherited bias outside the target ODD must also be measured.

## Method: input → processing → output

The four-layer Transformer has hidden dimension 192 and roughly 1.4 million parameters. It consumes 16 steps of proprioceptive observations and action history. Digit has 20 actuated joints, but foot joints are treated as passive; actions contain target position, Kp, and Kd for the other 16 motors, totaling 48 dimensions.

The policy runs at 50 Hz and the PD loop at 2000 Hz. During fine-tuning, PPO uses procedural downhill, uphill, rough, obstacle, slippery, and perturbation settings. The critic can observe terrain height maps, robot parameters, and absolute state, while the deployed actor remains blind and uses only proprioception.

The output is therefore not a terrain-aware planner. It is a history-conditioned reactive controller whose training critic had privileged terrain information. This distinction defines the deployment ODD.

## How to read the key figures

![Figure 8: flat-sequence pretraining and terrain fine-tuning](../assets/challenging-terrain-2410.03654v1/figure-8-pretrain-finetune.jpg)

Figure 8 separates data boundaries. Pretraining absorbs multi-source flat sequences and missing-action masks; terrain rewards and privileged height-map criticism enter only in fine-tuning. The deployment actor is still blind, so the figure does not support claims of exteroceptive foothold planning.

![Figure 9: sample efficiency versus scratch reinforcement learning](../assets/challenging-terrain-2410.03654v1/figure-9-sample-efficiency.jpg)

Figure 9 plots interaction budget rather than only final reward. Fine-tuned policies enter useful performance sooner on uneven terrain, pushes, and velocity tracking, while scratch is trained to 200M steps versus 100M for fine-tuning. This is the paper's clearest evidence for a better RL starting point, within the chosen network, reward, and terrain mix.

![Figure 11: gait morphology after pretraining and fine-tuning](../assets/challenging-terrain-2410.03654v1/figure-11-gait.jpg)

Figure 11 shows a relatively symmetric support pattern after fine-tuning and a left-leg-dragging scratch trajectory. It generates a hypothesis about retained gait quality but is vulnerable to cherry-picking. Dataset-level foot clearance, left-right support duration, trunk angular velocity, and cost of transport are needed to establish a general effect.

## Strongest experiment

Figure 9 is the strongest mechanism result because it separates faster learning from a better terminal score and grants the scratch policy a larger budget. Figure 10 further compares pretraining and fine-tuning across downhill, uphill, pushes, obstacles, rough ground, and slippery ground, with larger gains in harder conditions.

The real-world hiking evidence—five outings totaling about 4.3 miles, slopes up to 31%, and sand, mud, or wet ground—supports a durability case study. It has no randomized control, failure denominator, or complete intervention log, so it cannot establish the mechanism with the same strength as Figure 9.

## Paper-to-implementation status

As of 2026-08-10, the paper and official project page exposed paper, authors, and demonstrations but no uniquely verifiable official code repository, commit, or license. The status is `no_public_code_found`. No third-party reproduction can be used to invent symbol mappings for the mask token, pretraining loss, PPO initialization, or Digit deployment.

An independent implementation should explicitly label sequence slicing, mask ratios, loss reduction, optimizer state transfer, and privileged observation choices as reproduction decisions. Similar curves do not prove symbol-level identity.

## Limitations and safety boundary

The authors explicitly state that blind proprioception cannot anticipate discrete steps or stepping stones that require planned footholds; future work needs vision. Independent limits are rigid training terrains, soft-ground evidence that is primarily case-based, missing fall/intervention denominators for hikes, and policy-produced Kp/Kd, which enlarges the hardware risk surface.

Gain outputs must be bounded independently, with rate, oscillation, and sustained-stiffness monitoring. Simulated torque compliance does not certify temperature, peak current, gearbox impact, or structural fatigue.

Digit-specific actions, passive joints, gains, contacts, and termination rules cannot be copied to another robot. Hardware testing must start tethered, low-speed, and low-slope, with fall, takeover, slip, torque, current, and thermal logs.

## Bounded engineering takeaway

Use relevant trajectory pretraining as an explicit baseline against scratch, but compare equal and larger scratch budgets. Report procedural rigid terrain, unseen rigid terrain, and soft-ground cases separately. A long blind hiking demonstration must not erase the information boundary that the actor cannot foresee discrete obstacles.

## Reproduction and acceptance checklist

Build source cards for each pretraining dataset: generator, robot morphology, fields, action availability, frame rate, sequence length, and license. Compare random initialization, action-labeled-only pretraining, and full mixed data with `[M]` under equal capacity and budget. During fine-tuning, save complete curves and stratify success, speed error, foot clearance, slip, impulse, saturation, and termination by terrain. Audit Kp/Kd amplitude, rate, sustained high stiffness, and impact correlation. Hardware hikes require route, surface, slope, weather, payload, endurance, falls, interventions, shutdowns, and post-test inspection—not only traveled distance.
