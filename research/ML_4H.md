# A better 4-hour model: what the literature supports

Workstream B. Literature review only. Compiled 2026-09-25.

> **Caveat.** As in the other files, full texts were not reachable from this session, so numbers are from search-index excerpts [EX] unless marked derived [D]. Several sources are practitioner or capstone work [PR]. **n/s** means not seen.
> The review is written against our current model: gradient boosting plus a neural net, 60 price, calendar, news-timing and cross-market inputs, a 4 h horizon, the top 1% of predictions across 16 symbols. It earned +0.14 R/trade over 2018–26 but only +0.056 R/trade in 2025–26.

## 1. Bottom line

1. **The large benchmark studies say more model complexity rarely helps at short horizons. Better inputs and better selectivity do.**
   - Intraday ML on 5-minute equity market returns works mainly through **lagged cross-sectional returns** with **regularized linear or tree ensembles**. Ensembles did best: Sharpe **0.98 after costs** [EX] (Huddleston, Liu & Stentoft, JFEc 2023).
   - A 2021–2025 walk-forward study on MNQ found **no** significant edge from 14 OHLCV signal families [EX], and no edge from LSTMs or gradient boosting on 5-minute OHLCV alone (out-of-sample accuracy 50.0–50.9%; permutation p = 0.135 and 0.515) [EX] (Mesfin 2026, two papers).
   - Our own negative results (attention, mixture of experts, shorter windows, recency weights, per-asset models) fit this pattern.
2. **The 4 h horizon sits at a regime boundary.** Using futures tick data (14 years) and longer histories, Schmidhuber & Safari (Physica A 2025) find that markets **trend on time scales from a few hours to a few years** and **revert on shorter and longer scales**. Weak trends persist; strong ones tend to revert before they become significant [EX]. So a 4 h model should be told which regime a move belongs to. Give it both sub-hour reversion features and multi-hour trend features, and let the trees learn the interaction.
3. **The biggest likely gain is new information, not new architecture.** Workstream A found mechanism-based state variables our model does not have:
   - dealer gamma (GEX);
   - month-end 60/40 drift and days to month-end;
   - Treasury auction days and time to the 13:00 ET close;
   - the FOMC blackout flag;
   - an LETF flow proxy.
   Adding them is cheap and fits our "cross-market and calendar" inputs.
4. **Selectivity:** we already trade only the top 1%. A **meta-label or abstention layer** trained on *our own* signals (did this top-1% signal hit its target before its stop?) is the standard next step. The evidence is modest and mostly practitioner [PR], but it is cheap to add and hard to get badly wrong if validated properly.
5. **Validation hygiene** matters as much as model changes. With many variants tried, use purged/embargoed cross-validation (combinatorial where possible) and report the **Deflated Sharpe Ratio** and the **probability of backtest overfitting** [EX]. The recent fall in edge (+0.056 R) may be partly regression to the mean of an over-selected model.

## 2. Evidence by topic

