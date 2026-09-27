"""Goal-versus-floor sizing model behind research/SIZING.md.

Model only: daily P&L is Brownian motion with drift mu = s * sigma, where
s = annual Sharpe / sqrt(252) and sigma is daily volatility in % of the
initial balance. Target +a (10 then 6), static floor -b (12). No market data.

Run:  python3 sizing_model.py
Prints Table 1 (uncapped), Table 2 (capped policies), Table 3 (daily-loss
touch probabilities) and the current fixed-fraction policy proxy.
"""
import math
from math import exp, log, sqrt, erf

PHASES = [(10.0, 12.0), (6.0, 12.0)]  # (target a, floor b) in % of initial balance


def phi(x):
    return 0.5 * (1 + erf(x / sqrt(2)))


# ---------- Policy A: constant sigma (closed form) ----------
def const_sigma_for_pfail(sr_ann, a, b, pfail):
    """Return (sigma, E[T], P_fail) for the constant-sigma policy hitting a target P_fail."""
    s = sr_ann / sqrt(252)

    def pf(theta):
        return 1 - (exp(theta * b) - 1) / (exp(theta * b) - exp(-theta * a))

    lo, hi = 1e-6, 10.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if pf(mid) > pfail else (lo, mid)
    theta = 0.5 * (lo + hi)
    sigma = 2 * s / theta
    mu = s * sigma
    p = pf(theta)
    return sigma, (a * (1 - p) - b * p) / mu, p


def const_sigma_stats(sr_ann, sigma, a, b):
    s = sr_ann / sqrt(252)
    mu = s * sigma
    th = 2 * mu / sigma ** 2
    pu = (exp(th * b) - 1) / (exp(th * b) - exp(-th * a))
    return 1 - pu, (a * pu - b * (1 - pu)) / mu


# ---------- Policies B/C: (fractional) Kelly on a cushion (closed form) ----------
def kelly_cushion(sr_ann, a, b, pfail, k=1.0):
    """sigma(x) = k*s*(x + C). Solve the virtual floor C for P_fail. Return (C, sigma0, E[T], P_fail)."""
    s = sr_ann / sqrt(252)
    m = s * s * k * (1 - k / 2)
    v = (k * s) ** 2
    th = 2 * m / v

    def stats(C):
        u = log((C + a) / C)
        l = log((C - b) / C)
        pu = (1 - exp(-th * l)) / (exp(-th * u) - exp(-th * l))
        p = 1 - pu
        return p, (u * pu + l * p) / m

    lo, hi = b * 1.0000001, b * 1000
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        p, _ = stats(mid)
        lo, hi = (lo, mid) if p > pfail else (mid, hi)
    C = 0.5 * (lo + hi)
    p, ET = stats(C)
    return C, k * s * C, ET, p


# ---------- Capped policies: finite differences on the same ODEs ----------
def evaluate_policy(sig_fn, sr_ann, a, b, n=4001):
    """Solve 0.5 sig^2 P'' + s sig P' = 0 (P(-b)=1, P(a)=0) and the same with -1 on the
    right-hand side for E[T]. Returns (P_fail, E[T]) starting at x = 0."""
    s = sr_ann / math.sqrt(252)
    h = (a + b) / (n - 1)
    x = [-b + i * h for i in range(n)]
    lower = [0.0] * n
    diag = [0.0] * n
    upper = [0.0] * n
    diag[0] = diag[-1] = 1.0
    for i in range(1, n - 1):
        sg = sig_fn(x[i])
        d2 = 0.5 * sg * sg / h / h
        d1 = s * sg / (2 * h)
        lower[i], diag[i], upper[i] = d2 - d1, -2 * d2, d2 + d1

    def tri(r):
        cp = [0.0] * n
        dp = [0.0] * n
        cp[0] = upper[0] / diag[0]
        dp[0] = r[0] / diag[0]
        for i in range(1, n):
            m = diag[i] - lower[i] * cp[i - 1]
            cp[i] = upper[i] / m if i < n - 1 else 0.0
            dp[i] = (r[i] - lower[i] * dp[i - 1]) / m
        out = [0.0] * n
        out[-1] = dp[-1]
        for i in range(n - 2, -1, -1):
            out[i] = dp[i] - cp[i] * out[i + 1]
        return out

    rp = [0.0] * n
    rp[0] = 1.0
    rt = [-1.0] * n
    rt[0] = rt[-1] = 0.0
    P, T = tri(rp), tri(rt)
    i0 = int(round(b / h))
    return P[i0], T[i0]


