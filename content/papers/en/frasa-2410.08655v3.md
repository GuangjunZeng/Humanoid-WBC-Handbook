# FRASA: One Symmetry-Reduced Policy for Disturbance Recovery and Stand-Up

[中文版](../frasa-2410.08655v3.md)

Source: [arXiv:2410.08655v3](https://arxiv.org/abs/2410.08655v3). Code mapping refers to the pinned official FRASA revision linked by the Chinese page.

> **Bottom line:** FRASA exploits Sigmaban's bilateral symmetry to reduce control to five sagittal joint groups, then trains one CrossQ/SAC policy from randomized fallen states to both reject disturbances and stand up. The same symmetry that accelerates learning excludes important lateral/asymmetric recovery.

## Engineering problem
Separate balance and stand-up controllers require a brittle switch between recoverable and fallen. Random fallen states make rewards sparse, and simplified actuator models create deployment oscillation even with domain randomization.

## Method
Five actions are mirrored to left/right joints. Velocity actions integrate into position targets and the observation includes targets and action history. Episodes settle from random physical poses, with some starts near the goal to propagate value. Randomization covers mechanics, actuator parameters, voltage, and explicit sensor delays.

## Key figures
![Figure 2: symmetric state/action contract](../assets/frasa-2410.08655v3/figure-2-state-action.jpg)
The unified claim is explicitly limited to a five-DoF sagittal subspace.
![Figure 4 and Table II: training and randomization](../assets/frasa-2410.08655v3/figure-4-training-table-2.jpg)
Fast training depends on the reduced problem, 16 MuJoCo environments, and the reported randomization/latency contract.
![Tables III-IV: hardware stand-up and pendulum tests](../assets/frasa-2410.08655v3/table-3-4-hardware.jpg)
Prone/supine trials use 20 repetitions each; pendulum conditions use 10, with a same-platform KFB baseline.

## Decisive evidence
Controlled hardware denominators show faster prone/supine stand-up and recovery from front/back pendulum impacts up to the tested 7.3 J condition. Side impacts and asymmetric starts are absent, matching the model's main boundary.

## Paper-to-implementation mapping
The pinned code exposes symmetric observation/control, velocity-to-position integration, safety termination, randomization/fall initialization, and CrossQ configuration. The paper's full hardware integration is not a one-command deployment package.

## Limits and evidence boundary
Authors report real oscillation requiring lower gains and 100 Hz inference instead of 20 Hz training, plus manual rejection of mechanically harsh policies. Impact energy is not a universal safety rating; peak load, contact location, and fatigue remain unreported.

## Bounded engineering takeaway
Use symmetry as an explicit baseline for sagittal small-humanoid recovery, and immediately test the excluded lateral/asymmetric ODD. Record every rejected policy and mechanical reason so survivor selection is reproducible.

## Reproduction checklist
Lock symmetry signs, state/action integration, reset distribution, near-goal probability, rewards, randomization, delays, gains, and rate. Report seed curves, prone/supine/lateral/diagonal starts, impact direction/energy, load peaks, oscillation, rejected checkpoints, and mechanical inspection.
