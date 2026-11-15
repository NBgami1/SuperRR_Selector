# SupeRR Selector Season 2
## Methodology and Limitations

### 1. Dataset selection
- Competitions: IPL and T20I.
- Period: 2022 onwards, through the available 2026 data.
- Selected matches: 853.
- Matches with ball-by-ball data: 837.
- Matches without ball-by-ball data: 16.
- Super Over deliveries are excluded from regulation-innings rankings.

### 2. Pressure identification
A proxy pressure score is calculated using:

Pressure Score =
100 * (0.60 * innings progress + 0.40 * wicket pressure)

- Innings progress uses known legal balls before the delivery,
  divided by a reference of 120 balls.
- Wicket pressure uses wickets lost before the delivery,
  divided by 10.
- Both components are capped at 1.
- Deliveries with uncertain prior legal-ball counts are excluded.
- High pressure is defined as a score of 50 or higher.

This is a simplified pressure proxy. It is not a validated
win-probability model and does not include target, required
run rate or actual team score.

### 3. Batter ranking
- Minimum sample: 20 balls faced.
- High-pressure runs: 40%.
- Strike-rate percentile: 30%.
- Boundary-percentage percentile: 15%.
- Sample-sufficiency indicator: 15%.
- Sample sufficiency is capped at 100 balls.

Strike rate = high-pressure batter runs / balls faced * 100.

Boundary percentage = boundary runs / high-pressure batter runs * 100.

Wides are excluded from balls faced. Other and Penalty delivery
classifications are included in the current balls-faced proxy.

### 4. Bowler ranking
- Minimum sample: 24 known legal balls.
- High-pressure bowler-credited wickets percentile: 45%.
- Wickets per 24 known legal balls percentile: 30%.
- Sample-sufficiency indicator: 25%.
- Sample sufficiency is capped at 120 known legal balls.

Only Bowled, Caught, LBW, Stump and Hit Wicket dismissals
are counted as bowler-credited wickets.

### 5. Data limitations
- The source runs field was validated against two scorecards
  and appears to represent batter runs, not total team runs.
- Actual extras-run amounts are not reliably available.
- Economy rate, bowling average and true runs conceded
  are therefore not calculated.
- The 120-ball reference is a simplifying assumption.
- Revised-overs metadata semantics have not been independently
  validated.
- There are 260 deliveries with unknown legal-ball status.
  Later delivery states affected by these unknown records
  are excluded from ranking eligibility.
- The pressure score does not measure actual match-winning
  probability or required run rate.
- Ranking weights and sample thresholds are provisional
  design choices, not statistically trained parameters.

### 6. Interpretation
The composite scores are comparative project indices
under the stated assumptions. They should not be presented
as official player ratings or definitive measures of ability.