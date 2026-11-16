# SupeRR Selector Season 2
## Identifying Top T20 Batters and Bowlers Under Pressure

## 1. Project Overview

SupeRR Selector Season 2 is a cricket analytics project that identifies the Top 10 batters and Top 10 bowlers performing in high-pressure situations using ball-by-ball data from IPL/T20 and T20 International matches from 2022–2026.

The project combines:

- Ball-by-ball data processing
- Innings-state reconstruction
- Rule-based pressure scoring
- Role-specific player performance metrics
- Percentile-based player rankings
- Sensitivity and robustness testing
- Format-wise and seasonal comparisons
- An interactive Streamlit dashboard

**Important:** The pressure score is a statistical proxy based on innings progress and wickets lost. It does not directly measure psychological pressure.

## 2. Project Highlights

| Metric | Result |
|---|---:|
| Selected competitions | 139 |
| Selected matches | 853 |
| Matches with ball-by-ball data | 837 |
| Ball-by-ball deliveries | 194,014 |
| Regulation-innings deliveries | 193,988 |
| Eligible deliveries with complete prior state | 184,726 |
| High-pressure deliveries | 62,219 |
| Matches represented in high-pressure analysis | 816 |
| Bowler-credited wickets in high-pressure deliveries | 4,072 |

**Coverage:** 2022–2026.

## 3. Final Candidate-Restricted Leaderboards

The official competition submission ranks players from the 20 candidates supplied for the SupeRR Selector Season 2 challenge.

These results are distinct from exploratory full-player-pool rankings.

### 3.1 Top 10 Batters

| Rank | Player | Score | Pressure Runs | Pressure Strike Rate |
|---:|---|---:|---:|---:|
| 1 | Dinesh Karthik | 94.00 | 915 | 165.16 |
| 2 | Rashid Khan | 87.75 | 707 | 157.81 |
| 3 | Virat Kohli | 84.00 | 487 | 166.78 |
| 4 | Abdul Samad | 83.75 | 540 | 164.63 |
| 5 | Faf du Plessis | 82.75 | 170 | 168.32 |
| 6 | Mahendra Singh Dhoni | 82.75 | 598 | 154.92 |
| 7 | Ravindra Jadeja | 77.75 | 864 | 134.37 |
| 8 | Shikhar Dhawan | 71.00 | 118 | 147.50 |
| 9 | Rohit Sharma | 70.15 | 100 | 163.93 |
| 10 | Haider Ali | 54.20 | 68 | 117.24 |

### 3.2 Top 10 Bowlers

| Rank | Player | Score | Pressure Wickets | Pressure Legal Balls | Confidence |
|---:|---|---:|---:|---:|---|
| 1 | Rashid Khan | 95.50 | 80 | 1,008 | Strong |
| 2 | Dwayne Bravo | 88.79 | 9 | 95 | Limited |
| 3 | Ravindra Jadeja | 88.75 | 11 | 294 | Strong |
| 4 | Piyush Chawla | 86.21 | 7 | 115 | Limited |
| 5 | Ishant Sharma | 78.21 | 6 | 100 | Limited |
| 6 | Haider Ali | 76.46 | 6 | 70 | Limited |
| 7 | Amit Mishra | 69.00 | 4 | 36 | Limited |
| 8 | Basil Hameed | 62.08 | 2 | 64 | Limited |
| 9 | Dinesh Karthik | 25.63 | 0 | 6 | Insufficient |
| 10 | Bashir Ahmad | 25.63 | 0 | 6 | Insufficient |

**Interpretation:** The last two bowlers have insufficient high-pressure bowling samples. They are included to fulfil the required Top 10 output, but their positions should not be treated as strong evidence of consistent bowling performance.

## 4. Methodology

### 4.1 Pressure Score

The model calculates pressure using innings progress and wickets lost.

**Formula:**

Pressure = 100 × (0.60 × Innings Progress + 0.40 × Wicket Pressure)

Where:

- Innings Progress = legal balls completed before the delivery / 120.
- Wicket Pressure = wickets lost before the delivery / 10.
- Both components are capped at 1.

A delivery is classified as high pressure when:

- Its pressure score is at least 50.
- Its reconstructed prior innings state is complete.

The model uses the state before the delivery to avoid using the outcome of that delivery when calculating its pressure.

### 4.2 Batter Ranking

The batter model uses the following metrics:

| Metric | Weight |
|---|---:|
| High-pressure runs percentile | 40% |
| Strike-rate percentile | 30% |
| Boundary-percentage percentile | 15% |
| Sample reliability | 15% |

Minimum sample requirement: 20 balls faced in high-pressure situations.

Strike rate is calculated as:

Strike Rate = (Runs Scored / Balls Faced) × 100

### 4.3 Bowler Ranking

The bowler model uses:

| Metric | Weight |
|---|---:|
| Bowler-credited wickets percentile | 45% |
| Wickets per 24 legal balls percentile | 30% |
| Sample sufficiency | 25% |

Minimum sample requirement for reliable interpretation: 24 high-pressure legal balls.

Wickets per 24 legal balls:

Wicket Rate = (High-Pressure Wickets / High-Pressure Legal Balls) × 24

### 4.4 Sample Confidence

Bowler sample confidence is classified as follows:

| High-pressure legal balls | Confidence |
|---:|---|
| 120 or more | Strong |
| 24–119 | Limited |
| Below 24 | Insufficient |

Candidates below the minimum threshold may still appear in the required Top 10, but their rankings must be interpreted cautiously.

### 4.5 Percentile-Based Scoring

