# Recent research on prop-firm evaluation contracts (2026) and what it means for our FundingPips challenge

Added 2026-09-27 at the owner's request.

> **Access caveat (same as the rest of the dossier).** SSRN is still blocked by this environment's network policy, so no PDF was opened. Everything below comes from search-engine excerpts of the SSRN abstract pages [EX], plus my own derivations [D] and a small synthetic simulation [SIM] described in §4.

## 1. Verification: what was asked versus what exists

| # as given | Title / author / ID as given | What I found | Status |
|---|---|---|---|
| 1 | "The Price of a Funded Account: An Actuarial Analysis of Proprietary Trading Firm Challenges", Boon Chuan Lim, SSRN 7178078 | Exists: Lim, SSRN 7178078, first posted 25 Jul 2026, dated 5 Aug 2026 in a later listing [EX]. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7178078 | **Verified.** The quoted numbers (0.50 → 0.30; $500 → $221; 56%) match the abstract. The paper uses **arithmetic** Brownian motion [EX], not "geometric rules" |
| 2 | "Valuing Proprietary Trading Firm Evaluation Contracts: Closed Form, Cross-Firm Dispersion and the Source of the Margin", "Matilla Serrano", SSRN 7260819 | **Not found.** Neither the exact title nor ID 7260819 returns any indexed paper, and the "13 firms / 62% variance / trailing drawdowns latching onto intraday balances" claims appear nowhere I could search. Closest real papers: **Lim, "Phantom Generosity"** (SSRN 7184138) and **Matilla Serrano's contract "Atlas" and "Real Contracts" papers** (SSRN 7429100 and 7488382); see §2.2 | **Unverified; treat the 62% figure as unsupported.** The description may be an AI-generated blend of these real papers. Ask whoever supplied it for the link |
| 3 | "Market Edge versus Contract Edge: Negative-Expectancy Trading under an Idealized Evaluation Contract", "Matilla Serrano", SSRN 7468080 | Exists: **Francisco Matilla Serrano**, SSRN 7468080, 15 Sep 2026 [EX]. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7468080 | **Verified.** The main claim (a negative-expectancy trading rule can have positive *contract* value) is right. "Rules act as filters isolating variance rather than skill" is the supplier's gloss; the abstract says "the trading rule does not improve; **the contract changes the participant's payoff**" [EX] |

**One source to ignore:** "Coupon-Based Entry Incentives in Proprietary Trading: Evidence from Funding Pips' PROPFT 20% Discount" (Georgiou, SSRN 5626610). It sits among several near-identical "Funding Pips coupon code PROPFT" uploads by different names on SSRN and ResearchGate [EX]. It looks like promotional content, and its claims (e.g. a "23% increase in enrollment") should not be used as evidence.

## 2. What each paper says

### 2.1 Lim (2026a), "The Price of a Funded Account" (SSRN 7178078)
- **Model:** challenges priced as contingent claims. Trader equity is **arithmetic Brownian motion**, solved as a first-passage problem by Monte Carlo, **including funded-stage profit sweeps and fee refunds** [EX].
- **Results:**
  - The **time limit is the firm's hidden edge.** A zero-edge trader passes the frictionless benchmark with probability **0.50**, but the baseline contract with probability **0.30** [EX].
  - Contract value concentrates on a **narrow risk-sizing ridge near 2% daily volatility**, "which the product's marketing never discloses" [EX].
  - For an illustrative trader population with transaction-cost drag, a **USD 500** challenge is worth **USD 221** on average, a **56%** implied loss for the buyer and gross margin for the firm. **7.5%** of simulated buyers reach funded status [EX].
- **Policy proposal:** standardized disclosure (cohort funnel, payout ratio, conditional median payout), modelled on CFD loss-rate and gaming-machine return-to-player rules [EX].
- **Limits:** the baseline contract's exact target, drawdown and time-limit settings were not seen in the excerpts [n/s]. The results depend on the assumed trader population.

### 2.2 Closest matches to the unverified "Paper 2"
- **Lim (2026b), "Phantom Generosity: Contract Design and Value in the Market for Proprietary-trading Evaluations"** (SSRN 7184138, 26 Jul 2026) [EX]:
  - **Data:** hand-collected full rules and fees for **31 contracts across 21 firms**, with dated screenshot evidence (25–26 Jul 2026). Every contract was valued on a common population of trader skill and volatility, with a **300-trading-day evaluation cap** and a **one-year funded horizon**.
  - **29 of 31 contracts have negative benchmark expected value at list prices**, even *before* consistency rules, payout caps and monthly rebilling are counted. Those estimates are upper bounds.
  - **The fee explains almost none of the value variation.** Identically priced contracts at one firm differ in value by **$235**, and cheaper contracts are frequently better.
  - Among one-step contracts, **pass probability is negatively associated with value**, concentrated in contracts with **trailing drawdowns** and **tighter funded-stage terms**. This is consistent with firms competing on salient evaluation terms while tightening low-salience funded-stage terms.
  - Which firms are in the sample was **not seen**; do not assume FundingPips is included.
