
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from config import *
from styles import *
# Note: Ensure data.py exists with required functions

# Initialize
st.set_page_config(page_title=MESSAGES['header_title'], layout="wide")
apply_custom_css()

# Sidebar
st.sidebar.title(f"🏔️ {BRAND_NAME}")
page = st.sidebar.radio("📍 Choose Analysis:", PAGES)

# 🏠 OVERVIEW PAGE
if page == PAGES[0]:
    render_main_title(MESSAGES['header_title'], MESSAGES['header_subtitle'])
    
    col1, col2 = st.columns(2)
    with col1:
        render_success_box("""
        **FY2021-2024: Healthy Growth**
        * ✅ Revenue expanding (+10.5% avg)
        * ✅ Margins improving (+50 bps)
        * ✅ Sustainable model
        """)
    with col2:
        render_warning_box("""
        **FY2025: Concerning Shift**
        * ⚠️ Revenue decelerating (6.9%)
        * ⚠️ Margins propping profits
        * ❌ Unsustainable divergence
        """)

# 📚 DATA SOURCES PAGE
elif page == PAGES[7]:
    render_section_header("📚 Data Sources & References")
    
    col1, col2 = st.columns(2)
    with col1:
        render_info_box("""
        **🔍 Data Validation Process**
        1. **Collection**: Gathering from NSE/RBI
        2. **Verification**: Cross-source audit
        3. **Normalization**: Format standardizing
        """)
    
    render_warning_box("""
    **📌 Important Disclaimer**
    * Data aggregated from public sources.
    * No guarantee of absolute accuracy.
    * **Not financial advice.**
    """)

render_footer(AUTHOR, BRAND_NAME, "NSE, RBI, BSE, MCA")
