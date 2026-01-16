"""
Data Module - Data Preparation & Loading
Indian Market Analysis Dashboard
"""

import pandas as pd
import numpy as np
from config import BASE_EPS_FY24

# ═══════════════════════════════════════════════════════════════════════════
# 5-YEAR DATA
# ═══════════════════════════════════════════════════════════════════════════

def get_five_year_data() -> pd.DataFrame:
    """Get 5-year Nifty 50 performance data"""
    return pd.DataFrame({
        'Fiscal Year': ['FY2021', 'FY2022', 'FY2023', 'FY2024', 'FY2025 YTD'],
        'Revenue Growth (%)': [10.5, 15.4, 13.8, 10.7, 6.9],
        'EBITDA Growth (%)': [11.2, 22.8, 18.5, 14.3, 2.6],
        'PAT Growth (%)': [8.3, 25.7, 22.1, 16.8, 4.6],
        'EBITDA Margin (%)': [32.1, 33.5, 33.2, 33.0, 33.1],
        'PAT Margin (%)': [9.8, 10.4, 10.6, 10.5, 10.7]
    })

# ═══════════════════════════════════════════════════════════════════════════
# QUARTERLY DATA
# ═══════════════════════════════════════════════════════════════════════════

def get_quarterly_data() -> pd.DataFrame:
    """Get quarterly FY2025 performance data"""
    return pd.DataFrame({
        'Quarter': ['Q1FY25', 'Q2FY25', 'Q3FY25'],
        'Revenue Growth (%)': [9.6, 6.6, 4.5],
        'EBITDA Growth (%)': [9.4, 1.3, 6.9],
        'PAT Growth (%)': [0.8, -1.0, 9.5]
    })

# ═══════════════════════════════════════════════════════════════════════════
# SECTOR DATA
# ═══════════════════════════════════════════════════════════════════════════

def get_sector_data() -> pd.DataFrame:
    """Get sector performance data"""
    return pd.DataFrame({
        'Sector': ['Financials', 'Energy', 'IT', 'Industrials', 'Materials', 
                   'Consumer Disc.', 'Healthcare', 'Consumer Staples', 'Utilities', 'Telecom'],
        'Revenue Growth FY25 (%)': [12.3, 1.4, 7.0, 10.6, 1.7, 10.5, 7.6, 10.6, 7.5, 8.0],
        'Profit Growth FY25 (%)': [17.3, -35.4, 8.7, 25.7, -1.4, 6.6, 32.9, 6.1, -6.9, 95.9],
        'Weight in Nifty (%)': [35, 30, 9, 5, 11, 9, 3, 3, 3, 2],
        'Status': ['🟡 SLOWING', '🔴 CRISIS', '🟢 STABILIZING', '🟢 STRONG', 
                   '⚠️ MIXED', '⚠️ WEAKENING', '🟢 STRONG', '⚠️ MIXED', '⚠️ DECLINING', '🟢 EXCEPTIONAL']
    })

# ═══════════════════════════════════════════════════════════════════════════
# EARNINGS DOWNGRADE TRAJECTORY
# ═══════════════════════════════════════════════════════════════════════════

def get_downgrade_data() -> pd.DataFrame:
    """Get earnings downgrade trajectory"""
    return pd.DataFrame({
        'Date': ['Sep 30, 2024', 'Oct 31, 2024', 'Nov 30, 2024', 'Dec 31, 2024', 
                 'Jan 31, 2025', 'Feb 21, 2025'],
        'FY25 Profit Growth (%)': [9.8, 8.2, 5.8, 3.2, 4.9, 3.2]
    })

# ═══════════════════════════════════════════════════════════════════════════
# SCENARIO DATA
# ═══════════════════════════════════════════════════════════════════════════

