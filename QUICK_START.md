# Quick Start Guide

## 5-Minute Setup

### Step 1: Install Python 3.9+

Check your Python version:
```bash
python --version
```

If you need Python, download from [python.org](https://www.python.org/downloads/)

### Step 2: Install Dependencies

```bash
# Navigate to project directory
cd streamlit_market_analysis

# Install requirements
pip install --break-system-packages -r requirements.txt
```

**What gets installed:**
- streamlit 1.35.0
- pandas 2.2.0
- numpy 1.26.4
- plotly 5.18.0

### Step 3: Run the App

```bash
streamlit run app.py
```

✅ App opens automatically at `http://localhost:8501`

---

## Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```bash
pip install --upgrade --break-system-packages streamlit==1.35.0
```

### Issue: "Port 8501 is already in use"

**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### Issue: "Permission denied" on Linux/Mac

**Solution:**
```bash
chmod +x streamlit_market_analysis
```

---

## Deployment Options

### Option 1: Local Development

```bash
streamlit run app.py
```

**Best for**: Testing, customization, personal use

### Option 2: Streamlit Cloud (Free)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Deploy from GitHub repository

**Benefits**: Free hosting, auto-updates, shareable link

### Option 3: Self-Hosted Server

```bash
# Run with public access
streamlit run app.py \
  --server.port 80 \
  --server.address 0.0.0.0 \
  --logger.level error
```

---

## Customizing the Dashboard

### Change the Title

Edit `app.py`, line ~90:

```python
render_main_title(
    "📊 Your Custom Title",
    "Your custom subtitle"
)
```

### Update Data

Edit `data.py` and modify the dataframe values in:
- `get_five_year_data()`
- `get_quarterly_data()`
- `get_sector_data()`

### Change Colors

Edit `config.py`:

```python
COLORS = {
    'primary_dark': '#your_color',
    'accent_gold': '#your_color',
}
```

---

## File Structure Explained

```
streamlit_market_analysis/
│
├── app.py              # Main app - run this file
│                       # Contains all pages & logic
│
├── config.py           # Configuration
│                       # Colors, themes, settings
│
├── styles.py           # Styling functions
│                       # Reusable UI components
│
├── data.py             # Data module
│                       # All data preparation
│
├── requirements.txt    # Dependencies
│                       # pip install -r this
│
└── README.md          # Full documentation
```

---

## Running for the First Time

### On Windows

1. Open Command Prompt
2. Navigate to folder: `cd C:\path\to\streamlit_market_analysis`
3. Run: `streamlit run app.py`

### On Mac/Linux

1. Open Terminal
2. Navigate to folder: `cd /path/to/streamlit_market_analysis`
3. Run: `streamlit run app.py`

---

## Keyboard Shortcuts

| Command | Action |
|---------|--------|
| `R` | Rerun app |
| `C` | Clear cache |
| `Q` | Quit |
| `V` | Show/hide settings |

---

## Performance Tips

1. **Cache Data**: Already done with `@st.cache_data`
2. **Reduce Chart Quality**: Set `height=350` for smaller charts
3. **Lazy Load**: Charts only render when visible
4. **Optimize Images**: Keep plots under 2MB

---

## Updating Dependencies

To get the latest stable versions:

```bash
pip install --break-system-packages --upgrade -r requirements.txt
```

**Note**: Test changes in a separate environment first

---

## Getting Help

### Check Status
```bash
pip list | grep streamlit
python -c "import streamlit; print(streamlit.__version__)"
```

### View Logs
```bash
streamlit run app.py --logger.level debug
```

### Reset Everything
```bash
pip uninstall streamlit plotly pandas numpy -y
pip install --break-system-packages -r requirements.txt
```

---

## What's Next?

1. ✅ App is running
2. 📊 Explore all 7 analysis pages
3. 🎨 Customize colors and branding
4. 📈 Update data with your own
5. 🚀 Deploy to production

---

## Streamlit Documentation

- [Official Docs](https://docs.streamlit.io)
- [Component Gallery](https://streamlit.io/components)
- [Community Forum](https://discuss.streamlit.io)

---

**Good luck! 🚀**
