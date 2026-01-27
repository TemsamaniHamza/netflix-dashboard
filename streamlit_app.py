import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title="Netflix Analysis", page_icon="🎬", layout="wide")

df = pd.read_csv("netflix_data/netflix_titles.csv")  

logo = Image.open("images.png")

col1, col2 = st.columns([1, 6])  # adjust width ratios

with col1:
    st.image(logo, width=120)

with col2:
    st.title("Netflix Analysis Dashboard")
    st.markdown("#### Explore Netflix movies and TV shows interactively")

import pandas as pd
import streamlit as st

st.subheader("Raw Data Sample")

@st.cache_data
def clean_data(df):
    df = df.copy() 
    df['date_added'] = df['date_added'].astype(str).str.strip()
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    return df

df = clean_data(df)

st.write(f"**Total Titles:** {len(df):,}")

st.subheader("📊 Content Distribution")

col1, col2 = st.columns(2)

with col1:
    type_counts = df['type'].value_counts()
    fig = px.pie(data_frame=type_counts,
                 values=type_counts.values,
                 names=type_counts.index,
                 color_discrete_sequence=px.colors.qualitative.Set3
                 )
    st.plotly_chart(fig, use_container_width=True)
with col2:
    movies = len(df[df['type'] == 'Movie'])
    shows = len(df[df['type'] == 'TV Show'])
    
    st.metric("Movies", f"{movies:,}", f"{movies/len(df)*100:.1f}%")
    st.metric("TV Shows", f"{shows:,}", f"{shows/len(df)*100:.1f}%")

st.subheader("📈 Content Added Over Time")

# Group by year
yearly = df.groupby(['year_added', 'type']).size().reset_index(name='count')

fig = px.line(yearly, x='year_added', y='count', color='type',
              title='Netflix Content Growth',
              labels={'year_added': 'Year', 'count': 'Titles Added'},
              markers=True)
st.plotly_chart(fig, use_container_width=True)

st.info("📌 Netflix dramatically increased content production after 2015")



st.subheader("🌍 Top Content Producing Countries")

df_clean = df.dropna(subset=['release_year', 'country', 'type', 'listed_in'])
country_counts = df_clean['country'].value_counts().head(10)
fig_country = px.bar(
    x = country_counts.values,
    y = country_counts.index,
    title="Top 10 Countries by Number of Titles in All time",
    labels={'y':'Country', 'x':'Number of Titles'},
)
st.plotly_chart(fig_country, use_container_width=True)




st.sidebar.header("🔍 Filters")

# Type filter
type_filter = st.sidebar.multiselect(
    "Content Type",
    options=df['type'].unique(),
    default=df['type'].unique()
)

# Year filter
year_range = st.sidebar.slider(
    "Year Added",
    int(df['year_added'].min()),
    int(df['year_added'].max()),
    (int(df['year_added'].min()), int(df['year_added'].max()))
)

# Apply filters
filtered_df = df[
    (df['type'].isin(type_filter)) &
    (df['year_added'] >= year_range[0]) &
    (df['year_added'] <= year_range[1])
]

# Update all charts to use filtered_df instead of df






st.subheader("🎭 Popular Genres")

# Top genres
genres = df['listed_in'].dropna()
genre_list = []
for genre_str in genres:
    genre_list.extend([g.strip() for g in genre_str.split(',')])

top_genres = pd.Series(genre_list).value_counts().head(10)

fig = px.bar(top_genres, title='Top 10 Genres')
st.plotly_chart(fig, use_container_width=True)

# Ratings
st.subheader("⭐ Content Ratings")
ratings = df['rating'].value_counts().head(8)
fig = px.bar(ratings, title='Most Common Ratings')
st.plotly_chart(fig, use_container_width=True)




# Add at the top
st.markdown("""
### Key Insights 🔍
- 📺 TV Shows now dominate Netflix's catalog
- 🌍 International content has exploded since 2016
- 📊 2019 was the peak year for content additions
""")

# Add footer
st.markdown("---")
st.markdown("Built with Python • Streamlit • Plotly • Pandas")



















# # Sample data
# df = pd.DataFrame({
#     'year': [2018, 2019, 2020, 2021, 2022],
#     'count': [100, 150, 200, 180, 220]
# })

# # Display
# st.dataframe(df)

# # Chart
# fig = px.line(df, x='year', y='count', title='Growth Over Time')
# st.plotly_chart(fig)

# # Interaction
# year_filter = st.slider("Select Year", 2018, 2022)
# filtered = df[df['year'] >= year_filter]
# st.write(filtered)
