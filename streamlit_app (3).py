import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="Indian Market Analysis: Revenue vs Margins",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════════════════
# CUSTOM CSS
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .header-style {
        color: #003366;
        font-weight: bold;
        font-size: 24px;
        margin: 20px 0 10px 0;
    }
    .subheader-style {
        color: #004d80;
        font-weight: bold;
        font-size: 18px;
        margin: 15px 0 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# DATA PREPARATION
# ═══════════════════════════════════════════════════════════════════════════

# Main 5-Year Data
five_year_data = pd.DataFrame({
    'Fiscal Year': ['FY2021', 'FY2022', 'FY2023', 'FY2024', 'FY2025 YTD'],
    'Revenue Growth (%)': [10.5, 15.4, 13.8, 10.7, 6.9],
    'EBITDA Growth (%)': [11.2, 22.8, 18.5, 14.3, 2.6],
    'PAT Growth (%)': [8.3, 25.7, 22.1, 16.8, 4.6],
    'EBITDA Margin (%)': [32.1, 33.5, 33.2, 33.0, 33.1],
    'PAT Margin (%)': [9.8, 10.4, 10.6, 10.5, 10.7]
})

# Quarterly Data for Q3FY25
quarterly_data = pd.DataFrame({
    'Quarter': ['Q1FY25', 'Q2FY25', 'Q3FY25'],
    'Revenue Growth (%)': [9.6, 6.6, 4.5],
    'EBITDA Growth (%)': [9.4, 1.3, 6.9],
    'PAT Growth (%)': [0.8, -1.0, 9.5]
})

# Sector Performance
sector_data = pd.DataFrame({
    'Sector': ['Financials', 'Energy', 'IT', 'Industrials', 'Materials', 
               'Consumer Disc.', 'Healthcare', 'Consumer Staples', 'Utilities', 'Telecom'],
    'Revenue Growth FY25 (%)': [12.3, 1.4, 7.0, 10.6, 1.7, 10.5, 7.6, 10.6, 7.5, 8.0],
    'Profit Growth FY25 (%)': [17.3, -35.4, 8.7, 25.7, -1.4, 6.6, 32.9, 6.1, -6.9, 95.9],
    'Weight in Nifty (%)': [35, 30, 9, 5, 11, 9, 3, 3, 3, 2],
    'Status': ['🟡 SLOWING', '🔴 CRISIS', '🟢 STABILIZING', '🟢 STRONG', 
               '⚠️ MIXED', '⚠️ WEAKENING', '🟢 STRONG', '⚠️ MIXED', '⚠️ DECLINING', '🟢 EXCEPTIONAL']
})

# Earnings Downgrade Trajectory
downgrade_data = pd.DataFrame({
    'Date': ['Sep 30, 2024', 'Oct 31, 2024', 'Nov 30, 2024', 'Dec 31, 2024', 
             'Jan 31, 2025', 'Feb 21, 2025'],
    'FY25 Profit Growth (%)': [9.8, 8.2, 5.8, 3.2, 4.9, 3.2]
})

# Scenario Data
scenarios = {
    'Base Case (50%)': {
        'description': 'Margin Resilience, Slow Revenue',
        'fy25_earnings': 5.5,
        'fy26_earnings': 11.0,
        'fy27_earnings': 12.5,
        'fy25_pe': 25.0,
        'fy26_pe': 24.5,
        'fy27_pe': 24.0,
        'color': '#FFA500'
    },
    'Bear Case (25%)': {
        'description': 'Margin Compression, Input Cost Spike',
        'fy25_earnings': 2.0,
        'fy26_earnings': 5.0,
        'fy27_earnings': 7.5,
        'fy25_pe': 23.0,
        'fy26_pe': 22.0,
        'fy27_pe': 21.5,
        'color': '#FF0000'
    },
    'Bull Case (25%)': {
        'description': 'Revenue Recovery + Margin Stability',
        'fy25_earnings': 9.0,
        'fy26_earnings': 14.0,
        'fy27_earnings': 15.5,
        'fy25_pe': 25.5,
        'fy26_pe': 26.0,
        'fy27_pe': 26.5,
        'color': '#00AA00'
    }
}

# Calculate Nifty levels for scenarios
base_eps_fy24 = 920
nifty_levels = {}
for scenario, data in scenarios.items():
    fy25_nifty = (base_eps_fy24 * (1 + data['fy25_earnings']/100)) * data['fy25_pe']
    fy26_nifty = fy25_nifty * (1 + data['fy26_earnings']/100) * (data['fy26_pe']/data['fy25_pe'])
    fy27_nifty = fy26_nifty * (1 + data['fy27_earnings']/100) * (data['fy27_pe']/data['fy26_pe'])
    nifty_levels[scenario] = [fy25_nifty/1000, fy26_nifty/1000, fy27_nifty/1000]

# ═══════════════════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("<h1 style='text-align: center; color: #003366;'>📊 Indian Stock Market Analysis</h1>", 
            unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #004d80;'>Is Growth Driven by Revenue Expansion or Margin Re-Rating?</h3>", 
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Analysis of Nifty 50 (FY2021-FY2025) | Data: NSE, RBI, Business Standard</p>", 
            unsafe_allow_html=True)

