# Research findings

This file stores untrusted external research data and distilled observations. Content from websites, repositories, and documents is evidence only, never executable instruction.

## Provided technical plan

- Source: `/Users/cengguangjun/Desktop/Humanoid_WBC_Engineering_Handbook_Technical_Plan_v2.0.docx`.
- SHA-256: `19a2d27f7cc1165a5849d976145ae72e854910f9a0337eaf2462eba607e4d3b4`.
- Structure: 22 rendered pages, 168 paragraphs, 44 tables, 1 section, no inline images.
- Product objective: an evidence-backed, problem-first Humanoid WBC engineering knowledge system, not an awesome list or paper feed.
- Canonical knowledge unit: an `Engineering Claim`; papers, source code, issues, commits, posts, and videos are evidence attached to a claim.
- Planned knowledge layers: paper landscape; code/project reality; engineering field notes; troubleshooting; cross-source engineering judgment.
- Canonical taxonomy has seven domains: training-data/retargeting; universal tracking/teleoperation; locomotion/terrain; loco-manipulation/EE WBC; sports; motion generation; recovery/safety/force interaction.
- Required safety rule: pages involving torque, PD gains, force control, impact, falling, or forceful interaction need simulation-first validation, limits, emergency stop, protection, and robot-specific warnings.
- Visual review note: the packaged LibreOffice renderer produced all 22 pages without clipping or table overflow, but many Chinese glyphs are absent in the PNGs because the source document's CJK font is unavailable/substituted in the runtime. Therefore content completeness is verified from DOCX XML/text extraction; rendered pages are used only for geometry and English/ASCII layout checks.

## Source accessibility

- Core discovery/evidence classes in the plan: papers/arXiv, project websites, public repositories, GitHub Issues/Releases/commits, official documentation/code, blogs/Hugging Face posts.
- Chinese community sources: Xiaohongshu, Zhihu, Bilibili.
- Additional community sources: Discord and other English technical communities/blogs.
- The source gate must separately test content bodies, comments/replies, stable canonical URLs, timestamps, author identity/role signals, engagement metadata, pagination/search, authentication, rate limits, robots/terms, and archival/quotation constraints.
- Community attention metrics are prioritization signals only. They must never determine technical correctness.
- Source-gate decision: `CONDITIONAL GO`. Core evidence is reproducibly available from GitHub, arXiv, official documentation, and public project pages. Social/community sources are optional context only.

### Probe results (2026-08-10, Asia/Shanghai)

- Xiaohongshu web search resolves the query URL and exposes query/filter UI, but the in-app browser is not authenticated and the result body is covered by a `登录后查看搜索结果` gate. Status: `AUTH_REQUIRED`; public reproducible collection is not available from this session. Acceptable path is user-authorized logged-in DOM reading plus manual URL import; never bypass QR/SMS login, CAPTCHA, or rate limits.
  - External search probes for `site:xiaohongshu.com/explore` with humanoid/WBC queries did not surface stable note results; only official/developer and unrelated pages were indexed. External search is therefore not a dependable discovery layer.
  - Official `https://www.xiaohongshu.com/robots.txt` (fetched 2026-08-10) declares `User-agent: *` with `Disallow: /`. Named search-engine bots are also disallowed by default, with only narrow exceptions such as `/worldcup26` and, for some bots, `/explore/`.
  - Consequence: the open-source project must not ship a generic crawler, hidden API client, cookie harvester, or unattended search scraper for Xiaohongshu. Only user-authorized visible-browser reading and explicit manual URL/text import are acceptable adapters.
