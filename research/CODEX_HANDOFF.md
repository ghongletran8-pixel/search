# Handoff: FundingPips challenge research → local Codex

Read this first. It explains what the bundle is, how far to trust it, and what to do next. A ready-to-paste prompt is in §6.

## 1. What this bundle is
- A **web-research dossier** (Claude Code, 25–27 Sep 2026) answering the owner's brief: find tradable edges for a FundingPips 2-Step Flex $50k challenge; review 1–4 h ML literature; list free data; document FundingPips rules; derive a sizing policy. A follow-up adds 2026 papers on prop-firm contracts.
- **No market data was used and no strategy was backtested.** Every edge below is a **hypothesis with a pre-registered test**, to be run on the owner's own MT5 M1 data.
- **Trust labels used in every file:**
  - `[EX]`: a number read from a search-engine excerpt of the cited page. Research sites were blocked for direct reading in that session, so **none of these was checked against the full paper.** Verify any [EX] number that drives a decision by opening the linked PDF.
  - `[D]`: derived by the author; the arithmetic is shown.
  - `[SIM]`: output of the synthetic model scripts in `model_scripts/`.
  - `[PR]`: practitioner or blog evidence, not peer-reviewed.
  - `n/s`: not seen.

## 2. Files and reading order
| Order | File | What it gives you |
|---|---|---|
| 1 | `CODEX_HANDOFF.md` | This guide |
| 2 | `IDEAS.md` §1 | **Top 5 edges to test first** and the key findings |
| 3 | `IDEAS.md` §3 | 12 full strategy cards, each with rules, mechanism, evidence, decay, fit, data, rule risk and a **pre-registered test** |
| 4 | `FUNDINGPIPS_RULES.md` | Rules the system must encode (news windows, 2% per idea, 10-minute re-entry rule, weekends, EA ownership, lot limits, costs, Swap-Free add-on), plus 8 questions for FundingPips support |
| 5 | `SIZING.md` | Goal-vs-floor theory; recommended policy `σ_day = min(cap, k·ŝ·(x + C))`; comparison with the current 0.45%/trade policy |
| 6 | `PROP_FIRM_PAPERS.md` | 2026 prop-contract papers (Lim; Matilla Serrano), which of them exist, and a contract-value model of our account |
| 7 | `ML_4H.md` | 8 ranked, testable proposals for the 4 h model (P1: mechanism-based state features; P2: meta-label or abstention layer; …) and what does not work |
| 8 | `DATA_SOURCES.md` | Free data: economic calendar with actual/forecast (ForexFactory-derived), CFTC COT, SqueezeMetrics GEX, CBOE VIX family, FRED/ALFRED, Treasury auctions API, Fed calendars, index-rebalance rules |
| 9 | `ideas.csv` | One row per candidate (40), with scores and priorities |
| 10 | `SOURCES.md` | Every source with URL, type and what was taken |
| — | `PLAN.md`, `PROGRESS.md` | Search plan, deviations and working notes |
| — | `model_scripts/sizing_model.py` | Reproduces all tables in `SIZING.md` (pure Python, seconds) |
| — | `model_scripts/contract_value_mc.py` | Reproduces the contract-value table in `PROP_FIRM_PAPERS.md` §4 (pure Python, about 1 minute, seed 11) |

## 3. Context from the owner's brief (condensed)
- **Account:** FundingPips 2-Step Flex $50k, MT5 CFDs.
  - Targets: +10% (phase 1), then +6% (phase 2). No time limit.
  - Losses: daily loss limit 4% of max(day-open balance, equity), floating P&L included; static max loss 12%.
  - Inactivity breach after 30 days without a closed trade.
- **Master account:** 2% loss per trade idea (hard breach), no weekend holding, ±5 min news profit deduction unless the trade was opened ≥ 5 h before.
- **Data held:** MT5 M1 bid bars with spread and tick volume since 2015:
  - FX: EURUSD, GBPUSD, USDJPY, USDCHF, USDCAD, AUDUSD, NZDUSD, EURGBP, EURJPY, EURCHF;
  - metals: XAUUSD, XAGUSD;
  - US indices: NDX100, SPX500, DJI30;
  - shorter histories: USOIL (Nov 2024), GER40 (Sep 2021), UK100 (Jul 2023), JP225 (Apr 2024).
- **Round-trip costs (bps):** EURUSD/GBPUSD 0.5; USDJPY 0.6; USDCAD 0.8; AUDUSD 1.1; USDCHF 1.1; NZDUSD 1.5; EURGBP/EURJPY 0.8; EURCHF 1.0; XAUUSD 0.45; XAGUSD 2.7; NDX100 0.6; SPX500 1.0; DJI30 0.3; USOIL 4.8.
- **Live system:**
  1. a 4 h cross-asset ML model: +0.14 R/trade over 2018–26, but +0.056 R in 2025–26;
  2. NDX100 noise-area intraday momentum;
  3. pre-FOMC drift on NDX100, now faded.
  - The combined daily Sharpe (annualized) is about 1, which gives a median of about 330 days to pass. **Goal: portfolio Sharpe ≥ 2.5 by adding independent edges with Sharpe 0.5–1 each.**
