"""How likely is it to pass BOTH FundingPips 2-Step Flex phases within one month?

Synthetic model only (no market data), same conventions as contract_value_mc.py:
- daily P&L ~ N(mu, sigma^2) in % of the initial balance; mu = (SR/sqrt(252))*sigma,
  SR = annual Sharpe net of costs;
- intraday touches checked with a Brownian bridge;
- a -3% daily kill switch (the team's current rule): if the day's intraday loss touches
  -3% from the day's opening equity, the day closes at -3% (no slippage). Because the
  kill switch sits above the 4% daily limit, the model has no daily-limit breaches;
  real gaps and slippage would add some;
- static floor at -12% of the initial balance = failure;
- phase 1 target +10%, then one day to receive phase-2 credentials, then +6% from a
  fresh balance; targets are checked at the daily close;
- no time limit (FundingPips 2-Step Flex), so failing to pass in a month is not failure.
Policies: constant sigma, or "aggressive month then fall back" (sigma_hi for the first
21 trading days, then sigma_lo until pass or fail).

Run:  python3 one_month_mc.py   (about 1-2 minutes)
"""
import math
import random

SEED = 5
N = 5000
MONTH = 21            # trading days in one month
KILL = 3.0            # daily kill switch, % of initial balance
FLOOR = -12.0
TARGETS = (10.0, 6.0)
MAX_DAYS = 3000


def touch(x0, x1, level, sigma):
    if x0 <= level or x1 <= level:
        return 1.0
    return math.exp(-2.0 * (x0 - level) * (x1 - level) / (sigma * sigma))


def simulate(rng, sr, sigma_fn):
    """Return (passed, day_passed_or_failed)."""
    s = sr / math.sqrt(252)
    day = 0
    for phase, target in enumerate(TARGETS):
        if phase == 1:
            day += 1  # credential delay
        x = 0.0
        while True:
            day += 1
            if day > MAX_DAYS:
                return False, day
            sigma = sigma_fn(day)
            mu = s * sigma
            x1 = x + mu + sigma * rng.gauss(0, 1)
            lvl_kill = x - KILL
            lvl = max(lvl_kill, FLOOR)
            if rng.random() < touch(x, x1, lvl, sigma):
                if lvl == FLOOR or lvl_kill <= FLOOR:
                    return False, day          # static floor reached
                x = lvl_kill                    # kill switch: flat for the day
                continue
            x = x1
            if x >= target:
                break
    return True, day


def summarize(results):
    n = len(results)
    passed_days = sorted(d for ok, d in results if ok)
    p21 = sum(1 for ok, d in results if ok and d <= MONTH) / n
    p42 = sum(1 for ok, d in results if ok and d <= 2 * MONTH) / n
    p63 = sum(1 for ok, d in results if ok and d <= 3 * MONTH) / n
    pev = len(passed_days) / n
    med = passed_days[len(passed_days) // 2] if passed_days else float("nan")
    return p21, p42, p63, pev, med


def main():
    rng = random.Random(SEED)
    print("A) Constant sigma. Columns: P(pass both <=21d) | <=42d | <=63d | P(eventual pass) | median days to pass")
    for sr in [1.0, 2.0, 3.0, 4.0, 6.0]:
        for sg in [0.5, 1.0, 1.5, 2.0]:
            res = [simulate(rng, sr, lambda d, v=sg: v) for _ in range(N)]
            p21, p42, p63, pev, med = summarize(res)
            print(f" SR {sr:.0f} sigma {sg:.2f}%/d | {p21:.3f} | {p42:.3f} | {p63:.3f} | {pev:.3f} | {med:.0f}")
    print("\nB) Aggressive first month (sigma_hi) then fall back to 0.55%/d")
    for sr in [1.0, 2.0, 3.0, 4.0]:
        for hi in [1.0, 1.5, 2.0]:
            res = [simulate(rng, sr, lambda d, h=hi: h if d <= MONTH else 0.55) for _ in range(N)]
            p21, p42, p63, pev, med = summarize(res)
            print(f" SR {sr:.0f} hi {hi:.2f} | {p21:.3f} | {p42:.3f} | {p63:.3f} | {pev:.3f} | {med:.0f}")


if __name__ == "__main__":
    main()