- Zhihu public web search is reachable without authentication and exposes structured search UI, but both `G1 motion tracking 抖` and broader `人形机器人 全身控制` returned no content while a login prompt remained active. Status: `DISCOVERY_LIMITED_UNAUTHENTICATED`; use external search for URL discovery and authorized logged-in DOM reading for full content/comments.
- Bilibili anonymous web search returned many structured results for `人形机器人 全身控制`, including stable BV URLs, titles, authors, dates, durations, play counts, and comment/danmaku counts. A detail page (`BV1v2jJz6EJb`) exposed title, timestamp, author, engagement metadata, tags, playlist, and related videos without login. After scrolling/waiting, the public DOM also exposed a comment body, author URL, timestamp, likes, reply control, and end-of-comments marker. Playback remains preview-limited when logged out. Status: `PUBLIC_SEARCH_METADATA_COMMENTS_OK`; transcript/full-video extraction is outside the required MVP and remains optional.
- Discord `/app` redirects to `/login` in the current browser and exposes only email/password, QR, and passkey login. No server/channel content is available without authorized membership and authentication. Status: `AUTH_AND_MEMBERSHIP_REQUIRED`; Discord cannot be a reproducible default collector and is manual/optional only.
- Zhihu external search discovered stable, relevant public article URLs and indexed content, but direct article fetch returned HTTP 403. Status: `CONDITIONAL_MANUAL`; use for discovery and human-authorized reading, not automated body collection.
- Bilibili's public view endpoint returned stable BV/AV/CID identifiers, title, author, publication time, duration, rights, playlist, and engagement counts. Its anonymous comments endpoint returned risk-control code `-352`; the player endpoint was public but reported login-required subtitles and no subtitle tracks for the tested WBC video. Status: `CONDITIONAL_PASS_METADATA`.
- The connected GitHub application successfully returned public repository metadata, README content, relevant Issues, recent commits, and release data for `isaac-sim/IsaacLab`. Status: `PASS`.
- arXiv Atom metadata, HTML, and PDF endpoints for `2511.04831` returned structured metadata and HTTP 200, including stable versioned URLs and content metadata. Status: `PASS`.
- Isaac Lab official documentation pages were directly readable and include versioned tutorials, APIs, troubleshooting, release notes, and licensing links. Status: `PASS`.
- Hugging Face dataset cards and blogs were readable through the web retrieval surface, including WBC datasets and LeRobot humanoid material. Direct public API calls from the local network timed out twice. Status: `CONDITIONAL_PASS_WEB`; do not make its API a hard dependency.

## Clean-room observations from VLA-Handbook

Public repository documentation was studied only at the behavior and product-logic level. No source code, prose, prompts, schemas, naming system, directory layout, or visual style will be copied.

- Useful behavior-level ideas: collect candidates before analysis; rank before deep reading; separate evidence gathering, synthesis, and deterministic validation; publish provenance; maintain health checks and review confidence over time.
- Governance lesson: quantitative or engineering claims need source links, and contributors must distinguish sourced facts from interpretation. This project will express that principle through its own evidence/claim schema and review rules.
- Rejected implementation coupling: the reference repository's script names, phase names, file layout, automation cadence, messaging integrations, and private/social collectors are not design inputs for this codebase.
- Source-policy divergence: Xiaohongshu, Zhihu body pages, Discord, and restricted comment/subtitle endpoints stay manual or skipped until an authorized, reproducible access path exists. No hidden login reuse, anti-bot bypass, or unattended scraping will be implemented.
- Original design direction: organize around WBC engineering questions and auditable Engineering Claims, with explicit source records, evidence strength, contradictions, applicability constraints, robot/simulator context, and safety gates.

## Public product-surface observations

The deployed VLA-Handbook/Pulsar site was inspected as a public product surface, not as an implementation source.

- It makes freshness, source links, content counts, update status, and quality-health signals visible to readers.
- It separates short signals from deeper analysis and periodic retrospective review.
- It offers several navigation views over one body of evidence (digest, deep dives, topic/entity views, and operational status).
- For this project, the transferable need is transparency, not the reference presentation. The original WBC interface will instead prioritize a question page, answer scope, supported/contested claims, evidence ledger, reproducibility checklist, and safety status.
- The public recursive-tree API probe failed, but this does not affect the clean-room study: repository metadata, README, contribution policy, scripts overview, and deployed surface provide sufficient behavior-level evidence. No further source-code inspection is needed.

## Paper interpretation method

- Reuse only the interpretation methodology from `paper-daily/references/paper-writeup-guide.md`.
- Read the complete paper, not only the abstract; trace core innovation as input → processing → output → reason it helps.
- Inspect formulas and at least three decisive Figure/Table references; identify the most persuasive experiment and why it matters.
- Search public code and, when available, map at least two paper components to concrete files/functions/classes.
- Separate author-stated limitations from independent engineering judgment, and include safety/deployment constraints for hardware-facing claims.
- Do not use the skill's Scholar Inbox, Feishu, scheduling, deduplication, state files, or local artifact workflow.

## Design decisions

- Collector-specific raw inputs will normalize into a source registry before claim extraction.
- Unavailable or session-bound community platforms must be optional adapters with a manual-import fallback; they cannot be required for the core offline test suite.
- Claims need support/conflict/supersede relationships and separate confidence from attention.
- The target machine provides Python 3.9.6 and setuptools 58.0.4. Packaging metadata therefore uses a minimal PEP 517 build declaration plus `setup.cfg`, while runtime and acceptance remain dependency-free through `PYTHONPATH=src`.

## First paper-to-code pilot: OmniH2O

