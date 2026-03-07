# 🎬 Netflix Analysis Dashboard

<div align="center">
  
![Netflix](https://img.shields.io/badge/Netflix-E50914?style=for-the-badge&logo=netflix&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

**An interactive data visualization dashboard for exploring Netflix's content catalog**

[Live Demo](https://netflix-dashboard-pix.streamlit.app/) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Getting Started](#-getting-started)
- [Dashboard Features](#-dashboard-features-explained)
- [How the Filters Work](#-how-the-filters-work)
- [Design Decisions](#-design-decisions)
- [Key Insights](#-key-insights)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

The Netflix Analysis Dashboard is an interactive web application built with Streamlit that allows users to explore and analyze Netflix's extensive content catalog. With dynamic filtering capabilities and beautiful visualizations, users can uncover insights about content distribution, growth trends, geographical patterns, and genre popularity.

### Why This Project?

- **Interactive Exploration**: Filter and analyze data in real-time
- **Visual Insights**: Beautiful charts and graphs for easy understanding
- **Modern Design**: Clean, light-themed UI inspired by modern web applications
- **Data-Driven**: Backed by real Netflix content data

---

## ✨ Features

### 🔍 **Dynamic Filtering System**
- Filter by content type (Movies vs TV Shows)
- Select specific years when content was added
- Filter by country of origin (top 20 countries)
- Filter by content rating (PG-13, TV-MA, etc.)
- All filters work together and update visualizations in real-time

### 📊 **Interactive Visualizations**
- **Content Distribution**: Pie chart showing Movies vs TV Shows ratio
- **Growth Timeline**: Line chart tracking content additions over time
- **Country Analysis**: Bar chart of top content-producing countries
- **Genre Analysis**: Most popular genres across the platform
- **Rating Distribution**: Content rating breakdown

### 📈 **Key Metrics Dashboard**
- Total number of titles (with percentage of catalog)
- Movie count and percentage
- TV Show count and percentage
- Number of unique countries represented

### 🎨 **Modern Design**
- Clean, light-themed interface
- Netflix-inspired color scheme
- Gradient backgrounds and card-based layout
- Fully responsive design
- Smooth animations and transitions

---

## 🛠 Tech Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core programming language | 3.8+ |
| **Streamlit** | Web application framework | 1.31.0 |
| **Pandas** | Data manipulation and analysis | 2.2.0 |
| **Plotly** | Interactive visualizations | 5.18.0 |
| **Pillow** | Image processing | 10.2.0 |

---

## 📁 Project Structure

```
netflix-dashboard/
│
├── streamlit_app.py           # Main application file
├── requirements.txt           # Python dependencies
├── README.md                  # This file
│
├── netflix_data/
│   └── netflix_titles.csv    # Netflix dataset
│
├── images.png                # Netflix logo
│
└── venv/                     # Virtual environment (not in repo)
```

---

## 💻 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/netflix-dashboard.git
   cd netflix-dashboard
   ```

2. **Create a virtual environment**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python -c "import streamlit, pandas, plotly; print('✅ All packages installed successfully!')"
   ```

---

## 🚀 Getting Started

### Running the Dashboard

1. **Ensure your virtual environment is activated**
   ```bash
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

2. **Launch the application**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Access the dashboard**
   - Your browser should automatically open to `http://localhost:8501`
   - If not, manually navigate to the URL shown in your terminal

4. **Stop the application**
   - Press `Ctrl + C` in your terminal

---

## 📊 Dashboard Features Explained

### 1. **Header Section**
- Netflix logo and title
- Beautiful gradient background
- Subtitle describing the dashboard's purpose

### 2. **Sidebar Filters** (Left Panel)

#### Content Type Filter
- **Purpose**: Choose between Movies, TV Shows, or both
- **How it works**: Multi-select dropdown
- **Default**: Both types selected
- **Use case**: "Show me only TV Shows added in the last 3 years"

#### Year Added Filter
- **Purpose**: Select the time range when content was added to Netflix
- **How it works**: Interactive slider with min/max years
- **Default**: Full range (all years in dataset)
- **Use case**: "Show me content added between 2019-2021"

#### Country Filter
- **Purpose**: Filter by country of origin
- **How it works**: Multi-select showing top 20 countries
- **Default**: "All" (no filtering)
- **Use case**: "Compare content from United States vs India"

#### Rating Filter
- **Purpose**: Filter by content rating (age appropriateness)
- **How it works**: Multi-select showing all available ratings
- **Default**: "All" (no filtering)
- **Use case**: "Show me only TV-MA and R-rated content"

### 3. **Key Metrics** (Top Row)
Four cards displaying:
- **Total Titles**: Number of items matching filters (with % of catalog)
- **Movies**: Count and percentage of movies
- **TV Shows**: Count and percentage of shows
- **Countries**: Number of unique countries in filtered data

### 4. **Content Distribution** (Section 1)
- **Left**: Interactive donut chart (Movies vs TV Shows)
- **Right**: Quick stats card with percentages
- **Insight**: Understand the content mix at a glance

### 5. **Growth Timeline** (Section 2)
- **Visualization**: Multi-line chart showing content additions over time
- **Lines**: Separate lines for Movies (red) and TV Shows (teal)
- **Interaction**: Hover to see exact numbers, zoom in/out
- **Peak Year Indicator**: Automatically shows which year had the most additions

### 6. **Top Countries** (Section 3)
- **Visualization**: Horizontal bar chart
- **Data**: Top 10 content-producing countries
- **Color**: Gradient red scale (Netflix theme)
- **Labels**: Shows exact count on each bar

### 7. **Genres & Ratings** (Section 4)
Two side-by-side visualizations:
- **Left**: Top 10 most popular genres
- **Right**: Most common content ratings
- Both use bar charts with gradient coloring

### 8. **Key Insights** (Section 5)
Three insight cards explaining:
- Content mix strategy
- Global reach and international expansion
- Content addition patterns

### 9. **Data Preview** (Expandable)
- Click to expand and see raw filtered data
- Shows first 100 rows
- Displays key columns: title, type, country, year, rating, genres

---

## 🔧 How the Filters Work

### Filter Application Logic

```python
# Filters are applied sequentially:

1. Start with full dataset (df)
2. Copy to filtered_df
3. Apply Type filter → Keep only selected types
4. Apply Year filter → Keep only items in year range
5. Apply Country filter → Keep only selected countries (if not "All")
6. Apply Rating filter → Keep only selected ratings (if not "All")
7. All visualizations use filtered_df
```

### Example Filter Combinations

**Scenario 1: Recent US TV Shows**
```
Type: TV Show
Year: 2020-2024
Country: United States
Rating: All
→ Result: All US TV shows added in the last few years
```

**Scenario 2: International Family Content**
```
Type: All
Year: All
Country: All (except United States)
Rating: TV-G, TV-PG, PG, G
→ Result: Family-friendly international content
```

**Scenario 3: Mature Content Growth**
```
Type: All
Year: 2015-2024
Country: All
Rating: TV-MA, R
→ Result: Track growth of mature content over last decade
```

---

## 🎨 Design Decisions

### Why Light Theme?

Unlike the dark Netflix UI, this dashboard uses a light theme because:
1. **Better for data visualization**: Light backgrounds make charts more readable
2. **Professional appearance**: Clean, modern look for analytical tools
3. **Reduced eye strain**: Better for extended data exploration sessions
4. **Print-friendly**: Screenshots and exports look better

### Color Palette

```css
Netflix Red (#E50914):   Primary accent, brand recognition
Teal (#14b8a6):          Secondary accent, TV Shows
Blue (#2563eb):          Tertiary accent, insights
Dark Gray (#0f172a):     Text color
Light Gray (#f6f7fb):    Background
```

### Typography

- **Font Family**: Inter (modern, clean, highly readable)
- **Hierarchy**: Clear distinction between headings and body text
- **Sizing**: Responsive and accessible

### Layout Principles

1. **Card-based design**: Each section is visually contained
2. **Consistent spacing**: Uniform margins and padding
3. **Visual hierarchy**: Important metrics at the top
4. **Progressive disclosure**: Details hidden in expanders

---

## 💡 Key Insights

### What the Data Reveals

1. **Content Evolution**
   - Netflix's content strategy shifted dramatically around 2015-2016
   - Huge increase in TV Shows production
   - Peak content additions around 2019

2. **Global Expansion**
   - United States still dominates production
   - But India, UK, Japan, South Korea show significant growth
   - International content became a key strategy post-2016

3. **Genre Trends**
   - International Movies and Dramas are top categories
   - Stand-up Comedy saw massive growth
   - Documentaries remain consistently popular

4. **Rating Distribution**
   - TV-MA (Mature Audiences) is most common
   - Indicates focus on adult-oriented content
   - Family content (TV-G, PG) is smaller portion

---

## 🔮 Future Enhancements

### Planned Features

- [ ] **Search functionality**: Find specific titles by name
- [ ] **Director/Cast analysis**: Most prolific creators
- [ ] **Duration analysis**: Average runtime by type
- [ ] **Release year analysis**: Compare release year vs added year
- [ ] **Text analysis**: Word clouds from descriptions
- [ ] **Export feature**: Download filtered data as CSV
- [ ] **Comparison mode**: Side-by-side year comparisons
- [ ] **Dark mode toggle**: User preference for theme
- [ ] **Mobile optimization**: Better responsive design
- [ ] **Advanced filters**: Multiple genre selection, duration ranges

### Technical Improvements

- [ ] **Caching optimization**: Faster filter updates
- [ ] **Database integration**: Support larger datasets
- [ ] **API integration**: Real-time Netflix data (if available)
- [ ] **Unit tests**: Ensure data processing reliability
- [ ] **CI/CD pipeline**: Automated testing and deployment

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
6. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Add comments for complex logic
- Update documentation for new features
- Test thoroughly before submitting

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Dataset**: Netflix Titles Dataset from Kaggle
- **Streamlit**: Amazing framework for data apps
- **Plotly**: Powerful visualization library
- **Netflix**: Inspiration for design and content

---

<div align="center">

**⭐ If you found this project helpful, please consider giving it a star! ⭐**

Made with ❤️ using Python, Streamlit, and Plotly

</div>
