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
