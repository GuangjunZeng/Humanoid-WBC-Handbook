# Seed paper corpus

This directory contains original Chinese engineering interpretations of a deliberately bounded seed corpus. It is not an exhaustive survey and does not rank papers by popularity.

The canonical inventory is [`registry.json`](registry.json). “Every paper is interpreted” means every frozen registry entry is `complete` and passes the checks below.

## Completion gate

- full paper and relevant appendices read at the pinned version;
- problem, prior gap, input → processing → output mechanism, and strongest experiment explained;
- at least three exact formula/Figure/Table locators;
- public implementation mapped to at least two concrete symbols, or an explicit no-public-code finding;
- robot, simulator, sensors, control interface/rate, data, deployment assumptions, and unknowns recorded;
- author-stated limitations separated from independent engineering judgment;
- hardware-facing conclusions narrowed and linked to the project safety policy;
- version-pinned source metadata and at least one bounded candidate Engineering Claim added.

## Domain status and navigation

| Domain | Papers | Complete |
|---|---:|---:|
| [Training data & retargeting](domains/training-data-retargeting.md) | 2 | 2 |
| [Universal tracking & teleoperation](domains/universal-tracking-teleoperation.md) | 2 | 2 |
| [Locomotion & terrain](domains/locomotion-terrain.md) | 2 | 2 |
| [Loco-manipulation & EE WBC](domains/loco-manipulation-wbc.md) | 2 | 2 |
| [Sports & athletic skills](domains/sports-athletic-skills.md) | 2 | 2 |
| [Motion generation & commandable behavior](domains/motion-generation.md) | 2 | 2 |
| [Recovery, falling, safety & force interaction](domains/recovery-safety-force.md) | 2 | 2 |
| **Total** | **14** | **14** |

## Selection boundary

Each paper has exactly one primary functional domain. Secondary relevance is discussed in the brief rather than duplicating the paper across folders. The corpus favors papers with physical-humanoid control relevance, decisive experiments, and public code or enough implementation detail to support engineering analysis.

Ambiguous shorthand from the planning document—such as `DeepWBC` without a uniquely verifiable primary record—is not silently converted into a citation. Such labels remain discovery leads until identity can be established from a primary source.

Run `python3 scripts/check_corpus.py` to verify the frozen inventory, per-domain balance, brief locators, paper-source identity, claim coverage, and hardware safety-case presence without network access.
