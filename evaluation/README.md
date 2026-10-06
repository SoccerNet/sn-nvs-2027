# Evaluation — awaiting 2027 specification

No official 2027 scorer is released in this repository yet. The task leads must confirm the protocol before implementation.

## Required decisions

- Confirm supplied cameras, calibration, target views and timestamps.
- Specify scene-specific training versus generalization to unseen scenes.
- Freeze target resolution, color space, image format and filename mapping.
- Choose primary metric and aggregation across frames, views and scenes.
- Decide foreground masking, temporal evaluation and compute restrictions.

## Planned deliverables

A versioned local scoring command, environment, synthetic format example, malformed-submission checks, baseline score, and CodaBench integration if selected. Earlier-edition scores and formats are background only.

See [baseline references](../baselines/README.md) and [draft rules](../docs/rules.md).