- **Already rejected by the owner** (do not re-propose without a new, post-2015-evidenced conditioning variable): see the list in `PLAN.md` and the original brief. It covers unconditional time-of-day patterns, fix windows, TOM, CPI/PPI/NFP days, most central-bank events, noise-area momentum on FX and metals, multi-day strategies (swaps), and 1-minute scalping.

## 4. What to do next (priority order)
1. **Clarify rules with FundingPips support first** (`FUNDINGPIPS_RULES.md` §4):
   - the server time zone and daylight-saving behaviour (the help centre says "UTC+3", the brief says NY + 7 h);
   - the definition of "gap trading" (this blocks card C5);
   - whether Treasury auctions and FOMC press conferences are red news events;
   - the crypto commission basis;
   - index swap rates.
2. **Run the top-5 pre-registered tests** exactly as written in `IDEAS.md` §3, with the standard success criterion in `IDEAS.md` §2:
   1. **C1**: month-end 60/40 rebalancing (SPX500/DJI30/NDX100). Needs FRED `DGS10`.
   2. **C2**: last-30-min momentum (short gamma) or reversal (long gamma). Needs SqueezeMetrics `DIX.csv` (GEX).
   3. **C3**: last-30-min momentum in the GER40/UK100/STX50/JP225 cash sessions.
   4. **C4**: Treasury-auction days → USDJPY/XAUUSD/NDX100. Needs the fiscaldata auctions API.
   5. **C5**: overnight-to-intraday reversal. **Only after the "gap trading" answer.**
   - Then C6–C12 as time allows.
   - For every test: fix parameters before looking; report the Newey–West t, the last-24-months result, net Sharpe, correlation with the three live strategies, and the Deflated Sharpe with the number of variants tried.
3. **4 h model improvements:** ablations for `ML_4H.md` P1 (new state features: GEX, 60/40 drift and days to month-end, auction flags, FOMC blackout, LETF flow proxy, VIX/VIX3M), then P2 (meta-label or abstention), then P3 (time-of-day normalization). Use purged/embargoed CV.
4. **Sizing:** implement the daily-volatility-budget rule in `SIZING.md` §5.
   - Keep the −3% daily kill switch.
   - Cap each trade idea at ≤ 1% on Master.
   - Add a 10-minute cool-down after a losing exit (FundingPips idea grouping).
   - Only raise risk above today's level after higher Sharpe is **measured live**.
   - Decide the objective: ≥ 90% pass on one account (brief) or maximum expected value across several accounts (`PROP_FIRM_PAPERS.md` §4–5).
5. **Verify the key [EX] numbers** by reading the PDFs before relying on them. The most important are C1 (Harvey–Mazzoleni–Melone, NBER w33554), C2 (Baltussen et al., JFE 2021; Dim–Eraker–Vilkov, SSRN 4692190) and C4 (Fleming–Liu–Nguyen, NY Fed SR 1188).

## 5. Guardrails
- Treat every edge as unproven until it passes the pre-registered test on out-of-sample data.
- Do not tune parameters after seeing results without counting the variants (Deflated Sharpe).
- Encode FundingPips constraints in the backtest itself:
  - news ±5 min on the affected currency;
  - flat by Friday's close on Master;
  - no same-instrument opposite positions;
  - ≤ 20 lots per order;
  - daily loss measured from max(balance, equity) at the platform-time reset.
- Keep the EA source code under version control: FundingPips allows a fully automated **personal** EA only with proof of ownership.
- The papers "Valuing Proprietary Trading Firm Evaluation Contracts" (claimed SSRN 7260819) and the SSRN "Funding Pips coupon" item (5626610) are **not** valid sources; see `PROP_FIRM_PAPERS.md` §1.

## 6. Ready-to-paste prompt for Codex
```
You are working in our trading research repo. Read research/CODEX_HANDOFF.md first, then research/IDEAS.md,
research/FUNDINGPIPS_RULES.md and research/SIZING.md. Numbers tagged [EX] are unverified search-excerpt
figures; do not treat them as facts.

Task 1: Implement the pre-registered test for card C1 (month-end 60/40 rebalancing) exactly as written in
IDEAS.md section 3, on our MT5 M1 data for SPX500, DJI30 and NDX100 (2016-01-01 to 2026-08-31), using FRED
DGS10 for the bond leg. Net of our measured costs (see CODEX_HANDOFF.md section 3). Report: trades, mean net
bps per trade, Newey-West t, last-24-months mean, net annualized Sharpe of daily P&L, the two control results,
correlation with our three live strategies, and the Deflated Sharpe given the number of variants. Do not
change parameters after seeing results; if you must, log every variant.

Task 2: Same for card C2 (gamma-conditioned last-30-minute momentum/reversal) using SqueezeMetrics DIX.csv
(GEX) with GEX(t-1) only, excluding FOMC days.

Enforce FundingPips constraints in the simulation (news +-5 min on the affected currency, flat before the
weekend on Master, no opposite positions on one instrument, daily loss from max(balance, equity) at the reset).
Write results to research/results/<card>.md.
```

## 7. How this bundle was produced
Claude Code web session on branch `claude/vibrant-cerf-pzdxkk` of `ghongletran8-pixel/search`. The same files are in the `research/` folder of that branch.
