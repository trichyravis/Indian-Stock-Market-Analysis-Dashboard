
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
# DATA SOURCES & LINKS
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
        'description': 'Central bank data on interest rates and economic indicators',
        'data_used': 'Economic context, Inflation data'
    },
    'MCA': {
        'name': 'Ministry of Corporate Affairs',
        'url': 'https://www.mca.gov.in/',
        'description': 'Government repository for corporate filings',
        'data_used': 'Annual reports, Quarterly earnings'
    }
}

PRIMARY_DATA_SOURCES = [
    'NSE (https://www.nseindia.com/)',
    'RBI (https://www.rbi.org.in/)',
    'BSE (https://www.bseindia.com/)',
    'MCA (https://www.mca.gov.in/)'
]

RESEARCH_SOURCES = [
    'Business Standard (https://www.business-standard.com/)',
    'Economic Times (https://economictimes.indiatimes.com/)',
    'Motilal Oswal (https://www.motilaloswal.com/)'
]

GLOBAL_RESEARCH = [
    'Nomura (https://www.nomura.com/)',
    'Goldman Sachs (https://www.gs.com/)'
]

# ═══════════════════════════════════════════════════════════════════════════
# APPLICATION SETTINGS
# ═══════════════════════════════════════════════════════════════════════════

CHART_HEIGHT = 500
CHART_HEIGHT_SMALL = 350
CACHE_TTL = 3600  # 1 hour

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

# Consolidated MESSAGES dictionary (Fixed duplicate)
MESSAGES = {
    'header_title': '📊 Indian Stock Market Analysis Dashboard',
    'header_subtitle': 'Is Growth Driven by Revenue Expansion or Margin Re-Rating?',
    'sidebar_title': '🏔️ The Mountain Path',
    'nav_label': '📍 Choose Analysis:',
    'valuation_alert': '⚠️ Valuation Alert',
    'valuation_content': 'Current P/E: 25x\nFair Value P/E: 10-12x\nGap: -50% to -60%',
}

# ═══════════════════════════════════════════════════════════════════════════
# TYPOGRAPHY & THRESHOLDS
# ═══════════════════════════════════════════════════════════════════════════

FONTS = {
    'primary': '-apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto"',
    'mono': '"Courier New", monospace',
}

THRESHOLDS = {
    'revenue_growth_warning': 5.0,
    'profit_growth_warning': 0.0,
    'divergence_alert': 40,
}