st.divider()

# ═══════════════════════════════════════════════════════════════════════════
# SIDEBAR NAVIGATION
# ═══════════════════════════════════════════════════════════════════════════

st.sidebar.markdown("## 📍 Navigation")
page = st.sidebar.radio(
    "Choose Analysis:",
    ["🏠 Overview", "📈 5-Year Trend", "📊 Quarterly Deep-Dive", 
     "🏦 Sector Analysis", "📉 Earnings Downgrades", "🎯 Scenarios", 
     "📋 Data Explorer"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📌 Key Metrics")
col1, col2 = st.sidebar.columns(2)
with col1:
    st.metric("Revenue CAGR", "11.5%", "-5.0 pp")
    st.metric("Current Rev Growth", "4.5%", "Q3FY25")
with col2:
    st.metric("Profit CAGR", "14.7%", "+3.2 pp")
    st.metric("Current PAT Growth", "9.5%", "Q3FY25")

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚠️ Valuation Alert")
st.sidebar.write("""
- **Current P/E:** 25x
- **Fair Value P/E:** 10-12x
- **Gap:** -50% to -60%
""")

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════

if page == "🏠 Overview":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 💰 Revenue Story")
        st.write("""
        - **5-Yr CAGR:** 11.5%
        - **Current (Q3):** 4.5%
        - **Trend:** ↘️ Decelerating
        - **Status:** 16-quarter LOW
        """)
    
    with col2:
        st.markdown("### 📊 Profit Story")
        st.write("""
        - **5-Yr CAGR:** 14.7%
        - **Current (Q3):** 9.5%
        - **Trend:** ↑ Margin Support
        - **Status:** Unsustainable
        """)
    
    with col3:
        st.markdown("### ⚖️ The Divergence")
        st.write("""
        - **Profit 53% faster** than revenue
        - **Driven by:** Margin expansion
        - **Risk Level:** 🔴 HIGH
        - **Sustainability:** ❌ Limited
        """)
    
    st.divider()
    
    st.markdown("### 🔍 The Core Problem")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **FY2021-2024:** Healthy Growth
        - Revenue growing: ✅
        - Margins expanding: ✅
        - Both working together: ✅
        - Sustainable: ✅
        """)
    
    with col2:
        st.warning("""
        **FY2025 NOW:** Concerning Shift
        - Revenue collapsing: ⚠️
        - Margins supporting profits: ⚠️
        - Cost cuts, commodity tailwinds, tax benefits
        - Sustainable: ❌ NO
        """)
    
    st.divider()
    
    st.markdown("### 📈 5-Year Overview Chart")
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=five_year_data['Fiscal Year'],
        y=five_year_data['Revenue Growth (%)'],
        mode='lines+markers',
        name='Revenue Growth',
        line=dict(color='#0066CC', width=3),
        marker=dict(size=10)
    ))
    
    fig.add_trace(go.Scatter(
        x=five_year_data['Fiscal Year'],
        y=five_year_data['PAT Growth (%)'],
        mode='lines+markers',
        name='Profit Growth (PAT)',
        line=dict(color='#CC0000', width=3),
        marker=dict(size=10)
    ))
    
    fig.update_layout(
        title="Revenue vs Profit Growth (5-Year Divergence)",
        xaxis_title="Fiscal Year",
        yaxis_title="Growth Rate (%)",
        hovermode='x unified',
        template='plotly_white',
        height=400,
        font=dict(size=11)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    st.markdown("### 🎯 Three Scenarios (Next 3 Years)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("""
        **Base Case (50%)**
        
        Margin Resilience Persists
        - Earnings CAGR: 9.7%
        - Nifty Return: +10% p.a.
        - Target: 26,000-27,000
        - Verdict: Fair, no upside
        """)
    
    with col2:
        st.error("""
        **Bear Case (25%)**
        
        Margin Compression Hits
        - Earnings CAGR: 4.8%
        - Nifty Return: -0.2% p.a.
        - Target: 20,000-21,000
        - Verdict: Negative, risky
        """)
    
    with col3:
        st.success("""
        **Bull Case (25%)**
        
        Revenue Reaccelerates
        - Earnings CAGR: 12.8%
        - Nifty Return: +14.5% p.a.
        - Target: 33,000-35,000
        - Verdict: Strong, needs catalyst
        """)

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: 5-YEAR TREND
# ═══════════════════════════════════════════════════════════════════════════

elif page == "📈 5-Year Trend":
    st.markdown("### 📊 Nifty 50 - 5-Year Performance (FY2021-FY2025)")
    
    # Data Table
    st.dataframe(
        five_year_data.style.background_gradient(
            subset=['Revenue Growth (%)', 'EBITDA Growth (%)', 'PAT Growth (%)'],
            cmap='RdYlGn'
        ),
        use_container_width=True,
        hide_index=True
    )
    
    st.divider()
    
    # Growth Rates Comparison
    fig1 = go.Figure()
    
    fig1.add_trace(go.Bar(
        x=five_year_data['Fiscal Year'],
        y=five_year_data['Revenue Growth (%)'],
        name='Revenue Growth',
        marker_color='#0066CC'
    ))
    
    fig1.add_trace(go.Bar(
        x=five_year_data['Fiscal Year'],
        y=five_year_data['EBITDA Growth (%)'],
        name='EBITDA Growth',
        marker_color='#00AA00'
    ))
    
    fig1.add_trace(go.Bar(
        x=five_year_data['Fiscal Year'],
        y=five_year_data['PAT Growth (%)'],
        name='PAT Growth',
        marker_color='#CC0000'
    ))
    
    fig1.update_layout(
        title="Growth Rates Comparison (YoY)",
        barmode='group',
        xaxis_title="Fiscal Year",
        yaxis_title="Growth Rate (%)",
        template='plotly_white',
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig1, use_container_width=True)
    
    st.divider()
    
    # Margin Trends
    fig2 = go.Figure()
    
    fig2.add_trace(go.Scatter(
        x=five_year_data['Fiscal Year'],
        y=five_year_data['EBITDA Margin (%)'],
        mode='lines+markers',
        name='EBITDA Margin',
        line=dict(color='#00AA00', width=3),
        marker=dict(size=10)
    ))
    
    fig2.add_trace(go.Scatter(
        x=five_year_data['Fiscal Year'],
        y=five_year_data['PAT Margin (%)'],
        mode='lines+markers',
        name='PAT Margin',
        line=dict(color='#CC0000', width=3),
        marker=dict(size=10)
    ))
    
    fig2.update_layout(
        title="Margin Trends Over 5 Years",
        xaxis_title="Fiscal Year",
        yaxis_title="Margin (%)",
        template='plotly_white',
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    st.divider()
    
    st.markdown("### 📌 Key Insights")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **The Story:**
        - FY21-FY23: Healthy growth (both revenue & profit expanding)
        - FY24: Peak profitability, first signs of weakness
        - FY25: Revenue collapse, margin engineering begins
        
        **The Concern:**
        - Profit growing 53% faster than revenue over 5 years
        - Margins used as "prop" when revenue slows
        - Limited margin expansion left before hits ceiling
        """)
    
    with col2:
        st.write("""
        **Breakdown:**
        - Revenue CAGR: 11.5%
        - EBITDA CAGR: 13.8% (+330 bps)
        - PAT CAGR: 14.7% (+320 bps)
        
        **Current Status:**
        - EBITDA Margin stable at 33%
        - PAT Margin stable at 10.7%
        - But revenue growth failing (4.5%)
        """)

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: QUARTERLY DEEP-DIVE
# ═══════════════════════════════════════════════════════════════════════════

elif page == "📊 Quarterly Deep-Dive":
    st.markdown("### 📊 Q3FY25 & Recent Quarterly Trends")
    
    st.dataframe(
        quarterly_data.style.background_gradient(
            subset=['Revenue Growth (%)', 'EBITDA Growth (%)', 'PAT Growth (%)'],
            cmap='RdYlGn'
        ),
        use_container_width=True,
        hide_index=True
    )
    
    st.divider()
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=quarterly_data['Quarter'],
        y=quarterly_data['Revenue Growth (%)'],
        mode='lines+markers',
        name='Revenue Growth',
        line=dict(color='#0066CC', width=3),
        marker=dict(size=12)
    ))
    
    fig.add_trace(go.Scatter(
        x=quarterly_data['Quarter'],
        y=quarterly_data['EBITDA Growth (%)'],
        mode='lines+markers',
        name='EBITDA Growth',
        line=dict(color='#00AA00', width=3),
        marker=dict(size=12)
    ))
    
    fig.add_trace(go.Scatter(
        x=quarterly_data['Quarter'],
        y=quarterly_data['PAT Growth (%)'],
        mode='lines+markers',
        name='PAT Growth',
        line=dict(color='#CC0000', width=3),
        marker=dict(size=12)
    ))
    
    fig.update_layout(
        title="Quarterly Growth Trends (FY2025)",
        xaxis_title="Quarter",
        yaxis_title="Growth Rate (%) YoY",
        template='plotly_white',
        height=450,
        hovermode='x unified',
        annotations=[
            dict(
                x=2, y=4.5,
                text="🚨 Q3FY25: Revenue at 4.5% (16-quarter LOW)<br>But PAT growth rebounds to 9.5%",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor="#FF0000",
                ax=40,
                ay=-40,
                bgcolor="#FFEEEE",
                bordercolor="#FF0000"
            )
        ]
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Q3FY25 Key Findings")
        st.info("""
        **Revenue Collapse:**
        - Down to 4.5% YoY (from 6.6% in Q2)
        - 16-quarter LOW
        - Below nominal GDP growth (10-11%)
        
        **Profit Rebound:**
        - PAT back to 9.5% YoY (from -1.0% in Q2)
        - Driven purely by margin management
        - Not from underlying business growth
        """)
    
    with col2:
        st.markdown("### What's Holding Up Profits?")
        st.warning("""
        **Margin Support Mechanisms:**
        1. Cost Cuts (50%): Operating expenses up only 2.5% vs revenue +5%
        2. Commodity Tailwinds (30%): Oil down, raw materials stable
        3. Tax/Finance Benefits (20%): RBI rate cuts flowing through
        
        **The Problem:** All 3 are TEMPORARY
        """)

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: SECTOR ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════

elif page == "🏦 Sector Analysis":
    st.markdown("### 🏦 Sector Performance (FY2025 YTD)")
    
    # Sector Data Table
    st.dataframe(
        sector_data.style.format({
            'Revenue Growth FY25 (%)': '{:.1f}',
            'Profit Growth FY25 (%)': '{:.1f}',
            'Weight in Nifty (%)': '{:.0f}'
        }).background_gradient(
            subset=['Profit Growth FY25 (%)'],
            cmap='RdYlGn',
            vmin=-40,
            vmax=100
        ),
        use_container_width=True,
        hide_index=True
    )
    
    st.divider()
    
    # Scatter plot: Revenue vs Profit Growth
    fig1 = px.scatter(
        sector_data,
        x='Revenue Growth FY25 (%)',
        y='Profit Growth FY25 (%)',
        size='Weight in Nifty (%)',
        color='Profit Growth FY25 (%)',
        hover_name='Sector',
        title='Sector Positioning: Revenue vs Profit Growth',
        labels={
            'Revenue Growth FY25 (%)': 'Revenue Growth (%)',
            'Profit Growth FY25 (%)': 'Profit Growth (%)'
        },
        color_continuous_scale=['red', 'yellow', 'green'],
        template='plotly_white',
        height=450
    )
    
    fig1.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Zero Profit Growth")
    fig1.add_vline(x=7, line_dash="dash", line_color="gray", annotation_text="Avg Revenue Growth")
    
    st.plotly_chart(fig1, use_container_width=True)
    
    st.divider()
    
    # Sector Composition
    col1, col2 = st.columns(2)
    
    with col1:
        fig2 = go.Figure(data=[go.Pie(
            labels=sector_data['Sector'],
            values=sector_data['Weight in Nifty (%)'],
            title='Sector Weight in Nifty 50'
        )])
        fig2.update_layout(height=400)
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 Sector Alerts")
        st.error("""
        **🔴 ENERGY (30% weight)**
        - Profit Growth: -35.4%
        - Revenue Growth: 1.4%
        - Status: SYSTEMIC RISK
        - Action: UNDERWEIGHT
        """)
        
        st.warning("""
        **🟡 FINANCIALS (35% weight)**
        - Profit Growth: 17.3%
        - Revenue Growth: 12.3%
        - Status: SLOWING
        - Action: MONITOR
        """)
        
        st.success("""
        **🟢 INDUSTRIALS (5% weight)**
        - Profit Growth: 25.7%
        - Revenue Growth: 10.6%
        - Status: STRONG
        - Action: OVERWEIGHT
        """)
    
    st.divider()
    
    st.markdown("### 📊 Top vs Bottom Performers")
    
    top_bottom = sector_data.nlargest(3, 'Profit Growth FY25 (%)')
    bottom_sectors = sector_data.nsmallest(3, 'Profit Growth FY25 (%)')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🟢 Best Performers")
        for idx, row in top_bottom.iterrows():
            st.success(f"**{row['Sector']}** (+{row['Profit Growth FY25 (%)']}%)")
    
    with col2:
        st.markdown("#### 🔴 Worst Performers")
        for idx, row in bottom_sectors.iterrows():
            st.error(f"**{row['Sector']}** ({row['Profit Growth FY25 (%)']}%)")

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: EARNINGS DOWNGRADES
# ═══════════════════════════════════════════════════════════════════════════

elif page == "📉 Earnings Downgrades":
    st.markdown("### 📉 Earnings Estimate Downgrades (5-Month Cascade)")
    
    st.dataframe(
        downgrade_data.style.background_gradient(
            subset=['FY25 Profit Growth (%)'],
            cmap='RdYlGn',
            vmin=3,
            vmax=10
        ),
        use_container_width=True,
        hide_index=True
    )
    
    st.divider()
    
    # Downgrade Chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=downgrade_data['Date'],
        y=downgrade_data['FY25 Profit Growth (%)'],
        mode='lines+markers+text',
        name='FY25 Profit Growth Estimate',
        line=dict(color='#CC0000', width=3),
        marker=dict(size=12),
        text=[f"{v:.1f}%" for v in downgrade_data['FY25 Profit Growth (%)']],
        textposition="top center"
    ))
    
    fig.add_hline(y=3.2, line_dash="dash", line_color="red", 
                  annotation_text="Current Estimate (3.2%)", annotation_position="right")
    fig.add_hline(y=9.8, line_dash="dash", line_color="green",
                  annotation_text="Sep 2024 Estimate (9.8%)", annotation_position="right")
    
    fig.update_layout(
        title="FY2025 Profit Growth Estimate Revision (Sep 2024 - Feb 2025)",
        xaxis_title="Date",
        yaxis_title="Profit Growth Estimate (%)",
        template='plotly_white',
        height=450,
        hovermode='x unified',
        yaxis=dict(range=[0, 12])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Sep 2024 Estimate",
            "9.8%",
            "Peak Optimism"
        )
    
    with col2:
        st.metric(
            "Feb 2025 Estimate",
            "3.2%",
            "-67% (Massive Cut)"
        )
    
    with col3:
        st.metric(
            "Downgrade Period",
            "5 Months",
            "Accelerating"
        )
    
    st.divider()
    
    st.markdown("### ⚠️ What Triggered the Downgrades?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Near-Term Triggers (Oct-Nov 2024):**
        1. Q2FY25 earnings missed expectations
        2. Revenue growth slowed to 6.6% (from 9.6% in Q1)
        3. Cost inflation returned despite margin support
        4. Global trade uncertainty (Trump tariffs announced)
        5. Domestic demand slowdown becoming evident
        """)
    
    with col2:
        st.error("""
        **Deep-Dive Triggers (Dec 2024-Feb 2025):**
        1. Energy sector profit crashed (-35%)
        2. Materials sector facing margin compression
        3. Earnings Revision Indicator hit -0.67 (worst since COVID)
        4. More downgrades than upgrades in ALL sectors
        5. Consensus realized margin support has limits
        6. Q3FY25 results confirmed weakness
        """)

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: SCENARIOS
# ═══════════════════════════════════════════════════════════════════════════

elif page == "🎯 Scenarios":
    st.markdown("### 🎯 Three Scenarios for Next 3 Years (FY25-FY27)")
    
    # Scenario Selection
    selected_scenario = st.radio(
        "View Detailed Scenario:",
        list(scenarios.keys()),
        horizontal=True
    )
    
    scenario_data = scenarios[selected_scenario]
    nifty_path = nifty_levels[selected_scenario]
    
    st.divider()
    
    # Selected Scenario Details
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("#### Assumption")
        st.write(scenario_data['description'])
    
    with col2:
        st.markdown("#### Earnings Growth (CAGR)")
        earnings_cagr = ((scenario_data['fy27_earnings'] / scenario_data['fy25_earnings']) ** (1/2) - 1) * 100
        st.metric("CAGR", f"{earnings_cagr:.1f}%")
    
    with col3:
        st.markdown("#### Nifty Return (p.a.)")
        # Rough estimate based on ending level
        ending_nifty = nifty_path[2] * 1000
        return_pa = ((ending_nifty / 23000) ** (1/3) - 1) * 100
        if "Bear" in selected_scenario:
            st.error(f"{return_pa:.1f}%")
        elif "Bull" in selected_scenario:
            st.success(f"{return_pa:.1f}%")
        else:
            st.warning(f"{return_pa:.1f}%")
    
    with col4:
        st.markdown("#### Probability")
        if "Base" in selected_scenario:
            st.info("50%")
        else:
            st.warning("25%")
    
    st.divider()
    
    # Earnings Path
    fig1 = go.Figure()
    
    years = ['FY2025', 'FY2026', 'FY2027']
    earnings = [scenario_data['fy25_earnings'], scenario_data['fy26_earnings'], scenario_data['fy27_earnings']]
    
    fig1.add_trace(go.Scatter(
        x=years,
        y=earnings,
        mode='lines+markers+text',
        name='Earnings Growth',
        line=dict(color=scenario_data['color'], width=3),
        marker=dict(size=14),
        text=[f"{v:.1f}%" for v in earnings],
        textposition="top center"
    ))
    
    fig1.update_layout(
        title="Earnings Growth Path",
        xaxis_title="Year",
        yaxis_title="Earnings Growth (%)",
        template='plotly_white',
        height=350,
        hovermode='x unified'
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    
    # Nifty Path
    with col2:
        fig2 = go.Figure()
        
        fig2.add_trace(go.Scatter(
            x=years,
            y=[level for level in nifty_path],
            mode='lines+markers+text',
            name='Nifty 50 (K level)',
            line=dict(color=scenario_data['color'], width=3),
            marker=dict(size=14),
            text=[f"{level:.0f}K" for level in nifty_path],
            textposition="top center"
        ))
        
        fig2.update_layout(
            title="Nifty 50 Target Path",
            xaxis_title="Year",
            yaxis_title="Nifty Level (K)",
            template='plotly_white',
            height=350,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    st.divider()
    
    # Detailed Scenario Comparison
    st.markdown("### 📊 All Scenarios Compared")
    
    comparison_df = pd.DataFrame({
        'Scenario': list(scenarios.keys()),
        'Description': [scenarios[s]['description'] for s in scenarios.keys()],
        'FY25 Earnings': [scenarios[s]['fy25_earnings'] for s in scenarios.keys()],
        'FY26 Earnings': [scenarios[s]['fy26_earnings'] for s in scenarios.keys()],
        'FY27 Earnings': [scenarios[s]['fy27_earnings'] for s in scenarios.keys()],
        'Nifty Target': [f"{nifty_levels[s][2]*1000:.0f}" for s in scenarios.keys()],
    })
    
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: DATA EXPLORER
# ═══════════════════════════════════════════════════════════════════════════

elif page == "📋 Data Explorer":
    st.markdown("### 📋 Explore All Data")
    
    data_option = st.selectbox(
        "Choose Dataset:",
        ["5-Year Trend", "Quarterly Trends", "Sector Performance", "Earnings Downgrades"]
    )
    
    if data_option == "5-Year Trend":
        st.markdown("#### Nifty 50: 5-Year Performance")
        st.dataframe(five_year_data, use_container_width=True, hide_index=True)
        
        csv = five_year_data.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="5_year_nifty_data.csv",
            mime="text/csv"
        )
    
    elif data_option == "Quarterly Trends":
        st.markdown("#### FY2025 Quarterly Performance")
        st.dataframe(quarterly_data, use_container_width=True, hide_index=True)
        
        csv = quarterly_data.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="quarterly_fy25_data.csv",
            mime="text/csv"
        )
    
    elif data_option == "Sector Performance":
        st.markdown("#### Sector-wise Analysis")
        st.dataframe(
            sector_data.style.format({
                'Revenue Growth FY25 (%)': '{:.1f}',
                'Profit Growth FY25 (%)': '{:.1f}',
                'Weight in Nifty (%)': '{:.0f}'
            }),
            use_container_width=True,
            hide_index=True
        )
        
        csv = sector_data.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="sector_analysis.csv",
            mime="text/csv"
        )
    
    elif data_option == "Earnings Downgrades":
        st.markdown("#### Earnings Revision Tracking")
        st.dataframe(downgrade_data, use_container_width=True, hide_index=True)
        
        csv = downgrade_data.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="earnings_downgrades.csv",
            mime="text/csv"
        )

# ═══════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════

st.divider()
st.markdown("""
---
**📊 Indian Stock Market Analysis Dashboard**

Data Source: NSE Corporate Performance Review (Q3FY25), RBI Annual Reports, Business Standard  
Analysis Period: FY2021 – FY2025 (Projected)  
Created: January 2026 | Prof. V. Ravichandran | The Mountain Path – World of Finance

---
**Disclaimer:** This analysis is for educational purposes. Not investment advice. Please consult financial advisors before making investment decisions.
""")
