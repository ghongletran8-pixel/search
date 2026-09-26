# Research plan: tradable edges for a FundingPips 2-Step Flex $50k challenge

Status: started 2026-09-25. Web research only. No trading code, no backtests, no accounts, no paid data.

## Deliverables (commit + push after each)
| File | Workstream | Share of effort |
|---|---|---|
| `PLAN.md` (this file) | search plan and assumptions | - |
| `PROGRESS.md` | running log, so partial results survive | - |
| `IDEAS.md` + `ideas.csv` | A. strategy candidates: at least 30 screened, 12-15 full cards, top 5 | ~60% |
| `ML_4H.md` | B. literature on 1-4 h return prediction | ~15% |
| `DATA_SOURCES.md` | C. free data sources | ~10% |
| `FUNDINGPIPS_RULES.md` | D. official FundingPips rules (forum reports kept separate) | ~10% |
| `SIZING.md` | E. sizing theory for passing a challenge | ~5% |
| `SOURCES.md` | every source, typed, with what was taken from it | - |

## Order of work
1. **D-lite first (small):** check the official FundingPips help centre for the symbol list, crypto availability and leverage, and news/EA rules. This decides which candidates fit at all (e.g. crypto, extra indices).
2. **A, breadth first:** screen candidates against the eight filters in brief section 2 using abstracts, working-paper versions and practitioner summaries. Log each candidate with one line (kept/dropped, why).
3. **A, depth:** for the best 12-15, read the working-paper version (SSRN/NBER/Fed/ECB/BIS/arXiv or author page). Pull exact rules, timing, per-trade edge, Sharpe, sample, and any out-of-sample, post-publication or replication evidence. Report decay and counter-evidence as prominently as positive results.
4. **B:** benchmark studies of intraday/1-4 h prediction (feature families, labels, meta-labelling/abstention, regime models, ensembles, training windows), including negative results.
5. **C:** verify free data sources by opening each official page (URL, coverage start, frequency, format, time zone, revision status, licence).
6. **D:** full rules pass from the official help centre.
7. **E:** summarize Dubins-Savage, Browne (1995/1997/1999), Grossman-Zhou (1993), CPPI and fractional Kelly with loss limits, then derive a practical policy. Any numbers derived here come from closed-form formulas stated in the file, not from backtests.

## Search plan (where and what)
- **Primary literature:** SSRN, NBER, arXiv q-fin, Fed/ECB/BoE/BIS working papers; journals JF, JFE, RFS, JFQA, JFM (futures), JIMF, JBF.
- **Catalogues/practitioners:** Quantpedia free summaries, AQR, Man Group, Robeco, CME Group, Research Affiliates; replication blogs (Quantocracy index, Robot Wealth, QuantConnect, Quantitativo).
- **Seed topics (from the brief), then snowball through citing papers:**
  1. US index intraday: market intraday momentum (Gao-Han-Li-Zhou 2018) and gamma conditioning (Baltussen-Da-Lammers-Martens 2021); leveraged/inverse ETF rebalancing; closing auction/MOC; 0DTE era; VIX conditioning; overnight drift conditional on dealer inventory (Boyarchenko-Larsen-Whelan).
  2. Rebalancing flows: pension/balanced-fund month-end and quarter-end (Harvey-Mazzoleni-Melone); FX hedge rebalancing on foreign-vs-US equity performance; index rebalances.
  3. Rates: Treasury auction cycle (Lou-Yan-Zhang 2013) and spillovers; refunding; Fed blackout/speakers.
  4. FX: intraday momentum/reversal (Elaut-Froemmel-Lampaert 2018); lead-lag; post-2015 fix; Asia-to-London conditional; order-flow (CLS) results with price proxies; CNY fixing; FX option expiries.
  5. Metals/oil: COMEX options expiry, SGE fix, real yields, silver-gold lead-lag, OPEC+, roll.
  6. Non-US indices: opening drive/gap, closing auctions, Tokyo/HK lunch breaks, US-close-to-Asia lead-lag, USDJPY-to-Nikkei.
  7. Crypto CFDs: only if FundingPips offers them on MT5 (checked in step 1).
  8. Anything 2022-2026 on intraday predictability after costs or flow-driven price pressure.

## Screening rules (from brief section 2)
Mechanism; evidence from 2015 or later (decay reported); hold minutes to 1 day; >= 20 trades/yr/instrument or poolable; gross edge >= 2-3x our round-trip cost; testable with MT5 M1 bid bars + free data; rule-compatible (no news-spike trading, <2% loss per idea, flat at weekends preferred); independent of the 4 h ML model and NDX100 noise-area momentum. Anything on the "already rejected" list is dropped unless a new, post-2015-evidenced conditioning variable is found (and named).

## Assumptions (no questions asked, per brief)
- **Server time:** "New York + 7 h" means UTC+2 in NY winter and UTC+3 in NY summer, so the 00:00 server reset is 17:00 New York time all year. To be confirmed from official sources in workstream D.
- **Costs:** the brief's measured round-trip costs (bps) are the benchmark. "Gross edge >= 2-3x cost" is checked against them per instrument. Where a paper reports returns per trade in % or points, I convert to bps only when the conversion is unambiguous, and say so.
- **Per-trade edge from annual figures:** if a paper reports only annual return and trade count, per-trade edge = annual return / trades, labelled as derived.
- **Evidence scores (0-5):** 5 = peer-reviewed, post-2015 sample, independent replication and post-publication evidence; 3 = one credible study with post-2015 data; 1 = practitioner claim only; 0 = none.
- **Futures vs CFD:** results on index/commodity futures are assumed to transfer to the matching CFD minus our costs. Cash-session timings are given in exchange time and New York time.
- **"High-impact news":** the rule risk of an idea is judged against the FundingPips news rules found in workstream D. Where a trade window overlaps a scheduled release, I flag it.
- **Paywalls:** where only an abstract or summary was read, the card says so, and numbers from secondary sources are marked as such.
- **Subagents:** not used (not requested); the work is done in this session.

## Deviations from the plan (added at the end)
- **Access:** the session's network policy blocked direct fetches of nearly all research sites and of the FundingPips help centre. Only web search worked, so every number is from search-index excerpts ([EX]) or derived ([D]). No full texts were read. See the caveat boxes at the top of each file.
- **Scope:** 40 candidates screened, 12 full cards (brief: at least 30 and 12-15).
- **Sizing:** besides summarizing the theory, SIZING.md derives the minimum-expected-time policy under a failure-probability budget (Kelly on a cushion above a virtual floor) and evaluates it numerically against the current fixed-fraction policy.
