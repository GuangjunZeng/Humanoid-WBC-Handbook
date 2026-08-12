# Learning to Walk in Minutes: The Classic Massively Parallel RL Recipe and Its Limits

[中文版](../learning-walk-2109.11978.md)

Sources: [arXiv:2109.11978](https://arxiv.org/abs/2109.11978) · [pinned official code](https://github.com/leggedrobotics/legged_gym/tree/8fa29acc6fd1910c3d9659eef6310bdd301cde0a)

Review scope: the complete fourteen-page paper and supplement, plus terrain curriculum, observations, timeout bootstrapping, rewards, and PPO configuration in official legged_gym.

> In one sentence: 4,096 parallel robots, roughly one-hundred-thousand-sample PPO batches, and an automatic terrain curriculum train an ANYmal rough-terrain policy in under twenty minutes, but training speed is not proof of maximum hardware robustness.

Key terms include massively parallel reinforcement learning (大规模并行强化学习), terrain curriculum (地形课程), time-out bootstrapping (时间截断自举), rollout horizon (策略视野), domain randomization (域随机化), height map (高度图), PD position control (比例—微分位置控制), and sim-to-real transfer (仿真到现实迁移).

## Engineering problem

Legged reinforcement learning once spent much of its iteration cycle waiting for serial simulation and manually staged terrain. Hard environments produce repeated early falls; easy environments fail to teach stairs and obstacles. Long training makes every reward, observation, and randomization change expensive.

GPU simulation changes the operating model: thousands of robots experience different terrain and disturbances simultaneously. It resembles opening an entire driving school at once, with each student moved to a harder or easier course from current performance. The new systems problem is how to balance environment count, rollout horizon, batch size, memory, and PPO statistics.

More parallelism is not automatically better. A short rollout gives weak temporal credit; a very large batch changes update frequency and sample reuse; treating a time limit as a fall injects a false negative terminal reward into value learning. The paper is valuable because it measures these interactions.

## Core insight

Terrain is arranged as a directed difficulty grid. A robot that moves far enough advances to a harder row; a poor episode moves it down; successful robots at the highest level are redistributed. Thousands of current rows become an empirical capability distribution without training a curriculum generator.

Speed comes from the full GPU-resident loop—simulation, observation, reward, resets, and learning—not one kernel. The reference setup collects 24 steps from 4,096 robots, a 98,304-sample batch, and runs 1,500 updates in under twenty minutes for rough terrain; flat-ground training can finish in under four minutes.

Time-out bootstrapping treats a fixed episode limit as a truncated recording rather than a physical failure. Value should continue from the next state. The paper reports roughly 10–20% reward improvement and shows that horizons below about 25 steps damage PPO quality.

## Method: input → processing → output

Observations include base linear and angular velocity, projected gravity, joint position and velocity, previous action, and 108 sampled terrain heights around the base. Actions are joint position targets executed by PD control. Reward tracks commanded velocity and penalizes unwanted motion, torque, acceleration, action variation, collision, and body contact, with a term encouraging longer steps.

Terrain includes slopes, stairs, and discrete obstacles. Each environment changes difficulty from episode progress. Ground friction and observation noise are randomized, and robots receive random pushes. Isaac Gym produces parallel trajectories for PPO using a 24-step horizon.

Figure 4 shows that simulation throughput is nearly linear to around 4,000 environments, while 2,048–4,096 environments and roughly 100k–200k batches are the best trade-off on the reported hardware. This is a measured operating point, not a universal constant for future GPUs or larger humanoid networks.

The trained policy is deployed on ANYmal. Maximum command is reduced to 0.6 m/s partly because the local map is imperfect. The paper does not add an explicit optimization safety filter; deployment relies on training, PD control, and platform protection.

## How to read the key figures

![Figure 3: automatic terrain curriculum](../assets/learning-walk-2109.11978/figure-3-curriculum.jpg)

Figure 3 shows the distribution of 4,000 robots after 500 and 1,000 updates. Robots start in easy rows and migrate according to performance. The curriculum is a per-environment state machine, not a learned generator, and progress should be logged separately for each terrain family.

![Figure 4: parallelism, batch size, and training time](../assets/learning-walk-2109.11978/figure-4-parallelism.jpg)

Figure 4 is the most reusable systems experiment. It jointly displays environment count, batch, reward, and wall-clock time. It motivates the reported operating point but also requires each new GPU, simulator, and network size to be swept again.

![Figure 7: ANYmal hardware terrain deployment](../assets/learning-walk-2109.11978/figure-7-hardware.jpg)

Figure 7 demonstrates one policy on varied real obstacles. Images do not provide failure count, map-error distribution, or confidence intervals. Read with the reduced command limit and height-map discussion, it supports sim-to-real feasibility rather than arbitrary-environment robustness.

## Strongest experiment

The strongest evidence is the systems sweep in Figure 4 together with the under-twenty-minute rough-terrain result. Horizon and timeout ablations give a mechanism for the speed-quality trade-off, so “minutes” is more than a single benchmark number.

The authors explicitly caution that faster training does not imply absolutely best robustness, and hardware remains limited by map quality and state drift. A modern reproduction should report time to a fixed success threshold at fixed hardware and sample budget, then separately report real success, slip, stops, and estimation failures.

## Paper-to-code mapping

At commit `8fa29acc6fd1910c3d9659eef6310bdd301cde0a`, `legged_gym/envs/base/legged_robot.py::_update_terrain_curriculum` moves environments through terrain levels. The same file's `compute_observations`, rewards, and reset logic instantiate the training environment.

`legged_gym/envs/base/legged_robot_config.py` sets `num_envs=4096`; PPO configuration uses `num_steps_per_env=24`, and `send_timeouts=True` passes truncation information for bootstrapping. ANYmal configuration includes a learned actuator model. Reproduction must also pin Isaac Gym, PyTorch, GPU, and assets.

## Limitations and safety boundary

The authors explicitly state that speed is not proof of best robustness. Hardware performance is affected by height-map accuracy and state drift, and command speed is reduced to 0.6 m/s. They point toward teacher–student training to reduce terrain-measurement dependence.

Independent limitations include distance-based curriculum favoring fast but unstable behavior, hardware-specific parallelism optima, height-sampling failures at occlusions and stair edges, and absent long-duration fall, thermal, and actuator-saturation statistics.

Simulation termination and reward are not a hardware safety layer. Command limits, body and joint monitors, current and temperature protection, emergency stop, and tethered staging remain mandatory whenever speed, load, or terrain expands.

## Bounded engineering takeaway

The reusable recipe is thousands of environments, a horizon of a few dozen steps, a roughly hundred-thousand-sample batch, success-driven terrain levels, and correct timeout handling. It changes reinforcement learning from an overnight experiment into a rapid engineering loop.

The values 4,096, 24, and twenty minutes are not universal answers. New systems must sweep them and compare time to the same quality threshold. Hardware capability remains an independent acceptance problem.

## Reproduction and acceptance checklist

Pin GPU, drivers, Isaac Gym, PyTorch, commit, assets, and seeds. Sweep environment count while logging simulation FPS, update time, memory, total samples, and time to fixed reward and success thresholds. Sweep horizon and batch independently and unit-test that timeout and physical failure produce different value targets.

Report curriculum distribution and success per terrain type. Add simulation tests for friction, payload, latency, noise, extrapolated speed, and missing map data. Stage hardware from suspended signal checks through flat low-speed and tethered obstacles before expanding speed.

Hardware reports should include repeated-trial success, velocity error, slip, peak torque, saturation, falls, stops, and sustained duration. Re-run both training efficiency and final quality after simulator, GPU, network, or reward changes. Parallel simulation shortens the iteration cycle, not the safety case.
