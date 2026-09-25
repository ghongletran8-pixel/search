# IDEAS: tradable-edge candidates for the FundingPips 2-Step Flex challenge

Workstream A. Web research only: no backtests and no market data were used. Compiled 2026-09-25.

> **Read this first: how much to trust the numbers.**
> This session's network policy blocked direct access to almost every research site (SSRN, arXiv, NBER, ScienceDirect, Wiley, Fed/ECB/BIS, Quantpedia, CME, CBOE, the FundingPips help centre, and others). The only working tool was a web-search engine that returns excerpts of the indexed pages. So:
> - **[EX]** means a number taken from a search-index excerpt of the cited page (an abstract, summary or snippet). It has **not** been checked against the full paper.
> - **[D]** means I derived it, and the derivation is shown next to it.
> - **[PR]** means practitioner or blog evidence rather than peer review. **[n/s]** means the number was not seen.
> - Every card needs one full-text read before money is risked on it. The PDF links are given.
>
> **Times** are New York time (ET) unless stated. The brief says server time is ET + 7 h. The official help centre says the daily reset is at "00:00 Platform Time (UTC+3)". That matches ET + 7 h only if the server shifts with US daylight saving; see `FUNDINGPIPS_RULES.md`.

---

## 1. Executive summary

### 1.1 Top 5 to test first

