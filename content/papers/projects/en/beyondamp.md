# beyondAMP: modular adversarial motion priors for Isaac Lab and MJLab

[中文版](../beyondamp.md)

Reviewed snapshot: [Renforce-Dynamics/beyondAMP@`cee88cdc0958c417e316f9452f802e25a71bc289`](https://github.com/Renforce-Dynamics/beyondAMP/tree/cee88cdc0958c417e316f9452f802e25a71bc289), 281 stars at the 2026-08-12 snapshot. Official GitHub metadata did not assert a repository-wide license, so terms must be checked per directory before reuse. Stars are discovery metadata, not technical confidence or safety evidence.

## Why it is included

beyondAMP is not presented as a new paper. It extracts the dataset, discriminator, observation group, environment wrapper, and runner needed for Adversarial Motion Priors (AMP) into components intended for different robot tasks. It supports both Isaac Lab/PhysX and MJLab/MuJoCo-Warp, which makes it a useful engineering baseline for testing what a motion-style prior contributes.

It relates to locomotion, motion generation, and recovery/safety because AMP shapes movement style alongside task rewards and can change the state distribution visited by a policy. Inclusion does not mean the project has demonstrated recovery or superiority to tracking methods. Demonstrations must be interpreted through their exact task and configuration.

## Problem addressed

Locomotion rewards often combine hand-designed velocity, posture, foot, energy, and smoothness terms, yet the result can still look unnatural. AMP trains a discriminator on state transitions from reference motion and turns “looks like the data” into an additional reward. The engineering difficulty is that expert and policy transitions must agree in timing, joint order, normalization, and observation definition.

beyondAMP separates this machinery from one robot task so an existing Isaac Lab or MJLab environment can add an `amp` observation group and wrapper. Modularity reduces integration work but raises a silent-failure risk: a misordered feature vector may still let the discriminator optimize while rewarding the wrong statistics.

## Architecture and data flow

The flow is `NPZ motion → MotionDataset/WeightedMotionDataset → AMP observation builder → AMPEnvWrapper → policy and expert transitions → AMPDiscriminator → style reward → AMPOnPolicyRunner`. The base task still provides task reward. The discriminator does not replace command tracking, contact constraints, termination, or hardware limits.

Isaac Lab and MJLab have separate wrappers and observation implementations while reusing data and discriminator logic. Basic, soft-tracking, and hard-tracking examples change how strongly the reference constrains behavior. Backend comparisons must preserve transition rate, frame transformations, and normalization; otherwise differences cannot be attributed to physics.

## Code map

- [`AMPDiscriminator`](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/source/beyondAMP/beyondAMP/modules/amp_discriminator.py) implements the discriminator, its loss, and conversion into style reward.
- [`MotionDataset`](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/source/beyondAMP/beyondAMP/motion/motion_dataset.py) loads reference motion and constructs transitions.
- [Isaac Lab `AMPEnvWrapper`](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/source/beyondAMP/beyondAMP/isaaclab/rsl_rl/amp_wrapper.py) connects observations, next state, and AMP reward to RSL-RL.
- [MJLab `AMPEnvWrapper`](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/source/beyondAMP/beyondAMP/mjlab/rsl_rl/amp_wrapper.py) is the corresponding second-backend adapter.
- [`amp_obs_anchor_group`](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/source/beyondAMP/beyondAMP/obs_groups/amp_obs_anchor.py) makes the anchor-based discriminator input explicit.

## Minimal reproduction path

Pin the repository, Isaac Lab or MJLab, RSL-RL, and robot assets. Run a small-environment smoke test for `beyondAMP-DemoPunch-G1-BasicAMP`. Log every expert and policy AMP field, tensor shape, mean, variance, and transition interval. Verify that shuffled or time-reversed transitions change discriminator behavior before starting a full training run.

A minimal ablation includes task-only, AMP, soft tracking, and hard tracking under fixed seed, environment count, training steps, and task reward. Report task return, style reward, discriminator accuracy, action saturation, root posture, foot slip, termination causes, and multiple seeds. Reproduce the data contract on the second backend to separate algorithm and simulator effects.

## Capability boundaries

AMP makes selected policy features resemble the reference distribution. It does not guarantee semantic correctness, contact quality, or hardware safety. If motion data contain foot slip, penetration, or high impacts, the discriminator may reward those artifacts. Recommendations to use GMR or TrackerLab are workflow hints, not certification of every input sequence.

There is no uniform benchmark across all robots, backends, and motions. Examples use specific G1 configurations, and MJLab needs additional installation. The two backends are not fully interchangeable through one command. Because repository-wide license metadata are unclear, citations and acknowledgements cannot substitute for license review.

## Engineering assessment and risks

The most reusable elements are the explicit expert-transition contract and two backend adapters. The main hazard is treating style reward as a proxy for naturalness or safety. A new embodiment integration should include field-level unit tests, shuffled-joint and reversed-time negative controls, reference replay, and tools showing which features drive the discriminator.

Hardware policies need separate collision, joint, velocity, torque, impact, posture, and communication-timeout safety layers. Use independent sim-to-sim, then supported or suspended low-gain tests with an emergency stop. AMP may encourage highly dynamic motions present in the dataset; a higher reward is never a reason to relax hardware limits. This page provides no deployment parameters.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/Renforce-Dynamics/beyondAMP/tree/cee88cdc0958c417e316f9452f802e25a71bc289)
- [Official integration tutorial](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/docs/tutorial.md)
- [MJLab G1 task configuration](https://github.com/Renforce-Dynamics/beyondAMP/blob/cee88cdc0958c417e316f9452f802e25a71bc289/source/amp_tasks_mjlab/amp_tasks_mjlab/velocity/g1/amp_env_cfg.py)
