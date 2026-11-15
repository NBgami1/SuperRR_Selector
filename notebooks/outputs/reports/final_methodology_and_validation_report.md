
# SupeRR Selector Season 2
## Methodology, Results and Validation Report

### 1. Project Overview

This project develops an explainable statistical framework to identify
the Top 10 batters and Top 10 bowlers performing under high-pressure
situations in T20 cricket.

The analysis covers IPL/T20 and T20 International (T20I) matches
from 2022 to 2026.

The framework uses ball-by-ball data, a rule-based pressure proxy,
role-specific performance indicators, percentile-based scoring,
and sensitivity analysis.

The pressure score is a statistical proxy and should not be interpreted
as a direct measurement of a player's psychological pressure.

### 2. Dataset and Coverage

The filtered dataset contains:

- 853 selected matches.
- 194,014 ball-by-ball deliveries.
- 837 matches with ball-by-ball records.
- 16 matches without ball-by-ball records.
- Zero orphan delivery records.
- Coverage period: 2022 to 2026.

The regulation-innings analysis contains 193,988 deliveries.
A further 26 Super Over deliveries were excluded.

The format coverage is:

| Format | Matches | High-pressure deliveries |
|---|---:|---:|
| T20 | 367 | 27,595 |
| T20I | 470 | 34,624 |
| Total | 837 selected matches | 62,219 |

The high-pressure analysis covers 816 matches.

### 3. Data Preparation

The data preparation process included:

1. Filtering IPL/T20 and T20I competitions from 2022 onward.
2. Linking ball-by-ball records to match and competition metadata.
3. Restricting the main pressure analysis to regulation innings 1 and 2.
4. Classifying known legal and illegal deliveries.
5. Identifying bowler-credited dismissals.
6. Reconstructing innings state before each delivery.
7. Excluding deliveries whose preceding state could not be reconstructed
   reliably because of unknown delivery classifications.

Bowler-credited wickets include Bowled, Caught, LBW, Stumped and
Hit Wicket dismissals.

A total of 9,905 bowler-credited wickets were identified in the
regulation dataset.

### 4. Pressure Model

The pressure score is calculated from innings progress and wickets lost.

P = 100 × (0.60 × innings progress
           + 0.40 × wicket pressure)

Where:

- Innings progress = legal balls before the delivery / 120,
  capped at 1.
- Wicket pressure = wickets lost before the delivery / 10,
  capped at 1.

A delivery is classified as high pressure when:

- Pressure score is at least 50.
- The reconstructed prior innings state is complete.

The model produced:

- 184,726 eligible deliveries with complete prior state.
- 9,262 deliveries classified as uncertain.
- 62,219 high-pressure deliveries.
- 816 matches represented in high-pressure analysis.
- 4,072 bowler-credited wickets in high-pressure deliveries.

### 5. Batter Ranking Methodology

Minimum sample requirement: 20 balls faced.

The batter score uses four components:

| Component | Weight |
|---|---:|
| Runs percentile | 40% |
| Strike-rate percentile | 30% |
| Boundary percentage percentile | 15% |
| Sample reliability | 15% |

Sample reliability is calculated as balls faced / 100,
capped at 1.

The final score is a weighted combination of percentile values,
scaled to 100.

### 6. Bowler Ranking Methodology

Minimum sample requirement: 24 legal balls.

The bowler score uses three components:

| Component | Weight |
|---|---:|
| Bowler-credited wickets percentile | 45% |
| Wickets per 24 legal balls percentile | 30% |
| Sample sufficiency | 25% |

Sample sufficiency is calculated as legal balls / 120,
capped at 1.

### 7. Combined Top 10 Results

#### Batters

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

#### Bowlers

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

### 8. Model Validation

The following validation exercises were completed.

#### 8.1 Original Model Reproduction

The original ranking calculation was reproduced.

- Batter Top 10 overlap: 10/10.
- Bowler Top 10 overlap: 10/10.
- Maximum score difference: 0 for both roles.

#### 8.2 Scoring Weight Sensitivity

Alternative scoring weights were tested.

- Batter Top 10 overlap: 9/10 under both alternatives.
- Bowler Top 10 overlap: 10/10 under both alternatives.

The results indicate that the leading players are generally stable
under the tested weight variations, although some batter membership
changes occur.