def main():
    print("TABLE 1: uncapped policies, P(fail)=5% per phase")
    for sr in [1.0, 1.5, 2.0, 2.5, 3.0]:
        a1 = [const_sigma_for_pfail(sr, a, b, 0.05) for a, b in PHASES]
        b1 = [kelly_cushion(sr, a, b, 0.05, 1.0) for a, b in PHASES]
        c1 = [kelly_cushion(sr, a, b, 0.05, 0.5) for a, b in PHASES]
        print(f" SR {sr:.1f} | A const: sigma {a1[0][0]:.2f}%, days {a1[0][1]:.0f}+{a1[1][1]:.0f}={a1[0][1]+a1[1][1]:.0f}"
              f" | B Kelly-cushion: C {b1[0][0]:.2f}/{b1[1][0]:.2f}, sigma0 {b1[0][1]:.2f}%, days {b1[0][2]+b1[1][2]:.0f}"
              f" | C half-Kelly: C {c1[0][0]:.2f}/{c1[1][0]:.2f}, sigma0 {c1[0][1]:.2f}%, days {c1[0][2]+c1[1][2]:.0f}")

    print("\nTABLE 2: capped policies (total expected days, P(pass both))")
    for sr in [1.0, 1.5, 2.0, 2.5, 3.0]:
        s = sr / sqrt(252)
        for cap in [0.75, 1.0]:
            res = {}
            for name, fn in {
                "const": lambda v, c=cap: c,
                "KellyCushion": None,
                "halfKellyCushion": None,
            }.items():
                tot, ps = 0.0, 1.0
                for (a, b), (Cfull, Chalf) in zip(PHASES, [(13.48, 20.42), (14.12, 21.91)]):
                    if name == "const":
                        f = fn
                    elif name == "KellyCushion":
                        f = (lambda v, C=Cfull, c=cap: min(s * (v + C), c))
                    else:
                        f = (lambda v, C=Chalf, c=cap: min(0.5 * s * (v + C), c))
                    p, t = evaluate_policy(f, sr, a, b)
                    tot += t
                    ps *= (1 - p)
                res[name] = (tot, ps)
            print(f" SR {sr:.1f} cap {cap:.2f}%/d | " + " | ".join(f"{k}: {v[0]:.0f} d, {v[1]:.3f}" for k, v in res.items()))

    print("\nTABLE 3: P(intraday loss touches d within one day) ~ 2*Phi(-d/sigma)")
    for sig in [0.5, 0.75, 1.0, 1.25, 1.5]:
        p3, p4 = 2 * phi(-3 / sig), 2 * phi(-4 / sig)
        print(f" sigma {sig:.2f}%/d | -3%: {p3:.2e}/day, {1-(1-p3)**60:.3f} in 60d | -4%: {p4:.2e}/day, {1-(1-p4)**60:.3f} in 60d")

    print("\nCURRENT POLICY PROXY: 0.45% risk/trade, 1.5 trades/day -> sigma ~ 0.55%/day")
    sig = 0.45 * sqrt(1.5)
    for sr in [1.0, 1.5, 2.0, 2.5, 3.0]:
        tot, ps = 0.0, 1.0
        for a, b in PHASES:
            p, t = const_sigma_stats(sr, sig, a, b)
            tot += t
            ps *= (1 - p)
        print(f" SR {sr:.1f}: {tot:.0f} days, P(pass both) {ps:.3f}")


if __name__ == "__main__":
    main()
