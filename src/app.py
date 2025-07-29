# Modular Water Supply Dashboard

import streamlit as st
from datetime import datetime

# Import our modular components
from constants import TRANSLATIONS, PAGE_CONFIG, SUGGESTION_THRESHOLDS
from styles import (
    get_main_css, get_metrics_grid_css, get_satisfaction_grid_css,
    get_mobile_layout_css, get_toggle_switch_css, get_container_css
)
from data_processor import DataProcessor
from chart_builder import ChartBuilder

def initialize_app():
    """Initialize the Streamlit app with configuration and styling"""
    st.set_page_config(**PAGE_CONFIG)
    
    # Apply all CSS styling
    st.markdown(get_main_css(), unsafe_allow_html=True)
    st.markdown(get_metrics_grid_css(), unsafe_allow_html=True)
    st.markdown(get_satisfaction_grid_css(), unsafe_allow_html=True)
    st.markdown(get_mobile_layout_css(), unsafe_allow_html=True)
    st.markdown(get_toggle_switch_css(), unsafe_allow_html=True)
    st.markdown(get_container_css(), unsafe_allow_html=True)

def setup_language_toggle():
    """Setup language toggle functionality"""
    if 'language' not in st.session_state:
        st.session_state['language'] = 'Assamese'
    
    col1, col2, col3 = st.columns([6, 1, 2])
    with col3:
        def toggle_language():
            st.session_state['language'] = 'Assamese' if st.session_state['language'] == 'English' else 'English'
        
        try:
            lang_toggle = st.toggle(
                'English / Assamese',
                value=(st.session_state['language'] == 'Assamese'),
                key='lang_toggle',
                on_change=toggle_language
            )
        except AttributeError:
            lang_toggle = st.checkbox(
                'English / Assamese',
                value=(st.session_state['language'] == 'Assamese'),
                key='lang_toggle',
                on_change=toggle_language
            )
    
    # Get current language code and translations
    lang_code = 'as' if st.session_state.language == 'Assamese' else 'en'
    return TRANSLATIONS[lang_code]

