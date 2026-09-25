# FundingPips rules that matter for an automated multi-strategy system

Workstream D. Compiled 2026-09-25.

> **Source caveat.** `help.fundingpips.com` and `fundingpips.com` were **blocked** by this session's network policy. Everything in §1 comes from search-engine excerpts of the **official help-centre pages** linked beside each item: close to the official text, but read through a search summary. Treat the items as highly likely but **verify on the pages** before relying on them, especially anything marked ⚠.
> §3 holds third-party and trader reports and is kept separate on purpose.

Main official pages (all on help.fundingpips.com):
- 2 Step Flex: https://help.fundingpips.com/hc/en-us/articles/47835196271249-2-Step-Flex
- News Trading & Weekend Holding: https://help.fundingpips.com/hc/en-us/articles/34504137479441-News-Trading-Weekend-Holding
- Trading Conduct and Security Standards: https://help.fundingpips.com/hc/en-us/articles/34505029138449-Trading-Conduct-and-Security-Standards
- Risk Per Trade Idea: https://help.fundingpips.com/hc/en-us/articles/48174287980177-Risk-Per-Trade-Idea
- Responsible Trading Policy: https://help.fundingpips.com/hc/en-us/articles/47328410434065-Responsible-Trading-Policy
- Understanding Trading Mechanics: https://help.fundingpips.com/hc/en-us/articles/44559256768529-Understanding-Trading-Mechanics
- Get Started (instruments, commissions): https://help.fundingpips.com/hc/en-us/articles/44390730743825-Get-Started
- Trade Copier: https://help.fundingpips.com/hc/en-us/articles/49580068780817-Trade-Copier
- Compare Account Models: https://help.fundingpips.com/hc/en-us/articles/48368490585105-Compare-Account-Models

---

## 1. Official rules (help centre, via search excerpts)

### 1.1 2-Step Flex account parameters
| Item | Rule | Page |
|---|---|---|
| Targets | Phase 1 **10%**, Phase 2 **6%** | 2 Step Flex |
| Time limit | None, as long as at least one trade is completed every 30 days | Understanding Trading Mechanics |
| Minimum trading days | **1** for the 85% split option; the 95% option needs **3 profitable days of ≥ 0.5% each** | 2 Step Flex |
| Daily loss limit | **4%** of the higher of the day's opening balance and opening equity. Equity may not fall more than 4% below that baseline at any point in the day, **floating P&L included** | 2 Step Flex |
| Daily reset | **00:00 "Platform Time (UTC+3)"** ⚠ see §1.2 | 2 Step Flex |
| Max loss | **12% of the starting balance**, a static floor that never moves. It applies in both phases and on the Master account, floating losses included | 2 Step Flex |
| Inactivity | 30 days. Only **completed** trades (opened and fully closed) count; an open position does not reset the clock | 2 Step Flex |
| FX leverage | **1:100** (highest of the models) | 2 Step Flex |
| Crypto leverage | **1:2** during evaluation, described as temporary | 2 Step pages |
| Master leverage for metals, energies and indices | **Dynamic, per position:** the first 0.05 lots at 1:50, then stepping 1:30 → 1:25 → 1:20 → 1:10, with any volume **above 0.50 lots at 1:5** | 2 Step pages |
| Account sizes | $5k, $10k, $25k, $50k, $100k | 2 Step Flex |
| Rewards | Bi-weekly; **85%** split (1 min trading day) or **95%** split (3 profitable days ≥ 0.5%) | 2 Step Flex |

### 1.2 Server time and the daily reset ⚠
- The official pages say the daily loss limit resets at **00:00 Platform Time (UTC+3)** [2 Step Flex and other model pages].
- The brief says the server runs at **New York + 7 h**. That equals UTC+3 in US summer time but **UTC+2** in US winter time.
- If the platform stays at UTC+3 all year, the reset moves to **16:00 ET in US winter** instead of 17:00 ET. Many MT5 servers use GMT+2/GMT+3 with US daylight-saving switching, so both readings are plausible.
- **Action:** confirm in MT5 by comparing `TimeTradeServer()` with UTC on a date in each daylight-saving regime (e.g. a January and a July bar), and set every strategy window from that result.

