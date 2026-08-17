# Changelog

All notable changes to the standard itself. Assessments in `systems/` have
their own history via git.

## [0.1.0] - 2026-08-18

First public release.

- Four tiers: Memory (10 criteria, 36 points), Operations (14, 55),
  Dependability (11, 44), Compounding (6, 26). 41 criteria, maximum weighted
  score 644.
- Three level grammars: default (automation ladder), measured (measurement
  ladder), evidence (improvement-evidence ladder). Five levels each.
- Weight law fixed: a criterion's weight reflects the architecture's
  contribution above a bare frontier model. The argument ships per criterion
  in `criteria/*.yaml`.
- Adversarial pass: 12 of 41 criteria (29%) originate from rival
  architectures' worldviews. Origin is recorded per criterion and the
  vocabulary is defined in STANDARD.md.
- Two cross-tier sub-groups, reported as extra subtotals and never instead of
  the tier totals: Unprompted (O10 to O13, 72 points) and Owns (M10 and D8,
  28 points). Neither changes a weight, a level or an ID.
- Sub-groups are data. `criteria/subgroups.yaml` holds the definition and
  membership is declared per criterion, so there is one source of truth.
- ASSESS.md, a machine-runnable assessment protocol with anti-flattery rules,
  and `systems/TEMPLATE.yaml` for reporting a result.
- LIMITS.md: the three structural limits of the instrument, each with what
  would remove it.
- Licensed CC BY 4.0 for the standard, the criteria data, the documentation
  and the assessments; MIT for the build script in `scripts/`.
- Three IDs (M11, D7, D9) were retired during pre-release drafting and are
  listed in STANDARD.md. A retired ID is never reused, which is why the tier
  tables have gaps.
- Status: draft. Levels and weights can still change on argument, and freeze
  at 1.0.0.

Author: Dana Maman.