### 2.1 Feature families
| Family | What the evidence says | Horizon and market in source | Reported size | Transfer to us |
|---|---|---|---|---|
| **Lagged cross-sectional returns** (lead–lag) | Lagged 5-minute returns of index constituents predict the next 5-minute market return. Regularized linear models and trees work; ensembles best [EX] | 5 min, US equity index (Huddleston, Liu & Stentoft, JFEc 2023) | **Sharpe 0.98 after costs** [EX] | Our cross-section is 16 symbols plus the other FundingPips crosses. Use lagged 5/15/60-min returns of *all* symbols as inputs (we have some cross-market inputs; widen them) |
| **High-frequency factor-zoo returns** | Lagged high-frequency returns on many equity factors predict intraday market returns, with ML regularization and **separating continuous from jump increments** (jumps are not predictable) [EX] | Intraday US market (Aleti, Bollerslev & Siggaard, Management Science 2025) | "Sizeable out-of-sample Sharpe ratios and alphas after transaction costs" for ETF strategies [EX]; numbers n/s | We lack stock factors. Transferable ideas: **split returns into continuous and jump parts** and give the model only the continuous part as momentum input |
| **Realized higher moments and jumps** | Realized skewness (−) and kurtosis (+) predict **next-week** stock returns in the cross-section; realized volatility does not [EX] | Weekly, US stocks (Amaya, Christoffersen, Jacobs & Vasquez, JFE 2015) | n/s | Uncertain at 4 h in FX, indices and metals. Test realized skew, kurtosis and jump share over 1-day and 5-day windows as slow state features, not as signals |
| **Volatility- and time-of-day normalization** | Intraday volatility is a product of a daily level and a strong **intraday periodic component** in FX and equities [EX] (Andersen & Bollerslev, JEF 1997) | 5-min FX and equity | n/a (a data-cleaning result) | Divide every return, range and tick-volume input by its **same-time-of-day** norm (e.g. a 60-day median for that 5-min slot) and by a daily vol forecast. This stops the model learning session effects as signal |
| **Tick volume** | Practitioner study: tick counts track ECN-traded FX volume closely (a "90%" figure is quoted) [EX, PR] (Marney 2011, via Varianse/Paracurve PDFs) | Hourly FX | n/a | Our tick volume is a reasonable activity proxy. Normalize it by time of day as above |
| **Flow and calendar state** (from Workstream A) | Dealer gamma switches intraday momentum on and off (Baltussen et al. 2021; Dim, Eraker & Vilkov) [EX]; month-end rebalancing drift predicts next-day equity returns (Harvey et al.) [EX]; Treasury auction pressure (Fleming, Liu & Nguyen 2026) [EX] | Daily and intraday, US | See IDEAS.md C1, C2, C4 | **New inputs** for the 4 h model (proposal P1 below) |
| **News-regime labels** | LLM-classified news narratives behind market jumps; macro-news jumps carry the largest priced premium [EX] (He, arXiv 2604.13458, 2026) | Around the clock, US | "High out-of-sample Sharpe" for an annually rebalanced factor [EX] | Too heavy for us now. Our news-timing inputs cover the timing part |

### 2.2 Labels
- **Triple barrier:** label by which of the profit barrier, loss barrier or time barrier is hit first. It matches how trades are actually closed, unlike fixed-horizon labels that ignore the path [EX] (López de Prado 2018; summarized in the Mlfin.py docs).
  - A controlled comparison with fixed-horizon labels on the *same* model was not found in peer-reviewed work.
  - One capstone study (Singh & Joubert, Hudson & Thames) finds that **event-based sampling + triple barrier + meta-labeling** improves strategy metrics [EX, PR].
  - A Korean-market paper (arXiv 2504.02249) applies triple-barrier labels to OHLCV [EX]. Results n/s.
- **Trend scanning:** for each observation, fit linear trends over several look-ahead windows and label by the sign of the **maximum-t** trend, or 0 if none is significant [EX] (López de Prado, *Machine Learning for Asset Managers*, 2020).
  - Useful at our horizon because it lets the label choose between reversion and trend windows, which ties to §1 point 2.
  - No out-of-sample performance comparison was seen [n/s].
- **Recommendation:** keep the current target for the primary model. Use the **triple-barrier outcome of our actual trades** (with our real stop and target) as the **meta-label** (P2). Trend-scanning labels are a secondary experiment (P6).

### 2.3 Selectivity: meta-labeling, conformal prediction, abstention
- **Meta-labeling** (Joubert, *Journal of Financial Data Science* 2022, "Meta-Labeling: Theory and Framework"): a secondary ML model sits on top of a primary strategy to **filter false positives and size bets**. It improves Sharpe and drawdown in controlled experiments [EX]; magnitudes n/s. Code base: Hudson & Thames `meta-labeling` repository [EX].
- **Selective classification** (Chalkidis et al., "Trading via Selective Classification", ACM ICAIF 2021; arXiv 2110.14914):
  - Walk-forward on **commodity futures**, with logistic regression, random forests, feed-forward and recurrent nets.
  - Selective (abstaining) classifiers had **better accuracy and better backtests** than non-selective ones [EX]. Magnitudes n/s.
- **Conformal prediction:** distribution-free prediction sets with coverage guarantees. Conformal portfolio-selection work (Kato 2024, arXiv 2410.16333; and a Springer chapter on adaptive conformal portfolio selection) reports conformalized rules beating non-conformal ones "across multiple performance metrics" [EX]. Which study the quote belongs to was not pinned down.
  - For us, use it to **calibrate an abstention threshold**: trade only when the conformal set for the sign excludes the opposite sign.
