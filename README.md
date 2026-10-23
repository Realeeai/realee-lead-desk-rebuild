# Realee Lead Desk: the rebuild

Clief Notes Weekly Comp #15, "The Rebuild". This is our Comp #14 entry, [realee-lead-desk-control](https://github.com/Realeeai/realee-lead-desk-control) (3rd of 11), rebuilt from the judge's feedback and tested old against new.

**Headline** ([`results.md`](results.md)): the rebuild matches the operator's blind calls on 10 of 12 leads, against the original's 9, in both runs, using about half the input. The only tier that changed is the one rule he changed. What didn't improve:
- the two calls where he kept his rule on purpose;
- one score line in 24 that the rebuild left out;
- speed, which is the same.

The rebuild was first made in the Control repo, as our follow-up to the Comp #14 feedback, before Comp #15 was posted. This repo re-creates it in Comp #15's order and re-runs both arms.

## What's here

| Path | What it is |
|------|------------|
| [`feedback.md`](feedback.md) | The judge's feedback file for our Comp #14 entry, word for word |
| [`questions.md`](questions.md) | Five questions, one for each line of the feedback that asked for a change, with expected answers, plus the twelve leads with the operator's blind calls. Committed before `rebuild/` existed |
| [`original/`](original/) | The judged folder, byte for byte from the Control repo at `a887b92`, the last commit before the deadline. Read only |
| [`run-original/`](run-original/) | Two raw runs of the original on the twelve leads |
| [`rebuild/`](rebuild/) | The folder after the feedback: `rules.md`, the intake script and a README |
| [`run-rebuild/`](run-rebuild/) | Two raw runs of the rebuild, same leads, same order |
| [`results.md`](results.md) | Question by question, with what tied, what got worse and what we left alone |
| [`harness/`](harness/) | `run_arms.py` runs one arm; `grade.py` grades a run against `questions.md` |

**Why `rebuild/` has two files, not five.** Our own test showed that `identity.md`, `examples.md` and `reference/` (apart from the intake script) did nothing: across Haiku, Sonnet and Opus 5.5 at every effort level, the full folder never beat `rules.md` alone, and on Haiku it did worse. So we removed them. The evidence is in the Control repo's `results.md`.

## Re-run both arms

Needs Python 3.10+ and [Claude Code](https://docs.claude.com/en/docs/claude-code) on your PATH, logged in.

```bash
python harness/run_arms.py original 3
python harness/run_arms.py rebuild 3
python harness/grade.py run run-original/run-3
python harness/grade.py run run-rebuild/run-3
```

Use any run number that doesn't exist yet. The runner never overwrites a run. Both arms use the same model (`claude-opus-5-5`), effort (`high`), prompt, lead order and wrapper, with one fresh session per lead and no tools. The only difference is the folder. `--model` and `--effort` run any other setting.

## License

MIT
