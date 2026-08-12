# ProtoMotions 3: a unified research framework for humanoid motion learning, simulation, and deployment

[中文版](../protomotions.md)

Reviewed snapshot: [NVlabs/ProtoMotions@`5241478e35a7dcf5d1455dac2df0486d5e7f440a`](https://github.com/NVlabs/ProtoMotions/tree/5241478e35a7dcf5d1455dac2df0486d5e7f440a), 2,286 stars at the 2026-08-12 snapshot, Apache-2.0. SMPL and SMPL-H, Unitree and BeyondMimic material, simulator dependencies, models, datasets, and other third-party assets retain their own terms. Stars are a discovery signal, not confidence in algorithmic correctness, experimental reproducibility, or hardware safety.

## Why it is included

ProtoMotions is not one WBC algorithm. It places motion data, robot definitions, simulator adapters, reinforcement-learning agents, observation, reward and termination components, evaluation, and deployment interfaces inside one engineering framework. It is official code associated with CALM's controllable latent skills and MaskedMimic's masked motion inpainting, while the current version-three snapshot also contains general tracking, GPC and PEFT paths, cross-simulator tests, and a G1 deployment route. That makes it a useful map from paper ideas to a composable system.

This review evaluates the architecture at one commit. It does not treat the README's reports of more than forty hours of AMASS training data, four or twenty-four A100 GPUs, roughly 142,000 BONES-SEED motions, twelve-hour training, or zero-shot hardware demonstrations as independently reproduced results. Those are author-reported capabilities. Experimental confidence requires pinning datasets, configurations, hardware, seeds, checkpoints, and evaluation code and then rerunning the claims.

## Problem addressed

The recurring difficulty in motion-control research is not simply the absence of PPO. Different papers use incompatible motion formats, skeletons, observation contracts, rewards, simulators, logging, and termination rules. Comparing AMP, ASE, mimic, MaskedMimic, and latent-skill methods becomes unreliable, and changing from an SMPL character to H1_2 or G1 can silently alter frames, joint ordering, scaling, or gains. ProtoMotions attempts to expose these differences through shared context views and explicit component bindings.

It also attempts to reduce training-to-deployment observation drift. The exporter can place exportable observation computation and the policy in one ONNX artifact and generate a YAML description of inputs and outputs. The standalone MuJoCo tester reconstructs those inputs from raw simulator state, runs the policy, produces PD position targets, and advances physics. This is a valuable contract, but a successful export does not establish equivalent sensor calibration, timing, actuator bandwidth, or safety state machines on hardware.

## Architecture and data flow

The training route is `motion source → retargeted or packaged motion → RobotConfig and simulator → EnvContext → control components → observation, reward, and termination MdpComponents → PPO, AMP, mimic, or supervised latent agent → checkpoint and evaluation`. An experiment selects components rather than copying a monolithic environment class. Each pure tensor function binds its arguments to `FieldPath` values; runtime state comes from the live context while fixed constants remain static component parameters.

The steering example makes this concrete. `SteeringControl` owns target direction, target speed, and facing state. `compute_steering_obs` expresses the target in the robot-local frame. `compute_heading_velocity_rew` combines travel-direction and facing rewards. The experiment connects them as `MdpComponent` objects. The result resembles an inspectable control-system patch panel: every signal has a named source and destination, which is easier to replace and export than implicit access through a deep inheritance hierarchy.

For MaskedMimic, the control component maintains future target times and pose and body visibility masks. The model's prior predicts a deployable latent distribution from sparse observations. During training, a privileged encoder supplies a residual posterior, and a shared trunk decodes latent samples into actions. The current version-three classes implement ideas related to the 2024 paper but have been substantially reorganized; their presence must not be used to claim that every original paper table is reproduced by the current head.

The deployment route is `checkpoint and experiment configuration → MockContext and MdpComponent bindings → ONNX policy containing the observation graph plus a YAML contract → raw MuJoCo or robot state → quaternion and body-index conversion → policy inference → PD targets → simulator or hardware adapter`. It is an implementation route and example, not a third-party-certified functional-safety control stack.

## Code map

- [`MdpComponent`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/envs/mdp_component.py) separates dynamic `FieldPath` bindings, static parameters, and metadata, and exposes `get_bindings_dict()` to the ONNX path.
- [`EnvContext` and domain views](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/envs/context_views.py) define explicit current, historical, mimic, masked-mimic, steering, and other data contracts.
- [The steering `env_config`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/examples/experiments/steering/mlp.py) shows control, observation, and reward kernels wired through context paths.
- [`compute_heading_velocity_rew`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/envs/rewards/task.py) is a pure tensor task-reward kernel whose inputs, projections, and weights can be inspected separately.
- [`MaskedMimicControl`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/envs/control/masked_mimic_control.py) owns target times, pose and body masks, and sparse conditioning context.
- [`MaskedMimicModel`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/protomotions/agents/supervised/masked_mimic_model.py) separates the deployable prior, privileged training encoder, latent sampling, and shared action trunk.
- [`export_tracker`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/deployment/export_bm_tracker_onnx.py) derives ONNX inputs from component bindings, optionally compares onnxruntime results, and writes a YAML sidecar.
- [`run` and `build_onnx_inputs`](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/deployment/test_tracker_mujoco.py) expose the connection among raw MuJoCo state, quaternion order, body indices, history, inference, PD targets, and control decimation.

## Minimal reproduction path

First validate framework contracts without launching a large training job. Pin this commit, Python and CUDA, one simulator backend, and the license-compatible G1 or H1_2 assets. Run the smallest simulator tutorial and then pretrained mimic inference. Record the resolved `RobotConfig`, body and joint order, physics step, control decimation, observation dimensions, action scale, PD gains, and checkpoint hash. Dimension or naming mismatches should fail before long training starts.

Second, train a mimic MLP on a small motion subset. Inspect motion playback and contact consistency first. Use at least three seeds and report learning curves, success, rigid-body position and rotation errors, foot sliding, fall causes, and throughput instead of publishing only the best rollout. A MaskedMimic study should progress from dense full-body conditioning to sparse keyframes, partial bodies, and fully hidden intervals. It must verify that prior-only inference receives no privileged training information.

Third, test deployment explicitly. Export ONNX and compare PyTorch and onnxruntime outputs. Run the same motion in the training simulator and MuJoCo, aligning quaternion convention, body indices, joint signs, update rates, history, stiffness, and damping. Hardware trials require a harness or gantry, emergency stop, low initial gains, position and torque limits, fall detection, communication timeout, and direct supervision. Every safety event should retain synchronized observation and command logs.

## Capability boundaries

ProtoMotions does not make contact, friction, actuator, or integrator models equivalent across simulators. A passing sim-to-sim test does not prove sim-to-real transfer. The README's scale claims depend on high-end GPUs, particular datasets, and particular configurations and do not describe a generic workstation requirement. Support maturity also differs among Isaac Gym, Isaac Lab, Newton, MuJoCo, and Genesis; the repository itself marks Genesis as not fully tested, so an adapter directory is not equal evidence for every backend.

Apache-2.0 covers the project's own code, not every SMPL or SMPL-H model, robot mesh, dataset, pretrained checkpoint, or simulator. ProtoMotions 3 is newer than the experiment snapshots behind CALM and MaskedMimic. Reproducing those papers requires their version-specific records rather than assuming that current `main` preserves every historical configuration and metric.

The framework is also not a complete product WBC. It does not perform sensor calibration, real-actuator identification, thermal and current protection, venue risk assessment, or system-level fault recovery for the user. Author demonstrations of zero-shot G1 transfer are evidence for the reported setup, not a universal promise for arbitrary hardware, firmware, payloads, or floors.

## Engineering assessment and risks

The strongest reusable idea is an auditable data contract. Observation, reward, and termination logic can remain pure tensor computation; runtime values arrive through explicit `FieldPath` bindings; and the same bindings support ONNX export. This reduces the risk of using one implicit Python observation in training and a manually rewritten C++ observation at deployment, although numerical regression tests are still required to prove equivalence.

The largest risk is mistaking a unified framework for a unified benchmark. Algorithms are not fairly compared merely because they share a repository when motion sets, robots, conditioning information, network sizes, compute budgets, and termination rules differ. A second risk is version confusion: version-three refactoring cannot be projected backward as evidence for the original CALM or MaskedMimic experiments. A third is moving directly from visually attractive simulation to hardware, where aggressive whole-body motion can cause self-collision, support loss, overcurrent, or mechanical damage.

The review level here is therefore “architecture and interfaces inspected at a fixed commit,” not “all algorithms and README performance claims reproduced.” Every hardware-bound policy still needs independent motion cleaning, contact and dynamics tests, cross-simulator checks, and a qualified safety review.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/NVlabs/ProtoMotions/tree/5241478e35a7dcf5d1455dac2df0486d5e7f440a)
- [Apache-2.0 license at the reviewed commit](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/LICENSE.md)
- [Third-party asset exclusions at the reviewed commit](https://github.com/NVlabs/ProtoMotions/blob/5241478e35a7dcf5d1455dac2df0486d5e7f440a/pyproject.toml)
- [MaskedMimic primary paper](https://arxiv.org/abs/2409.14393)
- [CALM primary paper](https://arxiv.org/abs/2305.02195)
