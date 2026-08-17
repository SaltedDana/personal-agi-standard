# The Personal AGI Standard

A maturity standard for personal AGI: architectures that remember, act,
stay dependable, and compound for one person.

A personal AGI is an intelligence layer that holds the operator's evolving
context, acts on their behalf, and is owned by them. Its capability compounds
as it integrates into their life, not only through access to their devices,
but by capturing their perspective. What it gives the operator is agency:
the range of what one person can decide and carry out, widened by a machine
that knows their context and stays under their direction.

This file is generated from the data in `criteria/` by `scripts/build.py`.
Do not edit it directly; edit the data and rebuild.

**Version 0.1.0.** 41 criteria in 4 tiers. 12 (29%) originate from rival architectures' worldviews (adversarial pass). Maximum weighted score: 644 points.

## What the standard optimizes for

The standard optimizes for one operator's leverage, with trust held
constant. A personal AGI keeps one operator's context whole and applies
machine capability directly to it. The four tiers are the conditions for
that: nothing the operator knows or decides gets lost (Memory), work
happens with them and without them (Operations), output can be trusted
without watching the machinery (Dependability), and every month of use
makes the next month better instead of noisier (Compounding). Every
criterion measures progress toward one of those four promises. Intelligence
is not the target: the model supplies it, and the weight law zeroes out
anything a bare model already does. Automation volume is not the target
either: an autonomous system the operator cannot trust or audit scores
worse here, because leverage that must be re-checked by hand is not
leverage. Where two criteria pull against each other, autonomy against
control or output volume against verification, the tie breaks toward the
operator's trust.

## How scoring works

- Every criterion is scored 0 to 4 on its declared grammar (below).
- Scores are absolute and are never adjusted for a system's goals or budget.
- A system may publish a target profile: a target level per criterion with a
  reason from a fixed vocabulary (`out of scope for my stage`,
  `cost exceeds benefit at my volume`, `conflicting design goal`).
  The measured-versus-target gap is public and disputable; the measurement is not.
- Every score carries an evidence tag: `verified` (assessor saw it work),
  `documented` (artifact exists, not exercised), `inferred` (indirect evidence),
  `unknown` (no evidence either way). Unknown never rounds to zero; it stays unknown.
- Weighted score = level × weight, summed. Weights ship as data; disagree by
  re-weighting and rebuilding, not by disputing arithmetic.
- Criterion IDs are stable: a number always points to the same criterion.
  Criteria are added, edited, re-weighted or retired; a retired ID is never
  reused, which is why the tier tables have gaps. Retired IDs are listed below.
- Cross-tier sub-groups (below) are reported as additional subtotals, never instead
  of the tier totals. A sub-group changes no weight, no level and no ID.
- The unprompted sub-group (O10 to O13, 72 of the 644 points) is
  scored against artifacts the system itself produces and the operator rules on.
  Those artifacts record what the system surfaced. Nothing in them establishes what
  it should have surfaced and missed, because the only source for that list is the
  operator. The sub-group is reported as its own subtotal for this reason, and its
  levels are not independently reproducible by a third party. O3, O4 and O9 carry a
  weaker form of the same limit. A criterion leaves this set when a test supplies the
  missing denominator; the grammar moves to `measured` and the ID stays.

## Where the criteria come from

Every criterion declares an `origin`, recorded in the tier tables below.

- **`function`**: derived from what the capability must do, written before
  looking at any product that implements it.
- **`adversarial:<worldview>`**: written from a rival architecture's
  worldview, so that the set is not shaped by one builder's assumptions.
  The pass is mandatory at 20% of criteria and currently stands at 12 of 41 (29%).
  The worldviews used so far: `graph-memory`, `open-knowledge-metabolism`,
  `benchmarked-retrieval`, `graceful-degradation`, `plain-files`,
  `measured-autonomy`, `hooks-not-prompts`, `predictable-cost`,
  `tested-harness`, `confidence-scored-instincts`.
- **`practice+research`**: two sources feed it. The first is the
  field. Personal AGI stands on AGI research and the machine learning
  work under it, on the dependable-computing literature that gives
  Tier 3 its definition of the word, and on the current wave of
  operators pushing personalization and customization as fast as the
  models move, in public. The second is a running system: a
  production single-operator personal AGI in daily use, where every
  one of these capabilities is exercised under real work rather than
  described. Criteria tagged this way name capabilities both sources
  treat as load-bearing. They are weighted under the same law as
  every other criterion, since importance is a separate question from
  contribution above a bare model. O3 is the visible case: highly
  valued, weighted 2.

## Level grammars

### `default`: Automation ladder

- **0** Absent. The capability does not exist in any form.
- **1** Manual and ad hoc. The operator does it by hand when they remember to.
- **2** Systematic but unverified. A defined mechanism exists and is used, but nothing checks that it works.
- **3** Automated with evidence. Runs without the operator, and there is at least one auditable artifact showing it ran and worked.
- **4** Automated, measured over time, survives failure. Runs without the operator, its success rate is tracked, and there is evidence it kept working (or failed loudly and recovered) through at least one real failure.

### `measured`: Measurement ladder

- **0** Absent. The capability does not exist.
- **1** Exists, quality unknown. The capability works anecdotally; no one has measured it.
- **2** Spot-checked informally. Someone has probed quality by hand, without a method that another person could repeat.
- **3** Measured once, number stated. A repeatable method produced at least one concrete number (recall@k, error rate, hit rate), and the number is written down.
- **4** Measured continuously. The number is tracked over time, the trend is visible, and a threshold triggers action when it degrades.

### `evidence`: Improvement-evidence ladder (Compounding tier)

- **0** No improvement claim is possible. Nothing accumulates.
- **1** Anecdotal. The operator feels the system got better; no artifact supports it.
- **2** Mechanism without proof. A mechanism intended to produce improvement exists (feedback capture, pattern extraction), but no artifact shows the system actually got better.
- **3** One auditable artifact proves improvement. A stranger could inspect a concrete before/after artifact and agree the system improved.
- **4** Sustained, methodical proof. Repeated measurements over time show improvement continuing, and the measurement method itself is published with the claim.

## Cross-tier sub-groups

A sub-group marks criteria that answer one question together while sitting in
different tiers. Its subtotal is reported in addition to the tier totals, never
instead of them. Membership is declared per criterion in the data.

### Unprompted: Is the system proactive?

