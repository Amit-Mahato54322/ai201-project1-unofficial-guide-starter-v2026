# Milestone 4 — real retrieval evidence

Corpus: `campus_life`; default index; `all-MiniLM-L6-v2` ONNX embeddings; cosine distance; top-k 5.

Produced by `store.py::search`. No generation calls were made for this measurement.

## How are juniors and seniors ordered in the housing lottery before random tie-breaking?

In corpus: True. Best distance: 0.214776.

- `admin_housing_lottery.txt#0` — distance 0.214776
- `advising_registration.txt#0` — distance 0.672237
- `dining_the_atrium_followup.txt#0` — distance 0.737577
- `admin_parking_permits.txt#0` — distance 0.748727
- `housing_innisfree_hall.txt#0` — distance 0.756084

### admin_housing_lottery.txt#0 (0.214776)

```text
On the housing lottery

The housing lottery is not random in the way most people assume. Rising sophomores get a number drawn at random, but juniors and seniors are ordered by accumulated credit hours first, and only tie-break randomly. That means a senior who took summer courses reliably beats a senior who didn't. Numbers come out the second week of March and selection runs over four evenings.
```

### advising_registration.txt#0 (0.672237)

```text
Registration and your adviser

You need an adviser hold lifted before you can register, and advisers get busy in the week before registration opens. Book two weeks out.

Registration times are staggered by credit hours, same as the housing lottery. Popular courses fill in the first two days.
```

### dining_the_atrium_followup.txt#0 (0.737577)

```text
Re: The Atrium

Adding to what people have said about The Atrium. The wait figure of no queue matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: picked clean by 1:15 and not restocked again until the next morning. Nobody tells you this at orientation.
```

### admin_parking_permits.txt#0 (0.748727)

```text
On the parking permits

Student permits for the west lots go on sale in August and sell out in about three days. The east lot never sells out because it's a 12-minute walk. There is no waitlist — people who miss the window park on Verrill Street and walk in, which is legal but unmarked and confuses everyone.
```

### housing_innisfree_hall.txt#0 (0.756084)

```text
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.
```

## How much does one wash cost in Aldridge Hall, and what payment method do the machines accept?

In corpus: True. Best distance: 0.276681.

- `housing_aldridge_hall_laundry.txt#0` — distance 0.276681
- `housing_old_brewhouse_laundry.txt#0` — distance 0.402055
- `housing_innisfree_hall_laundry.txt#0` — distance 0.408649
- `housing_calder_annexe.txt#1` — distance 0.419475
- `housing_old_brewhouse.txt#1` — distance 0.424287

### housing_aldridge_hall_laundry.txt#0 (0.276681)

```text
Laundry in Aldridge Hall

Machines take $1.75 wash, $1.50 dry, card only. There are eight washers and six dryers for the building, which is the wrong ratio and means the dryers back up on Sunday evenings.

Best time to do laundry here is Tuesday or Wednesday morning. Sunday after 6pm you will wait.
```

### housing_old_brewhouse_laundry.txt#0 (0.402055)

```text
Laundry in Old Brewhouse

Machines take $1.50 wash, $1.50 dry, coin only, and the machines are old. There are eight washers and six dryers for the building, which is the wrong ratio and means the dryers back up on Sunday evenings.

Best time to do laundry here is Tuesday or Wednesday morning. Sunday after 6pm you will wait.
```

### housing_innisfree_hall_laundry.txt#0 (0.408649)

```text
Laundry in Innisfree Hall

Machines take $1.75 wash, $1.75 dry, app-based. There are eight washers and six dryers for the building, which is the wrong ratio and means the dryers back up on Sunday evenings.

Best time to do laundry here is Tuesday or Wednesday morning. Sunday after 6pm you will wait.
```

### housing_calder_annexe.txt#1 (0.419475)

```text
Calder Annexe — what it's actually like

Laundry costs $2.00 wash, $1.75 dry, app-based. On noise: depends entirely on your cluster; there's no building-wide pattern.
```

### housing_old_brewhouse.txt#1 (0.424287)

```text
Old Brewhouse — what it's actually like

Laundry costs $1.50 wash, $1.50 dry, coin only, and the machines are old. On noise: sound carries strangely because of the original brick; a room two floors up can be louder than next door.
```

## How many days into the semester can I change my meal plan, and where does a downgrade refund go?

In corpus: True. Best distance: 0.176299.

- `admin_meal_plan_changes.txt#0` — distance 0.176299
- `admin_dining_dollars.txt#0` — distance 0.570392
- `admin_add_drop_deadline.txt#0` — distance 0.600385
- `admin_withdrawal_deadline.txt#0` — distance 0.621493
- `money_jobs.txt#0` — distance 0.638143

