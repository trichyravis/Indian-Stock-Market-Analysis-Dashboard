"""
Styles Module - Reusable Styling Functions
Mountain Path Design System
"""

import streamlit as st
from config import COLORS

# ═══════════════════════════════════════════════════════════════════════════
# TYPOGRAPHY & HEADERS
# ═══════════════════════════════════════════════════════════════════════════

def render_main_title(title: str, subtitle: str = None):
    """Render main page title with optional subtitle"""
    st.markdown(f"<h1 style='text-align: center; color: {COLORS['primary_dark']};'>{title}</h1>", 
                unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<h3 style='text-align: center; color: {COLORS['primary_mid']};'>{subtitle}</h3>", 
                    unsafe_allow_html=True)

def render_section_header(text: str):
    """Render section header"""
    st.markdown(f"<h2 style='color: {COLORS['primary_dark']}; border-bottom: 2px solid {COLORS['primary_light']};'>{text}</h2>", 
                unsafe_allow_html=True)

def render_subsection_header(text: str):
    """Render subsection header"""
    st.markdown(f"<h3 style='color: {COLORS['primary_mid']};'>{text}</h3>", 
                unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# INFO BOXES & CALLOUTS
# ═══════════════════════════════════════════════════════════════════════════

def render_info_box(content: str, icon: str = "ℹ️"):
    """Render information box"""
    st.markdown(f"""
    <div style='
        background-color: #E8F4F8;
        border-left: 4px solid {COLORS['primary_dark']};
        padding: 15px;
        border-radius: 4px;
        margin: 10px 0;
    '>
    <strong>{icon} Information:</strong><br/>
    {content.replace(chr(10), '<br/>')}
    </div>
    """, unsafe_allow_html=True)

def render_warning_box(content: str, icon: str = "⚠️"):
    """Render warning box"""
    st.markdown(f"""
    <div style='
        background-color: #FFE8E8;
        border-left: 4px solid {COLORS['accent_red']};
        padding: 15px;
        border-radius: 4px;
        margin: 10px 0;
    '>
    <strong>{icon} Warning:</strong><br/>
    {content.replace(chr(10), '<br/>')}
    </div>
    """, unsafe_allow_html=True)

def render_success_box(content: str, icon: str = "✓"):
    """Render success box"""
    st.markdown(f"""
    <div style='
        background-color: #E8F8E8;
        border-left: 4px solid {COLORS['accent_green']};
        padding: 15px;
        border-radius: 4px;
        margin: 10px 0;
    '>
    <strong>{icon} Success:</strong><br/>
    {content.replace(chr(10), '<br/>')}
    </div>
    """, unsafe_allow_html=True)

def render_alert_box(content: str, alert_type: str = "info"):
    """Render alert box with type"""
    color_map = {
        'info': (COLORS['primary_dark'], '#E8F4F8'),
        'warning': (COLORS['accent_red'], '#FFE8E8'),
        'success': (COLORS['accent_green'], '#E8F8E8'),
        'error': (COLORS['accent_red'], '#FFD1D1')
    }
    border_color, bg_color = color_map.get(alert_type, color_map['info'])
    
    st.markdown(f"""
    <div style='
        background-color: {bg_color};
        border-left: 4px solid {border_color};
        padding: 15px;
        border-radius: 4px;
        margin: 10px 0;
    '>
    {content.replace(chr(10), '<br/>')}
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# METRIC DISPLAYS
# ═══════════════════════════════════════════════════════════════════════════

def render_metric_grid(metrics: dict):
    """Render multiple metrics in a grid"""
    cols = st.columns(len(metrics))
    for idx, (label, (value, change)) in enumerate(metrics.items()):
        with cols[idx]:
            st.metric(label, value, change)

def render_colored_metric(label: str, value: str, change: str = None, color: str = 'primary_dark'):
    """Render a colored metric"""
    st.metric(label, value, change)

# ═══════════════════════════════════════════════════════════════════════════
# TABLE STYLING
# ═══════════════════════════════════════════════════════════════════════════

def style_dataframe_gradient(df, columns: list, cmap: str = 'RdYlGn'):
    """Apply gradient styling to dataframe"""
    return df.style.background_gradient(subset=columns, cmap=cmap)

def style_dataframe_conditional(df, column: str):
    """Apply conditional styling to dataframe"""
    def highlight_positive_negative(val):
        if isinstance(val, (int, float)):
            if val < 0:
                return f'background-color: #FFE8E8; color: {COLORS["accent_red"]}'
            elif val > 0:
                return f'background-color: #E8F8E8; color: {COLORS["accent_green"]}'
    return df.style.applymap(highlight_positive_negative, subset=[column])

# ═══════════════════════════════════════════════════════════════════════════
# DIVIDERS & SPACING
# ═══════════════════════════════════════════════════════════════════════════

def render_divider(style: str = 'solid'):
    """Render custom divider"""
    st.markdown(f"""
    <hr style='
        border: none;
        height: 2px;
        background: linear-gradient(to right, {COLORS['primary_light']}, {COLORS['primary_dark']}, {COLORS['primary_light']});
        margin: 20px 0;
    '/>
    """, unsafe_allow_html=True)

def spacing(lines: int = 1):
    """Add vertical spacing"""
    for _ in range(lines):
        st.write("")

# ═══════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════

def render_footer(author: str, brand: str, data_source: str):
    """Render branded footer"""
    st.markdown(f"""
    ---
    <div style='text-align: center; padding: 20px; color: {COLORS['medium_gray']}; font-size: 12px;'>
        <strong>{brand}</strong><br/>
        Created by {author} | Bangalore, India<br/>
        Data Source: {data_source}<br/>
        Analysis Period: FY2021 – FY2025 | Created: January 2026<br/>
        <em>Disclaimer: For educational purposes only. Not investment advice.</em>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# SIDEBAR COMPONENTS
# ═══════════════════════════════════════════════════════════════════════════

def render_sidebar_metrics(metrics: dict):
    """Render metrics in sidebar"""
    st.sidebar.markdown("### 📌 Key Metrics")
    col1, col2 = st.sidebar.columns(2)
    
    items = list(metrics.items())
    for idx, (label, (value, change)) in enumerate(items):
        with col1 if idx % 2 == 0 else col2:
            st.metric(label, value, change)

def render_sidebar_alert(title: str, content: str, alert_type: str = "warning"):
    """Render alert in sidebar"""
    color_map = {
        'info': '#E8F4F8',
        'warning': '#FFE8E8',
        'success': '#E8F8E8',
        'error': '#FFD1D1'
    }
    
    st.sidebar.markdown(f"""
    <div style='
        background-color: {color_map.get(alert_type, "#E8F4F8")};
        border-left: 4px solid {COLORS['primary_dark']};
        padding: 12px;
        border-radius: 4px;
        margin: 10px 0;
    '>
    <strong>{title}</strong><br/>
    {content.replace(chr(10), '<br/>')}
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════
# BADGES & LABELS
# ═══════════════════════════════════════════════════════════════════════════

def render_badge(text: str, badge_type: str = 'default'):
    """Render badge/label"""
    color_map = {
        'default': COLORS['primary_dark'],
        'success': COLORS['accent_green'],
        'warning': COLORS['accent_orange'],
        'error': COLORS['accent_red'],
        'info': COLORS['primary_mid']
    }
    
    bg_color = color_map.get(badge_type, COLORS['primary_dark'])
    st.markdown(f"""
    <span style='
        background-color: {bg_color};
        color: white;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: bold;
    '>{text}</span>
    """, unsafe_allow_html=True)