The performance metrics are converted into percentile-based scores relative to the selected comparison pool.

The weighted scores are used to produce the final rankings.

The candidate-restricted competition leaderboard is generated from the supplied 20-player candidate list, rather than being treated as an unrestricted ranking of every player in the dataset.

## 5. Validation and Additional Analysis

The project includes the following validation exercises:

- Original model reproduction.
- Scoring-weight sensitivity analysis.
- Sample-size threshold sensitivity analysis.
- Fixed versus revised innings-duration pressure comparison.
- IPL/T20 versus T20I ranking comparison.
- Seasonal high-pressure rankings from 2022 to 2026.
- Repeat seasonal Top 10 appearance analysis.
- Pressure denominator and innings-state validation.

### Selected Validation Findings

- Original Top 10 membership remained unchanged under all tested stricter sample-size thresholds.
- Batter Top 10 overlap was 9/10 under the two alternative scoring-weight configurations.
- Bowler Top 10 overlap was 10/10 under those configurations.
- The revised-duration sensitivity test changed 550 pressure classifications across 28 matches.
- Seasonal analysis identified 24 repeat-performing batters and 23 repeat-performing bowlers, each with at least two seasonal Top 10 appearances.
- Original model reproduction achieved exact Top 10 reproduction for batters and bowlers, with zero maximum score difference.

These findings demonstrate robustness under the scenarios examined. They do not prove that the pressure proxy measures actual psychological pressure.

## 6. Interactive Streamlit Dashboard

The project includes an interactive dashboard with six sections:

1. Overview
2. Top 10 Batters
3. Top 10 Bowlers
4. Combined Leaderboard
5. Methodology
6. Project Information

The dashboard presents rankings, player statistics, sample-confidence information and downloadable leaderboard results.

### Run the Dashboard

Activate the project's Python environment and install the dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard from the project root:

```bash
python -m streamlit run app.py/streamlit_app.py
```

Windows PowerShell:

```powershell
python -m streamlit run .\app.py\streamlit_app.py
```

The application will be available at the local Streamlit URL displayed in the terminal, usually:

`http://localhost:8501`

## 7. Project Structure

```text
SupeRR_Selector_Season2/
│
├── app.py/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_model_validation.ipynb
│   │
│   └── outputs/
│       ├── reports/
│       ├── tables/
│       └── validation/
│
├── outputs/
│   └── tables/
│
├── .gitignore
├── README.md
└── requirements.txt
```

Raw and processed input datasets are not necessarily included in the public repository. The original input data should be obtained from its authorized source.

## 8. Important Output Files

### Main Rankings

- `top_10_batters.csv`
- `top_10_bowlers.csv`
- `combined_top_10_leaderboards.csv`

### Format-Wise Analysis

- `format_wise_batter_rankings.csv`
- `format_wise_bowler_rankings.csv`
- `ipl_t20i_top10_comparison.csv`

### Seasonal Analysis

- `seasonal_batter_rankings.csv`
- `seasonal_bowler_rankings.csv`
- `seasonal_batter_top10.csv`
- `seasonal_bowler_top10.csv`
- `batter_seasonal_consistency.csv`
- `bowler_seasonal_consistency.csv`
- `repeat_high_pressure_batters.csv`
- `repeat_high_pressure_bowlers.csv`

### Validation

- `batter_ranking_stability.csv`
- `bowler_ranking_stability.csv`
- `batter_sensitivity_results.csv`
- `bowler_sensitivity_results.csv`
- `batter_sample_threshold_tests.csv`
- `bowler_sample_threshold_tests.csv`
- `batter_scenario_comparison.csv`
- `bowler_scenario_comparison.csv`

### Documentation

- `final_methodology_and_validation_report.md`
- `methodology_and_limitations.md`

These outputs support inspection and reproducibility of the analysis.

## 9. Limitations

1. Pressure is estimated using innings progress and wickets lost, not measured psychological pressure.
2. Reliable team totals, target state and chase requirements were unavailable for the complete dataset.
3. A fixed 120-ball reference does not fully model shortened innings.
4. Unknown delivery classifications can make subsequent innings states ineligible.
5. Percentile scores depend on the selected player pool.
6. Seasonal rankings describe high-pressure performance only.
7. The framework has not been validated against external expert-labelled pressure data.
8. Small high-pressure samples can produce unstable player rankings.

## 10. Future Improvements

- Add target-aware pressure and required-run-rate features.
- Improve shortened-match and DLS handling.
- Incorporate reliable team-score reconstruction.
- Compare alternative statistical models.
- Validate against expert-labelled pressure situations.
- Extend the analysis to additional seasons and competitions.

## 11. Technologies Used

- Python
- Pandas
- NumPy
- Jupyter Notebook
- Streamlit
- Data visualization libraries

## 12. Reproducibility and Data Availability

The project includes exported rankings, validation tables and a methodology report to support inspection of the analysis.

The original input data should be obtained from its authorized source. Restricted, confidential or licensed raw datasets should not be uploaded to a public repository without permission.

## 13. Final Competition Output

The final competition submission consists of:

- `top_10_batters.csv`
- `top_10_bowlers.csv`
- `combined_top_10_leaderboards.csv`

The final candidate-restricted leaderboards rank the 20 supplied candidates using the project's pressure-performance scoring methodology.

The exported results and confidence indicators should be interpreted alongside the sample-size limitations and validation findings.

---

**SupeRR Selector Season 2 — Cricket Analytics Project**

Repository: https://github.com/NBgami1/SuperRR_Selector
