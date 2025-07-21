# filepath: /Users/a0s17ku/Projects/water-supply-dashboard/src/app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Language translations
translations = {
    'en': {
        'title': 'Jal Jeevan Mission Assam',
        'filter_question': 'Which village\'s performance do you want to see?',
        'select_village': 'Select Village',
        'performance_summary': 'Scheme Performance Summary',
        'performance_description': 'Review your metrics below and follow the next steps',
        'gets_water_daily': 'Gets Water Daily',
        'satisfied_quantity': 'Satisfied with Quantity',
        'same_time': 'Gets Water at Same Time',
        'satisfied_quality': 'Satisfied with Quality',
        'overall_satisfaction': 'Overall Satisfaction',
        'happy': 'Happy',
        'neutral': 'Neutral',
        'sad': 'Sad',
        'disgruntled_consumers': 'Disgruntled Consumers',
        'serial_number': 'Serial No',
        'consumer_name': 'Consumer Name',
        'consumer_phone': 'Consumer Phone Number',
        'water_supply_chart': 'Expected vs Received Water Supply',
        'date': 'Date',
        'volume_kl': 'Volume (kl)',
        'expected_water': 'Expected Water Supply',
        'supplied_water': 'Supplied Water (kl)',
        'next_steps': 'Next Steps',
        'low_satisfaction': 'Contact WUC and community members to see if improvements can be made',
        'timing_issues': 'Work with operators to establish a regular water supply schedule',
        'quality_issues': 'Test water quality and take necessary remedial measures',
        'general': 'Contact your SO to identify and resolve your scheme issues in time',
        'report_date': 'Report date: 04 Jun 2025',
        'footer': 'June 2025 | PHED',
        'sub_division': 'Sub Division'
    },
    'as': {
        'title': 'জল জীৱন মিছন অসম',
        'filter_question': 'কোন গাঁৱৰ কাৰ্যক্ষমতা আপুনি চাব বিচাৰে?',
        'select_village': 'গাঁও বাছনি কৰক',
        'performance_summary': 'আঁচনিৰ কাৰ্যক্ষমতাৰ সংক্ষিপ্তসাৰ',
        'performance_description': 'তলত আপোনাৰ মেট্ৰিকসমূহ পৰ্যালোচনা কৰক আৰু পৰৱৰ্তী পদক্ষেপসমূহ অনুসৰণ কৰক',
        'gets_water_daily': 'দৈনিক পানী পায়',
        'satisfied_quantity': 'পৰিমাণত সন্তুষ্ট',
        'same_time': 'একে সময়ত দৈনিক পানী পায়',
        'satisfied_quality': 'গুণগত মানত সন্তুষ্ট',
        'overall_satisfaction': 'মুঠ সন্তুষ্টি',
        'happy': 'সুখী',
        'neutral': 'নিৰপেক্ষ',
        'sad': 'দুঃখী',
        'disgruntled_consumers': 'অসন্তুষ্ট গ্ৰাহকসকল',
        'serial_number': 'ক্ৰমিক নম্বৰ',
        'consumer_name': 'গ্ৰাহকৰ নাম',
        'consumer_phone': 'গ্ৰাহকৰ ফোন নম্বৰ',
        'water_supply_chart': 'প্ৰত্যাশিত বনাম প্ৰাপ্ত পানী যোগান',
        'date': 'তাৰিখ',
        'volume_kl': 'আয়তন (kl)',
        'expected_water': 'প্ৰত্যাশিত পানী যোগান',
        'supplied_water': 'যোগান দিয়া পানী (kl)',
        'next_steps': 'পৰৱৰ্তী পদক্ষেপসমূহ',
        'low_satisfaction': 'WUC আৰু সম্প্ৰদায়ৰ সদস্যসকলৰ সৈতে যোগাযোগ কৰক, উন্নতি কৰিব পৰা যায় নেকি চাওক',
        'timing_issues': 'অপাৰেটৰসকলৰ সৈতে কাম কৰক যাতে এটা নিয়মীয়া পানী যোগান সময়সূচী স্থাপন কৰিব পৰা যায়',
        'quality_issues': 'পানীৰ গুণগত মান পৰীক্ষা কৰক আৰু প্ৰয়োজনীয় চিকিৎসা ব্যৱস্থা গ্ৰহণ কৰক',
        'general': 'আপোনাৰ আঁচনিৰ সমস্যাসমূহ সময়মতে চিনাক্ত আৰু সমাধান কৰিবলৈ আপোনাৰ SO-ৰ সৈতে যোগাযোগ কৰক',
        'report_date': 'Report date: 04 Jun 2025',
        'footer': 'June 2025 | PHED',
        'sub_division': 'উপ-বিভাগ'
    }
}

