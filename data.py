
"""
Data Module - Data Preparation & Loading
Indian Stock Market Analysis Dashboard

Comprehensive data management with:
- Data generation and caching
- Validation and error handling
- Scenario calculations
- Key metrics computation
"""

import pandas as pd
import numpy as np
import streamlit as st
from typing import Dict, Tuple

# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════

# Base earnings per share for Nifty 50 (FY2024)
BASE_EPS_FY24 = 2150

# Cache TTL (1 hour)
CACHE_TTL = 3600

# ═══════════════════════════════════════════════════════════════════════════
# 5-YEAR HISTORICAL DATA
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data(ttl=CACHE_TTL)
def get_five_year_data() -> pd.DataFrame:
    """
    Get 5-year Nifty 50 performance data (FY2021-FY2025 YTD)
    
    Returns:
        pd.DataFrame: Historical performance metrics
    """
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

@st.cache_data(ttl=CACHE_TTL)
def get_quarterly_data() -> pd.DataFrame:
    """
    Get quarterly FY2025 performance data
    
    Returns:
        pd.DataFrame: Quarterly growth metrics
    """
    return pd.DataFrame({
        'Quarter': ['Q1FY25', 'Q2FY25', 'Q3FY25'],
        'Revenue Growth (%)': [9.6, 6.6, 4.5],
        'EBITDA Growth (%)': [9.4, 1.3, 6.9],
        'PAT Growth (%)': [0.8, -1.0, 9.5]
    })

# ═══════════════════════════════════════════════════════════════════════════
# SECTOR PERFORMANCE DATA
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data(ttl=CACHE_TTL)
def get_sector_data() -> pd.DataFrame:
    """
    Get sector performance data for FY2025
    
    Returns:
        pd.DataFrame: Sector-wise analysis with growth and status
    """
    return pd.DataFrame({
        'Sector': [
            'Financials', 'Energy', 'IT', 'Industrials', 'Materials',
            'Consumer Disc.', 'Healthcare', 'Consumer Staples', 'Utilities', 'Telecom'
        ],
        'Revenue Growth FY25 (%)': [12.3, 1.4, 7.0, 10.6, 1.7, 10.5, 7.6, 10.6, 7.5, 8.0],
        'Profit Growth FY25 (%)': [17.3, -35.4, 8.7, 25.7, -1.4, 6.6, 32.9, 6.1, -6.9, 95.9],
        'Weight in Nifty (%)': [35, 30, 9, 5, 11, 9, 3, 3, 3, 2],
        'Status': [
            '🟡 SLOWING', '🔴 CRISIS', '🟢 STABILIZING', '🟢 STRONG',
            '⚠️ MIXED', '⚠️ WEAKENING', '🟢 STRONG', '⚠️ MIXED', '⚠️ DECLINING', '🟢 EXCEPTIONAL'
        ]
    })

# ═══════════════════════════════════════════════════════════════════════════
# EARNINGS DOWNGRADE TRAJECTORY
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data(ttl=CACHE_TTL)
def get_downgrade_data() -> pd.DataFrame:
    """
    Get earnings downgrade trajectory (Sep 2024 - Feb 2025)
    
    Returns:
        pd.DataFrame: FY25 profit growth estimate revisions
    """
    return pd.DataFrame({
        'Date': [
            'Sep 30, 2024', 'Oct 31, 2024', 'Nov 30, 2024', 'Dec 31, 2024',
            'Jan 31, 2025', 'Feb 21, 2025'
        ],
        'Period': ['Sep-24', 'Oct-24', 'Nov-24', 'Dec-24', 'Jan-25', 'Feb-25'],
        'FY25 Profit Growth (%)': [9.8, 8.2, 5.8, 3.2, 4.9, 3.2]
    })

# ═══════════════════════════════════════════════════════════════════════════
# SCENARIO DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data(ttl=CACHE_TTL)
def get_scenarios() -> Dict:
    """
    Get scenario definitions for future earnings projections
    
    Returns:
        dict: Three scenarios with earnings and P/E assumptions
    """
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

