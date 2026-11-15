
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="SupeRR Selector Season 2",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 SupeRR Selector – Season 2")

st.markdown(
    "### Pressure Performance Analytics Dashboard\n"
    "Identifying the Top 10 batters and bowlers under pressure."
)

# ============================================================
# 2. FILE PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
TABLE_DIR = BASE_DIR / "notebooks" / "outputs" / "tables"

BATTER_FILE = TABLE_DIR / "top_10_batters.csv"
BOWLER_FILE = TABLE_DIR / "top_10_bowlers.csv"
COMBINED_FILE = TABLE_DIR / "combined_top_10_leaderboards.csv"

# ============================================================
# 3. LOAD CSV FILES
# ============================================================

@st.cache_data
def load_data():

    batters = pd.read_csv(BATTER_FILE)
    bowlers = pd.read_csv(BOWLER_FILE)
    combined = pd.read_csv(COMBINED_FILE)

    # Remove accidental spaces from column names
    for df in [batters, bowlers, combined]:
        df.columns = df.columns.astype(str).str.strip()

    return batters, bowlers, combined


try:
    batters, bowlers, combined = load_data()

except FileNotFoundError as error:
    st.error("A required leaderboard CSV file was not found.")
    st.code(str(error))
    st.write("Expected folder:", str(TABLE_DIR))
    st.stop()

except Exception as error:
    st.error("Unable to load leaderboard files.")
    st.exception(error)
    st.stop()


# ============================================================
# 4. HELPER FUNCTIONS
# ============================================================

def find_column(row, possible_names, default=None):

    for name in possible_names:
        if name in row.index:
            value = row[name]

            if pd.notna(value):
                return value

    return default


def format_number(value, decimals=2):

    if value is None:
        return "N/A"

    try:
        if pd.isna(value):
            return "N/A"

        return f"{float(value):,.{decimals}f}"

    except (ValueError, TypeError):
        return str(value)


def get_player_name(row):
    return find_column(
        row,
        ["Player", "player", "player_name", "striker_name",
         "bowler_name", "Player_Name"],
        "Unknown"
    )


def get_rank(row):
    return find_column(row, ["Rank", "rank"], "N/A")


def get_final_score(row):
    return find_column(
        row,
        ["Final_Score", "final_score", "Batter_Score",
         "Bowler_Score", "composite_score", "Score"],
        None
    )


def get_batter_runs(row):
    return find_column(
        row,
        ["HP_Runs", "High_Pressure_Runs",
         "high_pressure_runs", "Pressure_Runs"],
        None
    )


def get_batter_balls(row):
    return find_column(
        row,
        ["HP_Balls", "High_Pressure_Balls",
         "balls_faced", "Balls_Faced"],
        None
    )


def get_batter_strike_rate(row):

    # First try available strike-rate columns
    value = find_column(
        row,
        ["HP_SR", "High_Pressure_SR", "Pressure_SR",
         "Strike_Rate", "StrikeRate", "SR",
         "high_pressure_strike_rate"],
        None
    )

    if value is not None:
        return value

    # Otherwise calculate from runs and balls
    runs = get_batter_runs(row)
    balls = get_batter_balls(row)

    try:
        if runs is not None and balls is not None:
            if float(balls) > 0:
                return (float(runs) / float(balls)) * 100
    except (ValueError, TypeError):
        pass

    return None


def get_batter_matches(row):
    return find_column(
        row,
        ["HP_Matches", "Matches", "Matches_Played",
         "matches_played", "High_Pressure_Matches"],
        None
    )


def get_bowler_wickets(row):
    return find_column(
        row,
        ["HP_Wickets", "High_Pressure_Wickets",
         "high_pressure_wickets", "Wickets"],
        None
    )


def get_bowler_balls(row):
    return find_column(
        row,
        ["HP_Legal_Balls", "Legal_Balls",
         "legal_balls", "High_Pressure_Legal_Balls"],
        None
    )


