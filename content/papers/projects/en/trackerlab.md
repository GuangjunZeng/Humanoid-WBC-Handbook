# trackerLab: connecting retargeting, tracking, skill graphs, and deployment interfaces

[中文版](../trackerlab.md)

Reviewed snapshot: [Renforce-Dynamics/trackerLab@`1e5ccc062b445712a0aa7308cfb99edd7296cc88`](https://github.com/Renforce-Dynamics/trackerLab/tree/1e5ccc062b445712a0aa7308cfb99edd7296cc88), 243 stars at the 2026-08-12 snapshot, MIT. Stars are a discovery gate, not technical confidence. The repository itself warns that a major restructure has made parts of the README and tutorial stale.

## Why it is included

trackerLab has no single corresponding paper, but it attempts to connect SMPL/FBX/AMASS retargeting, Isaac Lab trajectory tracking, finite-state-machine (FSM) skill composition, and deployment-side motion management. It is better understood as a cross-embodiment tracker workbench than a single algorithm implementation, so it is relevant to both retargeting and universal tracking.

Its value comes from inspectable configuration and code boundaries: joint mapping, data formats, skill transitions, and deployment interpolation can be traced. The same breadth creates risk, because documentation can drift from a rapidly restructured implementation. This review therefore pins one commit and treats current source code as the primary evidence.

## Problem addressed

Motion tracking stacks are often assembled from incompatible repositories: one script retargets human motion, another trains a task, a third performs sim-to-sim validation, and the real-robot side has a separate state machine. Coordinate conventions, joint order, sample rate, and command semantics can be lost at each boundary. trackerLab uses manager-based organization and configuration files to make those boundaries explicit across several humanoid models.

Unification does not remove errors, but it can make them localizable. If an NPZ looks correct in a viewer and fails inside Isaac Lab, observations, rewards, or reset conditions become likely suspects. If simulation succeeds and deployment fails, joint remapping, interpolation, timing, and actuator semantics should be examined before changing the learning algorithm.

## Architecture and data flow

The practical flow is `human motion → poselib retarget/alignment → NPZ plus configuration → trackerTask/Isaac Lab task → RSL-RL training → policy/checkpoint → deploylib/sim2simlib → FSM skill composition`. `source/poselib` contains skeleton and retargeting utilities, `source/trackerTask` contains task integration, and `source/deploylib` contains runtime motion state and interpolation. Script families provide data inspection, training, evaluation, and simulation entry points.

The FSM layer selects and blends motion states; it does not prove that one policy has learned every listed skill. The retargeting configuration defines the reference consumed by training. These are separate claims: one concerns when a motion is invoked, and the other concerns what trajectory the controller receives. Calling the combined framework a universal controller without task-level evidence would overstate the code.

## Code map

- [`RetargetingProcessor`](https://github.com/Renforce-Dynamics/trackerLab/blob/1e5ccc062b445712a0aa7308cfb99edd7296cc88/source/poselib/poselib/retarget/retargeting_processor.py) handles T-poses, base retargeting, and motion adjustment at the human-to-robot boundary.
- [`DeployManager.step`](https://github.com/Renforce-Dynamics/trackerLab/blob/1e5ccc062b445712a0aa7308cfb99edd7296cc88/source/deploylib/deploylib/deploy_manager/deploy_manager.py) owns motion state, FSM motion identifiers, interpolation, and per-cycle outputs.
- [`GMR_to_npz.py`](https://github.com/Renforce-Dynamics/trackerLab/blob/1e5ccc062b445712a0aa7308cfb99edd7296cc88/source/deploylib/scripts/data_fk/GMR_to_npz.py) converts external retargeting results into robot-aware training data through forward kinematics.
- [`data_flow.md`](https://github.com/Renforce-Dynamics/trackerLab/blob/1e5ccc062b445712a0aa7308cfb99edd7296cc88/docs/data_flow.md) documents intended interfaces, but must be checked against source because of the restructure warning.

## Minimal reproduction path

Start with the pinned commit and a fixed Isaac Lab environment. Download a versioned asset set, load one short motion in the data viewer, and verify T-pose orientation, joint names, frame rate, and foot height. Run one registered tracking task with fixed seed, configuration, and environment count. Reproduce the checkpoint in the Isaac Lab play path before moving to MuJoCo sim-to-sim.

At each boundary, record tensor shapes and joint order, policy observation/action dimensions, training and inference periods, errors before and after motion transitions, and sim-to-sim root height, orientation, foot slip, and failure rate. Claims of being self-contained should be reconciled with the actual asset and robot-library dependencies at the reviewed commit.

## Capability boundaries

The repository describes several robots and control modes, but examples, configuration completeness, and documentation freshness vary. The presence of a configuration file is not proof that a robot has been trained and deployed successfully. Demonstration videos are useful qualitative evidence but do not establish transition robustness or comparative performance.

The repository also contains or references third-party modules. License, version, and local modifications must be reviewed per directory. Because the project is undergoing restructuring, command paths may change after this snapshot. The pinned links are reliable for this review only; they should not be silently projected onto the current default branch.

## Engineering assessment and risks

trackerLab is most useful as an interface-alignment test bed, not as evidence for a new validated control algorithm. It can support controlled comparisons of data conversion, task definitions, and deployment paths. For a durable baseline it still needs a versioned task matrix, minimal CI, checkpoint-to-configuration manifests, and reproducible evaluation reports.

Hardware use requires independent simulation, output limiting, exact joint mapping, timing checks, initial-state checks, and transition testing. Commission with support or suspension, an operational emergency stop, conservative gains, and small motion envelopes. FSM transitions can introduce discontinuous references and need blending, timeout, and fallback behavior. This review provides neither safety parameters nor authorization to deploy.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/Renforce-Dynamics/trackerLab/tree/1e5ccc062b445712a0aa7308cfb99edd7296cc88)
- [Project structure documentation](https://github.com/Renforce-Dynamics/trackerLab/blob/1e5ccc062b445712a0aa7308cfb99edd7296cc88/docs/project_structure.md)
- [Recorded project problems](https://github.com/Renforce-Dynamics/trackerLab/blob/1e5ccc062b445712a0aa7308cfb99edd7296cc88/docs/problems.md)