def render_header(translations):
    """Render the header section"""
    st.markdown(
        f"""
        <div class="header-container" style="margin-bottom: 0; margin-top: 0;">
            <div style="flex: 1;"></div>
            <div style="text-align: right;">
                <p style="color: #666; margin: 0;">{translations['report_date']}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with st.container():
        st.markdown(f"""
            <h1 style='color: #2d63c7; margin: 0; text-align: center;'>{translations['title']}</h1>
        """, unsafe_allow_html=True)
        st.markdown(f"<h4 style='color: #000; margin: 0;'>{translations['filter_question']}</h4>", unsafe_allow_html=True)

def render_filters(data_processor, translations):
    """Render the filter section"""
    filter_col1, filter_col2, filter_col3, filter_col4 = st.columns([1, 1, 1, 1], gap="large")
    
    # Get filter options
    options = data_processor.get_filter_options()
    
    with filter_col1:
        st.markdown(f'<div class="filter-label">{translations["district"]}</div>', unsafe_allow_html=True)
        selected_district = st.selectbox(
            '',
            options=options['districts'],
            key='district_selectbox',
            label_visibility='collapsed'
        )
    
    # Update options based on selected district
    options = data_processor.get_filter_options(selected_district)
    
    with filter_col2:
        st.markdown(f'<div class="filter-label">{translations["division"]}</div>', unsafe_allow_html=True)
        selected_division = st.selectbox(
            '',
            options=options['divisions'],
            key='division_selectbox',
            label_visibility='collapsed'
        )
    
    # Update options based on selected division
    options = data_processor.get_filter_options(selected_district, selected_division)
    
    with filter_col3:
        st.markdown(f'<div class="filter-label">{translations["sub_division"]}</div>', unsafe_allow_html=True)
        selected_sub_div = st.selectbox(
            '',
            options=options['sub_divisions'],
            key='sub_division_selectbox',
            label_visibility='collapsed'
        )
    
    # Update options based on selected sub-division
    options = data_processor.get_filter_options(selected_district, selected_division, selected_sub_div)
    
    # Reset scheme selection if filters change
    if "last_district" not in st.session_state or st.session_state.last_district != selected_district:
        st.session_state["scheme_selectbox"] = options['schemes'][0] if options['schemes'] else None
    if "last_division" not in st.session_state or st.session_state.last_division != selected_division:
        st.session_state["scheme_selectbox"] = options['schemes'][0] if options['schemes'] else None
    if "last_sub_div" not in st.session_state or st.session_state.last_sub_div != selected_sub_div:
        st.session_state["scheme_selectbox"] = options['schemes'][0] if options['schemes'] else None
    
    st.session_state["last_district"] = selected_district
    st.session_state["last_division"] = selected_division
    st.session_state["last_sub_div"] = selected_sub_div
    
    with filter_col4:
        st.markdown(f'<div class="filter-label">{translations["select_village"]}</div>', unsafe_allow_html=True)
        selected_scheme = st.selectbox(
            '',
            options=options['schemes'],
            key="scheme_selectbox",
            label_visibility="collapsed"
        )
    
    return selected_district, selected_division, selected_sub_div, selected_scheme

def render_mobile_layout(data_processor, chart_builder, selected_scheme, current_row, translations):
    """Render mobile layout"""
    # Mobile header bar
    st.markdown(f'''
    <div class="mobile-header-bar">
        <span>{translations['report_date']}</span>
        <span style="color:#2d63c7;font-weight:bold;">{translations['title']}</span>
    </div>
    ''', unsafe_allow_html=True)
    
    # Scheme title and sub-division
    st.markdown(f'<div class="mobile-scheme-title">{selected_scheme}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="mobile-subdivision">[{current_row["Sub Division"]}]</div>', unsafe_allow_html=True)
    
    # Performance summary
    st.markdown(f'''
    <div class="mobile-summary-row">
        <span class="mobile-summary-icon">📊</span>
        <span class="mobile-summary-text">
            <span class="mobile-summary-title">{translations['performance_summary']}</span>
            <span class="mobile-summary-desc">{translations['performance_description']}</span>
        </span>
    </div>
    ''', unsafe_allow_html=True)
    
    # Format metrics and satisfaction for mobile
    metrics = data_processor.format_metrics(current_row, translations)
    satisfaction = data_processor.format_satisfaction(current_row, translations)
    
    # Mobile metrics grid
    st.markdown('<div class="mobile-metrics-grid">', unsafe_allow_html=True)
    for metric_key, metric_data in metrics.items():
        st.markdown(
            f'''<div class="mobile-metric-card">
                <div class="mobile-metric-icon">{metric_data['icon']}</div>
                <div class="mobile-metric-label">{metric_data['label']}</div>
                <div class="mobile-metric-value">{metric_data['value']}%</div>
            </div>''', 
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Mobile satisfaction
    satisfaction_html = f'''<div class="mobile-satisfaction-card">
        <div class="mobile-satisfaction-title">{translations['overall_satisfaction']}</div>
        <div class="mobile-satisfaction-row">'''
    
    for satisfaction_key, satisfaction_data in satisfaction.items():
        satisfaction_html += f'''<div class="mobile-satisfaction-box mobile-{satisfaction_data['class']}">
            <div class="mobile-satisfaction-emoji">{satisfaction_data['emoji']}</div>
            <div class="mobile-satisfaction-label">{satisfaction_data['label']}</div>
            <div class="mobile-satisfaction-value">{satisfaction_data['value']}%</div>
        </div>'''
    
    satisfaction_html += '</div></div>'
    st.markdown(satisfaction_html, unsafe_allow_html=True)
    
    # Mobile next steps
    current_suggestions = data_processor.get_suggestions(current_row, translations, SUGGESTION_THRESHOLDS)
    suggestions_html = f'''<div class="mobile-next-steps-card">
        <div class="mobile-next-steps-title">Suggested next steps</div>
        <ul style="margin:0 0 0 1rem;padding:0;">'''
    
    for suggestion in current_suggestions:
        suggestions_html += f'<li>{suggestion}</li>'
    
    suggestions_html += '</ul></div>'
    st.markdown(suggestions_html, unsafe_allow_html=True)
    
    # Mobile footer
    st.markdown(f'<div class="mobile-footer">{translations["footer"]}</div>', unsafe_allow_html=True)
    
    # Hide chart and table in mobile
    st.markdown('<style>.stPlotlyChart, .stDataFrame {display:none !important;}</style>', unsafe_allow_html=True)

def render_desktop_layout(data_processor, chart_builder, selected_scheme, current_row, translations):
    """Render desktop layout"""
    # Village name heading
    st.markdown(f"<h3 style='color: #1a237e; margin-top: 0.2rem; margin-bottom: 1.5rem;'>{selected_scheme}, {current_row['Sub Division']}</h3>", unsafe_allow_html=True)
    
    # Title Section
    st.markdown(
        f"""
        <div class="title-container">
            <h3 style="color: #2d63c7; display: flex; align-items: center; justify-content: center; gap: 10px;">
                <span>📈</span> {translations['performance_summary']}
            </h3>
            <p style="color: #666;">{translations['performance_description']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Format metrics and satisfaction
    metrics = data_processor.format_metrics(current_row, translations)
    satisfaction = data_processor.format_satisfaction(current_row, translations)
    
    # Key Metrics Section
    metrics_html = chart_builder.create_metrics_grid_html(metrics, translations)
    st.markdown(metrics_html, unsafe_allow_html=True)
    
    # Overall Satisfaction Section
    st.markdown(f"<h3 style='color: #1a237e; margin-top: 0.2rem; margin-bottom: 1.5rem;'>{translations['overall_satisfaction']}</h3>", unsafe_allow_html=True)
    satisfaction_html = chart_builder.create_satisfaction_grid_html(satisfaction, translations)
    st.markdown(satisfaction_html, unsafe_allow_html=True)
    
    # Add spacing before chart
    st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
    
    # Water Supply Chart
    ws_village = data_processor.get_water_supply_data(selected_scheme)
    if ws_village is not None:
        fig = chart_builder.create_water_supply_chart(ws_village, translations)
        st.markdown(f"<h4 style='color: #1a237e; margin-top: 2rem; margin-bottom: 1rem;'>{translations['water_supply_chart']}</h4>", unsafe_allow_html=True)
        st.markdown('<div style="overflow-x:auto; width:100%;">', unsafe_allow_html=True)
        st.plotly_chart(fig)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Suggested Next Steps
    current_suggestions = data_processor.get_suggestions(current_row, translations, SUGGESTION_THRESHOLDS)
    list_items = ''.join([f"<li style=\"color: #000;\">{suggestion}</li>" for suggestion in current_suggestions])
    
    st.markdown(
        f"""
        <div class="suggested-steps" style="color: #000;">
            <h3 style="margin-top: 0; color: #000;">{translations['next_steps']}</h3>
            <ul style="color: #000; margin-bottom: 0;">
                {list_items}
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Footer
    st.markdown("---")
    st.markdown(f"<p style='text-align: right; color: #666;'>{translations['footer']}</p>", unsafe_allow_html=True)

def main():
    """Main application function"""
    # Initialize app
    initialize_app()
    
    # Initialize components
    data_processor = DataProcessor()
    chart_builder = ChartBuilder()
    
    # Setup language toggle and get translations
    translations = setup_language_toggle()
    
    # Render header
    render_header(translations)
    
    # Render filters and get selections
    selected_district, selected_division, selected_sub_div, selected_scheme = render_filters(data_processor, translations)
    
    # Get current row data
    current_row = data_processor.get_filtered_data(selected_district, selected_division, selected_sub_div, selected_scheme)
    
    if current_row is None:
        st.error("No data found for the selected filters.")
        return
    
    # Mobile detection logic
    if 'force_mobile' not in st.session_state:
        try:
            col1, col2 = st.columns([1, 1])
            st.session_state['force_mobile'] = False
        except Exception:
            st.session_state['force_mobile'] = False
    
    # Render appropriate layout
    if st.session_state.get('force_mobile', False):
        render_mobile_layout(data_processor, chart_builder, selected_scheme, current_row, translations)
    else:
        render_desktop_layout(data_processor, chart_builder, selected_scheme, current_row, translations)

if __name__ == "__main__":
    main() 