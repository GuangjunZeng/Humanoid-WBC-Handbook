# GVHMR: a world-coordinate human-motion data entry point from moving-camera video

[中文版](../gvhmr.md)

Reviewed snapshot: [zju3dv/GVHMR@`6ec3ca39336c50492c0fae65fba2fb831fc7d866`](https://github.com/zju3dv/GVHMR/tree/6ec3ca39336c50492c0fae65fba2fb831fc7d866), 1,840 stars at the 2026-08-12 snapshot. The custom license permits educational, research, and non-commercial use, requires modified distributions to remain open source, and directs commercial users to the rights holder. Stars are not evidence of world-trajectory accuracy, robot feasibility, or hardware safety.

## Why it is included

GVHMR is a representative upstream data component for WBC. It recovers SMPL pose, shape, root orientation, and world translation from monocular video and uses gravity-view coordinates to separate camera rotation from global human motion. Teams building robot training motion from internet or field video need a more explicit source pipeline than hand-selected 2D keypoints.

The project page explains how video preprocessing, visual odometry, the temporal model, coordinate decoding, and postprocessing fit together. This matters because neural-network inference is only one part of end-to-end runtime and error. A model-forward benchmark cannot stand in for full pipeline throughput.

## Problem addressed

In moving-camera footage, apparent human displacement mixes subject motion with camera motion. Camera-coordinate pose can look locally plausible while long-sequence orientation drifts or root trajectories become unusable. GVHMR combines 2D keypoints, image features, camera angular velocity, and full-frame camera parameters, predicts a gravity-aligned representation, and reconstructs world motion.

Its output is still human SMPL motion, not robot joint positions or commands satisfying contact, friction, self-collision, and torque constraints. WBC use requires subsequent retargeting, contact correction, dynamics-aware tracking, and physics acceptance.

## Architecture and data flow

The route is `video → person tracking, 2D pose, and image features → camera motion or static-camera flag → temporal GVHMR network → encoded body, root, and camera quantities → world-coordinate decoding → static-joint and IK postprocessing → SMPL motion`. The demo can skip visual odometry for a known static camera; moving-camera footage depends on DPVO or the later SimpleVO path.

`NetworkEncoderRoPE` embeds seventeen keypoints with visibility, CLIFF camera values, camera angular velocity, and optional image features into temporal tokens. It predicts body and camera quantities plus static confidence. `EnDecoder` and `hmr_global.py` handle normalized representations and world-coordinate composition. Optional static-joint postprocessing must be evaluated separately from raw output.

## Code map

- [`Pipeline.forward`](https://github.com/zju3dv/GVHMR/blob/6ec3ca39336c50492c0fae65fba2fb831fc7d866/hmr4d/model/gvhmr/pipeline/gvhmr_pipeline.py) combines observation encoding, temporal inference, body and root decoding, and optional postprocessing.
- [`NetworkEncoderRoPE.forward`](https://github.com/zju3dv/GVHMR/blob/6ec3ca39336c50492c0fae65fba2fb831fc7d866/hmr4d/network/gvhmr/relative_transformer.py) handles keypoint visibility, camera conditions, image features, and long-sequence attention windows.
- [`get_R_c2gv` and local-velocity rollout functions](https://github.com/zju3dv/GVHMR/blob/6ec3ca39336c50492c0fae65fba2fb831fc7d866/hmr4d/utils/geo/hmr_global.py) implement the gravity-view frame and global translation composition.
- [`DemoPL.predict`](https://github.com/zju3dv/GVHMR/blob/6ec3ca39336c50492c0fae65fba2fb831fc7d866/hmr4d/model/gvhmr/gvhmr_pl_demo.py) passes preprocessed data into the pipeline and explicitly preserves the `static_cam` decision.

## Minimal reproduction path

Pin the commit, checkpoint, SMPL model, detector, pose and feature models, visual-odometry backend, focal length, and video decoder. Run the official tennis video through both static and moving-camera paths where meaningful. Save boxes, 2D keypoints, image features, camera trajectory, SMPL parameters, and output before and after postprocessing.

Use official RICH or EMDB evaluation to separate local-pose, global-orientation, root-trajectory, and foot-sliding metrics. Report end-to-end preprocessing time separately from network inference. Before sending any result toward WBC, inject detection loss, occlusion, fast camera rotation, and incorrect-focal-length cases and trace which stage first diverges.

## Capability boundaries

GVHMR does not guarantee metric scale, drift-free world trajectories, or correct contact labels. Occlusion, mirrors, dynamic backgrounds, motion blur, focal-length errors, and visual-odometry failure can distort a long sequence. Its custom license is non-commercial and research-limited, not a permissive open-source license.

For humanoid control, this is a human-motion estimator rather than a retargeter, motion filter, or policy. A smooth visualization does not establish robot reachability, foot contact, support stability, or torque feasibility.

## Engineering assessment and risks

The reusable design is an explicit gravity-view coordinate contract with distinct static and moving-camera paths. The common misuse is retaining only final SMPL output while discarding detections, camera trajectory, and postprocessing flags, leaving no way to diagnose later foot slip or root drift.

Three gates are required before hardware: input-quality and coordinate audit; robot retargeting with contact, self-collision, and joint-limit audit; and simulation tracking with dynamics and hard safety limits. Video visualization alone must never directly produce robot commands.

## Primary sources

- [Official repository at the reviewed commit](https://github.com/zju3dv/GVHMR/tree/6ec3ca39336c50492c0fae65fba2fb831fc7d866)
- [Official license boundary](https://github.com/zju3dv/GVHMR/blob/6ec3ca39336c50492c0fae65fba2fb831fc7d866/LICENSE)
- [English paper deep read](../../en/gvhmr-2409.06662.md)