def get_scenarios() -> dict:
    """Get scenario definitions"""
    return {
        'Base Case (50%)': {
            'description': 'Margin Resilience, Slow Revenue',
            'fy25_earnings': 5.5,
            'fy26_earnings': 11.0,
            'fy27_earnings': 12.5,
            'fy25_pe': 25.0,
            'fy26_pe': 24.5,
            'fy27_pe': 24.0,
            'color': '#FFA500',
            'probability': 0.50
        },
        'Bear Case (25%)': {
            'description': 'Margin Compression, Input Cost Spike',
            'fy25_earnings': 2.0,
            'fy26_earnings': 5.0,
            'fy27_earnings': 7.5,
            'fy25_pe': 23.0,
            'fy26_pe': 22.0,
            'fy27_pe': 21.5,
            'color': '#FF0000',
            'probability': 0.25
        },
        'Bull Case (25%)': {
            'description': 'Revenue Recovery + Margin Stability',
            'fy25_earnings': 9.0,
            'fy26_earnings': 14.0,
            'fy27_earnings': 15.5,
            'fy25_pe': 25.5,
            'fy26_pe': 26.0,
            'fy27_pe': 26.5,
            'color': '#00AA00',
            'probability': 0.25
        }
    }

# ═══════════════════════════════════════════════════════════════════════════
# NIFTY LEVEL CALCULATIONS
# ═══════════════════════════════════════════════════════════════════════════

def calculate_nifty_levels(scenarios: dict) -> dict:
    """Calculate Nifty 50 levels for each scenario"""
    nifty_levels = {}
    
    for scenario, data in scenarios.items():
        fy25_nifty = (BASE_EPS_FY24 * (1 + data['fy25_earnings']/100)) * data['fy25_pe']
        fy26_nifty = fy25_nifty * (1 + data['fy26_earnings']/100) * (data['fy26_pe']/data['fy25_pe'])
        fy27_nifty = fy26_nifty * (1 + data['fy27_earnings']/100) * (data['fy27_pe']/data['fy26_pe'])
        
        nifty_levels[scenario] = [fy25_nifty/1000, fy26_nifty/1000, fy27_nifty/1000]
    
    return nifty_levels

# ═══════════════════════════════════════════════════════════════════════════
# AGGREGATE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def get_all_data() -> dict:
    """Get all data at once"""
    scenarios = get_scenarios()
    
    return {
        'five_year': get_five_year_data(),
        'quarterly': get_quarterly_data(),
        'sector': get_sector_data(),
        'downgrades': get_downgrade_data(),
        'scenarios': scenarios,
        'nifty_levels': calculate_nifty_levels(scenarios)
    }

# ═══════════════════════════════════════════════════════════════════════════
# KEY METRICS
# ═══════════════════════════════════════════════════════════════════════════

def calculate_key_metrics() -> dict:
    """Calculate key metrics for dashboard"""
    five_year = get_five_year_data()
    quarterly = get_quarterly_data()
    
    # Revenue CAGR (FY2021-FY2025)
    revenue_cagr = ((6.9 / 10.5) ** (1/4) - 1) * 100 if 10.5 > 0 else 0
    
    # PAT CAGR
    pat_cagr = ((4.6 / 8.3) ** (1/4) - 1) * 100 if 8.3 > 0 else 0
    
    return {
        'revenue_cagr': revenue_cagr,
        'pat_cagr': pat_cagr,
        'current_rev_growth': quarterly.iloc[-1]['Revenue Growth (%)'],
        'current_pat_growth': quarterly.iloc[-1]['PAT Growth (%)'],
        'revenue_trend': 'Decelerating',
        'profit_trend': 'Margin Support',
        'divergence_factor': pat_cagr - revenue_cagr
    }

# ═══════════════════════════════════════════════════════════════════════════
# DATA VALIDATION
# ═══════════════════════════════════════════════════════════════════════════

def validate_data():
    """Validate all data sources"""
    try:
        five_year = get_five_year_data()
        quarterly = get_quarterly_data()
        sector = get_sector_data()
        downgrades = get_downgrade_data()
        scenarios = get_scenarios()
        
        assert len(five_year) == 5, "Five-year data should have 5 rows"
        assert len(quarterly) == 3, "Quarterly data should have 3 rows"
        assert len(sector) == 10, "Sector data should have 10 sectors"
        assert len(downgrades) == 6, "Downgrade data should have 6 data points"
        assert len(scenarios) == 3, "Should have 3 scenarios"
        
        return True, "All data validated successfully"
    except Exception as e:
        return False, f"Data validation error: {str(e)}"