*4 criteria · O10, O11, O12, O13 · 72 of the 644 points*

Work the system initiates itself: the operator's own commitments surfaced before anyone asks (O10), drift and opportunity raised without a prompt (O11), goals held across sessions rather than restated (O12), and the acceptance rate that decides whether initiative is worth having (O13).

**Reported as its own subtotal because:** A system can score well across Operations while never moving first, and the difference matters more than the tier total shows. The subtotal separates the two, and O13 keeps it honest by measuring how much of the unprompted output the operator actually wanted. This sub-group also carries the weakest evidence in the standard: its artifacts record what the system surfaced and cannot record what it missed, so its levels are not independently reproducible by a third party.

### Owns: What survives if every vendor withdraws?

*2 criteria · M10, D8 · 28 of the 644 points*

Ownership is the word "personal" cashed out mechanically: memory in open formats the operator can take elsewhere (M10), and a demonstrated survival of an upstream change the operator did not choose (D8).

**Reported as its own subtotal because:** These two criteria sit in different tiers because each earns its weight for a different reason: M10 shapes how memory is stored, D8 tests what happens when someone else's decision changes the ground under the system. Read together they answer whether the system is actually the operator's or only on loan from a vendor, on the only axis where a small system beats a centralized one. This is a subtotal and not a fifth tier because independence does not change what the system can do today, which is the same argument that sets M10's weight at 3. A plain-text folder that does nothing scores well here and near zero everywhere else, and that is the correct result.

## Retired criterion IDs

A criterion can be removed from the standard. Its ID is never reused, so a
number always points to the same question in every version. This is why the
tier tables below have gaps.

| ID | Was | Removed in | Why |
|----|-----|------------|-----|
| M11 | Confidentiality separation | pre-release | Out of scope. Protecting sensitive material is a different concern from the independence from a vendor that the Owns sub-group measures. |
| D7 | Security and privacy posture | pre-release | Out of scope, on the same argument as M11. |
| D9 | Clean-room mode | pre-release | Out of scope, on the same argument as M11. |

## Tier: Memory

What the system collects and keeps about the operator and their world: facts, interests, projects, decisions, preferences, commitments. The tier scores the memory itself, from capture through representation, retrieval, hygiene and ownership. A bare model remembers nothing between sessions; everything in this tier is architecture.

| ID | Criterion | Weight | Grammar | Cost | Origin |
|----|-----------|--------|---------|------|--------|
| M1 | Capture coverage | 5 | default | medium | function |
| M2 | Capture automaticity | 4 | default | medium | function |
| M3 | Structured representation | 3 | default | medium | adversarial:graph-memory |
| M4 | Provenance per fact | 3 | default | medium | adversarial:graph-memory |
| M5 | Confidence and freshness per claim | 4 | default | medium | adversarial:open-knowledge-metabolism |
| M6 | Retrieval precision, measured | 4 | measured | high | adversarial:benchmarked-retrieval |
| M7 | Retrieval quality at scale | 4 | measured | high | adversarial:graph-memory |
| M8 | Retrieval degradation path | 3 | default | low | adversarial:graceful-degradation |
| M9 | Correction and forgetting | 3 | default | medium | function |
| M10 | Data ownership and portability (owns) | 3 | default | low | adversarial:plain-files |

### M1. Capture coverage

*Weight 5 · grammar `default` · cost tier medium · origin function*

Is knowledge about the operator (decisions, preferences, projects, commitments, relationships) captured across the surfaces where it actually appears: conversations, documents, meetings, messages, browsing?

**In plain terms:** This is the raw-material question. Knowledge about an operator appears on many surfaces during a normal week: chat sessions, documents, meeting transcripts, messages, browsing. This criterion asks how many of those surfaces actually feed the memory store. A system that only remembers what the operator manually types into a notes app scores low even if the notes are excellent, because most knowledge never reached it. A system whose pipelines capture decisions from conversations, ingest meeting recordings, and file dropped documents covers the surfaces where knowledge actually lives.

**Level-4 proof artifact:** A coverage map listing capture surfaces, plus sampled evidence that facts appearing on those surfaces reached the store within a defined window.

**Why this weight:** A bare model captures nothing; every remembered fact exists only because the architecture caught it. This is the tier's foundation: everything downstream retrieves what capture caught.

### M2. Capture automaticity

*Weight 4 · grammar `default` · cost tier medium · origin function*

Does memory form as a byproduct of normal work (session hooks, ingest pipelines, scheduled extraction), or only when the operator remembers to file things?

**In plain terms:** Whether remembering costs the operator discipline. Failing looks like a great filing system that depends on the operator remembering to file: it works for two weeks and collapses under a busy month. Passing looks like memory forming as a side effect of work: a session ends and a hook extracts the decisions made in it; a file lands in the inbox and a scheduled job processes it. The test is simple: if the operator stops doing anything deliberate about memory, does capture continue?

**Level-4 proof artifact:** Logs showing memory written by automatic triggers over a sustained period, with no manual filing step in the path.

**Why this weight:** Manual capture collapses under real life; the architecture's contribution is removing the operator's discipline from the loop. Weighted one below coverage because a diligent operator can partially compensate by hand.

### M3. Structured representation

*Weight 3 · grammar `default` · cost tier medium · origin adversarial:graph-memory*

Are facts stored as atomic units with explicit links or typed relations, so questions that span several facts ("which clients touched X and what did I promise them") are answerable, rather than as undifferentiated prose blobs?

**In plain terms:** How facts are shaped once stored. A page of prose about a client contains facts, but they are trapped in the paragraph. Structured representation means each fact is an atomic unit connected to others by explicit links or typed relations, so a question that spans several facts ("which clients touched topic X, and what did I promise each of them") can be answered by following connections instead of re-reading everything. A vault of well-written essays fails this even when every fact is present, because nothing can traverse it. Note the difference from M4: M3 is about how facts connect to each other; M4 is about where each fact came from.

**Level-4 proof artifact:** A schema or convention document, plus a worked multi-hop query answered by traversing stored relations.

**Why this weight:** A strong model can partially reconstruct structure from prose at query time, at token cost. The architecture's delta is real but partial, so this weighs mid-range rather than high.

### M4. Provenance per fact

*Weight 3 · grammar `default` · cost tier medium · origin adversarial:graph-memory*

Does every stored fact trace to its source and date, at the statement level rather than the file level?

