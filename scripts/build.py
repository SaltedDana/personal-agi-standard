#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generate STANDARD.md from the data in criteria/.

Weights, levels and scores ship as data so anyone can re-weight and rebuild.
Usage: python3 scripts/build.py   (from the repo root or anywhere)
Requires: PyYAML  (pip install pyyaml)
"""

import sys
from pathlib import Path
from textwrap import wrap

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
CRITERIA_DIR = ROOT / "criteria"
CHANGELOG = ROOT / "CHANGELOG.md"
TIER_ORDER = ["memory", "operations", "dependability", "compounding"]
TIER_TITLES = {
    "memory": "Memory",
    "operations": "Operations",
    "dependability": "Dependability",
    "compounding": "Compounding",
}
REQUIRED_FIELDS = [
    "id", "name", "grammar", "question", "explainer", "proof_4",
    "weight", "weight_argument", "cost", "origin",
]


def version():
    """The current version is whatever CHANGELOG.md lists first. One source of truth."""
    for line in CHANGELOG.read_text().splitlines():
        if line.startswith("## ["):
            return line.split("[", 1)[1].split("]", 1)[0]
    sys.exit("no version heading found in CHANGELOG.md")


def load():
    grammars = yaml.safe_load((CRITERIA_DIR / "grammars.yaml").read_text())["grammars"]
    subgroups = yaml.safe_load((CRITERIA_DIR / "subgroups.yaml").read_text())["subgroups"]
    retired = yaml.safe_load((CRITERIA_DIR / "retired.yaml").read_text())["retired"]
    tiers = {}
    for tier in TIER_ORDER:
        tiers[tier] = yaml.safe_load((CRITERIA_DIR / f"{tier}.yaml").read_text())
    return grammars, subgroups, retired, tiers


def subgroup_keys(c):
    """A criterion may declare no sub-group, one, or several."""
    v = c.get("subgroup")
    if not v:
        return []
    return [v] if isinstance(v, str) else list(v)


def validate(grammars, subgroups, retired, tiers):
    errors = []
    seen_ids = set()
    for tier, data in tiers.items():
        for c in data["criteria"]:
            cid = c.get("id", "<missing id>")
            if cid in seen_ids:
                errors.append(f"duplicate id {cid}")
            seen_ids.add(cid)
            for f in REQUIRED_FIELDS:
                if f not in c:
                    errors.append(f"{cid}: missing field '{f}'")
            if c.get("grammar") not in grammars:
                errors.append(f"{cid}: unknown grammar '{c.get('grammar')}'")
            if not isinstance(c.get("weight"), int) or not 1 <= c["weight"] <= 5:
                errors.append(f"{cid}: weight must be an integer 1..5")
            if c.get("cost") not in ("low", "medium", "high"):
                errors.append(f"{cid}: cost must be low/medium/high")
            for key in subgroup_keys(c):
                if key not in subgroups:
                    errors.append(f"{cid}: unknown sub-group '{key}'")
    for r in retired:
        rid = r.get("id", "<missing id>")
        for f in ("id", "name", "removed_in", "reason"):
            if f not in r:
                errors.append(f"retired {rid}: missing field '{f}'")
        if rid in seen_ids:
            errors.append(f"retired id {rid} is reused by a live criterion")
    for key, g in subgroups.items():
        if not any(key in subgroup_keys(c)
                   for t in TIER_ORDER for c in tiers[t]["criteria"]):
            errors.append(f"sub-group '{key}' is defined but has no members")
        for f in ("name", "question", "description", "reported_because"):
            if f not in g:
                errors.append(f"sub-group '{key}': missing field '{f}'")
    if errors:
        sys.exit("validation failed:\n  " + "\n  ".join(errors))


def stats(subgroups, tiers):
    all_c = [c for t in TIER_ORDER for c in tiers[t]["criteria"]]
    adversarial = [c for c in all_c if str(c["origin"]).startswith("adversarial")]
    groups = {}
    for key in subgroups:
        members = [c for c in all_c if key in subgroup_keys(c)]
        groups[key] = {
            "members": members,
            "ids": [c["id"] for c in members],
            "count": len(members),
            "max_weighted": sum(4 * c["weight"] for c in members),
        }
    return {
        "total": len(all_c),
        "adversarial": len(adversarial),
        "adversarial_pct": round(100 * len(adversarial) / len(all_c)),
        "max_weighted": sum(4 * c["weight"] for c in all_c),
        "groups": groups,
    }


def id_range(ids):
    """`O10 to O13` when the ids run consecutively, otherwise a plain list."""
    if len(ids) < 3:
        return " and ".join(ids)
    prefix = ids[0].rstrip("0123456789")
    nums = [int(i[len(prefix):]) for i in ids if i.startswith(prefix)]
    if len(nums) == len(ids) and nums == list(range(nums[0], nums[0] + len(nums))):
        return f"{ids[0]} to {ids[-1]}"
    return ", ".join(ids[:-1]) + f" and {ids[-1]}"


def render(grammars, subgroups, retired, tiers):
    s = stats(subgroups, tiers)
    unp = s["groups"]["unprompted"]
    out = []
    w = out.append
    w("# The Personal AGI Standard")
    w("")
    w("A maturity standard for personal AGI: architectures that remember, act,")
    w("stay dependable, and compound for one person.")
    w("")
    w("A personal AGI is an intelligence layer that holds the operator's evolving")
    w("context, acts on their behalf, and is owned by them. Its capability compounds")
    w("as it integrates into their life, not only through access to their devices,")
    w("but by capturing their perspective. What it gives the operator is agency:")
    w("the range of what one person can decide and carry out, widened by a machine")
    w("that knows their context and stays under their direction.")
    w("")
    w("This file is generated from the data in `criteria/` by `scripts/build.py`.")
    w("Do not edit it directly; edit the data and rebuild.")
    w("")
    w(f"**Version {version()}.** {s['total']} criteria in 4 tiers. "
      f"{s['adversarial']} ({s['adversarial_pct']}%) originate from rival "
      "architectures' worldviews (adversarial pass). "
      f"Maximum weighted score: {s['max_weighted']} points.")
    w("")
    w("![The four tiers by weight](assets/tiers.png)")
    w("")
    w("## What the standard optimizes for")
    w("")
    w("The standard optimizes for one operator's leverage, with trust held")
    w("constant. A personal AGI keeps one operator's context whole and applies")
    w("machine capability directly to it. The four tiers are the conditions for")
    w("that: nothing the operator knows or decides gets lost (Memory), work")
    w("happens with them and without them (Operations), output can be trusted")
    w("without watching the machinery (Dependability), and every month of use")
    w("makes the next month better instead of noisier (Compounding). Every")
    w("criterion measures progress toward one of those four promises. Intelligence")
    w("is not the target: the model supplies it, and the weight law zeroes out")
    w("anything a bare model already does. Automation volume is not the target")
    w("either: an autonomous system the operator cannot trust or audit scores")
    w("worse here, because leverage that must be re-checked by hand is not")
    w("leverage. Where two criteria pull against each other, autonomy against")
    w("control or output volume against verification, the tie breaks toward the")
    w("operator's trust.")
    w("")
    w("## How scoring works")
    w("")
    w("- Every criterion is scored 0 to 4 on its declared grammar (below).")
    w("- Scores are absolute and are never adjusted for a system's goals or budget.")
    w("- A system may publish a target profile: a target level per criterion with a")
    w("  reason from a fixed vocabulary (`out of scope for my stage`,")
    w("  `cost exceeds benefit at my volume`, `conflicting design goal`).")
    w("  The measured-versus-target gap is public and disputable; the measurement is not.")
    w("- Every score carries an evidence tag: `verified` (assessor saw it work),")
    w("  `documented` (artifact exists, not exercised), `inferred` (indirect evidence),")
    w("  `unknown` (no evidence either way). Unknown never rounds to zero; it stays unknown.")
    w("- Weighted score = level \u00d7 weight, summed. Weights ship as data; disagree by")
    w("  re-weighting and rebuilding, not by disputing arithmetic.")
    w("- Criterion IDs are stable: a number always points to the same criterion.")
    w("  Criteria are added, edited, re-weighted or retired; a retired ID is never")
    w("  reused, which is why the tier tables have gaps. Retired IDs are listed below.")
    w("- Cross-tier sub-groups (below) are reported as additional subtotals, never instead")
    w("  of the tier totals. A sub-group changes no weight, no level and no ID.")
    w(f"- The unprompted sub-group ({id_range(unp['ids'])}, {unp['max_weighted']} of the "
      f"{s['max_weighted']} points) is")
    w("  scored against artifacts the system itself produces and the operator rules on.")
    w("  Those artifacts record what the system surfaced. Nothing in them establishes what")
    w("  it should have surfaced and missed, because the only source for that list is the")
    w("  operator. The sub-group is reported as its own subtotal for this reason, and its")
    w("  levels are not independently reproducible by a third party. O3, O4 and O9 carry a")
    w("  weaker form of the same limit. A criterion leaves this set when a test supplies the")
    w("  missing denominator; the grammar moves to `measured` and the ID stays.")
    w("")
    w("## Where the criteria come from")
    w("")
    w("Every criterion declares an `origin`, recorded in the tier tables below.")
    w("")
    w("- **`function`**: derived from what the capability must do, written before")
    w("  looking at any product that implements it.")
    w("- **`adversarial:<worldview>`**: written from a rival architecture's")
    w("  worldview, so that the set is not shaped by one builder's assumptions.")
    w("  The pass is mandatory at 20% of criteria and currently stands at "
      f"{s['adversarial']} of {s['total']} ({s['adversarial_pct']}%).")
    worldviews = []
    for tier in TIER_ORDER:
        for c in tiers[tier]["criteria"]:
            origin = str(c["origin"])
            if origin.startswith("adversarial:"):
                name = "`" + origin.split(":", 1)[1] + "`"
                if name not in worldviews:
                    worldviews.append(name)
    worldview_line = "The worldviews used so far: " + ", ".join(worldviews) + "."
    for line in wrap(worldview_line, 72, break_on_hyphens=False):
        w(f"  {line}")
    w("- **`practice+research`**: two sources feed it. The first is the")
    w("  field. Personal AGI stands on AGI research and the machine learning")
    w("  work under it, on the dependable-computing literature that gives")
    w("  Tier 3 its definition of the word, and on the current wave of")
    w("  operators pushing personalization and customization as fast as the")
    w("  models move, in public. The second is a running system: a")
    w("  production single-operator personal AGI in daily use, where every")
    w("  one of these capabilities is exercised under real work rather than")
    w("  described. Criteria tagged this way name capabilities both sources")
    w("  treat as load-bearing. They are weighted under the same law as")
    w("  every other criterion, since importance is a separate question from")
    w("  contribution above a bare model. O3 is the visible case: highly")
    w("  valued, weighted 2.")
    w("")
    w("## Level grammars")
    for gkey, g in grammars.items():
        w("")
        w(f"### `{gkey}`: {g['name']}")
        w("")
        for lvl in range(5):
            w(f"- **{lvl}** {g['levels'][lvl]}")
    w("")
    w("## Cross-tier sub-groups")
    w("")
    w("A sub-group marks criteria that answer one question together while sitting in")
    w("different tiers. Its subtotal is reported in addition to the tier totals, never")
    w("instead of them. Membership is declared per criterion in the data.")
    for key, g in subgroups.items():
        grp = s["groups"][key]
        w("")
        w(f"### {g['name']}: {str(g['question']).strip()}")
        w("")
        w(f"*{grp['count']} criteria · {', '.join(grp['ids'])} · "
          f"{grp['max_weighted']} of the {s['max_weighted']} points*")
        w("")
        w(str(g["description"]).strip())
        w("")
        w(f"**Reported as its own subtotal because:** {str(g['reported_because']).strip()}")
    w("")
    w("## Retired criterion IDs")
    w("")
    w("A criterion can be removed from the standard. Its ID is never reused, so a")
    w("number always points to the same question in every version. This is why the")
    w("tier tables below have gaps.")
    w("")
    w("| ID | Was | Removed in | Why |")
    w("|----|-----|------------|-----|")
    for r in retired:
        w(f"| {r['id']} | {r['name']} | {r['removed_in']} | {str(r['reason']).strip()} |")
    for tier in TIER_ORDER:
        data = tiers[tier]
        crits = data["criteria"]
        w("")
        w(f"## Tier: {TIER_TITLES[tier]}")
        w("")
        w(str(data["description"]).strip())
        w("")
        w("| ID | Criterion | Weight | Grammar | Cost | Origin |")
        w("|----|-----------|--------|---------|------|--------|")
        for c in crits:
            keys = subgroup_keys(c)
            sub = f" ({', '.join(subgroups[k]['name'].lower() for k in keys)})" if keys else ""
            w(f"| {c['id']} | {c['name']}{sub} | {c['weight']} | {c['grammar']} "
              f"| {c['cost']} | {c['origin']} |")
        for c in crits:
            w("")
            keys = subgroup_keys(c)
            sub = (" · sub-group: " + ", ".join(subgroups[k]["name"].lower() for k in keys)
                   if keys else "")
            w(f"### {c['id']}. {c['name']}")
            w("")
            w(f"*Weight {c['weight']} · grammar `{c['grammar']}` · cost tier {c['cost']} "
              f"· origin {c['origin']}{sub}*")
            w("")
            w(str(c["question"]).strip())
            w("")
            w(f"**In plain terms:** {str(c['explainer']).strip()}")
            w("")
            w(f"**Level-4 proof artifact:** {str(c['proof_4']).strip()}")
            w("")
            w(f"**Why this weight:** {str(c['weight_argument']).strip()}")
    w("")
    w("---")
    w("")
    w("Author and maintainer: Dana Maman ([saltedmind.co](https://saltedmind.co)).")
    w("See [README.md](README.md) for scope,")
    w("[CONTRIBUTING.md](CONTRIBUTING.md) for how to submit an assessment or dispute")
    w("a criterion, [ASSESS.md](ASSESS.md) for the machine-runnable assessment")
    w("protocol, and [LIMITS.md](LIMITS.md) for the structural limits of this")
    w("instrument.")
    w("")
    w("Licensed under [CC BY 4.0](LICENSE).")
    w("")
    return "\n".join(out)


def main():
    grammars, subgroups, retired, tiers = load()
    validate(grammars, subgroups, retired, tiers)
    (ROOT / "STANDARD.md").write_text(render(grammars, subgroups, retired, tiers))
    s = stats(subgroups, tiers)
    print(f"STANDARD.md written: {s['total']} criteria, "
          f"{s['adversarial']} adversarial ({s['adversarial_pct']}%), "
          f"max weighted score {s['max_weighted']}, "
          f"{len(retired)} retired ids.")
    for key, grp in s["groups"].items():
        print(f"  sub-group {key}: {grp['count']} criteria "
              f"({', '.join(grp['ids'])}), {grp['max_weighted']} points.")


if __name__ == "__main__":
    main()
