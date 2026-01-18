
"""
Styling Module for Indian Stock Market Analysis Dashboard

Provides reusable UI components and styling functions
consistent with Mountain Path - World of Finance design system.
"""

try:
    import streamlit as st
except ImportError:
    st = None

from config import COLORS, FONTS

# ═══════════════════════════════════════════════════════════════════════════
# CSS STYLING
# ═══════════════════════════════════════════════════════════════════════════

def get_custom_css():
    """
    Returns custom CSS for the application.
    Applies Mountain Path design system.
    """
    css = f"""
    <style>
    :root {{
        --primary: {COLORS['dark_blue']};
        --secondary: {COLORS['light_blue']};
        --accent: {COLORS['accent_gold']};
        --green: {COLORS['accent_green']};
        --red: {COLORS['accent_red']};
        --text-dark: {COLORS['text_dark']};
        --text-muted: {COLORS['text_muted']};
    }}

    * {{
        font-family: {FONTS['primary']};
    }}

    body {{
        color: {COLORS['text_dark']};
        background-color: {COLORS['bg_light']};
    }}

    .main {{
        padding: 0;
        background-color: {COLORS['bg_white']};
    }}

    /* Card Styles */
    .metric-card {{
        background: linear-gradient(135deg, {COLORS['dark_blue']}15, {COLORS['light_blue']}15);
        border-left: 4px solid {COLORS['dark_blue']};
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0, 51, 102, 0.08);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}

    .metric-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 51, 102, 0.12);
    }}

    .success-box {{
        background: {COLORS['accent_green']}10;
        border-left: 4px solid {COLORS['accent_green']};
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }}

    .warning-box {{
        background: {COLORS['accent_red']}10;
        border-left: 4px solid {COLORS['accent_red']};
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }}

    .info-box {{
        background: {COLORS['light_blue']}10;
        border-left: 4px solid {COLORS['light_blue']};
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }}

    /* Dividers */
    .header-divider {{
        height: 3px;
        background: linear-gradient(90deg, {COLORS['dark_blue']}, {COLORS['accent_gold']}, {COLORS['dark_blue']});
        margin: 1.5rem 0 2rem 0;
        border-radius: 2px;
    }}

    .subtle-divider {{
        height: 1px;
        background-color: {COLORS['border_color']};
        margin: 1.5rem 0;
    }}

    /* Typography */
    h1, h2, h3 {{
        color: {COLORS['dark_blue']};
        font-weight: 700;
        letter-spacing: -0.5px;
    }}

    h1 {{
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }}

    h2 {{
        font-size: 2rem;
        margin-bottom: 0.75rem;
    }}

    h3 {{
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }}

    h4 {{
        font-size: 1.125rem;
        color: {COLORS['dark_blue']};
        font-weight: 600;
        margin-bottom: 0.75rem;
    }}

    /* Metrics */
    .metric-label {{
        font-size: 0.875rem;
        color: {COLORS['text_muted']};
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }}

    .metric-value {{
        font-size: 2rem;
        font-weight: 700;
        color: {COLORS['dark_blue']};
        margin: 0.5rem 0;
    }}

    .metric-delta {{
        font-size: 0.875rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }}

    /* Sidebar */
    .sidebar {{
        background-color: {COLORS['dark_blue']}05;
    }}

    .sidebar-metric {{
        padding: 1rem;
        background: white;
        border-radius: 6px;
        margin-bottom: 0.75rem;
        border-left: 3px solid {COLORS['dark_blue']};
    }}

    /* Links */
    a {{
        color: {COLORS['light_blue']};
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s ease;
    }}

    a:hover {{
        color: {COLORS['accent_gold']};
        text-decoration: underline;
    }}

    /* Tables */
    table {{
        border-collapse: collapse;
        width: 100%;
    }}

    th {{
        background-color: {COLORS['dark_blue']}15;
        color: {COLORS['dark_blue']};
        font-weight: 600;
        padding: 0.75rem;
        text-align: left;
        border-bottom: 2px solid {COLORS['dark_blue']};
    }}

    td {{
        padding: 0.75rem;
        border-bottom: 1px solid {COLORS['border_color']};
    }}

    tr:hover {{
        background-color: {COLORS['bg_light']};
    }}

    /* Buttons */
    button {{
        background-color: {COLORS['dark_blue']};
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 6px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
    }}

    button:hover {{
        background-color: {COLORS['light_blue']};
        box-shadow: 0 4px 12px rgba(0, 51, 102, 0.2);
    }}

    /* Responsive */
    @media (max-width: 768px) {{
        h1 {{
            font-size: 1.75rem;
        }}

        .metric-value {{
            font-size: 1.5rem;
        }}
    }}
    </style>
    """
    return css

# ═══════════════════════════════════════════════════════════════════════════
# COMPONENT RENDERING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def render_main_title(title, subtitle):
    """Render main page title with subtitle"""
    st.markdown(f"# {title}")
    st.markdown(f"*{subtitle}*", unsafe_allow_html=True)


