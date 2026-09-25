# Progress log

Updated as work proceeds, so partial results survive if the session stops.

| Step | Status | Notes |
|---|---|---|
| PLAN.md | done | search plan and assumptions |
| D-lite: symbols, crypto, news/EA rules | done | via search-engine excerpts of official help-centre pages (direct access blocked) |
| A: breadth screen (>= 30 candidates) | in progress | |
| A: depth cards (12-15) + ideas.csv | not started | |
| B: ML_4H.md | not started | |
| C: DATA_SOURCES.md | not started | |
| D: FUNDINGPIPS_RULES.md | not started | |
| E: SIZING.md | not started | |
| SOURCES.md | not started | |

## Access limitation (important for reading every number in this dossier)
The session's network egress policy blocks direct fetches of almost every research site (SSRN, arXiv, NBER, ScienceDirect, Wiley, Fed/ECB/BIS, Quantpedia, Quantitativo, CME, CBOE, FRED, CFTC, TreasuryDirect, Kaggle, FundingPips help centre, and others; tested 2026-09-25). Only the web-search tool works. So evidence comes from **search-index excerpts** of the cited pages (abstracts, summaries, snippets), not from reading full texts. Each number taken this way is labelled as such. Numbers should be checked against the full paper before any money is risked on them.

## Raw findings so far (working notes, to be moved into the deliverables)

### FundingPips (official help-centre pages, read via search excerpts)
- Daily loss 4% of the higher of day-open balance/equity, floating P&L counts; **reset at 00:00 "Platform Time (UTC+3)"** (2 Step Flex page). This conflicts with the brief's "NY + 7 h" if the server does not shift with US DST. Needs confirmation in MT5 (compare server time with UTC in both DST regimes).
- Max loss 12% static (2 Step Flex page).
- Risk per trade idea (Master, accounts > $25k): 2% of Master account size. Hard breach. **Same instrument + same direction + open at the same time = one idea; also any new same-direction position opened within 10 minutes of closing a losing trade joins that idea.** Profits do not offset losses. Evaluation phases are exempt.
- News (Master): window is 5 minutes before to 5 minutes after restricted high-impact news **and speeches**, on the affected currency only. Profits from trades opened or closed in the window may be deducted. Trades opened >= 5 h before are exempt.
- Prohibited: gap trading, HFT, server spamming, latency arbitrage, toxic flow, hedging, long-short arbitrage, reverse arbitrage, tick scalping, server-execution exploits, opposite-account trading, churning and burning.
- **EAs: third-party EAs allowed only as trade or risk managers** (exception: 1K Instant account). Wording implies personal EAs with proof of ownership are treated differently. To be checked in workstream D; this matters a lot for an automated system.
- Symbols: FX 7 majors + 21 crosses; metals XAUUSD, XAGUSD; indices DJI30, FTSE100, GER40, JP225, NDX100, SPX500, STX50; energies UKOIL, USOIL; crypto BTCUSD, ETHUSD. **No FRA40, AUS200 or HK50.**
- Crypto: leverage 1:2 in evaluation; max 1 lot per click (20 lots per click overall). Commission: lot x price x 0.04%.
- Commission: FX and metals $5/lot, or **$10/lot with the Swap-Free add-on (MT5 only; removes swaps on FX and metals, not on indices, energies or crypto)**. Indices and energies: no commission.
- Dynamic leverage on Master for metals, energies and indices: first 0.05 lots at 1:50, then stepping 1:30, 1:25, 1:20, 1:10, and 1:5 above 0.50 lots.

