# Indian Market Analysis Dashboard

📊 **Comprehensive Nifty 50 Market Analysis Platform**  
**The Mountain Path - World of Finance**  
Prof. V. Ravichandran | Bangalore, India

---

## Overview

This Streamlit application provides an in-depth analysis of the Indian stock market (Nifty 50) with a focus on understanding whether profit growth is driven by **revenue expansion** or **margin re-rating**.

### Key Features

- **5-Year Performance Trend Analysis** - Historical growth patterns and margin evolution
- **Quarterly Deep-Dive** - Current quarter performance with risk indicators
- **Sector-wise Analysis** - Performance breakdown across 10 sectors with weight composition
- **Earnings Downgrade Tracking** - Visualization of consensus estimate revisions
- **3-Scenario Modeling** - Base, Bear, and Bull cases for next 3 years
- **Interactive Data Explorer** - Download and explore raw datasets

---

## Project Structure

```
streamlit_market_analysis/
├── app.py                 # Main application file
├── config.py             # Configuration & color scheme
├── styles.py             # Reusable styling functions
├── data.py               # Data loading & preparation
├── requirements.txt      # Dependencies
├── README.md            # This file
├── QUICK_START.md       # Installation & run instructions
└── CUSTOMIZATION_GUIDE.md # Styling & template customization
```

---

## Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Setup

1. **Clone or create project directory**
   ```bash
   mkdir streamlit_market_analysis
   cd streamlit_market_analysis
   ```

2. **Install dependencies**
   ```bash
   pip install --break-system-packages -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

The app will open at `http://localhost:8501`

---

## Design System

### Color Palette (Mountain Path Theme)

| Element | Color | RGB Code |
|---------|-------|----------|
| Primary Dark | Dark Blue | #003366 |
| Primary Mid | Medium Blue | #004d80 |
| Primary Light | Light Blue | #ADD8E6 |
| Accent Gold | Gold | #FFD700 |
| Accent Red | Red | #CC0000 |
| Accent Green | Green | #00AA00 |

### Typography

- **Headers**: Mountain Path styled headers with underlines
- **Font Size**: 12pt base, scaled for hierarchy
- **Style**: Professional academic presentation

---

## Features

### 🏠 Overview Page
- Executive summary of revenue vs profit divergence
- Key metrics sidebar
- Three-scenario projections
- Risk assessment

### 📈 5-Year Trend Analysis
- 5-year performance data table
- Growth rate comparison charts
- Margin trend visualization
- Historical insights and patterns

### 📊 Quarterly Analysis
- Q3FY25 deep-dive
- Quarterly growth trends
- Profit support mechanism breakdown
- Sustainability assessment

### 🏦 Sector Analysis
- 10-sector breakdown with weights
- Revenue vs Profit scatter plot
- Sector composition pie chart
- Risk-rated sector alerts

### 📉 Earnings Downgrades
- Estimate revision cascade (5-month)
- Key trigger analysis
- Downgrade timeline visualization

### 🎯 Scenarios
- Base Case (50% probability): 9.7% earnings CAGR
- Bear Case (25% probability): 4.8% earnings CAGR
- Bull Case (25% probability): 12.8% earnings CAGR
- Nifty 50 target paths for each scenario

### 📋 Data Explorer
- Interactive data tables
- CSV export functionality
- Multiple dataset views

---

## Data Sources

- **Primary**: NSE Corporate Performance Review (Q3FY25)
- **Secondary**: RBI Annual Reports, Business Standard
- **Analysis Period**: FY2021 – FY2025 (Projected)
- **Created**: January 2026

---

## Key Metrics

### Current Analysis (Q3FY25)

- **Revenue Growth CAGR (5-yr)**: 11.5%
- **Profit Growth CAGR (5-yr)**: 14.7%
- **Current Revenue Growth**: 4.5% (16-quarter LOW)
- **Current Profit Growth**: 9.5% (Margin-supported)
- **Divergence Factor**: 53% (Profit growing 53% faster than revenue)

### Valuation Metrics

- **Current P/E**: 25x
- **Fair Value P/E Range**: 10-12x
- **Overvaluation Gap**: -50% to -60%

---

## Main Insights

### The Core Problem: Margin Engineering

**FY2021-2024 (Healthy Growth)**
- ✅ Revenue growing
- ✅ Margins expanding
- ✅ Sustainable growth

**FY2025 (Concerning Shift)**
- ⚠️ Revenue collapsing (4.5% growth)
- ⚠️ Profit held up by margin support
- ❌ Not sustainable long-term

### Margin Support Mechanisms (Temporary)

1. **Cost Cuts (50%)**: Operating leverage
2. **Commodity Tailwinds (30%)**: Lower raw material costs
3. **Tax/Finance Benefits (20%)**: RBI rate cuts

---

## Customization Guide

### Updating Data

All data is in `data.py`:

```python
def get_five_year_data() -> pd.DataFrame:
    return pd.DataFrame({
        'Fiscal Year': [...],
        'Revenue Growth (%)': [...],
        # Update these arrays
    })
```

### Changing Colors

Edit `config.py`:

```python
COLORS = {
    'primary_dark': '#003366',  # Update hex codes
    'accent_gold': '#FFD700',
    # ... other colors
}
```

### Modifying Styling

Edit `styles.py` to customize:
- Header styles
- Info/Warning/Success boxes
- Footer content
- Sidebar components

---

## Performance Optimization

- **Data Caching**: Uses `@st.cache_data` for efficient data loading
- **Lazy Loading**: Charts render on-demand
- **Lightweight Dependencies**: Minimal package bloat

---

## Troubleshooting

### Streamlit not found
```bash
pip install --break-system-packages streamlit==1.35.0
```

### Port already in use
```bash
streamlit run app.py --logger.level=error --server.port 8502
```

### Import errors
Verify all files are in the same directory and run:
```bash
pip list | grep streamlit
```

---

## Author

**Prof. V. Ravichandran**
- 28+ Years Corporate Finance & Banking Experience
- 10+ Years Academic Excellence
- Bangalore, India

---

## License

Educational Use License  
All materials created for educational and training purposes.

---

## Disclaimer

This analysis is for educational purposes only. It is not investment advice. Please consult with financial advisors before making investment decisions based on this analysis.

---

## Version History

- **v1.0** (January 2026): Initial release with 7 analysis pages, 3 scenarios, sector breakdown
- **Latest**: v1.0

---

## Support & Feedback

For questions, customizations, or feedback regarding this dashboard, contact:
- Platform: The Mountain Path - World of Finance
- Author: Prof. V. Ravichandran
