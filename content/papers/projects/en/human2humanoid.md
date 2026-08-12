# human2humanoid: the shared H2O and OmniH2O tracking repository

[中文版](../human2humanoid.md)

Reviewed snapshot: [LeCAR-Lab/human2humanoid@`750f1fa052641f0fde43669d50cb4e407dabe6c8`](https://github.com/LeCAR-Lab/human2humanoid/tree/750f1fa052641f0fde43669d50cb4e407dabe6c8), 1,050 stars at the 2026-08-12 snapshot. The main project is marked CC BY-NC 4.0; dependencies, motions, models, and robot assets retain separate terms. Stars are not evidence of teleoperation latency, stability, or hardware safety.

## Why it is included

human2humanoid hosts the training paths for both H2O and OmniH2O. H2O maps RGB human pose to H1 whole-body tracking. OmniH2O reduces commands to head and two hands and uses a privileged teacher plus DAgger to train a history-based student without explicit global linear velocity.

The repository connects motion data, H1 task configuration, PPO/DAgger runners, and teacher labels in one traceable chain. H2O and OmniH2O still use different observation contracts and evidence boundaries; sharing a repository does not make their claims interchangeable.

## Problem addressed

Real-time whole-body teleoperation combines human references, robot proprioception, and uncertain latency into a fixed observation vector. Global linear velocity is trivial in simulation but depends on MoCap, VIO, or estimation on hardware. Treating it as ground truth during training can cause a deployment failure.

H2O uses sim-to-data filtering: a privileged imitator rejects retargeted motions that are hard for the robot. OmniH2O then lets a teacher generate action labels from privileged state while a student uses 25 frames of proprioception and previous actions to compensate for removed velocity information.

## Architecture and data flow

H2O follows `human pose → retargeted robot motion → privileged simulator filter → PPO full-body tracking → H1 policy`. OmniH2O follows `head/hand goals + privileged state → teacher action → rollout labels → DAgger student with 25-step history → sparse-command policy`.

`LeggedRobot.step` is the timing junction. It executes actions, updates histories, calculates teacher actions, and places labels in rollout information. The runner passes that data to PPO's imitation optimizer. A mismatched history order, normalization, or action scale can reduce loss while teaching the wrong control contract.

## Code map

- [`H1TeleopCfg`](https://github.com/LeCAR-Lab/human2humanoid/blob/750f1fa052641f0fde43669d50cb4e407dabe6c8/legged_gym/legged_gym/envs/h1/h1_teleop_config.py) defines actor and privileged observations, 19 actions, delay and gains, and mass/CoM/push randomization.
- [`LeggedRobot.load_expert` and `step`](https://github.com/LeCAR-Lab/human2humanoid/blob/750f1fa052641f0fde43669d50cb4e407dabe6c8/legged_gym/legged_gym/envs/base/legged_robot.py) load the teacher, label states seen by the student, and maintain history variants with and without linear velocity.
- [`OnPolicyRunner.learn`](https://github.com/LeCAR-Lab/human2humanoid/blob/750f1fa052641f0fde43669d50cb4e407dabe6c8/rsl_rl/rsl_rl/runners/on_policy_runner.py) organizes rollouts and labels; [`PPO._optimize_kin`](https://github.com/LeCAR-Lab/human2humanoid/blob/750f1fa052641f0fde43669d50cb4e407dabe6c8/rsl_rl/rsl_rl/algorithms/ppo.py) minimizes student-teacher action error.
- [`compute_observations`](https://github.com/LeCAR-Lab/human2humanoid/blob/750f1fa052641f0fde43669d50cb4e407dabe6c8/legged_gym/legged_gym/envs/base/legged_robot.py) and teleoperation rewards are the entry points for checking joint, base, target-keypoint, and previous-action ordering.

## Minimal reproduction path

Pin the commit, Isaac Gym/CUDA, H1 assets, motion file, and observation variant. Load a pretrained teacher/student with few environments and print names, shapes, means, and scales for actor, privileged, history, keypoint target, and action tensors.

For OmniH2O, reproduce the same 20 standing-motion comparison and add turns, fast hand motion, body occlusion, and delay injection. Report tracking error, failure categories, history ablations, and multiple seeds. A demonstration video is not a substitute for these measures.

## Capability boundaries

H2O's “RGB-only” describes the human command input; the paper still obtains robot global linear velocity from external MoCap. OmniH2O shows that history can omit explicit global linear velocity in its H1, 19-DoF, 50 Hz setup. It does not prove that every robot or dynamic motion needs no velocity estimator.

Different configurations retain velocity, history, and privileged-information variants. Without the exact configuration, a reported number cannot be assigned to a known observation contract.

## Engineering assessment and risks

The reusable design is placing teacher actions and student history in the same rollout semantics while making velocity dependence explicit. The main hazards are privileged leakage and changing history or action order after export without contract tests.

Hardware teleoperation needs handling for human-input loss, pose jumps, delay, position/velocity/torque limits, self-collision, impact, and a physical emergency stop. Begin with fixed commands, low speed, and supported or suspended tests before expanding the human command range.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/LeCAR-Lab/human2humanoid/tree/750f1fa052641f0fde43669d50cb4e407dabe6c8)
- [Teacher, history, and observation implementation](https://github.com/LeCAR-Lab/human2humanoid/blob/750f1fa052641f0fde43669d50cb4e407dabe6c8/legged_gym/legged_gym/envs/base/legged_robot.py)
- [OmniH2O English deep read](../../en/omnih2o-2406.08858v1.md) and [H2O English deep read](../../en/human2humanoid-2403.04436.md)