**In plain terms:** Every stored statement should be able to answer "says who, and since when". Provenance at the file level ("this page summarizes that podcast") is weaker than provenance at the statement level ("this specific claim came from minute 34" or "from the March email"). The payoff is auditability: when a stored fact turns out wrong, statement-level provenance lets you trace it to its source, judge whether the source was misread or the world changed, and fix every derived copy. Without it, a wrong fact is just wrong, with no trail.

**Level-4 proof artifact:** A random sample of stored facts, each resolvable to a dated source a stranger could check.

**Why this weight:** A bare model cannot cite where a belief came from; the store can. The delta is real, but provenance is a means to trust rather than a capability the operator feels daily, so it weighs mid-range.

### M5. Confidence and freshness per claim

*Weight 4 · grammar `default` · cost tier medium · origin adversarial:open-knowledge-metabolism*

Does a stored fact carry how sure and how fresh it is? Is there an enforced rule that classifies every fact by how it ages (timeless; dated with a validity window; defeasible, meaning valid until contradicted and replaced only with operator approval; or a pointer to a live source), with a per-class policy and a linter or audit that catches violations?

**In plain terms:** Facts age at different speeds, and a store that treats them uniformly will confidently assert last year's world. Passing means every fact is classified by how it ages, each class has a policy, and a linter enforces it. Example classes: volatile facts like monthly business revenue expire on a schedule; cyclical facts like client contact details require re-verification every couple of years; defeasible facts like research conclusions stay valid until contradicted by new evidence, and are replaced only with operator approval; timeless facts like past decisions never expire; pointer facts like a tool's current price are stored as a reference to a live source rather than a copied value. The linter is what makes this real: it flags the revenue figure that is two months old and the contact unverified for three years.

**Level-4 proof artifact:** The rule as written, plus linter or audit output showing stale or unmarked claims being caught.

**Why this weight:** Stale memory is worse than no memory: a bare model with no memory cannot confidently assert last year's facts as current, but a naive store will. The architecture must actively prevent a failure mode it created.

### M6. Retrieval precision, measured

*Weight 4 · grammar `measured` · cost tier high · origin adversarial:benchmarked-retrieval*

When the system reaches into memory for a task, do the right facts come back? Not "does search exist" but "has retrieval quality been measured and stated as a number" (recall@k, precision, answer accuracy on a test set).

**In plain terms:** The gap this measures is between an installed feature and a known capability. Passing looks like a fixed test set of questions with known correct facts, run against the store, producing a number: recall@10 of 85 percent, or answer accuracy of 9 in 10. Failing looks like a semantic index that demos well and has never been scored. Without the number, every downstream claim about the system "knowing" things rests on anecdote.

**Level-4 proof artifact:** A retrieval benchmark with a published method and number, tracked over time.

**Why this weight:** Retrieval is where remembering becomes usable; unmeasured retrieval is a feeling, not a capability. The bare model has nothing to retrieve from, so the whole capability is architecture.

### M7. Retrieval quality at scale

*Weight 4 · grammar `measured` · cost tier high · origin adversarial:graph-memory*

Does answer quality hold as the corpus grows by an order of magnitude, and is the degradation curve known rather than assumed?

**In plain terms:** Retrieval that works on two thousand documents can quietly degrade at twenty thousand: more near-duplicates, more stale hits, more plausible-but-wrong neighbors. This criterion asks whether the degradation curve is known rather than assumed: the same benchmark run at two corpus sizes an order of magnitude apart. It exists because memory systems are sold on their behavior at small scale and lived with at large scale.

**Level-4 proof artifact:** Measurements of retrieval or answer quality at two corpus sizes an order of magnitude apart, with the difference stated.

**Why this weight:** Every memory architecture works at fifty notes. The architectural claim is that day 1,000 still works; a system that silently degrades with growth defeats the point of accumulating at all.

### M8. Retrieval degradation path

*Weight 3 · grammar `default` · cost tier low · origin adversarial:graceful-degradation*

When an index, embedding backend, or search service is down, does retrieval fall back to something cheaper (keyword, catalog), or does the system's memory effectively vanish?

**In plain terms:** What remains of memory when the clever layer is down. If retrieval depends on an embedding index or a search service, the day that component breaks is the day the system's memory effectively vanishes, unless there is a cheaper fallback: plain files searchable by keyword, a human-readable catalog. Passing means the fallback exists and has actually been exercised (kill the index for a day and verify the system still answers). Architectures where the primary path is already plain files pass almost by construction; architectures where a dead vector database means amnesia fail.

**Level-4 proof artifact:** A documented fallback chain, plus evidence of an actual failover event or drill in which answers kept flowing.

**Why this weight:** A resilience property of the memory rather than a new capability. The delta above the bare model is keeping an existing capability alive under failure, so it weighs mid-range.

### M9. Correction and forgetting

*Weight 3 · grammar `default` · cost tier medium · origin function*

Can the operator correct or delete a stored fact and trust that the change propagates: duplicates consolidated, derived pages updated, the dead belief marked dead rather than resurfacing later?

**In plain terms:** Memory must be correctable, and corrections must stick. When the operator deletes or fixes a stored fact, the change has to propagate: duplicates consolidated, derived pages updated, the dead belief marked dead. The failure mode this guards against is the zombie fact: corrected in one place, resurfacing months later from an uncorrected copy, now wearing the authority of memory.

**Level-4 proof artifact:** A worked example: one correction traced through the store, showing every place the old fact lived and that none of them still asserts it.

**Why this weight:** A bare model forgets everything, which trivially includes wrong facts. The store creates the persistence-of-error problem and must solve it; the delta is corrective rather than additive.

### M10. Data ownership and portability

*Weight 3 · grammar `default` · cost tier low · origin adversarial:plain-files · sub-group: owns*

Is the memory stored in open formats the operator owns, readable without the tool, exportable whole, and usable by a different runtime or model?

**In plain terms:** Whose data is it, mechanically. Passing means the memory is stored in open formats the operator can read without the tool, export whole, and hand to a different runtime or model: plain text files in a directory the operator controls. Failing means the memory lives in a proprietary store with partial or no export, so leaving the tool means leaving years of accumulated context behind. This is the criterion that decides whether the operator owns the system or the system owns the operator.

**Level-4 proof artifact:** A demonstrated export or a second runtime answering questions from the same store.

**Why this weight:** Ownership does not change what the system can do today; it changes what survives tomorrow. Weighted mid-range because its value is conditional on an upstream change the operator did not choose, which D8 tests directly.

