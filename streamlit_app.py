
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
        width='stretch'
    )
    
    render_divider()
    
    # Metric Cards
    render_subsection_header("💹 Performance Metrics (FY2025 YTD)")
    
    five_year = data['five_year']
    current_year = five_year.iloc[-1]
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Revenue Growth", f"{current_year['Revenue Growth (%)']:.1f}%", delta="YoY")
    with col2:
        st.metric("EBITDA Growth", f"{current_year['EBITDA Growth (%)']:.1f}%", delta="YoY")
    with col3:
        st.metric("PAT Growth", f"{current_year['PAT Growth (%)']:.1f}%", delta="YoY")
    with col4:
        st.metric("EBITDA Margin", f"{current_year['EBITDA Margin (%)']:.1f}%", delta="vs FY24")
    
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
    
    # Growth Divergence Analysis
    render_subsection_header("🔍 Growth Divergence: Revenue vs Profit")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Revenue Story")
        st.markdown("""
        - **FY21-FY24:** Consistent 10-15% growth
        - **FY25:** Sharp deceleration to 6.9%
        - **Trend:** Deteriorating
        - **Concern:** Sustainability question
        """)
    
    with col2:
        st.markdown("#### Profit Story")
        st.markdown("""
        - **CAGR:** 19.8% (vs Revenue 9.2%)
        - **Source:** Margin expansion (+150 bps)
        - **Driver:** Operational leverage
        - **Risk:** Not sustainable indefinitely
        """)
    
    with col3:
        st.markdown("#### Key Question")
        st.markdown("""
        ### Can Nifty 50 profit growth sustain if revenue continues to decelerate?
        
        **Answer:** NO
        
        - Margin expansion is finite
        - One-time cost benefits fading
        - Needs revenue recovery
        """)
    
    render_divider()
    
    # Margin Analysis
    render_subsection_header("📈 Margin Expansion Breakdown")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### EBITDA Margin Evolution")
        ebitda_margins = five_year['EBITDA Margin (%)'].values
        st.markdown(f"""
        - **FY2021:** {ebitda_margins[0]:.1f}%
        - **FY2022:** {ebitda_margins[1]:.1f}%
        - **FY2023:** {ebitda_margins[2]:.1f}%
        - **FY2024:** {ebitda_margins[3]:.1f}%
        - **FY2025:** {ebitda_margins[4]:.1f}%
        
        **Trend:** Plateauing (marginal improvement)
        """)
    
    with col2:
        st.markdown("#### PAT Margin Evolution")
        pat_margins = five_year['PAT Margin (%)'].values
        st.markdown(f"""
        - **FY2021:** {pat_margins[0]:.1f}%
        - **FY2022:** {pat_margins[1]:.1f}%
        - **FY2023:** {pat_margins[2]:.1f}%
        - **FY2024:** {pat_margins[3]:.1f}%
        - **FY2025:** {pat_margins[4]:.1f}%
        
        **Trend:** Near peak (limited upside)
        """)
    
    render_divider()
    
    # Sector Contribution
    render_subsection_header("🏢 Top Contributing Sectors")
    
    sectors = data['sector']
    top_sectors = sectors.head(5)
    
    sector_display = pd.DataFrame({
        'Sector': top_sectors['Sector'],
        'Weight in Nifty %': top_sectors['Weight in Nifty (%)'].round(1),
        'Revenue Growth %': top_sectors['Revenue Growth FY25 (%)'].round(1),
        'Status': top_sectors['Status']
    })
    
    display_styled_dataframe(
        sector_display,
        width='stretch'
    )
    
    render_divider()
    
    # Investment Recommendation
    render_subsection_header("💼 Investment Recommendation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_info_box(
            "**For Growth Investors:**\n\n"
            "⚠️ CAUTION\n\n"
            "• Nifty 50 earnings growth at peak\n"
            "• Revenue deceleration is concerning\n"
            "• Valuation may not justify growth\n"
            "• Better opportunities in high-growth stocks"
        )
    
    with col2:
        render_info_box(
            "**For Value Investors:**\n\n"
            "✓ MONITOR\n\n"
            "• Solid dividend yields likely\n"
            "• Defensive characteristics\n"
            "• Look for margin stabilization\n"
            "• Wait for revenue recovery"
        )
    
    render_divider()
    
    # Investment Takeaway
    render_info_box(
        "**Bottom Line**\n\n"
        "The Nifty 50 profit growth (19.8% CAGR) masks slowing revenue growth (9.2% CAGR). "
        "While margin expansion provided tailwinds through FY24, FY25 shows concerning revenue deceleration to 6.9%. "
        "**Key Risk:** Profit growth cannot sustain if revenue continues to decelerate. "
        "Investors should focus on revenue growth recovery and sector-specific opportunities rather than broad-based index investing at current levels."
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
    
    st.plotly_chart(fig, width='stretch')
    
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
    
    st.plotly_chart(fig2, width='stretch')
    
    render_divider()
    
    display_styled_dataframe(
        five_year,
        columns_to_style=['Revenue Growth (%)', 'EBITDA Growth (%)', 'PAT Growth (%)'],
        width='stretch',
        hide_index=True
    )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 2: QUARTERLY DEEP-DIVE
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[2]:
    render_section_header("📊 FY2025 Quarterly Deep-Dive Analysis")
    
    st.markdown("""
    **Comprehensive Annual vs Quarterly Performance Analysis**  
    Analyzing FY2025 performance through both annual and quarterly lens
    """)
    
    render_divider()
    
    # Get data
    five_year = data['five_year']
    quarterly = data['quarterly']
    
    # ANNUAL PERFORMANCE (Last row of 5-year data)
    render_subsection_header("📈 Annual Performance (FY2025 YTD)")
    
    annual_row = five_year.iloc[-1]
    annual_cols = st.columns(4)
    with annual_cols[0]:
        st.metric("Revenue Growth", f"{annual_row['Revenue Growth (%)']:.1f}%", delta="YoY")
    with annual_cols[1]:
        st.metric("EBITDA Growth", f"{annual_row['EBITDA Growth (%)']:.1f}%", delta="YoY")
    with annual_cols[2]:
        st.metric("PAT Growth", f"{annual_row['PAT Growth (%)']:.1f}%", delta="YoY")
    with annual_cols[3]:
        st.metric("EBITDA Margin", f"{annual_row['EBITDA Margin (%)']:.1f}%", delta="vs FY24")
    
    render_divider()
    
    # QUARTERLY PERFORMANCE
    render_subsection_header("📊 Quarterly Breakdown (FY2025)")
    
    display_styled_dataframe(
        quarterly,
        columns_to_style=['Revenue Growth (%)', 'EBITDA Growth (%)', 'PAT Growth (%)'],
        width='stretch',
        hide_index=True
    )
    
    render_divider()
    
    # QUARTERLY vs ANNUAL COMPARISON
    render_subsection_header("🔍 Quarterly vs Annual Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_info_box(
            "**Quarterly Trend**\n\n"
            "• Q1 FY25: Revenue 9.6% | PAT 0.8%\n"
            "• Q2 FY25: Revenue 6.6% | PAT -1.0%\n"
            "• Q3 FY25: Revenue 4.5% | PAT 9.5%\n\n"
            "**Observation:** Revenue declining QoQ while profit recovery in Q3"
        )
    
    with col2:
        render_warning_box(
            "**Key Insights**\n\n"
            "• Annual revenue growth (6.9%) lower than prior years\n"
            "• Q2 showed negative PAT growth (-1.0%)\n"
            "• Q3 recovery driven by margin expansion\n"
            "• Divergence between revenue and profit trends"
        )
    
    render_divider()
    
    # ANNUAL TREND CHART
    render_subsection_header("📈 Annual Revenue Growth Trend (FY2021-2025)")
    
    fig_annual = go.Figure()
    
    annual_x = list(range(len(five_year)))
    annual_labels = five_year['Fiscal Year'].tolist()
    
    # Annual trend line
    fig_annual.add_trace(go.Scatter(
        x=annual_x,
        y=five_year['Revenue Growth (%)'],
        mode='lines+markers',
        name='Annual Revenue Growth',
        line=dict(color=COLORS['chart_blue'], width=4),
        marker=dict(size=14),
        fill='tozeroy',
        text=annual_labels,
        hovertemplate='<b>%{text}</b><br>Revenue Growth: %{y:.1f}%<extra></extra>'
    ))
    
    fig_annual.update_layout(
        title="Annual Revenue Growth Trajectory",
        xaxis_title="Fiscal Year",
        yaxis_title="Revenue Growth Rate (%)",
        xaxis=dict(
            ticktext=annual_labels,
            tickvals=annual_x
        ),
        template='plotly_white',
        height=450,
        showlegend=False
    )
    
    st.plotly_chart(fig_annual, use_container_width=True)
    
    render_divider()
    
    # QUARTERLY TREND CHART
    render_subsection_header("📊 Quarterly Revenue Growth Trend (FY2025)")
    
    fig_quarterly = go.Figure()
    
    quarterly_x = list(range(len(quarterly)))
    q_labels = quarterly['Quarter'].tolist()
    
    # Quarterly trend
    fig_quarterly.add_trace(go.Scatter(
        x=quarterly_x,
        y=quarterly['Revenue Growth (%)'],
        mode='lines+markers',
        name='Quarterly Revenue Growth',
        line=dict(color=COLORS['accent_red'], width=4),
        marker=dict(size=14, symbol='diamond'),
        fill='tozeroy',
        fillcolor='rgba(255, 0, 0, 0.2)',
        text=q_labels,
        hovertemplate='<b>%{text}</b><br>Revenue Growth: %{y:.1f}%<extra></extra>'
    ))
    
    fig_quarterly.update_layout(
        title="Quarterly Revenue Growth Deceleration",
        xaxis_title="Quarter (FY2025)",
        yaxis_title="Revenue Growth Rate (%)",
        xaxis=dict(
            ticktext=q_labels,
            tickvals=quarterly_x
        ),
        template='plotly_white',
        height=450,
        showlegend=False
    )
    
    st.plotly_chart(fig_quarterly, use_container_width=True)
    
    render_divider()
    
    render_info_box(
        "**Deep-Dive Takeaway**\n\n"
        "FY2025 shows concerning revenue deceleration when analyzed quarterly, suggesting temporary tailwinds may have faded. "
        "However, profit recovery in Q3 indicates management's ability to defend margins through cost management. "
        "The key question: Is Q3 recovery sustainable, or is it driven by one-time factors?"
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
        width='stretch',
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
        width='stretch',
        hide_index=True
    )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 5: SCENARIOS
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[5]:
    render_section_header("🎯 Investment Scenarios - Detailed Analysis")
    
    st.markdown("""
    **Select a scenario below to view detailed analysis including:**
    - Earnings projections (FY2025-2027)
    - P/E multiple assumptions
    - Nifty 50 target levels
    - Probability-weighted returns
    """)
    
    render_divider()
    
    # Get scenarios data
    scenarios_data = data['scenarios']
    nifty_levels = data['nifty_levels']
    
    # Radio button to select scenario
    scenario_names = list(scenarios_data.keys())
    selected_scenario = st.radio(
        "📍 Choose Investment Scenario:",
        scenario_names,
        index=0,
        key="scenario_selector"
    )
    
    render_divider()
    
    # Get selected scenario data
    scenario_info = scenarios_data[selected_scenario]
    nifty_targets = nifty_levels[selected_scenario]
    
    # Display selected scenario
    render_subsection_header(f"📊 {selected_scenario}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        **Scenario Description:**
        
        {scenario_info['description']}
        
        **Probability:** {scenario_info['probability']*100:.0f}%
        """)
    
    with col2:
        # Color indicator with HTML rendering
        st.markdown(f"""
        **Scenario Type & Color:**
        """)
        
        # Display colored indicator
        color = scenario_info['color']
        st.markdown(f"<p style='font-size: 24px; color: {color};'>● {selected_scenario}</p>", unsafe_allow_html=True)
        
        st.markdown(f"""
        **Key Characteristics:**
        
        {scenario_info['description']}
        """)
    
    render_divider()
    
    # Earnings Projections
    render_subsection_header("💰 Earnings Projections (FY2025-2027)")
    
    earnings_col1, earnings_col2, earnings_col3 = st.columns(3)
    
    with earnings_col1:
        st.metric("FY2025 Earnings", f"₹{scenario_info['fy25_earnings']:.1f}", delta="Growth")
    with earnings_col2:
        st.metric("FY2026 Earnings", f"₹{scenario_info['fy26_earnings']:.1f}", delta="CAGR")
    with earnings_col3:
        st.metric("FY2027 Earnings", f"₹{scenario_info['fy27_earnings']:.1f}", delta="Projection")
    
    render_divider()
    
    # P/E Multiples
    render_subsection_header("📈 P/E Multiple Assumptions")
    
    pe_col1, pe_col2, pe_col3 = st.columns(3)
    
    with pe_col1:
        st.metric("FY2025 P/E", f"{scenario_info['fy25_pe']:.1f}x", delta="Valuation")
    with pe_col2:
        st.metric("FY2026 P/E", f"{scenario_info['fy26_pe']:.1f}x", delta="Normalized")
    with pe_col3:
        st.metric("FY2027 P/E", f"{scenario_info['fy27_pe']:.1f}x", delta="Terminal")
    
    render_divider()
    
    # Nifty 50 Target Levels
    render_subsection_header("🎯 Nifty 50 Target Levels")
    
    target_col1, target_col2, target_col3 = st.columns(3)
    
    with target_col1:
        st.metric("FY2025 Target", f"{nifty_targets[0]:.0f}", delta="Near-term")
    with target_col2:
        st.metric("FY2026 Target", f"{nifty_targets[1]:.0f}", delta="Medium-term")
    with target_col3:
        st.metric("FY2027 Target", f"{nifty_targets[2]:.0f}", delta="Long-term")
    
    render_divider()
    
    # Scenario Analysis Table
    render_subsection_header("📊 Scenario Comparison Matrix")
    
    # Create comparison dataframe
    comparison_df = pd.DataFrame({
        'Metric': ['Probability', 'FY25 Earnings', 'FY26 Earnings', 'FY27 Earnings', 
                   'FY25 P/E', 'FY26 P/E', 'FY27 P/E',
                   'FY25 Target', 'FY26 Target', 'FY27 Target'],
        'Base Case (50%)': [
            f"{scenarios_data['Base Case (50%)']['probability']*100:.0f}%",
            f"₹{scenarios_data['Base Case (50%)']['fy25_earnings']:.1f}",
            f"₹{scenarios_data['Base Case (50%)']['fy26_earnings']:.1f}",
            f"₹{scenarios_data['Base Case (50%)']['fy27_earnings']:.1f}",
            f"{scenarios_data['Base Case (50%)']['fy25_pe']:.1f}x",
            f"{scenarios_data['Base Case (50%)']['fy26_pe']:.1f}x",
            f"{scenarios_data['Base Case (50%)']['fy27_pe']:.1f}x",
            f"{nifty_levels['Base Case (50%)'][0]:.0f}",
            f"{nifty_levels['Base Case (50%)'][1]:.0f}",
            f"{nifty_levels['Base Case (50%)'][2]:.0f}"
        ],
        'Bear Case (25%)': [
            f"{scenarios_data['Bear Case (25%)']['probability']*100:.0f}%",
            f"₹{scenarios_data['Bear Case (25%)']['fy25_earnings']:.1f}",
            f"₹{scenarios_data['Bear Case (25%)']['fy26_earnings']:.1f}",
            f"₹{scenarios_data['Bear Case (25%)']['fy27_earnings']:.1f}",
            f"{scenarios_data['Bear Case (25%)']['fy25_pe']:.1f}x",
            f"{scenarios_data['Bear Case (25%)']['fy26_pe']:.1f}x",
            f"{scenarios_data['Bear Case (25%)']['fy27_pe']:.1f}x",
            f"{nifty_levels['Bear Case (25%)'][0]:.0f}",
            f"{nifty_levels['Bear Case (25%)'][1]:.0f}",
            f"{nifty_levels['Bear Case (25%)'][2]:.0f}"
        ],
        'Bull Case (25%)': [
            f"{scenarios_data['Bull Case (25%)']['probability']*100:.0f}%",
            f"₹{scenarios_data['Bull Case (25%)']['fy25_earnings']:.1f}",
            f"₹{scenarios_data['Bull Case (25%)']['fy26_earnings']:.1f}",
            f"₹{scenarios_data['Bull Case (25%)']['fy27_earnings']:.1f}",
            f"{scenarios_data['Bull Case (25%)']['fy25_pe']:.1f}x",
            f"{scenarios_data['Bull Case (25%)']['fy26_pe']:.1f}x",
            f"{scenarios_data['Bull Case (25%)']['fy27_pe']:.1f}x",
            f"{nifty_levels['Bull Case (25%)'][0]:.0f}",
            f"{nifty_levels['Bull Case (25%)'][1]:.0f}",
            f"{nifty_levels['Bull Case (25%)'][2]:.0f}"
        ]
    })
    
    display_styled_dataframe(
        comparison_df,
        width='stretch',
        hide_index=True
    )
    
    render_divider()
    
    # Investment Perspective
    if selected_scenario == 'Base Case (50%)':
        render_success_box(
            "**Base Case (Most Likely - 50% Probability)**\n\n"
            "Margin resilience with slow revenue growth. Earnings grow from ₹5.5 (FY25) to ₹12.5 (FY27). "
            "P/E multiple compresses from 25x to 24x, limiting re-rating. Nifty target ranges from 56,700 to 67,900. "
            "This is the consensus scenario with moderate upside."
        )
    elif selected_scenario == 'Bear Case (25%)':
        render_warning_box(
            "**Bear Case (Stress - 25% Probability)**\n\n"
            "Margin compression due to input cost spike. Earnings growth severely impacted: ₹2.0 → ₹7.5. "
            "P/E multiple contracts from 23x to 21.5x. Nifty downside risk to 50,400-53,200. "
            "Triggered by commodities rally or demand shock."
        )
    else:
        render_info_box(
            "**Bull Case (Optimistic - 25% Probability)**\n\n"
            "Revenue recovery accelerates with margin stability. Strong earnings growth: ₹9.0 → ₹15.5. "
            "P/E multiple expands from 25.5x to 26.5x as confidence returns. Nifty upside to 59,700-81,700. "
            "Requires revenue inflection + operational efficiency."
        )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 6: DATA EXPLORER
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[6]:
    render_section_header("📋 Data Explorer")
    
    st.markdown("**All Datasets**")
    
    tab1, tab2, tab3, tab4 = st.tabs(["5-Year", "Quarterly", "Sectors", "Downgrades"])
    
    with tab1:
        display_styled_dataframe(data['five_year'], width='stretch', hide_index=True)
    
    with tab2:
        display_styled_dataframe(data['quarterly'], width='stretch', hide_index=True)
    
    with tab3:
        display_styled_dataframe(data['sector'], width='stretch', hide_index=True)
    
    with tab4:
        display_styled_dataframe(data['downgrades'], width='stretch', hide_index=True)

# ═══════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("---")
render_footer(AUTHOR, BRAND_NAME, "NSE, RBI, BSE, MCA, SEBI | Research: Business Standard, Economic Times, Brokerages")