#### 8.3 Sample-Size Sensitivity

Batter minimum thresholds tested: 20, 30, 40, 50, 75 and 100 balls.

Bowler minimum thresholds tested: 24, 36, 48, 60, 90 and 120 legal balls.

The original Top 10 membership remained unchanged at all tested
thresholds for both roles.

#### 8.4 Pressure Denominator Sensitivity

A revised-duration alternative was tested using available revised
innings metadata instead of the fixed 120-ball denominator.

- 3,135 deliveries were associated with revised-duration metadata.
- 550 high-pressure classifications changed across 28 matches.
- Batter Top 10 overlap with the original model: 9/10.
- Bowler Top 10 overlap with the original model: 9/10.

The fixed 120-ball model was retained as the primary model for
consistent comparison. The revised-duration analysis is treated
as a sensitivity test, not evidence that either version is more accurate.

#### 8.5 IPL/T20 and T20I Comparison

Combined Top 10 membership overlap:

| Role | Combined vs T20 | Combined vs T20I |
|---|---:|---:|
| Batter | 7/10 | 4/10 |
| Bowler | 4/10 | 6/10 |

Common membership between the separate format-specific Top 10 lists:

- Batters: 3 players.
- Bowlers: 2 players.

These comparisons measure membership overlap only.
Separate format rankings use within-format percentiles, so their
scores should not be compared directly across formats.

### 9. Seasonal High-Pressure Consistency

Separate seasonal rankings were calculated for T20 and T20I
from 2022 through 2026.

Each format-season produced a Top 10 list for batters and bowlers.

The seasonal analysis identified:

- 925 eligible batter player-season records.
- 836 eligible bowler player-season records.
- 24 batters with at least two seasonal Top 10 appearances.
- 23 bowlers with at least two seasonal Top 10 appearances.

Examples of repeated performers:

#### Batters

- Andre Russell: 4 T20 seasonal Top 10 appearances.
- Heinrich Klaasen: 3 T20 appearances.
- Nicholas Pooran: 3 T20 appearances.
- Tim David: 3 T20I appearances.

#### Bowlers

- Yuzvendra Chahal: 3 T20 seasonal Top 10 appearances.
- Rashid Khan: 3 T20 appearances.
- Haris Rauf: 3 T20I appearances.
- Arshdeep Singh: 3 T20I appearances.

These results describe consistency in the seasonal high-pressure
sample, not overall season performance.

### 10. Limitations

1. The pressure score is a proxy based on innings progress and
   wickets lost. It does not measure psychological pressure directly.

2. Reliable team totals, target state and chase requirements were
   not available for the full dataset. The model is therefore not
   target-aware.

3. The fixed 120-ball reference assumes a standard 20-over innings.
   Shortened and revised innings are not fully represented.

4. Some delivery classifications are unknown. Deliveries following
   an unknown prior state are excluded from pressure eligibility.

5. Batter runs are used as recorded in the available data.
   They should not be interpreted as complete team totals.

6. The analysis does not use an external expert-labelled pressure
   dataset or independently validated psychological-pressure labels.

7. Percentile-based scores are relative to the selected player pool.
   They are not absolute measures of player ability.

8. Seasonal rankings are based on high-pressure deliveries only.

9. Minimum sample requirements reduce low-volume observations but
   do not eliminate every possible sample-size bias.

### 11. Conclusion

The project presents a reproducible, explainable statistical
framework for ranking batters and bowlers in high-pressure T20
situations.

The original rankings were reproduced exactly, and the Top 10
membership showed substantial stability under the tested
sample-size and scoring-weight alternatives.

Format-specific and seasonal analyses provide additional insight
into differences between T20 and T20I cricket and the repeat
appearance of players in high-pressure Top 10 lists.

The framework should be considered a data-driven pressure proxy
and ranking methodology rather than a definitive measurement
of actual psychological pressure.

### 12. Future Improvements

- Incorporate reliable team score and target information.
- Add required run rate and wickets-in-hand for chase situations.
- Improve handling of DLS and shortened matches.
- Validate pressure categories against expert-labelled situations.
- Test alternative statistical models and uncertainty estimates.
- Expand the analysis with additional seasons and competitions.

---
Report generated for SupeRR Selector Season 2.
