# humanoid-control: OCS2 NMPC, estimation, and weighted/hierarchical WBC in one interface

[中文版](../humanoid-control.md)

Reviewed snapshot: [pocketxjl/humanoid-control@`3b5ffec98d29827730194b0dbf2f119fb7b265ca`](https://github.com/pocketxjl/humanoid-control/tree/3b5ffec98d29827730194b0dbf2f119fb7b265ca), 412 stars at the 2026-08-12 snapshot, MIT. Stars are a discovery threshold, not correctness or hardware-safety confidence. The project builds on OCS2 and legged-control ideas but has no paper covering the complete repository.

## Why it is included

The repository connects NMPC, model-reference tracking, state estimation, gait switching, weighted and hierarchical WBC, PD output, and MuJoCo/ROS control nodes. Its README explicitly states optimization variables, constraints, and rates. It is a rare readable end-to-end model-based implementation in the locomotion and loco-manipulation WBC topics.

Inclusion is not a claim of industrial real-time performance or hardware validation. Public demonstrations are primarily MuJoCo, and the README warns that at least a `RelWithDebInfo` build is required for speed. Its best use is tracing an OCS2 NMPC reference into a 500 Hz WBC, not copying parameters to another robot.

## Problem addressed

Biped control must plan contact forces and centroidal motion while satisfying floating-base dynamics, friction, stance-foot constraints, swing trajectories, and torque limits. OCS2 SQP NMPC handles a finite horizon. WBC converts current optimized state and input into joint acceleration, contact force, and torque. A linear Kalman filter uses stance-foot kinematics to estimate trunk position and velocity.

This hierarchy separates slower planning from faster execution, but NMPC coordinates, MRT interpolation, WBC tasks, and PD targets must agree. A wrong contact classification or drifting estimate corrupts both the planner initial state and WBC constraints. Increasing WBC weights cannot repair upstream state error.

## Architecture and data flow

The flow is `MuJoCo/ROS sensors → StateEstimateBase → OCS2 HumanoidInterface/SQP MPC → MRT policy interpolation → WeightedWbc or HierarchicalWbc → desired q/v/torque → PD/controller`. Gait scheduling switches contacts, while a cubic spline defines swing-foot height. MPC state contains centroidal momentum, base, and joints; input contains contact forces and joint velocity.

The WBC QP includes base and joint acceleration, four contact-point forces, and joint torque. Floating-base equations, torque limits, and friction are constraints; base, swing-foot, and contact-force tracking become costs. Weighted and hierarchical implementations expose the tradeoff between soft weight competition and strict priority.

## Code map

- [`HumanoidSqpMpcNode.cpp`](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/humanoid_dummy/src/HumanoidSqpMpcNode.cpp) starts OCS2 SQP MPC as the smallest planner-only entry.
- [`HumanoidInterface`](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/humanoid_interface/src/HumanoidInterface.cpp) assembles model, costs, constraints, initialization, and MPC settings.
- [`WeightedWbc`](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/humanoid_wbc/src/WeightedWbc.cpp) transforms tasks into one weighted QP.
- [`HierarchicalWbc`](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/humanoid_wbc/src/HierarchicalWbc.cpp) solves successive priorities for comparison with weighting.
- [`StateEstimateBase`](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/humanoid_estimation/src/StateEstimateBase.cpp) implements stance-foot-related state updates.

## Minimal reproduction path

Build only the OCS2 packages required by the README and pin OCS2, Pinocchio, hpp-fcl, qpOASES, ROS, and this commit. Use `RelWithDebInfo`. Start the OCS2 dummy node to verify planner solving, then run the controller with the cheat estimator, and only then enable the normal estimator. This separates planner/WBC faults from estimation faults.

Verify actual 100 Hz NMPC, 500 Hz MRT/WBC/estimation, and greater-than-1 kHz PD rates. Record solver status, iterations and duration, constraint residuals, friction margin, contact forces, torque, covariance, foot slip, and termination. Compare weighted and hierarchical WBC with identical reference, model, and initial state.

## Capability boundaries

The state dimension, four foot contact points, and chosen costs and constraints are a specific design, not a universal humanoid template. The linear estimator trusts the stance foot and can become biased under slip, compliant terrain, or contact misclassification. README formulas should be checked against source at the pinned commit.

The repository does not provide broad hardware statistics, complex-terrain evaluation, arm manipulation, or collision avoidance. MuJoCo success does not establish robustness to sensor noise, actuator bandwidth, bus latency, or structural compliance. A large external OCS2 dependency also creates version and build drift.

## Engineering assessment and risks

The project is strongest as an educational and auditable baseline. It clearly states NMPC state/input and WBC variables and permits estimation ablation. Durable use requires real-time monitoring, solver fallback, contact anomaly detection, reference freshness checks, configuration manifests, and automated regressions. Infeasibility needs an explicit safe response rather than stale output.

Hardware requires robot-specific mass, inertia, contact, actuator, and sensor calibration; strict position, velocity, torque, and impact limits; and staged startup under support or suspension, low gains, low speed, and an emergency stop. Validate the normal estimator on logs before closing the loop. This review provides no deployment parameters.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/pocketxjl/humanoid-control/tree/3b5ffec98d29827730194b0dbf2f119fb7b265ca)
- [Main controller implementation](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/humanoid_controllers/src/humanoidController.cpp)
- [MIT license](https://github.com/pocketxjl/humanoid-control/blob/3b5ffec98d29827730194b0dbf2f119fb7b265ca/LICENSE)
