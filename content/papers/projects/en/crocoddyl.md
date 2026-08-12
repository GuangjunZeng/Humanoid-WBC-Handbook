# Crocoddyl: multi-contact optimal control and FDDP engineering library

[中文版](../crocoddyl.md)

Reviewed snapshot: [loco-3d/crocoddyl@`46974c3c49ed956e41f8f95a329cf8537af7550b`](https://github.com/loco-3d/crocoddyl/tree/46974c3c49ed956e41f8f95a329cf8537af7550b), 1,274 stars at the 2026-08-12 snapshot, BSD-3-Clause. Stars indicate influence and discovery value, not guaranteed convergence, real-time deadlines, or hardware safety.

## Why it is included

Crocoddyl is a major open implementation of multi-contact optimal control and Differential Dynamic Programming (DDP). Built on Pinocchio rigid-body dynamics and analytical derivatives, it combines manifold states, action models, costs, contact and impulse dynamics, and shooting solvers.

For WBC readers, Crocoddyl is not one replacement low-level controller. It generates multi-contact trajectories, supports rolling MPC optimization, and studies warm starts. This page focuses on the current model-derivative-solver contract; the separate paper page bounds the 2019 FDDP experiments.

## Problem addressed

Classic shooting DDP expects a dynamically feasible state-control initial trajectory. Jumps, walking, and contact transitions often start with dynamics gaps. Forcing feasibility immediately can push the rollout into a poor basin.

FDDP retains and contracts gaps during its forward pass and includes them in expected improvement, allowing poor warm starts to approach feasibility. Crocoddyl combines that solver with contact forward dynamics, impulse models, prescribed contact sequences, and custom costs while avoiding repeated derivative implementations.

## Architecture and data flow

The route is `state/action/contact models + costs → ShootingProblem → calc/calcDiff → SolverFDDP backward pass → gap-aware forward rollout → line-search acceptance → optimized trajectory`. Every action model must provide dynamics, cost, and derivatives; otherwise performance and convergence interpretation are unreliable.

Contact gait examples prescribe support sequences and use impulse models at switches. This optimizes a trajectory under a known contact schedule; it is not automatic foothold or uncertain contact discovery.

## Code map

- [`SolverFDDP`](https://github.com/loco-3d/crocoddyl/blob/46974c3c49ed956e41f8f95a329cf8537af7550b/include/crocoddyl/core/solvers/fddp.hxx) implements gap-aware direction computation, backward pass, forward pass, and expected-improvement acceptance.
- [`contact-fwddyn.hxx`](https://github.com/loco-3d/crocoddyl/blob/46974c3c49ed956e41f8f95a329cf8537af7550b/include/crocoddyl/multibody/actions/contact-fwddyn.hxx) implements contact forward dynamics and derivative contracts.
- [`biped_gaits_fwddyn.py`](https://github.com/loco-3d/crocoddyl/blob/46974c3c49ed956e41f8f95a329cf8537af7550b/examples/biped_gaits_fwddyn.py) assembles biped contact/impulse action models, foot costs, and shooting problems.
- [The shooting-problem Python binding](https://github.com/loco-3d/crocoddyl/blob/46974c3c49ed956e41f8f95a329cf8537af7550b/bindings/python/crocoddyl/core/shooting.cpp) exposes problem and `calc`/`calcDiff` contracts.

## Minimal reproduction path

Pin the commit, Pinocchio, compiler, BLAS, thread count, CPU, and robot model. Begin with a short no-contact problem and verify `calcDiff` using finite differences or existing tests. Run a biped gait and save cost, gap norm, step length, regularization, acceptance, and wall time each iteration.

Use three warm starts: quasi-static interpolation, a wrong foothold, and a velocity-discontinuous trajectory. Hold contact sequence and costs fixed while comparing DDP and FDDP convergence, final cost, maximum gap, and tail latency. Then add friction, torque, joint, and collision checks instead of reproducing unconstrained throughput alone.

## Capability boundaries

The original FDDP experiments intentionally omit friction-cone and torque constraints to study the solver. The current library is broader, but current APIs cannot retroactively prove that the original paper performed hardware-safe validation.

Users generally provide contact schedules, costs, and initial guesses. Low cost does not guarantee no slip, collision, actuator violation, or robustness to model error. Those properties require explicit models and acceptance tests.

## Engineering assessment and risks

The reusable design is the action-model derivative contract combined with gap-aware shooting. The main risk is treating millisecond iterations as a hard real-time guarantee. Report end-to-end timing distributions and worst deadline misses, and inject derivative, rank-loss, and conditioning faults.

Hardware MPC/WBC needs iteration and time budgets, infeasibility and timeout fallbacks, previous-trajectory health checks, an independent feedback controller, and an emergency stop. Offline trajectories also need friction, torque, velocity, impact, and collision gates.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/loco-3d/crocoddyl/tree/46974c3c49ed956e41f8f95a329cf8537af7550b)
- [Core FDDP implementation](https://github.com/loco-3d/crocoddyl/blob/46974c3c49ed956e41f8f95a329cf8537af7550b/include/crocoddyl/core/solvers/fddp.hxx)
- [English companion-paper deep read](../../en/crocoddyl-1909.04947.md)
