# Free data sources for testing the candidates

Workstream C. Compiled 2026-09-25.

> **Access caveat.** Direct access to most of these sites (FRED, CBOE, CFTC, TreasuryDirect, Kaggle, SqueezeMetrics, Stooq) was **blocked** in this session, so nothing was downloaded or inspected here. Coverage, format and timing come from search-index excerpts of the official pages or dataset cards, marked [EX]. Anything not seen is marked **n/s**.
> Before first use, open each source and confirm: start date, time zone, whether values are revised, and the licence.

## Summary table

| # | Data | Source (URL) | Coverage start | Frequency and format | Timestamps | Point-in-time? | Licence and terms | Used by |
|---|---|---|---|---|---|---|---|---|
| 1 | **Economic calendar with actual, forecast and previous** | ForexFactory-derived: (a) Kaggle "Forex Factory Economic Data Entire Dataset" https://www.kaggle.com/datasets/randelltsen/forex-factory-entire-dataset-till-2024-08-16; (b) Hugging Face `Ehsanrs2/Forex_Factory_Calendar` https://huggingface.co/datasets/Ehsanrs2/Forex_Factory_Calendar; (c) GitHub `janickfarrell/newfac` rolling CSV release https://github.com/janickfarrell/newfac/releases/tag/calendar-data | (a) 2007-01-01 to 2024 [EX]; (b) 2007-01-01 to 2025-04-07 [EX]; (c) 2007-01-01 to today, refreshed daily at 00:10 UTC [EX] | Event rows: date, time, currency, impact, event, actual, forecast, previous [EX]; CSV | (b) ISO timestamps with offset, e.g. `2007-01-01T04:30:00+03:30`, scraped in the Asia/Tehran zone [EX]; (c) **GMT**, 24-h, set by FF's `fftimezone` cookie [EX]; (a) n/s | **Partly.** "Actual" is the first print as shown on FF (check whether later pages overwrite it). "Previous" shows the revised prior value. "Forecast" is FF's consensus, not Bloomberg's | (b) MIT licence on the dataset card, "educational and research purposes", check FF's policies before redistribution [EX]; (a) n/s; (c) n/s; FF's own terms apply | News filter; conditioning (Gao et al. news days); FundingPips rule checks |
| 2 | **CFTC Commitments of Traders**: Legacy, Disaggregated, **Traders in Financial Futures (TFF)** | https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm; historical compressed files https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm; API via the Public Reporting Environment https://publicreporting.cftc.gov/ | Legacy from **15 Jan 1986**; TFF and Disaggregated from **13 Jun 2006**; yearly compressed files from Sep 2009 [EX] | Weekly; CSV, TSV, XML via API; zipped yearly text files | Positions as of **Tuesday**; **released Friday 3:30 p.m. ET**, later around holidays [EX] | Released with a 3-day lag. Use the release time, not the Tuesday date, to avoid look-ahead | US government, public domain | 4 h model features (positioning), multi-day ideas |
| 3 | **Dealer gamma (GEX) and DIX** | SqueezeMetrics https://squeezemetrics.com/monitor/dix; guide https://squeezemetrics.com/monitor/static/guide.pdf; GEX white paper https://squeezemetrics.com/monitor/download/pdf/white_paper.pdf | **2011** [EX] | Daily CSV (`DIX.csv`): date, S&P 500 close, DIX, GEX [EX] | Date = trading day. The file updates **around 05:30 ET the next morning** [EX, third-party]. Use GEX(t−1) for day *t* | Model output, not a market price. Methodology changes may restate history (n/s) | Free download; terms n/s. Methodology is proprietary: its assumptions about who holds which options are in the white paper, which was not re-read in this session | C2, C10 |
| 4 | **VIX, VIX9D, VIX3M, VVIX** | Cboe historical data page https://www.cboe.com/tradable-products/vix/vix-historical-data; direct CSV pattern `https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv` (VVIX: `VVIX_History.csv`) [EX] | VIX **Jan 1990** (OHLC only from Jun 2004; earlier rows repeat the close) [EX]; VVIX **3 Jan 2007**, close only [EX]; VIX9D and VIX3M: n/s | Daily OHLC CSV | US/Eastern trading date; the exact close convention was n/s (check) | Not revised | Cboe terms of use (free download) | C2 conditioning; 4 h model |
| 5 | **Nominal and real US yields** | FRED: `DGS10` https://fred.stlouisfed.org/series/DGS10, `DGS2`, `DFII10` (10-y TIPS real yield) https://fred.stlouisfed.org/series/DFII10, `T10YIE` (breakeven) | `DFII10` from **2003-01-02** [EX]; `DGS10` long history (start n/s) | Daily; CSV, XLS and API (free API key) | H.15 end-of-day values; one value per US business day, available **after** the day (use t−1 intraday) | Market series are not revised in normal practice. Use **ALFRED** (https://alfred.stlouisfed.org/) to download vintages "as they existed" on a date [EX] | FRED terms; H.15 is public domain | C1 (bond leg proxy), C4, 4 h model |
| 6 | **Treasury auction schedule and results** | U.S. Treasury Fiscal Data, "Treasury Securities Auctions Data" https://fiscaldata.treasury.gov/datasets/treasury-securities-auctions-data/; API docs https://fiscaldata.treasury.gov/api-documentation/; upcoming auctions https://fiscaldata.treasury.gov/datasets/upcoming-auctions/ | **15 Nov 1979** onward [EX] | Per auction; JSON or CSV via the open API (**no key or registration**) [EX] | Dates in ET. Closing times differ by security: **competitive bids mostly 1:00 p.m. ET for notes and bonds, 11:30 a.m. ET for many bills** [EX, TreasuryDirect]. Read each auction's own close time where the dataset gives it | Results are final once published | US government, public domain | C4 |
| 7 | **FOMC calendar, blackout, Fed speeches** | FOMC calendars https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm; blackout policy https://www.federalreserve.gov/monetarypolicy/files/FOMC_ExtCommunicationStaff.pdf and blackout calendar https://www.federalreserve.gov/monetarypolicy/files/fomc-blackout-period-calendar.pdf; speeches by year e.g. https://www.federalreserve.gov/newsevents/2026-speeches.htm | Current FOMC calendar page lists 2021 onward plus future years [EX]; older years in the Fed's historical materials (n/s); speeches pages per year | HTML and PDF lists; scrape to CSV | ET. **Blackout: from 00:00 ET on the second Saturday before a meeting to 23:59 ET on the day after the meeting** [EX] | Historical lists are final (speech times need care: some pages list only dates) | Public domain | C2 (exclude FOMC days), C9, news filter |
| 8 | **Index rebalance calendars** | S&P quarterly rebalance (effective after the close on the **third Friday** of Mar, Jun, Sep, Dec) [EX]; Nasdaq-100 annual reconstitution (announced after the close on the **6th trading day before** the effective date, effective at the open on the first trading day after the **third Friday of December**) https://indexes.nasdaq.com/docs/Methodology_NDX.pdf [EX]; Russell US indexes **semi-annual from 2026** (4th Friday of June, and from 2026 the 2nd Friday of December) https://www.lseg.com/en/ftse-russell/russell-reconstitution [EX] | Rules published; derive the dates from the rules | Rule-based; build the calendar yourself | ET, after the close | n/a | Public methodology documents | S31 (screened out); avoid these closes in C2 and C8, or mark them as special |
| 9 | **Options expiries** | Standard monthly equity-index options expire on the **third Friday**, which coincides with the S&P quarterly rebalance dates above [EX]. SPX daily (0DTE) expiries exist in the 2022+ regime studied by Dim, Eraker & Vilkov [EX] | n/a | Rule-based | ET | n/a | — | C2 (flag monthly opex, since opex effects were already rejected) |
| 10 | **OPEC+ meetings** | OPEC press room, e.g. https://www.opec.org/pr-detail/590-1-february-2026.html. JMMC meets **every two months**; the OPEC and non-OPEC Ministerial Meeting **every six months** [EX] | Press releases archive | HTML; scrape dates | Vienna time (CET/CEST); many meetings by videoconference | Announcements can be rescheduled at short notice | Public | S18 (screened out) |
| 11 | **Foreign equity index daily closes** (for C6's relative-performance signal) | Stooq free database https://stooq.com/db/ (e.g. `^DAX`, `^UK100` tickers) [EX]; FRED `NIKKEI225` https://fred.stlouisfed.org/series/NIKKEI225; FRED `SP500` (10 years only) [EX] | Stooq: long histories (n/s per ticker); FRED SP500 limited to **10 years** [EX] | Daily CSV (Stooq also offers hourly and 5-min for some symbols [EX]) | Local exchange close dates | Not revised | **Nikkei via FRED:** research use allowed, redistribution needs Nikkei Inc. permission [EX]. **S&P via FRED:** copyrighted, pre-approval required for reuse [EX]. Stooq: terms n/s | C6, C7 |
| 12 | **Leveraged-ETF AUM and flows** | Issuer pages, e.g. ProShares TQQQ https://www.proshares.com/our-etfs/leveraged-and-inverse/tqqq (current NAV and AUM) | **Free historical daily AUM is hard to find** [EX]; prices are free (Nasdaq, Yahoo) | HTML and PDF fact sheets | Daily NAV as of 16:00 ET | n/a | Issuer terms | C10 (rough monthly snapshots may be the only free option) |
| 13 | **Crypto funding rates** (context for C11, S34) | Binance USDⓈ-M futures API `GET /fapi/v1/fundingRate` https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History | BTCUSDT records back to **Sep 2019** [EX] | JSON; up to 1,000 rows per call; limit 500 requests / 5 min / IP [EX] | `fundingTime` in epoch milliseconds (UTC) | Final | Public endpoint, free, no key [EX]; Binance API terms | C11 |
| 14 | **US Treasury trading around month-end strike times** (context) | NY Fed Liberty Street, "Treasury Trading at the Close" (22 Sep 2026) https://libertystreeteconomics.newyorkfed.org/2026/09/treasury-trading-at-the-close/ | Article | — | — | — | — | C8 (supports the 4 pm ET strike time since Jan 2021 [EX]) |

## Notes and pitfalls by source

### 1. Economic calendar (ForexFactory-derived)
- **Completeness:** all three datasets start in 2007 [EX], which covers our 2015+ M1 history. The Kaggle file stops in 2024 [EX]. The Hugging Face file stops in April 2025 [EX]. The GitHub release is refreshed daily [EX], so it is the one to keep current.
- **Time zones:** ForexFactory shows times in the viewer's selected zone. The files therefore differ: one is **GMT** [EX] and one is **Asia/Tehran with an explicit offset** [EX].
  - Before use, spot-check known events: US non-farm payrolls at 08:30 ET, FOMC statements at 14:00 ET, ECB decisions at their announced CET times.
  - Check that the DST transitions in March, October and November come through correctly.
- **Point-in-time issues:**
  - FF's **forecast** is a consensus compiled by FF; it can differ from Bloomberg or Reuters consensus.
  - **Actual** may be overwritten when the agency revises the number. Check a few events against the agencies' original releases, e.g. via ALFRED vintages for US data.
  - The **impact colour** is FF's classification, which may not equal **FundingPips' dashboard calendar**, the calendar that defines restricted red events [FundingPips help centre, EX]. Keep a mapping and treat FundingPips' list as authoritative for rule checks.
- **Licence:** scraping FF is subject to FF's terms. Use these files internally for research only.

### 2. CFTC COT
- Use the **release time** (Friday 15:30 ET) as the availability time. Holiday weeks shift the release [EX].
- TFF (dealer, asset manager, leveraged funds, other) is the right split for financial futures: FX, equity index and rates.

### 3. SqueezeMetrics GEX
- GEX is a **model estimate** built on assumptions about who is long and short options. Academic papers use their own gamma measures (e.g. Baltussen et al. from option open interest), so the proxy is imperfect.
- Use only values available **before** the trading decision (GEX(t−1) at 05:30 ET).
- Rank-based conditioning (quintiles over a trailing window) is safer than sign-based, because the level shifts with index level and option volume.

### 4. Cboe volatility indices
- The history files are the official source; third-party copies (Yahoo, datahub.io, Kaggle) exist as backups [EX].
- VIX OHLC before June 2004 repeats the close [EX], which matters only for pre-2004 research.

### 5. FRED and ALFRED
- `DFII10` starts 2003-01-02 [EX]. `DGS10` and `DFII10` come from the H.15 release.
- For macro series such as payrolls and CPI, use **ALFRED** vintages to build point-in-time features. Vintage dates approximately equal release dates [EX].

### 6. Treasury auctions
- The Fiscal Data API is open (no key) [EX].
- Use the **auction date plus the competitive-bid close time**. For the C4 test, restrict to coupon auctions with a 13:00 ET close and verify the times from the per-auction announcement PDFs on TreasuryDirect when in doubt [EX].

### 7. Fed calendars
- Blackout windows can be generated from the FOMC dates with the rule in the table [EX].
- Speech *times* are needed for the ±5 min rule. The Board's calendar pages list events by date and often by time. Regional Fed speeches are on the regional banks' sites. Build the list from both and treat it as incomplete.

## Data we could not find for free
- **Historical intraday data for GER40, UK100 and JP225 before our MT5 history begins.** Stooq offers intraday bars only for recent periods [EX], so C3 and C7 will be tested on short samples.
- **Historical daily LETF AUM** (for C10) [EX].
- **Option open interest by strike** for our own gamma estimates. OptionMetrics and Cboe DataShop are paid, so SqueezeMetrics is the free proxy.
- **WM/Reuters fixing rates and LBMA gold prices:** licensed benchmarks. Not verified in this session, so not listed as free.
