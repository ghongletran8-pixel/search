# Sizing to pass a challenge: theory and a practical policy

Workstream E. Compiled 2026-09-25.

> **What is computed here.** Theory citations come from search-index excerpts [EX] or are marked "from memory, not re-read". All numbers in the tables are **closed-form or numerical solutions of a Brownian-motion model** whose inputs are stated. They are **not backtests** and use no market data. The formulas are in §4, so anyone can reproduce them.

## 1. The problem in one paragraph

We control the risk we run. The account must reach **+10%** (phase 1, then a new account and **+6%** in phase 2) before touching a **static floor at −12%** of the initial balance, and must never lose **4% within one day** (floating P&L included; baseline = max(balance, equity) at 00:00 platform time). There is **no deadline**. The goal is to **minimize the expected number of trading days to pass both phases, subject to P(fail) ≤ 5–10%**. Our edge is positive (Sharpe > 0), so this is a **favourable game with a goal and a floor**.

**Interpreting "daily Sharpe of about 1".** I read it as the annualized Sharpe ratio of daily P&L (mean/sd × √252 ≈ 1).
- Check: with ~0.55% daily volatility (the current 0.45% risk per trade, 1–2 trades a day), the model below gives a mean of **≈ 400 days** to pass both phases at Sharpe 1 [D, table 2].
- That is consistent with the brief's *median* of ~330 days, because first-passage times are right-skewed, so the median is below the mean.
- With a literal per-day Sharpe of 1 the times would be a few days, which does not match.

## 2. What the theory says

| Result | Setting | Implication for us |
|---|---|---|
| **Dubins & Savage** (*How to Gamble If You Must*, 1965): **bold play** (stake everything, or just enough to hit the goal) maximizes the probability of reaching a goal when the casino is **subfair or fair** [EX] | Discrete bets, maximize P(goal before ruin) | Our game is **favourable**, so bold play is *not* optimal. Only if the realized edge turned negative would boldness become rational, and then the right answer is to stop trading |
| **Pestien & Sudderth** (1985), "Continuous-time red and black: how to control a diffusion to a goal" | Controlled diffusion, maximize P(goal before floor) | From memory, not re-read: the optimal control maximizes the ratio of drift to variance. With drift ∝ stake and variance ∝ stake², that ratio *rises as the stake falls*. So with no deadline, **smaller stakes raise P(success) toward 1 but make the expected time unbounded**. The real trade-off is **time versus failure** |
| **Browne (1995)**, *Math. of OR* 20(4): exponential utility and minimizing the probability of ruin [EX, title] | Continuous time, random risk process | From memory, not re-read: ruin-minimizing investment is a **constant amount** in the risky asset, independent of wealth, i.e. "constant-σ" in our notation (policy A below) |
| **Browne (1997)**, "Survival and Growth with a Liability", *Math. of OR* 22(2) | Wealth with a floor, maximize survival, then grow | For the survival problem **no optimal policy exists**, only ε-optimal ones [EX], consistent with timid play being optimal only in the limit. **Inside the safe region, the growth-optimal policy reaches a higher goal as quickly as possible** [EX]. That is the log-optimal, i.e. Kelly, rule |
| **Browne (1999)**, "Reaching Goals by a Deadline", *Adv. Appl. Prob.* 31 | Maximize P(reach goal by a fixed date) [EX] | With a deadline the optimal policy is a replicating strategy for a digital option. It becomes more aggressive when behind schedule. **We have no deadline**, so this only matters if we impose a time budget |
| **Grossman & Zhou (1993)**, *Mathematical Finance* 3 | Max growth s.t. wealth never falls below α × running maximum | Invest **in proportion to the surplus W − αM** [EX]: a CPPI with a moving floor. Later work shows it is "not always optimal" in some settings [EX, title] |
| **CPPI** (Black & Perold 1992; not re-read) | Exposure = multiplier × (wealth − floor) | Same structure as Grossman–Zhou with a fixed floor |
| **Fractional Kelly** (MacLean, Thorp & Ziemba 2010/2011, "good and bad properties") [EX] | Growth vs security trade-off | Full Kelly gives heavy drawdowns: at the Kelly optimum the **drawdown distribution is a power law with exponent 2** (Maslov & Zhang 1998) [EX]. Fractional Kelly trades growth for much smaller drawdowns |