def get_bowler_rate(row):
    value = find_column(
        row,
        ["HP_Wickets_Per_24", "Wickets_Per_24_Balls",
         "wickets_per_24_balls", "Pressure_Wicket_Rate"],
        None
    )

    if value is not None:
        return value

    wickets = get_bowler_wickets(row)
    balls = get_bowler_balls(row)

    try:
        if wickets is not None and balls is not None:
            if float(balls) > 0:
                return float(wickets) * 24 / float(balls)
    except (ValueError, TypeError):
        pass

    return None


def get_bowler_matches(row):
    return find_column(
        row,
        ["HP_Matches", "Matches", "Matches_Played",
         "matches_played", "High_Pressure_Matches"],
        None
    )


# ============================================================
# 5. LEADERBOARD DISPLAY
# ============================================================

def render_batter_leaderboard(data):

    st.dataframe(
        pd.DataFrame({
            "Rank": data.apply(get_rank, axis=1),
            "Player": data.apply(get_player_name, axis=1),
            "Pressure Runs": data.apply(get_batter_runs, axis=1),
            "Balls Faced": data.apply(get_batter_balls, axis=1),
            "Pressure Strike Rate": data.apply(
                get_batter_strike_rate, axis=1
            ),
            "Matches": data.apply(get_batter_matches, axis=1),
            "Final Score": data.apply(get_final_score, axis=1)
        }),
        use_container_width=True,
        hide_index=True
    )


def render_bowler_leaderboard(data):

    st.dataframe(
        pd.DataFrame({
            "Rank": data.apply(get_rank, axis=1),
            "Player": data.apply(get_player_name, axis=1),
            "Pressure Wickets": data.apply(get_bowler_wickets, axis=1),
            "Legal Balls": data.apply(get_bowler_balls, axis=1),
            "Wickets / 24 Balls": data.apply(get_bowler_rate, axis=1),
            "Matches": data.apply(get_bowler_matches, axis=1),
            "Confidence": data.apply(
                lambda row: find_column(
                    row, ["Confidence", "Sample_Reliability"], "N/A"
                ),
                axis=1
            ),
            "Final Score": data.apply(get_final_score, axis=1)
        }),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# 6. SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("🏏 Navigation")

page = st.sidebar.radio(
    "Select a page",
    [
        "Overview",
        "Top 10 Batters",
        "Top 10 Bowlers",
        "Combined Leaderboard",
        "Methodology",
        "Project Information"
    ]
)

st.sidebar.divider()
st.sidebar.caption("SupeRR Selector Season 2")
st.sidebar.caption("Cricket Analytics Project")


# ============================================================
# 7. OVERVIEW
# ============================================================

if page == "Overview":

    st.header("📊 Project Overview")

    top_batter = batters.iloc[0]
    top_bowler = bowlers.iloc[0]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Top 10 Batters", len(batters))
    c2.metric("Top 10 Bowlers", len(bowlers))
    c3.metric("Top Batter", str(get_player_name(top_batter)))
    c4.metric("Top Bowler", str(get_player_name(top_bowler)))

    st.divider()

    st.subheader("🏆 Highest Ranked Performers")

    left, right = st.columns(2)

    with left:

        st.markdown("### 🏏 Top Batter")

        st.metric("Player", str(get_player_name(top_batter)))

        st.metric(
            "Final Score",
            format_number(get_final_score(top_batter))
        )

        st.metric(
            "High-Pressure Runs",
            format_number(get_batter_runs(top_batter), 0)
        )

        st.metric(
            "High-Pressure Strike Rate",
            format_number(get_batter_strike_rate(top_batter))
        )

    with right:

        st.markdown("### 🎯 Top Bowler")

        st.metric("Player", str(get_player_name(top_bowler)))

        st.metric(
            "Final Score",
            format_number(get_final_score(top_bowler))
        )

        st.metric(
            "High-Pressure Wickets",
            format_number(get_bowler_wickets(top_bowler), 0)
        )

        st.metric(
            "Wickets per 24 Legal Balls",
            format_number(get_bowler_rate(top_bowler))
        )

    st.divider()

    st.subheader("Top 10 Batter Rankings")
    render_batter_leaderboard(batters)

    st.subheader("Top 10 Bowler Rankings")
    render_bowler_leaderboard(bowlers)


# ============================================================
# 8. TOP 10 BATTERS
# ============================================================

elif page == "Top 10 Batters":

    st.header("🏏 Top 10 Batters Under Pressure")

    render_batter_leaderboard(batters)

    st.divider()

    st.subheader("🔍 Individual Batter Analysis")

    player_names = batters.apply(
        lambda row: str(get_player_name(row)), axis=1
    ).tolist()

    selected_player = st.selectbox(
        "Select a Batter",
        player_names
    )

    selected = batters[
        batters.apply(
            lambda row: str(get_player_name(row)) == selected_player,
            axis=1
        )
    ].iloc[0]

    c1, c2, c3 = st.columns(3)

    c1.metric("Rank", str(get_rank(selected)))
    c2.metric("Final Score", format_number(get_final_score(selected)))
    c3.metric(
        "Pressure Runs",
        format_number(get_batter_runs(selected), 0)
    )

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "Balls Faced",
        format_number(get_batter_balls(selected), 0)
    )

    c5.metric(
        "Pressure Strike Rate",
        format_number(get_batter_strike_rate(selected))
    )

    c6.metric(
        "Matches",
        format_number(get_batter_matches(selected), 0)
    )

    normal_sr = find_column(
        selected,
        ["Normal_SR", "Normal_Strike_Rate"],
        None
    )

    sr_change = find_column(
        selected,
        ["SR_Change", "Strike_Rate_Change"],
        None
    )

    if normal_sr is not None:
        st.metric("Normal Strike Rate", format_number(normal_sr))

    if sr_change is not None:
        st.metric("Strike Rate Change", format_number(sr_change))


