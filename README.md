# The Unofficial Guide

Amit Mahato · Corpus: `campus_life`

Repository: https://github.com/Amit-Mahato54322/ai201-project1-unofficial-guide-starter-v2026

Run instructions are in [RUNNING.md](RUNNING.md). Acceptance criteria and their
pre-test targets are in [criteria.md](criteria.md).

---

# Unit 1

## What This Does

This project answers questions using 88 fictional campus-life posts supplied
with the course, covering housing, dining, classes, administrative rules, and
student services. It keeps titled paragraphs together, embeds them locally,
and retrieves five relevant chunks for questions such as how much Aldridge
laundry costs or when the library closes during reading week. A cosine-distance
gate refuses questions without a sufficiently close match before making a
Gemini call. Accepted questions receive a brief answer grounded in the retrieved
posts and naming its source file.

## Chunking Strategy

**Chunk size:** 400 characters as a soft target, including the title.
**Overlap:** 0 body characters; repeat the source title on each chunk.

Decision recorded before implementation: the `campus_life` documents are short
posts with a title followed by one or more paragraphs. A housing post separates
its description, good points, bad points, and laundry/noise details into
paragraphs; its title is needed to tell which building those details describe.
A 400-character target keeps the short administrative posts together while
allowing longer housing posts to separate at paragraph boundaries.

The chunker will pack whole paragraphs up to this target and repeat the title
when it starts a new chunk. It will keep an oversized paragraph intact rather
than split a sentence just to satisfy the size target. Body overlap is zero
because whole paragraphs already preserve the sentence context; title repetition
provides the building/course name without duplicating unrelated body text.
`fallback_split` remains available for comparison.

The real baseline index produced 88 chunks from 88 documents, averaging 317
characters (shortest 178, longest 549). The replacement produces 100 chunks,
averaging 282 characters (shortest 116, longest 400). The shortest new chunk is
a whole paragraph with its title, not a trailing character fragment. All source
body paragraphs are preserved once, in order; no source sentences are cut.
The baseline is retained as index variant `milestone2-baseline`.

## Sample Chunks

Printed by `python app.py --corpus campus_life chunks -n 5`.

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```text
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_cs_210.txt#0` — produced by: `chunker.py::split_documents`

```text
CS 210 Data Structures

I'm a junior and I've done this twice now. Format is lecture with weekly labs; slides go up after class, not before. Assessment: two midterms and a final, all drawn from lecture material rather than the textbook. Midterms are curved, the final is not.

Expect 8 to 10 hours a week outside class.
```

**Chunk 3** — source: `course_math_220_workload.txt#0` — produced by: `chunker.py::split_documents`

```text
Workload for MATH 220 Linear Algebra

People keep asking so: 6 to 8 hours a week, almost all of it on problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_the_ridgeway_cafe_followup.txt#0` — produced by: `chunker.py::split_documents`

```text
Re: The Ridgeway Café

Adding to what people have said about The Ridgeway Café. The wait figure of 10 to 15 minutes at 12:30 matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: seating is tight; about 40 seats for a building of 900. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_morrow_house.txt#0` — produced by: `chunker.py::split_documents`

```text
Morrow House — what it's actually like

Just finished a year in this building. Built 1954, partially renovated 2008. Rooms are singles and doubles, hall bathrooms.

The good: cheapest housing tier by about $900 a year, and the singles are real singles.

The bad: known damp problem on the ground floor; two rooms were taken offline in 2024.
```

All five retain their source title and complete body sentences. The first
three can independently answer: “When can I drop a course without a W?”,
“Are CS 210 midterms and the final curved?”, and “How much weekly work does
MATH 220 take?” The fourth answers when the café has its stated lunch queue;
the fifth answers how much cheaper Morrow House is and what its damp problem is.
The Morrow laundry paragraph is a separate titled chunk, so this sample does
not claim to answer a laundry question.

## Sample Answer

**Question:** How much does one wash cost in Aldridge Hall, and what payment
method do the machines accept?

**Answer (actual CLI output):**

```text
One wash in Aldridge Hall costs $1.75, and the machines accept card only (housing_aldridge_hall_laundry.txt).

Sources retrieved: housing_aldridge_hall_laundry.txt, housing_calder_annexe.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt
```

