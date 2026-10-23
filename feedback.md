# Comp #14 — The Control · feedback for Matt H

**Entry 03 — `03-matt-h-realee-lead-desk-control`** · https://github.com/Realeeai/realee-lead-desk-control
**Placed:** 3rd of 11
**Judged by:** David

> **Why you placed where you did.** You let the control rewrite your rules, published that three of your folder's four wins were rules you did not want, and reported the folder slower on every question. Rare, and hard to do.

Scores are not published — placement and reasoning are. Everything below was written by
your judge with your repo open, after they pinned it to the last commit before the 13 Oct
deadline and re-ran your arms themselves. It is their words, unedited.

---

**The read.** I re-ran both arms cold on `claude-opus-5-5` from your committed prompts and
system files and got 7/9 and 9/9 — your numbers, the same two questions (Q3 and Q5), and every
one of the folder's SCORE totals identical to your runs 9 and 10. That is the cleanest
reproduction in my pile — and the two questions that decide it reproduced again on a second rep,
same tier, same SCORE line, digit for digit. Then I ran the arm your repo doesn't have:
`rules.md` pasted alone, no `identity.md`, no `examples.md`, no `reference/`. It ties your folder
9/9, matches its SCORE line term for term on nine of ten leads including mine, and costs a third
of the input tokens. The finding I keep coming back to is still the one you led with — rewriting
the rules from the transcripts moved the bare model from 4/9 to 7/9 without re-running it — but
the rules-only arm says where your folder's margin comes from: the policy being written down.

**What worked.** `results.md`, "What we changed in the folder because of it", read against
`git log`. Four rounds, each with the commit that made the change and the question that caused
it — and round 2 (`75ab731`) sides with the bare model on Q8 against your own folder.

**Two fixes for this week.**
1. Run the rules-only arm yourself and publish it. 26% of your bundle carries the whole measured
result; that is the sharpest claim in your repo and nobody else this round can make it. Then
ask what `examples.md` and `reference/` have to earn. (Your other open item — re-running the
bare arm against the current rules instead of re-grading it — I ran for you, twice, cold. It
lands on your 7/9 both times.)
2. Get a key you didn't write. Every expected tier traces to `rules.md`, so the test can only
show the folder applies its own rules. Have your operator tier the nine leads blind before
seeing either arm and commit that as a third key; where he and `rules.md` disagree is the
most interesting data in the repo.

**What would have moved you up.** Writing `questions.md` before importing the Comp #8 folder.
As the history stands the folder is in the repo five minutes before the questions and the keys
come out of its rules, so the comparison starts inside the folder's own frame.

**My re-run:** matched exactly, twice on the pivotal questions · **My planted question:** a
60-person agency COO with a named kickoff handoff problem, ~15 hrs/week, $20k, two months →
folder tied on tier and returned my hand-computed 76/100 term for term; so did `rules.md` alone.

---

*Comp #14 panel, 19 Oct 2026. If you think a fact here is wrong — a file your judge missed,
an arm they ran differently — reply in the thread. The judges' full case notes exist and
can be shared with you on request.*
