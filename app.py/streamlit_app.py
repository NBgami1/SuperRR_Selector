
import streamlit as st
import pandas as pd
from pathlib import Path


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SupeRR Selector Season 2",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 SupeRR Selector — Season 2")

st.subheader(
    "Identifying the Top 10 Batters and Bowlers Under Pressure"
)

st.caption(
    "Cricket Analytics Project | IPL and T20I | 2022 onwards"
)


# ============================================================
# 2. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

TABLE_DIR = BASE_DIR / "notebooks" / "outputs" / "tables"

REPORT_PATHS = [
    BASE_DIR / "notebooks" / "outputs" / "reports"
    / "methodology_and_limitations.md",

    BASE_DIR / "outputs" / "reports"
    / "methodology_and_limitations.md"
]


# ============================================================
# 3. LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    batters = pd.read_csv(
        TABLE_DIR / "top_10_batters.csv"
    )

    bowlers = pd.read_csv(
        TABLE_DIR / "top_10_bowlers.csv"
    )

    combined = pd.read_csv(
        TABLE_DIR / "combined_top_10_leaderboards.csv"
    )

    return batters, bowlers, combined


try:

    batters, bowlers, combined = load_data()

except FileNotFoundError as error:

    st.error("Required CSV file could not be found.")

    st.code(str(error))

    st.info(
        "Check that the three CSV files are saved inside "
        "notebooks/outputs/tables."
    )

    st.stop()

except Exception as error:

    st.error("Unable to load the project data.")

    st.exception(error)

    st.stop()


# ============================================================
# 4. HELPER FUNCTIONS
# ============================================================

def get_value(row, possible_columns, default=0):

    for column in possible_columns:

        if column in row.index:

            value = row[column]

            if pd.notna(value):
                return value

    return default


def number(value, decimals=2):

    try:
        return f"{float(value):,.{decimals}f}"

    except (ValueError, TypeError):
        return str(value)


def display_score(score):

    try:

        score = float(score)

        score = max(0, min(score, 100))

        st.progress(score / 100)

    except (ValueError, TypeError):
        st.write("Score unavailable")


def render_leaderboard(data, name_columns, score_columns):

    if data.empty:

        st.warning("No leaderboard records available.")

        return

    for position, (_, row) in enumerate(data.iterrows(), start=1):

        rank = get_value(row, ["rank"], position)

        name = get_value(row, name_columns, "Unknown Player")

        score = get_value(row, score_columns, 0)

        st.markdown(
            f"**{int(rank)}. {name}** — "
            f"**{number(score)} points**"
        )

        display_score(score)


def render_metric(label, value):

    st.metric(label, value)


# ============================================================
# 5. TOP-LEVEL PROJECT METRICS
# ============================================================

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    render_metric("Ranked Players", "20")

with col2:
    render_metric("Top Batters", str(len(batters)))

with col3:
    render_metric("Top Bowlers", str(len(bowlers)))

with col4:
    render_metric("Selected Matches", "853")

st.divider()


# ============================================================
# 6. NAVIGATION TABS
# ============================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "🏆 Overview",
    "🏏 Batters",
    "🎯 Bowlers",
    "📘 Methodology"
])


# ============================================================
# TAB 1: OVERVIEW
# ============================================================

