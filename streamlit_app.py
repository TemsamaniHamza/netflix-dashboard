from __future__ import annotations

import html
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


APP_DIR = Path(__file__).parent
DATA_PATH = APP_DIR / "netflix_data" / "netflix_titles.csv"
RED, INK, MUTED, GRID = "#E50914", "#F4F4F5", "#A1A1AA", "rgba(255,255,255,.08)"

st.set_page_config(page_title="Netflix Catalog Intelligence", page_icon="N", layout="wide")

st.markdown(
    """
    <style>
    :root { --red:#E50914; --ink:#F4F4F5; --muted:#A1A1AA; --surface:#0A0A0B; --panel:#151517; --line:rgba(255,255,255,.09); }
    .stApp { background:var(--surface); color:var(--ink); }
    .block-container { max-width:1380px; padding:2.5rem 3rem 4rem; }
    header[data-testid="stHeader"] { background:transparent; }
    #MainMenu, footer { visibility:hidden; }
    [data-testid="stToolbar"] { display:none; }
    h1,h2,h3,p,label { color:var(--ink); } h2 { letter-spacing:-.035em; }
    div[data-testid="stCaptionContainer"] { color:var(--muted); }
    section[data-testid="stSidebar"] { background:#101011; border-right:1px solid var(--line); }
    section[data-testid="stSidebar"] .block-container { padding:2rem 1.35rem; }
    section[data-testid="stSidebar"] hr { border-color:var(--line); }
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    section[data-testid="stSidebar"] label { color:#D4D4D8; }
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div,
    div[data-testid="stTextInputRootElement"] { background:#19191C !important; border-color:var(--line) !important; border-radius:8px !important; }
    div[data-baseweb="tag"] { background:#303034 !important; }
    div[data-testid="stPlotlyChart"] { background:var(--panel); border:1px solid var(--line); border-radius:14px; padding:.35rem; overflow:hidden; }
    div[data-testid="stDataFrame"] { border:1px solid var(--line); border-radius:12px; overflow:hidden; }
    div[data-testid="stTabs"] button { color:var(--muted); }
    div[data-testid="stTabs"] button[aria-selected="true"] { color:white; }
    div[data-testid="stTabs"] [data-baseweb="tab-highlight"] { background:var(--red); }
    div[data-testid="stExpander"] { border:1px solid var(--line); background:var(--panel); border-radius:12px; }
    div.stButton > button, div.stDownloadButton > button { border-radius:8px; border:1px solid var(--line); background:#202023; color:white; font-weight:650; }
    div.stButton > button:hover, div.stDownloadButton > button:hover { border-color:var(--red); color:white; }
    .brand { display:flex; align-items:center; gap:7px; margin-bottom:2rem; }
    .brand-mark { color:var(--red); font-weight:950; font-size:30px; line-height:1; font-family:Arial Black,sans-serif; transform:scaleX(.78); transform-origin:left; }
    .brand-name { font-size:11px; letter-spacing:.15em; color:#D4D4D8; font-weight:750; }
    .eyebrow { color:var(--red); font-size:.72rem; font-weight:800; letter-spacing:.16em; text-transform:uppercase; margin-bottom:.65rem; }
    .hero { padding:1.7rem 0 2.1rem; border-bottom:1px solid var(--line); margin-bottom:1.4rem; }
    .hero h1 { color:white; max-width:880px; font-size:clamp(2.6rem,5vw,5rem); line-height:.96; letter-spacing:-.065em; margin:0 0 1rem; font-weight:800; }
    .hero p { color:var(--muted); max-width:720px; font-size:1.02rem; line-height:1.65; margin:0; }
    .hero-meta { margin-top:1.25rem; display:flex; gap:1.6rem; color:#71717A; font-size:.76rem; }
    .section-head { display:flex; align-items:end; justify-content:space-between; gap:1rem; margin:2.4rem 0 1rem; }
    .section-head h2 { font-size:1.55rem; margin:0; } .section-head p { color:var(--muted); margin:0; font-size:.84rem; }
    .metric-card { min-height:134px; padding:1.25rem 1.3rem; border:1px solid var(--line); background:linear-gradient(145deg,#19191C,#121214); border-radius:12px; }
    .metric-label { color:#8B8B93; font-size:.72rem; letter-spacing:.1em; text-transform:uppercase; font-weight:750; }
    .metric-value { color:white; font-size:2.2rem; line-height:1.15; letter-spacing:-.045em; font-weight:780; margin:.55rem 0 .3rem; }
    .metric-note { color:#71717A; font-size:.77rem; } .metric-accent { color:var(--red); }
    .signal { padding:1.1rem 1.2rem; background:var(--panel); border:1px solid var(--line); border-left:2px solid var(--red); border-radius:10px; min-height:116px; }
    .signal-index { color:#52525B; font-size:.68rem; font-weight:800; letter-spacing:.1em; }
    .signal-title { color:white; font-size:1.05rem; font-weight:700; margin:.45rem 0 .25rem; }
    .signal-copy { color:#8B8B93; font-size:.78rem; line-height:1.45; }
    .empty { border:1px solid var(--line); border-radius:12px; padding:4rem 2rem; text-align:center; background:var(--panel); color:var(--muted); }
    .detail-card { background:var(--panel); border:1px solid var(--line); border-radius:12px; padding:1.4rem; }
    .detail-card h3 { margin:.15rem 0 .5rem; font-size:1.55rem; letter-spacing:-.03em; }
    .detail-card p { color:var(--muted); line-height:1.6; }
    .pill { display:inline-block; padding:.22rem .55rem; margin:0 .3rem .3rem 0; border:1px solid #343438; border-radius:999px; color:#C7C7CC; font-size:.7rem; }
    .footer-note { color:#52525B; font-size:.72rem; margin-top:3rem; padding-top:1rem; border-top:1px solid var(--line); }
    @media (max-width:800px) { .block-container { padding:1.5rem 1rem 3rem; } .hero h1 { font-size:2.7rem; } .hero-meta { flex-direction:column; gap:.3rem; } }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def load_data(path: Path) -> pd.DataFrame:
    data = pd.read_csv(path)
    data["date_added"] = pd.to_datetime(data["date_added"].astype(str).str.strip(), errors="coerce")
    data = data.dropna(subset=["date_added"]).copy()
    data["year_added"] = data["date_added"].dt.year.astype(int)
    data["primary_country"] = data["country"].fillna("Unknown").astype(str).str.split(",").str[0].str.strip()
    for column, fallback in {"rating":"Unrated", "director":"Not listed", "cast":"Not listed", "description":"No description available."}.items():
        data[column] = data[column].fillna(fallback)
    data["age_when_added"] = data["year_added"] - data["release_year"]
    return data


def chart_layout(fig: go.Figure, height: int = 410) -> go.Figure:
    fig.update_layout(template="plotly_dark", height=height, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(family="Arial, sans-serif", color=MUTED, size=12), margin=dict(l=18,r=18,t=30,b=18), hoverlabel=dict(bgcolor="#27272A",bordercolor="#3F3F46",font_color="white"), legend=dict(orientation="h",y=1.08,x=0,title_text=""))
    fig.update_xaxes(gridcolor=GRID, zeroline=False, title=None)
    fig.update_yaxes(gridcolor=GRID, zeroline=False, title=None)
    return fig


def metric(label: str, value: str, note: str, accent: bool = False) -> None:
    value_class = "metric-value metric-accent" if accent else "metric-value"
    st.markdown(f'<div class="metric-card"><div class="metric-label">{html.escape(label)}</div><div class="{value_class}">{html.escape(value)}</div><div class="metric-note">{html.escape(note)}</div></div>', unsafe_allow_html=True)


def signal(index: str, title: str, copy: str) -> None:
    st.markdown(f'<div class="signal"><div class="signal-index">{html.escape(index)}</div><div class="signal-title">{html.escape(title)}</div><div class="signal-copy">{html.escape(copy)}</div></div>', unsafe_allow_html=True)


df = load_data(DATA_PATH)
st.sidebar.markdown('<div class="brand"><div class="brand-mark">N</div><div class="brand-name">CATALOG INTELLIGENCE</div></div>', unsafe_allow_html=True)
st.sidebar.markdown("#### Shape the catalog")
st.sidebar.caption("Every view and takeaway responds to these controls.")
type_options = sorted(df["type"].unique().tolist())
selected_types = st.sidebar.multiselect("Format", type_options, default=type_options)
year_min, year_max = int(df["year_added"].min()), int(df["year_added"].max())
selected_years = st.sidebar.slider("Added to Netflix", year_min, year_max, (year_min, year_max))
country_options = df["primary_country"].value_counts().head(30).index.tolist()
selected_countries = st.sidebar.multiselect("Production country", country_options, placeholder="All countries")
rating_options = sorted(df["rating"].unique().tolist())
selected_ratings = st.sidebar.multiselect("Maturity rating", rating_options, placeholder="All ratings")
query = st.sidebar.text_input("Find a title", placeholder="e.g. Stranger Things")
st.sidebar.markdown("---")
st.sidebar.caption(f"Dataset snapshot  •  {len(df):,} dated titles  •  through {year_max}")

filtered = df[df["type"].isin(selected_types) & df["year_added"].between(*selected_years)].copy()
if selected_countries:
    filtered = filtered[filtered["primary_country"].isin(selected_countries)]
if selected_ratings:
    filtered = filtered[filtered["rating"].isin(selected_ratings)]
if query.strip():
    filtered = filtered[filtered["title"].str.contains(query.strip(), case=False, na=False, regex=False)]

st.markdown(f'<div class="hero"><div class="eyebrow">Streaming portfolio analysis</div><h1>Inside the Netflix catalog.</h1><p>Explore how format, geography and release strategy shaped the titles available in this public catalog snapshot.</p><div class="hero-meta"><span>CATALOG WINDOW&nbsp; {year_min}—{year_max}</span><span>FILTERED VIEW&nbsp; {len(filtered):,} TITLES</span><span>UPDATED FROM LOCAL DATA</span></div></div>', unsafe_allow_html=True)

overview_tab, explorer_tab, notes_tab = st.tabs(["Overview", "Title explorer", "About the data"])

with overview_tab:
    if filtered.empty:
        st.markdown('<div class="empty"><strong>No titles match this view.</strong><br>Widen the year range or clear a filter in the sidebar.</div>', unsafe_allow_html=True)
    else:
        total = len(filtered)
        movies = int((filtered["type"] == "Movie").sum())
        shows = int((filtered["type"] == "TV Show").sum())
        median_age = filtered["age_when_added"].clip(lower=0).median()
        m1,m2,m3,m4 = st.columns(4)
        with m1: metric("Titles in view", f"{total:,}", f"{total / len(df):.1%} of the dated catalog", True)
        with m2: metric("Movies", f"{movies:,}", f"{movies / total:.0%} of this selection")
        with m3: metric("Series", f"{shows:,}", f"{shows / total:.0%} of this selection")
        lag_value = f"{median_age:.0f} yr" if round(median_age) == 1 else f"{median_age:.0f} yrs"
        with m4: metric("Typical catalog lag", lag_value, "Median release-to-addition gap")

        st.markdown('<div class="section-head"><h2>Catalog velocity</h2><p>Titles added each year, split by format</p></div>', unsafe_allow_html=True)
        yearly = filtered.groupby(["year_added","type"]).size().reset_index(name="titles")
        fig_timeline = px.area(yearly, x="year_added", y="titles", color="type", color_discrete_map={"Movie":RED,"TV Show":"#71717A"}, category_orders={"type":["TV Show","Movie"]}, labels={"year_added":"Year","titles":"Titles","type":"Format"})
        fig_timeline.update_traces(line=dict(width=2), hovertemplate="%{y:,} titles<extra>%{fullData.name}</extra>")
        fig_timeline.update_xaxes(dtick=2)
        st.plotly_chart(chart_layout(fig_timeline,440), width="stretch", config={"displayModeBar":False})

        peak_by_year = filtered.groupby("year_added").size()
        peak_year, peak_count = int(peak_by_year.idxmax()), int(peak_by_year.max())
        latest_year, latest_count = int(filtered["year_added"].max()), int(peak_by_year.loc[filtered["year_added"].max()])
        country_mode = filtered.loc[filtered["primary_country"] != "Unknown", "primary_country"].mode()
        top_country = country_mode.iloc[0] if not country_mode.empty else "Unknown"
        genres = filtered["listed_in"].dropna().str.split(",").explode().str.strip()
        top_genre = genres.mode().iloc[0] if not genres.empty else "Not available"
        st.markdown('<div class="section-head"><h2>Signals in this view</h2><p>Computed from the active selection</p></div>', unsafe_allow_html=True)
        s1,s2,s3 = st.columns(3)
        with s1: signal("01  ·  MOMENTUM", f"{peak_year} was the peak", f"{peak_count:,} titles were added—{peak_count / total:.0%} of this selection.")
        with s2: signal("02  ·  GEOGRAPHY", f"{top_country} leads", "It is the most common primary production country in the current view.")
        with s3: signal("03  ·  CONTENT", f"{top_genre} dominates", f"The latest selected year ({latest_year}) contains {latest_count:,} titles.")

        st.markdown('<div class="section-head"><h2>Portfolio composition</h2><p>Where the catalog comes from and what audiences get</p></div>', unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        with c1:
            countries = filtered.loc[filtered["primary_country"] != "Unknown", "primary_country"].value_counts().head(10).sort_values()
            fig_country = go.Figure(go.Bar(x=countries.values,y=countries.index,orientation="h",marker_color=["#3F3F46"]*max(len(countries)-1,0)+([RED] if len(countries) else []),text=countries.values,textposition="outside",cliponaxis=False,hovertemplate="%{x:,} titles<extra></extra>"))
            fig_country.update_layout(title=dict(text="Leading production countries",x=.04,font=dict(size=15,color=INK)))
            st.plotly_chart(chart_layout(fig_country), width="stretch", config={"displayModeBar":False})
        with c2:
            genre_counts = genres.value_counts().head(10).sort_values()
            fig_genre = go.Figure(go.Bar(x=genre_counts.values,y=genre_counts.index,orientation="h",marker_color="#52525B",text=genre_counts.values,textposition="outside",cliponaxis=False,hovertemplate="%{x:,} titles<extra></extra>"))
            fig_genre.update_layout(title=dict(text="Most represented genres",x=.04,font=dict(size=15,color=INK)))
            st.plotly_chart(chart_layout(fig_genre), width="stretch", config={"displayModeBar":False})

        st.markdown('<div class="section-head"><h2>Release recency</h2><p>How old titles were when they entered the catalog</p></div>', unsafe_allow_html=True)
        lag = filtered[filtered["age_when_added"].between(0,50)].copy()
        lag["lag_group"] = pd.cut(lag["age_when_added"], bins=[-1,0,2,5,10,20,50], labels=["Same year","1–2 years","3–5 years","6–10 years","11–20 years","21+ years"])
        lag_counts = lag["lag_group"].value_counts(sort=False)
        fig_lag = go.Figure(go.Bar(x=lag_counts.index.astype(str),y=lag_counts.values,marker_color=[RED]+["#3F3F46"]*(len(lag_counts)-1),text=lag_counts.values,textposition="outside",hovertemplate="%{y:,} titles<extra></extra>"))
        st.plotly_chart(chart_layout(fig_lag,350), width="stretch", config={"displayModeBar":False})

with explorer_tab:
    st.markdown('<div class="section-head"><h2>Browse the selection</h2><p>Search from the sidebar, then inspect a title</p></div>', unsafe_allow_html=True)
    if filtered.empty:
        st.markdown('<div class="empty">No titles available to explore.</div>', unsafe_allow_html=True)
    else:
        title_options = filtered.sort_values(["year_added","title"],ascending=[False,True])["title"].tolist()
        selected_title = st.selectbox("Title detail", title_options, label_visibility="collapsed")
        row = filtered[filtered["title"] == selected_title].iloc[0]
        tags = [row["type"],str(row["rating"]),str(row["duration"]),str(row["primary_country"])]
        tag_html = "".join(f'<span class="pill">{html.escape(tag)}</span>' for tag in tags if tag != "nan")
        st.markdown(f'<div class="detail-card"><div class="eyebrow">Added {row["date_added"]:%B %Y} · Released {int(row["release_year"])}</div><h3>{html.escape(str(row["title"]))}</h3><div>{tag_html}</div><p>{html.escape(str(row["description"]))}</p><p><strong style="color:#D4D4D8">Director</strong><br>{html.escape(str(row["director"]))}</p><p><strong style="color:#D4D4D8">Cast</strong><br>{html.escape(str(row["cast"]))}</p></div>', unsafe_allow_html=True)
        table = filtered[["title","type","release_year","year_added","primary_country","rating","duration"]].sort_values("year_added",ascending=False)
        st.markdown("#### All matching titles")
        st.dataframe(table,width="stretch",hide_index=True,column_config={"title":"Title","type":"Format","release_year":"Released","year_added":"Added","primary_country":"Country","rating":"Rating","duration":"Runtime"})
        st.download_button("Download filtered catalog",table.to_csv(index=False).encode("utf-8"),file_name="netflix_catalog_selection.csv",mime="text/csv")

with notes_tab:
    st.markdown("""### Read this dashboard correctly

This is a **historical catalog snapshot**, not a live view of Netflix availability. A title's “added” year reflects the dataset record and does not prove it remains available today.

- Country analysis uses the first listed country as the primary country.
- Genre counts are multi-label: one title can contribute to several genres.
- Catalog lag is the difference between release year and the year added to Netflix.
- Titles without a valid addition date are excluded from time-based analysis.

The dashboard is intended for exploratory portfolio analysis, not current availability decisions.
""")
    st.caption(f"Source file: {DATA_PATH.name} · {len(df):,} usable dated records · latest addition year: {year_max}")

st.markdown('<div class="footer-note">NETFLIX CATALOG INTELLIGENCE &nbsp;·&nbsp; Independent exploratory analysis &nbsp;·&nbsp; Netflix is a trademark of Netflix, Inc.</div>', unsafe_allow_html=True)
