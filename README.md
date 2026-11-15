# SupeRR Selector Season 2
### Identifying Top T20 Batters and Bowlers Under Pressure

## Project Overview

SupeRR Selector is a cricket analytics project that uses ball-by-ball
data from IPL/T20 and T20 International matches (2022–2026) to identify
the Top 10 batters and Top 10 bowlers performing in high-pressure
situations.

The project combines:
- Ball-by-ball data processing
- Innings-state reconstruction
- Rule-based pressure scoring
- Role-specific player performance metrics
- Percentile-based player rankings
- Sensitivity and robustness testing
- Format-wise and seasonal comparisons
- An interactive Streamlit dashboard

**Important:** The pressure score is a statistical proxy based on
innings progress and wickets lost. It is not a direct measurement
of psychological pressure.

## Project Highlights

| Metric | Result |
|---|---:|
| Selected matches | 853 |
| Matches with ball-by-ball data | 837 |
| Ball-by-ball deliveries | 194,014 |
| Regulation-innings deliveries | 193,988 |
| Eligible deliveries with complete prior state | 184,726 |
| High-pressure deliveries | 62,219 |
| Matches represented in high-pressure analysis | 816 |
| Bowler-credited wickets in high-pressure deliveries | 4,072 |

Coverage: 2022–2026.

## Combined Top 10 Batters

| Rank | Player | Score |
|---:|---|---:|
| 1 | Suryakumar Yadav | 97.80 |
| 2 | Tim David | 95.71 |
| 3 | Nicholas Pooran | 95.37 |
| 4 | Andre Russell | 94.70 |
| 5 | Shreyas Iyer | 93.80 |
| 6 | Heinrich Klaasen | 93.11 |
| 7 | Jos Buttler | 92.92 |
| 8 | Ashutosh Sharma | 91.89 |
| 9 | Marcus Stoinis | 91.87 |
| 10 | Harry Brook | 91.79 |

## Combined Top 10 Bowlers

| Rank | Player | Score |
|---:|---|---:|
| 1 | Mitchell Starc | 94.09 |
| 2 | Haris Rauf | 93.89 |
| 3 | Kuldeep Yadav | 93.06 |
| 4 | Yuzvendra Chahal | 92.63 |
| 5 | Wanindu Hasaranga | 92.50 |
| 6 | Shaheen Afridi | 92.48 |
| 7 | Mark Adair | 91.73 |
| 8 | Josh Hazlewood | 91.51 |
| 9 | Andre Russell | 90.87 |
| 10 | Matheesha Pathirana | 90.83 |

## Methodology

### 1. Pressure Score

The model calculates pressure using innings progress and wickets lost:

`Pressure = 100 × (0.60 × innings progress + 0.40 × wicket pressure)`

Where:

- Innings progress = legal balls before the delivery / 120.
- Wicket pressure = wickets lost before the delivery / 10.
- Both components are capped at 1.

A delivery is considered high pressure when its score is at least 50
and its reconstructed prior innings state is complete.

### 2. Batter Ranking

Minimum sample: 20 balls faced.

| Metric | Weight |
|---|---:|
| Runs percentile | 40% |
| Strike-rate percentile | 30% |
| Boundary percentage percentile | 15% |
| Sample reliability | 15% |

### 3. Bowler Ranking

Minimum sample: 24 legal balls.

| Metric | Weight |
|---|---:|
| Bowler-credited wickets percentile | 45% |
| Wickets per 24 legal balls percentile | 30% |
| Sample sufficiency | 25% |

Scores are weighted percentile-based scores relative to the selected
comparison pool.

## Validation and Additional Analysis

The project includes:

- Original model reproduction: exact Top 10 reproduction for batters
  and bowlers, with zero maximum score difference.
- Scoring-weight sensitivity analysis.
- Sample-size threshold sensitivity analysis.
- Fixed versus revised innings-duration pressure comparison.
- IPL/T20 versus T20I ranking comparison.
- Seasonal high-pressure rankings from 2022 to 2026.
- Repeat seasonal Top 10 appearance analysis.

### Selected Validation Findings

- Original Top 10 membership remained unchanged under all tested
  stricter sample-size thresholds.
- Batter Top 10 overlap was 9/10 under the two alternative scoring
  weight configurations.
- Bowler Top 10 overlap was 10/10 under those configurations.
- The revised-duration sensitivity test changed 550 pressure
  classifications across 28 matches.
- Seasonal analysis identified 24 repeat-performing batters and
  23 repeat-performing bowlers, each with at least two seasonal
  Top 10 appearances.

These tests demonstrate robustness under the scenarios examined;
they do not prove that the pressure proxy measures actual
psychological pressure.

## Interactive Dashboard

The project includes a Streamlit dashboard with:

- Overview
- Batter rankings
- Bowler rankings
- Methodology
- Download Centre

### Run the Dashboard

Activate the project's Python environment, install the dependencies,
and run:

```bash
python -m streamlit run app.py/streamlit_app.py
```

If running from Windows PowerShell:

```powershell
python -m streamlit run .\app.py\streamlit_app.py
```

## Project Structure

```text
SupeRR_Selector_Season2/
│
├── app.py/
│   └── streamlit_app.py
│
├── data/
│   └── processed/
│
├── notebooks/
│   └── outputs/
│       ├── tables/
│       ├── validation/
│       └── reports/
│
├── README.md
└── requirements.txt
```

Additional notebooks and source files may be present in the repository.

## Output Files

Important exported results include:

**Main rankings**
- `top_10_batters.csv`
- `top_10_bowlers.csv`
- `combined_top_10_leaderboards.csv`

**Format-wise analysis**
- `format_wise_batter_rankings.csv`
- `format_wise_bowler_rankings.csv`
- `ipl_t20i_top10_comparison.csv`

**Seasonal analysis**
- `seasonal_batter_rankings.csv`
- `seasonal_bowler_rankings.csv`
- `seasonal_batter_top10.csv`
- `seasonal_bowler_top10.csv`
- `batter_seasonal_consistency.csv`
- `bowler_seasonal_consistency.csv`
- `repeat_high_pressure_batters.csv`
- `repeat_high_pressure_bowlers.csv`

**Documentation**
- `final_methodology_and_validation_report.md`

## Limitations

1. Pressure is estimated using innings progress and wickets lost,
   not measured psychological pressure.
2. Reliable team totals, target state and chase requirements were
   unavailable for the complete dataset.
3. A fixed 120-ball reference does not fully model shortened innings.
4. Unknown delivery classifications can make subsequent innings
   states ineligible.
5. Percentile scores depend on the selected player pool.
6. Seasonal rankings describe high-pressure performance only.
7. The framework has not been validated against external
   expert-labelled pressure data.

## Future Improvements

- Add target-aware pressure and required run-rate features.
- Improve shortened-match and DLS handling.
- Incorporate reliable team-score reconstruction.
- Compare alternative statistical models.
- Validate against expert-labelled pressure situations.
- Extend the analysis to additional seasons and competitions.

## Technologies

Python, Pandas, NumPy, Jupyter Notebook, Streamlit and data
visualization libraries.

## Reproducibility

The project includes exported rankings, validation tables and a
methodology report to support inspection of the analysis.

The original input data should be obtained from its authorized
source. Do not upload restricted, confidential or licensed raw
datasets to a public repository without permission.

---

**SupeRR Selector Season 2 — Cricket Analytics Project**
