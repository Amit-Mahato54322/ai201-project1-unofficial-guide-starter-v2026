# Milestone 4 — answer and refusal checks

One development pass, not the three-run unit 2 evaluation. Corpus: campus_life; top-k: 5; cutoff: 0.64.

Produced by `app.py::ask_pipeline`; answer generation via `generate.py::answer_from_chunks`.

The Aldridge answer and its complete prompt are recorded separately in `milestone4_sample_answer.txt` (one real call, 583 tokens). The four other covered questions below used caching disabled (four real calls, 2,205 tokens).

## How are juniors and seniors ordered in the housing lottery before random tie-breaking?

- Best distance: 0.214776
- Refused: False
- Model calls: 1

```text
Juniors and seniors are ordered by accumulated credit hours first in the housing lottery before random tie-breaking. 

Source: admin_housing_lottery.txt
```

## How many days into the semester can I change my meal plan, and where does a downgrade refund go?

- Best distance: 0.176299
- Refused: False
- Model calls: 1

```text
You can change your meal plan tier once in the first ten days of the semester. A downgrade refunds the difference to your student account. 

Source: admin_meal_plan_changes.txt
```

## When does the library close during reading week compared with term time?

- Best distance: 0.448550
- Refused: False
- Model calls: 1

```text
During reading week, the library is open until 10pm, whereas during term time it is open until 2am. (Source: `study_library_hours.txt`)
```

## What minimum grade earns a pass under the pass/fail option?

- Best distance: 0.329099
- Refused: False
- Model calls: 1

```text
A grade of C- or better is needed to earn a pass under the pass/fail option (admin_pass_fail_option.txt).
```

## What is the capital of Mongolia?

- Best distance: 0.824593
- Refused: True
- Model calls: 0

```text
I don't have enough information about that.
```

## How do I change the oil in a diesel engine?

- Best distance: 0.923117
- Refused: True
- Model calls: 0

```text
I don't have enough information about that.
```

## Who won the 1994 World Cup?

- Best distance: 0.885860
- Refused: True
- Model calls: 0

```text
I don't have enough information about that.
```

## What is the recommended dosage of ibuprofen for a headache?

- Best distance: 0.844232
- Refused: True
- Model calls: 0

```text
I don't have enough information about that.
```

## How do I write a for loop in Rust?

- Best distance: 0.890692
- Refused: True
- Model calls: 0

```text
I don't have enough information about that.
```

## Manual review

All five covered answers name the correct source in the answer itself and contain every required fact in criterion 5: credit-hour priority; $1.75/card only; ten days/student account; 10pm versus 2am; C- or better. No unsupported claim was observed in these five answers. All five unrelated questions returned the exact refusal with zero additional model calls. This single pass does not replace the repeated unit 2 evaluation.
