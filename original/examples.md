# examples.md — Realee Lead Desk

Every SCORE line below adds up. `harness/grade.py examples` (at the repo root) re-adds each one against the weights in `rules.md` and fails by name if a total, an option's points or a tier drifts.

---

## Example 1 — HOT (pasted website form, two answers missing)

**Input:**

```text
Source: website form
Name: Sarah Chen
Role: VP Operations
Company: FleetRoute (logistics SaaS, ~200 employees per LinkedIn)
Message: "We're manually onboarding enterprise customers between Salesforce and NetSuite. It's breaking every quarter. We have budget approved to fix it this quarter. Can we talk?"
```

**Output:**

- **TIER:** HOT
- **SCORE:** P4(+20) + B?3(+12) + S4(+16) + A?3(+9) + R5(+10) + T4(+8) = 75/100
- **RULES:** 5a, 6a, 7a
- **ASK NEXT:** how many people would feel the difference; budget range (approved, amount not given)
- **NEXT ACTION:** Book discovery within 48h — send cal link today; ask team size and budget range on the call.
- **ARTIFACT:**

```text
[Lead Alert] HOT: Sarah Chen @ FleetRoute
Score 75/100 — VP Ops, ~200 people, manual Salesforce↔NetSuite onboarding that breaks every quarter, budget approved this quarter.
Ask on the call: how many people it affects, and the budget range.
Draft: "Sarah — manual onboarding between Salesforce and NetSuite is exactly what we build for. 15 min this week? [cal link]"
```

---

## Example 2 — DISQUALIFY (selling to us, scored first)

**Input:**

```text
LinkedIn DM: "Hi! I run a 12-person SEO agency. We'd love to help Realee rank for AI automation searches. Can I send over a proposal?"
```

**Output:**

- **TIER:** DISQUALIFY
- **SCORE:** P1(+5) + B?3(+12) + S2(+8) + A?3(+9) + R5(+10) + T?3(+6) = 50/100
- **RULES:** 3a, 6e, 7a
- **ASK NEXT:** not needed (pass)
- **NEXT ACTION:** Polite pass, no nurture.
- **ARTIFACT:**

```text
[Lead Alert] DISQUALIFY: unnamed @ 12-person SEO agency
Scored 50/100, then passed under 3a: they're offering their services to Realee, not asking for anything solved.
Pass: "Thanks for reaching out. We're not looking for SEO help right now, but best of luck."
```

---

## Example 3 — WARM (category evaluation, nothing broken named)

**Input:**

```text
Email reply to cold outreach
Name: James Ortiz
Role: Director RevOps
Company: ClearPath HR (~90 employees)
"We're looking at workflow automation vendors. Not urgent — probably evaluate over the next couple months."
```

**Output:**

- **TIER:** WARM
- **SCORE:** P2(+10) + B?3(+12) + S3(+12) + A?3(+9) + R4(+8) + T4(+8) = 59/100
- **RULES:** 5b, 6b, 7a
- **ASK NEXT:** what's breaking that they want automated; how many people would feel the difference; budget range
- **NEXT ACTION:** Nurture — send a case study in 3 days and ask what's breaking today.
- **ARTIFACT:**

```text
[Lead Alert] WARM: James Ortiz @ ClearPath HR
Score 59/100 — Director RevOps, ~90 people, evaluating automation vendors (a category, nothing broken named), next couple of months.
Action: nurture; no Matt calendar yet. Ask what's breaking, team size and budget range.
Suggested line: "James — happy to be on your list. Which handoff costs your team the most today? I'll send an example that matches."
```

---

## Example 4 — FLAG (two answers, too little to score)

**Input:**

```text
Referral from client: "Talk to Maria at Apex Industrial — she runs ops and hates their manual quoting process. Very interested."
```

**Output:**

- **TIER:** FLAG
- **SCORE:** P4(+20) + B?3(+12) + S?3(+12) + A?3(+9) + R4(+8) + T?3(+6) = 67/100 (provisional: only 2 of 6 answered)
- **RULES:** 4a, 6d, 7a
- **ASK NEXT:** company size; how many people would feel the difference; timeline; budget range
- **NEXT ACTION:** Ask the referrer for an intro, then run the intake questions before tiering.
- **ARTIFACT:**

```text
[Lead Alert] FLAG: Maria @ Apex Industrial
Provisional 67/100 — runs ops, named problem (manual quoting). Only 2 of 6 questions answered, so not tiered yet.
Ask: company size, how many people it affects, timeline, budget range.
```

---

## Example 5 — WARM (full intake chat, every question answered)

**Input:**

```text
Source: website chat
Q1 Name and email: Tom Becker, tom@lumacare-example.com
Q2 What would you like solved? "Our marketing team and leadership keep miscommunicating. Priorities change in meetings and nobody writes them down, so campaigns get redone."
   Follow-up, cost: "Probably two or three campaigns a quarter get scrapped and rebuilt."
Q3 Role: "Marketing manager."
Q4 Company and size: "LumaCare, a consumer skincare brand. About 120 people."
Q5 People affected: "The 8 of us in marketing, plus 3 people in leadership."
Q6 Timeline: "In about four months, before our spring launch."
Q7 Budget: "$5–15k."
```

**Output:**

- **TIER:** WARM
- **SCORE:** P5(+25) + B2(+8) + S3(+12) + A3(+9) + R3(+6) + T3(+6) = 66/100
- **RULES:** 5b, 6b, 7a
- **ASK NEXT:** nothing, all answered
- **NEXT ACTION:** Nurture — send a decision-log example in 3 days; offer a call when the budget firms up.
- **ARTIFACT:**

```text
[Lead Alert] WARM: Tom Becker @ LumaCare
Score 66/100 — marketing manager, ~120-person consumer brand, 11 people affected. Decisions made in meetings aren't written down, so 2–3 campaigns a quarter get rebuilt. About four months out, $5–15k.
Action: nurture with a decision-log example.
Suggested line: "Tom — lost meeting decisions are fixable, and two or three rebuilt campaigns a quarter is the cost worth killing. Here's how one team captured decisions automatically."
```
