# Sentis–Khatib WBC: Composing Constraints, Tasks, and Posture in Dynamic Null Spaces

[中文版](../sentis-khatib-wbc-2006.md)

Source: [author-hosted PDF](https://khatib.stanford.edu/publications/pdfs/Sentis_2006_ICRA.pdf)

Review scope: the complete eight-page paper, including priority, operational-space force control, joint-limit and near-body avoidance, floating base, and support contacts. No uniquely verifiable official public code was found.

> In one sentence: constraints receive highest priority, precise tasks operate in the constraint null space, and posture fills residual redundancy through dynamically consistent projection; this established hierarchical WBC language, but the evidence is real-time simulation rather than hardware.

Key terms include whole-body control (全身控制), operational-space control (操作空间控制), constraint primitive (约束 primitive), task primitive (任务 primitive), posture primitive (姿态 primitive), dynamically consistent null space (动力学一致零空间), free-floating system (自由浮动系统), support contact (支撑接触), and hybrid force/motion control (混合力/位控制).

## Engineering problem

A humanoid must stand, avoid obstacles, respect limits, move a hand, and keep a useful posture. These objectives conflict. A hand path can approach a wall or elbow limit, while posture competes with contact. A weighted sum lets a sufficiently large task weight defeat safety.

Local inverse kinematics also misses whole-body dynamics, task impedance, and contact reaction. A standing humanoid is not fixed-base: six base coordinates are unactuated and support forces govern them. Ignoring floating-base dynamics yields kinematically plausible but unrealizable torque.

The problem is therefore a compositional control language: what is non-negotiable, what may use remaining freedom, and how infeasibility is detected at runtime.

## Core insight

Control primitives are constraints, tasks, and postures. Contacts, limits, collision avoidance, and balance are constraints; hands, gaze, and feet are tasks; hip height, orientation, symmetry, and effort are posture. Torque is nested as `Γ_constraints + N_constraints^T(Γ_tasks + N_tasks^T Γ_postures)`.

Null-space projection resembles drawing on transparent sheets. The highest layer blocks immutable regions, tasks draw only in remaining space, and posture fills the last gaps. Dynamic consistency accounts for the mass matrix, so lower-priority torque does not create higher-priority task acceleration.

The task Jacobian becomes `J_t|c = J_tasks N_constraints` before task inertia and wrench are computed. Singularity of the prioritized Jacobian signals that the task is infeasible under active constraints rather than inviting unbounded gain.

## Method: input → processing → output

Equation 2 nests constraint, task, and posture torque. Operational-space dynamics produces desired wrench and supports impedance and hybrid force/motion. Constraints define the available subspace rather than contributing a soft penalty.

Joint limits activate a potential field before the hard bound. The elbow is pushed away while the hand task continues in residual space. Near-body obstacle avoidance similarly inserts the closest body point and obstacle distance as a constraint before hand control.

For a free-floating humanoid, six virtual unactuated base coordinates and zero support-contact acceleration are introduced. Support Jacobian and reaction force project base dynamics into actuated joints. The derivation assumes a stiff floor, high friction, and no support slip.

## How to read the key figures

![Figure 1: three primitive categories](../assets/sentis-khatib-wbc-2006/figure-1-primitives.jpg)

Figure 1 assigns contacts, limits, collision, and balance to constraints; hands, gaze, and feet to tasks; and hip, upper body, symmetry, and effort to posture. Misclassification cannot be repaired merely by a larger weight.

![Figure 3–4: hierarchy and contact](../assets/sentis-khatib-wbc-2006/figure-3-4-hierarchy.jpg)

Figure 3 displays nested projection, while Figure 4 places support, hip task, and posture on one body. Equation 2–6 require projecting the Jacobian before solving rather than adding independently computed torques.

![Figure 8: near-body obstacle](../assets/sentis-khatib-wbc-2006/figure-8-obstacle.jpg)

Figure 8 retains a hand trajectory while moving the body around a spherical obstacle. It demonstrates online reshaping in simulation, without perception error or contact impact.

![Figure 10: reaching beyond a wall](../assets/sentis-khatib-wbc-2006/figure-10-wall.jpg)

Figure 10 combines support, momentum, hand, hip, compliance, posture, and wall avoidance. The paper calls this real-time simulation and explicitly says hardware results are too early to show.

## Strongest experiment

The strongest evidence is the combined Figure 10 behavior plus the smooth insertion of joint-limit and obstacle constraints in Figure 7–8. Existing tasks continue after a new constraint changes their feasible subspace.

There is no quantitative tracking, violation, timing distribution, disturbance, or hardware experiment. Runtime feasibility is demonstrated mainly through Jacobian singularity and simulation.

## Paper-to-implementation status

There is no uniquely auditable official code or pinned implementation for this paper. Labeling an unrelated modern WBC repository as the original implementation would blur primary evidence and later engineering.

A reproduction must implement mass and bias, constraint/task/posture Jacobians, dynamically consistent generalized inverses, nested projectors, support selection, and wrench. Log frame, dimension, rank, condition, and damping, and define a bounded fallback near singularity.

## Limitations and safety boundary

The authors explicitly state that hardware is not ready to report, reliable estimation of joint-limit, self-collision, and balance constraints remains difficult, ordering among simultaneous constraints is unresolved, and floating-base/support treatment is preliminary.

Independent limitations include no-slip assumptions, potential-field local minima and chatter, conflicts within equal priority, absent unified torque/friction/CoP inequalities, and discontinuous rank at contact switches.

Hardware output needs joint, torque, rate, contact wrench, friction cone, CoP, and collision checks. Constraint-estimation loss or rank jumps require balance or stop fallback. Obstacle distance must include perception latency and geometry margins.

## Bounded engineering takeaway

Task classification precedes weight tuning. Specify inviolable safety, behavioral goals, then residual posture, each with infeasibility and fallback. A weighted cost alone obscures why safety was traded away.

Modern QP or HQP can express inequality constraints more directly, but inherits the priority design problem. The responsibilities remain valuable even when the solver changes.

## Reproduction and acceptance checklist

Start with fixed-base unit tests. Verify `J N`, generalized inverses, and invariance of high-priority acceleration to low-priority torque. Construct rank deficiency, conflicting tasks, and limit activation, checking bounded output, hysteresis, and explicit infeasibility.

Add floating-base single and double support. Audit selection matrices, support acceleration, wrench, and energy. Inject mass, friction, latency, contact-point, slip, and perception errors and report task error, violation, rank, condition number, torque, and deadline misses.

Stage hardware from low-force fixed-base through one hand and static support before contact switches. Use tether, soft limits, independent watchdog, and emergency stop. Log each constraint activation, projector rank, and fallback reason.

> **Engineering judgment:** the enduring idea is not one matrix; it is telling the controller which objectives may compromise and which never get a vote.
