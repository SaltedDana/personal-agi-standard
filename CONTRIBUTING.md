# Contributing

Two kinds of contribution are welcome: arguing with the standard, and
reporting a system against it. Both are load-bearing. Levels and weights are
still moving and they move on argument, and an untested criterion stays
untested until real systems have been scored against it in public.

## Argue with the standard

Open an issue. Disagreement, questions and reports of what actually happened
when you built something are all useful, and none of them require you to have
run an assessment first. The useful shapes:

- **"This criterion is wrong"**: argue from function (what the capability
  must do), not from what your system happens to implement.
- **"This weight is wrong"**: argue against the stated `weight_argument`
  under the weight law (contribution above a bare model). Arguments from a
  capability's usefulness alone do not move weights.
- **"A criterion is missing"**: propose it with a grammar, a level-4 proof
  artifact, a weight argument, and an origin. Criteria that no auditable
  artifact could ever prove are not accepted.
- **"This is what happened when I built it"**: an experience report, with no
  proposed change attached. What broke, what was harder than the level makes
  it sound, where the grammar failed to describe what you actually have. These
  are how missing criteria get found.
- **Re-weighting for your own use** needs no permission: weights are data,
  edit `criteria/*.yaml` and run `python3 scripts/build.py` in your fork.

## Submit an assessment

1. Run the protocol in [ASSESS.md](ASSESS.md) against your system (hand the
   repo to your AI assistant, or do it by hand).
2. Copy `systems/TEMPLATE.yaml` to `systems/<your-system>.yaml` and fill it
   in. Every score needs a level, an evidence tag, and at least one evidence
   line. `unknown` is a valid level.
3. Read the file before you open the pull request. An assessment describes
   your own system, so evidence lines can pick up file paths, tool names,
   client names or business details. Redact anything you would not want
   public. "Scheduler config, 6 jobs" works as evidence; the job names add
   nothing. Never include credentials, API keys or tokens.
4. Open a pull request. State in the PR whether the assessment was
   machine-run, human-run, or mixed.

A published assessment is the only public record of what this standard looks
like in use. It is also what makes a level disputable by someone other than
its author, so assessments and arguments feed each other.

Assessments are self-reported. The evidence lines are what make them worth
reading; a score without evidence will be asked to become `unknown`.

## Rules that are not up for PR

- Scores are absolute; no adjustment for goals or budget. Declared target
  profiles (see STANDARD.md) are the mechanism for "not my goal".
- Levels and weights are fixed within a released version. Disputes are
  accepted any time; accepted changes land in the next version and are logged
  in CHANGELOG.md. Below 1.0.0 the criteria set is still moving, so a minor
  version can add, remove or re-weight criteria; from 1.0.0 on, that requires
  a major version.
- Criterion IDs are immutable. A removed criterion keeps its ID, recorded in
  `criteria/retired.yaml` and listed in STANDARD.md. IDs are never reused.
- STANDARD.md is generated. Edit `criteria/*.yaml` and run
  `python3 scripts/build.py`; a pull request that edits STANDARD.md by hand
  will be asked to move the change into the data.
- No em dashes in the prose. House style.

## License

Contributions to the standard, the criteria data, the documentation and the
assessments are accepted under [CC BY 4.0](LICENSE). Contributions to the
build script in `scripts/` are accepted under the
[MIT License](scripts/LICENSE).
