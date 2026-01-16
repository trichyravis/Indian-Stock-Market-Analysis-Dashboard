# 📊 Indian Stock Market Analysis - Streamlit Dashboard

Interactive analysis of "Is Indian Stock Market Growth Driven by Revenue Expansion or Margin Re-Rating?"

---

## 🚀 Quick Start

### Installation

```bash
# Clone or navigate to the directory containing the app files

# Install dependencies
pip install -r requirements.txt --break-system-packages

# Run the app
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📱 Features

### 🏠 Overview Dashboard
- **Quick Summary**: Revenue vs Profit growth comparison
- **Visual Charts**: 5-year divergence illustrated
- **Scenario Picker**: Quick look at 3 probability-weighted scenarios
- **Alert Boxes**: Key metrics and concerns highlighted

### 📈 5-Year Trend Analysis
- **Comprehensive Table**: FY2021-FY2025 data with growth metrics
- **Bar Charts**: Revenue, EBITDA, PAT growth comparison
- **Line Charts**: Margin trends over 5 years
- **Insights**: Key patterns and observations

### 📊 Quarterly Deep-Dive
- **Recent Performance**: Q1, Q2, Q3 FY2025 trends
- **Divergence Highlight**: Revenue collapse vs profit recovery
- **Margin Support Analysis**: What's holding up profits?
- **Critical Observations**: 16-quarter low, margin engineering

### 🏦 Sector Analysis
- **Sector Performance Table**: 10 sectors with growth metrics
- **Scatter Plot**: Revenue vs Profit positioning
- **Pie Chart**: Sector weight in Nifty 50
- **Risk Alerts**:
  - 🔴 Energy: CRISIS (-35% profit)
  - 🟡 Financials: SLOWING (but largest)
  - 🟢 Industrials: STRONG (+25.7% profit)
  - 🟢 IT: STABILIZING (export recovery)
- **Top/Bottom Performers**: Best and worst sectors

### 📉 Earnings Downgrades
- **Downgrade Cascade**: Sep 2024 to Feb 2025 tracking
- **Visual Timeline**: Shows -67% earnings estimate cut
- **Impact Analysis**: What triggered downgrades?
- **Metrics**: Downgrade pace and magnitude

### 🎯 Scenario Analysis
- **Interactive Selector**: Choose scenario to analyze
- **Detailed Metrics**:
  - Assumption description
  - Earnings growth CAGR
  - Nifty return per annum
  - Probability weight
- **Earnings Path**: Year-by-year growth visualization
- **Nifty Target Path**: Stock market level projections
- **Scenario Comparison**: All 3 scenarios side-by-side

**Three Scenarios Included:**
1. **Base Case (50%)**: Margin resilience, slow revenue
   - Earnings CAGR: 9.7%
   - Nifty Target: 26,000-27,000
   - Return: +10% p.a.

2. **Bear Case (25%)**: Margin compression, input cost spike
   - Earnings CAGR: 4.8%
   - Nifty Target: 20,000-21,000
   - Return: -0.2% p.a.

3. **Bull Case (25%)**: Revenue recovery, RBI support
   - Earnings CAGR: 12.8%
   - Nifty Target: 33,000-35,000
   - Return: +14.5% p.a.

### 📋 Data Explorer
- **Download Datasets**: Export any table as CSV
- **Multiple Datasets**:
  - 5-Year Trend
  - Quarterly Performance
  - Sector Analysis
  - Earnings Downgrades

---

## 📊 Data Included

### 5-Year Dataset (FY2021-FY2025)
- Revenue Growth (%)
- EBITDA Growth (%)
- PAT Growth (%)
- EBITDA Margin (%)
- PAT Margin (%)

### Quarterly Data (FY2025)
- Q1, Q2, Q3 performance
- Revenue, EBITDA, PAT growth

### Sector Performance (10 sectors)
- Financials, Energy, IT, Industrials, Materials
- Consumer Discretionary, Healthcare, Consumer Staples, Utilities, Telecom
- Revenue growth, Profit growth, Weight in Nifty

### Earnings Downgrades
- Monthly tracking Sep 2024 – Feb 2025
- Consensus estimate revisions

### Scenario Models
- 3 probability-weighted scenarios
- 3-year earnings and valuation projections

---

## 🎨 Design Features

### Color Coding
- **Green (#00AA00)**: Positive, strong growth
- **Blue (#0066CC)**: Revenue, growth drivers
- **Red (#CC0000)**: Negative, concern areas
- **Orange (#FFA500)**: Neutral, base case
- **Yellow**: Warnings, caution areas

### Interactive Elements
- **Radio Buttons**: Page navigation
- **Dropdowns**: Data selection
- **Metrics Cards**: Key statistics
- **Download Buttons**: CSV export

### Responsive Layout
- **Columns**: Multi-column layouts for comparison
- **Charts**: Full-width Plotly visualizations
- **Tables**: Pandas dataframes with styling
- **Spacing**: Dividers for clarity

---

## 🔍 Navigation

**Sidebar Menu:**
- 7 main pages
- Quick metric summary
- Valuation alert display

**Each Page Includes:**
- Header explaining the section
- Multiple visualizations
- Detailed tables
- Key insights boxes
- Download options (where applicable)

---

## 💾 Download Data

From the Data Explorer page, you can download:
- `5_year_nifty_data.csv` - 5-year trend
- `quarterly_fy25_data.csv` - Quarterly performance
- `sector_analysis.csv` - Sector breakdown
- `earnings_downgrades.csv` - Downgrade tracking

---

## 📱 Deploy to Streamlit Cloud

To share your analysis publicly:

```bash
# 1. Push to GitHub
git push origin main