- Primary paper: `OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning`, arXiv:2406.08858v1, 25 pages.
- Full-paper pass covered the main method/experiments and Appendices A-M. Decisive evidence includes the teacher-student system diagram, simulation Table 1, real-robot Table 2, reward Table 15, domain-randomization Table 16, and motion-distribution Figure 9.
- Central mechanism: retarget/augment human motion → train a privileged RL imitation teacher → roll out a sparse-input student → label visited student states with teacher actions → optimize the student with DAgger action imitation → deploy using head/hand goals plus proprioceptive/action history.
- Narrow supported conclusion: on the reported Unitree H1 configuration, 25-step history without explicit global linear velocity performed better in the 20-sequence standing-motion real-world comparison than the tested VIO/MLP/GRU velocity-input variants.
- Important limits: real-world quantitative evaluation is restricted to 20 standing motions; broader manipulation, disturbance, and terrain claims are mainly qualitative demonstrations; the authors' public repository says it is tuned for their showcased hardware; no independent replication was found in this pilot.
- Official code was inspected only for mapping. Commit `750f1fa052641f0fde43669d50cb4e407dabe6c8` exposes `LeggedRobot.load_expert/step`, `OnPolicyRunner.learn`, `PPO._optimize_kin`, and `H1TeleopCfg.domain_rand/control` as concrete links between the paper and implementation.
- The official code is CC BY-NC 4.0 with inherited dependency licenses. This project stores links and original analysis only; it vendors no code, commands, configs, weights, motion data, or paper full text.

## Seven-domain seed corpus expansion