# ============================================================
# 9. TOP 10 BOWLERS
# ============================================================

elif page == "Top 10 Bowlers":

    st.header("🎯 Top 10 Bowlers Under Pressure")

    render_bowler_leaderboard(bowlers)

    st.divider()

    st.subheader("🔍 Individual Bowler Analysis")

    player_names = bowlers.apply(
        lambda row: str(get_player_name(row)), axis=1
    ).tolist()

    selected_player = st.selectbox(
        "Select a Bowler",
        player_names
    )

    selected = bowlers[
        bowlers.apply(
            lambda row: str(get_player_name(row)) == selected_player,
            axis=1
        )
    ].iloc[0]

    c1, c2, c3 = st.columns(3)

    c1.metric("Rank", str(get_rank(selected)))
    c2.metric("Final Score", format_number(get_final_score(selected)))
    c3.metric(
        "Pressure Wickets",
        format_number(get_bowler_wickets(selected), 0)
    )

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "Legal Balls",
        format_number(get_bowler_balls(selected), 0)
    )

    c5.metric(
        "Wickets per 24 Balls",
        format_number(get_bowler_rate(selected))
    )

    c6.metric(
        "Matches",
        format_number(get_bowler_matches(selected), 0)
    )

    confidence = find_column(
        selected,
        ["Confidence", "Sample_Reliability"],
        "Not available"
    )

    st.divider()
    st.metric("Sample Confidence", str(confidence))

    normal_rate = find_column(
        selected,
        ["Normal_Wickets_Per_24"],
        None
    )

    rate_change = find_column(
        selected,
        ["Wicket_Rate_Change"],
        None
    )

    if normal_rate is not None:
        st.metric(
            "Normal Wickets per 24 Balls",
            format_number(normal_rate)
        )

    if rate_change is not None:
        st.metric(
            "Wicket Rate Change",
            format_number(rate_change)
        )

    if str(confidence).lower() == "limited":
        st.warning(
            "Limited sample: interpret this player's pressure statistics "
            "with caution."
        )

    elif str(confidence).lower() == "insufficient":
        st.warning(
            "Insufficient sample: this player has very limited "
            "high-pressure bowling data."
        )


