# Known limits

Three limits in this standard are structural. They follow from what the
standard measures and how it measures it, and a later version will not remove
them. Each is stated here with what would.

## 1. The weights are indexed to a moving baseline

A criterion's weight reflects the architecture's contribution above a bare
frontier model with no system around it. That baseline moves with every model
release. Capability that used to require scaffolding gets absorbed into the
model, and the weight of the criteria covering it falls.

A falling weight records that a capability moved out of the scaffolding and
into the model, where everyone receives it without building anything. That is
the outcome this standard wants, and it costs the standard something real:
scores are not comparable across weight versions.

The standard resolves that by versioning the weights and re-weighting on model
releases, never by holding a weight up to protect an old score. What stays
weighted is what the model still does not supply on its own.

**What would remove this limit:** nothing. It is the price of measuring the
architecture instead of the model.

## 2. Assessments are self-reported

Nothing here is audited. An operator, or an assistant working for one, assigns
every level. Self-assessment inflates.

Three things contain the damage:

- The primary reader of an assessment is the operator who ran it. The score
  gates nothing, funds nothing and admits no one anywhere. Inflating it costs
  the person doing it the only thing the exercise produces, which is an
  accurate picture of where their own system fails.
- Every score carries an evidence tag. A level 4 tagged `inferred` with no
  proof artifact is visible to any reader, and so is a file carrying no
  `verified` tags at all.
- Every criterion declares a level-4 proof artifact, so a disputed score has a
  specific thing to ask for.

That containment applies to a self-assessment read by its own operator. It does
not carry over to a public ranking. Any leaderboard built from these files
inherits the incentive to inflate without inheriting the containment, and it
should be read on those terms.

**What would remove this limit:** independent assessment. A second assessor
scoring the same system, with the disagreement between the two published,
measures the instrument as well as the system.

## 3. Four criteria cannot be checked from outside

Thirty-seven of the 41 criteria can be checked by a third party with access.
Their level-4 artifacts are benchmarks, negative tests, drill records or
samples a stranger can resolve. Whether anyone has actually run them is a
separate question, and the evidence tags answer that one.

Four criteria are different. O10 to O13, the unprompted sub-group, worth 72 of
the 644 points, are scored against artifacts the system itself produces and the
operator rules on. Those artifacts record what the system surfaced. Nothing in
them establishes what it should have surfaced and missed, because the only
source for that list is the operator, who is also the person who does not
remember what was forgotten. There is no denominator.

That is why the sub-group is reported as its own subtotal instead of being
folded into the Operations score. It also carries the loudest claim in this
category. The subtotal exists so the claim travels with its own warning.

O3, O4 and O9 carry a weaker form of the same limit.

**What would remove this limit:** a test that supplies the denominator from
outside the system. Held-out commitments extracted by an independent model and
counted against what surfaced would do it for O10. Planted signals counted
against what was caught would do it for O11. A pre-registered goal file read by
an independent judge against the transcripts would do it for O12. When such a
test exists for a criterion, its grammar moves to `measured` and its ID stays.

---

Author and maintainer: Dana Maman ([saltedmind.co](https://saltedmind.co)).
See [STANDARD.md](STANDARD.md) for the criteria and [ASSESS.md](ASSESS.md) for
the assessment protocol.
