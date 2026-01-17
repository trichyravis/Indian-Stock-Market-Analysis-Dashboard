
"""
Indian Stock Market Analysis Dashboard
Analysis of Nifty 50 Growth: Revenue Expansion vs Margin Re-Rating
Version 2.4.0 - Restored Original State (7 Pages)
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

from config import COLORS, AUTHOR, BRAND_NAME, EXPERIENCE, LOCATION, YEAR, PAGES
from data import generate_data
from styles import (
    get_custom_css, display_styled_dataframe,
    render_section_header, render_subsection_header, render_divider,
    render_info_box, render_warning_box, render_success_box,
    render_footer
)

# ═══════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="Indian Stock Market Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# SIDEBAR & NAVIGATION
# ═══════════════════════════════════════════════════════════════════════════

st.sidebar.markdown(f"# 📊 {BRAND_NAME}")
st.sidebar.markdown("---")
st.sidebar.markdown(f"**Prof. V. Ravichandran**")
st.sidebar.markdown(f"*{EXPERIENCE}*")
st.sidebar.markdown("---")

# Only show first 7 pages (exclude data sources)
pages_list = PAGES[:7]

page = st.sidebar.radio(
    "📍 Choose Analysis:",
    pages_list,
    key="main_nav"
)

st.sidebar.markdown("---")
st.sidebar.markdown(f"📍 {LOCATION} | {YEAR}")

# ═══════════════════════════════════════════════════════════════════════════
# LOAD DATA
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data
def load_dashboard_data():
    return generate_data()

data = load_dashboard_data()

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 0: OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════

if page == PAGES[0]:
    render_section_header("📈 Nifty 50 Analysis: Growth Drivers & Sustainability")
    
    st.markdown("""
    **Analysis Period:** FY2021 - FY2025 YTD  
    **Focus:** Is growth driven by revenue expansion or margin re-rating?
    """)
    
    render_divider()
    
    # Key Metrics
    render_subsection_header("📊 Key Metrics Summary")
    
    metrics_data = {
        'Metric': ['Revenue CAGR (FY21-25)', 'Profit CAGR (FY21-25)', 'EBITDA Margin (FY25)', 'PAT Margin (FY25)'],
        'Value': ['9.2%', '19.8%', '33.0%', '10.5%']
    }
    
    display_styled_dataframe(
        pd.DataFrame(metrics_data),
        columns_to_style=['Value'],
        use_container_width=True
    )
    
    render_divider()
    
    # Key Insights
    render_subsection_header("📌 Key Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_success_box(
            "**FY2021-2024: Healthy Growth**\n\n"
            "✅ Revenue expanding (+10.5% avg)\n"
            "✅ Margins improving (+50 bps)\n"
            "✅ Both drivers working\n"
            "✅ Sustainable model"
        )
    
    with col2:
        render_warning_box(
            "**FY2025: Concerning Shift**\n\n"
            "⚠️ Revenue decelerating (6.9%)\n"
            "⚠️ Margins propping profits\n"
            "⚠️ One-time tailwinds fading\n"
            "❌ Unsustainable"
        )
    
    render_divider()
    
    # Investment Takeaway
    render_info_box(
        "**Investment Perspective**\n\n"
        "The Nifty 50 profit growth (19.8% CAGR) masks slowing revenue growth (9.2% CAGR). "
        "While margin expansion provided tailwinds through FY24, FY25 shows concerning revenue deceleration. "
        "Investors should focus on revenue growth sustainability rather than margin-driven earnings growth."
    )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 1: 5-YEAR TREND
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[1]:
    render_section_header("📈 5-Year Trend Analysis")
    
    render_subsection_header("💹 5-Year Performance")
    
    five_year = data['five_year']
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=five_year['Fiscal Year'],
        y=five_year['Revenue Growth (%)'],
        mode='lines+markers',
        name='Revenue Growth',
        line=dict(color=COLORS['chart_blue'], width=3),
        marker=dict(size=10)
    ))
    
    fig.add_trace(go.Scatter(
        x=five_year['Fiscal Year'],
        y=five_year['PAT Growth (%)'],
        mode='lines+markers',
        name='Profit Growth',
        line=dict(color=COLORS['accent_red'], width=3),
        marker=dict(size=10)
    ))
    
    fig.update_layout(
        title="Revenue vs Profit Growth Trends",
        xaxis_title="Fiscal Year",
        yaxis_title="Growth Rate (%)",
        template='plotly_white',
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    render_divider()
    
    render_subsection_header("📊 Margin Trends")
    
    fig2 = go.Figure()
    
    fig2.add_trace(go.Scatter(
        x=five_year['Fiscal Year'],
        y=five_year['EBITDA Margin (%)'],
        mode='lines+markers',
        name='EBITDA Margin',
        line=dict(color=COLORS['accent_gold'], width=3),
        marker=dict(size=10)
    ))
    
    fig2.add_trace(go.Scatter(
        x=five_year['Fiscal Year'],
        y=five_year['PAT Margin (%)'],
        mode='lines+markers',
        name='PAT Margin',
        line=dict(color=COLORS['accent_red'], width=3),
        marker=dict(size=10)
    ))
    
    fig2.update_layout(
        title="Margin Trends",
        xaxis_title="Fiscal Year",
        yaxis_title="Margin (%)",
        template='plotly_white',
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    render_divider()
    
    display_styled_dataframe(
        five_year,
        columns_to_style=['Revenue Growth (%)', 'EBITDA Growth (%)', 'PAT Growth (%)'],
        use_container_width=True,
        hide_index=True
    )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 2: QUARTERLY DEEP-DIVE
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[2]:
    render_section_header("📊 FY2025 Quarterly Analysis")
    
    quarterly = data['quarterly']
    display_styled_dataframe(
        quarterly,
        columns_to_style=['Revenue Growth (%)', 'EBITDA Growth (%)', 'PAT Growth (%)'],
        use_container_width=True,
        hide_index=True
    )
    
    render_divider()
    
    render_info_box(
        "**Quarterly Insights**\n\n"
        "FY25 shows declining revenue growth quarter-on-quarter, while profit growth remains supported by margin expansion. "
        "Q3 data should clarify if revenue stabilizes or continues decelerating."
    )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 3: SECTOR ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[3]:
    render_section_header("🏦 Sector Performance Analysis")
    
    sectors = data['sector']
    display_styled_dataframe(
        sectors,
        columns_to_style=['Contribution (%)', 'Growth (%)'],
        use_container_width=True,
        hide_index=True
    )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 4: EARNINGS DOWNGRADES
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[4]:
    render_section_header("📉 6-Month Earnings Revision Trend")
    
    downgrades = data['downgrades']
    display_styled_dataframe(
        downgrades,
        columns_to_style=['Direction (%)'],
        use_container_width=True,
        hide_index=True
    )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 5: SCENARIOS
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[5]:
    render_section_header("🎯 Investment Scenarios")
    
    scenarios = {
        'Base Case (50%)': {'description': 'Margin Resilience', 'return': '+10% p.a.'},
        'Bear Case (25%)': {'description': 'Margin Compression', 'return': '-0.2% p.a.'},
        'Bull Case (25%)': {'description': 'Revenue Recovery', 'return': '+18% p.a.'}
    }
    
    cols = st.columns(3)
    
    for idx, (scenario, details) in enumerate(scenarios.items()):
        with cols[idx]:
            render_info_box(
                f"**{scenario}**\n\n"
                f"*{details['description']}*\n\n"
                f"Expected Return: {details['return']}"
            )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 6: DATA EXPLORER
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[6]:
    render_section_header("📋 Data Explorer")
    
    st.markdown("**All Datasets**")
    
    tab1, tab2, tab3, tab4 = st.tabs(["5-Year", "Quarterly", "Sectors", "Downgrades"])
    
    with tab1:
        display_styled_dataframe(data['five_year'], use_container_width=True, hide_index=True)
    
    with tab2:
        display_styled_dataframe(data['quarterly'], use_container_width=True, hide_index=True)
    
    with tab3:
        display_styled_dataframe(data['sector'], use_container_width=True, hide_index=True)
    
    with tab4:
        display_styled_dataframe(data['downgrades'], use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("---")
render_footer(AUTHOR, BRAND_NAME, "NSE, RBI, BSE, MCA, SEBI | Research: Business Standard, Economic Times, Brokerages")
