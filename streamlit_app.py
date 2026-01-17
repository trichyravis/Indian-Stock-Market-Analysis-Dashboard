
"""
Indian Stock Market Analysis Dashboard
Main Application Module

Architecture: Streamlit + Plotly + Pandas
Design System: Mountain Path - World of Finance
Version: 2.0 (Refactored with data.py module)

IMPROVEMENTS:
- Modular imports from data, config, and styles
- Clean separation of concerns
- Centralized configuration
- Reusable UI components
- Production-grade error handling
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import warnings

# ═══════════════════════════════════════════════════════════════════════════
# MATPLOTLIB AVAILABILITY CHECK
# ═══════════════════════════════════════════════════════════════════════════

try:
    import matplotlib
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

# ═══════════════════════════════════════════════════════════════════════════
# MODULE IMPORTS
# ═══════════════════════════════════════════════════════════════════════════

# Data module imports
try:
    from data import (
        get_five_year_data,
        get_quarterly_data,
        get_sector_data,
        get_downgrade_data,
        get_scenarios,
        calculate_nifty_levels,
        calculate_key_metrics,
        load_all_data,
        validate_data,
        get_data_summary,
        export_to_csv,
        CACHE_TTL
    )
except ImportError as e:
    st.error(f"Error importing data module: {str(e)}")
    st.stop()

# Config module imports
try:
    from config import (
        COLORS,
        AUTHOR,
        BRAND_NAME,
        EXPERIENCE,
        LOCATION,
        CHART_HEIGHT,
        CHART_HEIGHT_SMALL,
        PAGES,
        MESSAGES
    )
    # Try to import data sources (may not exist in old config)
    try:
        from config import (
            DATA_SOURCES_INFO,
            PRIMARY_DATA_SOURCES,
            RESEARCH_SOURCES,
            GLOBAL_RESEARCH
        )
    except ImportError:
        # Fallback if data sources not in config
        DATA_SOURCES_INFO = {}
        PRIMARY_DATA_SOURCES = []
        RESEARCH_SOURCES = []
        GLOBAL_RESEARCH = []
except ImportError as e:
    st.error(f"Error importing config module: {str(e)}")
    st.stop()

# Styles module imports
try:
    from styles import (
        render_main_title,
        render_section_header,
        render_subsection_header,
        render_info_box,
        render_warning_box,
        render_success_box,
        render_divider,
        render_footer,
        render_sidebar_metrics,
        render_sidebar_alert,
        apply_custom_css
    )
except ImportError as e:
    st.error(f"Error importing styles module: {str(e)}")
    st.stop()

warnings.filterwarnings('ignore')

# ═══════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def display_styled_dataframe(df, columns_to_style=None, width='stretch', hide_index=True):
    """
    Display DataFrame with optional styling, fallback if matplotlib unavailable
    
    Args:
        df: DataFrame to display
        columns_to_style: List of columns to apply gradient to
        width: Column width ('stretch' or 'content')
        hide_index: Hide row index
    """
    if MATPLOTLIB_AVAILABLE and columns_to_style:
        try:
            styled_df = df.style.background_gradient(
                subset=columns_to_style,
                cmap='RdYlGn'
            )
            st.dataframe(styled_df, width=width, hide_index=hide_index)
        except Exception as e:
            # Fallback to unstyled
            st.warning(f"⚠️ Styling failed: {str(e)}. Displaying without styling.")
            st.dataframe(df, width=width, hide_index=hide_index)
    else:
        # Display without styling
        st.dataframe(df, width=width, hide_index=hide_index)

# ═══════════════════════════════════════════════════════════════════════════
# PAGE INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data(ttl=CACHE_TTL)
def initialize_page():
    """Initialize page configuration"""
    st.set_page_config(
        page_title=MESSAGES['header_title'],
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    return True

# Initialize page
initialize_page()
apply_custom_css()

# ═══════════════════════════════════════════════════════════════════════════
# DATA LOADING & VALIDATION
# ═══════════════════════════════════════════════════════════════════════════

try:
    # Validate data integrity
    is_valid, validation_msg = validate_data()
    if not is_valid:
        st.warning(f"Data validation warning: {validation_msg}")
    
    # Load all data
    data = load_all_data()
    scenarios = data['scenarios']
    nifty_levels = data['nifty_levels']
    metrics = data['metrics']
    
except Exception as e:
    st.error(f"Failed to load data: {str(e)}")
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════
# SIDEBAR NAVIGATION
# ═══════════════════════════════════════════════════════════════════════════

st.sidebar.markdown(f"### 🏔️ {BRAND_NAME}")
st.sidebar.markdown(f"*{AUTHOR}*")
st.sidebar.markdown(f"*{EXPERIENCE}*")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "📍 Choose Analysis:",
    PAGES,
    key="main_nav"
)

st.sidebar.markdown("---")

# Sidebar Metrics
sidebar_metrics = {
    'Revenue CAGR': (f"{metrics['revenue_cagr']:.1f}%", f"Current: {metrics['current_rev_growth']:.1f}%"),
    'Profit CAGR': (f"{metrics['pat_cagr']:.1f}%", f"Current: {metrics['current_pat_growth']:.1f}%"),
    'Divergence': (f"{metrics['divergence_factor']:.1f} pp", "Profit vs Revenue"),
    'P/E Multiple': (f"{metrics['pe_current']:.1f}x", f"Fair: {metrics['pe_fair_range'][0]}-{metrics['pe_fair_range'][1]}x"),
}
render_sidebar_metrics(sidebar_metrics)

st.sidebar.markdown("---")
render_sidebar_alert(
    "⚠️ Market Alert",
    f"Current P/E: {metrics['pe_current']:.1f}x\nFair Value: {metrics['pe_fair_range'][0]}-{metrics['pe_fair_range'][1]}x\nValuation Gap: {((metrics['pe_current']/(metrics['pe_fair_range'][0]+metrics['pe_fair_range'][1])/2)-1)*100:.0f}%",
    "warning"
)

# ═══════════════════════════════════════════════════════════════════════════
# MAIN HEADER
# ═══════════════════════════════════════════════════════════════════════════

render_main_title(
    MESSAGES['header_title'],
    MESSAGES['header_subtitle']
)

st.markdown(
    f"<p style='text-align:center; color:{COLORS['text_muted']}; font-size:0.9rem;'>"
    f"Analysis of Nifty 50 (FY2021-FY2025 YTD) | Data: NSE, RBI, BSE, MCA"
    f"</p>",
    unsafe_allow_html=True
)

render_divider()

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════

if page == PAGES[0]:  # 🏠 Overview
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 💰 Revenue Story")
        st.write(f"- **5-Yr Growth:** Declining trend\n- **Current:** {metrics['current_rev_growth']:.1f}%\n- **Status:** Below nominal GDP\n- **Concern:** Structural slowdown")
    
    with col2:
        st.markdown("### 📊 Profit Story")
        st.write(f"- **5-Yr Growth:** Elevated levels\n- **Current:** {metrics['current_pat_growth']:.1f}%\n- **Driver:** Margin expansion\n- **Risk:** Unsustainable")
    
    with col3:
        st.markdown("### ⚖️ The Divergence")
        st.write(f"- **Gap:** {metrics['divergence_factor']:.1f} pp faster\n- **Source:** Cost cuts + tailwinds\n- **Risk Level:** 🔴 HIGH\n- **Timeline:** 2-3 quarters")
    
    render_divider()
    render_section_header("🔍 Growth Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_success_box(
            "<b>FY2021-2024: Healthy Growth</b><br>"
            "✅ Revenue expanding (+10.5% avg)<br>"
            "✅ Margins improving (+50 bps)<br>"
            "✅ Both drivers working<br>"
            "✅ Sustainable model"
        )
    
    with col2:
        render_warning_box(
            "<b>FY2025: Concerning Shift</b><br>"
            "⚠️ Revenue decelerating (6.9%)<br>"
            "⚠️ Margins propping profits<br>"
            "⚠️ One-time tailwinds fading<br>"
            "❌ Unsustainable"
        )
    
    render_divider()
    render_subsection_header("📈 5-Year Performance")
    
    five_year = data['five_year']
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=five_year['Fiscal Year'],
        y=five_year['Revenue Growth (%)'],
        mode='lines+markers',
        name='Revenue Growth',
        line=dict(color=COLORS['chart_blue'], width=3),
        marker=dict(size=10),
        hovertemplate='<b>%{x}</b><br>Revenue: %{y:.1f}%<extra></extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=five_year['Fiscal Year'],
        y=five_year['PAT Growth (%)'],
        mode='lines+markers',
        name='Profit Growth',
        line=dict(color=COLORS['accent_red'], width=3),
        marker=dict(size=10),
        hovertemplate='<b>%{x}</b><br>Profit: %{y:.1f}%<extra></extra>'
    ))
    
    fig.update_layout(
        title="Revenue vs Profit Growth - 5 Year Divergence",
        xaxis_title="Fiscal Year",
        yaxis_title="Growth Rate (%)",
        hovermode='x unified',
        template='plotly_white',
        height=CHART_HEIGHT,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='white',
        margin=dict(l=50, r=50, t=80, b=50)
    )
    
    st.plotly_chart(fig, width='stretch')
    
    render_divider()
    render_subsection_header("🎯 Scenario Framework")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        render_success_box(
            "<b>Base Case (50%)</b><br>"
            "<i>Margin Resilience</i><br>"
            f"• Earnings: {scenarios['Base Case (50%)']['fy25_earnings']:.1f}%<br>"
            "• Nifty: +10% p.a.<br>"
            "• Fair value"
        )
    
    with col2:
        render_warning_box(
            "<b>Bear Case (25%)</b><br>"
            "<i>Margin Compression</i><br>"
            f"• Earnings: {scenarios['Bear Case (25%)']['fy25_earnings']:.1f}%<br>"
            "• Nifty: -0.2% p.a.<br>"
            "• Risky"
        )
    
    with col3:
        render_success_box(
            "<b>Bull Case (25%)</b><br>"
            "<i>Revenue Recovery</i><br>"
            f"• Earnings: {scenarios['Bull Case (25%)']['fy25_earnings']:.1f}%<br>"
            "• Nifty: +14.5% p.a.<br>"
            "• Catalyst needed"
        )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: 5-YEAR TREND
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[1]:  # 📈 5-Year Trend
    render_section_header("📊 5-Year Performance Analysis (FY2021-FY2025 YTD)")
    
    five_year = data['five_year']
    display_styled_dataframe(
        five_year,
        columns_to_style=['Revenue Growth (%)', 'EBITDA Growth (%)', 'PAT Growth (%)'],
        width='stretch',
        hide_index=True
    )
    
    render_divider()
    
    # Growth Rates Comparison
    fig1 = go.Figure()
    
    fig1.add_trace(go.Bar(
        x=five_year['Fiscal Year'],
        y=five_year['Revenue Growth (%)'],
        name='Revenue',
        marker_color=COLORS['chart_blue']
    ))
    
    fig1.add_trace(go.Bar(
        x=five_year['Fiscal Year'],
        y=five_year['EBITDA Growth (%)'],
        name='EBITDA',
        marker_color=COLORS['accent_green']
    ))
    
    fig1.add_trace(go.Bar(
        x=five_year['Fiscal Year'],
        y=five_year['PAT Growth (%)'],
        name='PAT',
        marker_color=COLORS['accent_red']
    ))
    
    fig1.update_layout(
        title="Growth Comparison (YoY)",
        barmode='group',
        xaxis_title="Fiscal Year",
        yaxis_title="Growth Rate (%)",
        template='plotly_white',
        height=CHART_HEIGHT,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig1, width='stretch')
    
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
        title="Margin Trends",
        xaxis_title="Fiscal Year",
        yaxis_title="Margin (%)",
        template='plotly_white',
        height=CHART_HEIGHT,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig2, width='stretch')
    
    render_divider()
    render_subsection_header("📌 Key Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_info_box(
            "<b>Historical Narrative:</b><br>"
            "• FY21-FY23: Strong revenue growth (10-15%)<br>"
            "• FY24: Revenue slowed to 10.7%<br>"
            "• FY25: Sharp deceleration to 6.9%<br>"
            "• Margins: Stable 33% EBITDA / 10.5% PAT"
        )
    
    with col2:
        render_info_box(
            "<b>Divergence Analysis:</b><br>"
            "• Revenue CAGR: Declining trajectory<br>"
            "• Profit CAGR: Elevated by margin expansion<br>"
            "• Gap widening: Profit 53% faster than revenue<br>"
            "• Sustainability: Limited 2-3 quarter runway"
        )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: QUARTERLY DEEP-DIVE
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[2]:  # 📊 Quarterly Deep-Dive
    render_section_header("📊 FY2025 Quarterly Analysis")
    
    quarterly = data['quarterly']
    display_styled_dataframe(
        quarterly,
        columns_to_style=['Revenue Growth (%)', 'EBITDA Growth (%)', 'PAT Growth (%)'],
        width='stretch',
        hide_index=True
    )
    
    render_divider()
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=quarterly['Quarter'],
        y=quarterly['Revenue Growth (%)'],
        mode='lines+markers',
        name='Revenue',
        line=dict(color=COLORS['chart_blue'], width=3),
        marker=dict(size=12)
    ))
    
    fig.add_trace(go.Scatter(
        x=quarterly['Quarter'],
        y=quarterly['EBITDA Growth (%)'],
        mode='lines+markers',
        name='EBITDA',
        line=dict(color=COLORS['accent_green'], width=3),
        marker=dict(size=12)
    ))
    
    fig.add_trace(go.Scatter(
        x=quarterly['Quarter'],
        y=quarterly['PAT Growth (%)'],
        mode='lines+markers',
        name='PAT',
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
    
    st.plotly_chart(fig, width='stretch')
    
    render_divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_subsection_header("Q3FY25 Summary")
        render_warning_box(
            "<b>Revenue Concern:</b><br>"
            f"• Growth: {quarterly.iloc[-1]['Revenue Growth (%)']}% YoY<br>"
            "• Trend: Declining 3 quarters<br>"
            "• Status: Multi-quarter LOW<br>"
            "• Implication: Structural slowdown"
        )
    
    with col2:
        render_subsection_header("Margin Support")
        render_warning_box(
            "<b>Profit Rebound:</b><br>"
            f"• Growth: {quarterly.iloc[-1]['PAT Growth (%)']}% (vs -1% Q2)<br>"
            "• Driver: Margin expansion<br>"
            "• Sustainability: Limited<br>"
            "• Risk: Mean reversion coming"
        )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: SECTOR ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[3]:  # 🏦 Sector Analysis
    render_section_header("🏦 Sector Performance Analysis")
    
    sector = data['sector']
    display_styled_dataframe(
        sector,
        columns_to_style=['Profit Growth FY25 (%)'],
        width='stretch',
        hide_index=True
    )
    
    render_divider()
    
    # Sector Positioning
    fig1 = px.scatter(
        sector,
        x='Revenue Growth FY25 (%)',
        y='Profit Growth FY25 (%)',
        size='Weight in Nifty (%)',
        color='Profit Growth FY25 (%)',
        hover_name='Sector',
        title='Sector Positioning: Revenue vs Profit',
        color_continuous_scale=['red', 'yellow', 'green'],
        template='plotly_white',
        height=CHART_HEIGHT
    )
    
    fig1.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Break-even")
    fig1.add_vline(x=7, line_dash="dash", line_color="gray", annotation_text="Nominal GDP")
    
    st.plotly_chart(fig1, width='stretch')
    
    render_divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig2 = go.Figure(data=[go.Pie(
            labels=sector['Sector'],
            values=sector['Weight in Nifty (%)'],
            title='Sector Weights'
        )])
        st.plotly_chart(fig2, width='stretch')
    
    with col2:
        render_subsection_header("🎯 Risk Assessment")
        
        # Find critical sectors
        crisis_sectors = sector[sector['Profit Growth FY25 (%)'] < -20]
        strong_sectors = sector[sector['Profit Growth FY25 (%)'] > 25]
        
        for _, row in crisis_sectors.iterrows():
            render_warning_box(
                f"<b>🔴 {row['Sector'].upper()}</b><br>"
                f"Profit: {row['Profit Growth FY25 (%)']:.1f}% | Weight: {row['Weight in Nifty (%)']:.0f}%"
            )
        
        for _, row in strong_sectors.iterrows():
            render_success_box(
                f"<b>🟢 {row['Sector'].upper()}</b><br>"
                f"Profit: {row['Profit Growth FY25 (%)']:.1f}% | Weight: {row['Weight in Nifty (%)']:.0f}%"
            )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: EARNINGS DOWNGRADES
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[4]:  # 📉 Earnings Downgrades
    render_section_header("📉 Earnings Downgrade Trajectory")
    
    downgrades = data['downgrades']
    display_styled_dataframe(
        downgrades,
        columns_to_style=['FY25 Profit Growth (%)'],
        width='stretch',
        hide_index=True
    )
    
    render_divider()
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=downgrades['Period'],
        y=downgrades['FY25 Profit Growth (%)'],
        mode='lines+markers+text',
        name='FY25 Estimate',
        line=dict(color=COLORS['accent_red'], width=3),
        marker=dict(size=12),
        text=[f"{v:.1f}%" for v in downgrades['FY25 Profit Growth (%)']],
        textposition="top center"
    ))
    
    fig.update_layout(
        title="FY2025 Profit Growth Estimate Revision",
        xaxis_title="Month",
        yaxis_title="Profit Growth (%)",
        template='plotly_white',
        height=CHART_HEIGHT,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, width='stretch')
    
    render_divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Sep 2024", "9.8%", "-67%")
    
    with col2:
        st.metric("Feb 2025", "3.2%", "Latest")
    
    with col3:
        st.metric("Duration", "5 Months", "Cascade")
    
    render_divider()
    render_subsection_header("⚠️ Downgrade Catalysts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_warning_box(
            "<b>Near-term Triggers (Oct-Nov):</b><br>"
            "1. Q2 earnings miss<br>"
            "2. Revenue slowdown 9.6%→6.6%<br>"
            "3. Cost pressures<br>"
            "4. Trade uncertainty"
        )
    
    with col2:
        render_warning_box(
            "<b>Deep-dive Triggers (Dec-Feb):</b><br>"
            "1. Energy crisis (-35%)<br>"
            "2. Margin ceiling identified<br>"
            "3. Consensus reset<br>"
            "4. Q3 confirms weakness"
        )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: SCENARIOS
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[5]:  # 🎯 Scenarios
    render_section_header("🎯 Scenario Analysis (FY25-FY27)")
    
    selected_scenario = st.radio(
        "Select Scenario:",
        list(scenarios.keys()),
        horizontal=True
    )
    
    scenario_data = scenarios[selected_scenario]
    nifty_path = nifty_levels[selected_scenario]
    
    render_divider()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**Assumption**")
        st.write(scenario_data['description'])
    
    with col2:
        st.markdown("**Earnings CAGR**")
        earnings_cagr = ((scenario_data['fy27_earnings'] / scenario_data['fy25_earnings']) ** (1/2) - 1) * 100
        st.metric("CAGR", f"{earnings_cagr:.1f}%")
    
    with col3:
        st.markdown("**Nifty Return**")
        ending_nifty = nifty_path[2] * 1000
        return_pa = ((ending_nifty / 23500) ** (1/3) - 1) * 100
        
        if "Bear" in selected_scenario:
            st.error(f"{return_pa:.1f}%")
        elif "Bull" in selected_scenario:
            st.success(f"{return_pa:.1f}%")
        else:
            st.warning(f"{return_pa:.1f}%")
    
    with col4:
        st.markdown("**Probability**")
        st.info(f"{scenario_data['probability']*100:.0f}%")
    
    render_divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = go.Figure()
        years = ['FY2025', 'FY2026', 'FY2027']
        earnings = [scenario_data['fy25_earnings'], scenario_data['fy26_earnings'], scenario_data['fy27_earnings']]
        
        fig1.add_trace(go.Scatter(
            x=years, y=earnings,
            mode='lines+markers+text',
            line=dict(color=scenario_data['color'], width=3),
            marker=dict(size=14),
            text=[f"{v:.1f}%" for v in earnings],
            textposition="top center"
        ))
        
        fig1.update_layout(
            title="Earnings Path",
            yaxis_title="Growth (%)",
            height=CHART_HEIGHT_SMALL,
            template='plotly_white'
        )
        st.plotly_chart(fig1, width='stretch')
    
    with col2:
        fig2 = go.Figure()
        
        fig2.add_trace(go.Scatter(
            x=years,
            y=nifty_path,
            mode='lines+markers+text',
            line=dict(color=scenario_data['color'], width=3),
            marker=dict(size=14),
            text=[f"{level:.0f}K" for level in nifty_path],
            textposition="top center"
        ))
        
        fig2.update_layout(
            title="Nifty Target",
            yaxis_title="Level (K)",
            height=CHART_HEIGHT_SMALL,
            template='plotly_white'
        )
        st.plotly_chart(fig2, width='stretch')

# ═══════════════════════════════════════════════════════════════════════════
# PAGE: DATA EXPLORER
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[6]:  # 📋 Data Explorer
    render_section_header("📋 Data Download & Exploration")
    
    data_option = st.selectbox(
        "Choose Dataset:",
        ["All Data", "5-Year Trend", "Quarterly Trends", "Sector Performance", "Earnings Downgrades"]
    )
    
    if data_option == "All Data":
        st.markdown("#### 📊 Complete Dataset Overview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📈 5-Year Performance")
            st.dataframe(data['five_year'], width='stretch', hide_index=True)
            csv = data['five_year'].to_csv(index=False)
            st.download_button(
                label="📥 Download 5-Year Data (CSV)",
                data=csv,
                file_name="5_year_nifty_data.csv",
                mime="text/csv"
            )
        
        with col2:
            st.markdown("##### 📊 Quarterly FY2025")
            st.dataframe(data['quarterly'], width='stretch', hide_index=True)
            csv = data['quarterly'].to_csv(index=False)
            st.download_button(
                label="📥 Download Quarterly Data (CSV)",
                data=csv,
                file_name="quarterly_fy25_data.csv",
                mime="text/csv"
            )
        
        render_divider()
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown("##### 🏦 Sector Analysis")
            st.dataframe(data['sector'], width='stretch', hide_index=True)
            csv = data['sector'].to_csv(index=False)
            st.download_button(
                label="📥 Download Sector Data (CSV)",
                data=csv,
                file_name="sector_analysis.csv",
                mime="text/csv"
            )
        
        with col4:
            st.markdown("##### 📉 Earnings Downgrades")
            st.dataframe(data['downgrades'], width='stretch', hide_index=True)
            csv = data['downgrades'].to_csv(index=False)
            st.download_button(
                label="📥 Download Downgrades (CSV)",
                data=csv,
                file_name="earnings_downgrades.csv",
                mime="text/csv"
            )
        
        render_divider()
        
        # Summary Statistics
        st.markdown("#### 📊 Data Summary")
        
        summary = {
            '📈 Analysis Periods': '5 Years (FY2021-FY2025 YTD)',
            '📅 Quarterly Data': '3 Quarters (Q1-Q3 FY2025)',
            '🏦 Sectors Analyzed': '10 major sectors',
            '📉 Downgrade Tracking': '6 months (Sep 2024 - Feb 2025)',
            '🎯 Scenarios Modeled': '3 scenarios (Bull/Base/Bear)',
            '📊 Total Data Points': '100+ metrics',
            '🔄 Data Updated': 'Feb 21, 2025',
            '⏱️ Cache Duration': '1 hour'
        }
        
        col1, col2, col3, col4 = st.columns(4)
        
        stats = list(summary.items())
        for i, (col, (label, value)) in enumerate(zip([col1, col2, col3, col4] * 2, stats)):
            with col:
                st.metric(label, value)
    
    elif data_option == "5-Year Trend":
        st.markdown("#### 📊 5-Year Performance Data")
        st.dataframe(data['five_year'], width='stretch', hide_index=True)
        
        csv = data['five_year'].to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="5_year_nifty_data.csv",
            mime="text/csv"
        )
    
    elif data_option == "Quarterly Trends":
        st.markdown("#### 📊 FY2025 Quarterly Data")
        st.dataframe(data['quarterly'], width='stretch', hide_index=True)
        
        csv = data['quarterly'].to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="quarterly_fy25_data.csv",
            mime="text/csv"
        )
    
    elif data_option == "Sector Performance":
        st.markdown("#### 🏦 Sector Analysis")
        st.dataframe(data['sector'], width='stretch', hide_index=True)
        
        csv = data['sector'].to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="sector_analysis.csv",
            mime="text/csv"
        )
    
    elif data_option == "Earnings Downgrades":
        st.markdown("#### 📉 Earnings Revision Tracking")
        st.dataframe(data['downgrades'], width='stretch', hide_index=True)
        
        csv = data['downgrades'].to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="earnings_downgrades.csv",
            mime="text/csv"
        )


# ═══════════════════════════════════════════════════════════════════════════
# PAGE: DATA SOURCES
# ═══════════════════════════════════════════════════════════════════════════

elif page == PAGES[7]:  # 📚 Data Sources
    render_section_header("📚 Data Sources & References")
    
    st.markdown("""
    This dashboard aggregates data from multiple authoritative sources to provide 
    comprehensive analysis of the Indian stock market. Below are the key data sources 
    used in this analysis with direct links.
    """)
    
    render_divider()
    
    # Primary Data Sources
    render_section_header("🏛️ Primary Data Sources")
    
    st.markdown("""
    These are the official government and market regulatory bodies providing 
    authoritative market data and corporate disclosures.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # NSE
        st.markdown("""
        #### 📊 [National Stock Exchange (NSE)](https://www.nseindia.com/)
        
        **Official Website:** https://www.nseindia.com/
        
        **Data Provided:**
        - Nifty 50 Index historical data
        - Company corporate actions
        - Real-time market data
        - Sector indices and weights
        - Historical performance metrics
        
        **Used For:** 5-year performance, sector weights, quarterly trends
        """)
        
        # RBI
        st.markdown("""
        #### 🏦 [Reserve Bank of India (RBI)](https://www.rbi.org.in/)
        
        **Official Website:** https://www.rbi.org.in/
        
        **Data Provided:**
        - Interest rate data
        - Monetary policy decisions
        - Economic indicators
        - Inflation metrics
        - Market surveys
        
        **Used For:** Economic context, policy environment, valuation assumptions
        """)
    
    with col2:
        # BSE
        st.markdown("""
        #### 📈 [Bombay Stock Exchange (BSE)](https://www.bseindia.com/)
        
        **Official Website:** https://www.bseindia.com/
        
        **Data Provided:**
        - Alternative market indices
        - Corporate disclosures
        - Market data and analytics
        - Sector indices
        
        **Used For:** Data validation, cross-checking, sector analysis
        """)
        
        # MCA
        st.markdown("""
        #### 📋 [Ministry of Corporate Affairs (MCA)](https://www.mca.gov.in/)
        
        **Official Website:** https://www.mca.gov.in/
        
        **Data Provided:**
        - Annual reports (Form 20-B)
        - Quarterly results (Form 20-B)
        - Corporate filings
        - Financial statements
        
        **Used For:** Earnings data, financial metrics, quarterly performance
        """)
    
    render_divider()
    
    # Research & Media Sources
    render_section_header("📰 Research & Media Sources")
    
    st.markdown("""
    These are leading financial news outlets and research houses providing 
    analysis, estimates, and market commentary.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 📰 [Business Standard](https://www.business-standard.com/)
        https://www.business-standard.com/
        
        • Earnings estimates
        • Market analysis
        • Company downgrades
        • Sector trends
        """)
        
        st.markdown("""
        #### 📰 [The Economic Times](https://economictimes.indiatimes.com/)
        https://economictimes.indiatimes.com/
        
        • Market updates
        • Company news
        • Economic reports
        • Policy analysis
        """)
    
    with col2:
        st.markdown("""
        #### 🏢 [Motilal Oswal](https://www.motilaloswal.com/)
        https://www.motilaloswal.com/
        
        • Equity research
        • Earnings forecasts
        • Sector analysis
        • Company ratings
        """)
        
        st.markdown("""
        #### 🏢 [ICICI Securities](https://research.icicisecurities.com/)
        https://research.icicisecurities.com/
        
        • Company analysis
        • Earnings revisions
        • Market insights
        • Stock recommendations
        """)
    
    with col3:
        st.markdown("""
        #### 🏢 [HDFC Securities](https://www.hdfcsec.com/)
        https://www.hdfcsec.com/
        
        • Investment research
        • Market outlook
        • Sector studies
        • Economic analysis
        """)
        
        st.markdown("""
        #### 🌐 [SEBI](https://www.sebi.gov.in/)
        https://www.sebi.gov.in/
        
        • Regulatory filings
        • Market circulars
        • Compliance data
        • Enforcement actions
        """)
    
    render_divider()
    
    # Global Research
    render_section_header("🌍 Global Research Houses")
    
    st.markdown("""
    International investment banks providing global perspective and 
    sophisticated analysis of Indian markets.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🏦 [Nomura](https://www.nomura.com/)
        https://www.nomura.com/
        
        **Global Investment Bank**
        
        • India equity research
        • Valuation analysis
        • Market forecasts
        • Sector research
        • Scenario modeling
        """)
    
    with col2:
        st.markdown("""
        #### 🏦 [Goldman Sachs](https://www.gs.com/)
        https://www.gs.com/
        
        **Global Investment Bank**
        
        • Market research
        • Economic analysis
        • Investment insights
        • Trend analysis
        • Risk assessment
        """)
    
    render_divider()
    
    # Data Collection Methodology
    render_section_header("📊 Data Collection Methodology")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_info_box("""
        **🔍 Data Validation Process**
        
        1. **Collection**: Data gathered from multiple sources
        2. **Verification**: Cross-checked across sources
        3. **Reconciliation**: Discrepancies resolved
        4. **Normalization**: Standardized formats
        5. **Validation**: Range and consistency checks
        6. **Documentation**: Source attribution
        """)
    
    with col2:
        render_success_box("""
        **✅ Data Quality Standards**
        
        ✓ **Accuracy**: Verified against official sources
        ✓ **Timeliness**: Updated monthly or quarterly
        ✓ **Completeness**: All required fields present
        ✓ **Consistency**: Cross-validated
        ✓ **Attribution**: All sources documented
        ✓ **Traceability**: Source links provided
        """)
    
    render_divider()
    
    # Data Timeline
    render_section_header("📅 Data Timeline & Updates")
    
    st.markdown("""
    | Data Type | Frequency | Latest | Source |
    |-----------|-----------|--------|--------|
    | **Nifty 50 Levels** | Real-time | Daily | NSE |
    | **Corporate Actions** | Event-based | Immediate | NSE/BSE |
    | **Quarterly Earnings** | Quarterly | Q3 FY2025 | MCA/Company websites |
    | **Sector Indices** | Daily | Daily | NSE/BSE |
    | **Research Estimates** | Monthly | Feb 2025 | Brokerages |
    | **Economic Data** | Monthly | Latest | RBI/Government |
    | **News & Analysis** | Daily | Real-time | Media sources |
    """)
    
    render_divider()
    
    # How to Access
    render_section_header("🔗 How to Access These Sources")
    
    st.markdown("""
    ### **For Real-Time Market Data:**
    1. Visit: https://www.nseindia.com/
    2. Navigate to: Market Data section
    3. Select: Indices → Nifty 50
    4. View: Historical data, daily updates
    
    ### **For Corporate Filings:**
    1. Visit: https://www.mca.gov.in/ (MCA Portal)
    2. Search: Company name
    3. View: Financial statements, annual reports
    4. Download: Official documents
    
    ### **For Research Reports:**
    1. Visit: Individual brokerage websites
    2. Navigate: Research/Reports section
    3. Search: Company or sector name
    4. Read: Latest analyst views and estimates
    
    ### **For Economic Context:**
    1. Visit: https://www.rbi.org.in/
    2. Navigate: Statistics and Publications
    3. View: Interest rates, inflation data
    4. Download: RBI research papers
    """)
    
    render_divider()
    
    # Data Disclaimer
    render_warning_box("""
    **📌 Important Disclaimer**
    
    • Data is aggregated from publicly available sources
    • While efforts are made to ensure accuracy, no guarantee is provided
    • Users should verify critical data points from original sources
    • This dashboard is for informational purposes only
    • Not financial advice - consult professionals for decisions
    • Sources may update their data; dashboard updated monthly
    • All sources and links are accurate as of: Feb 21, 2025
    """)
    
    render_divider()
    
    # Contact for data issues
    st.markdown("""
    ### 📞 Data Issues or Feedback?
    
    If you notice any data discrepancies or outdated information:
    - Verify the original source (links provided above)
    - Contact the respective organization
    - Report issues for dashboard improvement
    
    **Last Data Update:** Feb 21, 2025  
    **Next Expected Update:** March 21, 2025
    """)

# ═══════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════

render_divider()
render_footer(AUTHOR, BRAND_NAME, "NSE, RBI, BSE, MCA, SEBI | Research: Business Standard, Economic Times, Brokerages")

st.markdown(
    f"<p style='text-align:center; color:{COLORS['text_muted']}; font-size:0.85rem; margin-top:3rem;'>"
    f"<i>© 2026 The Mountain Path - World of Finance | All Rights Reserved</i>"
    f"</p>",
    unsafe_allow_html=True
)