# 2. Go to https://share.streamlit.io/
# 3. Deploy by connecting GitHub repo
# 4. Select: streamlit_app.py as main file
# 5. App will be live at: https://share.streamlit.io/username/repo
```

---

## 🛠️ Customization

### Change Colors
Edit the `scenarios` dictionary colors:
```python
'color': '#003366'  # Change to your preferred color
```

### Add More Data
Update the DataFrames at the top of the script:
```python
five_year_data = pd.DataFrame({
    'Fiscal Year': [...],
    # Add more columns here
})
```

### Modify Scenarios
Update the `scenarios` dictionary:
```python
scenarios = {
    'Your Scenario (XX%)': {
        'description': 'Your assumption',
        'fy25_earnings': X.X,
        # Adjust parameters
    }
}
```

---

## 📋 File Structure

```
outputs/
├── streamlit_app.py          ← Main application file
├── requirements.txt          ← Dependencies
├── README_STREAMLIT.md       ← This file
├── 04_Indian_Market_Analysis_Revenue_vs_Margins.md
├── 05_Executive_Summary_OnePager.md
├── 06_Visual_Chart_Descriptions.md
├── 07_Master_Index_Complete_Package.md
└── [other analysis documents]
```

---

## 🚨 Troubleshooting

### Port Already in Use
```bash
streamlit run streamlit_app.py --server.port 8502
```

### Module Not Found
```bash
pip install -r requirements.txt --break-system-packages
```

### Charts Not Displaying
- Ensure Plotly is installed: `pip install plotly --break-system-packages`
- Clear browser cache and refresh

### Data Not Updating
- Edit the data dictionaries in the script
- Restart Streamlit: `Ctrl+C` and `streamlit run streamlit_app.py`

---

## 📞 Support

For questions about the analysis:
→ Refer to the analysis documents (04_Indian_Market_Analysis_...)

For Streamlit documentation:
→ Visit https://docs.streamlit.io/

---

## 📊 Key Findings Summary

**Headline:** Nifty 50 profit growth is decoupling from revenue growth

**Critical Numbers:**
- Revenue CAGR: 11.5% (FY21-FY25)
- Profit CAGR: 14.7% (53% faster)
- Current Revenue Growth: 4.5% (16-quarter LOW)
- Current Profit Growth: 9.5% (margin support only)
- Valuation Gap: -50% to -60%

**Three Scenarios:**
1. **Base (50%):** +10% annual, Nifty 26K-27K
2. **Bear (25%):** -0.2% annual, Nifty 20K-21K
3. **Bull (25%):** +14.5% annual, Nifty 33K-35K

**Critical Date:** Q4FY25 Earnings (May 2025)

---

## ✅ Changelog

### Version 1.0 (Jan 2026)
- Initial release
- 7 main pages
- 4 datasets included
- 3 scenarios
- 10 sector analysis
- Full interactive dashboard

---

## 📄 License & Attribution

**Analysis by:** Prof. V. Ravichandran | The Mountain Path – World of Finance (January 2026)

**Data Sources:** NSE, RBI, Business Standard, LSEG, CMIE

**Disclaimer:** This analysis is for educational purposes only. Not investment advice.

---

**Ready to explore the data? Run `streamlit run streamlit_app.py` and dive in!** 🚀
