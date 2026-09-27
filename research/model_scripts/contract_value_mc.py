"""Synthetic contract-value model behind research/PROP_FIRM_PAPERS.md section 4.

Stylized FundingPips 2-Step Flex ($50k) under a drifted Brownian P&L:
- daily P&L ~ N(mu, sigma^2) in % of the initial balance, mu = (SR/sqrt(252))*sigma
  (SR is annual and net of costs);
- daily steps with Brownian-bridge checks for intraday touches of the -12% static
  floor and of the 4% daily loss limit measured from the day's opening equity;
- targets +10% then +6% checked at the daily close, no time limit;
- one-year funded stage: every 10 trading days, 85% of any positive P&L is paid and
  the account resets to its initial balance; the account is lost at the floor or
  the daily limit; no fee refund, no discounting.
NOT modelled: the 2% per-trade-idea rule, news windows, weekend closures, payout
denials. Synthetic paths only; no market data.

Output V = P(pass both) * E[first-year payouts | funded] in dollars = break-even fee.
Run:  python3 contract_value_mc.py      (takes ~1 minute)
"""
import math
import random

SEED = 11
N_PATHS = 8000
ACCOUNT = 50_000
SPLIT = 0.85
FLOOR = -12.0
DAILY_LIMIT = 4.0
TARGETS = (10.0, 6.0)
FUNDED_DAYS = 252
PAYOUT_CYCLE = 10


def bridge_touch_prob(x0, x1, level, sigma):
    """P(min of a Brownian bridge from x0 to x1 over one day <= level)."""
    if x0 <= level or x1 <= level:
        return 1.0
    return math.exp(-2.0 * (x0 - level) * (x1 - level) / (sigma * sigma))


def run_phase(rng, target, mu, sigma, max_days=6000):
    x, day = 0.0, 0
    while day < max_days:
        day += 1
        x1 = x + mu + sigma * rng.gauss(0, 1)
        level = max(x - DAILY_LIMIT, FLOOR)
        if rng.random() < bridge_touch_prob(x, x1, level, sigma):
            return False, day
        if x1 >= target:
            return True, day
        x = x1
    return False, day


def funded_year(rng, mu, sigma):
    x, paid = 0.0, 0.0
    for d in range(1, FUNDED_DAYS + 1):
        x1 = x + mu + sigma * rng.gauss(0, 1)
        level = max(x - DAILY_LIMIT, FLOOR)
        if rng.random() < bridge_touch_prob(x, x1, level, sigma):
            return paid, True
        x = x1
        if d % PAYOUT_CYCLE == 0 and x > 0:
            paid += SPLIT * x
            x = 0.0
    return paid, False


def evaluate(rng, sr, sigma, n=N_PATHS):
    mu = sr / math.sqrt(252) * sigma
    passes, times, pays = 0, [], []
    for _ in range(n):
        ok1, t1 = run_phase(rng, TARGETS[0], mu, sigma)
        if not ok1:
            pays.append(0.0)
            continue
        ok2, t2 = run_phase(rng, TARGETS[1], mu, sigma)
        if not ok2:
            pays.append(0.0)
            continue
        passes += 1
        times.append(t1 + t2)
        pays.append(funded_year(rng, mu, sigma)[0])
    times.sort()
    median = times[len(times) // 2] if times else float("nan")
    value = sum(pays) / n / 100 * ACCOUNT
    return passes / n, median, value


def main():
    rng = random.Random(SEED)
    sigmas = [0.5, 0.75, 1.0, 1.25, 1.5]
    print("SR (annual, net) | per sigma (%/day): P(pass both), median days, V = break-even fee in $ on $50k")
    for sr in [-2.0, -1.0, 0.0, 1.0, 2.0]:
        cells = []
        for sg in sigmas:
            p, med, v = evaluate(rng, sr, sg)
            cells.append(f"{sg:.2f}: P {p:.3f}, {med:.0f} d, V ${v:,.0f}")
        print(f"SR {sr:+.1f} | " + " | ".join(cells))


if __name__ == "__main__":
    main()