@st.cache_data(ttl=CACHE_TTL)
def calculate_nifty_levels(scenarios: Dict) -> Dict:
    """
    Calculate Nifty 50 levels for each scenario
    
    Calculation:
        Nifty = EPS * P/E Multiple
    
    Args:
        scenarios (dict): Scenario definitions with earnings and P/E
        
    Returns:
        dict: Nifty levels for FY25, FY26, FY27 by scenario (in thousands)
    """
    nifty_levels = {}
    
    for scenario, data in scenarios.items():
        try:
            # Calculate EPS for each year
            fy25_eps = BASE_EPS_FY24 * (1 + data['fy25_earnings'] / 100)
            fy26_eps = fy25_eps * (1 + data['fy26_earnings'] / 100)
            fy27_eps = fy26_eps * (1 + data['fy27_earnings'] / 100)
            
            # Calculate Nifty levels
            fy25_nifty = fy25_eps * data['fy25_pe']
            fy26_nifty = fy26_eps * data['fy26_pe']
            fy27_nifty = fy27_eps * data['fy27_pe']
            
            # Store in thousands
            nifty_levels[scenario] = [
                fy25_nifty / 1000,
                fy26_nifty / 1000,
                fy27_nifty / 1000
            ]
        except Exception as e:
            print(f"Error calculating Nifty levels for {scenario}: {str(e)}")
            nifty_levels[scenario] = [0, 0, 0]
    
    return nifty_levels

# ═══════════════════════════════════════════════════════════════════════════
# KEY METRICS CALCULATION
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data(ttl=CACHE_TTL)
def calculate_key_metrics() -> Dict:
    """
    Calculate key metrics for dashboard display
    
    Returns:
        dict: Key metrics including CAGRs, trends, and divergence
    """
    five_year = get_five_year_data()
    quarterly = get_quarterly_data()
    
    try:
        # Get growth rates
        fy2021_rev = five_year.iloc[0]['Revenue Growth (%)']
        fy2025_rev = five_year.iloc[-1]['Revenue Growth (%)']
        fy2021_pat = five_year.iloc[0]['PAT Growth (%)']
        fy2025_pat = five_year.iloc[-1]['PAT Growth (%)']
        
        # Calculate CAGR
        if fy2021_rev > 0 and fy2025_rev > 0:
            revenue_cagr = ((fy2025_rev / fy2021_rev) ** (1/4) - 1) * 100
        else:
            revenue_cagr = 0
        
        if fy2021_pat > 0 and fy2025_pat > 0:
            pat_cagr = ((fy2025_pat / fy2021_pat) ** (1/4) - 1) * 100
        else:
            pat_cagr = 0
        
        current_rev = quarterly.iloc[-1]['Revenue Growth (%)']
        current_pat = quarterly.iloc[-1]['PAT Growth (%)']
        
        divergence = pat_cagr - revenue_cagr
        
        return {
            'revenue_cagr': revenue_cagr,
            'pat_cagr': pat_cagr,
            'current_rev_growth': current_rev,
            'current_pat_growth': current_pat,
            'revenue_trend': 'Decelerating' if current_rev < 8 else 'Stable',
            'profit_trend': 'Margin Support' if divergence > 5 else 'Balanced',
            'divergence_factor': divergence,
            'nifty_current': 23500,  # As of latest data point
            'pe_current': 25.0,
            'pe_fair_range': (10, 12)
        }
    except Exception as e:
        print(f"Error calculating key metrics: {str(e)}")
        return {
            'revenue_cagr': 0,
            'pat_cagr': 0,
            'current_rev_growth': 0,
            'current_pat_growth': 0,
            'revenue_trend': 'Unknown',
            'profit_trend': 'Unknown',
            'divergence_factor': 0,
            'nifty_current': 0,
            'pe_current': 0,
            'pe_fair_range': (0, 0)
        }

# ═══════════════════════════════════════════════════════════════════════════
# DATA VALIDATION
# ═══════════════════════════════════════════════════════════════════════════

