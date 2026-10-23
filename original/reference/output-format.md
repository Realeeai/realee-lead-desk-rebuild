# Output format

Every run returns this block (markdown):

```text
---
TIER: [HOT|WARM|COLD|DISQUALIFY|FLAG]
SCORE: P?(+?) + B?(+?) + S?(+?) + A?(+?) + R?(+?) + T?(+?) = [total]/100
RULES: [rule IDs that decided the tier, e.g. 5a, or 3a, or 4a]
ASK NEXT: [each unanswered question, in script order; one that could move the tier goes first, marked "(decides the tier)"; or "nothing, all answered"]
NEXT ACTION: [one line]
---

LEAD: {Name} | {Company} | {Role}
SOURCE: {if known}
PROBLEM: {1-2 sentences, in their words where possible}

RATIONALE: {which option each factor got, and why}

--- DRAFT ALERT ---
Subject: [Lead Alert] {TIER}: {Name} from {Company}

{2-4 sentences for Matt or hello@realee.ai}

Suggested line to lead (HOT/WARM only):
"{paste-ready reply}"

FLAG tier: list the questions to ask in the draft body.

DISQUALIFY tier: include polite pass wording in the draft body.
```

## The SCORE line (show the addition)

All six factors, always in the order P, B, S, A, R, T. Each term is the factor's letter, the option (1–5), and its points (option × weight from `rules.md`) in brackets. An unanswered factor gets a `?` before its option and scores option 3.

| Case | SCORE line |
|------|------------|
| All answered | `SCORE: P5(+25) + B4(+16) + S3(+12) + A3(+9) + R5(+10) + T4(+8) = 80/100` |
| Some unanswered | `SCORE: P4(+20) + B?3(+12) + S4(+16) + A?3(+9) + R5(+10) + T4(+8) = 75/100` |
| DISQUALIFY (still scored) | `SCORE: P4(+20) + B?3(+12) + S2(+8) + A?3(+9) + R2(+4) + T?3(+6) = 59/100`, with RULES: 3a |

The total must equal the sum of the terms written. If it doesn't, the run is wrong, whatever the tier.

## Sheet row (optional paste to CRM/Sheets)

| Field | Value |
|-------|-------|
| Name | |
| Email | |
| Company | |
| Role | |
| Source | |
| Score | |
| Tier | |
| Problem | |
| Ask next | |