- **Evidence strength:** moderate for the idea, weak for the size of the gain. It is mostly practitioner and conference work.

### 2.4 Regime models
- **HMM with side information for intraday momentum** ("Hidden Markov Models Applied To Intraday Momentum Trading With Side Information", arXiv 2006.08307, 2020; authors not checked): a latent momentum state avoids the lag of filters.
  - Side information: a **ratio of realized volatilities** and **intraday seasonality**. Model selection prefers 2–3 states.
  - Reported **Sharpe > 2.0 in simulation on E-mini S&P 500** [EX]. That is a single-market simulation, so treat it as weak evidence.
- **Observable regime variables** are cheaper and better grounded than latent states: dealer gamma sign, VIX term structure (VIX/VIX3M), realized-vol percentile and news-day flags. The gamma evidence is peer-reviewed (Baltussen et al. 2021; Dim, Eraker & Vilkov) [EX].

### 2.5 Ensembles, complexity and training windows
- **Complexity:** Kelly, Malamud & Zhou (JF 2024) argue that very high-parameter models improve return prediction [EX]. Nagel ("Seemingly Virtuous Complexity in Return Prediction", NBER WP 34104, 2025) shows the result **reduces to a simple volatility-timed momentum strategy** [EX]. Buncic (2025) and Cartea, Jin & Shi (2025) raise further critiques [EX].
  - Lesson for us: large models on price-only inputs often re-learn momentum times volatility. Our attention and MoE failures fit this.
- **Ensembles:** in the largest 5-minute study, ensembles beat single models across time [EX] (Huddleston et al. 2023). Cheap version for us: average across random seeds, feature subsets and training windows rather than adding depth.
- **Training windows and re-estimation:** in volatility forecasting, the **fitting scheme** (training window and re-estimation frequency) mattered more than model class. A well-fitted linear HAR beat tuned ML on 1,455 stocks, and performance **deteriorated when not re-estimated daily**, even at 2–5-day refits [EX] (Audrino & Chassot, *International Journal of Forecasting* 2025; arXiv 2406.08041).
  - That was **volatility**, not returns. We already found that 1–2-year windows and monthly or two-weekly retraining did not help our return model.
  - Next test: **daily incremental refits** of a cheap linear or ridge overlay on top of the frozen GBM/NN, not full retrains.
- **Market-wide evidence of difficulty:** in the **M6** competition (Feb 2022–Feb 2023), **only 23.3%** of teams beat the forecast benchmark, **28.8%** beat the portfolio benchmark, and **6.7%** beat both [EX] (Makridakis et al., IJF 2025). Be sceptical of small in-sample gains.

### 2.6 What does NOT work (benchmark and negative studies)
| Study | Setting | Result |
|---|---|---|
| Mesfin (arXiv 2605.04004, 2026) | MNQ, 5-min OHLCV, 947 days 2021–2025, 14 signal families, walk-forward, 2-point friction | **None passed**. Max gross 0.07–1.50 points/trade, below the 2-point friction [EX] |
| Mesfin (arXiv 2605.17724, 2026) | MNQ, LSTM vs gradient boosting on 5-min OHLCV, 944 days | Out-of-sample accuracy **50.00–50.89%** (GBM) and **50.59%** (LSTM); permutation p = 0.135 and 0.515; unstable feature importance [EX] |
| Makridakis et al. (M6, IJF 2025) | Real-time stock/ETF forecasting and portfolios | Majority underperformed benchmarks (see above) [EX] |
| Nagel (NBER WP 34104, 2025) | "Complexity" models | Gains reduce to volatility-timed momentum [EX] |
| Audrino & Chassot (IJF 2025) | Volatility, 1,455 stocks | Tuned ML fails to beat a properly refitted HAR [EX] |
| Our own tests (brief) | 4 h model | 2 h horizon, engineered cross-asset factors, attention/MoE, 1–2-year windows, recency weights, frequent retraining, FX-only, per-asset-class, equity-curve filters, 2.5R targets, trailing and partial exits: **no improvement** |

