
"""
Configuration Module for Indian Stock Market Analysis Dashboard

Defines all constants, color schemes, and configuration settings.
Follows Mountain Path - World of Finance design standards.
"""

# ═══════════════════════════════════════════════════════════════════════════
# COLOR SCHEME - MOUNTAIN PATH BRANDING
# ═══════════════════════════════════════════════════════════════════════════

COLORS = {
    # Primary Colors
    'dark_blue': '#003366',          # RGB(0, 51, 102)
    'light_blue': '#004d80',         # RGB(0, 77, 128)
    'accent_gold': '#FFD700',        # RGB(255, 215, 0)
    
    # Chart Colors
    'chart_blue': '#0066CC',
    'accent_green': '#10B981',
    'accent_red': '#EF4444',
    'accent_orange': '#F97316',
    'accent_purple': '#8B5CF6',
    
    # Background & Text
    'bg_light': '#F8F9FA',
    'bg_white': '#FFFFFF',
    'text_dark': '#1F2937',
    'text_muted': '#6B7280',
    'text_light': '#9CA3AF',
    
    # UI Elements
    'border_color': '#E5E7EB',
    'hover_bg': '#F3F4F6',
}

# ═══════════════════════════════════════════════════════════════════════════
# AUTHOR & BRANDING
# ═══════════════════════════════════════════════════════════════════════════

AUTHOR = "Prof. V. Ravichandran"
BRAND_NAME = "The Mountain Path - World of Finance"
EXPERIENCE = "28+ Years Corporate Finance & Banking | 10+ Years Academic Excellence"
LOCATION = "Bangalore, India"
YEAR = 2026

# ═══════════════════════════════════════════════════════════════════════════
# DATA SOURCES WITH EXACT LINKS
# ═══════════════════════════════════════════════════════════════════════════

DATA_SOURCES_INFO = {
    'NSE': {
        'name': 'National Stock Exchange of India',
        'url': 'https://www.nseindia.com/',
        'description': 'Official source for Nifty 50 index data and corporate announcements',
        'data_used': '5-year performance, Quarterly data, Sector weights'
    },
    'RBI': {
        'name': 'Reserve Bank of India',
        'url': 'https://www.rbi.org.in/',
        'description': 'Central bank data on interest rates, monetary policy, and economic indicators',
        'data_used': 'Economic context, Inflation data, Policy environment'
    },
    'BSE': {
        'name': 'Bombay Stock Exchange',
        'url': 'https://www.bseindia.com/',
        'description': 'Alternative exchange data for validation and cross-checking',
        'data_used': 'Sector indices, Corporate disclosures'
    },
    'MCA': {
        'name': 'Ministry of Corporate Affairs',
        'url': 'https://www.mca.gov.in/',
        'description': 'Government repository for corporate filings and financial statements',
        'data_used': 'Annual reports, Quarterly earnings'
    },
    'SEBI': {
        'name': 'Securities and Exchange Board of India',
        'url': 'https://www.sebi.gov.in/',
        'description': 'Market regulator providing market data and company disclosures',
        'data_used': 'Regulatory filings, Market circulars'
    },
    'Business_Standard': {
        'name': 'Business Standard (India)',
        'url': 'https://www.business-standard.com/',
        'description': 'Financial news and analysis on Indian markets',
        'data_used': 'Earnings estimates, Market analysis, Downgrades'
    },
    'Economic_Times': {
        'name': 'The Economic Times',
        'url': 'https://economictimes.indiatimes.com/',
        'description': 'Indian business and financial news',
        'data_used': 'Market trends, Sector updates'
    },
    'Motilal_Oswal': {
        'name': 'Motilal Oswal Financial Services',
        'url': 'https://www.motilaloswal.com/',
        'description': 'Investment research and market analysis',
        'data_used': 'Earnings estimates, Sector analysis'
    },
    'ICICI_Securities': {
        'name': 'ICICI Securities Research',
        'url': 'https://research.icicisecurities.com/',
        'description': 'Equity research and market insights',
        'data_used': 'Company analysis, Earnings revisions'
    },
    'HDFC_Securities': {
        'name': 'HDFC Securities Research',
        'url': 'https://www.hdfcsec.com/',
        'description': 'Investment advisory and research',
        'data_used': 'Market outlook, Sector recommendations'
    },
    'Nomura': {
        'name': 'Nomura India Research',
        'url': 'https://www.nomura.com/indices/india',
        'description': 'Global investment bank research on Indian markets',
        'data_used': 'Valuation analysis, Market trends'
    },
    'Goldman_Sachs': {
        'name': 'Goldman Sachs Research',
        'url': 'https://www.gs.com/',
        'description': 'Global investment banking and research',
        'data_used': 'Market forecasts, Scenario analysis'
    }
}

# Primary data sources
PRIMARY_DATA_SOURCES = [
    'NSE (https://www.nseindia.com/)',
    'RBI (https://www.rbi.org.in/)',
    'BSE (https://www.bseindia.com/)',
    'MCA (https://www.mca.gov.in/)'
]

# Research sources
RESEARCH_SOURCES = [
    'Business Standard (https://www.business-standard.com/)',
    'Economic Times (https://economictimes.indiatimes.com/)',
    'Motilal Oswal (https://www.motilaloswal.com/)',
    'ICICI Securities (https://research.icicisecurities.com/)',
    'HDFC Securities (https://www.hdfcsec.com/)'
]

