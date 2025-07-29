# Constants for the Water Supply Dashboard

# File paths
EXCEL_PATH = 'data/IVR PoC - Scheme Report Sample.xlsx'
SHEET_NAME = 'IVR PoC - Scheme Report'
WATER_SUPPLY_SHEET = 'Water Supply - Last 7 days'

# Page configuration
PAGE_CONFIG = {
    'page_title': "Scheme Report",
    'page_icon': "💧",
    'layout': "wide",
    'initial_sidebar_state': "collapsed"
}

# Data columns
METRICS_COLS = [
    'Gets Water Daily %',
    'Gets Water at Same Time %',
    'Satisfied with Quantity %',
    'Satisfied with Quality %',
    'Overall Happy %',
    'Overall Neutral %',
    'Overall Sad %',
    'Sub Division',
]

# Chart colors
CHART_COLORS = {
    'bar_color': '#7ec8e3',  # light blue
    'line_color': '#FFD700',  # yellow
    'text_color': 'white',
    'line_text_color': '#FFD700'
}

# Chart styling
CHART_STYLING = {
    'bar_opacity': 0.85,
    'marker_size': 8,
    'text_font_size': 11,
    'line_text_font_size': 14,
    'chart_width': 700,
    'chart_height': 400,
    'margin': {'l': 20, 'r': 20, 't': 110, 'b': 80}
}

# Language translations
TRANSLATIONS = {
    'en': {
        'title': 'Jal Jeevan Mission Assam',
        'filter_question': 'Which village\'s performance do you want to see?',
        'district': 'District',
        'division': 'Division',
        'select_village': 'Village',
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
        'district': 'জিলা',
        'division': 'বিভাগ',
        'select_village': 'গাঁও',
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

# Suggestion thresholds
SUGGESTION_THRESHOLDS = {
    'low_satisfaction': 50,  # Overall Happy % threshold
    'timing_issues': 70,     # Gets Water at Same Time % threshold
    'quality_issues': 70     # Satisfied with Quality % threshold
} 