### 2.7 Validation standards to adopt
- **Purged k-fold with an embargo**, and combinatorial purged CV where compute allows, to avoid label-overlap leakage with 4 h labels [EX] (López de Prado 2018; skfolio/mlfinlab implementations).
- **Deflated Sharpe Ratio**, which corrects for selection over many trials and for non-normal returns [EX] (Bailey & López de Prado 2014), and the **probability of backtest overfitting** [EX] (Bailey et al.).
- Report results by year. Our 2025–26 fall should be tested for significance against 2018–24, since the per-year SE of mean R is large with ~300–500 trades/yr [D: ~1–2 trades/day × 252].

## 3. Concrete, testable proposals (ranked)

| # | Proposal | Why (source) | Reported effect | Pre-registered test |
|---|---|---|---|---|
| **P1** | **Add mechanism-based state features** from Workstream A: GEX(t−1) percentile; 60/40 drift `z` and trading days to month-end (C1); auction-day flag and minutes to 13:00 ET (C4); FOMC blackout flag and days to FOMC; LETF flow proxy (C10); VIX/VIX3M | Gamma switches intraday momentum on and off [EX]; rebalancing drift predicts next-day returns (−17 bps) [EX]; auction pressure [EX] | Model-level effect n/s | Ablation: current model versus current + P1 features, same folds (purged CV, 2018–2026). Primary metric: mean R of the top-1% trades and Deflated Sharpe. Accept if mean R improves in 2025–26 **and** over the full sample, with overlapping-trade-adjusted t ≥ 2 |
| **P2** | **Meta-label or abstention layer** on the current top-1% signals: predict P(target before stop within 4 h) from signal features plus P1 states; trade and size only above a calibrated threshold (conformal or selective) | Joubert (JFDS 2022) [EX]; Chalkidis et al. (2021): selective classifiers beat non-selective in commodity-futures backtests [EX]; Singh & Joubert [EX, PR] | Improvements reported; magnitude n/s | Train on 2018–2022 signals, validate 2023, test 2024–26. Compare against the same trades unfiltered. Accept if R per trade rises and total R does not fall by more than 25% (fewer but better trades) |
| **P3** | **Time-of-day and vol normalization** of all return, range and tick-volume inputs, and **continuous/jump separation** of returns | Andersen & Bollerslev (1997) periodicity [EX]; Aleti, Bollerslev & Siggaard (2025) jump separation [EX] | n/s | Ablation as in P1 |
| **P4** | **Wider lagged cross-section:** lagged 5/15/60-min returns of all 16 symbols plus key FundingPips crosses (e.g. AUDJPY, EURAUD, GBPJPY) and STX50/FTSE100, fitted with **regularized** models (elastic net or GBM with strong shrinkage) | Huddleston et al. (2023): lagged cross-section, ensembles best, Sharpe 0.98 after costs at 5 min [EX] | 5-min equity only; 4 h effect n/s | Ablation. Also test a separate linear model on these inputs, blended 20–30% into the score |
| **P5** | **Horizon-mixing features:** sub-hour reversion features (last 5–30 min z-scores) *and* multi-hour trend features (4–24 h slope t-stats), with an interaction on volatility regime | Schmidhuber & Safari (2025): trend from a few hours upward, reversion below [EX] | n/s | Ablation |
| **P6** | **Trend-scanning labels** as an alternative target (look-ahead 1–4 h, choose the max-t window) | López de Prado (2020) [EX] | n/s | Train an alternative primary model; compare top-1% R on the same folds |
| **P7** | **Ensembling over seeds, windows and feature subsets** in place of deeper architectures | Huddleston et al. (2023) [EX]; Nagel (2025) [EX]; our attention/MoE failures | n/s | Average 10 seeds × 3 windows. Accept if variance falls without loss of mean R |
| **P8** | **Daily incremental recalibration** of a light overlay (ridge on the model's score plus the P1 states), keeping the heavy model frozen and retrained yearly | Audrino & Chassot (2025): re-estimation frequency dominates in vol forecasting [EX] | Vol forecasting only | Compare the frozen model alone against frozen + daily overlay on 2024–26 |

**What not to spend time on** (per literature and our results): deeper sequence models on price-only inputs, more complex architectures without new information, shorter training windows, and equity-curve filters.

## 4. Source list for this file
See `SOURCES.md` (section B) for full citations and URLs.