### 1.3 Automation (Expert Advisors)
- **Default rule:** third-party EAs are permitted **only as a trade or risk manager** [Trading Conduct and Security Standards].
- **Personal EA:** if the EA is your own, **full automation is permitted with proof of ownership**. Acceptable proof includes source code, version-control history, development-environment evidence, or explaining the EA's logic on a live call. **A compiled binary alone is not proof** [Trading Conduct and Security Standards].
- **Exceptions:** third-party EAs and copiers are allowed on the 1K Instant account; **all EAs are prohibited** in the Monthly Competition.
- **Implication:** keep the strategy code in version control with dated commits and be ready to explain the logic. Do not run anyone else's EA as the signal source.

### 1.4 Prohibited practices (termination offences)
- The official list [Trading Conduct and Security Standards]: **gap trading, high-frequency trading, server spamming, latency arbitrage, toxic trading flow, hedging, long-short arbitrage, reverse arbitrage, tick scalping, server execution exploits, opposite account trading, and churning and burning.**
- Clear breaches can lead to termination without notice.
- ⚠ **"Gap trading" and "tick scalping" are not defined** in the excerpts. No minimum trade duration was found in the "Understanding Trading Mechanics" page.
- Ask support in writing:
  - whether fading an opening gap *after* the open is allowed (candidate C5);
  - whether trades held for only a few minutes count as tick scalping (candidates C2, C3, C8 hold 28–58 minutes).
- **Hedging:** "hedging" is prohibited. Holding opposite positions in *correlated* instruments, e.g. C4's long USDJPY with short gold, is not obviously hedging, but a long and a short **on the same instrument** must never coexist. Netting logic must enforce this.
- **Multiple accounts:** trading the same direction across your own accounts is allowed. **Coordinated hedging across accounts** ("opposite account trading") is not.

### 1.5 News rules
- **Official source:** the **Economic Calendar on the FundingPips dashboard**. Only **red (high-impact)** events are restricted [News Trading & Weekend Holding].
- **All phases:** *purposely* trading news and **speeches**, meaning deliberately opening or closing positions around high-impact news to exploit the volatility, is prohibited and leads to account closure.
- **Evaluation:** no other news restrictions. Trades may be **held and managed** through news.
- **Master (1 Step Flex, 2 Step Standard, 2 Step Flex, 2 Step Pro):**
  - Profits from trades **opened or closed within 5 minutes before to 5 minutes after** restricted high-impact news **or speeches** on the **affected currency** may be deducted.
  - **Exemption:** trades opened **≥ 5 hours before** the event may be closed inside the window with the profit counting.
  - Only the affected currency is restricted.
- ⚠ One excerpt also mentions a **10-minute** window in which positions may not be opened, closed **or held**. It appears to belong to **FundingPips Zero**, whose Master account forbids holding, opening or closing during restricted news. Confirm that the 5-minute rule is the one that applies to 2 Step Flex Master.
- **Implication:**
  - Add a calendar filter that blocks entries and exits in [t−5 min, t+5 min] around red events for the traded currency. For index CFDs, map to USD for US indices, EUR for GER40/STX50, GBP for UK100, JPY for JP225 (an assumption; ask support how indices are mapped).
  - Treat Fed **speeches** (including FOMC press conferences) as restricted.

### 1.6 Weekend holding
- **Evaluation (2 Step Flex):** weekend holds are **permitted for all instruments**.
- **Master:** since **29 January 2026** a temporary change bars weekend holds on the 2 Step Flex Master and other standard models, **crypto included**.
  - Open trades are **closed automatically** before the weekend. This is **not a hard breach**, but the day does not count as a valid trading day.
  - Profits still count, and the day's biggest win or loss enters the **consistency score** [News Trading & Weekend Holding].
- **Implication:** every strategy must be flat by Friday's close on Master. Multi-day strategies that span weekends need a Friday exit and Monday re-entry rule.

### 1.7 Master-account risk rules
- **Risk Per Trade Idea** [Risk Per Trade Idea]:
  - For Master accounts above $25k, the maximum **combined realized and unrealized loss** on one trade idea is **2% of the Master account size**. One excerpt refers to "2% / 3%" limits; the 3% presumably applies to smaller sizes (⚠ verify).
  - **Hard breach:** the account is locked, trades are closed and the account becomes view-only.
  - The limit does **not** apply during the evaluation.
- **What counts as one trade idea:**
  1. positions open **at the same time on the same instrument in the same direction**;
  2. **any new same-direction position opened within 10 minutes of closing a losing trade** on that instrument, which joins the losing idea;
  3. profits from other trades **do not offset** the idea's losses.
- **Striking system (warnings):**
  - A strike is recorded when one idea's loss reaches **1.2%** of the Master size (2 Step Standard) or **1% floating** (1 Step Flex). The 2 Step Flex threshold was not seen ⚠.
  - **Profit from ideas that received a warning is deducted**, and warnings accumulate across reward cycles.