# ============================================================
# 10. COMBINED LEADERBOARD
# ============================================================

elif page == "Combined Leaderboard":

    st.header("🏆 Combined Leaderboard")

    st.dataframe(
        combined,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("📥 Download Results")

    c1, c2, c3 = st.columns(3)

    c1.download_button(
        "Download Batter CSV",
        data=batters.to_csv(index=False).encode("utf-8"),
        file_name="top_10_batters.csv",
        mime="text/csv"
    )

    c2.download_button(
        "Download Bowler CSV",
        data=bowlers.to_csv(index=False).encode("utf-8"),
        file_name="top_10_bowlers.csv",
        mime="text/csv"
    )

    c3.download_button(
        "Download Combined CSV",
        data=combined.to_csv(index=False).encode("utf-8"),
        file_name="combined_top_10_leaderboards.csv",
        mime="text/csv"
    )


# ============================================================
# 11. METHODOLOGY
# ============================================================

elif page == "Methodology":

    st.header("📚 Methodology")

    st.subheader("1. Dataset")

    st.write(
        """
        - IPL and T20I ball-by-ball data from 2022 onward.
        - Player candidates restricted to the competition-provided list.
        - Match and delivery data processed for pressure analysis.
        """
    )

    st.subheader("2. Pressure Score")

    st.latex(
        r"P = 100(0.60 \times \text{Innings Progress}"
        r" + 0.40 \times \text{Wicket Pressure})"
    )

    st.write(
        """
        A delivery is classified as high pressure when its pressure
        score is at least 50.
        """
    )

    st.subheader("3. Batter Ranking")

    st.write(
        """
        Batter scores use the following components:

        - High-pressure runs: 40%
        - High-pressure strike rate: 30%
        - Boundary performance: 15%
        - Sample sufficiency: 15%
        """
    )

    st.subheader("4. Bowler Ranking")

    st.write(
        """
        Bowler scores use:

        - High-pressure wickets: 45%
        - Wickets per 24 legal balls: 30%
        - Sample sufficiency: 25%
        """
    )

    st.subheader("5. Bowling Sample Confidence")

    st.write(
        """
        - Strong: at least 120 high-pressure legal balls.
        - Limited: 24 to 119 high-pressure legal balls.
        - Insufficient: fewer than 24 high-pressure legal balls.
        """
    )

    st.info(
        "The 120-ball innings assumption is a modelling choice. "
        "Results should be interpreted within the selected match formats."
    )


# ============================================================
# 12. PROJECT INFORMATION
# ============================================================

elif page == "Project Information":

    st.header("ℹ️ Project Information")

    st.subheader("SupeRR Selector – Season 2")

    st.write(
        """
        This project identifies the Top 10 batters and Top 10 bowlers
        under pressure using cricket ball-by-ball data.

        It applies data cleaning, feature engineering, pressure
        classification, statistical scoring, and validation.
        """
    )

    st.subheader("Project Deliverables")

    st.write(
        """
        - Top 10 batter leaderboard.
        - Top 10 bowler leaderboard.
        - Combined leaderboard.
        - Pressure performance metrics.
        - Bowling sample confidence indicators.
        - Interactive Streamlit dashboard.
        """
    )

    st.warning(
        "These are model-based rankings within the supplied candidate "
        "list and selected dataset, not universal rankings of all players."
    )


# ============================================================
# 13. FOOTER
# ============================================================

st.divider()

st.caption(
    "SupeRR Selector Season 2 | Cricket Analytics | "
    "Pressure Performance Dashboard"
)
