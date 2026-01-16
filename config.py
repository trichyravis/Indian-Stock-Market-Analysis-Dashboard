"""
Configuration Module - Indian Market Analysis Dashboard
Color Scheme: Mountain Path (Dark Blue & Gold)
"""

import streamlit as st
from typing import Dict

# ═══════════════════════════════════════════════════════════════════════════
# COLOR PALETTE - Mountain Path Theme
# ═══════════════════════════════════════════════════════════════════════════

COLORS = {
    'primary_dark': '#003366',      # Dark Blue (Main)
    'primary_mid': '#004d80',       # Medium Blue
    'primary_light': '#ADD8E6',     # Light Blue
    'accent_gold': '#FFD700',       # Gold
    'accent_red': '#CC0000',        # Red (Alerts)
    'accent_green': '#00AA00',      # Green (Positive)
    'accent_orange': '#FFA500',     # Orange (Neutral)
    'white': '#FFFFFF',
    'light_gray': '#f8f9fa',
    'medium_gray': '#666666',
    'chart_blue': '#0066CC',
}

# ═══════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

def configure_page():
    """Configure Streamlit page settings"""
    st.set_page_config(
        page_title="Indian Market Analysis: Revenue vs Margins",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "Indian Stock Market Analysis Dashboard\nCreated by Prof. V. Ravichandran\nThe Mountain Path - World of Finance"
        }
    )

# ═══════════════════════════════════════════════════════════════════════════
# CUSTOM CSS STYLING
# ═══════════════════════════════════════════════════════════════════════════

def apply_custom_css():
    """Apply Mountain Path branded CSS styling"""
    st.markdown(f"""
    <style>
        /* Main Background */
        .main {{
            background-color: {COLORS['light_gray']};
        }}
        
        /* Metric Cards */
        .metric-card {{
            background: {COLORS['white']};
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-left: 4px solid {COLORS['primary_dark']};
        }}
        
        /* Headers */
        .header-style {{
            color: {COLORS['primary_dark']};
            font-weight: bold;
            font-size: 24px;
            margin: 20px 0 10px 0;
        }}
        
        .subheader-style {{
            color: {COLORS['primary_mid']};
            font-weight: bold;
            font-size: 18px;
            margin: 15px 0 8px 0;
        }}
        
        /* Info/Alert Boxes */
        .info-box {{
            background-color: #E8F4F8;
            border-left: 4px solid {COLORS['primary_dark']};
            padding: 12px;
            border-radius: 4px;
        }}
        
        .alert-box {{
            background-color: #FFE8E8;
            border-left: 4px solid {COLORS['accent_red']};
            padding: 12px;
            border-radius: 4px;
        }}
        
        .success-box {{
            background-color: #E8F8E8;
            border-left: 4px solid {COLORS['accent_green']};
            padding: 12px;
            border-radius: 4px;
        }}
        
        /* Links */
        a {{
            color: {COLORS['primary_dark']};
        }}
        
        /* Divider */
        hr {{
            border: 1px solid {COLORS['primary_light']};
            margin: 20px 0;
        }}
    </style>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# THEME CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

STREAMLIT_THEME = {
    'primaryColor': COLORS['primary_dark'],
    'backgroundColor': COLORS['light_gray'],
    'secondaryBackgroundColor': COLORS['white'],
    'textColor': COLORS['medium_gray'],
    'font': 'sans serif'
}

# ═══════════════════════════════════════════════════════════════════════════
# NAVIGATION STRUCTURE
# ═══════════════════════════════════════════════════════════════════════════

PAGES = {
    '🏠 Overview': 'pages/01_overview.py',
    '📈 5-Year Trend': 'pages/02_five_year_trend.py',
    '📊 Quarterly Deep-Dive': 'pages/03_quarterly_analysis.py',
    '🏦 Sector Analysis': 'pages/04_sector_analysis.py',
    '📉 Earnings Downgrades': 'pages/05_earnings_downgrades.py',
    '🎯 Scenarios': 'pages/06_scenarios.py',
    '📋 Data Explorer': 'pages/07_data_explorer.py'
}

# ═══════════════════════════════════════════════════════════════════════════
# CHART CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

PLOTLY_CONFIG = {
    'responsive': True,
    'displayModeBar': True,
    'displaylogo': False,
    'modeBarButtonsToRemove': ['lasso2d'],
}

CHART_HEIGHT = 450
CHART_HEIGHT_SMALL = 350

# ═══════════════════════════════════════════════════════════════════════════
# DATA CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

BASE_EPS_FY24 = 920
CURRENT_NIFTY = 23000

# Scenario Probability Weights
SCENARIO_WEIGHTS = {
    'Base Case (50%)': 0.50,
    'Bear Case (25%)': 0.25,
    'Bull Case (25%)': 0.25
}

# ═══════════════════════════════════════════════════════════════════════════
# BRANDING
# ═══════════════════════════════════════════════════════════════════════════

BRAND_NAME = "The Mountain Path - World of Finance"
AUTHOR = "Prof. V. Ravichandran"
EXPERIENCE = "28+ Years Corporate Finance & Banking Experience, 10+ Years Academic Excellence"
LOCATION = "Bangalore, India"

# ═══════════════════════════════════════════════════════════════════════════
# DATA SOURCES
# ═══════════════════════════════════════════════════════════════════════════

DATA_SOURCES = {
    'primary': "NSE Corporate Performance Review (Q3FY25)",
    'secondary': ["RBI Annual Reports", "Business Standard"],
    'analysis_period': "FY2021 – FY2025",
    'created': "January 2026"
}
