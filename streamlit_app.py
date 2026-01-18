
"""
Indian Stock Market Analysis Dashboard
Analysis of Nifty 50 Growth: Revenue Expansion vs Margin Re-Rating
Version 2.5.0 - 9 Pages with "About This Research" Landing Page
Cache Buster: FORCE_REFRESH_PAGES_20250118_001
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
# MAIN PAGE HEADER
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("""
<div style="background-color: #003366; color: #FFD700; padding: 20px 20px; border-radius: 0; margin: -16px -16px 25px -16px; text-align: center;">
    <h1 style="margin: 0 0 8px 0; font-size: 24px; font-weight: 700;">
        📚 The Mountain Path - World of Finance
    </h1>
    <h2 style="margin: 0 0 8px 0; font-size: 24px; font-weight: 700; color: #FFD700;">
        Indian Stock Market Analysis: Nifty 50 (Year 2021-25) Growth Drivers & Sustainability
    </h2>
    <p style="margin: 0; font-size: 24px; font-weight: 700; color: #FFD700; letter-spacing: 0.5px;">
        Is profit growth driven by revenue expansion or margin expansion?
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar Radio Button Styling - Contrast Background
st.markdown("""
<style>
/* Sidebar container background */
section[data-testid="stSidebar"] {
    background-color: #F5F5F5 !important;
}

/* Radio button group container */
section[data-testid="stSidebar"] [role="radiogroup"] {
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
}

/* Individual radio button styling */
section[data-testid="stSidebar"] [role="radio"] {
    background-color: #FFFFFF !important;
    border: 2px solid #003366 !important;
    border-radius: 8px !important;
    padding: 12px 14px !important;
    margin: 4px 0 !important;
    font-weight: 600 !important;
    color: #003366 !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    display: flex !important;
    align-items: center !important;
}

/* Hover state - light blue background */
section[data-testid="stSidebar"] [role="radio"]:hover {
    background-color: #F0F7FF !important;
    border-color: #005599 !important;
    box-shadow: 0 2px 6px rgba(0, 51, 102, 0.15) !important;
}

/* Selected/Active radio button - dark blue background with white text */
section[data-testid="stSidebar"] [role="radio"][aria-checked="true"] {
    background: linear-gradient(135deg, #003366 0%, #005599 100%) !important;
    color: #FFFFFF !important;
    border-color: #003366 !important;
    box-shadow: 0 4px 12px rgba(0, 51, 102, 0.25) !important;
    font-weight: 700 !important;
}

/* Radio circle styling */
section[data-testid="stSidebar"] input[type="radio"] {
    accent-color: #003366 !important;
    cursor: pointer !important;
}

/* Selected radio circle white */
section[data-testid="stSidebar"] [aria-checked="true"] input[type="radio"] {
    accent-color: #FFFFFF !important;
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# SIDEBAR & NAVIGATION
# ═══════════════════════════════════════════════════════════════════════════

st.sidebar.markdown(f"# 📊 {BRAND_NAME}")
st.sidebar.markdown("---")
st.sidebar.markdown(f"**Prof. V. Ravichandran**")
st.sidebar.markdown(f"*{EXPERIENCE}*")
st.sidebar.markdown("---")

# Show all 8 pages with explicit list
pages_list = [
    "📚 About This Research",
    "🏠 Overview",
    "📈 5-Year Trend",
    "📊 Quarterly Deep-Dive",
    "🏦 Sector Analysis",
    "📉 Earnings Downgrades",
    "🎯 Scenarios",
    "📋 Data Explorer"
]

page = st.sidebar.radio(
    "📍 Choose Analysis:",
    pages_list,
    key="main_nav"
)

# Convert selected page string to index for comparison
page_index = pages_list.index(page) if page in pages_list else 0

st.sidebar.markdown("---")
st.sidebar.markdown(f"📍 {LOCATION} | {YEAR}")
st.sidebar.markdown("---")

# Social Links - Simplified
st.sidebar.markdown("""
**Connect with me:**

[LinkedIn Profile](https://www.linkedin.com/in/trichyravis)

[GitHub Profile](https://github.com/trichyravis)
""")

# ═══════════════════════════════════════════════════════════════════════════
# LOAD DATA
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data
def load_dashboard_data():
    return generate_data()

data = load_dashboard_data()

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 0: ABOUT THIS RESEARCH
# ═══════════════════════════════════════════════════════════════════════════

if page_index == 0:
    render_section_header("📚 About This Research Analysis")
    
    st.markdown("""
    **Indian Stock Market Analysis: Nifty 50 Growth Drivers & Sustainability**
    
    A comprehensive research dashboard analyzing the Nifty 50 index composition and performance drivers
    """)
    
    render_divider()
    
    # Research Objective
    render_subsection_header("🎯 Research Objective")
    
    render_info_box(
        "**Understanding Nifty 50 Growth Drivers**\n\n"
        "This analysis investigates whether the Nifty 50's impressive profit growth (19.8% CAGR) is driven by "
        "sustainable revenue expansion or unsustainable margin re-rating. By examining growth divergence, we identify "
        "critical inflection points and assess investment implications."
    )
    
    render_divider()
    
    # Key Research Questions
    render_subsection_header("❓ Key Research Questions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Primary Questions:**
        
        1. Is profit growth driven by revenue expansion or margin expansion?
        2. Are margins sustainable at current levels?
        3. What's the divergence between revenue and profit growth?
        4. Where are the inflection points in growth trajectory?
        5. What's the forward earnings outlook?
        """)
    
    with col2:
        st.markdown("""
        **Secondary Questions:**
        
        6. How are different sectors contributing to growth?
        7. What are analyst sentiment and revisions indicating?
        8. What are possible future scenarios?
        9. Which sectors are leading vs lagging?
        10. What's the sustainability score?
        """)
    
    render_divider()
    
    # Analysis Approach
    render_subsection_header("📊 Analysis Approach")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **1. Historical Analysis**
        
        • 5-year trend examination
        • Revenue & profit decomposition
        • Margin expansion analysis
        • Growth rate trajectory
        • Inflection point identification
        """)
    
    with col2:
        st.markdown("""
        **2. Current Performance**
        
        • FY2025 quarterly breakdown
        • Intra-year deceleration trends
        • Quarterly vs annual comparison
        • Momentum indicators
        • Performance sustainability
        """)
    
    with col3:
        st.markdown("""
        **3. Forward Analysis**
        
        • Analyst earnings revisions
        • Scenario-based projections
        • Multiple valuation models
        • Risk assessment
        • Investment recommendations
        """)
    
    render_divider()
    
    # What You Can Explore
    render_subsection_header("🔍 What You Can Explore Using This Dashboard")
    
    st.markdown("""
    This dashboard provides 7 comprehensive analysis sections:
    """)
    
    analysis_info = {
        "1️⃣ Overview": {
            "content": "Executive summary of Nifty 50 growth dynamics with key metrics, "
                      "divergence analysis, margin breakdown, and investment recommendations. "
                      "Perfect for understanding the big picture.",
            "key_insights": "Growth divergence, margin limits, sustainability concerns"
        },
        "2️⃣ 5-Year Trend": {
            "content": "Comprehensive 5-year performance analysis showing revenue vs profit growth trends, "
                      "margin evolution, and growth divergence patterns. Includes historical data and analysis.",
            "key_insights": "Revenue deceleration, profit CAGR divergence, margin expansion limits"
        },
        "3️⃣ Quarterly Deep-Dive": {
            "content": "FY2025 quarterly performance breakdown with annual vs quarterly comparison. "
                      "Shows the sharp deceleration within the fiscal year with detailed metrics.",
            "key_insights": "Quarterly deceleration, intra-year trends, momentum shifts"
        },
        "4️⃣ Sector Analysis": {
            "content": "Top 10 sectors contributing to Nifty 50 with their growth rates, index weights, "
                      "and performance status. Identify sector-specific opportunities and risks.",
            "key_insights": "Sector contribution, growth heterogeneity, diversification insights"
        },
        "5️⃣ Earnings Downgrades": {
            "content": "6-month analyst earnings revision trend showing consensus changes. "
                      "Track the dramatic 67% downgrade from 9.8% to 3.2% in profit growth expectations.",
            "key_insights": "Analyst sentiment, consensus shifts, earnings risk, forecast reliability"
        },
        "6️⃣ Scenarios": {
            "content": "Three investment scenarios (Base/Bear/Bull) with earnings projections, "
                      "valuation multiples, and Nifty targets. Interactive scenario selector with probability-weighted analysis.",
            "key_insights": "Risk scenarios, valuation ranges, target price calculations"
        },
        "7️⃣ Data Explorer": {
            "content": "Interactive tabbed interface to explore all underlying datasets with comprehensive "
                      "documentation on data sources, methodology, and metric definitions.",
            "key_insights": "Raw data access, source transparency, calculation verification"
        }
    }
    
    for title, info in analysis_info.items():
        with st.expander(f"**{title}**", expanded=False):
            st.markdown(f"**Description:** {info['content']}")
            st.markdown(f"\n**Key Insights:** {info['key_insights']}")
    
    render_divider()
    
    # Data Sources
    render_subsection_header("📋 Data Sources & Reliability")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Primary Data Sources:**
        
        • NSE (National Stock Exchange) - Official index data
        • RBI (Reserve Bank of India) - Macro indicators
        • BSE (Bombay Stock Exchange) - Sector analysis
        • SEBI (Securities & Exchange Board) - Regulatory data
        • Company Financial Statements - Audited reports
        """)
    
    with col2:
        st.markdown("""
        **Secondary Sources:**
        
        • Business Standard - Market analysis
        • Economic Times - Business news
        • Brokerage Research - Institutional forecasts
        • MCA Filings - Corporate disclosures
        • Stock Exchange Reports - Official data
        """)
    
    render_divider()
    
    # Who Should Use This
    render_subsection_header("👥 Who Should Use This Dashboard?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        render_success_box(
            "**Portfolio Managers**\n\n"
            "✓ Index rebalancing decisions\n"
            "✓ Sector allocation insights\n"
            "✓ Risk assessment\n"
            "✓ Growth trend analysis"
        )
    
    with col2:
        render_warning_box(
            "**Equity Analysts**\n\n"
            "⚠️ Earnings forecast validation\n"
            "⚠️ Sector performance tracking\n"
            "⚠️ Growth divergence analysis\n"
            "⚠️ Valuation benchmarking"
        )
    
    with col3:
        render_info_box(
            "**Individual Investors**\n\n"
            "ℹ️ Market trend understanding\n"
            "ℹ️ Growth sustainability assessment\n"
            "ℹ️ Scenario planning\n"
            "ℹ️ Data-driven decision making"
        )
    
    render_divider()
    
    # Key Findings Preview
    render_subsection_header("🔑 Key Findings (Preview)")
    
    findings = {
        "Revenue Growth": "Decelerating from 15.4% (FY22) to 6.9% (FY25)",
        "Profit Growth": "Higher but vulnerable at 4.6% (FY25)",
        "CAGR Divergence": "Profit 15.5% vs Revenue 9.2% (unsustainable)",
        "Margin Status": "Expansion complete, now facing limits",
        "Earnings Revisions": "Dramatic 67% downgrade in 6 months",
        "Analyst Sentiment": "Shifting from optimistic to cautious",
        "Sector Concentration": "Financials 35% + Energy 30% = 65% of index",
        "Investment Implication": "Revenue recovery critical for profit sustainability"
    }
    
    for key, value in findings.items():
        st.markdown(f"**{key}:** {value}")
    
    render_divider()
    
    # Navigation Guide
    render_subsection_header("🧭 How to Navigate This Dashboard")
    
    st.markdown("""
    **Recommended Analysis Path:**
    
    1. **Start Here** (📚 About This Research) - Understand objectives and context
    2. **Overview** (🏠) - Get executive summary of key findings
    3. **5-Year Trend** (📈) - Understand historical context and patterns
    4. **Quarterly Deep-Dive** (📊) - See current deceleration in detail
    5. **Sector Analysis** (🏦) - Identify sector-specific risks/opportunities
    6. **Earnings Downgrades** (📉) - Assess analyst sentiment and revisions
    7. **Scenarios** (🎯) - Explore future possibilities and valuations
    8. **Data Explorer** (📋) - Verify sources and explore raw data
    
    **Or jump directly to sections most relevant to your questions!**
    """)
    
    render_divider()
    
    # Investment Perspective
    render_subsection_header("💡 Investment Perspective")
    
    render_info_box(
        "**Critical Insight:**\n\n"
        "The Nifty 50 has benefited from impressive profit growth (19.8% CAGR FY21-25), but this masks a concerning reality: "
        "profit growth is decelerating faster than revenue growth, indicating margin expansion is losing steam. With revenue growth "
        "down to 6.9% and analysts cutting profit forecasts by 67%, the index faces a critical inflection point. "
        "\n\nInvestors must focus on revenue recovery and sector-specific opportunities rather than relying on broad-based margin expansion. "
        "The dashboard provides comprehensive analysis tools to navigate this transition."
    )

elif page_index == 1:
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
# PAGE 2: 5-YEAR TREND
# ═══════════════════════════════════════════════════════════════════════════

elif page_index == 2:
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
    
    # COMPREHENSIVE SUMMARY
    render_subsection_header("📋 5-Year Performance Summary")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Revenue Growth Story**
        
        - FY21: 10.5%
        - FY22: 15.4% (Peak)
        - FY23: 13.8%
        - FY24: 10.7%
        - FY25: 6.9% ⬇️
        
        **CAGR: 9.2%**
        
        **Trend:** Consistent deceleration
        """)
    
    with col2:
        st.markdown("""
        **Profit Growth Story**
        
        - FY21: 8.3%
        - FY22: 25.7% (Peak)
        - FY23: 22.1%
        - FY24: 16.8%
        - FY25: 4.6% ⬇️
        
        **CAGR: 15.5%**
        
        **Trend:** Sharper decline than revenue
        """)
    
    with col3:
        st.markdown("""
        **Margin Story**
        
        - EBITDA: 32.1% → 33.1% (stable)
        - PAT: 9.8% → 10.7% (slight gain)
        
        **Peak:** FY22 EBITDA 33.5%
        
        **Status:** Margin expansion phase over
        """)
    
    render_divider()
    
    # Key Insights
    render_subsection_header("🔍 Key Findings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_success_box(
            "**FY2021-2024: Strong Performance**\n\n"
            "✅ Revenue CAGR: 12.6% (FY21-24)\n"
            "✅ Profit CAGR: 18.6% (FY21-24)\n"
            "✅ Margin expansion: +140 bps\n"
            "✅ Dual drivers: Volume + Margin"
        )
    
    with col2:
        render_warning_box(
            "**FY2025: Inflection Point**\n\n"
            "⚠️ Revenue growth slows: 6.9%\n"
            "⚠️ Profit growth halves: 4.6%\n"
            "⚠️ Margin gains plateau\n"
            "❌ Profit growth now dependent on revenue"
        )
    
    render_divider()
    
    # Growth Divergence Analysis
    render_subsection_header("📊 Growth Divergence Analysis")
    
    divergence_data = pd.DataFrame({
        'Fiscal Year': five_year['Fiscal Year'],
        'Revenue Growth %': five_year['Revenue Growth (%)'].round(1),
        'Profit Growth %': five_year['PAT Growth (%)'].round(1),
        'Divergence (pts)': (five_year['PAT Growth (%)'] - five_year['Revenue Growth (%)']).round(1),
        'Driver': ['Vol+Mar', 'Vol+Mar', 'Vol+Mar', 'Vol+Mar', 'Margin']
    })
    
    display_styled_dataframe(
        divergence_data,
        width='stretch'
    )
    
    render_divider()
    
    # Investment Perspective
    render_subsection_header("💼 Investment Conclusion")
    
    render_info_box(
        "**5-Year Analysis Verdict**\n\n"
        "The Nifty 50 demonstrated strong operational leverage through FY21-FY24, with profit growth (15.5% CAGR) significantly "
        "outpacing revenue growth (9.2% CAGR). However, FY2025 marks an inflection point where profit growth (4.6%) has collapsed "
        "disproportionately to revenue deceleration (6.9%), signaling margin expansion limits. \n\n"
        "**Going Forward:** Investors should monitor revenue growth closely as further revenue deceleration will directly impact "
        "profitability given margin headrooms are exhausted. The current valuation may not adequately price this transition risk."
    )
    
    render_divider()
    
    # Full Data Table
    render_subsection_header("📈 Complete 5-Year Data")
    
    display_styled_dataframe(
        five_year,
        columns_to_style=['Revenue Growth (%)', 'EBITDA Growth (%)', 'PAT Growth (%)'],
        width='stretch',
        hide_index=True
    )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 2: QUARTERLY DEEP-DIVE
# ═══════════════════════════════════════════════════════════════════════════

elif page_index == 3:
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

elif page_index == 4:
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

elif page_index == 5:
    render_section_header("📉 6-Month Earnings Revision Trend")
    
    st.markdown("""
    **Analysis Period:** Sep 2024 - Feb 2025  
    **Focus:** FY2025 Profit Growth Revisions
    """)
    
    render_divider()
    
    downgrades = data['downgrades']
    
    # Display data table
    render_subsection_header("📊 Earnings Revision History")
    display_styled_dataframe(
        downgrades,
        width='stretch',
        hide_index=True
    )
    
    render_divider()
    
    # Key Metrics
    render_subsection_header("📈 Revision Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Latest Estimate", f"{downgrades.iloc[-1]['FY25 Profit Growth (%)']:.1f}%", delta="Current")
    with col2:
        st.metric("Highest Estimate", f"{downgrades['FY25 Profit Growth (%)'].max():.1f}%", delta="Sep 2024")
    with col3:
        st.metric("Lowest Estimate", f"{downgrades['FY25 Profit Growth (%)'].min():.1f}%", delta="Recent")
    with col4:
        total_revision = downgrades['FY25 Profit Growth (%)'].iloc[0] - downgrades['FY25 Profit Growth (%)'].iloc[-1]
        st.metric("Total Revision", f"{total_revision:.1f}%", delta="Downgrade")
    
    render_divider()
    
    # Revision Trend Chart
    render_subsection_header("📉 Revision Trend Over Time")
    
    fig = go.Figure()
    
    # Create x-axis positions
    x_pos = list(range(len(downgrades)))
    date_labels = downgrades['Date'].tolist()
    
    # Revision line
    fig.add_trace(go.Scatter(
        x=x_pos,
        y=downgrades['FY25 Profit Growth (%)'],
        mode='lines+markers',
        name='FY25 Profit Growth Estimate',
        line=dict(color=COLORS['accent_red'], width=4),
        marker=dict(size=12, symbol='circle'),
        fill='tozeroy',
        fillcolor='rgba(255, 0, 0, 0.1)',
        text=date_labels,
        hovertemplate='<b>%{text}</b><br>Estimate: %{y:.1f}%<extra></extra>'
    ))
    
    fig.update_layout(
        title="FY2025 Profit Growth Estimate Revision",
        xaxis_title="Revision Date",
        yaxis_title="FY25 Profit Growth (%)",
        xaxis=dict(
            ticktext=date_labels,
            tickvals=x_pos,
            tickangle=-45
        ),
        template='plotly_white',
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    render_divider()
    
    # Analysis Boxes
    render_subsection_header("🔍 Revision Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_warning_box(
            "**Downgrade Trend**\n\n"
            "• Sep 2024: 9.8% (Initial estimate)\n"
            "• Dec 2024: 3.2% (Sharp decline)\n"
            "• Feb 2025: 3.2% (Stabilized)\n\n"
            "**Observation:** 67% downgrade in 6 months"
        )
    
    with col2:
        render_info_box(
            "**What This Means**\n\n"
            "• Analysts have cut profit growth expectations significantly\n"
            "• Recent estimates stable (suggesting capitulation)\n"
            "• Current estimate: 3.2% (down from 9.8%)\n"
            "• Risk: Further downgrades possible if revenue weakens"
        )
    
    render_divider()
    
    # Monthly Revision Rates
    render_subsection_header("📋 Monthly Revision Details")
    
    revision_data = pd.DataFrame({
        'Date': downgrades['Date'],
        'Period': downgrades['Period'],
        'FY25 Profit Growth %': downgrades['FY25 Profit Growth (%)'].round(1),
        'Revision from Previous': [
            '-',
            f"{downgrades.iloc[1]['FY25 Profit Growth (%)'] - downgrades.iloc[0]['FY25 Profit Growth (%)']:.1f}%",
            f"{downgrades.iloc[2]['FY25 Profit Growth (%)'] - downgrades.iloc[1]['FY25 Profit Growth (%)']:.1f}%",
            f"{downgrades.iloc[3]['FY25 Profit Growth (%)'] - downgrades.iloc[2]['FY25 Profit Growth (%)']:.1f}%",
            f"{downgrades.iloc[4]['FY25 Profit Growth (%)'] - downgrades.iloc[3]['FY25 Profit Growth (%)']:.1f}%",
            f"{downgrades.iloc[5]['FY25 Profit Growth (%)'] - downgrades.iloc[4]['FY25 Profit Growth (%)']:.1f}%"
        ]
    })
    
    display_styled_dataframe(
        revision_data,
        width='stretch'
    )
    
    render_divider()
    
    # Investment Perspective
    render_subsection_header("💼 Investment Perspective")
    
    render_info_box(
        "**Key Takeaway**\n\n"
        "The dramatic downgrade from 9.8% to 3.2% reflects deteriorating profit growth expectations. "
        "While the recent stabilization suggests consensus has been reached, the current 3.2% estimate is concerning given: "
        "(1) Revenue growth declining to 6.9%, (2) Margin expansion limits, (3) Lack of operational catalysts. "
        "Monitor Q3 results closely—further deterioration could trigger additional downgrades."
    )

# ═══════════════════════════════════════════════════════════════════════════
# PAGE 5: SCENARIOS
# ═══════════════════════════════════════════════════════════════════════════

elif page_index == 6:
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

elif page_index == 7:
    render_section_header("📋 Data Explorer")
    
    st.markdown("""
    **All Datasets - Interactive View**
    
    Access complete datasets for all analysis sections. Each tab contains detailed performance metrics and calculations.
    """)
    
    render_divider()
    
    # Custom CSS for tab styling - Simplified approach
    st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] button {
        background-color: #E8EDEF !important;
        border: 2px solid #003366 !important;
        border-radius: 6px !important;
        padding: 12px 20px !important;
        margin-right: 10px !important;
        font-weight: 600 !important;
        color: #003366 !important;
        font-size: 14px !important;
    }
    
    .stTabs [data-baseweb="tab-list"] button:hover {
        background-color: #D0D8E8 !important;
        border-color: #005599 !important;
    }
    
    .stTabs [data-baseweb="tab-list"] [aria-selected="true"] {
        background-color: #003366 !important;
        color: #FFFFFF !important;
        border-color: #003366 !important;
    }
    
    .stTabs [data-baseweb="tab-panel"] {
        padding: 20px !important;
        background-color: #F8FAFB !important;
        border-radius: 8px !important;
        border-left: 5px solid #003366 !important;
        margin-top: 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📈 5-Year", "📊 Quarterly", "🏢 Sectors", "📉 Downgrades", "📝 Data Notes", "📥 Downloads"])
    
    with tab1:
        render_subsection_header("📈 5-Year Performance Data")
        st.markdown("""
        **Coverage:** FY2021 to FY2025 YTD
        
        **Metrics Included:**
        - Revenue Growth (%) - Year-on-year revenue growth rate
        - EBITDA Growth (%) - Year-on-year EBITDA growth rate
        - PAT Growth (%) - Year-on-year Profit After Tax growth rate
        - EBITDA Margin (%) - EBITDA as percentage of revenue
        - PAT Margin (%) - PAT as percentage of revenue
        
        **Use Case:** Analyze 5-year trends, identify inflection points, assess margin evolution
        """)
        display_styled_dataframe(data['five_year'], width='stretch', hide_index=True)
    
    with tab2:
        render_subsection_header("📊 Quarterly Performance Data")
        st.markdown("""
        **Coverage:** Q1 FY2025 to Q3 FY2025
        
        **Metrics Included:**
        - Quarter - Quarter designation (Q1FY25, Q2FY25, Q3FY25)
        - Revenue Growth (%) - Quarterly revenue growth
        - EBITDA Growth (%) - Quarterly EBITDA growth
        - PAT Growth (%) - Quarterly profit after tax growth
        
        **Use Case:** Analyze intra-year deceleration trends, identify seasonal patterns, assess quarterly momentum
        """)
        display_styled_dataframe(data['quarterly'], width='stretch', hide_index=True)
    
    with tab3:
        render_subsection_header("🏢 Sector Performance Data")
        st.markdown("""
        **Coverage:** Top 10 sectors in Nifty 50
        
        **Metrics Included:**
        - Sector - Sector name within Nifty 50 index
        - Revenue Growth FY25 (%) - FY2025 revenue growth by sector
        - Profit Growth FY25 (%) - FY2025 profit growth by sector
        - Weight in Nifty (%) - Sector's contribution to index
        - Status - Performance status indicator (Strong, Stabilizing, Slowing, Crisis, Mixed)
        
        **Use Case:** Identify sector-specific trends, assess diversification, spot sector strength/weakness
        """)
        display_styled_dataframe(data['sector'], width='stretch', hide_index=True)
    
    with tab4:
        render_subsection_header("📉 Earnings Revision Data")
        st.markdown("""
        **Coverage:** 6-month earnings revision history (Sep 2024 - Feb 2025)
        
        **Metrics Included:**
        - Date - Revision date
        - Period - Month designation
        - FY25 Profit Growth (%) - Current analyst estimate for FY25 profit growth
        
        **Use Case:** Track analyst sentiment shifts, identify consensus changes, assess earnings risk
        """)
        display_styled_dataframe(data['downgrades'], width='stretch', hide_index=True)
    
    with tab5:
        render_subsection_header("📝 Data Documentation & Sources")
        
        st.markdown("**Data Collection & Methodology**")
        st.markdown("""
        All data presented in this dashboard is compiled from official and verified sources. 
        Below is comprehensive documentation of data collection methodology and sources.
        """)
        
        render_divider()
        
        st.markdown("**1. NIFTY 50 PERFORMANCE DATA**")
        st.markdown("""
        Source: National Stock Exchange (NSE), Reserve Bank of India (RBI)
        
        Collection Method:
        - Annual performance data (FY2021-2025) extracted from NSE official database
        - Revenue and profit figures sourced from consolidated financial statements
        - Growth rates calculated as year-on-year percentage changes
        - Margin data calculated from audited financial statements
        
        Frequency: Annual (with YTD for current fiscal year)
        Reliability: High - Official stock exchange and RBI data
        """)
        
        render_divider()
        
        st.markdown("**2. QUARTERLY PERFORMANCE DATA**")
        st.markdown("""
        Source: NSE, Stock Exchange Filings, Company Reports
        
        Collection Method:
        - Quarterly results compiled from official NSE filings
        - Extracted from Nifty 50 constituent quarterly reports
        - Growth rates calculated on quarter-on-quarter basis
        - Data represents FY2025 performance (Q1-Q3)
        
        Frequency: Quarterly
        Reliability: High - Official quarterly reports and filings
        """)
        
        render_divider()
        
        st.markdown("**3. SECTOR ANALYSIS DATA**")
        st.markdown("""
        Source: BSE (Bombay Stock Exchange), Sectoral Index Reports
        
        Collection Method:
        - Sector-wise breakdown derived from Nifty 50 constituents
        - Weight percentages calculated from market capitalization
        - Growth rates aggregated from sector index performance
        - Status indicators based on comparative performance analysis
        
        Frequency: Monthly review
        Reliability: High - Official BSE data and index calculation methodology
        """)
        
        render_divider()
        
        st.markdown("**4. EARNINGS REVISION DATA**")
        st.markdown("""
        Source: SEBI (Securities and Exchange Board of India), Brokerage Research Aggregates
        
        Collection Method:
        - Earnings revision history compiled from analyst consensus estimates
        - Data spans 6-month rolling average of forecasts
        - Profit growth estimates for FY25 tracked from Sep 2024 onwards
        - Sources include major brokerages and institutional research teams
        
        Frequency: Monthly tracking
        Reliability: Medium-High - Aggregated analyst estimates subject to volatility
        """)
        
        render_divider()
        
        st.markdown("**5. RESEARCH SOURCES**")
        st.markdown("""
        Analysis Framework Based On:
        - Business Standard - Daily market analysis and corporate reporting
        - Economic Times - Macro trends and business news
        - Brokerage Research - Institutional equity research and forecasts
        - SEBI Filings - Official regulatory disclosures
        
        Secondary Sources:
        - MCA (Ministry of Corporate Affairs) - Company regulatory filings
        - RBI Publications - Macroeconomic data and policy indicators
        - NSE Research - Technical analysis and trading data
        """)
        
        render_divider()
        
        st.markdown("**6. DATA QUALITY & LIMITATIONS**")
        st.markdown("""
        Data Quality Assurance:
        - All data sourced from official government and exchange databases
        - Cross-verified against multiple sources where applicable
        - Annual figures audited and officially published
        - Quarterly data from official stock exchange filings
        
        Known Limitations:
        - FY2025 is year-to-date; final annual figures may differ
        - Quarterly data represents 9-month snapshot (Q1-Q3)
        - Sector classifications based on NSE standard definitions
        - Analyst estimates subject to revision and consensus changes
        - Margin calculations based on consolidated financial statements
        
        Data Currency:
        - Last Updated: February 2025
        - Update Frequency: Monthly during fiscal year
        - Historical data: FY2021 onwards
        """)
        
        render_divider()
        
        st.markdown("**7. METRIC DEFINITIONS**")
        st.markdown("""
        Growth Rates (Year-on-Year):
        - Revenue Growth % = (Current Year Revenue - Prior Year Revenue) / Prior Year Revenue * 100
        - Profit Growth % = (Current Year PAT - Prior Year PAT) / Prior Year PAT * 100
        - EBITDA Growth % = (Current Year EBITDA - Prior Year EBITDA) / Prior Year EBITDA * 100
        
        Margins (Percentage of Revenue):
        - EBITDA Margin % = (EBITDA / Revenue) * 100
        - PAT Margin % = (PAT / Revenue) * 100
        
        Index Weight:
        - Weight in Nifty % = (Sector Market Cap / Total Nifty 50 Market Cap) * 100
        
        Earnings Estimates:
        - FY25 Profit Growth % = Consensus analyst estimate for FY25 PAT growth rate
        """)
        
        render_divider()
        
        st.markdown("**8. DISCLAIMERS & IMPORTANT NOTES**")
        st.markdown("""
        - This dashboard presents historical and current data for informational purposes only
        - Projections and estimates are subject to market volatility and unforeseen events
        - Past performance does not guarantee future results
        - Data is compiled from publicly available sources; accuracy not guaranteed
        - For investment decisions, consult with qualified financial advisors
        - All data presented as of February 2025; check sources for latest updates
        - Quarterly estimates are preliminary; subject to revision with final results
        """)
    
    with tab6:
        render_subsection_header("📥 Download All Datasets")
        
        st.markdown("""
        **Download all analysis datasets in CSV format for external analysis, modeling, or integration with your tools.**
        """)
        
        render_divider()
        
        # Create downloadable datasets
        five_year_df = data['five_year']
        quarterly_df = data['quarterly']
        sectors_df = data['sector']
        downgrades_df = data['downgrades']
        
        # Convert to CSV
        five_year_csv = five_year_df.to_csv(index=False)
        quarterly_csv = quarterly_df.to_csv(index=False)
        sectors_csv = sectors_df.to_csv(index=False)
        downgrades_csv = downgrades_df.to_csv(index=False)
        
        # Download buttons in columns
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📈 5-Year Performance Data**")
            st.markdown(f"*Records: {len(five_year_df)} | Metrics: {len(five_year_df.columns)}*")
            st.download_button(
                label="📥 Download 5-Year Data (CSV)",
                data=five_year_csv,
                file_name="nifty50_5year_performance.csv",
                mime="text/csv",
                key="download_5year"
            )
        
        with col2:
            st.markdown("**📊 Quarterly Performance Data**")
            st.markdown(f"*Records: {len(quarterly_df)} | Metrics: {len(quarterly_df.columns)}*")
            st.download_button(
                label="📥 Download Quarterly Data (CSV)",
                data=quarterly_csv,
                file_name="nifty50_quarterly_performance.csv",
                mime="text/csv",
                key="download_quarterly"
            )
        
        st.markdown("---")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown("**🏢 Sector Analysis Data**")
            st.markdown(f"*Records: {len(sectors_df)} | Metrics: {len(sectors_df.columns)}*")
            st.download_button(
                label="📥 Download Sector Data (CSV)",
                data=sectors_csv,
                file_name="nifty50_sector_analysis.csv",
                mime="text/csv",
                key="download_sectors"
            )
        
        with col4:
            st.markdown("**📉 Earnings Revisions Data**")
            st.markdown(f"*Records: {len(downgrades_df)} | Metrics: {len(downgrades_df.columns)}*")
            st.download_button(
                label="📥 Download Earnings Revisions (CSV)",
                data=downgrades_csv,
                file_name="nifty50_earnings_revisions.csv",
                mime="text/csv",
                key="download_downgrades"
            )
        
        st.markdown("---")
        
        render_subsection_header("📦 Combined Download")
        
        st.markdown("""
        **Download all datasets combined into a single CSV file**
        """)
        
        # Create combined dataset
        combined_data = {
            'Dataset Type': [],
            'Data': []
        }
        
        all_datasets = {
            '5-Year Performance': five_year_df,
            'Quarterly Performance': quarterly_df,
            'Sector Analysis': sectors_df,
            'Earnings Revisions': downgrades_df
        }
        
        combined_text = "=== NIFTY 50 ANALYSIS DASHBOARD - COMPLETE DATA EXPORT ===\n"
        combined_text += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        combined_text += "=" * 70 + "\n\n"
        
        for dataset_name, df in all_datasets.items():
            combined_text += f"\n{'='*70}\n"
            combined_text += f"{dataset_name.upper()}\n"
            combined_text += f"{'='*70}\n"
            combined_text += df.to_csv(index=False)
            combined_text += "\n"
        
        st.download_button(
            label="📥 Download All Data Combined (TXT)",
            data=combined_text,
            file_name="nifty50_complete_analysis_export.txt",
            mime="text/plain",
            key="download_combined"
        )
        
        st.markdown("---")
        
        render_subsection_header("ℹ️ Download Information")
        
        st.markdown("""
        **Available Formats:**
        - Individual datasets: CSV format (recommended for data analysis tools)
        - Combined export: TXT format (for quick reference)
        
        **Files Include:**
        - All historical performance data
        - Quarterly analysis metrics
        - Sector-wise breakdown
        - Analyst earnings revisions
        
        **Usage:**
        - Import into Excel, Python, R, Power BI, Tableau
        - Conduct custom analysis
        - Build predictive models
        - Create custom visualizations
        - Integration with data pipelines
        
        **File Naming Convention:**
        - `nifty50_5year_performance.csv` - 5-year historical data
        - `nifty50_quarterly_performance.csv` - Quarterly FY2025 data
        - `nifty50_sector_analysis.csv` - Top 10 sector contribution
        - `nifty50_earnings_revisions.csv` - 6-month analyst revisions
        - `nifty50_complete_analysis_export.txt` - All data combined
        """)

# ═══════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════

st.markdown("---")
render_footer(AUTHOR, BRAND_NAME, "NSE, RBI, BSE, MCA, SEBI | Research: Business Standard, Economic Times, Brokerages")