## Tier: Operations

What the system does with its memory of the operator: goal-driven work executed with skills, agents, routines and loops, grounded in accumulated context rather than a fresh briefing each time. This tier scores the acting; the machinery's own reliability while it acts belongs to Dependability. The "unprompted" sub-group covers work the system starts by itself; its score is also reported separately.

| ID | Criterion | Weight | Grammar | Cost | Origin |
|----|-----------|--------|---------|------|--------|
| O1 | Context-grounded execution | 5 | default | medium | function |
| O2 | Skill packaging and reuse | 3 | default | low | function |
| O3 | Range extension | 2 | default | low | practice+research |
| O4 | Reflective partnership | 2 | default | low | practice+research |
| O5 | Scheduled routines | 5 | default | medium | function |
| O6 | Parallel presence | 4 | default | medium | function |
| O7 | Action in absence | 5 | default | high | practice+research |
| O8 | External actuation | 3 | default | medium | function |
| O9 | Escalation judgment | 4 | default | medium | function |
| O10 | Commitment tracking (unprompted) | 5 | default | medium | practice+research |
| O11 | Drift and opportunity surfacing (unprompted) | 4 | default | high | practice+research |
| O12 | Goal grip (unprompted) | 5 | default | medium | practice+research |
| O13 | Initiative precision (unprompted) | 4 | measured | medium | function |
| O14 | Autonomy horizon | 4 | measured | high | adversarial:measured-autonomy |

### O1. Context-grounded execution

*Weight 5 · grammar `default` · cost tier medium · origin function*

Does the system execute tasks using the operator's accumulated context (goals, preferences, history, current projects) without being re-briefed, and is the grounding visible in the output rather than claimed?

**In plain terms:** The point of accumulated context is that work products arrive already grounded in it. Ask the system to draft a proposal and it should come back in the operator's voice, aware of the pricing history with that client, respecting constraints established months ago, without a re-briefing paragraph. The grounding must be visible in the output, not claimed in marketing. A bare model produces a competent generic draft; the architecture's contribution is everything that makes it this operator's draft.

**Level-4 proof artifact:** Side-by-side artifacts: the same task done cold versus through the system, with the context-dependent differences identified.

**Why this weight:** This is the hinge between the Memory tier and everything else: memory that never reaches the work is storage, not an operating system. A bare model needs the full briefing every single time.

### O2. Skill packaging and reuse

*Weight 3 · grammar `default` · cost tier low · origin function*

Is know-how packaged as named, reusable procedures (skills, templates, playbooks) that are discoverable when relevant, rather than re-derived or re-prompted from scratch each time?

**In plain terms:** Whether know-how accumulates as named, reusable procedures (skills, templates, playbooks) that surface when relevant, or gets re-derived from scratch each time. The test: when a task type repeats, does the system reach for a packaged procedure that encodes the lessons of previous rounds, or does quality depend on how well the operator prompts today? Discoverability is part of the criterion: a skill library nobody triggers is shelf-ware.

**Level-4 proof artifact:** A skill inventory plus invocation logs showing repeated reuse, and a discovery mechanism that loads the right skill without loading all.

**Why this weight:** A bare model can perform most of these procedures when prompted well; the architecture's delta is consistency and zero re-derivation cost, not the ability itself.

### O3. Range extension

*Weight 2 · grammar `default` · cost tier low · origin practice+research*

Does the system reliably extend the operator into fields they never practiced (design, code, data analysis), with persistent quality gates per field, so results are dependable rather than occasional?

**In plain terms:** Whether the system reliably extends the operator into fields they never practiced: a non-designer shipping decks, a non-programmer shipping working software. The key word is reliably. One good result is the model; dependable results require persistent quality gates per field (a design QA pass, a test suite) so the operator can trust output in a domain where they cannot judge the details themselves.

**Level-4 proof artifact:** Delivered artifacts in fields the operator does not practice, each passed through a defined per-field quality gate.

**Why this weight:** Most of this power is the bare model's: a chat window already writes code and analyzes data. The architecture adds persistence and quality gates, a real but thin layer, so this weighs low despite being one of the most personally valued capabilities. Weight follows the contribution-above-bare-model law, not felt value.

### O4. Reflective partnership

*Weight 2 · grammar `default` · cost tier low · origin practice+research*

Does deep accumulated context enable dialogue the operator could not have with a stranger: reflection, self-insight, learning, in-context teaching that adapts to what the operator already knows?

**In plain terms:** The conversational payoff of deep context: dialogue the operator could not have with a stranger. Reflection that draws on months of logged decisions, teaching that adapts to what the operator already knows instead of starting from zero, pattern-surfacing ("you have made this trade-off three times and regretted it twice"). A bare model can be a brilliant conversationalist; it cannot be a partner with a shared history.

**Level-4 proof artifact:** Session artifacts where the system's contribution demonstrably depends on longitudinal knowledge of the operator (references to past decisions, patterns across months), not on the current conversation alone.

**Why this weight:** A bare model is already a strong reflective interlocutor within one conversation. The architecture's delta is longitudinal grounding, which deepens the dialogue but does not create the capability.

### O5. Scheduled routines

*Weight 5 · grammar `default` · cost tier medium · origin function*

Do recurring jobs run unattended on a schedule and produce output that is actually used, rather than output that accumulates unread?

**In plain terms:** Do recurring jobs run unattended on a schedule, and produce output someone actually uses? Passing means real scheduler entries (cron, launchd) with a run history, failure visibility, and recovery for missed windows: the morning brief that appears every day including the days the operator forgot it exists. Failing means "routines" that are actually the operator remembering to ask.

**Level-4 proof artifact:** Scheduler configuration plus run logs plus evidence of consumption (outputs referenced, acted on, or feeding other work).

**Why this weight:** A bare model does nothing between prompts. Work that happens without the operator present is the clearest possible architecture delta, and it is the mechanism behind most of this tier.

### O6. Parallel presence

*Weight 4 · grammar `default` · cost tier medium · origin function*

Can multiple workstreams advance concurrently without the operator attending to each: parallel agents, background jobs, queued pipelines that do not serialize behind one conversation?

**In plain terms:** Whether the system can be in more than one place at once: background jobs running while the operator works on something else, parallel agents on independent subtasks, a channel from the operator's phone while away from the machine. This is the difference between a tool the operator operates and a staff that operates alongside them.