def render_section_header(text):
    """Render section header with contrast background and color"""
    if st is None:
        return
    # HTML with contrast background (dark blue) and white text
    st.markdown(
        f'<div style="background-color: #003366; color: #FFFFFF; padding: 20px; border-radius: 10px; margin-bottom: 20px;"><h2 style="margin: 0; font-size: 28px; font-weight: 700;">{text}</h2></div>',
        unsafe_allow_html=True
    )


def render_subsection_header(text):
    """Render subsection header"""
    if st is None:
        return
    st.markdown(f"#### {text}")


def render_info_box(content):
    """Render info box using st.info with markdown support"""
    if st is None:
        return
    st.info(content)


def render_warning_box(content):
    """Render warning box using st.warning with markdown support"""
    if st is None:
        return
    st.warning(content)


def render_success_box(content):
    """Render success box using st.success with markdown support"""
    if st is None:
        return
    st.success(content)


def render_divider():
    """Render subtle divider line"""
    if st is None:
        return
    st.markdown("---")


def display_styled_dataframe(df, columns_to_style=None, width='stretch', hide_index=True):
    """
    Display DataFrame with optional styling and full width support.
    
    Args:
        df: DataFrame to display
        columns_to_style: List of columns to apply gradient styling
        width: Column width ('stretch' or 'content')
        hide_index: Hide row index
    """
    if st is None:
        return
    
    try:
        # Convert width parameter to use_container_width for st.dataframe
        use_width = (width == 'stretch')
        st.dataframe(df, use_container_width=use_width, hide_index=hide_index)
    except Exception as e:
        st.warning(f"Could not display dataframe: {str(e)}")


def render_footer(author, brand, sources):
    """
    Render page footer with author, brand, and sources.
    
    Args:
        author (str): Author name
        brand (str): Brand name
        sources (str): Data sources
    """
    if st is None:
        return
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"**Author:** {author}")
    
    with col2:
        st.markdown(f"**Platform:** {brand}")
    
    with col3:
        st.markdown(f"**Sources:** {sources}")
    
    st.markdown(
        f"<p style='text-align:center; color:{COLORS['text_muted']}; "
        f"font-size:0.85rem; margin-top:2rem;'>"
        f"<i>© 2026 The Mountain Path - World of Finance | All Rights Reserved</i>"
        f"</p>",
        unsafe_allow_html=True
    )


def render_sidebar_metrics(metrics_dict):
    """
    Render metrics in sidebar with consistent styling.
    
    Args:
        metrics_dict (dict): Dictionary of {label: (value, note)}
    """
    for label, (value, note) in metrics_dict.items():
        st.sidebar.markdown(f"**{label}**")
        st.sidebar.markdown(
            f"<div class='metric-value'>{value}</div>",
            unsafe_allow_html=True
        )
        st.sidebar.markdown(
            f"<span class='metric-label'>{note}</span>",
            unsafe_allow_html=True
        )
        st.sidebar.markdown("")


def render_sidebar_alert(title, content, alert_type="warning"):
    """
    Render alert box in sidebar.
    
    Args:
        title (str): Alert title
        content (str): Alert content
        alert_type (str): Type - 'warning', 'error', or 'info'
    """
    if alert_type == "warning":
        st.sidebar.warning(f"**{title}**\n\n{content}")
    elif alert_type == "error":
        st.sidebar.error(f"**{title}**\n\n{content}")
    else:
        st.sidebar.info(f"**{title}**\n\n{content}")


def spacing(lines=1):
    """Add vertical spacing between elements"""
    for _ in range(lines):
        st.markdown("")


def render_metric_card(label, value, delta=None, delta_color=None):
    """
    Render a metric card with label and value.
    
    Args:
        label (str): Metric label
        value (str): Metric value
        delta (str, optional): Change indicator (e.g., "+10%")
        delta_color (str, optional): Color for delta - 'green', 'red', or 'neutral'
    """
    delta_html = ""
    if delta:
        color_map = {
            'green': COLORS['accent_green'],
            'red': COLORS['accent_red'],
            'neutral': COLORS['text_muted']
        }
        color = color_map.get(delta_color, COLORS['text_muted'])
        delta_html = f'<span class="metric-delta" style="color:{color};">{delta}</span>'
    
    html = f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def render_comparison_box(title, items):
    """
    Render a comparison box with multiple items.
    
    Args:
        title (str): Box title
        items (dict): Dictionary of {label: value}
    """
    html = f"<b>{title}</b><br>"
    for label, value in items.items():
        html += f"{label}: <b>{value}</b><br>"
    
    render_info_box(html)


def apply_custom_css():
    """Apply custom CSS to Streamlit app"""
    st.markdown(get_custom_css(), unsafe_allow_html=True)
