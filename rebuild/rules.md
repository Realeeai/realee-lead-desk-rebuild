# rules.md — Realee Lead Desk

The desk works in two steps, and they never mix:

1. **Ask.** The intake script (`reference/intake-script.md`) asks every question, in order, whatever the answers. Nothing is judged and nothing is stopped while the questions are being asked.
2. **Score.** After the last answer, or when the desk is handed a finished conversation or a pasted lead, it scores all six factors, then decides the tier. If someone stopped partway, whatever they answered is still scored and passed on.

**This is the only file with numbers.** Weights, scales and tier cut-offs live here and nowhere else.

---

## 1. Six factors, each on a 5-option scale

Place each answer on its factor's scale, option 1 to 5. **Points = option × weight.** The weights add up to 20, so the most a lead can score is 100.

| ID | Factor | Weight | Max |
|----|--------|--------|-----|
| **P** | Problem: what they want solved | 5 | 25 |
| **B** | Budget | 4 | 20 |
| **S** | Company size | 4 | 20 |
| **A** | People affected | 3 | 15 |
| **R** | Role | 2 | 10 |
| **T** | Timeline | 2 | 10 |

The problem weighs most, because the problem is what Realee solves. Budget and company size come next, and larger is better on both.

| Option | P — Problem | B — Budget | S — Company size | A — People affected | R — Role | T — Timeline |
|---|---|---|---|---|---|---|
| **1** | Nothing specific: curious, "what can AI do for us" | Under $5k | 1–9 people | 1–2 people | No business role (student, job seeker) | None, or a year or more |
| **2** | A general area or category, nothing broken named ("evaluating automation platforms") | $5k to under $15k | 10–49 | 3–9 | Individual contributor, coordinator | 6–12 months |
| **3** | A real problem in general terms ("intake is slow and things slip", "marketing and leadership keep miscommunicating") | $15k to under $30k | 50–199 | 10–24 | Manager, team lead | 3–6 months |
| **4** | A specific broken step, handoff or manual task, or a specific thing they want built | $30k to under $70k | 200–999 | 25–99 | Director, head of a function | 1–3 months |
| **5** | Specific, and they say what it costs them now: hours, people, money, errors, lost deals | $70k or more | 1,000 or more | 100 or more | VP, C-suite, founder, owner | Under a month, or "now" |

Industry and company type are not factors. A consumer brand, an agency or a marketing team scores on the same six questions as anyone else.

---

## 2. Unanswered questions

- **An unanswered question scores option 3, the middle.** A missing answer neither sinks a lead nor lifts it. Mark it with `?` in the SCORE line (`B?3(+12)`) and put the question under ASK NEXT.
- **"Budget approved" with no amount** is unanswered for B: option 3, and the range goes under ASK NEXT.
- **A range that spans two options** (for example "11-50 people") counts as the higher option. Put the exact figure under ASK NEXT; if the lower option would change the tier, it goes first, marked "(decides the tier)".
- **Every output lists ASK NEXT:** each question the lead hasn't answered, in script order, or "nothing, all answered".

---

## 3. Passes (3a–3b), decided after scoring

After scoring, check in this order: passes (§3), then FLAG (§4), then the score (§5). The first one that applies sets the tier.

Only two things end in **DISQUALIFY**, and only after the lead has been scored. The score is still shown.

| ID | Pass when what they said shows… |
|----|------|
| **3a** | They're selling to Realee: a vendor, agency, contractor, recruiter or competitor offering their services |
| **3b** | A student or learner asking for themselves, with no business behind it (homework, a capstone, "teach me AI") |

Nothing else is a pass. Industry, company type and wanting an app built never are.

---

## 4. FLAG (4a)

**4a.** If the problem (P) is unanswered, or fewer than three of the six questions are answered, there's too little to score → **FLAG**. Ask every unanswered question before tiering.

**FLAG means 4a and nothing else.** A scored lead is never held back for one missing answer, whatever FLAG is taken to mean elsewhere. When a single unanswered question could move the score across a tier line, the lead still gets the tier its score gives. That question goes **first** under ASK NEXT, marked "(decides the tier)", and is asked straight away: on the booked call for HOT, in the first nurture message for WARM. That's how the desk asks the deciding question first without stopping the lead.

---

## 5. Tiers (5a–5c)

If no pass and no FLAG, the score decides:

| ID | Score | Tier |
|----|-------|------|
| **5a** | 70–100 | **HOT** |
| **5b** | 50–69 | **WARM** |
| **5c** | 0–49 | **COLD** |

A lead that's average on every question (option 3 across the board) scores 60, the middle of WARM. HOT means above average overall; COLD means below.

**Show the addition.** The SCORE line lists all six factors in the order P, B, S, A, R, T, each with its option and points, then the total:
`SCORE: P4(+20) + B?3(+12) + S4(+16) + A2(+6) + R5(+10) + T4(+8) = 72/100`. The total must equal the sum of the terms written.

---

## 6. Next action (6a–6e)

| Tier | ID | Next action |
|------|-----|-------------|
| HOT | **6a** | Book discovery within 48h, and ask anything in ASK NEXT on the call |
| WARM | **6b** | Nurture: send a value asset in 3 days, and ask what's in ASK NEXT |
| COLD | **6c** | Park, with a monthly check-in, and ask what's in ASK NEXT if they reply |
| FLAG | **6d** | Ask every question in ASK NEXT, then score again |
| DISQUALIFY | **6e** | Polite pass, no nurture |

---

## 7. Draft artifact (7a)

Always end with a short internal alert for Matt, for every tier:

| Tier | Draft content |
|------|----------------|
| HOT / WARM | Full alert + suggested reply line to the lead |
| COLD | Internal alert; no suggested reply line |
| FLAG | Alert + the questions to ask |
| DISQUALIFY | Internal alert + polite pass wording |
