# OpenLoong Dynamics Control: a readable MPC plus prioritized-WBC humanoid stack

[中文版](../openloong-dyn-control.md)

Reviewed snapshot: [loongOpen/OpenLoong-Dyn-Control@`4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e`](https://github.com/loongOpen/OpenLoong-Dyn-Control/tree/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e), 350 stars at the 2026-08-12 snapshot, Apache-2.0. Stars are only a discovery signal, not confidence in control correctness or hardware safety. The repository is cited as software and has no single paper covering its complete implementation.

## Why it is included

OpenLoong exposes a classical model-based humanoid chain: state estimation, gait scheduling, foot placement, model predictive control (MPC), priority-based whole-body control (WBC), and joint commands. Compared with a black-box policy repository, it lets a reader trace desired quantities, constraints, and outputs through a shared data bus.

It belongs to locomotion and loco-manipulation WBC. Its role is a readable engineering anchor for model-based control, not a claim of state-of-the-art performance. The project reports walking and blind obstacle stepping on the Qinglong prototype, while the publicly reproducible path is primarily MuJoCo.

## Problem addressed

Dynamic walking needs a lower-rate horizon planner for future contacts and forces, a higher-rate controller for instantaneous full-body dynamics and task priorities, and faster joint servo execution. One monolithic QP mixes horizon planning with instantaneous constraints, while fully independent layers can produce incompatible desired forces. OpenLoong connects modules through `DataBus` with explicit read-compute-write order.

MPC generates desired state and contact force from a reduced centroidal model. WBC computes generalized acceleration and torque at the current instant. Foot placement, gait scheduling, and estimation provide phase and feedback. This separation supports module-level debugging but creates cross-rate, frame, sign, and latency contracts that must be verified.

## Architecture and data flow

The loop is `MuJoCo sensors → StateEst/PinoKinDyn → GaitScheduler plus FootPlacement → MPC → WBC_priority → joint PVT command → MuJoCo`. `walk_mpc_wbc.cpp` schedules modules at different frequencies, and DataBus carries base state, feet, desired trajectories, contact state, and outputs. The README describes MPC at 100 Hz, MRT/WBC/estimation at 500 Hz, and joint PD above 1 kHz.

WBC uses prioritized tasks and QP. The documented ordering includes redundant joints, static contact, torso orientation/height, horizontal position, swing leg, and hand tracking. Reordering changes the feasible subspace; it is not cosmetic configuration. MPC, WBC, and servo layers must also agree on contact and sign conventions.

## Code map

- [`demo/walk_mpc_wbc.cpp`](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/demo/walk_mpc_wbc.cpp) connects estimation, gait, MPC, WBC, and joint commands at their scheduled rates.
- [`MPC`](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/algorithm/mpc.cpp) builds the receding-horizon problem and returns contact-related control quantities.
- [`WBC_priority`](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/algorithm/wbc_priority.cpp) implements task priorities and full-body dynamics solving.
- [`PriorityTasks`](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/algorithm/priority_tasks.cpp) exposes task matrices, PD targets, and stacking logic.
- [`StateEst`](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/algorithm/StateEst.cpp) produces feedback needed to close the control loop.

## Minimal reproduction path

Pin the Ubuntu/compiler environment, repository commit, and bundled dependency versions. Build and run `walk_wbc`, then `walk_mpc_wbc`. Preserve the robot model, joint-control JSON, MPC weights, WBC task order, gait period, and simulation step. Repeat the same initial state enough times to check deterministic behavior.

Acceptance should record MPC and WBC solve times and status, QP infeasibility, contact-force and friction-cone margin, foot slip, CoM and torso error, joint torque/velocity saturation, and missed deadlines. Add regressions for issues named in the changelog: sensor IDs, MPC matrix dimensions, and first-priority computation.

## Capability boundaries

Public examples focus on Qinglong, walking, blind obstacle stepping, and jumping. They do not establish a generic biped or loco-manipulation product. Bundled MuJoCo and Pinocchio may differ from upstream releases. The model-replacement tutorial helps migration but cannot infer correct inertias, contacts, task dimensions, or gains for a new robot.

The hardware statements are project reports without a common failure rate, disturbance envelope, or public hardware logs. Estimation, contact switching, and passive-ankle assumptions materially affect stability. Simulation parameters cannot be copied to robots with different motors, transmissions, and compliance.

## Engineering assessment and risks

The repository’s strongest value is modular readability and direct access to classical WBC debugging, especially the path from planned references into an instantaneous QP. Production use needs solver-status monitoring, infeasibility fallback, contact consistency, real-time deadline checks, dimension assertions, and parameter manifests. Historical fixes demonstrate how matrix and sensor-index errors alter behavior.

Hardware requires robot-specific dynamics and actuator calibration, strict position/velocity/torque limits, validated estimation and contact detection, support or suspension, low-speed and low-gain commissioning, and a physical emergency stop. A feasible QP is not a safety proof. This review provides no deployment-ready parameters.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/loongOpen/OpenLoong-Dyn-Control/tree/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e)
- [Model replacement tutorial](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/Tutorial.md)
- [Apache-2.0 license](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/4dd7a7e42a9cfd588afc78f3e429998ed8a30f4e/LICENSE)