- **Matilla Serrano (2026a), "A Versioned Contract Atlas of Retail Futures Evaluations: Product Families, Stage Transitions, and Scenario-Conditional Probabilities"** (SSRN 7429100, 7 Sep 2026) [EX]: a version-aware database and executable rule taxonomy of **futures** prop evaluations (trailing drawdown, payout eligibility; Monte Carlo). Futures only, so FundingPips (CFDs) is presumably out of scope.
- **Matilla Serrano (2026b), "Real Contracts under Common Trading Scenarios: A Comparison Framework with a Source-Linked Pilot"** (SSRN 7488382, 18 Sep 2026) [EX]:
  - Holds trading scenarios fixed and replays versioned contracts.
  - The Atlas holds **177 product-route-size configurations across 22 providers**; 155 evaluation and 103 funded configurations have enough inputs to run.
  - It separates **passing, funded eligibility, actual payment and net cash flow**, and replays **EOD, intraday and static loss floors**, soft daily limits, consistency thresholds, minimum and qualifying days, and first-payout hurdles under three synthetic P&L paths.
  - This is the real "cross-firm dispersion from hidden rule structure" work. **The 62% number was not seen.**

### 2.3 Matilla Serrano (2026c), "Market Edge versus Contract Edge" (SSRN 7468080)
- **Binary-cycle model** [EX]:
  - In the market, a strategy wins **U** with probability p and loses **D** otherwise: market expectancy = `pU − (1 − p)D`.
  - Under the contract, the participant pays fee **F**, passes the evaluation with probability **p**, then passes a second (funded) stage with conditional probability **q** and receives payout **W** at share **s**, paying activation fee **A** on passing: contract expectancy = `p·q·s·W − F − p·A`.
- **Baseline** (q = p, s = 1, A = 0): the contract has positive expectancy when **p > √(F/W)**, while the market strategy is negative when **p < D/(U + D)** [EX].
  - Example: a "50K" account with U = $3,000, D = $2,000, F = $40, W = $3,000 gives **11.55% < p < 40%**: negative in the market, positive under the contract [EX].
  - Check [D]: √(40/3000) = 0.1155 and 2000/5000 = 0.40.
- **Less generous terms** (F, A, s) = ($90, $100, 90%) raise the break-even p to **20.20%**, and at p = q = 20% the participant's expected cash flow is **−$2** [EX].
  - Check [D]: 0.2 × 0.2 × 0.9 × 3000 − 90 − 0.2 × 100 = 108 − 90 − 20 = −2, and solving 2700p² − 100p − 90 = 0 gives p = 0.2020.
- Exact finite-N enumeration: probability of strict profit over 50 cycles = **87.01%** (baseline) versus **40.37%** (less generous) [EX].
- The author states it is **not an arbitrage claim**, **describes no identified firm**, and is the start of a research programme on rules, heterogeneity, strategic risk, payout governance and multi-account dependence [EX].

## 3. How our contract differs (FundingPips 2-Step Flex, $50k)