def validate_data() -> Tuple[bool, str]:
    """
    Validate all data sources for consistency and completeness
    
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        five_year = get_five_year_data()
        quarterly = get_quarterly_data()
        sector = get_sector_data()
        downgrades = get_downgrade_data()
        scenarios = get_scenarios()
        
        # Validate data shapes
        assert len(five_year) == 5, "Five-year data should have 5 rows"
        assert len(quarterly) == 3, "Quarterly data should have 3 rows"
        assert len(sector) == 10, "Sector data should have 10 sectors"
        assert len(downgrades) == 6, "Downgrade data should have 6 data points"
        assert len(scenarios) == 3, "Should have 3 scenarios"
        
        # Validate column presence
        assert 'Revenue Growth (%)' in five_year.columns
        assert 'PAT Growth (%)' in quarterly.columns
        assert 'Weight in Nifty (%)' in sector.columns
        assert 'FY25 Profit Growth (%)' in downgrades.columns
        
        # Validate numeric values
        assert all(five_year['Revenue Growth (%)'] > -100), "Growth rates should be > -100%"
        assert all(five_year['Revenue Growth (%)'] < 100), "Growth rates should be < 100%"
        
        # Validate scenarios
        for scenario_name, scenario_data in scenarios.items():
            assert 'fy25_earnings' in scenario_data
            assert 'fy25_pe' in scenario_data
            assert scenario_data['probability'] > 0
        
        return True, "✅ All data validated successfully"
    
    except AssertionError as e:
        return False, f"❌ Validation failed: {str(e)}"
    except Exception as e:
        return False, f"❌ Data validation error: {str(e)}"

# ═══════════════════════════════════════════════════════════════════════════
# AGGREGATE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data(ttl=CACHE_TTL)
def load_all_data() -> Dict:
    """
    Load all data at once for efficient dashboard initialization
    
    Returns:
        dict: Complete dataset with all analysis components
    """
    scenarios = get_scenarios()
    
    return {
        'five_year': get_five_year_data(),
        'quarterly': get_quarterly_data(),
        'sector': get_sector_data(),
        'downgrades': get_downgrade_data(),
        'scenarios': scenarios,
        'nifty_levels': calculate_nifty_levels(scenarios),
        'metrics': calculate_key_metrics()
    }

# ═══════════════════════════════════════════════════════════════════════════
# DATA SUMMARY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def get_data_summary() -> Dict:
    """
    Get summary statistics for the dashboard
    
    Returns:
        dict: Summary statistics and key findings
    """
    five_year = get_five_year_data()
    quarterly = get_quarterly_data()
    sector = get_sector_data()
    scenarios = get_scenarios()
    
    return {
        'periods_analyzed': len(five_year),
        'quarters_analyzed': len(quarterly),
        'sectors_analyzed': len(sector),
        'scenarios_modeled': len(scenarios),
        'latest_revenue_growth': quarterly.iloc[-1]['Revenue Growth (%)'],
        'latest_pat_growth': quarterly.iloc[-1]['PAT Growth (%)'],
        'best_sector': sector.loc[sector['Profit Growth FY25 (%)'].idxmax(), 'Sector'],
        'worst_sector': sector.loc[sector['Profit Growth FY25 (%)'].idxmin(), 'Sector'],
        'total_weight_analyzed': sector['Weight in Nifty (%)'].sum(),
        'data_updated': 'Feb 21, 2025'
    }

# ═══════════════════════════════════════════════════════════════════════════
# EXPORT FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def export_to_csv(data_type: str) -> str:
    """
    Export specific dataset to CSV format
    
    Args:
        data_type (str): Type of data to export
        
    Returns:
        str: CSV formatted string
    """
    data_map = {
        'five_year': get_five_year_data(),
        'quarterly': get_quarterly_data(),
        'sector': get_sector_data(),
        'downgrades': get_downgrade_data()
    }
    
    if data_type in data_map:
        return data_map[data_type].to_csv(index=False)
    else:
        return ""

# ═══════════════════════════════════════════════════════════════════════════
# INITIALIZATION CHECK
# ═══════════════════════════════════════════════════════════════════════════

def initialize_data():
    """
    Initialize and validate all data on module load
    
    Returns:
        tuple: (success: bool, message: str)
    """
    success, message = validate_data()
    if success:
        # Pre-load all data for faster access
        load_all_data()
    return success, message


# Run initialization on import
if __name__ != "__main__":
    initialize_data()
