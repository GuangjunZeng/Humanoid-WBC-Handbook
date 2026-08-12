# WBC-AGILE: an environment-verification, training, evaluation, and deployment loop for humanoid RL

[中文版](../wbc-agile.md)

Reviewed snapshot: [nvidia-isaac/WBC-AGILE@`7259792cf10803aab814d101134d493d24c8f22f`](https://github.com/nvidia-isaac/WBC-AGILE/tree/7259792cf10803aab814d101134d493d24c8f22f), 313 stars at the 2026-08-12 snapshot. Most code is Apache-2.0 and the RSL-RL portion is BSD-3-Clause. Corresponding paper: [AGILE, arXiv:2603.20147v1](https://arxiv.org/abs/2603.20147v1). Stars are discovery metadata, not confidence or safety certification.

## Why it is included

Initial screening treated WBC-AGILE as a project without a paper. The official repository and arXiv now provide the AGILE paper, so the catalog relationship is corrected to official paper code. A separate project page remains useful because the main contribution is an engineering workflow: interactive verification, reproducible training, unified evaluation, descriptor-driven deployment, and sim-to-MuJoCo regression.

It covers loco-manipulation WBC and universal tracking and includes stand-up, velocity/height tracking, dancing, and teleoperation tasks. The paper reports five skill categories on G1 and Booster T1. This page explains how the repository organizes evidence; experimental numbers and figures still require a full paper review.

## Problem addressed

Humanoid RL code may produce a training video while lacking environment sanity checks, fixed-scenario regression, randomized rollout statistics, or a portable deployment contract. Changing embodiment or action dimension can silently misalign observations, actions, joints, normalization, and runtime parsing. AGILE divides the policy lifecycle into inspectable stages and describes interfaces through YAML descriptors.

A second problem is evaluation only in the training simulator. AGILE provides sim-to-MuJoCo tools and common metrics before a checkpoint reaches hardware. This catches some simulator and runtime dependence; it does not prove sim-to-real. Its purpose is earlier failure detection with retained regression records.

## Architecture and data flow

The main flow is `task YAML/Python configuration → interactive play verification → scripts/train.py → checkpoint → scripts/eval.py scenario/random evaluation → IO descriptor export → sim2mujoco → robot/task descriptor deployment`. A teacher-student path uses privileged observations for the teacher and distills a deployable student, so the two input contracts must be tracked separately.

Data-recording tools store observations and actions in HDF5 and convert them to a GR00T-compatible layout, forming an interface between an upper-level model and a WBC policy. Their presence demonstrates integration intent, not that arbitrary VLA output satisfies low-level dynamic or safety constraints.

## Code map

- [`scripts/train.py`](https://github.com/nvidia-isaac/WBC-AGILE/blob/7259792cf10803aab814d101134d493d24c8f22f/scripts/train.py) is the main task, configuration, and RSL-RL training entry.
- [`scripts/eval.py`](https://github.com/nvidia-isaac/WBC-AGILE/blob/7259792cf10803aab814d101134d493d24c8f22f/scripts/eval.py) loads checkpoints and executes scenario and randomized evaluation.
- [`sim2mujoco_watcher.py`](https://github.com/nvidia-isaac/WBC-AGILE/blob/7259792cf10803aab814d101134d493d24c8f22f/scripts/sim2mujoco_watcher.py) monitors checkpoints and reports fall rate, survival time, and command-tracking errors.
- [`ActionProcessor`](https://github.com/nvidia-isaac/WBC-AGILE/blob/7259792cf10803aab814d101134d493d24c8f22f/agile/sim2mujoco/actions.py) turns descriptor action terms into joint commands at the cross-simulator boundary.
- [`HDF5DataRecorder`](https://github.com/nvidia-isaac/WBC-AGILE/blob/7259792cf10803aab814d101134d493d24c8f22f/scripts/data_recording/data_recorder.py) records observation/action episodes from multiple environments.

## Minimal reproduction path

Pin Isaac Lab 2.3.2, Isaac Sim 5.1, robot assets, and the reviewed commit. First use zero, random, or sinusoidal actions in `scripts/play.py` to verify joint directions, limits, and reset. Train a small-environment `Velocity-T1-v0` run and preserve resolved environment and agent configuration, seeds, dependency commits, and checkpoint manifest.

Run fixed scenarios and randomized rollouts through `scripts/eval.py`, retaining episode-level termination reasons. Export the IO descriptor and run `scripts/sim2mujoco_eval.py` or the watcher, verifying field order, normalization, action processing, and joint names. Hardware commissioning should start only after both simulators pass predeclared thresholds.

## Capability boundaries

Workflow portability is not zero-modification policy transfer. Each embodiment still requires assets, actuators, rewards, descriptors, and runtime adaptation. The paper’s five skill categories define a bounded validation set, not evidence that every repository task or GR00T integration has equivalent hardware results.

MuJoCo and Isaac Lab share some descriptors, but their contact, actuator, and sensor models may both differ from hardware. Privileged teacher observations must not leak into student deployment inputs. Recorded image, state, action, timestamp, and task-text streams also need synchronization checks.

## Engineering assessment and risks

AGILE’s strongest contribution is making regression evaluation a first-class artifact. A checkpoint should not be released with only a video; it should carry fixed scenarios, randomized rollout results, sim-to-sim metrics, and an IO contract. Single-file task configuration helps auditability, while shared functions and dependencies still require a complete CI-pinned snapshot.

Hardware requires descriptor schema validation, joint and unit checks, action limits, timeout fallback, an emergency stop, conservative gains and speeds, and support or suspension during commissioning. Upper-level generated tasks or actions must never bypass the low-level safety layer. Papers and videos are not safety certification, and this review provides no deployment parameters.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/nvidia-isaac/WBC-AGILE/tree/7259792cf10803aab814d101134d493d24c8f22f)
- [arXiv:2603.20147v1](https://arxiv.org/abs/2603.20147v1)
- [Repository license notice](https://github.com/nvidia-isaac/WBC-AGILE/blob/7259792cf10803aab814d101134d493d24c8f22f/LICENCE)
