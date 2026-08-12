# TSID: task-space inverse dynamics built on Pinocchio

[中文版](../tsid.md)

Reviewed snapshot: [stack-of-tasks/tsid@`eae96180ed8d289bc2c634f9d0857020ebfa6d90`](https://github.com/stack-of-tasks/tsid/tree/eae96180ed8d289bc2c634f9d0857020ebfa6d90), 345 stars at the 2026-08-12 snapshot, BSD-2-Clause. Stars are a discovery signal, not proof of solver correctness, real-time performance, or hardware safety.

## Why it is included

TSID, Task Space Inverse Dynamics, is a direct open implementation anchor for optimization-based Whole-Body Control (WBC). It goes beyond a QP equation by connecting robot models, motion tasks, rigid contacts, force and actuation limits, hierarchical QP (HQP) solvers, and Python bindings in one inspectable library.

The repository includes manipulator, humanoid, and quadruped exercises. It is useful for answering how tasks and contacts actually enter a solver, but it is not a complete robot-control stack. State estimation, contact-transition planning, actuator identification, hardware I/O, and safety supervision remain integration responsibilities.

## Problem addressed

Multi-contact humanoid control must combine rigid-body dynamics, support forces, center-of-mass, end-effector and posture tasks, plus joint and torque limits. When every project rewrites Jacobians, constraint packing, and solver adapters, errors hide in dimensions, frames, and priority levels.

TSID turns those concepts into typed `TaskMotion`, `ContactBase`, `Constraint*`, and `SolverHQP*` objects. The user supplies q/v and task references; the formulation builds hierarchical QP data and a solver returns accelerations, contact forces, and actuator quantities. Reuse improves, but feasibility is not automatic.

## Architecture and data flow

The typical flow is `URDF/Pinocchio model + q,v → task/contact computation → InverseDynamicsFormulationAccForce::computeProblemData → HQPData → SolverHQP::solve → accelerations/contact forces/torques`. Motion tasks include SE(3) end effectors, CoM, angular momentum, and joint posture. Inequalities cover joint, velocity, acceleration, or actuation bounds.

`priorityLevel` selects the hierarchy level, while weights trade objectives within a level. This distinction matters: placing a safety constraint as a low-weight soft task has a different failure mode from placing it in a high-priority inequality.

## Code map

- [`InverseDynamicsFormulationAccForce::computeProblemData`](https://github.com/stack-of-tasks/tsid/blob/eae96180ed8d289bc2c634f9d0857020ebfa6d90/src/formulations/inverse-dynamics-formulation-acc-force.cpp) updates Pinocchio data, computes tasks and contacts, and assembles HQP levels. The same file implements `addMotionTask` and `addRigidContact`.
- [`TaskSE3Equality::compute`](https://github.com/stack-of-tasks/tsid/blob/eae96180ed8d289bc2c634f9d0857020ebfa6d90/src/tasks/task-se3-equality.cpp) converts current and reference SE(3) states into a six-dimensional motion constraint.
- [`TaskActuationBounds::compute`](https://github.com/stack-of-tasks/tsid/blob/eae96180ed8d289bc2c634f9d0857020ebfa6d90/src/tasks/task-actuation-bounds.cpp) creates actuator bounds; their numerical values still come from robot-specific configuration.
- [`tsid_biped.py`](https://github.com/stack-of-tasks/tsid/blob/eae96180ed8d289bc2c634f9d0857020ebfa6d90/exercizes/tsid_biped.py) shows how biped contacts, CoM, angular momentum, posture, feet, and joint bounds are assembled.

## Minimal reproduction path

Install pinned TSID, Pinocchio, and solver dependencies through Conda or robotpkg. Begin with a Python manipulator exercise and validate q/v dimensions, references, HQP status, and integration without hardware. Then run the biped-balance example and log solver status, task residuals, constraint violations, contact forces, and the solve-time distribution every frame.

A minimal ablation adds posture, SE(3), CoM, contact, and actuation bounds one by one, recording where infeasibility or conditioning deteriorates. Deliberately create conflicting tasks and confirm that the system reports failure or enters a designed degradation mode instead of emitting an unchecked control vector.

## Capability boundaries

TSID is an inverse-dynamics formulation and solver library, not a walking MPC, state estimator, contact planner, or robot driver. It can express contacts and force bounds, but friction coefficients, support polygons, torque limits, and model parameters are not automatically correct.

The companion paper's phrase “without joint-torque sensors” must not be read as “without any force sensing.” Its HRP-2 experiment still uses wrist/ankle six-axis force sensors, an IMU, and encoders. This repository is also not a packaged reproduction of the complete actuator-identification pipeline from that paper.

## Engineering assessment and risks

The most reusable elements are the task/contact/constraint contracts and solver adapters. The dangerous mistake is treating an `optimal` solver status as proof that an output is physically realizable. Model error, contact switching, rank loss, scaling, and integration drift all require upstream monitoring.

Hardware integration needs hard position, torque, power, and velocity limits; contact-force monitoring; solver-timeout and infeasibility fallbacks; estimator-health checks; and a physical emergency stop. Inject conflicts and timeouts in simulation, then use supported or suspended low-speed and low-force tests. This page contains no deployable gains or limits.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/stack-of-tasks/tsid/tree/eae96180ed8d289bc2c634f9d0857020ebfa6d90)
- [Official installation and examples](https://github.com/stack-of-tasks/tsid/blob/eae96180ed8d289bc2c634f9d0857020ebfa6d90/README.md)
- [English companion-paper deep read](../../en/torque-control-high-ratio-gearboxes-2016.md)