**Level-4 proof artifact:** Logs of overlapping unattended runs on distinct workstreams, with their outputs.

**Why this weight:** Being in several places at once is impossible for the operator and for a single chat session; the architecture manufactures it. One step below routines because it builds on them.

### O7. Action in absence

*Weight 5 · grammar `default` · cost tier high · origin practice+research*

If the operator disappears for days, does the system keep operating: routines run, incoming work is triaged, decisions above its authority queue cleanly for return, nothing silently rots?

**In plain terms:** The strongest form of operating: artifacts exist because the system acted while the operator was absent. The brief was written before they woke; the inbox was processed overnight; the health check ran and fixed something on a day nobody opened a session. Scored on evidence (artifacts with timestamps, heartbeat logs), not on the theoretical capability.

**Level-4 proof artifact:** A documented absence fire drill: the period, what ran, what queued, what broke, and the state the operator returned to.

**Why this weight:** The strongest single test of the whole architecture: it requires deep memory, judgment about authority boundaries, and self-maintenance at once. A bare model cannot survive one hour of absence. Daily operation makes this the capability whose absence is felt first.

### O8. External actuation

*Weight 3 · grammar `default` · cost tier medium · origin function*

Can the system act on the world beyond its own files (send, publish, deploy, book, buy) through permission gates that distinguish reversible from irreversible actions?

**In plain terms:** Whether the system can act on the outside world: send, publish, deploy, book, buy. A system that only reads and drafts leaves the last mile to the operator every time. This criterion deliberately sits in tension with governance (O9, D6): a system may score modestly here by design because its operator wants every outbound action gated. That is what a declared target with a design-conflict reason is for.

**Level-4 proof artifact:** The gate definitions as code or configuration, plus logs of gated actions including at least one correctly blocked attempt.

**Why this weight:** Modern harnesses already provide tool use; the architecture's delta is the gate discipline, not the reach. Ungated reach is a liability, so the criterion measures the gates.

### O9. Escalation judgment

*Weight 4 · grammar `default` · cost tier medium · origin function*

Does the system know when to stop and ask: does it distinguish what it may decide from what belongs to the operator, and does it hold that line under pressure to be helpful?

**In plain terms:** Whether the system knows what it may do alone and what needs the operator, and whether that boundary is real. Passing means codified authority lanes (act freely; act and flag; hard stop and ask) with the hard-stop lane enforced in code rather than left to the model's judgment in the moment. The failure modes on both sides are costly: a system that asks about everything is a tool, and a system that asks about nothing is a liability.

**Level-4 proof artifact:** An escalation log showing correct stops at the authority boundary, and no boundary crossings, over a sustained period.

**Why this weight:** Autonomy without a stopping rule is a hazard, not a capability. The bare model has no standing authority model of one specific operator to stop against; the architecture supplies it.

### O10. Commitment tracking

*Weight 5 · grammar `default` · cost tier medium · origin practice+research · sub-group: unprompted*

Does the system surface the operator's own promises and commitments unprompted: overdue items raised at the right moment, not stored in a list nobody reopens?

**In plain terms:** Promises are the highest-stakes facts an operator generates. This criterion asks whether commitments (to clients, colleagues, themselves) are tracked with owner and deadline, and whether the system follows through unprompted: surfacing the overdue, flagging the at-risk before the deadline rather than after. Capturing commitments into a list nobody re-reads scores low; a scheduled check that raises flags scores high.

**Level-4 proof artifact:** Instances of unprompted surfacing traced from the original commitment to the surfaced reminder to the outcome.

**Why this weight:** Remembering what the operator promised and raising it unasked is pure architecture: a bare model does not know a promise was made, and a list the operator must reopen is the operator working, not the system.

### O11. Drift and opportunity surfacing

*Weight 4 · grammar `default` · cost tier high · origin practice+research · sub-group: unprompted*

Does the system notice, unprompted, when reality diverges from the operator's stated goals (output drifting off positioning, a client's world changing, an opening worth acting on) and raise it?

**In plain terms:** Whether the system notices things the operator did not ask about: relevant developments in their field, drift in the system's own output, an opportunity matching their goals. Passing requires unprompted delivery with artifacts (a daily or weekly scan that lands on its own schedule), not the ability to research when asked. This is the watchtower function: its value is precisely that nobody had to remember to ask.

**Level-4 proof artifact:** Logged unprompted interventions of this kind with what triggered each and what happened next.

**Why this weight:** Requires holding the operator's goals as standing state and comparing the world against them continuously. Entirely architecture; weighted one below commitment tracking because judging drift is fuzzier than a dated promise and misfires cost attention.

### O12. Goal grip

*Weight 5 · grammar `default` · cost tier medium · origin practice+research · sub-group: unprompted*

Does the system argue back with standing: cite the operator's own recorded goals and decisions against a current instruction that contradicts them? Is the grip strength operator-configurable, and is there an intervention log with outcomes?

**In plain terms:** Whether the system holds the operator's goals firmly or just displays them. A dashboard that shows the goal of the quarter while every session drifts to whatever came up scores low. Grip means the stated goal actually structures behavior: sessions open oriented to it, unrelated requests get gently flagged as off-goal, and the firmness is calibrated per goal (some goals warrant a hard pull back, others a light note). This criterion was born from observing that nobody has built calibrated grip, which is itself informative.

**Level-4 proof artifact:** The grip configuration, plus an intervention log showing pushbacks, the operator's rulings, and the hit rate.

**Why this weight:** A bare model bends toward whatever the current prompt wants; holding yesterday's stated goal against today's impulse requires durable goals and licensed disagreement, both pure architecture. Precision without pushback is the failure daily operation exposes: a system that executes the request and loses the goal.

### O13. Initiative precision

*Weight 4 · grammar `measured` · cost tier medium · origin function · sub-group: unprompted*

Of everything the system raises unprompted, how much deserved the operator's attention? Is the signal-to-noise of initiative measured, so unprompted work earns trust instead of becoming spam?

**In plain terms:** The quality control on initiative. A system that acts unprompted (O10, O11, O12) can be a partner or a nuisance, and the difference is measurable: of the unprompted actions and suggestions, what fraction does the operator accept? Passing means the acceptance rate is actually tracked and the system adapts (fewer, better interventions over time). An unmeasured initiative stream that feels noisy scores low no matter how sophisticated the triggers are.

**Level-4 proof artifact:** A measured acceptance rate for unprompted interventions, tracked over time.

