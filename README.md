# IF Halal

IF Halal Meat — order form plus a customer support agent.

## Customer support agent

Open `CustomerSupportAgent.html` in a browser. No build step.

The page is a working desk for IF Halal:

- **Customer chat** — tracks seeded orders (`IF-1042`, `IF-1038`, `IF-1029`, `IF-1015`), quotes cuts, cites zabiha / delivery / refund policy, and escalates when it should not guess.
- **Staff desk** — email-style queue with AI drafts, confidence, sources, send / wait / escalate / resolve.
- **Knowledge** — the only policy the agent is allowed to speak from.
- **Evals** — 10 launch-gate scenarios (intent, required facts, escalation). Ship bar is 10/10.

Demo data lives in `localStorage` (`if-support-v1`). Use **Reset demo data** to restore the seed tickets.

## Order form

`HalalMeatOrder.html` is the original order form stub.