- **Implications for our system:**
  - Per-idea risk must be capped well below 2%, and below the strike threshold if one applies to 2 Step Flex.
  - Stop-loss placement must include slippage and the widening of spreads at news [Understanding Trading Mechanics].
  - Any re-entry logic needs a **≥ 10-minute cool-down after a losing exit** in the same direction, or it must budget the combined loss.
  - Strategies that pyramid or scale into the same instrument are one idea for the 2% cap.

### 1.8 Profit concentration and consistency
- **Profit Concentration Policy (evaluation):** if a **single trade idea is more than 60% of a phase's profit target**, the Master account then requires **4 minimum profitable days before each reward** [Responsible Trading Policy / risk-framework excerpts].
- **Consistency:** for **On-Demand Rewards**, a **35% consistency score** is required: no single day may exceed 35% of total profit. Whether this applies to 2 Step Flex bi-weekly rewards was not seen ⚠.
- **Responsible Trading Policy:** treat simulated capital as your own stake. Avoid excessive leverage and overexposure. "Churning and burning" accounts is not allowed.

### 1.9 Order and position limits
- **20 lots per trade**, a hard platform limit.
- **Crypto: 1 lot per click.**
- No maximum number of open positions was seen in the excerpts ⚠.

### 1.10 Allocation, multiple accounts and copying
- **Total allocation cap: $400k**, shared across all active evaluation, Master and Prime accounts [Trading Conduct and Security Standards].
- Copying trades between **different users' accounts is prohibited**.
- Copying **into** a FundingPips account from any outside source (signal providers, copiers with FundingPips as the slave) is **prohibited** and treated as third-party account management.
- Copying **from** a FundingPips account to outside accounts is allowed. The Trade Copier beta allows up to 4 accounts, with a FundingPips account as the lead [Trade Copier].
- **Implication:** run each account from our own EA instance rather than copying into it. Copying our own FundingPips master account *outward* to our other FundingPips accounts in the same direction appears allowed; confirm it.

### 1.11 Costs
| Class | Commission | Swaps | Page |
|---|---|---|---|
| FX and metals | **$5/lot** (standard, 4 evaluation models); **$10/lot with the Swap-Free add-on** | Charged at rollover. **Removed** for FX and metals with the Swap-Free add-on | Get Started |
| Indices and energies | **None** | Charged (the add-on does **not** remove them) | Get Started |
| Crypto | **lot size × price × 0.04%** (e.g. 1 lot ETH at $2,600 = $1.04). Per side or round trip n/s ⚠ | Charged | Get Started |
| Prime accounts | $10/lot flat except crypto | — | Get Started |

- **Swap-Free add-on:**
  - Available on **MT5 only**, chosen **at purchase**, for **FX and metals only**.
  - It raises the FX/metals commission from $5 to $10/lot and **removes swaps on FX and metals**.
  - **Consequence:** multi-day FX and gold strategies previously rejected because of swaps should be re-tested at an extra ~$5/lot round trip (≈ 0.45 bps on EURUSD at 1.10, derived: $5 / $110,000).
  - It also removes any **positive** carry.
- Spreads are variable and shown in the platform. The help centre gives no official spread table [Get Started / third-party].

### 1.12 Symbol list (official "Get Started" excerpt)
| Class | Symbols |
|---|---|
| FX majors (7) | EURUSD, GBPUSD, USDJPY, USDCHF, USDCAD, AUDUSD, NZDUSD |
| FX crosses (21) | AUDCAD, AUDCHF, AUDJPY, AUDNZD, CADCHF, CADJPY, CHFJPY, EURAUD, EURCAD, EURCHF, EURGBP, EURJPY, EURNZD, GBPAUD, GBPCAD, GBPCHF, GBPJPY, GBPNZD, NZDCAD, NZDCHF, NZDJPY |
| Metals (2) | XAUUSD, XAGUSD |
| Indices (7) | DJI30, **FTSE100** (our "UK100"), GER40, JP225, NDX100, SPX500, **STX50** |
| Energies (2) | UKOIL (Brent), USOIL (WTI) |
| Crypto (2) | BTCUSD, ETHUSD |

- **Not offered:** FRA40, AUS200 and HK50 are **not** in the list, so the brief's optional indices are unavailable except STX50.
- **Trading hours, contract sizes and swap rates** are shown per symbol **inside the platform**. They are not published in the help centre excerpts, so export them from MT5 `SymbolInfo*` for each symbol.

