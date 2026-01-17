
import streamlit as st
from config import COLORS, FONTS

def get_custom_css():
    return f"""
    <style>
    .header-divider {{
        height: 3px;
        background: linear-gradient(90deg, {COLORS['dark_blue']}, {COLORS['accent_gold']}, {COLORS['dark_blue']});
        margin: 1rem 0 1.5rem 0;
        border-radius: 2px;
    }}
    .metric-value {{
        font-size: 1.8rem;
        font-weight: 700;
        color: {COLORS['dark_blue']};
    }}
    .metric-label {{
        font-size: 0.85rem;
        color: {COLORS['text_muted']};
    }}
    </style>
    """

def apply_custom_css():
    st.markdown(get_custom_css(), unsafe_allow_html=True)

def render_main_title(title, subtitle):
    st.markdown(f"# {title}")
    st.markdown(f"*{subtitle}*")

def render_section_header(text):
    st.markdown(f"### {text}")
    st.markdown('<div class="header-divider"></div>', unsafe_allow_html=True)

def render_info_box(content):
    st.info(content)

def render_warning_box(content):
    st.warning(content)

def render_success_box(content):
    st.success(content)

def render_divider():
    st.markdown("---")

def render_sidebar_metrics(metrics_dict):
    for label, (value, note) in metrics_dict.items():
        st.sidebar.markdown(f"**{label}**")
        st.sidebar.markdown(f"<div class='metric-value'>{value}</div>", unsafe_allow_html=True)
        st.sidebar.markdown(f"<span class='metric-label'>{note}</span>", unsafe_allow_html=True)
        st.sidebar.markdown("---")

def render_footer(author, brand, sources):
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1: st.markdown(f"**Author:** {author} | **Brand:** {brand}")
    with col2: st.markdown(f"**Sources:** {sources}")