**New result derived here (§4.3).** For "minimize E[time] + λ·P(fail)" with drift proportional to risk, the Hamilton–Jacobi–Bellman solution is **full Kelly on the cushion above a virtual floor −C lying slightly below the real floor**: `σ*(x) = s·(x + C)`, with `s` the per-day Sharpe and `x` the P&L in % of initial balance. This is exactly the CPPI / Grossman–Zhou structure with the multiplier set by Kelly. The virtual floor `C` is set by the allowed failure probability. In practice the rule is capped by the daily-loss limit (§3), which binds once Sharpe ≥ ~1.5.

## 3. Numbers (model: daily P&L is Brownian with drift = s·σ, s = SR/√252)

### Table 1. Uncapped policies, P(fail) = 5% per phase (≈ 90% pass both), floor −12%
| Annual SR | **A. Constant σ** (σ %/day; E[T1] + E[T2] = total days) | **B. Full Kelly on cushion** (σ at start; total days) | **C. Half Kelly on cushion** (σ at start; total days) |
|---|---|---|---|
| 1.0 | 0.52%; 272 + 145 = **417** | 0.85%; 210 + 122 = **332** | 0.64%; 225 + 128 = **353** |
| 1.5 | 0.78%; 121 + 65 = **185** | 1.27%; 93 + 54 = **148** | 0.96%; 100 + 57 = **157** |
| 2.0 | 1.04%; 68 + 36 = **104** | 1.70%; 53 + 30 = **83** | 1.29%; 56 + 32 = **88** |
| 2.5 | 1.30%; 44 + 23 = **67** | 2.12%; 34 + 20 = **53** | 1.61%; 36 + 21 = **56** |
| 3.0 | 1.56%; 30 + 16 = **46** | 2.55%; 23 + 14 = **37** | 1.93%; 25 + 14 = **39** |

- Virtual floors: B uses C = 13.48% (phase 1) and 14.12% (phase 2); C uses C = 20.42% and 21.91%.
- Two checks: time scales as 1/SR² (e.g. 417 → 104 from SR 1 to 2, a ratio of 4.0 [D]), matching the brief's rule of thumb. At equal failure probability the cushion policy saves ~20% of the time.
- **But** at SR ≥ 1.5 these volatilities break the daily-loss limit (Table 3), so the uncapped numbers are **not achievable**.

### Table 2. Policies with a daily-volatility cap (floor −12%)
| Annual SR | Cap %/day | A. Constant σ = cap: total days, P(pass both) | B. Kelly-cushion ∧ cap | C. Half-Kelly-cushion ∧ cap |
|---|---|---|---|---|
| 1.0 | 0.75 | 253, 0.81 | 364, 0.92 | 358, 0.90 |
| 1.0 | 1.00 | 158, 0.72 | 336, 0.91 | 353, 0.90 |
| 1.5 | 0.75 | 202, 0.92 | 219, 0.95 | 209, 0.93 |
| 1.5 | 1.00 | 135, 0.85 | 173, 0.93 | 165, 0.91 |
| 2.0 | 0.75 | 162, 0.97 | 165, 0.98 | 163, 0.97 |
| 2.0 | 1.00 | **114, 0.92** | 123, 0.95 | 118, 0.93 |
| 2.5 | 0.75 | 133, 0.99 | 134, 0.99 | 133, 0.99 |
| 2.5 | 1.00 | **96, 0.96** | 99, 0.97 | 97, 0.96 |
| 3.0 | 1.00 | **83, 0.98** | 83, 0.99 | 83, 0.98 |

- **Current policy** (fixed 0.45% risk per trade, ~1.5 trades/day, so σ ≈ 0.55%/day [D: 0.45 × √1.5, R-multiple sd ≈ 1]):
  - SR 1.0: 251 + 148 = **399 days**, P(pass) 0.90.
  - SR 1.5: 296 days, 0.97.
  - SR 2.0: 228 days, 0.99.
  - SR 2.5: **184 days**, 0.998.