| Feature | Typical contract in these papers | FundingPips 2-Step Flex (see `FUNDINGPIPS_RULES.md`) | Consequence |
|---|---|---|---|
| Time limit | Yes (Lim's baseline); 300-day cap in "Phantom Generosity" | **None** (a closed trade every 30 days is enough) | **Lim's main firm edge (0.50 → 0.30) does not apply to us** |
| Drawdown | Often trailing (intraday or EOD) | **Static 12% floor** | The trailing-drawdown penalty in "Phantom Generosity" does not apply |
| Daily loss | Varies | **4% of max(balance, equity) at day start, intraday, floating P&L counts** | **This is our contract's main firm edge** (§4) |
| Targets | Often one step | 10% then 6% (two steps; p is the product) | Zero-edge pass probability = 12/22 × 12/18 = **36.4%** with no daily limit [D: gambler's ruin, P = b/(a + b)] |
| Fee refund | Sometimes | **None on 2-Step Flex** (the refund applies to 2 Step Standard after the 4th reward) [EX, FundingPips blog and help centre] | W is not offset by a refund |
| Payouts | Share s, caps, consistency | 85% (1 min day) or 95% (3 profitable days ≥ 0.5%); bi-weekly; **first request 14 days after the first Master trade**; split chosen at purchase [EX] | s = 0.85 or 0.95 |
| Funded-stage restrictions | Consistency, payout caps, rebilling | 2% per trade idea (hard breach), strikes, ±5-min news profit deductions, no weekend holds (temporary) | Cap the variance you can run in the funded stage |

## 4. Applying their framework to our contract (synthetic model)

**Model [SIM]** (scratchpad simulation; synthetic paths only, no market data):
- Daily P&L ~ N(μ, σ²) in % of the initial balance, with μ = (SR/√252)·σ, so **SR is annualized and net of costs**.
- Daily steps with Brownian-bridge checks for intraday touches of the **−12% static floor** and the **4% daily limit** (from the day's opening equity).
- Target checked at the daily close.
- Phase 1 (+10%), then phase 2 (+6%), with no time limit.
- Then a **one-year funded stage** (the horizon Lim uses): every 10 trading days, 85% of any positive P&L is paid and the account resets to its initial balance. The account is lost at the floor or the daily limit.
- No fee refund and no discounting. The 2% per-idea rule, news rules and weekend closures are **not** modelled.
- 6,000–8,000 paths per cell. Monte Carlo error is about ±1–2 pp on probabilities and about ±5% on values.
- Output "V" = P(pass both) × E[first-year payouts | funded], in dollars on a $50k account. **V is the break-even fee**: the contract has positive expected value if the fee is below V.

| Annual SR (net) | σ = 0.50%/day | 0.75 | **1.00** | 1.25 | 1.50 |
|---|---|---|---|---|---|
| −2.0 | P 0.000, V $0 | P 0.003, V $2 | P 0.013, V $11 | P 0.023, V $35 | P 0.032, V $36 |
| −1.0 | P 0.014, V $16 | P 0.047, V $77 | P 0.075, V $159 | P 0.096, V $199 | P 0.097, V $212 |
| 0.0 | P 0.350, V $850 | P 0.344, V $1,167 | **P 0.349, V $1,443** | P 0.310, V $1,355 | P 0.234, V $810 |
| 1.0 | P 0.919, V $4,056 | P 0.803, V $5,227 | **P 0.713, V $5,750** | P 0.599, V $5,001 | P 0.423, V $2,784 |
| 2.0 | P 0.996, V $7,226 | P 0.967, V $10,382 | **P 0.910, V $12,533** | P 0.801, V $11,757 | P 0.601, V $6,765 |

Median days to pass both phases (from the same runs): at SR 1.0, **397 / 221 / 139 / 90 / 59** days for σ = 0.5 → 1.5; at SR 2.0, **237 / 153 / 104 / 74 / 51** days.

**What this shows:**
1. **Our contract's value ridge sits near σ ≈ 1%/day,** not the ~2% Lim finds for his (time-limited) baseline. The **4% daily limit** is what cuts value above ~1.25%/day. Even a zero-edge trader's pass probability falls from 0.35 to 0.23 between σ = 1.0 and 1.5 [SIM].
2. **Matilla Serrano's point holds for our contract.** A strategy with SR ≈ −1 still has positive contract value (~$160–210 per $50k at σ ≥ 1%), purely from payout convexity. At SR ≈ −2 the value is close to zero. The firm's margin comes from buyers deep in negative edge and trading too large. **Do not read positive contract value as evidence of skill.**
3. **Two objectives, two different risk levels.**
   - Our brief's objective (pass with ≥ 90% probability, as fast as possible) gives σ ≈ 0.55%/day at SR 1 (`SIZING.md`).
   - The **value-maximizing** risk is ≈ 1%/day, with only ~71% pass probability at SR 1 but ~40% more value ($5,750 vs $4,056) [SIM].
   - If failure costs only the fee and the time to restart, and several accounts can be run (FundingPips caps total allocation at **$400k**), maximizing value per account can beat maximizing single-account pass probability. **This is a decision for the owner.** At SR ≥ 2 the two nearly coincide (σ ≈ 1% gives 91% pass *and* near-maximum value).
4. **The fee is small next to the modelled value** for SR ≥ 0 (a few hundred dollars against thousands). The real risks are not in this model:
   - rule breaches: the 2% per-idea hard limit, news-window deductions, the "gap trading" or "gambling" interpretations;
   - payout denials, firm solvency and counterparty risk;
   - the fact that our live Sharpe is lower than backtests.
   Lim's and Matilla Serrano's work shows how much **funded-stage terms** drive value. Read the 2-Step Flex Master terms in full before scaling.
5. **The 95% split option** raises every payout by 95/85 − 1 ≈ **11.8%** [D]. It needs 3 profitable days of ≥ 0.5% each [EX; whether per reward cycle or once was n/s], which an automated system running ~1%/day volatility should usually meet. Worth choosing if the purchase price difference is small (price n/s).

## 5. Changes to our plan
- `SIZING.md` remains the rule for the **evaluation** under the brief's objective. This file adds the **contract-value view**, which argues for σ ≈ 1%/day per account if the owner accepts a lower single-account pass rate in exchange for higher expected value across several accounts.
- `FUNDINGPIPS_RULES.md` should be read alongside §3: no fee refund on 2-Step Flex; first reward 14 days after the first Master trade; split fixed at purchase.
- **Open question for the owner:** is the target "≥ 90% pass on one account" (brief) or "maximum expected value across a set of accounts within the $400k cap"? The optimal risk differs, as shown in §4.

## 6. Sources for this file
See `SOURCES.md` section F.