# Load data from Excel
EXCEL_PATH = 'data/IVR PoC - Scheme Report Sample.xlsx'
SHEET_NAME = 'IVR PoC - Scheme Report'
df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)

# Prepare data: ensure all relevant columns are present and fill NAs if any
metrics_cols = [
    'Gets Water Daily %',
    'Gets Water at Same Time %',
    'Satisfied with Quantity %',
    'Satisfied with Quality %',
    'Overall Happy %',
    'Overall Neutral %',
    'Overall Sad %',
    'Sub Division',
]
df = df.fillna(0)

# Load disgruntled consumers data
dis_df = pd.read_excel('data/IVR PoC - Scheme Report Sample.xlsx', sheet_name='IVR PoC - Disgruntled Consumers')

# Set page configuration
st.set_page_config(
    page_title="Scheme Report",
    page_icon="💧",
    layout="wide"
)

# Custom CSS for toggle switch and layout
st.markdown("""
    <style>
    .stApp { background-color: #f0f6ff !important; }
    .reportview-container .main .block-container { padding: 1rem; max-width: 1200px; background-color: #f0f6ff; }
    .header-container { display: flex; justify-content: space-between; align-items: start; margin-bottom: 2rem; }
    .title-container { text-align: center; margin: 2rem 0; }
    .metric-card { background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); text-align: center; }
    .metric-value { font-size: 3.5rem; font-weight: bold; color: #2d63c7; margin: 1rem 0; }
    .metric-label { font-size: 1.2rem; color: #555; }
    .emoji-card { padding: 1rem; border-radius: 10px; text-align: center; }
    .emoji { font-size: 2.5rem; margin-bottom: 0.5rem; }
    .suggested-steps { background: white; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #2d63c7; margin-top: 2rem; }
    h1, h2, h3 { color: #2d63c7; font-weight: normal; }
    
    /* Toggle Switch Styles */
    .toggle-container {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 1rem;
        justify-content: flex-end;
    }
    
    .toggle-switch {
        position: relative;
        width: 50px;
        height: 24px;
        background-color: #ccc;
        border-radius: 12px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    
    .toggle-switch.active {
        background-color: #000;
    }
    
    .toggle-thumb {
        position: absolute;
        top: 2px;
        left: 2px;
        width: 20px;
        height: 20px;
        background-color: white;
        border-radius: 50%;
        transition: transform 0.3s;
    }
    
    .toggle-switch.active .toggle-thumb {
        transform: translateX(26px);
    }
    
    .language-label {
        font-weight: bold;
        color: #333;
        font-size: 14px;
    }
    .filter-label {
        font-weight: bold;
        color: #1a237e !important;
        margin-bottom: 0.25rem;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# Add custom CSS for mobile responsiveness (smaller font, wrapping)
st.markdown('''
    <style>
    /* Make Streamlit dataframe font smaller and allow wrapping for mobile */
    .stDataFrame thead tr th, .stDataFrame tbody tr td {
        font-size: 12px !important;
        white-space: pre-line !important;
        word-break: break-word !important;
        max-width: 120px;
    }
    @media (max-width: 600px) {
        .stDataFrame thead tr th, .stDataFrame tbody tr td {
            font-size: 10px !important;
            max-width: 80px;
        }
    }
    </style>
''', unsafe_allow_html=True)

# Ensure language is initialized in session state
if 'language' not in st.session_state:
    st.session_state['language'] = 'Assamese'

# Language toggle using a Streamlit-native toggle at the top right with improved logic and darker styling
col1, col2, col3 = st.columns([6, 1, 2])
with col3:
    # Add custom CSS for dark background and white text for the toggle itself
    st.markdown('''
        <style>
        div[data-testid="stToggle"], div[data-testid="stCheckbox"] {
            background: #222 !important;
            border-radius: 18px !important;
            padding: 6px 18px 6px 18px !important;
            display: inline-block !important;
            margin-bottom: 0.5rem !important;
        }
        div[data-testid="stToggle"] label, div[data-testid="stCheckbox"] label {
            color: #fff !important;
            font-weight: bold !important;
            font-size: 18px !important;
        }
        </style>
    ''', unsafe_allow_html=True)
    # Language toggle with both languages displayed
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

# Get current language code
lang_code = 'as' if st.session_state.language == 'Assamese' else 'en'
t = translations[lang_code]

# Header with Scheme Selection
st.markdown(
    f"""
    <div class="header-container" style="margin-bottom: 0.5rem; margin-top: 0;">
        <div style="flex: 1;"></div>
        <div style="text-align: right;">
            <p style="color: #666; margin: 0;">{t['report_date']}</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Scheme Filter
# 1. Move 'Jal Jeevan Mission Assam' to the very top
st.markdown(f"""
    <h1 style='color: #2d63c7; margin-bottom: 0.1rem; margin-top: 0; text-align: center;'>{t['title']}</h1>
""", unsafe_allow_html=True)

# Display filter question above the two filters
st.markdown(f"<h4 style='color: #000; margin-top: 1.2rem; margin-bottom: 0.5rem;'>{t['filter_question']}</h4>", unsafe_allow_html=True)
# 2. Add filter by section for sub division and villages (side by side, never stacked)
filter_col1, filter_col2 = st.columns([1, 1], gap="large")
with filter_col1:
    st.markdown(f'<div class="filter-label">{t["sub_division"]}</div>', unsafe_allow_html=True)
    sub_divisions = df['Sub Division'].unique().tolist()
    selected_sub_div = st.selectbox(
        '',
        options=sub_divisions,
        key='sub_division_selectbox',
        label_visibility='collapsed'
    )

# Filter the dataframe based on selected sub-division
filtered_df = df[df['Sub Division'] == selected_sub_div]
scheme_names = filtered_df['Scheme Name'].unique().tolist()

# Reset the selected scheme if the sub-division changes
if "last_sub_div" not in st.session_state or st.session_state.last_sub_div != selected_sub_div:
    st.session_state["village_selectbox"] = scheme_names[0] if scheme_names else None
st.session_state["last_sub_div"] = selected_sub_div

with filter_col2:
    st.markdown(f'<div class="filter-label">{t["select_village"]}</div>', unsafe_allow_html=True)
    selected_scheme = st.selectbox(
        '',
        options=scheme_names,
        key="village_selectbox",
        label_visibility="collapsed"
    )
current_row = filtered_df[filtered_df['Scheme Name'] == selected_scheme].iloc[0]

# 3. Village name heading in darker color, with less top margin to reduce gap
st.markdown(f"<h3 style='color: #1a237e; margin-top: 0.2rem; margin-bottom: 1.5rem;'>{selected_scheme}, {current_row['Sub Division']}</h3>", unsafe_allow_html=True)

# Title Section (remove village name and sub division from here)
st.markdown(
    f"""
    <div class="title-container">
        <h3 style="color: #2d63c7; display: flex; align-items: center; justify-content: center; gap: 10px;">
            <span>📈</span> {t['performance_summary']}
        </h3>
        <p style="color: #666;">{t['performance_description']}</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Key Metrics Section
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div style="font-size: 2rem;">💧</div>
            <div class="metric-value">{current_row['Gets Water Daily %']*100:.0f}%</div>
            <div class="metric-label">{t['gets_water_daily']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class="metric-card" style="margin-top: 1rem;">
            <div style="font-size: 2rem;">🚰</div>
            <div class="metric-value">{current_row['Satisfied with Quantity %']*100:.0f}%</div>
            <div class="metric-label">{t['satisfied_quantity']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="metric-card">
            <div style="font-size: 2rem;">⏰</div>
            <div class="metric-value">{current_row['Gets Water at Same Time %']*100:.0f}%</div>
            <div class="metric-label">{t['same_time']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class="metric-card" style="margin-top: 1rem;">
            <div style="font-size: 2rem;">✅</div>
            <div class="metric-value">{current_row['Satisfied with Quality %']*100:.0f}%</div>
            <div class="metric-label">{t['satisfied_quality']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Overall Satisfaction Section
st.markdown(f"<h3 style='color: #1a237e; margin-top: 0.2rem; margin-bottom: 1.5rem;'>{t['overall_satisfaction']}</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="emoji-card" style="background: #dcf7f3;">
            <div class="emoji">😊</div>
            <div style="font-weight: bold; color: #000;">{t['happy']}</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: #000;">{current_row['Overall Happy %']*100:.0f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="emoji-card" style="background: #ffefd5;">
            <div class="emoji">😐</div>
            <div style="font-weight: bold; color: #000;">{t['neutral']}</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: #000;">{current_row['Overall Neutral %']*100:.0f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="emoji-card" style="background: #ffd4d4;">
            <div class="emoji">😔</div>
            <div style="font-weight: bold; color: #000;">{t['sad']}</div>
            <div style="font-size: 1.5rem; font-weight: bold; color: #000;">{current_row['Overall Sad %']*100:.0f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Disgruntled consumers table (moved up)
st.markdown(f"<h4 style='color: #1a237e; margin-top: 2rem;'>{t['disgruntled_consumers']}</h4>", unsafe_allow_html=True)
dis_table = dis_df[dis_df['Scheme Name'] == selected_scheme][[
    'Consumer Name',
    'Consumer Ph Number',
    'Gets Water Daily',
    'Gets Water Daily at Same Time',
    'Satisfied with quantity',
    'Satisfied with Quality',
    'Overall Satisfaction'
]].reset_index(drop=True)
dis_table.insert(0, 'Sl No', dis_table.index + 1)
dis_table = dis_table.rename(columns={
    'Sl No': t['serial_number'],
    'Consumer Name': t['consumer_name'],
    'Consumer Ph Number': t['consumer_phone'],
    'Gets Water Daily': t['gets_water_daily'],
    'Gets Water Daily at Same Time': t['same_time'],
    'Satisfied with quantity': t['satisfied_quantity'],
    'Satisfied with Quality': t['satisfied_quality'],
    'Overall Satisfaction': t['overall_satisfaction'],
})
# Show the table with responsive width (fits screen size) and hide the default index
st.dataframe(dis_table, use_container_width=True, hide_index=True)

# Add spacing before the line chart to prevent overlap
st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)

# After the disgruntled consumers table, add the expected vs received water supply line graph
import plotly.graph_objects as go
ws_df = pd.read_excel('data/IVR PoC - Scheme Report Sample.xlsx', sheet_name='Water Supply - Last 7 days')
ws_village = ws_df[ws_df['Scheme Name'] == selected_scheme].copy()
ws_village['Expected water delivery'] = ws_village['Expected water delivery'].fillna(0)
ws_village['Water Supplied (in kl)'] = ws_village['Water Supplied (in kl)'].fillna(0)
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=ws_village['Date (Prev 7 days)'],
    y=ws_village['Expected water delivery'],
    mode='lines+markers+text',
    name=t['expected_water'],
    line=dict(color='#2ecc40'),  # green
    text=ws_village['Expected water delivery'],
    textposition='top center',
    hoverinfo='skip'
))
fig.add_trace(go.Scatter(
    x=ws_village['Date (Prev 7 days)'],
    y=ws_village['Water Supplied (in kl)'],
    mode='lines+markers+text',
    name=t['supplied_water'],
    line=dict(color='#ff7f0e'),
    text=ws_village['Water Supplied (in kl)'],
    textposition='top center',
    hoverinfo='skip'
))
fig.update_layout(
    title=t['water_supply_chart'],
    xaxis_title=t['date'],
    yaxis_title=t['volume_kl'],
    legend_title='',
    template='simple_white',
    margin=dict(l=20, r=20, t=40, b=20)
)
st.plotly_chart(fig, use_container_width=True)

# Suggested Next Steps
suggestions = {
    'low_satisfaction': t['low_satisfaction'],
    'timing_issues': t['timing_issues'],
    'quality_issues': t['quality_issues'],
    'general': t['general']
}

# Dynamic suggestions based on metrics
current_suggestions = []
if current_row['Overall Happy %']*100 < 50:
    current_suggestions.append(suggestions['low_satisfaction'])
if current_row['Gets Water at Same Time %']*100 < 70:
    current_suggestions.append(suggestions['timing_issues'])
if current_row['Satisfied with Quality %']*100 < 70:
    current_suggestions.append(suggestions['quality_issues'])
current_suggestions.append(suggestions['general'])

# Build the list items string with double quotes for style attribute
list_items = ''.join([f"<li style=\"color: #000;\">{suggestion}</li>" for suggestion in current_suggestions])
st.markdown(
    f"""
    <div class="suggested-steps" style="color: #000;">
        <h3 style="margin-top: 0; color: #000;">{t['next_steps']}</h3>
        <ul style="color: #000; margin-bottom: 0;">
            {list_items}
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown("---")
st.markdown(f"<p style='text-align: right; color: #666;'>{t['footer']}</p>", unsafe_allow_html=True)