Produced by `app.py::ask_pipeline` and `generate.py::answer_from_chunks` using
`gemini-3.5-flash-lite`. The real call used 551 input tokens and 32 output
tokens. The full grounding instruction, assembled prompt, answer, and source
line are saved in [the CLI transcript](results/milestone4_sample_answer.txt).

**My relevance cutoff:** `0.64` (cosine distance; lower is closer).

| Question | In corpus? | Best distance |
|---|---|---|
| How are juniors and seniors ordered in the housing lottery before random tie-breaking? | Yes | 0.214776 |
| How much does one wash cost in Aldridge Hall, and what payment method do the machines accept? | Yes | 0.276681 |
| How many days into the semester can I change my meal plan, and where does a downgrade refund go? | Yes | 0.176299 |
| When does the library close during reading week compared with term time? | Yes | 0.448550 |
| What minimum grade earns a pass under the pass/fail option? | Yes | 0.329099 |
| What is the capital of Mongolia? | No | 0.824593 |
| How do I change the oil in a diesel engine? | No | 0.923117 |
| Who won the 1994 World Cup? | No | 0.885860 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.844232 |
| How do I write a for loop in Rust? | No | 0.890692 |

The covered questions span 0.176299–0.448550; unrelated questions span
0.824593–0.923117. The midpoint between the largest covered distance and
smallest unrelated distance is about 0.637, so 0.64 leaves space on both sides.
On these ten questions it passes all five covered questions and refuses all
five unrelated ones. This calibration sample cannot establish performance on
new questions: a relevant paraphrase above 0.64 would be refused, and an
unsupported question below 0.64 could reach generation. The gate uses a strict
less-than comparison, so a distance exactly equal to 0.64 is refused.

**Retrieval review and top-k:** I kept `TOP_K = 5`. The first result for each
of the five questions contains the required facts. Reading all five results
for the first three questions also exposed noise: the housing-lottery query
retrieves an Atrium dining post, and the Aldridge query retrieves laundry rules
for other buildings. Those matches share broad topic words but do not answer
the exact question. Keeping five preserves context for other questions; it does
not mean all five results are equally relevant. The frozen criterion explicitly
measures the top five. Full distances and the first three sets of chunk texts
are in [the retrieval record](results/milestone4_retrieval.md), with all ten sets
of full chunks in [the raw data](results/milestone4_retrieval.json).

**Grounding review:** The existing instruction requires only provided evidence,
a refusal when evidence is missing, and a source filename. In the sample above,
the model correctly selected Aldridge's $1.75/card-only rule despite receiving
other buildings' prices and payment methods. It did not import their rules.
The existing instruction was retained. Four additional real answers also
matched their required facts and named the correct source; no drift requiring
a prompt change was observed in this development pass. The “Sources retrieved” line lists available
context, whereas the filename in the answer identifies the source actually used.

**Refusal check:** All five unrelated questions returned exactly
“I don't have enough information about that.” with zero additional model calls.
The four additional covered answers and all five refusal outputs are saved in
[the answer-check record](results/milestone4_answer_checks.md). This is one
milestone 4 development pass, not the three-run unit 2 evaluation.

## How I Used AI

**1.** I asked AI to replace the fixed-window chunker with one suited to the
campus-life posts. It implemented paragraph-based chunks with a 400-character
soft target, repeated titles, and no body overlap. I haven’t made further
changes to that implementation.

**2.** I asked AI to measure retrieval distances and tune the relevance cutoff.
It measured five covered and five unrelated questions, then changed the cutoff
from 0.6 to 0.64. I haven’t adjusted that cutoff further.

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

Evaluation file: [Saved before evaluation](results/run_2026-09-23_1942_before.md).

The evaluation asked all five questions three times with response caching
disabled. There is no scorer.py, so the saved answers were reviewed manually
against criteria.md.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunks contain the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Sample chunks preserve context and complete sentences | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Answers preserve exact facts and conditions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

For criterion 1, the saved retrieval passages contain the required facts
for all five questions. The evaluation records the same retrieved source
sets and matching best distances across all three runs. Passage evidence
comes from [the earlier retrieval record](results/milestone4_retrieval.json);
the evaluation itself records source names and distances, not passage text.
This assessment reuses that saved retrieval evidence for the same corpus,
default index, and top-k of 5.

For criterion 2, all fifteen generated answers name a retrieved source
filename inside the answer itself.

