# Plan: passing both FundingPips phases in one month

Added 2026-09-27. Covers (1) further 2026 research on prop-firm evaluations, (2) what a one-month pass of both phases requires, and (3) a plan to improve the existing model toward that goal.

> **Evidence labels** (same as the rest of the dossier):
> - [EX] = search-engine excerpt, since SSRN and most research sites remain blocked for direct reading;
> - [OFF] = a firm's or regulator's own disclosure (read via excerpt);
> - [PRESS] or [PR] = press or practitioner;
> - [SIM] = the synthetic model `model_scripts/one_month_mc.py`, which uses no market data;
> - [D] = derived here.

## 1. Bottom line

1. **Passing both phases (+10%, then +6%) within one month (~21 trading days) is not a realistic plan with the current system.**
   - At today's Sharpe (~1), the model gives **0% at safe risk**. Even at gambling-level risk (2%/day volatility) it gives only **~7%**, and that setting fails the account ~48% of the time [SIM].
   - A coin-flip chance of a one-month pass needs an annual Sharpe of roughly **6–7 at 2%/day volatility**, or **~9 at 1.5%/day** [SIM].
   - That is 2–3× beyond the portfolio Sharpe that plausible, documented edges could reach (§3.3).
2. **The fastest responsible path is to raise the Sharpe first, then size for speed.** With portfolio SR ≈ 2.5 (the brief's target), the model gives:
   - **~4%** within 1 month, **~28%** within 2 months and **~51%** within 3 months at 1.5%/day volatility, with an 87% eventual pass;
   - or a **~95%** eventual pass at 1%/day (median ~90 trading days) [SIM].
3. **If the owner still wants to try for one month,** use an *aggressive first month, then fall back* policy. At SR 2.5, running 2%/day for 21 trading days and then 0.55%/day gives a **~14%** chance of passing in month 1 and keeps a **~92%** eventual pass, against ~100% for the safe policy [SIM].
   - That is a deliberate trade: roughly **+14 pp one-month chance for −8 pp eventual pass**.
   - It is allowed by FundingPips' rules only if trading stays sensible. Avoid anything that looks like "gambling" or "churning and burning" (both are prohibited).
4. **The 2026 research supports this caution.**
   - Firms profit mainly from buyers who take large risk with little edge. Industry data shows ~7% of challenge buyers ever get paid [PRESS].
   - Topstep's own 2025 disclosure: **16.8%** of evaluations passed, but **51.8%** of people passed at least one. **Repeat attempts** matter more than single-attempt speed [OFF].

## 2. More 2026 research on prop-firm evaluations (review)

Adds to `PROP_FIRM_PAPERS.md`, which covered Lim (SSRN 7178078, 7184138) and Matilla Serrano (SSRN 7468080).

| # | Item | Type | Key content | Relevance to us |
|---|---|---|---|---|
| R1 | Matilla Serrano, "A Versioned Contract Atlas of Retail Futures Evaluations: Product Families, Stage Transitions, and Scenario-Conditional Probabilities", SSRN 7429100 (7 Sep 2026) | WP [EX] | Nominal size, target, maximum drawdown and price "are insufficient to identify the contract". Builds a version-aware atlas: 23 futures providers, 177 product-route-size configurations across 22 providers as of 5 Sep 2026. Records EOD/intraday/static drawdown, daily stops, consistency, minimum days and payout hurdles. Related work warns that ranking evaluations by price or target-to-drawdown ratio "assumes that omitted contract terms do not change the ordering" [EX] | Futures only (FundingPips is CFDs). Lesson: **model every rule of our contract** (daily limit from max(balance, equity), 10-minute idea grouping, news windows, weekend auto-close), not just target and drawdown |
| R2 | Figures surfaced with R1/R3 in the same search excerpt: evaluation pass probability **48.02% at 25K → 28.55% at 150K** as the target-to-drawdown ratio rises; conditional first-payout eligibility **38.63% → 51.96%** as the funded hurdle-to-drawdown ratio falls [EX] | WP [EX] | The excerpt did not name the paper. Most likely Matilla Serrano's Atlas or Real Contracts paper, but **unattributed** | Confirms that the **target-to-drawdown ratio** drives pass probability. Ours is 10/12 then 6/12 (<1), which is favourable |
| R3 | Matilla Serrano, "Real Contracts under Common Trading Scenarios: A Comparison Framework with a Source-Linked Pilot", SSRN 7488382 (18 Sep 2026) | WP [EX] | Replays 155 evaluation and 103 funded configurations under three synthetic P&L scenarios. Separates passing, funded eligibility, actual payment and net cash flow | The same method we use in `model_scripts/`. Their conclusion: rules beyond target and drawdown change outcomes |
| R4 | Topstep 2025 trader-performance disclosure | OFF [EX] | **16.8%** of Trading Combines passed. **51.8%** of individuals passed at least one. **33.3%** of funded individuals received a payout. **0.71%** of Express Funded traders were moved to a Live account (Jan–Dec 2025) | Single-attempt pass rates are low, but **persistence across attempts** works for most people who keep going. Plan for more than one attempt rather than betting everything on month one |
| R5 | Earn2Trade published pass rates | OFF via third-party [EX] | **10.42% (2024)**, **8.89% (2025)** | Industry baseline |
| R6 | Industry aggregates (Track360; Finance Magnates) | PRESS/PR [EX] | Blended challenge pass rate **12.3%** (2025–26, Track360). About **45%** of funded traders get at least one payout; **~7%** of all challenge buyers ever get paid. Finance Magnates: "only 7% of 300,000 prop trading accounts achieved payouts" | Base rates. Our edge must be far above the typical buyer's |
| R7 | FTMO (third-party estimates; FTMO publishes no official pass rate) | PR [EX] | Stage 1 ≈ 32–37%, stage 2 ≈ 50–60% of stage-1 passers, combined ≈ 10% | A two-phase structure like ours: phase 2 is roughly a coin flip even for phase-1 passers in the general population |
| R8 | FundingPips payout figures (third-party) | PR [EX] | Over $266M in rewards since 2022, over $69M in H1 2026 and over 70,000 rewards in H1 2026 (CoinLaw/others). **No official FundingPips pass-rate disclosure found** | The firm pays at scale. Pass rate unknown |
| R9 | Regulation: CFTC 2026 consultation (per trade press) on whether **challenge fees could be commodity-pool participation interests**, closing around 30 Nov 2026. Possible proposed rule in Q1 2027 [PRESS]. The CFTC separately sought comment on CPO/CTA registration rule changes (press release 9284-26) [OFF] | PRESS/OFF [EX] | Regulators question whether challenges are financial services or gambling | Business-continuity risk for US-facing futures firms. FundingPips is a Dubai-based CFD firm, so the impact is indirect. Watch terms changes |
| R10 | Barucci & Lan, "Shortermism and excessive risk taking in optimal execution with a target performance", arXiv 2505.15611 (2025) | WP [EX] | With a success-or-nothing target payoff, the optimal strategy is **short-termist but not excessively risky**: act fast early, then balance reaching the upper barrier against avoiding the lower one. High probability of reaching the upper barrier and very low of hitting the lower one | Supports a **front-loaded but barrier-aware** policy, not bold play (see §4) |
| R11 | Browne (1999); Cvitanić & Spivak (1999): maximizing P(reach a goal by a deadline) means replicating a **digital option** [EX] | PR | Risk rises as the deadline nears when behind target | Our deadline (one month) is **self-imposed**. FundingPips has no time limit, so failing the deadline is not failing the account. That is why the fall-back policy in §4 beats pure deadline play |

**Checked and not found:** any 2026 paper on *optimal trader strategy* specifically for prop challenges. The prop-challenge literature is about contract valuation (Lim, Matilla Serrano), and optimal play comes from goal-reaching control theory (R10, R11, and `SIZING.md`).

## 3. What a one-month pass requires (model)

### 3.1 Model [SIM]
- Daily P&L ~ N(μ, σ²), with μ = (SR/√252)·σ, SR = annual net Sharpe.
- A −3% daily kill switch (current rule), checked intraday with a Brownian bridge.
- −12% static floor = failure.
- Phase 1 at +10% at a daily close, one day for phase-2 credentials, then phase 2 at +6% from a fresh balance.
- No time limit. 4,000–5,000 paths per cell.
- Not modelled: news windows, weekend auto-close on Master, slippage through the kill switch, fat tails. **Real results would be somewhat worse.**

### 3.2 Probability of passing both phases by a deadline
| Annual SR | σ (%/day) | ≤ 1 month (21 d) | ≤ 2 months | ≤ 3 months | Eventual pass | Median days |
|---|---|---|---|---|---|---|
| 1.0 (today) | 0.50 | 0.000 | 0.000 | 0.000 | 0.919 | 399 |
| 1.0 | 1.00 | 0.000 | 0.021 | 0.076 | 0.717 | 143 |
| 1.0 | 2.00 | 0.068 | 0.247 | 0.368 | 0.523 | 45 |
| 1.5 | 0.55 | 0.000 | 0.000 | 0.003 | 0.973 | 267 |
| 1.5 | 1.50 | 0.028 | 0.171 | 0.338 | 0.706 | 66 |
| 2.0 | 1.00 | 0.001 | 0.051 | 0.170 | 0.914 | 105 |
| 2.0 | 2.00 | 0.101 | 0.366 | 0.544 | 0.701 | 41 |
| **2.5 (brief's target)** | 0.55 | 0.000 | 0.001 | 0.008 | 0.998 | 176 |
| 2.5 | 1.00 | 0.002 | 0.075 | 0.238 | 0.952 | 90 |
| 2.5 | 1.50 | 0.041 | 0.278 | 0.512 | 0.872 | 56 |
| 2.5 | 2.00 | 0.140 | 0.451 | 0.632 | 0.779 | 38 |
| 3.0 | 1.50 | 0.057 | 0.364 | 0.601 | 0.920 | 50 |
| 4.0 | 1.50 | 0.100 | 0.511 | 0.773 | 0.967 | 41 |
| 4.0 | 2.00 | 0.247 | 0.663 | 0.836 | 0.908 | 30 |
| 5.0 | 2.00 | 0.320 | 0.785 | — | 0.953 | 27 |
| 6.0 | 2.00 | 0.427 | 0.886 | 0.964 | 0.977 | 23 |
| 8.0 | 2.00 | 0.632 | 0.973 | — | 0.994 | 18 |
| 10.0 | 2.00 | 0.817 | 0.996 | — | 0.999 | 15 |

**"Aggressive first month, then fall back to 0.55%/day":**

| Annual SR | Month-1 σ | ≤ 1 month | ≤ 2 months | ≤ 3 months | Eventual pass | Median days |
|---|---|---|---|---|---|---|
| 1.0 | 2.00 | 0.067 | 0.093 | 0.119 | 0.760 | 240 |
| 1.5 | 2.00 | 0.085 | 0.123 | 0.158 | 0.859 | 188 |
| 2.0 | 2.00 | 0.103 | 0.143 | 0.198 | 0.897 | 149 |
| 2.5 | 1.50 | 0.042 | 0.097 | 0.172 | 0.971 | 137 |
| 2.5 | 2.00 | 0.135 | 0.194 | 0.273 | 0.922 | 112 |
| 3.0 | 2.00 | 0.159 | 0.231 | 0.328 | 0.941 | 93 |
| 4.0 | 2.00 | 0.232 | 0.334 | 0.474 | 0.969 | 65 |

**Reading the tables:**
- The one-month probability is driven almost entirely by **Sharpe**, and secondarily by accepting high volatility.
- Above ~2%/day the −3% kill switch fires on ~13% of days (2Φ(−1.5) [D]). Gap and slippage risk to the 4% hard limit becomes material in reality, and the FundingPips **Profit Concentration Policy** becomes a risk.
- Reaching ~50% in one month needs **SR ≈ 6–7 at 2%/day**. Reaching ~90% needs **SR ≈ 10 at 2.5%/day** (not shown in the table; 0.898 in the same model run) [SIM].

### 3.3 How much Sharpe can we realistically build?
For uncorrelated strategies combined at optimal weights, **Sharpe ratios add in quadrature**: `SR_p = √(Σ SR_i²)` [D: the maximum Sharpe of uncorrelated assets].

| Scenario (illustrative component Sharpes, *not* evidence) | Portfolio SR [D] |
|---|---|
| Today: 4 h model + NDX momentum + faded pre-FOMC | ≈ 1.0 (brief) |
| + 4 h model repaired to its 2018–26 average (~2.5× today's R/trade: 0.14 vs 0.056 R), C1 at 0.8, C2 at 0.7, C3 at 0.7, C4 at 0.5 | √(1.3² + 0.8² + 0.7² + 0.7² + 0.5²) ≈ **1.9** |
| Optimistic: core 1.3 + ten independent new edges at 0.8 each | √(1.69 + 6.4) ≈ **2.8** |
| Needed for a coin-flip one-month pass at 2%/day | **≈ 6–7**, i.e. ~55–75 independent 0.8-Sharpe edges on top of the core [D] |

**Conclusion:** plan for **SR ≈ 2–3**. That gives a realistic **2–4-month** pass with high probability, or a **~10–15%** chance of one month with the aggressive-then-fall-back policy.

## 4. The improvement plan

Each step has a **gate**: a measurable condition before moving on. Tests follow the pre-registered designs in `IDEAS.md` §3 and the standard success criterion in `IDEAS.md` §2.

### Step 0 (days 1–5): measure, prune and set up
1. **Measure live and forward Sharpe per component** (4 h model, NDX noise-area, pre-FOMC) on 2025–26 and the last 90 days. **Remove the faded pre-FOMC component.** A zero-Sharpe component only adds variance, which lowers portfolio Sharpe [D].
2. **Encode every FundingPips rule in the simulator:**
   - daily limit from max(balance, equity) at the platform-time reset;
   - −3% kill switch;
   - ±5-minute news block on the affected currency;
   - Master: 2% per idea, the 10-minute same-direction re-entry grouping, flat before the weekend;
   - **Profit Concentration Policy:** no single idea may exceed **60% of the phase target**, i.e. **6% of the account in phase 1 and 3.6% in phase 2** [D]. Breaching it is not a fail, but it delays Master rewards by requiring 4 profitable days before each [EX].
3. **Send the eight support questions** in `FUNDINGPIPS_RULES.md` §4. The "gap trading" answer gates C5, and the server time zone gates every time window.
4. **Gate:** simulator reproduces live P&L within tolerance, and rules are confirmed.

### Step 1 (weeks 1–4): biggest Sharpe gains per unit of effort
1. **Repair the 4 h model** (`ML_4H.md`):
   - P1: add mechanism features (GEX(t−1), 60/40 drift and days to month-end, auction-day flags, FOMC blackout, VIX/VIX3M);
   - P2: meta-label or abstention layer on the top-1% signals;
   - P3: time-of-day normalization.
   - **Target:** R/trade back to ≥ 0.10 over 2024–26 with purged CV and a Deflated Sharpe above zero.
2. **Test C1** (month-end 60/40 rebalancing) and **C2** (gamma-conditioned last-30-min) on SPX500/DJI30/NDX100.
3. **Test C3** (non-US cash-session momentum) on GER40, UK100 and JP225.
4. **Gate:** each accepted edge has net SR ≥ 0.5 on its test and correlation ≤ 0.3 with the others. Target portfolio SR ≥ 1.8 in the combined walk-forward.

### Step 2 (weeks 3–8): breadth
1. **Test C4** (Treasury-auction days → USDJPY/XAUUSD/NDX100). **Test C5** only if support confirms it is not "gap trading". Then C6 and C7.
2. **Extend accepted edges to more FundingPips symbols**: the 21 FX crosses, STX50, FTSE100, UKOIL. Each independent instrument where an edge holds raises Sharpe by the quadrature rule. **Watch costs**, and measure each symbol's spread in MT5 first.
3. **Cut costs:**
   - Express US-index exposure through DJI30 (0.3 bps) rather than SPX500 (1.0 bps) where signals are equivalent.
   - Avoid rollover-hour spreads.
   - Consider the **Swap-Free add-on** if any multi-day FX or metal strategy survives.
4. **Gate:** combined walk-forward SR ≥ 2.0 net of costs, with the correlation matrix and Deflated Sharpe reported.

### Step 3 (weeks 6–12): portfolio build and forward test
1. **Weighting:** volatility-target each strategy, then set weights ∝ SR_i/σ_i with shrinkage toward equal risk (avoids over-trusting noisy Sharpe estimates). Cap any strategy at 35% of risk.
2. **Forward test for ≥ 30–40 trading days** on a demo or small account with the exact execution stack, and measure **live** SR and slippage.
3. **Launch gate:** live SR ≥ 1.5 (plan with SR = 2 at most until more data exists).

### Step 4: challenge execution
**Default ("fast but safe"):**
- Run the `SIZING.md` §5 rule: `σ_day = min(cap, 0.5·ŝ·(x + C))`, with **cap = 1%/day**.
- Expected (modelled as a constant 1%/day): at SR 2–2.5, a median of ~90–105 trading days with a ≥ 91% eventual pass [SIM].

**Optional ("one-month attempt"), only if live SR ≥ 2.5 has been measured over ≥ 60 trading days:**
- **Month 1:** σ ≈ **1.5%/day**, not 2%, because of the 4% hard limit, slippage risk and profit concentration.
  - Per-idea risk ≤ 1.2% of the account.
  - No idea's profit may exceed 6% of the account (phase 1) or 3.6% (phase 2).
  - −3% kill switch.
  - No trades opened or closed within ±5 min of red news.
- **After day 21**, if not passed: drop to **0.55–0.75%/day** and continue. There is no time limit, so do not escalate risk to chase the deadline.
- **Expected at SR 2.5** [SIM]: ~4% within 1 month, ~10% within 2 months, ~17% within 3 months, ~97% eventual pass. At 2%/day in month 1: ~14% within 1 month, ~92% eventual pass.
- **Do not** open several accounts with the same strategy to "buy lottery tickets":
  - Same-strategy accounts are almost perfectly correlated, so they add little.
  - Repeated high-risk account cycling is "churning and burning", which FundingPips prohibits.
  - A second account only helps if it runs a genuinely **different and independent** strategy set, and that lowers each account's Sharpe.

### Step 5: after passing (Master)
- Drop per-idea risk to ≤ 1% (the 2% per-idea hard limit and strikes).
- Stay flat on weekends.
- Pick the reward split with `PROP_FIRM_PAPERS.md` §4 in mind: the contract-value ridge is ~1%/day.

## 5. Decision table for the owner
| Your priority | Recommended policy | Expected outcome at SR 2.5 [SIM] |
|---|---|---|
| Highest chance of passing | Kelly-cushion rule, cap 0.75%/day | ~99% eventual; ~134 trading days *mean* (`SIZING.md` Table 2; a slightly different model without the kill switch) |
| Balanced speed and safety (**recommended**) | Cap 1%/day | ~95% eventual; ~90 trading days median; ~24% within 3 months |
| Maximum one-month chance while keeping the account | 1.5–2%/day for 21 days, then 0.55%/day | 4–14% within 1 month; 92–97% eventual |
| One month at any cost | Not recommended: SR ≈ 6–7 needed for 50%; at SR 2.5 even 2%/day constant gives 14% in 1 month and a 22% fail risk | — |

## 6. Tasks for Codex (in order)
1. Build the rule-complete simulator from Step 0, with the profit-concentration and 10-minute idea-grouping rules included.
2. Measure component Sharpe (2025–26 and the last 90 days). Prune the pre-FOMC component.
3. 4 h model: P1 → P2 → P3 ablations with purged CV (`ML_4H.md` §3).
4. Pre-registered tests C1, C2, C3 (`IDEAS.md` §3), then C4 (and C5 after the rule answer).
5. Portfolio construction and a walk-forward combined Sharpe with the correlation matrix.
6. Forward test (≥ 30–40 days); report live SR, slippage and kill-switch frequency.
7. Re-run `model_scripts/one_month_mc.py` with the **measured** SR to set the launch policy.
