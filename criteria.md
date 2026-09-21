# Acceptance criteria — The Unofficial Guide

Corpus: `campus_life`. These targets and the five question/`expects` pairs in
`questions.py` are fixed before milestone 3 chunking and milestone 4 retrieval
measurements. The phrases are useful scoring hints; they are not sufficient on
their own to establish that a complete answer is correct.

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions in `questions.py`, the top 5 retrieved
chunks include at least one chunk containing the facts needed to answer every
part of the question.

**Why this target:** The meal-plan, laundry, and library questions each require
keeping two related facts together, while several campus posts repeat similar
language about different buildings. Four of five allows one retrieval miss but
still requires success on most of these paired-fact questions; three would
leave too much of this small test set unanswered.

## 2. Every answer names a source

For all 5 test questions in `questions.py`, the answer text names at least one
retrieved source filename; a separate “Sources retrieved” line does not count,
and a refusal counts as a miss for these in-corpus questions.

**Why this target:** Every retrieved chunk already carries its filename, and
the generation instruction asks the model to name it, so there is no missing
metadata that would justify accepting four citations out of five. Requiring
all five makes unsupported-looking answers visible even when their facts sound
plausible.

## 3. The relevance gate stops out-of-corpus questions

For at least 4 of the 5 questions in `OUT_OF_SCOPE`, the relevance gate stops
generation and returns exactly “I don't have enough information about that.”
without making a model call.

**Why this target:** The five prompts concern unrelated subjects such as engine
maintenance and world sports, rather than campus life, so most should be easy
to reject. Four of five tolerates one accidental semantic match without
accepting a gate that routinely passes unrelated questions; distance overlap
has not yet been measured.

## 4. Sample chunks preserve context and complete sentences

At least 4 of the 5 chunks printed by `python app.py chunks -n 5` include their
source document's title and at least one complete body sentence, with no body
sentence cut off at either boundary.

**Why this target:** Campus posts often name the building or course only in the
title, and a laundry price or opening time without that name is ambiguous.
Four of five requires context-preserving boundaries in most of the sample,
while allowing one unusual source format rather than assuming all short posts
are perfectly structured.

## 5. Answers preserve exact facts and conditions

At least 4 of the 5 answers to `questions.py` correctly include every fact in
the corresponding reference row below, without adding a conflicting number,
condition, or claim not supported by the retrieved text. A refusal counts as
a miss.

| Question topic | Required facts | Reference document |
|---|---|---|
| Housing lottery | Juniors and seniors are ordered by accumulated credit hours before random tie-breaking. | `admin_housing_lottery.txt` |
| Aldridge wash | One wash costs $1.75; payment is card only. | `housing_aldridge_hall_laundry.txt` |
| Meal-plan change | The window is the first ten days of the semester; a downgrade refund goes to the student account. | `admin_meal_plan_changes.txt` |
| Library closing | Reading week closes at 10pm; term time closes at 2am. | `study_library_hours.txt` |
| Pass/fail grade | A pass requires C- or better. | `admin_pass_fail_option.txt` |

**Why this target:** A fluent answer that swaps term-time and reading-week hours
or omits card-only payment can send a student to the wrong place at the wrong
time. Four complete, accurate answers out of five is more demanding than merely
matching an `expects` phrase, while allowing one generation failure to diagnose
in unit 2.

## Self-check before testing

The assignment's separately named self-check was not supplied in the repository.
The following checks use the requirements in the milestone: a defined sample,
a count or observable outcome, a reason for the target, and a test another
reader can perform. No retrieval or generated-answer results were used to set
these targets.

For each criterion, this is exactly how to test the sentence as written:

1. Retrieve the top five chunks for each question. Read the chunks against all
   parts of that question and count questions with one sufficient chunk. Pass
   at four or five.
2. Read each of the five answer texts and compare filenames in the text with
   that question's retrieved filenames. Count refusals and answers with no
   matching filename as misses. Pass only at five.
3. Send each of the five `OUT_OF_SCOPE` questions through the pipeline. Record
   the gate decision, exact returned text, and change in model-call count. Count
   cases with a refusal, the specified text, and zero additional calls. Pass
   at four or five.
4. Print the specified five chunks and compare each with its source file.
   Count chunks containing the title and a complete body sentence, without a
   truncated boundary sentence. Pass at four or five.
5. Compare each answer with its reference row and retrieved text. Count it only
   if it includes every required fact and no unsupported or conflicting claim.
   Pass at four or five.

## Unit 2 preservation rule

Keep these original criteria and reasons visible. If a criterion cannot be
measured reliably, add a dated revision and explain the measurement problem
underneath it. Do not lower a target because a run missed it. For criteria
measured over three runs, the target must hold in every run; the deterministic
chunk and gate checks need only one pass.