# Global research
GLOBAL_RESEARCH = [
    'Nomura (https://www.nomura.com/)',
    'Goldman Sachs (https://www.gs.com/)'
]
ANALYSIS_PERIOD = "FY2021-FY2025"
CURRENT_QUARTER = "Q3FY25"

# ═══════════════════════════════════════════════════════════════════════════
# CHART SETTINGS
# ═══════════════════════════════════════════════════════════════════════════

CHART_HEIGHT = 500
CHART_HEIGHT_SMALL = 350
CHART_HEIGHT_MINI = 250

# ═══════════════════════════════════════════════════════════════════════════
# CACHE SETTINGS
# ═══════════════════════════════════════════════════════════════════════════

CACHE_TTL = 3600  # 1 hour in seconds

# ═══════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

PAGE_CONFIG = {
    'page_title': 'Indian Stock Market Analysis | The Mountain Path',
    'page_icon': '📊',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded',
}

# ═══════════════════════════════════════════════════════════════════════════
# NAVIGATION PAGES
# ═══════════════════════════════════════════════════════════════════════════

PAGES = [
    "🏠 Overview",
    "📈 5-Year Trend",
    "📊 Quarterly Deep-Dive",
    "🏦 Sector Analysis",
    "📉 Earnings Downgrades",
    "🎯 Scenarios",
    "📋 Data Explorer",
    "📚 Data Sources"
]

# ═══════════════════════════════════════════════════════════════════════════
# MESSAGES & LABELS
# ═══════════════════════════════════════════════════════════════════════════

MESSAGES = {
    'header_title': '📊 Indian Stock Market Analysis Dashboard',
    'header_subtitle': 'Is Growth Driven by Revenue Expansion or Margin Re-Rating?',
    'sidebar_title': '🏔️ The Mountain Path - World of Finance',
}

# ═══════════════════════════════════════════════════════════════════════════
# METRICS & KPIs
# ═══════════════════════════════════════════════════════════════════════════

KEY_METRICS = {
    'revenue_cagr': 11.5,
    'revenue_current': 4.5,
    'profit_cagr': 14.7,
    'profit_current': 9.5,
    'pe_current': 25,
    'pe_fair_min': 10,
    'pe_fair_max': 12,
    'nifty_current': 23000,
}

# ═══════════════════════════════════════════════════════════════════════════
# SCENARIO ASSUMPTIONS
# ═══════════════════════════════════════════════════════════════════════════

SCENARIOS_CONFIG = {
    'Base Case (50%)': {
        'description': 'Margin resilience persists',
        'probability': 0.50,
        'color': '#FFD700',
        'nifty_return_pa': 0.10,
        'earnings_cagr_range': (8.5, 10.8),
    },
    'Bear Case (25%)': {
        'description': 'Margin compression hits',
        'probability': 0.25,
        'color': '#EF4444',
        'nifty_return_pa': -0.002,
        'earnings_cagr_range': (1.5, 8.0),
    },
    'Bull Case (25%)': {
        'description': 'Revenue reaccelerates',
        'probability': 0.25,
        'color': '#10B981',
        'nifty_return_pa': 0.145,
        'earnings_cagr_range': (12.0, 15.6),
    },
}

# ═══════════════════════════════════════════════════════════════════════════
# SECTOR CLASSIFICATIONS
# ═══════════════════════════════════════════════════════════════════════════

SECTORS = {
    'Financials': {'weight': 35, 'color': '#0066CC'},
    'Energy': {'weight': 30, 'color': '#F97316'},
    'IT': {'weight': 12, 'color': '#8B5CF6'},
    'Industrials': {'weight': 5, 'color': '#10B981'},
    'Materials': {'weight': 10, 'color': '#EF4444'},
    'Consumer': {'weight': 8, 'color': '#FFD700'},
}

# ═══════════════════════════════════════════════════════════════════════════
# ANALYSIS THRESHOLDS
# ═══════════════════════════════════════════════════════════════════════════

THRESHOLDS = {
    'revenue_growth_warning': 5.0,      # Below this is concerning
    'profit_growth_warning': 0.0,       # Below zero is problematic
    'margin_compression_alert': -1.0,   # Basis points
    'estimate_downgrade_alert': -30,    # Percentage downgrade
    'divergence_alert': 40,             # Profit growing faster than revenue (%)
}

# ═══════════════════════════════════════════════════════════════════════════
# TYPOGRAPHY
# ═══════════════════════════════════════════════════════════════════════════

FONTS = {
    'primary': '-apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto"',
    'mono': '"Courier New", monospace',
}

# ═══════════════════════════════════════════════════════════════════════════
# MESSAGES & LABELS
# ═══════════════════════════════════════════════════════════════════════════

MESSAGES = {
    'header_title': '📊 Indian Stock Market Analysis',
    'header_subtitle': 'Is Growth Driven by Revenue Expansion or Margin Re-Rating?',
    'sidebar_title': '🏔️ The Mountain Path - World of Finance',
    'nav_label': '📍 Choose Analysis:',
    'valuation_alert': '⚠️ Valuation Alert',
    'valuation_content': 'Current P/E: 25x\nFair Value P/E: 10-12x\nGap: -50% to -60%',
}

# ═══════════════════════════════════════════════════════════════════════════
# EXPORT SETTINGS
# ═══════════════════════════════════════════════════════════════════════════

EXPORT_FORMATS = {
    '5_year': '5_year_nifty_data.csv',
    'quarterly': 'quarterly_fy25_data.csv',
    'sector': 'sector_analysis.csv',
    'downgrades': 'earnings_downgrades.csv',
}