**Why this weight:** Unprompted capabilities are only as valuable as their precision; a noisy system trains the operator to ignore it, silently zeroing O10 through O12. This criterion makes the sub-group falsifiable.

### O14. Autonomy horizon

*Weight 4 · grammar `measured` · cost tier high · origin adversarial:measured-autonomy*

When the operator is away, how long does the system keep producing usable output before a human is needed? Is that horizon measured and tracked, rather than assumed?

**In plain terms:** O5, O6 and O7 ask whether work happens without the operator. None of them asks for how long. A system that runs unattended for twenty minutes and a system that runs unattended for three weeks both satisfy "acts in absence", and the distance between them is most of the distance in this category. This criterion asks for the number: the longest unattended period whose output was still usable without intervention, established by observation rather than by intention. Passing means the horizon is a tracked number with a threshold, and a regression in it gets noticed.

**Level-4 proof artifact:** A stated horizon with its method (the longest unattended period whose output was accepted without intervention), at least two dated measurements, and a threshold that triggers investigation when the horizon shortens.

**Why this weight:** The axis this field is currently racing on, and the one where claims inflate fastest, because "runs autonomously" is said identically by a system that survives an hour and one that survives a month. A bare model's horizon is a single turn, so everything above that is the architecture's contribution. Held below O7's weight because a measured horizon presumes the absence capability O7 already scores.

## Tier: Dependability

Whether the output can be trusted without watching the machinery produce it. The word carries its engineering sense: service delivery that is justifiably trusted, which makes self-monitoring, self-repair, integrity, verification, control, cost transparency and evidence all part of one property. Everything here is the system directed at itself. A bare model has no machinery to maintain; every criterion here exists because the architecture does.

| ID | Criterion | Weight | Grammar | Cost | Origin |
|----|-----------|--------|---------|------|--------|
| D1 | Self-monitoring | 5 | default | medium | function |
| D2 | Self-repair within safe bounds | 4 | default | medium | function |
| D3 | Backup and tested restore | 5 | default | low | function |
| D4 | Memory accuracy audit | 4 | measured | medium | function |
| D5 | Output verification | 4 | default | medium | function |
| D6 | Enforced versus advisory rules | 4 | default | low | adversarial:hooks-not-prompts |
| D8 | Vendor-change resilience (owns) | 4 | default | high | practice+research |
| D10 | Behavior control | 3 | default | medium | practice+research |
| D11 | Assembly transparency | 4 | default | medium | practice+research |
| D12 | Cost observability and control | 3 | default | low | adversarial:predictable-cost |
| D13 | Tests on the system itself | 4 | default | medium | adversarial:tested-harness |

### D1. Self-monitoring

*Weight 5 · grammar `default` · cost tier medium · origin function*

Does the system know when its own machinery fails? Are silent failures (a routine that stopped firing, a pipeline producing empty output) detected by the system rather than discovered by the operator?

**In plain terms:** Whether the system knows when it is broken. Passing means the system checks its own pulse on a schedule: routine failure rates, dead jobs, silent-failure canaries, with findings surfaced where the operator will actually see them. The alternative is discovering that a pipeline died three weeks ago only when its absence finally hurts. Monitoring that itself dies silently fails the criterion; that is what canaries are for.

**Level-4 proof artifact:** Monitoring configuration plus at least one real incident where the system detected its own failure before the operator did.

**Why this weight:** An unmonitored factory degrades invisibly and spends the operator's trust without their knowledge. Installed is not the same as working; only the system itself can watch at the required frequency.

### D2. Self-repair within safe bounds

*Weight 4 · grammar `default` · cost tier medium · origin function*

When the system detects a fault, can it fix the safe and reversible subset itself, and does it correctly route the dangerous subset to the operator instead of attempting it?

**In plain terms:** One step past monitoring: when the check finds a safe, reversible problem (a stuck queue, a stale cache, a missed run), does the system fix it and leave an artifact trail, or file a ticket for the operator? The boundary matters: self-repair should cover the routine and reversible, and escalate the risky. A system that repairs nothing burdens the operator; one that repairs beyond its authority is a hazard.

**Level-4 proof artifact:** A remediation log showing automatic fixes applied, each within a declared safe-action boundary, and dangerous cases escalated.

**Why this weight:** Detection without repair still consumes the operator's time for every fault. The delta is bounded autonomy over the system's own health; one below monitoring because repair without detection is impossible.

### D3. Backup and tested restore

*Weight 5 · grammar `default` · cost tier low · origin function*

Is the system's state (memory, configuration, code) versioned and backed up automatically, and has restore actually been tested rather than assumed?

**In plain terms:** The criterion is deliberately named "backup and tested restore" because the second half is where systems fail. Copies that have never been restored are hope, not backup. Passing means backups exist, run automatically, and a restore has actually been rehearsed end to end (fresh folder, recover everything, verify it works), with the rehearsal repeated on a schedule. The gap between "we have backups" and "we have restored from backups" is where data loss lives.

**Level-4 proof artifact:** Backup configuration plus a documented restore drill with its outcome.

**Why this weight:** The system's accumulated memory is the one component that cannot be re-derived at any price; years of context can vanish in one disk failure. The drill is weighted with the backup because the recovery path is the half that fails in practice.

### D4. Memory accuracy audit

*Weight 4 · grammar `measured` · cost tier medium · origin function*

Is the stored memory sampled against reality on a schedule, with an error rate stated and tracked? Not "is the store organized" but "is it actually correct".

**In plain terms:** Memory is only an asset if it is true. This criterion asks whether stored claims are systematically audited against reality: a sampled fact-check on a schedule (pull twenty stored facts, verify each, score the store), with wrong facts corrected through the M9 machinery. Without it, confidence in memory rests on the assumption that nothing captured was wrong and nothing true went stale, and both assumptions are false at any real corpus size.

**Level-4 proof artifact:** Audit method, sample results, and an error-rate number tracked across audits.

**Why this weight:** A confidently wrong memory is the known failure mode of every system in this category. The audit is what keeps the Memory tier honest: with no sampled error rate, every score in that tier measures the shape of the store rather than its truth.

### D5. Output verification

*Weight 4 · grammar `default` · cost tier medium · origin function*

Does the system verify its own work products against defined acceptance criteria before delivery (facts checked, links opened, renders viewed), or does the operator carry the full checking burden?