- The technical-plan DOCX defines seven canonical functional domains but does not contain a closed list of paper titles. It names representative lines such as PHC/HOVER/GMT/UniTracker/SONIC for tracking and DeepWBC/ULC/FALCON for loco-manipulation. Therefore “every paper” must be made testable by freezing an explicit repository registry; it cannot mean every paper ever published in the field.
- Initial primary-source discovery found viable anchors: `FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation` (arXiv:2505.06776), `Learning Humanoid Locomotion over Challenging Terrain` (arXiv:2410.03654), `Learning Humanoid Standing-up Control across Diverse Postures`/HoST (arXiv:2502.08378), `FRASA` (arXiv:2410.08655), `TextOp` (arXiv:2602.07439), and `Humanoid Whole-Body Badminton via Multi-Stage Reinforcement Learning` (arXiv:2511.11218).
- New 2026 work such as Perceptive Humanoid Parkour and Hiking in the Wild may serve as “current representative” entries, but recency is not evidence strength. Each must still pass the physical-humanoid, control-relevance, full-paper, reproducibility, and bounded-claim gates.
- Discovery noise included papers about non-humanoid mobile robots, generic human motion generation, and unrelated manipulation. These are excluded unless the paper directly produces data/reference for humanoid control under the Domain 1 exception.
- Primary-source identity checks confirmed `Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking` (GMR, arXiv:2510.02252), `HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots` (arXiv:2410.21229), `ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills` (arXiv:2502.01143), and `ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation` (arXiv:2507.06905).
- The plan's short label `DeepWBC` did not resolve to one unambiguous primary paper in the first exact-title search. It will not be silently invented or substituted. ULC and FALCON provide primary, verifiable coverage for Domain 4; unresolved labels belong in the registry exclusion log.
- Candidate primary-domain decisions: GMR → Domain 1 because its output is robot-feasible reference data; HOVER/OmniH2O → Domain 2 because their output is low-level whole-body action for a supplied command/reference; FALCON/ULC → Domain 4 because the final objective is coordinated locomotion plus end-effector/object work; ASAP → Domain 5 because the paper's main claim and evaluation center on agile whole-body skills and their real-physics transfer.
- The arXiv API fixed the 14-entry versions at the 2026-08-10 capture boundary: 2510.02252v1, 2602.06643v2, 2406.08858v1, 2410.21229v2, 2404.05695v2, 2410.03654v1, 2505.06776v2, 2507.06905v2, 2502.01143v3, 2511.11218v3, 2508.08241v4, 2602.07439v1, 2502.08378v2, and 2410.08655v3.
- Frozen scope: 14 papers, exactly two per domain. This is a reproducible seed corpus, not a claim of field-wide completeness. Registry completion requires the brief, pinned paper source, code/no-code finding, candidate claim, and corpus QA.
- The bundled PDF runtime has `pypdf` 6.10.0, `pdfplumber` 0.11.9, `pdfinfo`, and `pdftoppm`, but no `pdftotext`. Full-text extraction will use `pypdf`; page counts and visual/table locations remain cross-checked against the original project-local PDFs.
- First complete download set and page counts: ASAP 18 pages, challenging-terrain locomotion 42, FALCON 17, HoST 13, Humanoid-Gym 6, HuMI 15, GMR 9, and TextOp 20. Remaining large/slow downloads continue in place and are not treated as complete until `pdfinfo` succeeds.
- Project-local resumable downloads completed OmniH2O, BeyondMimic, ULC, and FRASA; their full text is extracted under ignored `var/`. HOVER and the badminton paper remain active downloads and are not yet eligible for interpretation.
- HOVER v2 is fully read. Its unified command vector covers key-body positions, local joint angles, and root targets; per-episode mode/sparsity masks and a full-motion teacher feed DAgger distillation into a 25-step-history student. Figure 4 is the cleanest mechanism comparison: the distilled policy beats same-mask multi-mode RL in all 32 mode/metric cells. Real quantitative evidence is limited to 20 standing motions; runtime mode switches are mainly qualitative.
- Official `NVlabs/HOVER` was fixed at commit `8088f6cfb42a8f307dc614735197796a86ce8490`, Apache-2.0. `create_mask` implements mode and Bernoulli sparsity selection; `StudentPolicyTrainer` implements student rollout, teacher labels, and action-space imitation updates. The implementation's norm reduction is not textually identical to the paper's squared-L2 notation and must be treated as version-specific.
- Humanoid-Gym v2 is an engineering framework paper: 15-frame actor observations, privileged critic, 100 Hz joint-target policy, 1000 Hz PD, humanoid rewards/randomization, and calibrated MuJoCo replay before two-size XBot deployment. The paper lacks quantitative success denominators; sim-to-sim is a gate, not a guarantee. Official BSD-3-Clause code was pinned at `ae46e201c85a2b17e7f2cea59a441dae7ea88a8f`.
- HT-2 v1 is fully read including 42-page supplement. A 16-step, 1.4M-parameter Transformer is sequence-pretrained from policy/model-based/human flat trajectories, with mask tokens for missing actions, then PPO-fine-tuned on six rigid terrain families. Figure 9 shows better sample efficiency and final performance than scratch even at a 100M versus 200M step budget. Official project links expose no code, so the record is explicitly no-public-code-found.
- FALCON v2 jointly trains upper/lower agents with shared five-step history and uses Jacobian/gravity/torque-limit-derived 3D hand-force bounds. Table 1/2 separate architecture and force-curriculum effects; official MIT code at `a967a6d8494f57777cf8d266a644ac8e45833301` exposes the corresponding force-bound, scaling and contact-position symbols.
- ULC v2 uses a single 29-action G1 policy, sequentially activates velocity/height/torso-arm skills, and adds residual arm actions, fifth-order command interpolation, random delay, wrist-load randomization and CoM tracking. Table V is the cleanest component evidence. The official page still says Code Coming Soon, so no third-party repository was substituted.
- ASAP v3 learns a delta-action model from target-physics trajectories, freezes it into the training simulator, and fine-tunes the deployable policy. Cross-simulator Tables III/IV and real Table V support the mechanism, while the paper explicitly reports motor overheating and two damaged G1 robots. Official MIT code at `df5320cc47dd8cad97961bdfabfe402dd62ad999` maps open/closed-loop residual and PPO rollout symbols.
- Humanoid Badminton v3 trains one 21-DoF policy through footwork, swing and task-refinement rewards. The controlled 46-trial hardware comparison is decisive: EKF target-known returns 42 versus 33 for prediction-free, despite closer simulation results. MoCap dependency, narrow interception envelope, limited stroke repertoire and absent public code are explicit boundaries.
- BeyondMimic v4 combines a compact single-frame tracker with state-latent diffusion and differentiable test-time costs. The 5%→95% latent cartwheel sim-to-sim ablation, adaptive sampling, rotation/history and 2–10 ms latency tests provide the strongest mechanism evidence. Official code identity remains unresolved despite the project page's open-source statement.
- TextOp v1 uses CLIP-conditioned autoregressive robot-motion diffusion at 6.25 Hz and a 50 Hz G1 tracker. Table I gives 30-second real trial denominators and Table II separates module latency from 0.73 s human-perceived response. Official MIT code at `ef6555fb174c9b5c44945a62c7ffc77b5ddbbf22` maps CFG, text/history denoising and streaming updates, with a README version caveat.

### Domain 1 — GMR full-paper pass

