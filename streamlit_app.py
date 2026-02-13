
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(page_title="Netflix Analysis", page_icon="🎬", layout="wide")

# =========================================================
# LIGHT MODERN UI (CSS)
# =========================================================
st.markdown(
    """
<style>
:root{
  --bg: #f6f7fb;
  --panel: #ffffff;
  --panel2: #fbfbfd;
  --border: rgba(15, 23, 42, 0.10);
  --text: #0f172a;
  --muted: rgba(15, 23, 42, 0.65);
  --accent: #E50914;   /* Netflix red */
  --accent2: #ff3b30;
  --blue: #2563eb;
  --teal: #14b8a6;
  --shadow: 0 10px 28px rgba(2,6,23,0.08);
  --shadow2: 0 16px 40px rgba(2,6,23,0.10);
  --radius: 16px;
}

/* App background */
.stApp{
  background: radial-gradient(900px 550px at 20% 0%, rgba(229,9,20,0.12), transparent 55%),
              radial-gradient(900px 550px at 90% 10%, rgba(37,99,235,0.10), transparent 55%),
              var(--bg);
  color: var(--text);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji";
}

/* Container spacing */
.block-container { padding-top: 1.4rem; padding-bottom: 2rem; }

/* Headings */
h1, h2, h3, h4 { color: var(--text) !important; }
a { color: var(--blue) !important; }

/* Sidebar */
section[data-testid="stSidebar"]{
  background: rgba(255,255,255,0.80);
  border-right: 1px solid var(--border);
  backdrop-filter: blur(10px);
}
section[data-testid="stSidebar"] * { color: var(--text) !important; }

/* Inputs */
div[data-baseweb="select"] > div{
  background: var(--panel) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  box-shadow: 0 6px 16px rgba(2,6,23,0.06);
}

/* Metric cards */
div[data-testid="stMetric"]{
  background: var(--panel);
  border: 1px solid var(--border);
  padding: 16px 16px;
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}
div[data-testid="stMetric"] label,
div[data-testid="stMetric"] div { color: var(--text) !important; }
div[data-testid="stMetricDelta"] { color: var(--muted) !important; }

/* Alerts */
div[data-testid="stAlert"]{
  background: var(--panel);
  border: 1px solid var(--border);
  border-left: 5px solid var(--accent);
  border-radius: var(--radius);
  color: var(--text) !important;
  box-shadow: var(--shadow);
}

/* Expanders */
details{
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 10px 12px;
  box-shadow: var(--shadow);
}

/* Dataframe */
div[data-testid="stDataFrame"]{
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow);
}

/* Small card helper */
.card{
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 16px 16px;
  box-shadow: var(--shadow);
}

/* Footer */
.footer{
  text-align:center;
  color: var(--muted);
  padding: 18px 0 8px 0;
  font-size: 13px;
}
</style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# PLOTLY LIGHT THEME HELPERS
# =========================================================
NETFLIX_RED = "#E50914"
BLUE = "#2563eb"
TEAL = "#14b8a6"
TEXT = "#0f172a"
GRID = "rgba(15, 23, 42, 0.10)"


def apply_light_plotly(fig):
    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=TEXT),
        title_font=dict(size=18, color=TEXT),
        margin=dict(l=20, r=20, t=60, b=20),
        legend=dict(
            bgcolor="rgba(255,255,255,0.85)",
            bordercolor="rgba(15,23,42,0.10)",
            borderwidth=1,
        ),
    )
    fig.update_xaxes(showgrid=True, gridcolor=GRID, zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor=GRID, zeroline=False)
    return fig


# =========================================================
# LOAD AND CLEAN DATA
# =========================================================
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_data/netflix_titles.csv")
    return df


@st.cache_data
def clean_data(df):
    df = df.copy()

    df["date_added"] = df["date_added"].astype(str).str.strip()
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["year_added"] = df["date_added"].dt.year

    df["primary_country"] = (
        df["country"].fillna("Unknown").astype(str).str.split(",").str[0].str.strip()
    )

    df_clean = df.dropna(subset=["year_added"]).copy()
    df_clean["year_added"] = df_clean["year_added"].astype(int)

    return df_clean


df = load_data()
df = clean_data(df)

# =========================================================
# HEADER (LIGHT MODERN HERO)
# =========================================================
try:
    logo = Image.open("images.png")
except Exception:
    logo = None

col1, col2 = st.columns([1, 7], vertical_alignment="center")
with col1:
    if logo:
        st.image(logo, width=90)
    else:
        st.markdown("<div class='card' style='text-align:center;'>🎬</div>", unsafe_allow_html=True)

with col2:
    st.markdown(
        f"""
    <div style="
      padding: 18px 18px;
      border-radius: 18px;
      border: 1px solid rgba(15,23,42,0.10);
      background: linear-gradient(135deg, rgba(229,9,20,0.12), rgba(37,99,235,0.10), rgba(255,255,255,0.85));
      box-shadow: 0 16px 40px rgba(2,6,23,0.10);
    ">
      <h1 style="margin:0; font-size: 38px; color:#0f172a;">
        Netflix <span style="color:{NETFLIX_RED};">Analysis</span> Dashboard
      </h1>
      <p style="margin:6px 0 0 0; color: rgba(15,23,42,0.65); font-size: 15px;">
        🎬 Explore Netflix movies and TV shows interactively
      </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("")

# =========================================================
# SIDEBAR FILTERS
# =========================================================
st.sidebar.header("🔍 Filters")
st.sidebar.markdown("Use these filters to customize your view")

type_filter = st.sidebar.multiselect(
    "Content Type",
    options=sorted(df["type"].dropna().unique().tolist()),
    default=sorted(df["type"].dropna().unique().tolist()),
    help="Select one or more content types",
)

min_year = int(df["year_added"].min())
max_year = int(df["year_added"].max())

year_range = st.sidebar.slider(
    "Year Added to Netflix",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
    help="Filter content by the year it was added to Netflix",
)

top_countries = df["primary_country"].value_counts().head(20).index.tolist()
country_filter = st.sidebar.multiselect(
    "Country of Origin",
    options=["All"] + top_countries,
    default=["All"],
    help="Filter by country of origin (top 20 countries)",
)

ratings_list = sorted(df["rating"].dropna().unique().tolist())
rating_filter = st.sidebar.multiselect(
    "Content Rating",
    options=["All"] + ratings_list,
    default=["All"],
    help="Filter by content rating (e.g., PG-13, TV-MA)",
)

st.sidebar.markdown("---")
st.sidebar.info("💡 Tip: Select multiple options in each filter to compare segments.")

# =========================================================
# APPLY FILTERS
# =========================================================
filtered_df = df.copy()

if type_filter:
    filtered_df = filtered_df[filtered_df["type"].isin(type_filter)]

filtered_df = filtered_df[
    (filtered_df["year_added"] >= year_range[0]) & (filtered_df["year_added"] <= year_range[1])
]

if country_filter and "All" not in country_filter:
    filtered_df = filtered_df[filtered_df["primary_country"].isin(country_filter)]

if rating_filter and "All" not in rating_filter:
    filtered_df = filtered_df[filtered_df["rating"].isin(rating_filter)]

# =========================================================
# KEY METRICS
# =========================================================
st.subheader("📊 Key Metrics")

m1, m2, m3, m4 = st.columns(4)

total_titles = len(filtered_df)
movies = len(filtered_df[filtered_df["type"] == "Movie"])
shows = len(filtered_df[filtered_df["type"] == "TV Show"])

with m1:
    delta = (
        f"{(total_titles / len(df) * 100):.1f}% of catalog"
        if len(df) > 0 and total_titles != len(df)
        else None
    )
    st.metric("Total Titles", f"{total_titles:,}", delta=delta)

with m2:
    st.metric("Movies", f"{movies:,}", delta=f"{(movies / total_titles * 100):.1f}%" if total_titles else "0%")

with m3:
    st.metric("TV Shows", f"{shows:,}", delta=f"{(shows / total_titles * 100):.1f}%" if total_titles else "0%")

with m4:
    st.metric("Countries", f"{filtered_df['primary_country'].nunique() if total_titles else 0:,}")

st.markdown("---")

# =========================================================
# CONTENT DISTRIBUTION
# =========================================================
st.subheader("📺 Content Type Distribution")

left, right = st.columns([2, 1])

with left:
    if total_titles:
        type_counts = filtered_df["type"].value_counts()

        fig = px.pie(
            values=type_counts.values,
            names=type_counts.index,
            title="Movies vs TV Shows",
            hole=0.45,
            color_discrete_sequence=[NETFLIX_RED, TEAL],
        )
        fig.update_traces(textposition="inside", textinfo="percent+label", textfont_size=14)
        fig.update_layout(height=420)
        st.plotly_chart(apply_light_plotly(fig), use_container_width=True)
    else:
        st.warning("No data available for the selected filters")

with right:
    st.markdown("### 📈 Quick Stats")
    if total_titles:
        movie_pct = (movies / total_titles * 100) if total_titles else 0
        show_pct = (shows / total_titles * 100) if total_titles else 0

        st.markdown(
            f"""
        <div class="card">
            <p style="font-size: 18px; margin: 8px 0;">
                🎬 Movies: <b style="color:{NETFLIX_RED};">{movie_pct:.1f}%</b>
            </p>
            <p style="font-size: 18px; margin: 8px 0;">
                📺 TV Shows: <b style="color:{TEAL};">{show_pct:.1f}%</b>
            </p>
            <p style="font-size: 13px; margin-top: 14px; color: rgba(15,23,42,0.65);">
                Total: {total_titles:,} titles
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )
    else:
        st.info("Adjust filters to see statistics")

st.markdown("---")

# =========================================================
# CONTENT GROWTH OVER TIME
# =========================================================
st.subheader("📈 Content Added Over Time")

if total_titles:
    yearly = (
        filtered_df.groupby(["year_added", "type"])
        .size()
        .reset_index(name="count")
        .sort_values("year_added")
    )

    fig = px.line(
        yearly,
        x="year_added",
        y="count",
        color="type",
        title="Netflix Content Growth Timeline",
        labels={"year_added": "Year Added", "count": "Number of Titles", "type": "Content Type"},
        markers=True,
        color_discrete_map={"Movie": NETFLIX_RED, "TV Show": TEAL},
    )
    fig.update_traces(line=dict(width=3), marker=dict(size=8))
    fig.update_layout(hovermode="x unified", height=460)
    st.plotly_chart(apply_light_plotly(fig), use_container_width=True)

    peak = yearly.groupby("year_added")["count"].sum()
    if len(peak) > 0:
        st.info(f"📌 Peak year: **{int(peak.idxmax())}** with **{int(peak.max())}** titles added")
else:
    st.warning("No data available for the selected filters")

st.markdown("---")

# =========================================================
# TOP COUNTRIES
# =========================================================
st.subheader("🌍 Top Content Producing Countries")

if total_titles:
    country_counts = filtered_df["primary_country"].value_counts().head(10)

    fig_country = px.bar(
        x=country_counts.values,
        y=country_counts.index,
        orientation="h",
        title="Top 10 Countries by Number of Titles",
        labels={"x": "Number of Titles", "y": "Country"},
        text=country_counts.values,
        color=country_counts.values,
        color_continuous_scale="Reds",
    )
    fig_country.update_traces(textposition="outside")
    fig_country.update_layout(height=480, coloraxis_showscale=False)
    st.plotly_chart(apply_light_plotly(fig_country), use_container_width=True)
else:
    st.warning("No data available for the selected filters")

st.markdown("---")

# =========================================================
# GENRES + RATINGS
# =========================================================
st.subheader("🎭 Popular Genres")
g1, g2 = st.columns(2)

with g1:
    if total_titles:
        genres = filtered_df["listed_in"].dropna()
        genre_list = []
        for genre_str in genres:
            genre_list.extend([g.strip() for g in str(genre_str).split(",")])

        top_genres = pd.Series(genre_list).value_counts().head(10)

        fig_genre = px.bar(
            x=top_genres.values,
            y=top_genres.index,
            orientation="h",
            title="Top 10 Genres",
            labels={"x": "Number of Titles", "y": "Genre"},
            text=top_genres.values,
            color=top_genres.values,
            color_continuous_scale="Reds",
        )
        fig_genre.update_traces(textposition="outside")
        fig_genre.update_layout(height=480, coloraxis_showscale=False)
        st.plotly_chart(apply_light_plotly(fig_genre), use_container_width=True)
    else:
        st.warning("No data available")

with g2:
    st.markdown("### ⭐ Content Ratings")
    if total_titles:
        ratings = filtered_df["rating"].value_counts().head(8)

        fig_rating = px.bar(
            x=ratings.index,
            y=ratings.values,
            title="Most Common Ratings",
            labels={"x": "Rating", "y": "Number of Titles"},
            text=ratings.values,
            color=ratings.values,
            color_continuous_scale="Reds",
        )
        fig_rating.update_traces(textposition="outside")
        fig_rating.update_layout(height=480, coloraxis_showscale=False)
        st.plotly_chart(apply_light_plotly(fig_rating), use_container_width=True)
    else:
        st.warning("No data available")

st.markdown("---")

# =========================================================
# KEY INSIGHTS
# =========================================================
st.subheader("🔍 Key Insights")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        f"""
    <div class="card" style="border-left: 5px solid {NETFLIX_RED};">
      <h4 style="margin: 0 0 6px 0;">📺 Content Mix</h4>
      <p style="margin:0; color: rgba(15,23,42,0.65);">
        Netflix includes both movies and TV shows, with the balance shifting over the years.
      </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        f"""
    <div class="card" style="border-left: 5px solid {TEAL};">
      <h4 style="margin: 0 0 6px 0;">🌍 Global Reach</h4>
      <p style="margin:0; color: rgba(15,23,42,0.65);">
        The catalog spans many countries, with international content expanding significantly over time.
      </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        f"""
    <div class="card" style="border-left: 5px solid {BLUE};">
      <h4 style="margin: 0 0 6px 0;">📊 Content Strategy</h4>
      <p style="margin:0; color: rgba(15,23,42,0.65);">
        Growth spikes often reflect periods of aggressive expansion and original content investment.
      </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# =========================================================
# DATA PREVIEW
# =========================================================
with st.expander("📋 View Filtered Dataset"):
    cols = ["title", "type", "primary_country", "release_year", "rating", "listed_in", "year_added"]
    st.dataframe(filtered_df[cols].head(100), use_container_width=True)
    st.caption(f"Showing first 100 of {len(filtered_df):,} filtered titles")

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    """
<div class="footer">
  <p>Built with ❤️ using Python • Streamlit • Plotly • Pandas</p>
  <p style="font-size: 12px;">Data source: Netflix Titles Dataset</p>
</div>
""",
    unsafe_allow_html=True,
)
