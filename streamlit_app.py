
"""
Indian Stock Market Analysis Dashboard
Main Application Module

Architecture: Streamlit + Plotly + Pandas
Design System: Mountain Path - World of Finance
Created: January 2026
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Import custom modules
from config import (
    configure_page, apply_custom_css, COLORS, CHART_HEIGHT, CHART_HEIGHT_SMALL,
    AUTHOR, BRAND_NAME, EXPERIENCE, LOCATION, DATA_SOURCES
)
from styles import (
    render_main_title, render_section_header, render_subsection_header,
    render_info_box, render_warning_box, render_success_box, render_divider,
    render_footer, render_sidebar_metrics, render_sidebar_alert, spacing
)
from data import (
    get_five_year_data, get_quarterly_data, get_sector_data, 
    get_downgrade_data, get_scenarios, calculate_nifty_levels,
    calculate_key_metrics
)

# ═══════════════════════════════════════════════════════════════════════════
# PAGE INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════

configure_page()
apply_custom_css()

# Load all data once
@st.cache_data
def load_data():
    return {
        'five_year': get_five_year_data(),
        'quarterly': get_quarterly_data(),
        'sector': get_sector_data(),
        'downgrades': get_downgrade_data(),
        'scenarios': get_scenarios(),
        'metrics': calculate_key_metrics()
    }

data = load_data()
scenarios = data['scenarios']
nifty_levels = calculate_nifty_levels(scenarios)

# ═══════════════════════════════════════════════════════════════════════════
# SIDEBAR NAVIGATION
# ═══════════════════════════════════════════════════════════════════════════

st.sidebar.markdown(f"### 🏔️ {BRAND_NAME}")
st.sidebar.markdown(f"*{AUTHOR}*")
st.sidebar.markdown(f"*{EXPERIENCE}*")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "📍 Choose Analysis:",
    ["🏠 Overview", "📈 5-Year Trend", "📊 Quarterly Deep-Dive", 
     "🏦 Sector Analysis", "📉 Earnings Downgrades", "🎯 Scenarios", 
     "📋 Data Explorer"],
    key="main_nav"
)

st.sidebar.markdown("---")

# Sidebar Metrics
sidebar_metrics = {
    'Revenue CAGR': (f"{data['metrics']['revenue_cagr']:.1f}%", "-5.0 pp"),
    'Current Rev Growth': (f"{data['metrics']['current_rev_growth']:.1f}%", "Q3FY25"),
    'Profit CAGR': (f"{data['metrics']['pat_cagr']:.1f}%", "+3.2 pp"),
    'Current PAT Growth': (f"{data['metrics']['current_pat_growth']:.1f}%", "Q3FY25")
}

render_sidebar_metrics(sidebar_metrics)

st.sidebar.markdown("---")
render_sidebar_alert(
    "⚠️ Valuation Alert",
    "Current P/E: 25x<br/>Fair Value P/E: 10-12x<br/>Gap: -50% to -60%",
    "warning"
)

# ═══════════════════════════════════════════════════════════════════════════
# MAIN HEADER
# ═══════════════════════════════════════════════════════════════════════════

render_main_title(
    "📊 Indian Stock Market Analysis",
    "Is Growth Driven by Revenue Expansion or Margin Re-Rating?"
)

st.markdown(
    f"<p style='text-align: center; color: {COLORS['medium_gray']};'>"
    f"Analysis of Nifty 50 (FY2021-FY2025) | Data: NSE, RBI, Business Standard</p>",
    unsafe_allow_html=True
)

render_divider()

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════

if page == "🏠 Overview":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 💰 Revenue Story")
        st.write("- **5-Yr CAGR:** 11.5%\n- **Current (Q3):** 4.5%\n- **Trend:** ↘️ Decelerating\n- **Status:** 16-quarter LOW")
    
    with col2:
        st.markdown("### 📊 Profit Story")
        st.write("- **5-Yr CAGR:** 14.7%\n- **Current (Q3):** 9.5%\n- **Trend:** ↑ Margin Support\n- **Status:** Unsustainable")
    
    with col3:
        st.markdown("### ⚖️ The Divergence")
        st.write("- **Profit 53% faster** than revenue\n- **Driven by:** Margin expansion\n- **Risk Level:** 🔴 HIGH\n- **Sustainability:** ❌ Limited")
    
    render_divider()
    
    render_section_header("🔍 The Core Problem")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_success_box(
            "<strong>FY2021-2024: Healthy Growth</strong><br/>"
            "✅ Revenue growing<br/>"
            "✅ Margins expanding<br/>"
            "✅ Both working together<br/>"
            "✅ Sustainable"
        )
    
    with col2:
        render_warning_box(
            "<strong>FY2025 NOW: Concerning Shift</strong><br/>"
            "⚠️ Revenue collapsing<br/>"
            "⚠️ Margins supporting profits<br/>"
            "⚠️ Cost cuts, commodity tailwinds, tax benefits<br/>"
            "❌ Sustainable: NO"
        )
    
    render_divider()
    
    render_subsection_header("📈 5-Year Overview Chart")
    
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
        name='Profit Growth (PAT)',
        line=dict(color=COLORS['accent_red'], width=3),
        marker=dict(size=10)
    ))
    
    fig.update_layout(
        title="Revenue vs Profit Growth (5-Year Divergence)",
        xaxis_title="Fiscal Year",
        yaxis_title="Growth Rate (%)",
        hovermode='x unified',
        template='plotly_white',
        height=CHART_HEIGHT,
        font=dict(size=11)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    render_divider()
    
    render_subsection_header("🎯 Three Scenarios (Next 3 Years)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        render_success_box(
            "<strong>Base Case (50%)</strong><br/>"
            "Margin Resilience Persists<br/>"
            "• Earnings CAGR: 9.7%<br/>"
            "• Nifty Return: +10% p.a.<br/>"
            "• Target: 26,000-27,000<br/>"
            "• Verdict: Fair, no upside"
        )
    
    with col2:
        render_warning_box(
            "<strong>Bear Case (25%)</strong><br/>"
            "Margin Compression Hits<br/>"
            "• Earnings CAGR: 4.8%<br/>"
            "• Nifty Return: -0.2% p.a.<br/>"
            "• Target: 20,000-21,000<br/>"
            "• Verdict: Negative, risky"
        )
    
    with col3:
        render_success_box(
            "<strong>Bull Case (25%)</strong><br/>"
            "Revenue Reaccelerates<br/>"
            "• Earnings CAGR: 12.8%<br/>"
            "• Nifty Return: +14.5% p.a.<br/>"
            "• Target: 33,000-35,000<br/>"
            "• Verdict: Strong, needs catalyst"
        )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: 5-YEAR TREND
# ═══════════════════════════════════════════════════════════════════════════

elif page == "📈 5-Year Trend":
    render_section_header("📊 Nifty 50 - 5-Year Performance (FY2021-FY2025)")
    
    five_year = data['five_year']
    
    st.dataframe(
        five_year.style.background_gradient(
            subset=['Revenue Growth (%)', 'EBITDA Growth (%)', 'PAT Growth (%)'],
            cmap='RdYlGn'
        ),
        use_container_width=True,
        hide_index=True
    )
    
    render_divider()
    
    # Growth Rates Comparison
    fig1 = go.Figure()
    
    fig1.add_trace(go.Bar(
        x=five_year['Fiscal Year'],
        y=five_year['Revenue Growth (%)'],
        name='Revenue Growth',
        marker_color=COLORS['chart_blue']
    ))
    
    fig1.add_trace(go.Bar(
        x=five_year['Fiscal Year'],
        y=five_year['EBITDA Growth (%)'],
        name='EBITDA Growth',
        marker_color=COLORS['accent_green']
    ))
    
    fig1.add_trace(go.Bar(
        x=five_year['Fiscal Year'],
        y=five_year['PAT Growth (%)'],
        name='PAT Growth',
        marker_color=COLORS['accent_red']
    ))
    
    fig1.update_layout(
        title="Growth Rates Comparison (YoY)",
        barmode='group',
        xaxis_title="Fiscal Year",
        yaxis_title="Growth Rate (%)",
        template='plotly_white',
        height=CHART_HEIGHT,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig1, use_container_width=True)
    
    render_divider()
    
    # Margin Trends
    fig2 = go.Figure()
    
    fig2.add_trace(go.Scatter(
        x=five_year['Fiscal Year'],
        y=five_year['EBITDA Margin (%)'],
        mode='lines+markers',
        name='EBITDA Margin',
        line=dict(color=COLORS['accent_green'], width=3),
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
        title="Margin Trends Over 5 Years",
        xaxis_title="Fiscal Year",
        yaxis_title="Margin (%)",
        template='plotly_white',
        height=CHART_HEIGHT,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    render_divider()
    
    render_subsection_header("📌 Key Insights")
    col1, col2 = st.columns(2)
    
    with col1:
        render_info_box(
            "<strong>The Story:</strong><br/>"
            "• FY21-FY23: Healthy growth (both revenue & profit expanding)<br/>"
            "• FY24: Peak profitability, first signs of weakness<br/>"
            "• FY25: Revenue collapse, margin engineering begins<br/><br/>"
            "<strong>The Concern:</strong><br/>"
            "• Profit growing 53% faster than revenue over 5 years<br/>"
            "• Margins used as 'prop' when revenue slows<br/>"
            "• Limited margin expansion left before hits ceiling"
        )
    
    with col2:
        render_info_box(
            "<strong>Breakdown:</strong><br/>"
            "• Revenue CAGR: 11.5%<br/>"
            "• EBITDA CAGR: 13.8% (+330 bps)<br/>"
            "• PAT CAGR: 14.7% (+320 bps)<br/><br/>"
            "<strong>Current Status:</strong><br/>"
            "• EBITDA Margin stable at 33%<br/>"
            "• PAT Margin stable at 10.7%<br/>"
            "• But revenue growth failing (4.5%)"
        )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: QUARTERLY DEEP-DIVE
# ═══════════════════════════════════════════════════════════════════════════

elif page == "📊 Quarterly Deep-Dive":
    render_section_header("📊 Q3FY25 & Recent Quarterly Trends")
    
    quarterly = data['quarterly']
    
    st.dataframe(
        quarterly.style.background_gradient(
            subset=['Revenue Growth (%)', 'EBITDA Growth (%)', 'PAT Growth (%)'],
            cmap='RdYlGn'
        ),
        use_container_width=True,
        hide_index=True
    )
    
    render_divider()
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=quarterly['Quarter'],
        y=quarterly['Revenue Growth (%)'],
        mode='lines+markers',
        name='Revenue Growth',
        line=dict(color=COLORS['chart_blue'], width=3),
        marker=dict(size=12)
    ))
    
    fig.add_trace(go.Scatter(
        x=quarterly['Quarter'],
        y=quarterly['EBITDA Growth (%)'],
        mode='lines+markers',
        name='EBITDA Growth',
        line=dict(color=COLORS['accent_green'], width=3),
        marker=dict(size=12)
    ))
    
    fig.add_trace(go.Scatter(
        x=quarterly['Quarter'],
        y=quarterly['PAT Growth (%)'],
        mode='lines+markers',
        name='PAT Growth',
        line=dict(color=COLORS['accent_red'], width=3),
        marker=dict(size=12)
    ))
    
    fig.update_layout(
        title="Quarterly Growth Trends (FY2025)",
        xaxis_title="Quarter",
        yaxis_title="Growth Rate (%) YoY",
        template='plotly_white',
        height=CHART_HEIGHT,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    render_divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_subsection_header("Q3FY25 Key Findings")
        render_warning_box(
            "<strong>Revenue Collapse:</strong><br/>"
            "• Down to 4.5% YoY (from 6.6% in Q2)<br/>"
            "• 16-quarter LOW<br/>"
            "• Below nominal GDP growth (10-11%)<br/><br/>"
            "<strong>Profit Rebound:</strong><br/>"
            "• PAT back to 9.5% YoY (from -1.0% in Q2)<br/>"
            "• Driven purely by margin management<br/>"
            "• Not from underlying business growth"
        )
    
    with col2:
        render_subsection_header("What's Holding Up Profits?")
        render_warning_box(
            "<strong>Margin Support Mechanisms:</strong><br/>"
            "1. Cost Cuts (50%): Operating expenses up only 2.5% vs revenue +5%<br/>"
            "2. Commodity Tailwinds (30%): Oil down, raw materials stable<br/>"
            "3. Tax/Finance Benefits (20%): RBI rate cuts flowing through<br/><br/>"
            "<strong>The Problem:</strong> All 3 are TEMPORARY"
        )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: SECTOR ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════

elif page == "🏦 Sector Analysis":
    render_section_header("🏦 Sector Performance (FY2025 YTD)")
    
    sector = data['sector']
    
    st.dataframe(
        sector.style.format({
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
    
    render_divider()
    
    # Scatter plot
    fig1 = px.scatter(
        sector,
        x='Revenue Growth FY25 (%)',
        y='Profit Growth FY25 (%)',
        size='Weight in Nifty (%)',
        color='Profit Growth FY25 (%)',
        hover_name='Sector',
        title='Sector Positioning: Revenue vs Profit Growth',
        color_continuous_scale=['red', 'yellow', 'green'],
        template='plotly_white',
        height=CHART_HEIGHT
    )
    
    fig1.add_hline(y=0, line_dash="dash", line_color="gray")
    fig1.add_vline(x=7, line_dash="dash", line_color="gray")
    
    st.plotly_chart(fig1, use_container_width=True)
    
    render_divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig2 = go.Figure(data=[go.Pie(
            labels=sector['Sector'],
            values=sector['Weight in Nifty (%)'],
            title='Sector Weight in Nifty 50'
        )])
        fig2.update_layout(height=400)
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        render_subsection_header("🎯 Sector Alerts")
        render_warning_box(
            "<strong>🔴 ENERGY (30% weight)</strong><br/>"
            "• Profit Growth: -35.4%<br/>"
            "• Revenue Growth: 1.4%<br/>"
            "• Status: SYSTEMIC RISK<br/>"
            "• Action: UNDERWEIGHT"
        )
        
        render_warning_box(
            "<strong>🟡 FINANCIALS (35% weight)</strong><br/>"
            "• Profit Growth: 17.3%<br/>"
            "• Revenue Growth: 12.3%<br/>"
            "• Status: SLOWING<br/>"
            "• Action: MONITOR"
        )
        
        render_success_box(
            "<strong>🟢 INDUSTRIALS (5% weight)</strong><br/>"
            "• Profit Growth: 25.7%<br/>"
            "• Revenue Growth: 10.6%<br/>"
            "• Status: STRONG<br/>"
            "• Action: OVERWEIGHT"
        )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: EARNINGS DOWNGRADES
# ═══════════════════════════════════════════════════════════════════════════

elif page == "📉 Earnings Downgrades":
    render_section_header("📉 Earnings Estimate Downgrades (5-Month Cascade)")
    
    downgrades = data['downgrades']
    
    st.dataframe(
        downgrades.style.background_gradient(
            subset=['FY25 Profit Growth (%)'],
            cmap='RdYlGn',
            vmin=3,
            vmax=10
        ),
        use_container_width=True,
        hide_index=True
    )
    
    render_divider()
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=downgrades['Date'],
        y=downgrades['FY25 Profit Growth (%)'],
        mode='lines+markers+text',
        name='FY25 Profit Growth Estimate',
        line=dict(color=COLORS['accent_red'], width=3),
        marker=dict(size=12),
        text=[f"{v:.1f}%" for v in downgrades['FY25 Profit Growth (%)']],
        textposition="top center"
    ))
    
    fig.update_layout(
        title="FY2025 Profit Growth Estimate Revision (Sep 2024 - Feb 2025)",
        xaxis_title="Date",
        yaxis_title="Profit Growth Estimate (%)",
        template='plotly_white',
        height=CHART_HEIGHT,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    render_divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Sep 2024 Estimate", "9.8%", "Peak Optimism")
    
    with col2:
        st.metric("Feb 2025 Estimate", "3.2%", "-67% (Massive Cut)")
    
    with col3:
        st.metric("Downgrade Period", "5 Months", "Accelerating")
    
    render_divider()
    
    render_subsection_header("⚠️ What Triggered the Downgrades?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_warning_box(
            "<strong>Near-Term Triggers (Oct-Nov 2024):</strong><br/>"
            "1. Q2FY25 earnings missed expectations<br/>"
            "2. Revenue growth slowed to 6.6% (from 9.6% in Q1)<br/>"
            "3. Cost inflation returned despite margin support<br/>"
            "4. Global trade uncertainty (Trump tariffs announced)<br/>"
            "5. Domestic demand slowdown becoming evident"
        )
    
    with col2:
        render_warning_box(
            "<strong>Deep-Dive Triggers (Dec 2024-Feb 2025):</strong><br/>"
            "1. Energy sector profit crashed (-35%)<br/>"
            "2. Materials sector facing margin compression<br/>"
            "3. Earnings Revision Indicator hit -0.67 (worst since COVID)<br/>"
            "4. More downgrades than upgrades in ALL sectors<br/>"
            "5. Consensus realized margin support has limits<br/>"
            "6. Q3FY25 results confirmed weakness"
        )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: SCENARIOS
# ═══════════════════════════════════════════════════════════════════════════

elif page == "🎯 Scenarios":
    render_section_header("🎯 Three Scenarios for Next 3 Years (FY25-FY27)")
    
    selected_scenario = st.radio(
        "View Detailed Scenario:",
        list(scenarios.keys()),
        horizontal=True
    )
    
    scenario_data = scenarios[selected_scenario]
    nifty_path = nifty_levels[selected_scenario]
    
    render_divider()
    
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
    
    render_divider()
    
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
        height=CHART_HEIGHT_SMALL,
        hovermode='x unified'
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    
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
            height=CHART_HEIGHT_SMALL,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    render_divider()
    
    render_subsection_header("📊 All Scenarios Compared")
    
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
    render_section_header("📋 Explore All Data")
    
    data_option = st.selectbox(
        "Choose Dataset:",
        ["5-Year Trend", "Quarterly Trends", "Sector Performance", "Earnings Downgrades"]
    )
    
    if data_option == "5-Year Trend":
        st.markdown("#### Nifty 50: 5-Year Performance")
        st.dataframe(data['five_year'], use_container_width=True, hide_index=True)
        
        csv = data['five_year'].to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="5_year_nifty_data.csv",
            mime="text/csv"
        )
    
    elif data_option == "Quarterly Trends":
        st.markdown("#### FY2025 Quarterly Performance")
        st.dataframe(data['quarterly'], use_container_width=True, hide_index=True)
        
        csv = data['quarterly'].to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="quarterly_fy25_data.csv",
            mime="text/csv"
        )
    
    elif data_option == "Sector Performance":
        st.markdown("#### Sector-wise Analysis")
        st.dataframe(
            data['sector'].style.format({
                'Revenue Growth FY25 (%)': '{:.1f}',
                'Profit Growth FY25 (%)': '{:.1f}',
                'Weight in Nifty (%)': '{:.0f}'
            }),
            use_container_width=True,
            hide_index=True
        )
        
        csv = data['sector'].to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="sector_analysis.csv",
            mime="text/csv"
        )
    
    elif data_option == "Earnings Downgrades":
        st.markdown("#### Earnings Revision Tracking")
        st.dataframe(data['downgrades'], use_container_width=True, hide_index=True)
        
        csv = data['downgrades'].to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="earnings_downgrades.csv",
            mime="text/csv"
        )

# ═══════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════

render_divider()
render_footer(AUTHOR, BRAND_NAME, "NSE Corporate Performance Review (Q3FY25), RBI Annual Reports, Business Standard")