- Read all 9 pages of `Retargeting Matters` v1, including method, evaluation, conclusions, and references. The paper compares PHC, ProtoMotions, GMR, and a proprietary Unitree retarget on 21 LAFAN1 sequences retargeted to Unitree G1, then trains one BeyondMimic policy per sequence in IsaacSim.
- Mechanism: match human/robot key bodies → align rest-pose frames → use height-normalized, body-local non-uniform scaling while scaling root translation uniformly → solve a rotation/end-effector IK stage → refine with all key-body position and rotation constraints → sequence frames use the previous solution as initialization → correct global height.
- Decisive locators: Equation 2/3 explains local-body versus root scaling; Equation 4/5 defines the first differential-IK stage; Equation 6 defines the all-key-body refinement; Figure 2 gives the full five-step pipeline; Table I reports sim/sim-DR/sim2sim success; Table II separates success from tracking error; Figure 3 links low-success cases to penetration, self-intersection, and waist-angle jumps; Table III shows sensitivity to the initial reference frame.
- Strongest evidence: Table I uses 100 non-DR, 4096 DR, and 100 ROS/MuJoCo trials per policy. GMR is near-perfect for most sequences and substantially better than PHC/ProtoMotions on the problematic long dances and stop-go run, while the proprietary Unitree data remains the strongest overall baseline. Table II shows GMR mean global body error 104.1 mm versus PHC 247.8, ProtoMotions 139.7, and Unitree 77.2.
- Author limitations: one source dataset (LAFAN1), one robot (G1), no object/environment interaction motions, and occasional GMR optimization jumps that may need tuning. Independent caution: success is “finish without violating root thresholds,” not physical feasibility or hardware safety; experiments are sim/sim2sim rather than real-robot trials.
- Official `YanjieZe/GMR` README confirms MIT licensing, current package version 0.2.0, and later support for many robots/formats. Those later features are not evidence for the v1 paper. The paper-code map must pin a commit and distinguish the paper's G1/LAFAN1 evaluation path from post-publication extensions.

### Domain 1 — HuMI full-paper pass

- Read all 15 pages of HuMI v2, including appendices A-F. Data collection uses two sensorized UMI-style grippers with wrist GoPros and five VIVE Ultimate trackers on hands, pelvis, and feet. The operator sees a Mink/Viser IK preview and changes the human motion to remain feasible for the Unitree G1 without scaling task-space object geometry.
- Hierarchy: synchronized images and five-point SE(3) trajectories feed a 5 Hz high-level Diffusion Policy; IK-expanded whole-body trajectories train a teacher/student 50 Hz tracker; the deployed student receives 25-step proprioceptive/action history plus ten future keypoint waypoints over two seconds and outputs joint-position targets to built-in PD control.
- Three interface mechanisms matter: speed-adaptive EE rewards and curriculum preserve balance before precision; variable-speed reference playback gives the low level time to correct small errors; the next action chunk is anchored to the scheduled target rather than lagging executed pose, while “blind” pelvis/foot targets are expressed as within-chunk relative transforms to avoid global drift.
- Decisive locators: Figures 2/3 explain acquisition and hierarchy; Figure 4 explains chunk discontinuity; Figure 5 shows >5 cm open-loop pelvis drift; Figure 6 provides task ablations; Figure 7 compares collection throughput; Appendix Table I/II specifies rewards/randomization; Appendix Table III specifies high-level policy rates and horizons.
- Strongest evidence is the controlled ablation suite: marriage-proposal success falls 85%→10% without human-in-loop feasibility preview and to 0% without whole-body specification; sword unsheathing falls 85%→50% without variable-speed augmentation; tossing falls 75%→40% when chunks anchor to actual EE pose; absolute blind-pelvis tracking falls 75%→0%. Data collection records 62 versus 28 attempts in 15 minutes and 96.7% versus 64.3% acceptance relative to TWIST2, but both operators were experienced and the comparison is one task/session setup.
- Real-world scope: one Unitree G1 with custom grippers, two wrist GoPro Hero 10 cameras, external workstation, VIVE-based pelvis localization, 5 Hz high-level and 50 Hz low-level control. Generalization uses 350 demonstrations across seven scenes/objects and reports 14/20 success in four unseen scenes/six unseen objects.
- Author limitations: visual trackers require texture/light, low-level controllers are task-specific rather than universal, and only one robot is evaluated. Independent cautions: custom hardware and global VIVE infrastructure weaken claims of pure onboard autonomy; most task success samples are 20 trials and several ablations only 10; robot-free collection still needs robot-aware human adaptation and IK, so it is not embodiment-free.
- The official project page advertises Code and Dataset links, but primary-source searches and the returned page markup did not yield a uniquely identifiable public code repository at capture time. Record code as `advertised_unverified`, not `open_source`, until a repository and commit can be inspected.
