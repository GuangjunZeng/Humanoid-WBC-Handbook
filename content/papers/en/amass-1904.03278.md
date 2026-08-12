# AMASS: Unifying Motion Data Is More Than Joining Folders

[中文版](../amass-1904.03278.md)

Sources: [arXiv:1904.03278](https://arxiv.org/abs/1904.03278) · [pinned official code](https://github.com/nghorbani/amass/tree/a9888a92a4e62533454aa43e5f979d9a8bc8c893)

Review scope: the complete twelve-page paper and supplement, plus the official data-preparation and SMPL-H visualization code. AMASS is human-motion data infrastructure, not a robot controller.

> In one sentence: MoSh++ maps fifteen marker datasets with incompatible layouts into SMPL-H+DMPL, producing 42 hours from 346 people and 11,451 motions; it solves representation consistency, not robot feasibility, contact, licensing, or real-time processing.

Key terms include optical motion capture (光学动作捕捉), surface shape (表面形状), latent marker (潜在 marker), parametric body model (人体参数模型), soft-tissue dynamics (软组织动力学), pose parameters (姿态参数), motion retargeting (动作重定向), and kinematic feasibility (运动学可行性).

## Engineering problem

Motion-capture archives resemble parts made by different factories. They all describe humans moving, yet they use 37–91 markers, different labels, skeletons, sampling rates, body shapes, and coordinate conventions. Concatenating files lets a learner confuse capture-system identity with motion. A WBC data pipeline needs a common body representation.

Earlier MoSh estimated shape and pose from sparse markers, but BlendSCAPE, fixed marker weighting, and a weaker soft-tissue model limited accuracy. AMASS effectively remeasures old archives with one three-dimensional ruler: infer subject-level shape and marker locations, then explain per-frame pose, translation, and tissue motion.

A natural SMPL-H motion is not automatically trackable by G1, H1, or Atlas. Humans and robots differ in limits, bandwidth, feet, mass, collision, and torque. AMASS provides a common language, not a certificate of robotic feasibility.

## Core insight

MoSh++ separates time scales. Stage I samples twelve frames from a sequence and jointly estimates body shape, latent marker placement, and pose. Stage II holds sequence-level variables fixed and estimates pose, root translation, and DMPL coefficients frame by frame. It is analogous to calibrating the ruler before measuring every frame.

The representation uses a 52-joint SMPL-H model, 159 pose values including root orientation, sixteen static shape coefficients, eight DMPL dynamics coefficients, and translation. The same output schema accommodates very different input marker sets and retains articulated hands where marker evidence exists.

Missing markers are not replaced by zeros. Data weight changes with visible-marker count, while the pose prior grows when multiple markers disappear, by as much as 3.5×. This prevents divergence but can pull uncommon genuine poses toward the prior.

## Method: input → processing → output

Input consists of labeled 3D marker positions. Stage I combines marker residual, shape, pose, hand, and surface-distance terms. Stage II adds temporal smoothness, velocity consistency, and DMPL priors. Figure 3 and Equation 5–7 show that the result is a regularized inference, not a purely geometric inversion.

The authors recorded SSM, synchronized optical markers and high-resolution 4D scans, to tune and evaluate against surface evidence. Three subjects and thirty motions are divided between hyperparameter search and held-out tests. This avoids evaluating only against the same markers used for fitting.

Fifteen archives are then standardized. Mislabeled, swapped, and missing markers are manually inspected, corrected, or excluded. That human intervention matters: representation unification does not make source corruption disappear, so provenance and an exception list remain required.

## How to read the key figures

![Figure 1: one representation for heterogeneous archives](../assets/amass-1904.03278/figure-1-unified-corpus.jpg)

Figure 1 shows one SMPL surface and skeleton receiving very different marker layouts from CMU, MPI, BioMotionLab, TCD, and ACCAD. It proves schema unification, not removal of demographic, capture, or motion-distribution bias.

![Figure 3: MoSh++ and SMPL](../assets/amass-1904.03278/figure-3-moshpp-smpl.jpg)

Figure 3 compares MoSh/BlendSCAPE with MoSh++/SMPL. The visible difference is modest, but a standard skeleton, articulated hands, and a better surface make cross-dataset learning possible. Equation 6–7 also exposes the contribution of priors.

![Figure 6–8: accuracy, tissue, hands, and scale](../assets/amass-1904.03278/figure-6-8-evaluation.jpg)

Figure 6 reduces shape error from 12.1 to 7.4 mm and pose error without dynamics from 10.5 to 8.1 mm; with dynamics, the reported comparison is approximately 10.24 versus 7.3 mm. Figure 7–8 are qualitative for tissue and hands, while Table 1 totals 346 people, 11,451 motions, and 2,488 minutes. Hand results have no independent ground truth.

![Figure 9: choosing model dimension](../assets/amass-1904.03278/figure-9-model-size.jpg)

Figure 9 supports sixteen shape and eight DMPL components on the SSM validation set. More dimensions overfit. The optimum is tied to three subjects and one marker setting and should not be copied blindly into a robot state.

## Strongest experiment

The strongest evidence is scan-to-mesh error on synchronized held-out scans. MoSh++ with 46 markers approaches or exceeds older MoSh with 67, and improves shape, pose, and soft tissue. This connects the gain to model and optimization quality rather than denser observation alone.

The 42-hour corpus is useful but heterogeneous in license, sampling, and action distribution. Robotics work should report how much survives retargeting, contact repair, and closed-loop tracking instead of quoting raw AMASS hours as usable robot data.

## Paper-to-code mapping

At commit `a9888a92a4e62533454aa43e5f979d9a8bc8c893`, `src/amass/data/prepare_data.py::dump_amass2pytroch` reads `*_poses.npz` and extracts poses, DMPL, translation, shape, and gender. `AMASS_Augment.fetch_data` adds matrix-rotation features, matching the standardized learning interface.

`src/amass/tools/make_teaser_image.py` passes root, body and hand pose, shape, and DMPL values to `BodyModel`. The repository exposes consumption and visualization, not the complete MoSh++ optimization pipeline. Models and data have separate licenses, so “official code” does not imply unrestricted end-to-end use.

## Limitations and safety boundary

The authors explicitly state that MoSh++ is not real time. The supplement reports roughly 25 minutes per sequence for Stage I, 0.5 seconds per frame without dynamics, and two seconds per frame with dynamics. Face motion is absent, hands lack ground truth, and missing-marker handling remains imperfect.

Independent limitations include a three-subject SSM evaluation, absence of force-consistent foot contacts, robot-infeasible velocities and collisions, and source-specific licenses. Scan accuracy is not robot tracking accuracy. Shape and tissue dimensions may add conversion errors without helping WBC.

Never stream AMASS joint values directly to hardware. Retargeting must enforce limits, self-collision, foot contact, speed, acceleration, and torque, followed by closed-loop simulation. Hardware staging requires low gains, tethering, emergency stop, and current and temperature monitoring.

## Bounded engineering takeaway

Use AMASS as an upstream normalized human-motion layer. Preserve source dataset, subject, sequence, frame rate, license, hash, and conversion version. Derive robot joints, contacts, and feasibility without overwriting the human representation, and keep geometric, dynamic, and safety validity separate.

For WBC, usable scale is a funnel: motions retargeted, tracked by a privileged policy, robust under randomization, and accepted by hardware checks. AMASS completes only the first stage.

## Reproduction and acceptance checklist

Pin AMASS, SMPL-H, DMPL, human_body_prior, and the official commit. Record every source license, frame rate, marker layout, and checksum. Visualize random samples and audit axes, units, body model, root motion, hands, and tissue. Preserve explicit failures, NaNs, extreme velocities, and relabeling decisions.

Test pose slicing and axis-angle round trips. Verify root, body, hand, sixteen shape, eight DMPL, and translation dimensions. Split train, validation, and test by subject and original sequence rather than adjacent frames.

After retargeting, report inverse-kinematics residual, limit and collision rates, slip, contact switches, and policy success by motion class. Inject dynamics and observation disturbances in simulation. Only motions passing those gates should enter tethered, low-energy hardware trials.

> **Engineering judgment:** AMASS makes heterogeneous human motion speak one language; safe translation into a particular humanoid remains a separate engineering system.
