# Styling components for the Water Supply Dashboard

def get_main_css():
    """Return the main CSS styling for the dashboard"""
    return """
    <style>
    .stApp { background-color: #f0f6ff !important; }
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
    
    /* Responsive filter spacing */
    @media (max-width: 1200px) {
        .filter-label {
            font-size: 14px;
            margin-bottom: 0.2rem;
        }
        .stSelectbox {
            margin-bottom: 0.5rem !important;
        }
    }
    
    @media (max-width: 768px) {
        .filter-label {
            font-size: 13px;
            margin-bottom: 0.15rem;
        }
        .stSelectbox {
            margin-bottom: 0.3rem !important;
        }
    }
    
    @media (max-width: 600px) {
        .filter-label {
            font-size: 12px;
            margin-bottom: 0.1rem;
        }
        .stSelectbox {
            margin-bottom: 0.2rem !important;
        }
    }
    </style>
    """

def get_metrics_grid_css():
    """Return CSS for metrics grid layout"""
    return '''
    <style>
    .metrics-grid, .mobile-metrics-grid {
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        gap: 1rem !important;
        margin-bottom: 1.2rem !important;
    }
    .metric-card, .mobile-metric-card {
        background: #fff;
        border-radius: 16px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.07);
        padding: 1.2rem 0.5rem 0.7rem 0.5rem;
        text-align: center;
        min-width: 0;
    }
    @media (max-width: 600px) {
        .metrics-grid, .mobile-metrics-grid {
            grid-template-columns: 1fr 1fr !important;
        }
    }
    </style>
    '''

def get_satisfaction_grid_css():
    """Return CSS for satisfaction grid layout"""
    return '''
    <style>
    .satisfaction-grid {
        display: grid !important;
        grid-template-columns: 1fr 1fr 1fr !important;
        gap: 1rem !important;
        margin-bottom: 1.2rem !important;
    }
    .satisfaction-card {
        border-radius: 12px;
        padding: 0.7rem 0.2rem;
        text-align: center;
        font-size: 1rem;
    }
    .satisfaction-happy { background: #dcf7f3; }
    .satisfaction-neutral { background: #ffefd5; }
    .satisfaction-sad { background: #ffd4d4; }
    .satisfaction-emoji {
        font-size: 1.5rem;
        margin-bottom: 0.2rem;
    }
    .satisfaction-label {
        font-weight: bold;
        color: #222;
    }
    .satisfaction-value {
        font-size: 1.2rem;
        font-weight: bold;
        color: #222;
    }
    @media (max-width: 600px) {
        .satisfaction-grid {
            grid-template-columns: 1fr 1fr 1fr !important;
        }
    }
    </style>
    '''

def get_mobile_layout_css():
    """Return CSS for mobile layout"""
    return '''
    <style>
    @media (max-width: 600px) {
        body, .stApp { background: #f0f6ff !important; }
        .mobile-header-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #fff;
            border-radius: 8px;
            margin: 0.5rem 0 1rem 0;
            padding: 0.7rem 1rem;
            border-left: 6px solid #2d63c7;
            font-size: 1rem;
        }
        .mobile-scheme-title {
            font-size: 2rem !important;
            font-weight: bold;
            color: #2d63c7;
            margin-bottom: 0.2rem;
        }
        .mobile-subdivision {
            font-size: 1.1rem !important;
            color: #888;
            margin-bottom: 1.2rem;
        }
        .mobile-summary-row {
            display: flex;
            align-items: flex-start;
            gap: 0.7rem;
            margin-bottom: 1.2rem;
        }
        .mobile-summary-icon {
            font-size: 2.2rem;
            margin-right: 0.5rem;
        }
        .mobile-summary-text {
            display: flex;
            flex-direction: column;
        }
        .mobile-summary-title {
            font-size: 1.2rem;
            font-weight: bold;
            color: #2d63c7;
        }
        .mobile-summary-desc {
            font-size: 1rem;
            color: #5a9cf8;
        }
        .mobile-metrics-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin-bottom: 1.2rem;
        }
        .mobile-metric-card {
            background: #fff;
            border-radius: 16px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.07);
            padding: 1.2rem 0.5rem 0.7rem 0.5rem;
            text-align: center;
            min-width: 0;
        }
        .mobile-metric-icon {
            font-size: 2rem;
            margin-bottom: 0.2rem;
        }
        .mobile-metric-label {
            font-size: 1rem;
            color: #222;
            margin-bottom: 0.2rem;
        }
        .mobile-metric-value {
            font-size: 2rem;
            font-weight: bold;
            color: #222;
        }
        .mobile-satisfaction-card {
            background: #fff;
            border-radius: 16px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.07);
            padding: 1rem 0.5rem 0.7rem 0.5rem;
            margin-bottom: 1.2rem;
        }
        .mobile-satisfaction-title {
            font-size: 1.1rem;
            font-weight: bold;
            color: #222;
            margin-bottom: 0.7rem;
        }
        .mobile-satisfaction-row {
            display: flex;
            gap: 0.7rem;
        }
        .mobile-satisfaction-box {
            flex: 1;
            border-radius: 12px;
            padding: 0.7rem 0.2rem;
            text-align: center;
            font-size: 1rem;
        }
        .mobile-satisfaction-happy { background: #dcf7f3; }
        .mobile-satisfaction-neutral { background: #ffefd5; }
        .mobile-satisfaction-sad { background: #ffd4d4; }
        .mobile-satisfaction-emoji {
            font-size: 1.5rem;
            margin-bottom: 0.2rem;
        }
        .mobile-satisfaction-label {
            font-weight: bold;
            color: #222;
        }
        .mobile-satisfaction-value {
            font-size: 1.2rem;
            font-weight: bold;
            color: #222;
        }
        .mobile-next-steps-card {
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.07);
            padding: 1rem 1rem 1rem 1.2rem;
            border-left: 6px solid #2d63c7;
            margin-bottom: 1.2rem;
        }
        .mobile-next-steps-title {
            font-size: 1.1rem;
            font-weight: bold;
            color: #222;
            margin-bottom: 0.5rem;
        }
        .mobile-footer {
            text-align: center;
            color: #888;
            font-size: 1rem;
            margin-top: 2rem;
        }
        /* Hide chart and table in mobile */
        .mobile-hide { display: none !important; }
    }
    </style>
    '''

def get_toggle_switch_css():
    """Return CSS for toggle switch styling"""
    return '''
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
    '''

def get_container_css():
    """Return CSS for container styling"""
    return """
        <style>
        .stApp { margin-top: -100px !important; }
        .main .block-container { padding-top: 0 !important; margin-top: 0 !important; }
        </style>
    """ 