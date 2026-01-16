# Customization Guide

## Overview

This guide explains how to customize every aspect of your dashboard while maintaining the Mountain Path design system.

---

## Part 1: Color Customization

### Using the Color Palette

All colors are defined in `config.py`:

```python
COLORS = {
    'primary_dark': '#003366',      # Dark Blue
    'primary_mid': '#004d80',       # Medium Blue
    'primary_light': '#ADD8E6',     # Light Blue
    'accent_gold': '#FFD700',       # Gold
    'accent_red': '#CC0000',        # Red
    'accent_green': '#00AA00',      # Green
    'accent_orange': '#FFA500',     # Orange
}
```

### Changing the Theme

**Example: Switch to Red & Gold theme**

In `config.py`:

```python
COLORS = {
    'primary_dark': '#8B0000',      # Dark Red
    'primary_mid': '#A52A2A',       # Brown Red
    'primary_light': '#FFE4E1',     # Light Pink
    'accent_gold': '#FFD700',       # Keep Gold
    'accent_red': '#DC143C',        # Crimson
    'accent_green': '#00AA00',      # Keep Green
}
```

All references automatically update throughout the app.

### Hex Color Resources

- [Color Picker](https://htmlcolorcodes.com)
- [Coolors.co](https://coolors.co) - Color scheme generator
- [Material Design Colors](https://material.io/design/color/)

---

## Part 2: Styling Components

### Headers

#### Option 1: Use Provided Functions

```python
from styles import render_main_title, render_section_header

# Main title
render_main_title(
    "📊 Your Title",
    "Your subtitle"
)

# Section header
render_section_header("📈 Your Section")
```

#### Option 2: Custom Header

```python
st.markdown("""
<h1 style='
    color: #003366;
    text-align: center;
    font-size: 32px;
    margin: 20px 0;
'>
📊 Your Custom Title
</h1>
""", unsafe_allow_html=True)
```

### Info Boxes

#### Success Box
```python
from styles import render_success_box

render_success_box(
    "<strong>✓ Key Success</strong><br/>"
    "Point 1<br/>"
    "Point 2"
)
```

#### Warning Box
```python
from styles import render_warning_box

render_warning_box(
    "<strong>⚠️ Key Warning</strong><br/>"
    "Alert 1<br/>"
    "Alert 2"
)
```

#### Info Box
```python
from styles import render_info_box

render_info_box(
    "<strong>ℹ️ Information</strong><br/>"
    "Detail 1<br/>"
    "Detail 2"
)
```

### Custom Boxes

Create a new styled box:

```python
from config import COLORS

st.markdown(f"""
<div style='
    background-color: #E8F4F8;
    border-left: 4px solid {COLORS['primary_dark']};
    padding: 15px;
    border-radius: 4px;
'>
Your custom content here
</div>
""", unsafe_allow_html=True)
```

---

## Part 3: Data Customization

### Updating 5-Year Data

In `data.py`:

```python
def get_five_year_data() -> pd.DataFrame:
    return pd.DataFrame({
        'Fiscal Year': ['FY2021', 'FY2022', ...],
        'Revenue Growth (%)': [10.5, 15.4, ...],  # ← Update these
        'EBITDA Growth (%)': [11.2, 22.8, ...],
        'PAT Growth (%)': [8.3, 25.7, ...],
    })
```

### Adding New Data

```python
def get_custom_data() -> pd.DataFrame:
    return pd.DataFrame({
        'Period': ['Jan', 'Feb', 'Mar'],
        'Metric1': [10, 15, 12],
        'Metric2': [20, 18, 25],
    })
```

Then use in `app.py`:

```python
from data import get_custom_data

custom_data = get_custom_data()
st.dataframe(custom_data)
```

---

## Part 4: Chart Customization

### Changing Chart Types

#### Bar Chart → Line Chart

```python
# Original (Bar)
fig = go.Figure()
fig.add_trace(go.Bar(
    x=data['Fiscal Year'],
    y=data['Revenue Growth (%)']
))

# Changed to Line
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=data['Fiscal Year'],
    y=data['Revenue Growth (%)'],
    mode='lines+markers'
))
```

### Chart Styling

```python
fig.update_layout(
    title="Your Chart Title",
    xaxis_title="X Axis",
    yaxis_title="Y Axis",
    template='plotly_white',
    height=450,
    hovermode='x unified',
    font=dict(size=12),
    showlegend=True,
    plot_bgcolor='rgba(240,240,240,0.5)'
)
```

### Color in Charts

```python
from config import COLORS

fig.add_trace(go.Scatter(
    x=data['x'],
    y=data['y'],
    line=dict(color=COLORS['primary_dark'], width=3),
    marker=dict(color=COLORS['accent_gold'], size=10)
))
```

---

## Part 5: Page Structure

### Adding a New Page

1. **Add to Navigation** (app.py):

```python
page = st.sidebar.radio(
    "📍 Choose Analysis:",
    ["🏠 Overview", "📈 5-Year Trend", ..., "🆕 New Page"],  # ← Add here
    key="main_nav"
)
```

2. **Add Page Content** (app.py):

```python
elif page == "🆕 New Page":
    render_section_header("🆕 Your New Analysis")
    
    # Add content here
    st.write("Your content")
    
    # Add charts, tables, etc.
```

### Page Template

```python
elif page == "📊 Your Page":
    render_section_header("📊 Section Title")
    
    # Content section 1
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Left Content")
        # Add content
    
    with col2:
        st.markdown("### Right Content")
        # Add content
    
    render_divider()
    
    # Content section 2
    render_subsection_header("Subsection Title")
    st.dataframe(your_data)
```

---

## Part 6: Sidebar Customization

### Add Metrics to Sidebar

```python
from styles import render_sidebar_metrics

sidebar_metrics = {
    'Metric 1': ('Value 1', 'Change 1'),
    'Metric 2': ('Value 2', 'Change 2'),
}

render_sidebar_metrics(sidebar_metrics)
```

### Add Alert to Sidebar

```python
from styles import render_sidebar_alert

render_sidebar_alert(
    "⚠️ Alert Title",
    "Alert content here",
    alert_type="warning"  # or "info", "success", "error"
)
```

---

## Part 7: Typography & Text

### Font Sizes

```python
# In markdown
st.markdown(f"<h1 style='font-size: 36px;'>Large Title</h1>", unsafe_allow_html=True)
st.markdown(f"<h2 style='font-size: 28px;'>Medium Title</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size: 14px;'>Body Text</p>", unsafe_allow_html=True)
```

### Text Formatting

```python
# Bold
st.markdown("**Bold Text**")

# Italic
st.markdown("*Italic Text*")

# Code
st.markdown("`code`")

# Combined
st.markdown("**Bold** and *italic* and `code`")
```

---

## Part 8: Tables & Data Display

### Gradient Styling

```python
df_styled = df.style.background_gradient(
    subset=['Column1', 'Column2'],
    cmap='RdYlGn'  # Red-Yellow-Green
)
st.dataframe(df_styled)
```

### Conditional Formatting

```python
def color_negative_red(val):
    return 'color: red' if val < 0 else 'color: green'

df_styled = df.style.applymap(
    color_negative_red,
    subset=['Column1']
)
st.dataframe(df_styled)
```

### Number Formatting

```python
df_styled = df.style.format({
    'Revenue': '{:,.2f}',
    'Percentage': '{:.1f}%',
    'Large Number': '{:,.0f}'
})
st.dataframe(df_styled)
```

---

## Part 9: Complete Example: Custom Dashboard

Here's a complete example of a customized page:

```python
elif page == "💼 Custom Analysis":
    # Header
    render_section_header("💼 Custom Business Analysis")
    
    # Key metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Revenue", "$1M", "+5%")
    with col2:
        st.metric("Growth", "15%", "-2pp")
    with col3:
        st.metric("Margin", "25%", "+1pp")
    
    render_divider()
    
    # Data table
    render_subsection_header("Performance Data")
    st.dataframe(your_data.style.format({
        'Revenue': '${:,.0f}',
        'Growth %': '{:.1f}%'
    }))
    
    render_divider()
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=['A', 'B', 'C'], y=[1, 2, 3]))
        fig1.update_layout(title="Chart 1", height=400)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=['A', 'B', 'C'], y=[1, 3, 2], 
                                  mode='lines+markers'))
        fig2.update_layout(title="Chart 2", height=400)
        st.plotly_chart(fig2, use_container_width=True)
    
    render_divider()
    
    # Insights
    render_subsection_header("Key Insights")
    render_success_box("✓ Positive finding")
    render_warning_box("⚠️ Risk area")
```

---

## Part 10: Best Practices

### ✅ DO

- Use config.py for all colors
- Use styles.py for consistent formatting
- Cache data with `@st.cache_data`
- Keep functions focused and small
- Document your customizations

### ❌ DON'T

- Hardcode colors in HTML
- Mix different styling approaches
- Reload data on every interaction
- Make massive functions
- Skip comments for complex logic

---

## Common Customization Tasks

### Change Dashboard Title

In `app.py`:
```python
render_main_title(
    "📊 Your New Title",
    "Your New Subtitle"
)
```

### Change Brand Name

In `config.py`:
```python
BRAND_NAME = "Your New Brand Name"
```

### Add Your Logo

In `app.py`:
```python
st.sidebar.image("path/to/logo.png", width=200)
```

### Change Footer

In `app.py`:
```python
render_footer(
    author="Your Name",
    brand="Your Brand",
    data_source="Your Data Source"
)
```

---

## Troubleshooting Customizations

### Issue: Colors not updating
**Solution**: Clear cache (`Ctrl+C` in terminal, restart app)

### Issue: Charts look distorted
**Solution**: Adjust height parameter: `height=450`

### Issue: Text overlapping
**Solution**: Use `st.divider()` or `spacing()` to add space

### Issue: Data not showing
**Solution**: Check column names match exactly (case-sensitive)

---

## Performance Tips

1. **Cache expensive operations**:
   ```python
   @st.cache_data
   def load_data():
       return expensive_operation()
   ```

2. **Use columns for layout**:
   ```python
   col1, col2 = st.columns(2)  # Side-by-side
   ```

3. **Lazy load charts** - only render when visible

4. **Minimize data size** - filter before passing to chart

---

## Version Control

When customizing, keep track of changes:

```bash
git add .
git commit -m "Customized colors and added new page"
git push
```

---

## Next Steps

1. Review `README.md` for full documentation
2. Explore the main `app.py` file
3. Modify `data.py` with your own data
4. Customize colors in `config.py`
5. Add new pages following the template
6. Deploy to Streamlit Cloud

---

**Happy customizing! 🎨**