- **Reading the table:**
  - At **SR ≈ 1** the cushion rule is what keeps failure near 10%. Constant σ at a 1% cap fails 28% of the time.
  - At **SR ≥ 2**, running at the cap gives ~96–114 days with ≥ 92% pass probability. The current 0.45% risk is **too timid** there (184–228 days).

### Table 3. Why a cap near 1%/day: the 4% daily limit
Probability that the intraday running loss touches `d` within one day, using the driftless reflection bound `2Φ(−d/σ)` [D]:

| σ %/day | touch −3% (kill switch) per day | …within 60 days | touch −4% (breach) per day | …within 60 days |
|---|---|---|---|---|
| 0.50 | ~0 | ~0 | ~0 | ~0 |
| 0.75 | 6e-5 | 0.4% | 1e-7 | ~0 |
| 1.00 | 0.27% | 15% | 6e-5 | 0.4% |
| 1.25 | 1.6% | 63% | 0.14% | 8% |
| 1.50 | 4.6% | 94% | 0.77% | 37% |

- Normal tails **understate** real ones: news gaps, slippage and correlated stops across strategies.
- With a −3% kill switch, **σ ≈ 0.8–1.0%/day** is the practical ceiling. At that level the kill switch fires a few times a year, and a true −4% breach needs a gap through the kill switch.

## 4. Formulas (for reproduction)

Notation: `x` = P&L in % of the initial balance; target `a` (10, then 6); floor `−b` (b = 12); per-day Sharpe `s = SR/√252`; policy volatility `σ(x)` in %/day; drift `μ = s·σ`.

### 4.1 Constant σ (policy A)
- `θ = 2μ/σ² = 2s/σ`
- `P(pass) = (e^{θb} − 1)/(e^{θb} − e^{−θa})`, `P(fail) = 1 − P(pass)`
- `E[T] = (a·P(pass) − b·P(fail))/μ` (days)
- Given a target P(fail), solve for θ, then set `σ = 2s/θ`. **So E[T] ∝ 1/s²** at fixed failure probability.

### 4.2 Kelly-type policy on a cushion (policies B and C)
- `σ(x) = k·s·(x + C)`, where `k` = Kelly fraction (1 = full, 0.5 = half) and `−C` = virtual floor, `C ≥ b`.
- The log-cushion is Brownian with drift `m = s²k(1 − k/2)` and variance `v = k²s²`, so `θ' = 2m/v = (2 − k)/k`.
- With `u = ln((C + a)/C)` and `l = ln((C − b)/C)`:
  - `P(pass) = (1 − e^{−θ' l})/(e^{−θ' u} − e^{−θ' l})`
  - `E[T] = (u·P(pass) + l·P(fail))/m`
- For **k = 1**: `P(fail) = a(C − b)/(C(a + b))`, so for a target p, `C = ab/(a − p(a + b))`. With a = 10, b = 12, p = 5%: **C = 13.48** [D].

### 4.3 Why the cushion policy is optimal (sketch)
- Minimize `E[T] + λ·1{fail}` over `σ(·) ≥ 0`. The HJB equation is `min_σ { s·σ·V′ + ½σ²V″ } + 1 = 0`, with `V(a) = 0` and `V(−b) = λ`.
- The minimizer is `σ* = −s·V′/V″`. Substituting gives `V″ = s²V′²/2`, so `V′ = −2/(s²(x + C))` and `σ* = s·(x + C)`, i.e. **full Kelly on the cushion**.
- `λ` fixes `C` through `V(−b) = (2/s²)·ln((a + C)/(C − b)) = λ`.
- With a vol cap, the optimal rule becomes `σ = min(cap, s·(x + C))` (not proven here; evaluated numerically in Table 2 by finite differences on the same ODEs).

### 4.4 Daily-loss touch probability
- `P(min over the day ≤ −d) ≈ 2Φ(−d/σ)` for a driftless Brownian path.
- The drift is negligible at one day for these Sharpe ratios. Normality understates tails.

## 5. Recommended policy

