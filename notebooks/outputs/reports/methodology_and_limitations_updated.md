# SupeRR Selector Season 2

## Methodology and Limitations

### 1. Dataset selection

-   Competitions: IPL and T20I.
-   Period: 2022 onwards, through the available 2026 data.
-   Selected matches: 853.
-   Matches with ball-by-ball data: 837.
-   Matches without ball-by-ball data: 16.
-   Super Over deliveries are excluded from regulation-innings rankings.

### 2. Pressure identification

A proxy pressure score is calculated using:

Pressure Score = 100 \* (0.60 \* innings progress + 0.40 \* wicket
pressure)

-   Innings progress uses known legal balls before the delivery, divided
    by a reference of 120 balls.
-   Wicket pressure uses wickets lost before the delivery, divided by
    10.
-   Both components are capped at 1.
-   Deliveries with uncertain prior legal-ball counts are excluded.
-   High pressure is defined as a score of 50 or higher.

This is a simplified pressure proxy. It is not a validated
win-probability model and does not include target, required run rate or
actual team score.

### 3. Batter ranking

-   Minimum sample: 20 balls faced.
-   High-pressure runs: 40%.
-   Strike-rate percentile: 30%.
-   Boundary-percentage percentile: 15%.
-   Sample-sufficiency indicator: 15%.
-   Sample sufficiency is capped at 100 balls.

Strike rate = high-pressure batter runs / balls faced \* 100.

Boundary percentage = boundary runs / high-pressure batter runs \* 100.

Wides are excluded from balls faced. Other and Penalty delivery
classifications are included in the current balls-faced proxy.

### 4. Bowler ranking

-   Minimum sample for standard interpretation: 24 known legal balls.
-   High-pressure bowler-credited wickets percentile: 45%.
-   Wickets per 24 known legal balls percentile: 30%.
-   Sample-sufficiency indicator: 25%.
-   Sample sufficiency is capped at 120 known legal balls.

Only Bowled, Caught, LBW, Stump and Hit Wicket dismissals are counted as
bowler-credited wickets.

### 5. Candidate-restricted competition ranking

The competition supplied a list of 20 eligible candidates. The final
competition Top 10 batter and bowler leaderboards are calculated only
among those candidates.

The candidate-restricted scores are percentile-based comparative indices
within that 20-player candidate pool. They should not be compared
directly with scores from the exploratory full-player-pool analysis,
because the comparison populations differ.

The final candidate-restricted batter Top 10 is:

    Rank Player                   Score
  ------ ---------------------- -------
       1 Dinesh Karthik           94.00
       2 Rashid Khan              87.75
       3 Virat Kohli              84.00
       4 Abdul Samad              83.75
       5 Faf du Plessis           82.75
       6 Mahendra Singh Dhoni     82.75
       7 Ravindra Jadeja          77.75
       8 Shikhar Dhawan           71.00
       9 Rohit Sharma             70.15
      10 Haider Ali               54.20

The final candidate-restricted bowler Top 10 is:

  -----------------------------------------------------------------------------------
          Rank Player            Score   High-pressure   High-pressure Confidence
                                               Wickets     Legal Balls 
  ------------ ---------- ------------ --------------- --------------- --------------
             1 Rashid            95.50              80           1,008 Strong
               Khan                                                    

             2 Dwayne        88.791667               9              95 Limited
               Bravo                                                   

             3 Ravindra          88.75              11             294 Strong
               Jadeja                                                  

             4 Piyush        86.208333               7             115 Limited
               Chawla                                                  

             5 Ishant        78.208333               6             100 Limited
               Sharma                                                  

             6 Haider Ali    76.458333               6              70 Limited

             7 Amit              69.00               4              36 Limited
               Mishra                                                  

             8 Basil         62.083333               2              64 Limited
               Hameed                                                  

             9 Dinesh           25.625               0               6 Insufficient
               Karthik                                                 

            10 Bashir           25.625               0               6 Insufficient
               Ahmad                                                   
  -----------------------------------------------------------------------------------

Bowler confidence is interpreted as: - Strong: at least 120
high-pressure legal balls. - Limited: 24--119 high-pressure legal
balls. - Insufficient: fewer than 24 high-pressure legal balls.

Dinesh Karthik and Bashir Ahmad have only 6 high-pressure legal balls
each. They are included to complete the required candidate-restricted
Top 10, but they do not meet the 24-ball minimum sample for reliable
bowler interpretation. Their rankings should therefore be treated as
insufficiently supported by sample volume.

### 6. Data limitations

-   The source runs field was validated against two scorecards and
    appears to represent batter runs, not total team runs.
-   Actual extras-run amounts are not reliably available.
-   Economy rate, bowling average and true runs conceded are therefore
    not calculated.
-   The 120-ball reference is a simplifying assumption.
-   Revised-overs metadata semantics have not been independently
    validated.
-   There are 260 deliveries with unknown legal-ball status. Later
    delivery states affected by these unknown records are excluded from
    ranking eligibility.
-   The pressure score does not measure actual match-winning probability
    or required run rate.
-   Ranking weights and sample thresholds are provisional design
    choices, not statistically trained parameters.
-   The original full-player-pool validation results do not
    automatically validate the candidate-restricted leaderboard.
    Candidate-restricted rankings require their own sensitivity checks
    before making equivalent stability claims.

### 7. Interpretation

The composite scores are comparative project indices under the stated
assumptions. They should not be presented as official player ratings or
definitive measures of ability.

The exploratory full-player-pool results and final candidate-restricted
competition results use different comparison groups. They should be
labelled separately in presentations, reports and submissions.
