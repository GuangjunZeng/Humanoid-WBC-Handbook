# Robotics safety policy

This repository is an engineering knowledge tool, not a real-time controller and not a substitute for a robot manufacturer's limits, workplace procedures, or qualified review.

## Mandatory hardware gate

Any claim involving torque, gains, force control, contact, impacts, falls, recovery, high velocity, joint-limit proximity, or forceful interaction must be marked `hardware_critical`. It cannot pass validation without simulation evidence, bounded commands, emergency stop, protection controls, robot-specific warnings, and staged deployment.

## Minimum deployment sequence

1. Reproduce in deterministic simulation with logs and seed/configuration recorded.
2. Test limit enforcement, watchdog behavior, communication loss, invalid observations, and emergency stop.
3. Use the lowest practical energy/velocity/force envelope on restrained or protected hardware.
4. Keep people outside the reachable/fall zone and use appropriate supports or shielding.
5. Expand the envelope one variable at a time while retaining rollback criteria and logs.

## Publication language

- State measured conditions and applicability; avoid universal claims such as “safe” or “works on hardware.”
- Separate observations, author conclusions, and reviewer judgment.
- Preserve negative results and conflicting evidence.
- Do not provide executable hardware parameters without robot model, actuator/control mode, firmware/software versions, test conditions, and safety case.

Validation catches missing documentation, not physical hazards. Final hardware authorization remains a human responsibility.