with tab1:

    st.header("🏆 Project Overview")

    st.write(
        "SupeRR Selector Season 2 identifies outstanding "
        "batting and bowling performances under pressure "
        "using IPL and T20I ball-by-ball data from 2022 onwards."
    )

    st.divider()

    st.subheader("⭐ Top Performers")

    left, right = st.columns(2)

    # ---------------- TOP BATTER ----------------

    with left:

        st.markdown("### 🏏 Top Batter")

        if not batters.empty:

            top_batter = batters.iloc[0]

            batter_name = get_value(
                top_batter,
                ["striker_name", "player_name"],
                "Unknown"
            )

            batter_score = get_value(
                top_batter,
                ["batter_score", "composite_score"],
                0
            )

            batter_runs = get_value(
                top_batter,
                ["high_pressure_runs"],
                0
            )

            batter_sr = get_value(
                top_batter,
                ["strike_rate"],
                0
            )

            st.metric(
                "Rank 1 — " + str(batter_name),
                number(batter_score) + " points"
            )

            st.write(
                "High-pressure runs:",
                number(batter_runs, 0)
            )

            st.write(
                "Strike rate:",
                number(batter_sr)
            )

            display_score(batter_score)

    # ---------------- TOP BOWLER ----------------

    with right:

        st.markdown("### 🎯 Top Bowler")

        if not bowlers.empty:

            top_bowler = bowlers.iloc[0]

            bowler_name = get_value(
                top_bowler,
                ["bowler_name", "player_name"],
                "Unknown"
            )

            bowler_score = get_value(
                top_bowler,
                ["bowler_score", "composite_score"],
                0
            )

            bowler_wickets = get_value(
                top_bowler,
                ["high_pressure_wickets"],
                0
            )

            bowler_rate = get_value(
                top_bowler,
                ["wickets_per_24_balls"],
                0
            )

            st.metric(
                "Rank 1 — " + str(bowler_name),
                number(bowler_score) + " points"
            )

            st.write(
                "High-pressure wickets:",
                number(bowler_wickets, 0)
            )

            st.write(
                "Wickets per 24 legal balls:",
                number(bowler_rate)
            )

            display_score(bowler_score)

    st.divider()

    # ---------------- BATTER RANKINGS ----------------

    st.subheader("🏏 Top 10 Batter Scores")

    render_leaderboard(
        batters,
        ["striker_name", "player_name"],
        ["batter_score", "composite_score"]
    )

    st.divider()

    # ---------------- BOWLER RANKINGS ----------------

    st.subheader("🎯 Top 10 Bowler Scores")

    render_leaderboard(
        bowlers,
        ["bowler_name", "player_name"],
        ["bowler_score", "composite_score"]
    )

    st.divider()

    st.header("📥 Download Centre")

    st.write(
        "Download the final rankings and analytical results "
        "for further research and evaluation."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.download_button(
            label="🏏 Download Batter Rankings",
            data=batters.to_csv(index=False).encode("utf-8"),
            file_name="top_10_batters.csv",
            mime="text/csv",
            key="download_batters"
        )

    with col2:
        st.download_button(
            label="🎯 Download Bowler Rankings",
            data=bowlers.to_csv(index=False).encode("utf-8"),
            file_name="top_10_bowlers.csv",
            mime="text/csv",
            key="download_bowlers"
        )

    with col3:
        st.download_button(
            label="🏆 Download Combined Rankings",
            data=combined.to_csv(index=False).encode("utf-8"),
            file_name="combined_top_10_leaderboards.csv",
            mime="text/csv",
            key="download_combined"
        )


# ============================================================
# TAB 2: BATTERS
# ============================================================

with tab2:

    st.header("🏏 Top 10 Batters Under Pressure")

    st.write(
        "Players ranked using their high-pressure batting "
        "performance and the project's composite scoring system."
    )

    st.divider()

    if not batters.empty:

        st.subheader("Batter Leaderboard")

        render_leaderboard(
            batters,
            ["striker_name", "player_name"],
            ["batter_score", "composite_score"]
        )

        st.divider()

        st.subheader("Explore Individual Batter")

        batter_names = [
            str(get_value(row, ["striker_name", "player_name"], "Unknown"))
            for _, row in batters.iterrows()
        ]

        selected_batter = st.selectbox(
            "Select a batter",
            batter_names,
            key="selected_batter"
        )

        selected_row = batters.iloc[
            batter_names.index(selected_batter)
        ]

        st.markdown(f"### {selected_batter}")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Composite Score",
                number(get_value(
                    selected_row,
                    ["batter_score", "composite_score"]
                ))
            )

        with c2:

            st.metric(
                "High-Pressure Runs",
                number(get_value(
                    selected_row,
                    ["high_pressure_runs"]
                ), 0)
            )

        with c3:

            st.metric(
                "Strike Rate",
                number(get_value(
                    selected_row,
                    ["strike_rate"]
                ))
            )

        c4, c5, c6 = st.columns(3)

        with c4:

            st.metric(
                "Balls Faced",
                number(get_value(
                    selected_row,
                    ["balls_faced", "high_pressure_balls_faced"]
                ), 0)
            )

        with c5:

            st.metric(
                "Fours",
                number(get_value(
                    selected_row,
                    ["fours"]
                ), 0)
            )

        with c6:

            st.metric(
                "Sixes",
                number(get_value(
                    selected_row,
                    ["sixes"]
                ), 0)
            )

        st.metric(
            "Matches Played",
            number(get_value(
                selected_row,
                ["matches_played"]
            ), 0)
        )

        st.metric(
            "Boundary Percentage",
            number(get_value(
                selected_row,
                ["boundary_percentage"]
            ))
            + "%"
        )

    else:

        st.warning("Batter data is unavailable.")


# ============================================================
# TAB 3: BOWLERS
# ============================================================