**In plain terms:** Whether work products pass through gates before they reach the operator or the world. Examples: a design QA script on every rendered deliverable, a test suite on every code change, a voice check on every draft leaving in the operator's name. The criterion distinguishes systems that verify outputs from systems that emit them; at volume, unverified output quietly transfers the review burden back to the operator.

**Level-4 proof artifact:** Gate definitions per output type plus logs showing outputs blocked or corrected by the gates.

**Why this weight:** If the operator must re-check everything, the system saves production time and spends it back in review. Self-verification is what converts output volume into trusted output.

### D6. Enforced versus advisory rules

*Weight 4 · grammar `default` · cost tier low · origin adversarial:hooks-not-prompts*

Of the rules the system claims to follow, how many are blocked in code (hooks, gates, permissions) versus requested in prose the model may ignore? Is the enforced set identified and deliberate?

**In plain terms:** The load-bearing distinction of the whole tier: is a rule enforced in code, or written in prose and left to the model's judgment? "Never commit secrets" in an instruction file is advisory; a pre-commit hook that blocks the commit is enforced. Advisory rules fail exactly when it matters: long sessions, degraded attention, adversarial input. Count the rules that would survive the model having a bad day; those are the enforced ones.

**Level-4 proof artifact:** An inventory mapping each claimed rule to its enforcement mechanism, plus a negative test showing an enforced rule actually blocking.

**Why this weight:** Instructions in context are suggestions, not configuration; every system in this category markets rules, and they diverge exactly here. The architecture's delta is turning stated policy into physics.

### D8. Vendor-change resilience

*Weight 4 · grammar `default` · cost tier high · origin practice+research · sub-group: owns*

Does the system survive changes it does not control: a model swap, a harness update, a provider policy change? Is portability to another runtime demonstrated rather than presumed from open formats?

**In plain terms:** Every personal AGI runs on someone else's model and runtime, and upstream changes without asking. This criterion asks what happens then: is there a fallback runtime, are the data and skill layers portable enough to migrate, has any of this been tried? A system whose memory is plain files (M10) has the raw material for resilience, but untested portability is a plan, not a capability. Deep single-vendor integration may be the right trade; this criterion prices it.

**Level-4 proof artifact:** A documented swap or upgrade drill: the change, what broke, time to recover, and the system running on the alternative.

**Why this weight:** The system's foundation is rented from a vendor who may change it any day, and a single upstream change can idle the whole factory. Resilience here is the difference between an outage and an ending. Origin includes a real near-loss from an upstream harness change.

### D10. Behavior control

*Weight 3 · grammar `default` · cost tier medium · origin practice+research*

Can the operator control the model's character, not just its knowledge: damp trained tendencies like flattery and agreement-seeking, and verify with tests that the control actually holds?

**In plain terms:** A model arrives with a trained character: it agrees readily, flatters, and softens bad news. Those tendencies are invisible in a demo and expensive over months, because a system that tells the operator what they want to hear corrupts every judgment built on its output. This criterion asks whether the operator can damp them, and what proves the damping holds. Passing means behavioral tests: scripted scenarios that invite the tendency (a weak plan presented confidently, a wrong claim asserted as fact) scored on whether the system pushed back, re-run after every model or harness update. Prose rules plus good intentions score low because nothing detects drift between the rulebook and actual behavior.

**Level-4 proof artifact:** The control mechanism plus behavioral test results demonstrating the damped tendency, re-run after model or harness updates.

**Why this weight:** Vendors tune character globally; the operator inherits it. The architecture can only partially counteract training, so the delta is real but bounded, and it must be verified to exist at all.

### D11. Assembly transparency

*Weight 4 · grammar `default` · cost tier medium · origin practice+research*

Can the operator lift the hood on any answer: see what was loaded, what fired, what was retrieved, what was on and off when the answer was produced?

**In plain terms:** When the system answers, what went into the answer? Assembly transparency means the operator can lift the hood on a given response: which memory files loaded, which skills fired, which rules were in force. This is the anti-black-box criterion: without it, debugging a bad answer means guessing, and trusting a good one means faith. Silent retrieval pipelines that inject unlogged context are the failure mode.

**Level-4 proof artifact:** A per-answer trace (context manifest, retrieval log, active-component list) a stranger could follow.

**Why this weight:** Without visibility into what assembled an answer, the operator cannot debug wrong answers, audit privacy, or calibrate trust; every other trust criterion becomes unverifiable folklore. A bare chat has almost nothing to hide; the architecture does.

### D12. Cost observability and control

*Weight 3 · grammar `default` · cost tier low · origin adversarial:predictable-cost*

Is spend visible and steerable: cost per routine and per delivered artifact known, idle cost known, expensive jobs flagged before they run, budgets enforced rather than discovered on the bill?

**In plain terms:** Whether the operator knows what the system costs, before the invoice. Passing means spend is visible at useful granularity (per day, per routine, per heavy job), with thresholds that alert on anomalies rather than relying on the operator to notice. An autonomous system without cost observability has an unbounded budget by default; this criterion prices metered-API architectures honestly against flat-fee ones.

**Level-4 proof artifact:** Cost telemetry per routine and artifact, plus a budget mechanism shown intercepting an over-budget run.

**Why this weight:** An unaffordable factory shuts down regardless of quality, but cost control is survival infrastructure rather than capability. Mid-weight: its absence kills slowly, its presence adds nothing to output.

### D13. Tests on the system itself

*Weight 4 · grammar `default` · cost tier medium · origin adversarial:tested-harness*

Is the machinery regression-tested: do the hooks, routines, retrieval and gates have a test suite that runs on change and on schedule, or is only the output ever judged?

**In plain terms:** The system itself is software: skills, hooks, schedulers, config. This criterion asks whether that layer is tested like software: a test suite that gates changes to skills and hooks, scheduled checks that config matches reality (every scheduled job exists, every referenced file is present). Without it, the system's own plumbing is the least-tested code the operator depends on daily.

**Level-4 proof artifact:** A test suite covering the system's own mechanisms, in continuous integration or a scheduled run, with its pass history.

**Why this weight:** A system that changes weekly without tests is betting the factory on every edit. Tests are what let the system evolve without silently breaking; they are the enforcement layer of trustworthiness itself.

## Tier: Compounding

Whether the system gets better from what it accumulates, and can prove it: day 300 better than day 30, on auditable evidence. The tier is named for the mechanic it demands: gains building on prior gains rather than accruing in a straight line. It is the category most systems claim and almost none can demonstrate; the evidence grammar exists because the claim is cheap and the proof is not.