---

## 2. Checklist for an automated multi-strategy system
1. **Code ownership:** keep all EA source in version control with dated history. The EA must be ours and explainable on a call.
2. **Clock:** derive server-to-UTC from MT5 in both daylight-saving regimes. Compute every window in ET or exchange time and convert.
3. **News filter:**
   - Load the FundingPips dashboard calendar (red events only), plus Fed speeches.
   - Block opens and closes within ±5 min on the affected currency.
   - Tag trades opened ≥ 5 h before events so they may be closed inside the window.
4. **Idea accounting:**
   - Group by instrument and direction.
   - Add the 10-minute post-loss window.
   - Hard-cap each idea's worst case (stop plus slippage) at ≤ 1% on Master, so strikes are unlikely and there is 2× headroom to the 2% breach. The 1% is a proposal, not a rule.
5. **Daily loss guard:**
   - Compute the baseline as max(balance, equity) at 00:00 platform time.
   - Kill switch at −3% (current policy), counting floating P&L.
   - Size positions so that a simultaneous stop-out of all open ideas stays under the kill switch.
6. **Weekends:** on Master, flat by Friday's close (the system auto-closes, and the day then does not count as a trading day).
7. **No same-instrument opposite positions.** No cross-account hedging.
8. **Inactivity:** ensure at least one **closed** trade every < 30 days per account.
9. **Lots:** ≤ 20 lots per order, ≤ 1 lot per click on crypto.
10. **Allocation:** ≤ $400k total across accounts.
11. **Profit concentration:** no single idea above 60% of a phase target (≥ $3,000 on phase 1 of a $50k account, derived: 60% × $5,000). Otherwise the Master account needs 4 profitable days before each reward.

---

## 3. Third-party and trader reports (NOT official; kept separate)
- **Trustpilot** shows about **4.5 stars from 60,000+ reviews** as of July 2026 [fundedtrading.com summary, EX]. The main complaint themes are:
  1. the **Risk Per Trade Idea grouping** closing accounts traders thought were within limits;
  2. terminations over **device ID or shared-IP matches** with little evidence given;
  3. disputes over whether the daily loss is computed from balance or equity [EX].
  - Source: https://fundedtrading.com/propfirm/fundingpips/ and https://www.trustpilot.com/review/fundingpips.com
- **Relevance to us:** run each account from a dedicated VPS or IP. Never share devices or IPs with other traders' accounts. Log baseline balance and equity at each reset.
- **Swap timing** (Propvator blog): FX swaps are tripled on **Wednesdays**, indices on **Fridays** [EX]. This fits the brief's "triple once a week" but should be checked in MT5 symbol specs. Source: https://propvator.com/blog/funding-pips-trading-conditions/
- **Third-party leverage summary** (LuxAlgo): up to 1:50 FX (1:100 on 2-Step), 1:20 indices, 1:30 metals, 1:10 energy, 1:2 crypto [EX]. Evaluation leverage for indices, metals and energy on 2 Step Flex was **not** confirmed from an official page ⚠. Source: https://www.luxalgo.com/prop-firms/funding-pips/
- **Payouts:** third-party trackers cite over $150m paid [EX].
- **Spreads:** Myfxbook keeps live FundingPips spread pages (e.g. EURUSD, XAUUSD) that could be scraped for a cross-check of our cost measurements. Sources: https://www.myfxbook.com/prop-firms-spreads/fundingpips/16351,1 and https://www.myfxbook.com/prop-firms-spreads/fundingpips/16351,51

---

## 4. Questions to send to FundingPips support (in writing)
1. Is the MT5 server clock UTC+3 all year, or GMT+2/GMT+3 following US or EU daylight saving? At what New York time does the daily reset happen in January?
2. How are "gap trading" and "tick scalping" defined? Is a trade opened 5 minutes after the cash open, fading the overnight move and closed the same day, allowed?
3. Which currency does an index CFD map to for the news restriction (US indices → USD, GER40/STX50 → EUR, FTSE100 → GBP, JP225 → JPY)?
4. Are US Treasury auctions or FOMC press conferences red events in the dashboard calendar?
5. What is the strike threshold on 2 Step Flex Master? Does the 35% consistency rule apply to bi-weekly rewards on 2 Step Flex?
6. Is there a maximum number of simultaneous open positions or orders?
7. Crypto commission: is lot × price × 0.04% charged per side or per round trip?
8. What are index-CFD swap rates, and on which day is the triple charged?
