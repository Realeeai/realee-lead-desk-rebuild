# Results: the original against the rebuild

Both arms ran twice on the twelve leads in [`questions.md`](questions.md), with Claude Opus 5.5 at effort `high`, the setting the Comp #14 entry was judged on. Both runs are graded against the operator's blind key: `python harness/grade.py run run-<arm>/run-<n>`.

## What didn't improve, first

1. **Two of the operator's blind calls are still missed, on purpose.** Q6 is a curious VP with nothing specific in mind: Matt said FLAG, and both arms say WARM. Q8 is "interested. call me." with no name: he said DISQUALIFY, and both arms say FLAG. When he saw where his calls and his rules disagreed, he kept both rules. On Q6, both answers ask what's broken first, so only the label differs. On Q8, the desk is built never to lose a lead over a missing answer. So 10 of 12 is the most any desk that follows his rules can score on his key.
2. **The score line got slightly worse.** The original wrote a SCORE line that adds up on 24 of 24 answers, the rebuild on 23 of 24. The miss was Q8 in rebuild run 1: the lead with nothing to score came back FLAG with no SCORE line. That's likely because the rebuild has no worked examples or output format. The tier was right both times.
3. **It isn't faster.** Both arms take about 22 seconds per answer.
4. **The rebuild already existed before Comp #15 was posted.** We built it as our follow-up to the Comp #14 feedback, on 2026-10-22 and 23, in [realee-lead-desk-control](https://github.com/Realeeai/realee-lead-desk-control), before we'd seen this comp. The order there was still questions first: the blind key was pushed at 12:52:45 UTC on 10-22, before any change to the folder. This repo rebuilds that work in Comp #15's layout and re-runs both arms here. So these runs aren't blind to the outcome: every expected answer in `questions.md` was predicted from the earlier runs.

## The five questions

| # | Question (from the feedback) | Expected | Original | Rebuild | Verdict |
|---|---|---|---|---|---|
| 1 | Does a desk with only `rules.md` and the intake script give the same tiers as the full folder? | Same on every lead but O1 | | | **Yes.** The same tier on 11 of 12 leads in all four runs. O1 is the one rule that changed (question 4). |
| 2 | What do the removed files earn? | Half the input, same time; the score line could slip | 122,000 input tokens per twelve leads; 24 of 24 score lines; $0.61–0.75 | 66,000 input tokens (54%); 23 of 24 score lines; $0.54–0.64 | **One score line in 24, for nearly twice the input.** Same time, about 22 s per answer. |
| 3 | How many of the operator's twelve blind calls does each arm match? | Original 9, rebuild 10 | 9 of 12 in both runs | 10 of 12 in both runs | **The rebuild matches him once more:** O1. |
| 4 | Where he and `rules.md` disagreed (Q6, Q8, O1), does each arm land where he then decided? | O1 HOT in the rebuild only; Q6 WARM and Q8 FLAG in both | O1 WARM, Q6 WARM, Q8 FLAG | O1 HOT, Q6 WARM, Q8 FLAG | **Yes**, in all four runs. |
| 5 | Were the questions committed before the folder changed? | Yes | | | **Yes**, see the order below. |

Every lead, every run:

| Lead | Matt's call | Original run 1 | Original run 2 | Rebuild run 1 | Rebuild run 2 |
|---|---|---|---|---|---|
| Q1 | HOT | HOT | HOT | HOT | HOT |
| Q2 | DISQUALIFY | DISQUALIFY | DISQUALIFY | DISQUALIFY | DISQUALIFY |
| Q3 | WARM | WARM | WARM | WARM | WARM |
| Q4 | HOT | HOT | HOT | HOT | HOT |
| Q5 | HOT | HOT | HOT | HOT | HOT |
| Q6 | FLAG | WARM | WARM | WARM | WARM |
| Q7 | DISQUALIFY | DISQUALIFY | DISQUALIFY | DISQUALIFY | DISQUALIFY |
| Q8 | DISQUALIFY | FLAG | FLAG | FLAG | FLAG |
| Q9 | HOT | HOT | HOT | HOT | HOT |
| O1 | HOT | WARM | WARM | **HOT** | **HOT** |
| O2 | HOT | HOT | HOT | HOT | HOT |
| O3 | WARM | WARM | WARM | WARM | WARM |

| Per run, twelve leads | Original run 1 | Original run 2 | Rebuild run 1 | Rebuild run 2 |
|---|---|---|---|---|
| Matt's key | 9 / 12 | 9 / 12 | 10 / 12 | 10 / 12 |
| SCORE lines that add up | 12 / 12 | 12 / 12 | 11 / 12 | 12 / 12 |
| Median seconds per answer | 22.7 | 23.2 | 22.3 | 22.0 |
| Input tokens | 121,934 | 121,952 | 66,064 | 66,050 |
| Output tokens | 27,447 | 26,517 | 24,215 | 23,696 |
| Cost at list price, from the raw JSON | $0.75 | $0.61 | $0.64 | $0.54 |

## The order, from GitHub rather than from us

`gh api repos/Realeeai/realee-lead-desk-rebuild/activity`:

| Pushed (UTC, 2026-10-23) | Commit | What |
|---|---|---|
| 16:07:29 | `12e38ce` | `questions.md` and `feedback.md`. No rebuild in the repo |
| 16:08:32 | `838f8f1` | `original/`, pinned, and the runner |
| 16:20:07 | `c8a3e18` | `run-original/` |
| 16:20:10 | `8df7fa4` | `rebuild/` |
| 16:31:00 | `6fccc1e` | `run-rebuild/` |

In the Control repo, where the rebuild was first made (`gh api repos/Realeeai/realee-lead-desk-control/activity`): the blind key (`e2e2def`) and the rules-only arm were pushed at 12:52:45 UTC on 2026-10-22, before any run graded against the key. The rule change came later (key `b7911d3`, then rule `f7b60f2`), and the trim after that (`afaf097`).

**Checking the pins:** `git rev-parse HEAD:original` gives `7b73dfc…`, the same tree as `a887b92:lead-desk` in the Control repo. `git rev-parse HEAD:rebuild` gives `1bd29d4…`, the same tree as `7fb31ea:lead-desk` there.

## What changed in the rebuild, and why

- **One rule.** A company-size range that spans two options now counts as the higher option, not the lower (`rules.md` §2). Matt's blind call on O1, a freight broker losing 30 hours a week and $4,200 to manual invoice matching, was HOT. The old rule held it at WARM (66). Now it scores 70, HOT, and the exact headcount is the first thing to ask.
- **The trim.** `identity.md`, `examples.md`, `reference/icp.md` and `reference/output-format.md` are gone. Comp #15's template has the rebuild keep the usual five files. We removed four because our own test showed they did nothing. Across Haiku, Sonnet and Opus 5.5 at all five effort levels, the full folder never got a lead right more often than `rules.md` alone, and on Haiku the extra files made it worse: 6 to 10 of 12, against 11 to 12. The whole grid is in the Control repo's `results.md`.
- **One line of wording.** `rules.md` §7 no longer points at the removed output format.
- **Left alone on purpose:** the Q6 and Q8 rules (Matt's call), the six factors, their weights and the tier lines, and the intake script.

## Limits

- One model and setting here: Opus 5.5 at `high`. The other models and effort levels are in the Control repo.
- Twelve leads, two runs per arm.
- Matt's key isn't fully blind. He wrote the rules and had seen earlier answers, and `questions.md` says so.
- The expected answers were predicted from runs we had already done.
- Claude Code adds a short preamble to every call: an Agent SDK line, the date and folder, and the signed-in account's email. No run file contains that email.