### Workstream A notes
- A1 Harvey, Mazzoleni & Melone (NBER w33554, 2025; revised Jan 2026): 60/40 drift signal from daily ES and 10y T-note futures returns. Threshold signal (rebalance when drift > delta) and Calendar signal (rebalance on last business day; signal interacted with a last-5-days-of-month dummy). "When stocks are overweight ... 17 bps lower equity return over the next day." QuantReturns replication (secondary): strongest 4-5 days before month-end; can flip on the final day; Sharpe > 1 over 1997-2023. Concretum Group replicated with ETFs 2003-2026, "positive and significant alpha" after conservative costs (no numbers in excerpt). Critique: Kent Daniel's discussion (Red Rock 2025) calls it largely a reversal strategy and thinks the cost-to-investors figure is overstated.
- A2 Market intraday momentum (Gao, Han, Li & Zhou, JFE 2018): SPY 1993-2013; first half-hour (prev close to 10:00 ET) predicts last half-hour (15:30-16:00). Timing strategy 6.67%/yr, SD 6.19%, Sharpe 1.08 (search excerpt). Derived: ~2.6 bps/day. Stronger on volatile, high-volume, recession and macro-news days. Decay: Komarov (2017) says US morning to last-half-hour link disappeared or reversed after 2001; one excerpt says the pattern weakened ~75% recently (source unclear). Out-of-sample R2 1.4% (first half-hour alone).
- A3 Gamma-conditioned intraday momentum (Baltussen, Da, Lammers & Martens, JFE 2021): 60+ futures 1974-2020; rest-of-day return predicts last 30 min; asset-class Sharpe 0.87-1.73; momentum present when negative gamma exposure (NGE) is negative (dealers short gamma) and absent on positive-gamma days; reversal over following days. Dim, Eraker & Vilkov (0DTE, SSRN 4692190): market-maker 0DTE gamma on average positive; positive gamma strengthens intraday reversal, negative strengthens momentum. Barbon, Beckmeyer, Buraschi & Moerke (SSRN 3925725): LETF rebalancing effect declining over time; options-gamma effect persistent. A 2024 survey (AIMS QFE) finds most LETF papers have methodological problems and the economic effect looks insignificant. Practitioner GitHub bot (forum-level): ~3 bps/day edge on 26 short-gamma sessions, gone at 3 bps cost.
- A4 Intraday momentum outside the US: Li, Sakkas & Urquhart (JFM 2022): 16 developed markets, 1-min data, ITSM significant in and out of sample in most; stronger with low liquidity, high volatility, news. Limkriangkrai et al. (PBFJ 2023): APAC ETFs; momentum mainly in China and Japan, weak in Korea, none in HK/Singapore; weaker in COVID period.
- A5 Nikkei after US: "How the prior day's S&P 500 returns influence the intraday returns of Nikkei 225 futures" (Elsevier, 2026): higher prior-day S&P return -> lower Nikkei returns in first 30 min (reversal), higher in last 30 min (momentum). Sample period not seen.
- A6 Overnight drift (Boyarchenko, Larsen & Whelan; NY Fed SR917; RFS): ES futures 02:00-03:00 ET, larger after sell-offs (end-of-day order imbalance). DECAY: NY Fed Liberty Street (July 2026) "The Disappearing Overnight Drift": ~3.7%/yr before, ~zero since 2021.
- A7 FX fixings W-pattern (Krohn, Mueller & Whelan, JF 2024): USD up before fixes, down after; ~2 bps/day swing for long-G9 portfolio. This is a time-of-day pattern already rejected on our data. FCA: short-term reversals around the London fix gone from 2015.
- A8 Month-end FX hedge rebalancing (Melvin & Prins, JFM 2015; 2004-2013): relative equity-market appreciation predicts that currency's depreciation into the month-end London 4pm fix, partial reversal next day. Camanho, Hau & Rey (RFS 2022): fund-level rebalancing on foreign excess returns; US$7.1bn equity outflow shock ~1% USD. Post-2015 evidence: practitioner bank models only.
- A9 Treasury auction cycle (Lou, Yan & Zhang, RFS 2013; sample to 2008): yields rise into auctions, fall after. Later excerpt: 2010-2025 foreign long yields no longer fall after US auctions. No study found linking it to equity, USDJPY or gold intraday.
- A10 Crypto on FundingPips: BTCUSD, ETHUSD, 1:2 leverage in evaluation, weekend holds not allowed on Master (temporary restriction since 29 Jan 2026; auto-close Friday, not a hard breach). Shen, Urquhart & Wang (Fin. Review 2022): BTC first half-hour predicts last half-hour. Concretum (practitioner): BTC intraday trend benchmark Sharpe ~1.6 gross 2018-2025; strongest Sunday evening NY to Monday ("Monday Asia open"), which conflicts with the weekend rule.
- Negative/benchmark: Mesfin (arXiv 2605.04004, 2026): 14 OHLCV intraday signal families on MNQ, 947 days 2021-2025, none survive a 2-point round-trip friction with walk-forward validation.
- Noise-area momentum paper (Zarattini, Aziz & Barbon 2024): SPY 2007-2024, 19.6%/yr net, Sharpe 1.33 (the team's existing edge).