For criterion 3, the evaluation refused all five out-of-scope questions.
This deterministic check ran once, so its count is repeated across the
three columns. Earlier pipeline checks also recorded the exact refusal
text and zero model calls; that additional evidence is identified below.

For criterion 4, all five saved samples in the Unit 1 Sample Chunks
section retain their titles and complete body sentences. This reuses the
single deterministic chunk review, repeated across the three columns,
not three new chunk measurements.

For criterion 5, all five answers in each run include the required facts:
credit-hour priority; $1.75 and card-only payment; ten days and a refund
to the student account; 10pm during reading week versus 2am during term;
and C- or better. No conflicting or unsupported claim was found when
comparing the answers with the saved retrieved passages.

Although the scores are identical, the answer wording varies between
runs. run_eval.py::run_once explicitly passes cache=False to generation.

### Criterion 1 — actual retrieved text

Evidence file: results/milestone4_retrieval.md.
Retrieved by store.py::search; chunk produced by
chunker.py::split_documents.

Source: admin_meal_plan_changes.txt#0

```text
On the meal plan changes

You can change your meal plan tier once, in the first ten days of the semester. After that it's locked. Downgrading refunds the difference to your student account; upgrading bills you immediately.
```

### Criterion 2 — actual answer naming a source

Evidence file: results/run_2026-09-23_1942_before.md, Aldridge question,
Run 1. Produced by generate.py::answer_from_chunks and recorded by
run_eval.py::write_report.

```text
One wash in Aldridge Hall costs $1.75, and the machines accept card only.

Source: housing_aldridge_hall_laundry.txt
```

### Criterion 3 — actual gate results

Evidence file: results/run_2026-09-23_1942_before.md.
Produced by run_eval.py::check_out_of_scope using gate.py::check.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.923 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.891 | refused |

Additional saved pipeline evidence from
results/milestone4_answer_checks.md, produced by app.py::ask_pipeline:

Question: What is the capital of Mongolia?

- Best distance: 0.824593
- Refused: True
- Model calls: 0

```text
I don't have enough information about that.
```

### Criterion 4 — actual sample chunk

Evidence: the Unit 1 Sample Chunks section of this README.
Produced by chunker.py::split_documents and printed by app.py::cmd_chunks.

Source: course_cs_210.txt#0

```text
CS 210 Data Structures

I'm a junior and I've done this twice now. Format is lecture with weekly labs; slides go up after class, not before. Assessment: two midterms and a final, all drawn from lecture material rather than the textbook. Midterms are curved, the final is not.

Expect 8 to 10 hours a week outside class.
```

### Criterion 5 — actual answer preserving the required facts

Evidence file: results/run_2026-09-23_1942_before.md, library question,
Run 1. Produced by generate.py::answer_from_chunks and recorded by
run_eval.py::write_report.

```text
During reading week, the library is open until 10pm, whereas during term time it is open until 2am. (Source: `study_library_hours.txt`)
```

## Verdicts

The original targets in criteria.md are unchanged. A criterion must meet its
target in every generated-answer run, not just on average.

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET | All five questions have a sufficient chunk in the saved top-five retrieval evidence, exceeding 4/5; all three evaluation runs record matching source sets and best distances. |
| 2 | Every answer names a source | MET | Each of the five answers in each of the three runs names a retrieved filename inside its answer, meeting 5/5 every time. |
| 3 | Gate stops out-of-corpus questions | MET | The deterministic gate pass refused 5/5 against a 4/5 target; the earlier pipeline evidence confirms the exact refusal and zero calls for all five. |
| 4 | Sample chunks preserve context and complete sentences | MET | All five saved sample chunks retain the source title and complete body sentences, exceeding 4/5; this deterministic check is measured once. |
| 5 | Answers preserve exact facts and conditions | MET | All fifteen answers contain every required fact from the reference rows, with no conflicting or unsupported additions, exceeding 4/5 in each run. |

**Challenge to these verdicts:** The strongest argument against MET is about
measurement coverage, not a failing answer: the before evaluation did not save
chunk text, and its out-of-scope loop checked gate decisions without recording
actual pipeline refusal strings or call counts. Criteria 1, 3, and 4 therefore
also rely on the explicitly linked earlier evidence. Matching retrieval
settings, source sets, and distances support that comparison, but do not make
those earlier records new measurements. The after evaluation will capture fresh
retrieval text, sample chunks, and pipeline refusals to make its evidence direct.
No original target is lowered or revised.

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