with tab3:

    st.header("🎯 Top 10 Bowlers Under Pressure")

    st.write(
        "Players ranked using high-pressure wickets, "
        "wicket-taking rate and sample sufficiency."
    )

    st.divider()

    if not bowlers.empty:

        st.subheader("Bowler Leaderboard")

        render_leaderboard(
            bowlers,
            ["bowler_name", "player_name"],
            ["bowler_score", "composite_score"]
        )

        st.divider()

        st.subheader("Explore Individual Bowler")

        bowler_names = [
            str(get_value(row, ["bowler_name", "player_name"], "Unknown"))
            for _, row in bowlers.iterrows()
        ]

        selected_bowler = st.selectbox(
            "Select a bowler",
            bowler_names,
            key="selected_bowler"
        )

        selected_row = bowlers.iloc[
            bowler_names.index(selected_bowler)
        ]

        st.markdown(f"### {selected_bowler}")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Composite Score",
                number(get_value(
                    selected_row,
                    ["bowler_score", "composite_score"]
                ))
            )

        with c2:

            st.metric(
                "High-Pressure Wickets",
                number(get_value(
                    selected_row,
                    ["high_pressure_wickets"]
                ), 0)
            )

        with c3:

            st.metric(
                "Wickets per 24 Legal Balls",
                number(get_value(
                    selected_row,
                    ["wickets_per_24_balls"]
                ))
            )

        c4, c5 = st.columns(2)

        with c4:

            st.metric(
                "Legal Balls",
                number(get_value(
                    selected_row,
                    ["legal_balls"]
                ), 0)
            )

        with c5:

            st.metric(
                "Matches Played",
                number(get_value(
                    selected_row,
                    ["matches_played"]
                ), 0)
            )

    else:

        st.warning("Bowler data is unavailable.")


# ============================================================
# TAB 4: METHODOLOGY
# ============================================================

with tab4:

    st.header("📘 Ranking Methodology")

    st.write(
        "The project uses a pressure-based approach to "
        "evaluate batting and bowling performance."
    )

    st.divider()

    st.subheader("1. Dataset Coverage")

    st.write("Competition formats: IPL and T20I")

    st.write("Data period: 2022 onwards")

    st.write("Selected matches: 853")

    st.write("Selected ball-by-ball records: 194,014")

    st.divider()

    st.subheader("2. Pressure Calculation")

    st.latex(
        r"P = 100(0.60 \times \text{Innings Progress}"
        r" + 0.40 \times \text{Wicket Pressure})"
    )

    st.write(
        "**Innings Progress:** Known legal balls completed "
        "before the delivery divided by 120, capped at 1."
    )

    st.write(
        "**Wicket Pressure:** Wickets fallen before the "
        "delivery divided by 10, capped at 1."
    )

    st.caption(
        "The 120-ball reference is a provisional assumption "
        "and is not validated for every shortened match."
    )

    st.divider()

    st.subheader("3. Batter Ranking Weights")

    st.write("High-pressure runs: 40%")

    st.write("Strike rate: 30%")

    st.write("Boundary percentage: 15%")

    st.write("Sample sufficiency: 15%")

    st.divider()

    st.subheader("4. Bowler Ranking Weights")

    st.write("High-pressure wickets: 45%")

    st.write("Wickets per 24 legal balls: 30%")

    st.write("Sample sufficiency: 25%")

    st.divider()

    st.subheader("5. Important Limitations")

    st.warning(
        """
        - The pressure formula is a provisional model.
        - The 120-ball reference may not represent shortened matches.
        - Some deliveries have unknown legal-ball classifications.
        - Actual extras runs are unavailable or unreliable.
        - Bowling economy rate is not calculated because total
          runs conceded are unavailable.
        - Batter and bowler composite scores use different
          scoring models and should not be compared directly.
        - Ranking weights are provisional and may be improved
          through further validation.
        """
    )

    st.divider()

    st.subheader("6. Full Methodology Report")

    report_file = next(
        (path for path in REPORT_PATHS if path.exists()),
        None
    )

    if report_file:

        try:

            report_text = report_file.read_text(
                encoding="utf-8"
            )

            with st.expander(
                "Read complete methodology and limitations report"
            ):

                st.markdown(report_text)

        except Exception as error:

            st.error(
                "Could not read the methodology report."
            )

            st.write(str(error))

    else:

        st.info(
            "The full methodology report was not found. "
            "The summary above is displayed instead."
        )


# ============================================================
# 7. FOOTER
# ============================================================

st.divider()

st.caption(
    "SupeRR Selector Season 2 | Cricket Analytics Project"
)

st.caption(
    "Data-driven cricket performance analysis | IPL and T20I"
)