### admin_meal_plan_changes.txt#0 (0.176299)

```text
On the meal plan changes

You can change your meal plan tier once, in the first ten days of the semester. After that it's locked. Downgrading refunds the difference to your student account; upgrading bills you immediately.
```

### admin_dining_dollars.txt#0 (0.570392)

```text
On the dining dollars

Declining balance — what everyone calls dining dollars — rolls over from the autumn semester to the spring, but not from spring to the following autumn. Whatever is left in May disappears.
```

### admin_add_drop_deadline.txt#0 (0.600385)

```text
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

### admin_withdrawal_deadline.txt#0 (0.621493)

```text
On the withdrawal deadline

Withdrawal is a different thing from dropping and has a different date. Dropping ends at week six. Withdrawal runs to week ten, requires an adviser signature, and puts a W on the transcript that doesn't affect GPA. The two dates appear on different pages of the registrar's site and this catches people every year.
```

### money_jobs.txt#0 (0.638143)

```text
On-campus work

Library and dining jobs post in the first week of each semester and go fast. Pay is the same across departments — the difference is whether you can study during the shift. Library desk: usually yes. Dining: no.

Maximum is 20 hours a week during term. Most people find 10 to 12 is the point where it stops affecting coursework.
```

## When does the library close during reading week compared with term time?

In corpus: True. Best distance: 0.448550.

- `study_library_hours.txt#0` — distance 0.448550
- `housing_calder_annexe_noise.txt#0` — distance 0.484335
- `admin_library_holds.txt#0` — distance 0.489289
- `housing_morrow_house_noise.txt#0` — distance 0.493941
- `course_hist_118_workload.txt#0` — distance 0.537286

## What minimum grade earns a pass under the pass/fail option?

In corpus: True. Best distance: 0.329099.

- `admin_pass_fail_option.txt#0` — distance 0.329099
- `course_stat_150_exams.txt#0` — distance 0.587735
- `admin_graduation_requirements.txt#0` — distance 0.633880
- `course_stat_150.txt#1` — distance 0.678196
- `admin_grade_appeals.txt#0` — distance 0.679545

## What is the capital of Mongolia?

In corpus: False. Best distance: 0.824593.

- `course_hist_118_exams.txt#0` — distance 0.824593
- `course_hist_118.txt#0` — distance 0.869272
- `housing_morrow_house.txt#0` — distance 0.873895
- `housing_morrow_house_laundry.txt#0` — distance 0.910530
- `housing_calder_annexe.txt#0` — distance 0.917836

## How do I change the oil in a diesel engine?

In corpus: False. Best distance: 0.923117.

- `dining_verrill_street_grill.txt#1` — distance 0.923117
- `course_stat_150.txt#1` — distance 0.933539
- `admin_meal_plan_changes.txt#0` — distance 0.934011
- `course_engl_205.txt#1` — distance 0.938279
- `course_econ_101_exams.txt#0` — distance 0.947412

## Who won the 1994 World Cup?

In corpus: False. Best distance: 0.885860.

- `course_hist_118_exams.txt#0` — distance 0.885860
- `course_hist_118.txt#0` — distance 0.937370
- `course_engl_205.txt#1` — distance 0.942967
- `housing_innisfree_hall.txt#0` — distance 0.943701
- `admin_study_abroad.txt#0` — distance 0.947474

## What is the recommended dosage of ibuprofen for a headache?

In corpus: False. Best distance: 0.844232.

- `money_textbooks.txt#0` — distance 0.844232
- `course_hist_118.txt#0` — distance 0.860232
- `course_econ_101.txt#0` — distance 0.864023
- `course_cs_340_exams.txt#0` — distance 0.865958
- `dining_the_ridgeway_cafe.txt#0` — distance 0.870754

## How do I write a for loop in Rust?

In corpus: False. Best distance: 0.890692.

- `course_engl_205.txt#0` — distance 0.890692
- `course_hist_118_exams.txt#0` — distance 0.895998
- `course_engl_205_exams.txt#0` — distance 0.905611
- `course_hist_118.txt#0` — distance 0.914244
- `housing_calder_annexe_laundry.txt#0` — distance 0.917800

## Interpretation and cutoff decision

The first hit for each covered question contains its required facts. For the
first three questions, the full chunk review above shows that lower-ranked
hits sometimes share only a broad topic: the Atrium post does not explain the
housing lottery, and other buildings' laundry rules do not answer the Aldridge
question. Top-k remains 5; the answer must still select the correct named source.

Covered range: 0.176299–0.448550. Unrelated range: 0.824593–0.923117.
Gap midpoint: approximately 0.637. Selected threshold: 0.64. This separates the
ten calibration questions, but does not establish accuracy on unseen questions.
