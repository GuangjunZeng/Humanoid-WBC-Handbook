# Periodic Reward Composition: Gait Timing Without Joint-by-Joint Reference Tracking

[中文版](../periodic-gaits-2011.01387v2.md)

Source: [arXiv:2011.01387v2](https://arxiv.org/abs/2011.01387v2). Code facts refer to the pinned official APEX revision linked by the Chinese page.

> **Bottom line:** The paper describes stance and swing as periodic expectations over foot force and foot velocity, then composes those clocks to train standing, walking, running, hopping, and skipping. It reduces dependence on dense motion references but does not remove phase design, reward tuning, or sim-to-real validation.

## Engineering problem
Dense reference trajectories constrain every joint and require new motion data for each gait. Hand-written sparse rewards, however, often fail to encode when each foot should support or move.

## Method
A phase variable defines smooth periodic coefficients for stance-force and swing-velocity objectives. Relative phase, duty factor, and cycle duration generate different bilateral gait patterns; task terms then regulate speed and orientation. The policy remains free to choose joint trajectories inside that contact rhythm.

## Key figures
![Figures 1-2: common Cassie gaits](../assets/periodic-gaits-2011.01387/figure-1-2-gaits.jpg)
The sequence establishes that one reward grammar can express several gait families and transitions.
![Figures 3-4: phase and contact coefficients](../assets/periodic-gaits-2011.01387/figure-3-4-phase.jpg)
These are the semantic core: they show exactly when force and foot velocity are rewarded or penalized.
![Table I and Figure 5: transfer](../assets/periodic-gaits-2011.01387/table-1-figure-5-transfer.jpg)
The randomization table and sim/real force comparison bound the zero-shot transfer claim.

## Decisive evidence
The most useful evidence is continuous switching among gaits on Cassie hardware plus measured force patterns. It supports a shared contact-timing abstraction, not unrestricted motion generation.

## Paper-to-implementation mapping
The pinned APEX code exposes Cassie state/action handling, phase clocks, reward terms, dynamics randomization, and trained-model configuration. Phase convention and control decimation must match the reward implementation exactly.

## Limits and evidence boundary
A clock can become misaligned after slip, delay, or disturbance. Smooth reward freedom may admit high torque, impact, or awkward posture unless separately constrained. Cassie results do not directly cover upper-body humanoids or contact-rich tasks.

## Bounded engineering takeaway
Use periodic contact rewards when rhythm matters more than pose imitation. Keep phase/contact plots, task performance, torque, and impact as separate diagnostics so a high total reward cannot hide a physically poor gait.

## Reproduction checklist
Lock phase convention, cycle/duty factors, smoothing, force/velocity signs, reward weights, action rate, PD, randomization, estimator, and hardware limits. Compare dense-reference, task-only, and periodic rewards; report transitions, contacts, slip, torque, impact, and real interventions.