| Rank | Card | Idea | Why first | Main risk |
|---|---|---|---|---|
| 1 | C1 | **Front-run month-end 60/40 pension rebalancing** on SPX500/DJI30/NDX100 | Clear forced flow (fixed-weight funds must rebalance). New (NBER 2025, AFA 2026) with a large next-day effect: −17 bps when equities are overweight [EX]. Sharpe > 1 over 1997–2023 [EX]. Two independent replications [PR]. Unrelated to intraday momentum. | Published Jan 2025, so decay is likely. A discussant calls it mostly a reversal strategy. Low frequency (~48 signal-days/yr [D]). |
| 2 | C2 | **Last-30-minute momentum/reversal on US indices, conditioned on dealer gamma** (free SqueezeMetrics GEX) | Strongest mechanism in the intraday literature (option dealers' delta hedging). Momentum when dealers are short gamma, reversal when long gamma: JFE 2021, plus 0DTE-era evidence 2024–25 [EX]. ~250 opportunities/yr/index. DJI30 costs only 0.3 bps. | The momentum branch overlaps the NDX noise-area strategy. US intraday momentum has decayed since the 2000s (Komarov 2017) [EX]. |
| 3 | C3 | **Intraday momentum in the non-US cash sessions** (GER40, FTSE100/UK100, STX50, JP225) | Documented in 12 of 16 developed markets (JFM 2022) [EX] and in 8 European index futures to 2020 (JFE 2021) [EX]. The sessions end at 11:00–11:30 ET (Europe) and 01:00–02:30 ET (Japan), away from our US trades. | Short M1 history for UK100 and JP225. No per-market cost or edge numbers were seen. |
| 4 | C4 | **Treasury-auction-day price pressure transmitted to USDJPY, gold and NDX100** | New NY Fed evidence over 33 years: yields rise in the hours before an auction and reverse after, still present in 2015–2024 [EX]. ~90–100 coupon auctions/yr [D]. Uses our lowest-cost FX and metal. | The spillover into FX, gold and equity CFDs is **untested** anywhere I could find. The card is a cheap falsification test. |
| 5 | C5 | **Overnight-to-intraday (CO-OC) reversal** on index CFDs: fade the overnight move during the cash session | 2–5× the Sharpe of ordinary reversal, across futures asset classes [EX]. Practitioner replications through recent years favour equity index futures [PR]. Likely **negatively** correlated with our momentum edges, which diversifies. | FundingPips lists "gap trading" as prohibited without defining it. **Ask support before testing.** Futures results were "much weaker" than for stocks [EX]. |

Next in line: C6 (FX month-end hedge rebalancing conditioned on *foreign minus US* equity performance, as the brief asked), C7 (Nikkei's first and last 30 minutes conditioned on the prior-day S&P 500 return, from a new 2026 paper), and C8 (the month-end last-hour variant of C1).

### 1.2 What the screen found

1. **Flow-based edges hold up better than pattern-based ones.** The two ideas with the best recent evidence (C1 rebalancing and C2 dealer gamma) both name a forced trader. Pure OHLCV patterns on liquid index futures failed a 2021–2025 walk-forward falsification study on MNQ at realistic costs: 14 signal families, none passed [EX] ([Mesfin 2026](https://arxiv.org/abs/2605.04004)).
2. **Decay is documented, so be careful:**
   - The US **overnight drift** (02:00–03:00 ET, about 3.7%/yr) has averaged **close to zero since 2021**, per its own authors (NY Fed, July 2026) [EX].
   - **Leveraged-ETF** end-of-day effects declined over time and look economically insignificant once fund flows are counted [EX]. But LETF rebalancing reached a record ~$50bn/day in 2026 [EX, press], so this may have changed; see C10.
   - **US market intraday momentum** weakened or reversed after 2001 in one study [EX].
   - **London-fix reversals** disappeared from 2015 onward in FCA work [EX].
3. **Rules and costs matter as much as any single edge** (details in `FUNDINGPIPS_RULES.md`):
   - **Swap-Free add-on (MT5):** FX and metals pay $10/lot instead of $5/lot and **no overnight swaps**. This undercuts the "multi-day strategies die from swaps" rejection for FX and metals, so re-test them under that cost model. Indices, energies and crypto still pay swaps. It is bought with the account.
   - **Trade-idea grouping (Master):** a new same-direction position opened within **10 minutes after closing a loser** on the same instrument joins the losing idea toward the 2% hard limit [EX]. Any re-entry logic needs a 10-minute cool-down.
   - **Automation:** a *personal* EA may run fully automated with **proof of ownership** (source code, version history, or a live explanation). Third-party EAs may only manage trades or risk [EX].
   - **Weekends (Master):** a temporary restriction since 29 Jan 2026 closes all trades at Friday's close on 2-Step Flex Master accounts, crypto included [EX].
   - **"Gap trading" is prohibited but not defined** [EX]. This matters for C5 and any gap strategy.
4. **No candidate here has published post-2020 net-of-cost results on CFDs.** Treat every card as a hypothesis. Rank by the strength of the mechanism and the independence of the edge, and pre-register the tests as written below.

---

## 2. How to read the cards

- **Scores (0–5):**
  - *evidence*: 5 = peer-reviewed, post-2015 data, independent replication and post-publication data;
  - *persistence*: evidence that it still works in 2020–2026;
  - *fit*: to our instruments and costs;
  - *independence*: from the 4 h ML model and NDX noise-area momentum;
  - *data*: free and point-in-time.
- **Priority** is 1 for the first to test.
- **Rule risk** is low, medium or high against the FundingPips rules in `FUNDINGPIPS_RULES.md`.
- **Standard success criterion.** Each card's test lists its own conditions; unless it says otherwise, a card must meet all of these:
  - sample 2016-01-01 to 2026-08-31, or the instrument's full M1 history if shorter;
  - net of our measured costs, with parameters fixed before looking;
  - **mean net return per trade > 0 with Newey–West t ≥ 2.0**;
  - positive mean in the **last 24 months**;
  - net annualized Sharpe of the strategy's daily P&L ≥ 0.5;
  - the effect is larger than in the stated control (difference t ≥ 1.5);
  - daily P&L correlation with our three live strategies ≤ 0.3;
  - report the Deflated Sharpe Ratio (Bailey & López de Prado) with the number of variants tried.
- "Gross edge vs cost" compares a per-trade gross figure with the brief's measured round-trip cost for that instrument.

---

## 3. Full cards (12)

### C1. Front-run month-end 60/40 rebalancing (pension and balanced-fund flows)
- **Instruments:** SPX500 (primary), DJI30, NDX100. Optional: GER40/STX50 as a test of non-US pension flow; no evidence was seen for these.
- **Rule as published** (Harvey, Mazzoleni & Melone, "The Unintended Consequences of Rebalancing", NBER WP 33554, Jan 2025, revised 2026; AFA 2026 program):
  - Track the weight drift of a 60% equity / 40% bond portfolio using daily returns of front E-mini S&P 500 and 10-year T-note futures, mid-Sep 1997 to mid-Mar 2023 [EX].
  - Two signals:
    - **Calendar:** the drift is assumed to be rebalanced on the last business day of each month. The signal is interacted with a dummy equal to 1 in the **last 5 trading days** of the month [EX].
    - **Threshold:** rebalance whenever the drift exceeds a band δ [EX; δ n/s].
  - The trade is long/short S&P futures against T-note futures, with the two signals scaled to equal risk [EX].
  - Results:
    - "When stocks are overweight … a decrease in equity returns of **17 basis points over the next day**" [EX];
    - the strategy's **Sharpe ratio is above 1 over 1997–2023** [EX];
    - "calendar predictability **peaks in the last four days** of the month" [EX];
    - a replication finds the signal strongest **4–5 days before month-end**, often **flipping on the final day** [EX, PR].
- **Our adaptation (pre-registered):**
  - For each day *d* among the last 5 trading days of month *m* except the last day:
    - `w = 0.6(1+R_eq)/(0.6(1+R_eq) + 0.4(1+R_bd))`, where:
      - `R_eq` = S&P 500 return from the last close of month *m*−1 to the close of day *d* (our SPX500 bars at 16:00 ET);
      - `R_bd` = the 10y T-note return over the same span, proxied by `−7 × Δy10` with `y10` = FRED `DGS10` (or the IEF ETF from Stooq).
    - `z = w − 0.60`.
  - **Intraday version (primary, no swap):** if `z > 0` short, if `z < 0` long, SPX500 and DJI30 on day *d*+1 from 09:35 to 15:55 ET, sized ∝ |z| and capped.
  - **Daily version:** hold 15:55 ET on day *d* to 15:55 ET on day *d*+1, paying one swap. Close before the Friday close on the Master account.
- **Mechanism:**
  - Defined-benefit pensions, target-date funds, balanced funds and endowments hold fixed weights and trade back to target on calendar dates or at bands. That demand is price-insensitive and predictable.
  - Press estimates for Q2-2026: Goldman, ~$30bn of US pension equity selling; JPMorgan, up to $165bn globally, including ~$55bn from US DB plans and ~$60bn from Japan's GPIF [EX, press].
  - The other side: dealers and front-runners who get paid for warehousing that flow.
- **Evidence and replications:**
  - The NBER paper [EX].
  - QuantReturns futures replication, Sharpe > 1 [EX, PR].
  - Concretum Group with SPY/TLT, 2003–2026: "positive and statistically significant alpha … even under conservative transaction-cost assumptions" (no number seen) [EX, PR].
  - CXO Advisory summary [EX].
- **Counter-evidence and decay:**
  - Kent Daniel's discussion (Red Rock 2025) argues it is largely a **reversal** strategy and that the investor-cost estimate is overstated [EX].
  - The paper appeared in Jan 2025 and banks publish month-end flow estimates, so crowding and pre-positioning are likely.
  - No post-2023 out-of-sample result from the authors was seen.
  - The **last-day flip** means the day choice matters.
- **Fit:**
  - About 4 signal-days × 12 months ≈ **48 trades/yr per index** [D]. The three US indices are nearly the same bet.
  - Gross 17 bps next day [EX] against 1.0 bps round trip on SPX500 (0.3 on DJI30) gives **≈17×** cost [D], before any swap.
  - Correlation with our system: **low** with NDX intraday momentum (different horizon and conditioning); low to medium with the 4 h model (it has calendar inputs but no rebalancing-drift input).
- **Data:** free.
  - Own SPX500/DJI30 bars.
  - FRED `DGS10` (daily; H.15).
  - Optional: IEF/TLT daily closes from Stooq.
  - For quarter-ends, press flow estimates can be a check but are not point-in-time data.
- **FundingPips rule risk: low.**
  - Month-end days often have releases such as PCE or Chicago PMI. Entries at 09:35 and 15:55 ET avoid the ±5 min windows around 08:30 and 10:00 releases.
  - Holding through news is allowed.
  - Weekends: flat at Friday's close.
  - Loss per idea is well inside 2% at normal sizing.
- **Pre-registered test:**
  - Rule, instruments and windows as above.
  - Controls:
    1. The same rule applied on trading days −10 to −6 (mid-month), where no calendar flow is expected.
    2. The unconditional mean of the last-5-day window (no sign from `z`).
  - Success: the standard criterion, plus the quarter-end months showing a larger mean than the other months. The last criterion is directional and informative, not required.
- **Scores:** evidence 4, persistence 3, fit 4, independence 4, data 5. Rule risk low. **Priority 1.**

### C2. Late-day momentum or reversal on US indices, conditioned on dealer gamma
- **Instruments:** DJI30 (cheapest, 0.3 bps), NDX100 (0.6), SPX500 (1.0).
- **Rules as published:**
  - *Gao, Han, Li & Zhou (JFE 2018)*:
    - The first half-hour return (previous 16:00 close to 10:00 ET) predicts the last half-hour (15:30–16:00) on SPY, 1993–2013 [EX].
    - A timing strategy on its sign made **6.67%/yr with volatility 6.19%, Sharpe 1.08** [EX]. That is ≈ **2.6 bps per trading day** [D: 6.67%/252].
    - The effect is stronger on volatile, high-volume, recession and **major macro-news** days [EX].
    - Out-of-sample R² was 1.4% for the first half-hour alone [EX].
  - *Baltussen, Da, Lammers & Martens (JFE 2021)*:
    - Over 60+ futures (equity, bond, commodity, FX), 1974–2020, the **rest-of-day return** (previous close to 30 min before the close) predicts the **last 30 minutes** [EX].
    - Asset-class Sharpe ratios are **0.87–1.73** [EX].
    - For the S&P 500 the momentum exists when dealers' gamma exposure is negative, gets stronger the more negative it is, and is **absent on positive-gamma days** [EX].
    - Returns revert over the following days [EX].
  - *Dim, Eraker & Vilkov (SSRN 4692190; 0DTE era)*:
    - Market makers' 0DTE gamma is **positive on average**.
    - Positive gamma strengthens intraday **reversal**, negative gamma strengthens momentum. The evidence is consistent with delta hedging, not informed trading [EX].
  - *Barbon & Buraschi ("Gamma Fragility")*: momentum or reversal from negative or positive gamma imbalance interacting with illiquidity [EX].
- **Our adaptation (pre-registered):**
  - Signal: `r_ROD = ln(P(15:30) / P(prev 16:00 close))`.
  - Gamma state: SqueezeMetrics GEX for the previous day, posted around 05:30 ET the next morning [EX], so it is known before the open.
  - **Short-gamma branch:** if GEX(t−1) is in the bottom quintile of its trailing 250-day distribution, or below zero, trade **sign(r_ROD)** from 15:30 to 15:58 ET.
  - **Long-gamma branch:** if GEX(t−1) is in the top quintile, trade **−sign(r_ROD)** over the same window.
  - Both branches require |r_ROD| > 0.5 × its 20-day standard deviation.
  - Exclude FOMC days: the 14:30 press conference counts as a speech under FundingPips news rules.
- **Mechanism:**
  - Option dealers who are short gamma must buy strength and sell weakness to stay delta-neutral. Long gamma does the opposite.
  - Leveraged-ETF rebalancing adds same-direction flow near the close (see C10).
  - The other side: dealers' hedging flow, and late-informed or infrequent rebalancers who trade near the close (Gao et al.) [EX].
- **Out-of-sample evidence and replications:**
  - Li, Sakkas & Urquhart (JFM 2022) find intraday momentum internationally [EX].
  - Practitioner GEX bot on MES: ~3 bps/day on only 26 short-gamma sessions, gone at 3 bps cost. Too few trades to conclude anything [EX, PR].
  - Barbon et al. (SSRN 3925725): the gamma effect is **persistent** through their sample, while the LETF effect declines [EX].
- **Counter-evidence and decay:**
  - Komarov ("Intra-Day Momentum", SSRN 2905713, 2017): the morning-to-last-half-hour relation in the S&P 500 disappeared or reversed after 2001 [EX].
  - The 0DTE regime (2022 onward) makes dealer gamma positive on average [EX]. That may have moved the edge from momentum toward reversal.
  - MNQ falsification 2021–2025: OHLCV intraday signals do not beat friction [EX].
- **Fit:**
  - ~250 candidate days/yr per index. The two quintile branches give ≈ **100 trades/yr per index** [D].
  - Gross ≈ 2.6 bps/day unconditional (SPY 1993–2013) [D]. The conditional edge should be larger but was n/s.
  - Against cost: ≈ **8.7× on DJI30**, 4.3× on NDX100, 2.6× on SPX500 [D].
  - Correlation: the **short-gamma branch** overlaps NDX noise-area momentum (both trade with the trend into the close), so *medium-high*. The **long-gamma branch** is a fade, so *low or negative*.
- **Data:** free.
  - SqueezeMetrics `DIX.csv` (date, price, DIX, GEX; from 2011) [EX].
  - Own M1 bars.
  - Optional conditioning: VIX/VIX9D from CBOE.
- **FundingPips rule risk: low.** Few red-folder releases fall at 15:30–16:00. Exclude FOMC days. Flat before the close, so no weekend exposure. The loss per idea is small.
- **Pre-registered test:**
  - Rule, instruments and windows as above, 2016–2026.
  - Controls:
    1. The same 15:30–15:58 trade on all days, unconditional (the Gao/Baltussen rule).
    2. Middle-quintile GEX days.
  - Success: the standard criterion for each branch separately, plus a branch mean greater than the control-2 mean.
  - Report the correlation of each branch with the noise-area strategy.
- **Scores:** evidence 4, persistence 3, fit 4, independence 2 (momentum branch) or 4 (reversal branch), data 4. Rule risk low. **Priority 2.**

### C3. Intraday momentum in non-US cash sessions (GER40, FTSE100/UK100, STX50, JP225)
- **Instruments:** GER40 (our data from Sep 2021), UK100 = FundingPips "FTSE100" (from Jul 2023), JP225 (from Apr 2024), STX50 (offered by FundingPips; we hold no data).
- **Rules as published:**
  - *Li, Sakkas & Urquhart (JFM 2022)*:
    - Intraday time-series momentum in **16 developed markets** using 1-minute data. It is significant in and out of sample "in most countries", described elsewhere as **12 of 16** [EX].
    - Stronger with low liquidity, high volatility and discrete news [EX].
    - The first three half-hour returns strongly predict the last half-hour [EX].
  - *Baltussen et al. (2021)*: includes **8 European equity index futures**, Dec 1974–May 2020 [EX].
  - *Limkriangkrai et al. (PBFJ 2023)*: APAC ETFs. Momentum **present in Japan and China**, weak in Korea, absent in Hong Kong and Singapore, **weaker in the COVID period** [EX].
- **Our adaptation (pre-registered):**
  - For each index, in its own cash session: `r_ROD` from the previous official close to 30 minutes before the close. Trade `sign(r_ROD)` over the last 30 minutes, with the same |r_ROD| filter as C2.
  - **GER40/STX50:** Xetra runs 09:00–17:30 CET with a closing auction ending 17:30–17:35 [EX]. Trade 17:00–17:29 CET (11:00–11:29 ET).
  - **UK100:** LSE continuous trading 08:00–16:30 UK, closing auction 16:30–16:35 [EX]. Trade 16:00–16:29 UK (11:00–11:29 ET).
  - **JP225:** TSE afternoon session 12:30–15:30 JST with a closing auction since 5 Nov 2024 [EX]; before that date the close was 15:00. Trade 15:00–15:29 JST (02:00–02:29 ET in US summer, 01:00–01:29 in US winter).
- **Mechanism:** the same as C2 (dealers' gamma hedging, infrequent rebalancers and late-informed traders converging on the close). The other side: liquidity providers and hedgers who must be flat or hedged at the close.
- **Counter-evidence and decay:**
  - The APAC effect is weaker in COVID and absent in HK and Singapore [EX].
  - No post-2020 per-market numbers were seen.
  - The brief's rejected "European-open drift" is a different window; this card uses the close.
- **Fit:**
  - ~250 opportunities/yr per index, ≈ 125 after the magnitude filter [D].
  - Gross edge per trade n/s. Our costs for these CFDs are not in the brief. FundingPips charges no commission on indices, so only spread matters; measure it.
  - Correlation: *medium* for GER40/UK100/STX50, whose close (11:00–11:30 ET) overlaps the US morning; *low* for JP225, whose close (01:00–02:30 ET) is outside our US trades.
- **Data:** own M1 bars, but short. Only GER40 has about 5 years. For JP225 before 2024, free intraday history of Nikkei futures is unlikely; we could buy nothing, so the test power is limited.
- **FundingPips rule risk: low.** European windows at 11:00 ET usually avoid US releases (08:30 and 10:00). Japan's window is free of major US releases.
- **Pre-registered test:**
  - As above, pooled across the four indices with index fixed effects.
  - Control: the same 30-minute window placed 60 minutes earlier (a mid-afternoon window).
  - Success: the standard criterion on the pooled sample, the last-24-months condition per index where history allows, and the JP225 result reported separately.
- **Scores:** evidence 3, persistence 3, fit 3, independence 3 (Europe) or 4 (Japan), data 3. Rule risk low. **Priority 3.**

### C4. Treasury-auction-day price pressure, transmitted to USDJPY, gold and NDX100
- **Instruments:** USDJPY (0.6 bps), XAUUSD (0.45 bps), NDX100 (0.6 bps).
- **Evidence (rates):**
  - Fleming, Liu & Nguyen, "Intraday Price Pressure and Order Flow Around U.S. Treasury Auctions" (NY Fed Staff Report 1188, Mar 2026):
    - With **33 years** of intraday data, **yields rise in the hours before an auction and reverse afterward** [EX].
    - The pressure is stronger when dealers are more constrained and weaker when investor demand is strong or elastic [EX].
    - Price pressure "has **not increased in recent years**" because non-dealers absorb more supply. The paper treats **2015–2024** as a separate period [EX].
    - Magnitudes n/s.
  - Earlier work: Lou, Yan & Zhang (RFS 2013; sample to 2008) on multi-day auction cycles [EX]; Sigaux (ECB WP 2208) on trading ahead of auctions [EX].
  - One excerpt says foreign long-term yields no longer fall after US auctions over 2010–2025 [EX].
- **The spillover is not documented.** I found no study linking auction-day pressure to USDJPY, gold or equity index futures intraday. Press anecdotes show weak auctions coinciding with equity sell-offs (e.g. a $70bn 5-year auction in 2026) [EX, press]. The hypothesis is that part of the pre-auction rise in yields appears as USDJPY up, gold down and long-duration equities (NDX) down, and then reverses after 13:00 ET.
- **Our adaptation (pre-registered):**
  - On coupon-auction days only (2/3/5/7/10/20/30-year and TIPS; 13:00 ET close; dates and times from fiscaldata.treasury.gov):
    - **Pre-auction leg:** 09:35 → 12:55 ET: long USDJPY, short XAUUSD, short NDX100 (equal risk).
    - **Post-auction leg:** 13:05 → 15:55 ET: the reverse.
  - Variants to register in advance: only 10/20/30-year auctions; weighting by auction size.
- **Mechanism:** primary dealers must absorb new supply and demand a concession, bought back after the auction, when yields reverse. The cross-asset part relies on intraday yield sensitivity of USDJPY, gold and long-duration equities. That is plausible but unquantified here.
- **Fit:**
  - ≈ **90–100 coupon auctions/yr** [D: monthly 2/3/5/7-year (≈48), monthly 10/30-year including reopenings (≈24), monthly 20-year (≈12), plus TIPS (≈8). Count exactly from fiscaldata].
  - Gross edge n/s.
  - Correlation: **low** with both live strategies (event calendar, not price pattern). The 4 h model may partly see rates moves but has no auction input.
- **Data:** free. Fiscaldata "Treasury Securities Auctions Data" API: auction dates and security terms since 1979, no key needed [EX]. Closing times are standard (13:00 ET for coupons, 11:30 ET for bills); check them in the dataset.
- **FundingPips rule risk: low to medium.** Auctions are usually rated low impact (the US 10-year note auction is rated "Low" on Myfxbook's calendar [EX]), but FundingPips uses its own dashboard calendar, where only red events are restricted [EX]. Check that auctions are not red. Entries and exits at ±5 min around 13:00 are set so no trade is opened or closed inside [12:55, 13:05].
- **Pre-registered test:**
  - As above.
  - Controls: the same legs on non-auction weekdays of the same weeks, and the sign-flipped rule.
  - Success: the standard criterion on the combined two-leg P&L, plus the pre-auction leg mean significantly above the control-days mean (t ≥ 2).
- **Scores:** evidence 2 (strong for bonds, none for the spillover), persistence 3, fit 4, independence 4, data 5. Rule risk low to medium. **Priority 4.**

### C5. Overnight-to-intraday (CO-OC) reversal on index CFDs
- **Instruments:** SPX500, NDX100, DJI30 (US cash session); GER40, UK100, STX50, JP225 (own sessions). Optionally XAUUSD around COMEX hours.
- **Rules as published:**
  - *Della Corte, Kosowski & Wang, "Market Closure and Short-Term Reversal"* (2015/2016) and *Liu, Liu, Wang, Zhou & Zhu, "Overnight-Intraday Reversal Everywhere"* (SSRN 2730304):
    - Each day, go long assets with low overnight (close → open) returns and short those with high ones; hold open → close.
    - Returns and Sharpe ratios are **2–5× those of close-to-close reversal**, in equity index, interest-rate, commodity and currency futures [EX].
    - Explained by liquidity provision under periodic market closures (the Hong & Wang 2000 model) and by cross-sectional dispersion [EX].
  - The magnitudes for futures (1982–2014) are "**much weaker**" than for US stocks [EX, CXO summary].
  - QuantReturns (2016–2024 period reviewed, practitioner): CO-OC gave the best risk-adjusted results among reversal variants for ES, YM, NQ, EMD, NKD and RTY [EX, PR].
- **Our adaptation (pre-registered):**
  - *Time-series:* `r_ON` = previous cash close → today's cash open (09:30 ET for the US; local opens elsewhere).
    - Trade `−sign(r_ON)` from open + 5 min to close − 2 min, only when |r_ON| > 0.5 × its 20-day standard deviation.
  - *Cross-sectional (US trio only):* long the index with the lowest `r_ON` z-score and short the highest, open + 5 → close − 2.
- **Mechanism:** overnight order imbalances are absorbed by liquidity providers at the open, who are then paid as prices revert during the day. It is the same inventory logic as the NY Fed overnight-drift work, but in the opposite window.
- **Counter-evidence:**
  - Weaker results in futures than in stocks [EX].
  - No post-2016 peer-reviewed out-of-sample result was seen.
  - Our NDX noise-area momentum trades breakouts from the open, so the two will often disagree. That diversifies, but it can make netting messy.
- **Fit:**
  - ~250 opportunities/yr per index, ≈ 125 after the filter [D]. Gross n/s.
  - Correlation: *negative or low* against noise-area momentum (a fade against a breakout); low against the 4 h model.
- **Data:** own M1 bars only.
- **FundingPips rule risk: HIGH until clarified.** "**Gap trading**" is on the prohibited list and is not defined in what I could read [EX]. Fading an opening gap *after* the open, without holding through the close-to-open gap, is probably not what prop firms mean (usually positions opened before a market closure to profit from the reopening gap). **Get a written answer from support before spending test time.**
- **Pre-registered test:**
  - Time-series rule as above.
  - Control: the same holding window on days with |r_ON| below the filter.
  - Success: the standard criterion, plus a negative correlation with the noise-area strategy's daily P&L. The negative correlation is reported, not required.
- **Scores:** evidence 3, persistence 2, fit 3, independence 4, data 5. Rule risk **high (pending clarification)**. **Priority 5.**

### C6. Month-end FX hedge rebalancing, conditioned on foreign-minus-US equity performance
- **Instruments:** EURUSD, GBPUSD, USDJPY, AUDUSD, NZDUSD, USDCAD, USDCHF, all at 0.5–1.5 bps.
- **Rule as published:**
  - *Melvin & Prins (JFM 2015)*:
    - When a market's equities **appreciate relative to others** during the month, **its currency depreciates into the last London 4 pm fix of the month**, then partly reverses the next day [EX].
    - This is consistent with international funds resizing currency hedges. Eight most liquid currencies, 2004–2013 [EX].
  - *Camanho, Hau & Rey (RFS 2022)*:
    - Fund-level rebalancing after foreign excess returns.
    - A US$7.1bn equity outflow shock moves the dollar ~1% [EX].
- **Our adaptation (pre-registered):**
  - For currency *k* ≠ USD: `x_k` = month-to-date USD return of the local index (DAX or Euro Stoxx 50 for EUR, FTSE 100 for GBP, Nikkei 225 for JPY, ASX 200 for AUD, NZX 50 for NZD, TSX for CAD, SMI for CHF) **minus** the S&P 500's month-to-date return, through the close before the last business day.
  - US-based holders of foreign equities hedge by selling currency *k* forward. A higher foreign value means more *k* to sell into the fix, so *k* weakens. Foreign holders of US equities work the other way and are captured by the minus sign.
  - Trade: on the last business day, 11:00 → 15:59 London, go **short currency *k* against USD when `x_k` > 0** and long when `x_k` < 0.
  - Optional leg: reverse from 16:05 London to 12:00 ET the next business day.
- **Mechanism:** passive hedged equity mandates reset currency hedges at month-end fixes, a benchmark-driven, price-insensitive flow. Bank month-end models (e.g. Credit Agricole) publish the implied USD direction each month [EX].
- **Counter-evidence:**
  - Our own test with the S&P 500 alone was **mixed**.
  - FCA work finds that short-term reversals around the fix **disappeared from 2015** [EX].
  - A practitioner study over 138 month-ends (Feb 2015–Jul 2026) with S&P-only conditioning reports "a coherent pattern" but no numbers were seen [EX, PR].
  - The relative-performance variable is the new element; no post-2015 academic test of it was found.
- **Fit:**
  - 12 events/yr × 7 pairs, strongly correlated through USD, so about 12–20 effective bets/yr [D]. Gross n/s.
  - Correlation: **low** with both live strategies.
- **Data:** free daily closes for the foreign indices (Stooq; FRED has the Nikkei 225) and our FX M1 bars.
- **FundingPips rule risk: low.** Month-end mornings in the US (e.g. Chicago PMI at 09:45 ET) fall inside the London window. Holding through them is allowed; do not open or close within ±5 min.
- **Pre-registered test:**
  - As above.
  - Controls: (a) the same window on the 15th business day of the month; (b) S&P-only conditioning, our earlier test.
  - Success: the standard criterion on the pooled pairs, plus relative-performance conditioning beating S&P-only conditioning (paired difference t ≥ 1.5).
- **Scores:** evidence 3, persistence 2, fit 4, independence 4, data 4. Rule risk low. **Priority 6.**

### C7. JP225 first and last 30 minutes, conditioned on the prior-day S&P 500 return
- **Instruments:** JP225. Also a candidate for GER40 and STX50 using the same logic after the US session.
- **Evidence:** "How the prior day's S&P 500 returns influence the intraday returns of Nikkei 225 futures" (Elsevier journal, 2026):
  - When the previous day's S&P 500 return is higher, **returns in the first 30 minutes of Japanese trading are lower** (reversal) and **returns in the last 30 minutes are higher** (momentum) [EX].
  - The authors attribute the momentum to differences in investor rebalancing frequency and the reversal to temporary overreaction [EX].
  - Sample period and magnitudes n/s.
- **Our adaptation (pre-registered):**
  - `s` = S&P 500 close-to-close return of US day *t*−1, known at 16:00 ET.
  - **Leg A (reversal):** trade `−sign(s)` on JP225 from 09:00 to 09:29 JST, when |s| > 0.5 × its 20-day standard deviation.
  - **Leg B (momentum):** trade `+sign(s)` from 15:00 to 15:29 JST (14:30–14:59 before 5 Nov 2024).
- **Mechanism:** US news is priced overnight, first overreacting in Tokyo's open and then being worked in by slower rebalancers into the close. The other side: early-session liquidity providers, and closing-auction flows.
- **Counter-evidence:** a single new paper, sample n/s. Japan's close moved from 15:00 to 15:30 in Nov 2024 [EX].
- **Fit:**
  - ≈ 125 trades/yr per leg after the filter [D]. Gross n/s. Our JP225 cost is not in the brief.
  - Correlation: **low**, since the trading hours (19:00–20:30 ET the evening before, and 01:00–02:30 ET) are outside our US strategies.
- **Data:** our JP225 M1 from Apr 2024 only, about 2.4 years. The test has little power, so treat it as exploratory.
- **FundingPips rule risk: low.** JPY releases (e.g. Tokyo CPI) come at 08:30 JST, before the 09:00 open. Check BoJ days.
- **Pre-registered test:**
  - As above.
  - Control: the same legs on days with |s| below the filter.
  - Success: both legs' means have the predicted sign with t ≥ 1.5 (a lower bar because the history is short). Promote to live only after 12 more months out of sample.
- **Scores:** evidence 2, persistence 2, fit 2, independence 5, data 3. Rule risk low. **Priority 7.**

### C8. Month-end last-hour flow (intraday variant of C1)
- **Instruments:** SPX500, DJI30, NDX100.
- **Evidence:**
  - C1's excerpts say calendar predictability peaks in the last four days and "on the final day, it often flips" [EX].
  - NY Fed Liberty Street (22 Sep 2026): Treasury trading is increasingly concentrated on the **last trading day of the month** and around the **4 pm fixed-income index "strike" time**. A major index provider moved its strike from 3 pm to 4 pm in Jan 2021, and activity moved with it [EX]. That is bond-side evidence that month-end rebalancing concentrates at the close.
  - Press flow estimates as in C1 [EX].
- **Our adaptation (pre-registered):** on the last trading day of the month:
  - **Leg A:** trade *with* the expected rebalancing flow (short if `z > 0`, long if `z < 0`, with `z` from C1 computed at the previous close) from 15:00 to 15:58 ET.
  - **Leg B:** the "flip", taking the opposite position from 09:35 to 11:30 ET on the first trading day of the next month.
- **Mechanism:** market-on-close execution of pension and balanced-fund rebalancing, then a reversal when the price-insensitive flow ends.
- **Counter-evidence:** no direct intraday test was found. The "flip" wording suggests the flow may be absorbed *before* the last close.
- **Fit:** 12 trades/yr per index per leg; low frequency but nearly free to test. Independence is high.
- **Data:** as in C1.
- **FundingPips rule risk: low.** The first business day often has ISM at 10:00 ET inside Leg B. Hold through it, and do not open or close within ±5 min.
- **Pre-registered test:**
  - As above.
  - Control: Leg A's window on the second-to-last day.
  - Success: the standard criterion, except that the t threshold is 1.5 given n ≈ 120.
- **Scores:** evidence 2, persistence 3, fit 4, independence 4, data 5. Rule risk low. **Priority 8.**

### C9. Post-FOMC reversal in FX, 12–24 hours after the statement
- **Instruments:** EURUSD, USDJPY, GBPUSD, AUDUSD. Test XAUUSD separately.
- **Evidence:** Lee & Wang, "Jumps and Post-FOMC Announcement Returns in Currency Markets" (Review of Asset Pricing Studies 2025):
  - Post-FOMC currency returns are significantly low and **cancel about 65% of the positive pre-FOMC drift** [EX].
  - The reversal is realized **mostly 12–24 hours after** the announcement and is linked to resolution of uncertainty [EX].
  - Sample and magnitudes n/s.
- **Our adaptation (pre-registered):**
  - Let `d` = the currency pair's return from 14:00 ET the day before the FOMC day to 13:55 ET on the FOMC day (the pre-FOMC drift window).
  - Take `−sign(d)` from **02:05 ET** the day after the FOMC day (statement + ~12 h) to **13:55 ET** (statement + ~24 h).
- **Mechanism:** the risk premium earned before the announcement for bearing FOMC uncertainty is partly given back once the uncertainty is resolved.
- **Counter-evidence:** our own tests found that pre-FOMC drift in EURUSD and USDJPY is **gone** in 2025–26. If there is no pre-drift there may be nothing to reverse, so condition on `|d|` large.
- **Fit:** 8 events/yr, so **low frequency**. It pools across pairs but they are the same USD event. Gross n/s. Correlation low.
- **Data:** free (FOMC calendar at federalreserve.gov) and our FX bars.
- **FundingPips rule risk: low to medium.** The holding window often contains 08:30 ET releases (e.g. jobless claims on Thursdays). Holding is allowed and entries at 02:05 are far from releases. But the day-after window can include Fed speeches once the blackout ends at midnight after the meeting [EX], and FundingPips restricts speeches too.
- **Pre-registered test:**
  - As above.
  - Control: the same clock window one week later.
  - Success: mean sign as predicted with t ≥ 1.5 (n ≈ 8 × 10 years × 4 pairs, highly dependent), plus consistency across pairs. Given the low frequency, adopt only as a cheap add-on.
- **Scores:** evidence 3, persistence 2, fit 3, independence 4, data 5. Rule risk low to medium. **Priority 9.**

### C10. Leveraged-ETF rebalancing flow as a close-of-day conditioning variable
- **Instruments:** NDX100 (most LETF assets track the Nasdaq-100 and semiconductors), SPX500.
- **Evidence:**
  - LETFs must trade in the direction of the day's return at the close, in proportion to `AUM × L × (L−1) × r` (the standard rebalancing identity, summarized in the literature [EX]).
  - Shum et al. (Review of Finance 2016; 2006–2011): potential rebalancing is related to end-of-day volatility, largest on the most volatile days, but "not all economically significant" [EX].
  - Ivanov & Lenkey (JFM 2018; 2006–2014): fund **capital flows offset rebalancing**, and the late-day effect is economically insignificant [EX].
  - Barbon, Beckmeyer, Buraschi & Moerke (SSRN 3925725): LETF effects **decreasing significantly over time**, while the gamma effect persists. The LETF effect is **short-lived because it attracts liquidity provision** [EX].
  - A 2024 survey (AIMS QFE) says most LETF studies have "serious methodological errors" and economic effects look insignificant [EX].
- **What may have changed:**
  - Press, July 2026: daily LETF rebalancing flows reached a **record ~$50bn**, **~$10bn per 1% move** in June 2026, concentrated in semiconductor single-stock and sector funds [EX, press].
  - Zhao (arXiv 2608.03703, Aug 2026): speculators pre-positioning into the closing rebalances of new single-stock LETFs **in Korea in 2026** raised volatility sharply [EX].
- **Our adaptation (pre-registered):**
  - Estimate `F_t = Σ_i AUM_i(t−1) × L_i(L_i−1) × r_i(09:30→15:30)` over the largest Nasdaq-100 and S&P 500 LETFs (TQQQ, SQQQ, QLD, QID, SSO, SDS, UPRO, SPXU, plus SOXL/SOXS for semis).
  - Normalize by the index's average daily dollar volume.
  - Trade `sign(F_t)` from 15:30 to 15:58 ET only when |F_t| is in the top quintile. This is an **additional condition inside C2**, not a separate strategy.
- **Fit:** ~50 trades/yr [D]. Correlation with noise-area momentum: **high**, because it trades with the trend into the close.
- **Data:** partly free. Issuers publish current AUM and NAV. **Free historical daily AUM is hard to find** [EX]. Approximate with shares outstanding from issuer files if available, or with monthly snapshots.
- **FundingPips rule risk:** low.
- **Pre-registered test:** as C2's short-gamma branch, with top-quintile |F| as the condition and the same controls. Split the sample at 2025-12-31 to test whether the 2026 regime differs.
- **Scores:** evidence 2, persistence 2, fit 3, independence 2, data 2. Rule risk low. **Priority 10.**

### C11. BTCUSD/ETHUSD intraday time-series momentum (weekdays only)
- **Instruments:** BTCUSD, ETHUSD. FundingPips lists only these two coins.
- **Evidence:**
  - Shen, Urquhart & Wang ("Bitcoin intraday time series momentum", Financial Review 2022): the first half-hour positively predicts the last half-hour of the (UTC) day. Predictability is strongest when the first session has the highest volume or volatility, and gains are largest in downturns [EX].
  - Concretum Group (practitioner): a high-frequency BTC trend benchmark had a **gross Sharpe ≈ 1.6 over 2018–2025**, against ≈ 0.8 for vol-targeted buy-and-hold [EX, PR]. The strongest performance is from **Sunday evening NY into Monday** ("Monday Asia open") [EX, PR], which **we cannot use on Master accounts** because weekends are restricted.
- **Our adaptation (pre-registered):** UTC-day version: `r_1` = 00:00–00:30 UTC return; trade `sign(r_1)` from 23:30 to 23:59 UTC, Monday to Thursday only (flat Friday by the close).
- **Mechanism:** trend-following and liquidation flows in a 24/7 market with leveraged perpetual futures. The other side: liquidity providers and funding-rate arbitrageurs.
- **Counter-evidence:** peer-reviewed sample ends around 2020 [EX]; post-publication evidence is practitioner only. Weekday-only trading removes the best-documented window.
- **Fit:**
  - ~200 trades/yr per coin [D].
  - Costs are **higher and uncertain**: commission = lot × price × 0.04% (whether per side or round trip is n/s) plus spread [EX].
  - Evaluation leverage 1:2; max 1 lot per click [EX].
  - Correlation: *medium* with NDX momentum.
- **Data:** we hold no crypto data. Free exchange 1-minute data is widely available; the Binance public API also offers perpetual funding history since 2019 [EX]. Measure the FundingPips CFD spread directly.
- **FundingPips rule risk: medium** (weekend restriction on Master; crypto margin at 1:2 in evaluation).
- **Pre-registered test:**
  - As above, 2019–2026.
  - Control: the same last-30-minute window with the sign drawn from the 12:00–12:30 UTC return.
  - Success: the standard criterion after FundingPips crypto costs.
- **Scores:** evidence 2, persistence 3, fit 2, independence 3, data 3. Rule risk medium. **Priority 11.**

### C12. Overnight drift after US sell-offs (conditional European-open drift)
- **Instruments:** SPX500, NDX100.
- **Evidence and decay:**
  - Boyarchenko, Larsen & Whelan ("The Overnight Drift", RFS; NY Fed SR 917): a large US equity-futures return from **02:00 to 03:00 ET** (the European open). It is strongly **negatively related to the previous day's end-of-day order imbalance**, so sell-offs are followed by robust overnight reversals, with a weaker effect after rallies [EX].
  - **But:** the same authors (NY Fed Liberty Street, 1 Jul 2026, "The Disappearing Overnight Drift") find that the window "previously generated roughly 3.7 percent per annum" and "has averaged **close to zero since 2021**" [EX].
- **Why it is still a card:** our rejection covered the *unconditional* European-open drift. The **conditioning variable** (prior-day sell-off, i.e. a late-day negative return or order imbalance) is new and cheap to test on our data. The authors' 2026 post examines which channel (closing-imbalance dispersion, return variance, or liquidity providers' risk-bearing capacity) explains the fade, so read it first.
- **Our adaptation (pre-registered):** if the 15:00–16:00 ET return on day *t* is in the bottom quintile of its trailing 250-day distribution, go long from 02:00 to 02:59 ET on day *t*+1.
- **Fit:** ~50 trades/yr [D]. Gross (unconditional, pre-2021) ≈ 1.5 bps/day [D: 3.7%/252]. Now ≈ 0 unconditionally [EX]. Holding from 02:00 to 03:00 involves no swap. Independence high.
- **Data:** own M1 bars.
- **FundingPips rule risk: low.** The window can overlap European data releases (e.g. German data at 02:00 ET), so check the red events.
- **Pre-registered test:**
  - As above.
  - Control: the same window after top-quintile (rally) days.
  - Success: the standard criterion, **including the last-24-months condition**, which is the real hurdle here.
- **Scores:** evidence 4 (for the original), persistence 1, fit 4, independence 4, data 5. Rule risk low. **Priority 12 (falsification check only).**

---

## 4. Screened list (40 candidates)

Kept means it has a full card above. For each dropped candidate the reason is given in one line.

| ID | Candidate | Verdict | One-line reason |
|---|---|---|---|
| C1 | 60/40 month-end rebalancing front-run | **Kept (P1)** | Forced flow, new strong evidence, independent of intraday momentum. |
| C2 | Gamma-conditioned last-30-min momentum/reversal (US) | **Kept (P2)** | Mechanism plus free GEX conditioning; reversal branch diversifies. |
| C3 | Non-US cash-session intraday momentum | **Kept (P3)** | Documented in most developed markets; sessions separate from our US trades. |
| C4 | Treasury-auction pressure transmitted to USDJPY, gold, NDX | **Kept (P4)** | Rates effect documented to 2024; cross-asset effect untested, so a cheap, high-frequency test. |
| C5 | CO-OC reversal on indices | **Kept (P5)** | Cross-asset evidence; likely diversifying; rule clarification needed first. |
| C6 | FX month-end hedge rebalancing on relative equity performance | **Kept (P6)** | The brief's requested new conditioning variable; weaker post-2015 evidence. |
| C7 | JP225 conditional on prior S&P return | **Kept (P7)** | New 2026 paper; fully independent hours; short data history. |
| C8 | Month-end last-hour flow and next-day flip | **Kept (P8)** | Nearly free variant of C1; bond-side 2026 evidence of close concentration. |
| C9 | Post-FOMC FX reversal at 12–24 h | **Kept (P9)** | Peer-reviewed 2025; low frequency; our pre-FOMC FX drift has faded. |
| C10 | LETF flow conditioning at the close | **Kept (P10)** | Historic effect decayed, but 2026 flows are record size; use inside C2. |
| C11 | Crypto intraday momentum (weekdays) | **Kept (P11)** | Some evidence; costs and weekend rule weaken it. |
| C12 | Overnight drift after sell-offs | **Kept (P12)** | Authors report it gone since 2021; cheap falsification of the conditional version. |
| S13 | Unconditional market intraday momentum (Gao et al.) | Merged into C2 | Used as C2's control. The unconditional US effect has weakened (Komarov 2017). |
| S14 | FX fixing "W" pattern (Krohn, Mueller & Whelan, JF 2024; ~2 bps/day swing) | Dropped | Unconditional time-of-day FX pattern, already rejected on our data. FCA: London-fix reversals gone from 2015. |
| S15 | US overnight vs intraday premium | Dropped | Already rejected; no new conditioning variable found beyond C5 and C12. |
| S16 | BoJ ETF afternoon support after down mornings | Dropped | The mechanism ended: BoJ made no ETF purchases even on slumps in 2024 [EX]. |
| S17 | Crude-oil intraday momentum (Wen et al. 2021) | Dropped | USO 2006–2018 timing strategy made 1.85%/yr [EX], too small against a 4.8 bps oil cost; oil data only from Nov 2024. |
| S18 | OPEC+ meeting trades | Dropped | News-driven (news-spike rule risk), ~6–12 events/yr, oil costs high. |
| S19 | WTI roll-period ("Goldman roll") pressure | Dropped | No post-2015 evidence found; CFD roll handling unclear. |
| S20 | FX intraday momentum (Elaut et al. 2018, RUB/USD exchange) | Dropped | Exchange-traded RUB with a daily close, not 24 h G10 FX; FX noise-area momentum already rejected. |
| S21 | FX post-macro-news drift (enter after the first minutes) | Dropped | Excerpts indicate little post-announcement drift in FX; high news-rule risk. |
| S22 | CNY fixing surprise → AUD/NZD in Asia | Dropped | Only market commentary found, no study. |
| S23 | FX option-expiry pinning at the 10:00 NY cut | Dropped | Commentary only; DTCC data would make it testable but no evidence was found. |
| S24 | COMEX gold option-expiry pinning | Dropped | Practitioner claims only. |
| S25 | Shanghai Gold Exchange premium → gold in the Asian session | Dropped (untested idea) | Plausible demand signal, but no study found; SGE data is public. |
| S26 | Silver–gold lead–lag | Dropped | 15-minute evidence is old (silver carries the adjustment [EX]); silver cost 2.7 bps. |
| S27 | Gold vs real yields at intraday horizons | Dropped | No lead–lag evidence at 1–4 h was found; the relation is contemporaneous. |
| S28 | Vol-control and risk-parity deleveraging flows | Dropped | Multi-day and path-dependent; no academic return evidence found. |
| S29 | Fed blackout and Fed speeches | Dropped | Effects documented at weekly horizons (Neuhierl & Weber); speeches are restricted news for Master. |
| S30 | Treasury quarterly refunding announcements | Dropped | 4 events/yr. |
| S31 | Index reconstitutions (S&P quarterly, NDX annual, Russell semi-annual from 2026) | Dropped | Stock-level effects; no index-level direction documented; overlaps rejected opex days. |
| S32 | Tokyo lunch break | Dropped | Only volatility patterns are documented, no return predictability. |
| S33 | Crypto "Monday Asia open" and weekend effects | Dropped | Weekend holds not allowed on Master (temporary rule since Jan 2026); gap-trading ban. |
| S34 | Crypto perpetual funding-time effects (00/08/16 UTC) | Dropped | No study found. |
| S35 | CME bitcoin futures weekend gap | Dropped | Weekend plus gap-trading ban. |
| S36 | Opening-range breakout on GER40/UK100 | Dropped | Practitioner only; overlaps C3 and NDX momentum. |
| S37 | Same-slot intraday seasonality (Heston–Korajczyk–Sadka; Schlie & Zhou 2026) | Dropped | Stock-level; the US effect has weakened [EX]. |
| S38 | Cross-sectional end-of-day stock reversal (Baltussen, Da & Soebhag) | Dropped | Needs single stocks, which we cannot trade (0.24%/day long-short [EX]). |
| S39 | Multi-day FX and metals strategies under the Swap-Free add-on | **Kept as a structural note** | Not a new edge: re-run previously rejected multi-day FX and gold tests at $10/lot and zero swap (see §1.2). |
| S40 | Gold last-30-min momentum before COMEX settlement | Dropped | Overlaps the rejected gold noise-area momentum; no free gold-options gamma for conditioning. |

(Also considered and merged: VIX-term-structure conditioning goes into C2 as a secondary variable; macro-news-day conditioning into C2, following Gao et al.; the index opening-gap fade into C5; the US lunch-time reversal into C2's long-gamma branch; Nikkei and USDJPY minute-level lead–lag was dropped because the only price-discovery work found concerns Nikkei futures venues, where CME leads SGX and OSE [EX].)

---

## 5. What I could not verify, and what to check first

1. Full texts of every [EX] number, especially C1 (δ and the exact signal), C2 (conditional magnitudes and post-2015 subsamples), C3 (per-market Sharpe ratios) and C4 (magnitudes).
2. Whether FundingPips' dashboard calendar marks Treasury auctions or FOMC press conferences as red (C4, C2, C9).
3. FundingPips' definition of "gap trading" (C5).
4. Whether our MT5 server time is ET + 7 h all year or a fixed UTC+3; this affects every window above.
5. The index-CFD swap rates for daily holds (C1's daily version).