1. **Size to a daily-volatility budget, not to a fixed per-trade percentage.**
   - Target `σ_day = min(cap, k·ŝ·(x + C))` with **cap = 0.9%/day** and **k = 0.5**.
   - Use the half-Kelly virtual floor for P(fail) = 5% per phase: **C ≈ 20.4%** (phase 1) and **≈ 21.9%** (phase 2) [D].
   - Take `ŝ` as a **haircut** Sharpe: the brief notes published anomalies lose about half their strength after publication (McLean & Pontiff 2016), and our own 4 h edge fell from +0.14 to +0.056 R. Use a live or rolling estimate, and never more than half of a new strategy's backtest Sharpe.
   - At SR ≈ 1 this gives σ ≈ 0.6%/day at the start, similar to today. At SR ≥ 2 it hits the cap.
2. **Convert to per-trade risk.** With `n` roughly independent trades a day and R-multiple sd ≈ 1, `risk per trade ≈ σ_day/√n_eff`, where `n_eff` accounts for correlation between concurrent trades. Example: σ = 0.9% and n_eff = 1.5 give **≈ 0.73% per trade** [D]; today's rule is 0.45%.
3. **Portfolio level.** When several strategies run, compute σ_day from the **covariance of the strategies' daily R** (estimated on overlapping history), not from summing trade risks. Concurrent positions on the same instrument and direction are one FundingPips "idea" and must be capped together.
4. **Daily guard.**
   - Keep the **−3% kill switch** on equity versus the day's baseline.
   - Add a soft brake: after **−2%** on the day, halve new-trade risk.
   - Size so that the *simultaneous stop-out of all open ideas* stays inside the kill switch.
5. **Near the floor.** The cushion rule shrinks risk automatically as `x` falls. At x = −8% with C = 20.4, risk is (20.4 − 8)/20.4 ≈ **61%** of the starting level [D]. This replaces the current ad hoc "scale down near the floor".
6. **Near the target.** There is no reward for overshooting and no deadline. Do not switch to bold play. The cushion rule *raises* risk slightly after gains, but the cap keeps it bounded.
7. **Master account.** Keep risk per idea ≤ 1% (with slippage buffer) so the **2% per-idea hard limit** and any strike threshold are far away. That is compatible with the cap. Remember the 10-minute same-direction re-entry rule (see `FUNDINGPIPS_RULES.md`).
8. **Re-estimate monthly.** If live Sharpe falls, the rule automatically moves toward smaller risk (longer time, same failure budget).

## 6. Comparison with the current policy

| Policy | SR 1.0 | SR 1.5 | SR 2.0 | SR 2.5 |
|---|---|---|---|---|
| **Current**: 0.45% per trade (σ ≈ 0.55%/day), scaled down near the floor, −3% kill switch | 399 d, pass 0.90 | 296 d, 0.97 | 228 d, 0.99 | 184 d, 0.998 |
| **Proposed**: half-Kelly on cushion with cap 0.9–1.0%/day | ~353 d, 0.90 (cap not binding) | ~165 d, 0.91 | ~118 d, 0.93 | ~97 d, 0.96 |

The proposed row uses Table 2's cap = 1.0% values; with a 0.9% cap the times sit between the 0.75% and 1.0% rows.

**Conclusions:**
- At today's Sharpe (~1), the current policy is **already close to efficient**. Better sizing saves perhaps 10–15% of the time.
- **The main lever is Sharpe itself.** Time ∝ 1/SR².
- If new edges lift SR to 2–2.5, the current fixed 0.45% risk leaves **about half of the speed** unused (184–228 days versus ~97–118). Raise risk to the 0.9–1.0%/day cap then, and only after the higher Sharpe is **measured live**.

## 7. Caveats
- **Estimation risk dominates:** over-estimating Sharpe leads to over-betting. The cushion formula is only as good as `ŝ`.
- Brownian and normal assumptions ignore fat tails, volatility clustering, serial correlation of daily P&L, discrete trades and news gaps. All of these make the real floor and daily-limit risks larger than shown.
- The baseline for the 4% limit is max(balance, equity) at the start of the day, so open profits carried overnight raise the next day's baseline. That makes the effective daily limit tighter after good days with open trades.
- Phase 2 restarts from the initial balance. Times add and pass probabilities multiply, as computed.