| ID | Criterion | Weight | Grammar | Cost | Origin |
|----|-----------|--------|---------|------|--------|
| C1 | Corrections become behavior | 5 | evidence | medium | function |
| C2 | Learned-pattern promotion | 4 | evidence | medium | adversarial:confidence-scored-instincts |
| C3 | Memory accretion pays off | 4 | measured | high | function |
| C4 | Longitudinal capability benchmark | 5 | measured | high | function |
| C5 | Self-directed improvement | 4 | evidence | high | function |
| C6 | Error recurrence declines | 4 | measured | medium | function |

### C1. Corrections become behavior

*Weight 5 · grammar `evidence` · cost tier medium · origin function*

When the operator corrects the system, does the correction become a durable behavior change: encoded, applied in future sessions, and demonstrably not repeated?

**In plain terms:** The base loop of compounding: when the operator corrects the system, the correction must become durable behavior, encoded where future sessions will hit it, and demonstrably not repeated. The test is longitudinal: take a correction from months ago and check whether the old mistake still occurs. A system that receives the same correction three times is not learning; it is being operated.

**Level-4 proof artifact:** A corrections ledger tracing individual corrections to their encoded form and to later sessions where the old behavior would have occurred and did not, with recurrence measured over time.

**Why this weight:** A bare model resets to factory behavior every session; the operator pays for each mistake exactly once only if the architecture makes it so. This is the atomic unit of compounding: without it, every other improvement mechanism leaks.

### C2. Learned-pattern promotion

*Weight 4 · grammar `evidence` · cost tier medium · origin adversarial:confidence-scored-instincts*

Does the system extract patterns from its own activity and promote them into durable capability (skills, instincts, defaults) with confidence tracking, so repeated work becomes encoded work?

**In plain terms:** Whether the system notices its own repetition and promotes it into capability. When the same multi-step workflow gets performed by hand for the third time, a compounding system extracts it into a named skill, with confidence tracking so promotion is earned rather than premature. Hand-authoring skills is the manual version and scores in the middle; the criterion points at the pipeline where repeated work becomes encoded work with decreasing operator involvement.

**Level-4 proof artifact:** A promotion trail: recurring activity, the pattern extracted from it, its confidence record, and the promoted skill in later use.

**Why this weight:** Corrections capture what went wrong; pattern promotion captures what went right. It converts operating history into capability without the operator authoring anything, which no bare model can accumulate.

### C3. Memory accretion pays off

*Weight 4 · grammar `measured` · cost tier high · origin function*

Do answers get better as memory grows, demonstrably? The antithesis of context rot: is there evidence that more accumulated memory improved output quality rather than degrading it?

**In plain terms:** The counterweight to context rot. The industry's default experience is that more accumulated context makes models worse: noisier retrieval, staler facts, longer prompts. A compounding system claims the opposite, and this criterion demands evidence: any measurement showing answers improved as the store grew (the same question answered better with memory than without, quality tracked as the corpus doubled). Growth in file count is not the claim; growth in usefulness is.

**Level-4 proof artifact:** The same task class evaluated at two corpus sizes or dates, showing quality rising with accumulation, method stated.

**Why this weight:** Accumulation is the system's core bet and it is not free: unmanaged growth degrades models. Proving the bet pays is what separates a compounding system from a hoarding one.

### C4. Longitudinal capability benchmark

*Weight 5 · grammar `measured` · cost tier high · origin function*

Is there a fixed benchmark run over the system's lifetime: the same task set executed at intervals, showing day 300 beating day 30 on defined measures?

**In plain terms:** The tier's headline claim, measured the only honest way: a fixed benchmark run over the system's lifetime. Freeze a set of representative tasks, execute it at intervals on defined measures (quality, speed, how much operator intervention was needed), and see whether day 300 beats day 30. Without this, "the system gets better over time" is a feeling, and feelings about one's own system are systematically optimistic.

**Level-4 proof artifact:** The benchmark definition, at least two dated runs, and the score trend.

**Why this weight:** Every other criterion in this tier shows a mechanism; this one shows the curve, which is what makes the tier's claim falsifiable rather than merely argued.

### C5. Self-directed improvement

*Weight 4 · grammar `evidence` · cost tier high · origin function*

Does the system propose and execute improvements to itself from its own telemetry (failure patterns, cost data, usage analytics), through the same safety gates as any other change?

**In plain terms:** Whether improvement itself is becoming autonomous. The system watches its own telemetry (failure patterns, cost data, which skills go unused) and proposes or executes improvements, through the same safety gates as any other change. The gates are the point: self-modification without change control is how systems rot; with it, maintenance becomes another scheduled routine instead of the operator's weekend project.

**Level-4 proof artifact:** An improvement backlog generated by the system from its own telemetry, with executed items and their measured effect.

**Why this weight:** The closure of the loop: the factory maintaining itself is Dependability; the factory upgrading itself is Compounding. Requires telemetry, judgment and gates working together, all architecture.

### C6. Error recurrence declines

*Weight 4 · grammar `measured` · cost tier medium · origin function*

Is the rate of repeated mistakes tracked, and is it falling? Not "are errors logged" but "does the same class of error happen less over time", as a number.

**In plain terms:** The negative-space measurement of learning: is the rate of repeated mistakes falling? Passing requires an error taxonomy (classes of mistake, not individual incidents), recurrence counts per class, and a visible trend. Logging errors is not the criterion; the criterion is the number that shows the same class of error happening less this quarter than last. A flat or rising recurrence curve falsifies the compounding claim no matter how sophisticated the learning machinery looks.

**Level-4 proof artifact:** An error taxonomy with recurrence counts across periods, showing the trend.

**Why this weight:** The negative image of the benchmark: improvement must show up as fewer repeated failures, or the learning mechanisms are decorative. Recurrence is the honest metric because it cannot be gamed by adding features.

---

Author and maintainer: Dana Maman ([saltedmind.co](https://saltedmind.co)).
See [README.md](README.md) for scope,
[CONTRIBUTING.md](CONTRIBUTING.md) for how to submit an assessment or dispute
a criterion, [ASSESS.md](ASSESS.md) for the machine-runnable assessment
protocol, and [LIMITS.md](LIMITS.md) for the structural limits of this
instrument.

Licensed under [CC BY 4.0](LICENSE).
