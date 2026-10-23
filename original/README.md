# Realee Lead Desk

A portable folder operator for Claude Projects, or for any chat or voice agent. First entered in Clief Notes Comp #8 (The Wildcard); revised for Comp #14 (The Control). The repo root explains the Comp #14 test.

**It asks every inbound lead the same questions, then scores the answers: a tier, a score out of 100 with the addition shown, what's still unanswered, a next action and a draft alert.**

Built for founders and small teams selling to businesses who waste afternoons re-qualifying the same inbound shapes, and who never want to lose a lead because it didn't answer everything.

## How it works

1. **Ask.** `reference/intake-script.md` is the script: seven questions, asked in order, every time. Nothing is judged or stopped while asking.
2. **Score.** After the last answer, `rules.md` places each answer on a 5-option scale: problem, budget, company size, people affected, role and timeline. Each factor has a weight. Unanswered questions score the middle option and are listed under ASK NEXT, so a missing answer never sinks a lead.
3. **Decide.** Only two things are passes: people selling to you, and students with no business behind them. Industry never is. Everything else is HOT, WARM or COLD by score, or FLAG when too little was answered to score.

Methodology: [Interpretable Context Methodology](https://arxiv.org/html/2603.16021v2) — folder structure as agent architecture.

## How to use

1. Drop this folder into a Claude Project (**Project knowledge → upload the files**), or give the intake script to your chat or voice agent.
2. To fit it to your offer, edit **`rules.md`**. It's the only file with numbers: weights, the 5-option scales, tier cut-offs.
3. Run the script with a lead, or paste in a finished conversation or any inbound message.
4. Expect: **TIER**, **SCORE** (the addition written out, out of 100), **RULES**, **ASK NEXT**, **NEXT ACTION**, **DRAFT ALERT**.

## Try in 60 seconds

Paste these three. Each should land on a **different tier**:

1. `VP Ops, 180-employee logistics SaaS, "we're drowning in manual onboarding between Salesforce and NetSuite, budget approved this quarter"` → **HOT** (71/100)
2. `Founder, 12-person agency, "curious about AI, no timeline"` → **COLD** (46/100)
3. `Director RevOps, 90 employees, "evaluating workflow automation, call in 2 weeks"` → **WARM** (61/100)

## Folder map

| File | Job |
|------|-----|
| `identity.md` | Who Lead Desk is, its five outcomes, and what it refuses |
| `rules.md` | Weights, the 5-option scales, passes, FLAG and tiers. **The only file with numbers** |
| `examples.md` | Five worked leads; every SCORE line adds up |
| `reference/intake-script.md` | The questions, in order, for chat or voice |
| `reference/icp.md` | Who Realee sells to, in words |
| `reference/output-format.md` | The output block and the SCORE line format |

## License

MIT — use, fork, adapt the rubric for your offer.
