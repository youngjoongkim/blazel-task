# LinkedIn Posts Data Analysis Project

A comprehensive data analysis project for LinkedIn posts dataset using Python, Pandas, and Plotly visualizations with Jupyter Notebook reporting.

## Project Structure

```
blazel-task/
├── notebooks/                          # Jupyter notebooks for analysis
│   ├── 01_data_cleaning.ipynb         # Data loading, cleaning, and validation
│   ├── 02_exploratory_analysis.ipynb  # Exploratory data analysis
│   ├── 03_engagement_analysis.ipynb   # Engagement metrics analysis
│   ├── 04_content_analysis.ipynb      # Content features analysis
│   ├── 05_temporal_analysis.ipynb     # Time-based patterns
│   ├── 06_industry_analysis.ipynb     # Industry-specific insights
│   └── 07_final_report.ipynb          # Comprehensive report
├── src/                                # Source code utilities
│   ├── data_loader.py                 # Data loading functions
│   ├── data_cleaner.py                # Data cleaning utilities
│   ├── feature_engineering.py         # Feature creation functions
│   ├── visualization_utils.py         # Plotly helper functions
│   └── analysis_utils.py              # Statistical analysis helpers
├── output/                             # Output files
│   ├── figures/                       # Plotly visualizations (HTML)
│   ├── tables/                        # CSV exports and statistics
│   └── report/                        # Final report exports
├── data/                               # Data directory
│   └── dataset_linkedin-post_*.json   # Raw dataset
├── ANALYSIS_PLAN.md                   # Detailed analysis plan
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

## Dataset Overview

- **11,227 LinkedIn posts** (83.42 MB JSON file)
- **41 unique fields** including engagement metrics, author info, content, timestamps
- **Key metrics**: likes, shares, comments, follower counts
- **Date range**: November 2024 - November 2025

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone or download this repository

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Install additional NLTK data (optional, for text analysis):
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Usage

### Running the Analysis

1. **Start Jupyter Notebook/Lab**:
```bash
jupyter lab
# or
jupyter notebook
```

2. **Run notebooks in order**:
   - Start with `01_data_cleaning.ipynb` to clean and prepare the data
   - Continue through notebooks 02-06 for specific analyses
   - Review `07_final_report.ipynb` for comprehensive findings

### Using Data Loader Directly

```python
from src.data_loader import load_and_prepare_data

# Load and prepare data
df = load_and_prepare_data('dataset_linkedin-post_2025-11-23_06-22-48-536.json')

# Display basic info
print(df.shape)
print(df.columns)
```

## Analysis Components

### 1. Data Cleaning (Notebook 01)
- Load raw JSON data
- Identify missing data and inconsistencies
- Clean and validate data
- Create derived features (text length, engagement scores, temporal features)
- Export cleaned dataset

### 2. Exploratory Analysis (Notebook 02)
- Generate descriptive statistics
- Analyze distributions
- Identify patterns and correlations
- Create summary visualizations

### 3. Engagement Analysis (Notebook 03)
- Post length vs engagement correlation
- Content type performance comparison
- Engagement metrics analysis
- Optimal post characteristics

### 4. Content Analysis (Notebook 04)
- Text features impact (hashtags, mentions, emojis)
- Media type effectiveness
- Content structure analysis
- Viral post characteristics

### 5. Temporal Analysis (Notebook 05) (TBD)
- Best posting times and days
- Temporal engagement patterns
- Time series analysis
- Seasonal trends

### 6. Industry Analysis (Notebook 06) (TBD)
- Industry-specific engagement patterns
- Content preferences by industry
- Cross-industry comparisons

### 7. Final Report (Notebook 07)
- Executive summary
- Key findings and insights
- Data-driven recommendations
- Interactive visualizations

## Key Features Created

### Text Features
- `text_length`: Character count
- `word_count`: Word count
- `has_question`: Contains question mark
- `has_hashtag`: Contains hashtags
- `has_emoji`: Contains emojis
- `has_url`: Contains URLs

### Engagement Features
- `total_engagement`: Sum of likes, shares, comments
- `engagement_score`: Weighted engagement (likes×1 + comments×2 + shares×3)
- `comment_to_like_ratio`: Engagement depth metric
- `share_to_like_ratio`: Virality metric
- `engagement_per_follower`: Normalized engagement

### Temporal Features
- `post_hour`, `post_dayofweek`, `post_dayname`: Posting time
- `time_of_day`: Morning/Afternoon/Evening/Night
- `is_weekend`: Weekend flag
- `post_quarter`: Quarterly grouping

### Categorical Features
- `length_category`: Empty/Very Short/Short/Medium/Long/Very Long
- `primary_content_type`: Image/Video/Article/Text/Reshare/etc.

## Visualizations

All visualizations are created using **Plotly** for interactivity:
- Hover tooltips with detailed information
- Zoom and pan capabilities
- Range sliders for time series
- Dropdown menus for metric switching
- Interactive legends

Visualizations are saved as standalone HTML files in `output/figures/` and can be viewed in any web browser.

## Output Files

### Tables (CSV)
- `linkedin_posts_cleaned.csv`: Cleaned dataset with all features
- `data_quality_report.csv`: Data quality metrics
- `missing_data_stats.csv`: Missing data analysis

### Figures (HTML)
- Interactive Plotly charts
- Standalone HTML files
- Embeddable in reports

### Reports
- Jupyter notebooks exported as HTML
- PDF exports (optional)

## Key Insights Expected

1. **Optimal post length** for maximum engagement
2. **Best performing content types**
3. **Impact of media** (images, videos, articles)
4. **Follower count influence** on engagement
5. **Best posting times** by day and hour
6. **Content features** that drive engagement
7. **Industry-specific patterns**
8. **Viral post characteristics**

## Technologies Used

- **Python 3.13+**: Core language
- **Pandas**: Data manipulation
- **NumPy**: Numerical operations
- **Plotly**: Interactive visualizations
- **Jupyter**: Interactive notebooks
- **SciPy/Scikit-learn**: Statistical analysis
- **NLTK**: Natural language processing

## Data Quality Notes

- ~10% of posts missing follower count data
- ~0.2% missing author information
- All timestamps are valid (Nov 2024 - Nov 2025)
