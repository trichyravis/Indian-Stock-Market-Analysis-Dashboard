
"""
Data Module - Data Preparation & Loading
Indian Stock Market Analysis Dashboard
"""

import pandas as pd
import numpy as np
import streamlit as st
from typing import Dict, Tuple

# ═══════════════════════════════════════════════════════════════════════════
# CONSTANTS & EPS DATA
# ═══════════════════════════════════════════════════════════════════════════

BASE_EPS_FY24 = 2150  # Base earnings per share for Nifty 50
CACHE_TTL = 3600      # 1 hour

# ═══════════════════════════════════════════════════════════════════════════
# DATA LOADING (CACHED)
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data(ttl=CACHE_TTL)
def get_five_year_data() -> pd.DataFrame:
    return pd.DataFrame({
        'Fiscal Year': ['FY2021', 'FY2022', 'FY2023', 'FY2024', 'FY2025 YTD'],
        'Revenue Growth (%)': [10.5, 15.4, 13.8, 10.7, 6.9],
        'EBITDA Growth (%)': [11.2, 22.8, 18.5, 14.3, 2.6],
        'PAT Growth (%)': [8.3, 25.7, 22.1, 16.8, 4.6],
        'EBITDA Margin (%)': [32.1, 33.5, 33.2, 33.0, 33.1],
        'PAT Margin (%)': [9.8, 10.4, 10.6, 10.5, 10.7]
    })

@st.cache_data(ttl=CACHE_TTL)
def get_quarterly_data() -> pd.DataFrame:
    return pd.DataFrame({
        'Quarter': ['Q1FY25', 'Q2FY25', 'Q3FY25'],
        'Revenue Growth (%)': [9.6, 6.6, 4.5],
        'EBITDA Growth (%)': [9.4, 1.3, 6.9],
        'PAT Growth (%)': [0.8, -1.0, 9.5]
    })

@st.cache_data(ttl=CACHE_TTL)
def get_sector_data() -> pd.DataFrame:
    return pd.DataFrame({
        'Sector': ['Financials', 'Energy', 'IT', 'Industrials', 'Materials',
                   'Consumer Disc.', 'Healthcare', 'Consumer Staples', 'Utilities', 'Telecom'],
        'Revenue Growth FY25 (%)': [12.3, 1.4, 7.0, 10.6, 1.7, 10.5, 7.6, 10.6, 7.5, 8.0],
        'Profit Growth FY25 (%)': [17.3, -35.4, 8.7, 25.7, -1.4, 6.6, 32.9, 6.1, -6.9, 95.9],
        'Weight in Nifty (%)': [35, 30, 9, 5, 11, 9, 3, 3, 3, 2],
        'Status': ['🟡 SLOWING', '🔴 CRISIS', '🟢 STABILIZING', '🟢 STRONG', '⚠️ MIXED', 
                   '⚠️ WEAKENING', '🟢 STRONG', '⚠️ MIXED', '⚠️ DECLINING', '🟢 EXCEPTIONAL']
    })

@st.cache_data(ttl=CACHE_TTL)
def get_downgrade_data() -> pd.DataFrame:
    return pd.DataFrame({
        'Period': ['Sep-24', 'Oct-24', 'Nov-24', 'Dec-24', 'Jan-25', 'Feb-25'],
        'FY25 Profit Growth (%)': [9.8, 8.2, 5.8, 3.2, 4.9, 3.2]
    })

# ═══════════════════════════════════════════════════════════════════════════
# CALCULATIONS
# ═══════════════════════════════════════════════════════════════════════════

@st.cache_data(ttl=CACHE_TTL)
def calculate_nifty_levels(scenarios: Dict) -> Dict:
    nifty_levels = {}
    for scenario, data in scenarios.items():
        # Calculate EPS projections based on scenario growth rates
        fy25_eps = BASE_EPS_FY24 * (1 + data['fy25_earnings'] / 100)
        fy26_eps = fy25_eps * (1 + data['fy26_earnings'] / 100)
        fy27_eps = fy26_eps * (1 + data['fy27_earnings'] / 100)
        
        # Store Nifty target (divided by 1000 for display units)
        nifty_levels[scenario] = [
            (fy25_eps * data['fy25_pe']) / 1000,
            (fy26_eps * data['fy26_pe']) / 1000,
            (fy27_eps * data['fy27_pe']) / 1000
        ]
    return nifty_levels

@st.cache_data(ttl=CACHE_TTL)
def calculate_key_metrics() -> Dict:
    five_year = get_five_year_data()
    quarterly = get_quarterly_data()
    
    # Calculate CAGR using the first and last year's performance
    rev_start, rev_end = five_year.iloc[0]['Revenue Growth (%)'], five_year.iloc[-1]['Revenue Growth (%)']
    pat_start, pat_end = five_year.iloc[0]['PAT Growth (%)'], five_year.iloc[-1]['PAT Growth (%)']
    
    revenue_cagr = ((rev_end / rev_start) ** (1/4) - 1) * 100 if rev_start > 0 else 0
    pat_cagr = ((pat_end / pat_start) ** (1/4) - 1) * 100 if pat_start > 0 else 0
    
    return {
        'revenue_cagr': revenue_cagr,
        'pat_cagr': pat_cagr,
        'current_rev_growth': quarterly.iloc[-1]['Revenue Growth (%)'],
        'current_pat_growth': quarterly.iloc[-1]['PAT Growth (%)'],
        'divergence_factor': pat_cagr - revenue_cagr,
        'pe_current': 25.0,
        'pe_fair_range': (10, 12)
    }

# ═══════════════════════════════════════════════════════════════════════════
# AGGREGATE LOAD & VALIDATION
# ═══════════════════════════════════════════════════════════════════════════

def validate_data() -> Tuple[bool, str]:
    try:
        # Check basic integrity of the DataFrames
        assert not get_five_year_data().empty, "Historical data is missing"
        assert not get_sector_data().empty, "Sector data is missing"
        return True, "Data Validation Successful"
    except Exception as e:
        return False, str(e)

@st.cache_data(ttl=CACHE_TTL)
def load_all_data() -> Dict:
    # Explicitly import from config to get scenario structure if needed
    # (Assuming get_scenarios is defined in data.py or passed in)
    from data import get_scenarios
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

# Function to satisfy the get_scenarios call in load_all_data
@st.cache_data(ttl=CACHE_TTL)
def get_scenarios() -> Dict:
    return {
        'Base Case (50%)': {'fy25_earnings': 5.5, 'fy26_earnings': 11.0, 'fy27_earnings': 12.5, 'fy25_pe': 25.0, 'fy26_pe': 24.5, 'fy27_pe': 24.0, 'color': '#FFA500', 'probability': 0.50},
        'Bear Case (25%)': {'fy25_earnings': 2.0, 'fy26_earnings': 5.0, 'fy27_earnings': 7.5, 'fy25_pe': 23.0, 'fy26_pe': 22.0, 'fy27_pe': 21.5, 'color': '#FF0000', 'probability': 0.25},
        'Bull Case (25%)': {'fy25_earnings': 9.0, 'fy26_earnings': 14.0, 'fy27_earnings': 15.5, 'fy25_pe': 25.5, 'fy26_pe': 26.0, 'fy27_pe': 26.5, 'color': '#00AA00', 'probability': 0.25}
    }
