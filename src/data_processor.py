# Data processing components for the Water Supply Dashboard

import pandas as pd
from constants import EXCEL_PATH, SHEET_NAME, WATER_SUPPLY_SHEET, METRICS_COLS

class DataProcessor:
    """Handles all data loading and processing operations"""
    
    def __init__(self):
        self.df = None
        self.water_supply_df = None
        self._load_data()
    
    def _load_data(self):
        """Load data from Excel files"""
        try:
            # Load main data
            self.df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)
            
            # Load water supply data
            self.water_supply_df = pd.read_excel(EXCEL_PATH, sheet_name=WATER_SUPPLY_SHEET)
            
            # Prepare data: ensure all relevant columns are present and fill NAs
            self.df = self.df.fillna(0)
            self.water_supply_df = self.water_supply_df.fillna(0)
            
        except Exception as e:
            print(f"Error loading data: {e}")
            # Create empty DataFrames as fallback
            self.df = pd.DataFrame()
            self.water_supply_df = pd.DataFrame()
    
    def get_filter_options(self, selected_district=None, selected_division=None, selected_sub_div=None):
        """Get filter options based on current selections"""
        options = {}
        
        # Get districts
        options['districts'] = self.df['District'].unique().tolist()
        
        # Get divisions based on selected district
        if selected_district:
            filtered_by_district = self.df[self.df['District'] == selected_district]
            options['divisions'] = filtered_by_district['Division'].unique().tolist()
        else:
            options['divisions'] = []
        
        # Get sub-divisions based on selected district and division
        if selected_district and selected_division:
            filtered_by_division = filtered_by_district[filtered_by_district['Division'] == selected_division]
            options['sub_divisions'] = filtered_by_division['Sub Division'].unique().tolist()
        else:
            options['sub_divisions'] = []
        
        # Get schemes based on all selections
        if selected_district and selected_division and selected_sub_div:
            filtered_df = filtered_by_division[filtered_by_division['Sub Division'] == selected_sub_div]
            options['schemes'] = filtered_df['Scheme Name'].unique().tolist()
        else:
            options['schemes'] = []
        
        return options
    
    def get_filtered_data(self, selected_district, selected_division, selected_sub_div, selected_scheme):
        """Get filtered data based on selections"""
        filtered_df = self.df[
            (self.df['District'] == selected_district) &
            (self.df['Division'] == selected_division) &
            (self.df['Sub Division'] == selected_sub_div) &
            (self.df['Scheme Name'] == selected_scheme)
        ]
        
        if filtered_df.empty:
            return None
        
        return filtered_df.iloc[0]
    
    def get_water_supply_data(self, selected_scheme):
        """Get water supply data for a specific scheme"""
        ws_village = self.water_supply_df[self.water_supply_df['Scheme Name'] == selected_scheme].copy()
        
        if ws_village.empty:
            return None
        
        # Ensure data is properly formatted
        ws_village['Expected water delivery'] = ws_village['Expected water delivery'].fillna(0)
        ws_village['Water Supplied (in kl)'] = ws_village['Water Supplied (in kl)'].fillna(0)
        
        return ws_village
    
    def get_suggestions(self, current_row, translations, thresholds):
        """Generate suggestions based on current metrics"""
        suggestions = {
            'low_satisfaction': translations['low_satisfaction'],
            'timing_issues': translations['timing_issues'],
            'quality_issues': translations['quality_issues'],
            'general': translations['general']
        }
        
        current_suggestions = []
        
        # Check thresholds and add suggestions
        if current_row['Overall Happy %']*100 < thresholds['low_satisfaction']:
            current_suggestions.append(suggestions['low_satisfaction'])
        
        if current_row['Gets Water at Same Time %']*100 < thresholds['timing_issues']:
            current_suggestions.append(suggestions['timing_issues'])
        
        if current_row['Satisfied with Quality %']*100 < thresholds['quality_issues']:
            current_suggestions.append(suggestions['quality_issues'])
        
        # Always add general suggestion
        current_suggestions.append(suggestions['general'])
        
        return current_suggestions
    
    def format_metrics(self, current_row, translations):
        """Format metrics for display"""
        metrics = {
            'gets_water_daily': {
                'label': translations['gets_water_daily'],
                'value': int(current_row['Gets Water Daily %']*100),
                'icon': '💧'
            },
            'same_time': {
                'label': translations['same_time'],
                'value': int(current_row['Gets Water at Same Time %']*100),
                'icon': '⏰'
            },
            'satisfied_quantity': {
                'label': translations['satisfied_quantity'],
                'value': int(current_row['Satisfied with Quantity %']*100),
                'icon': '🚰'
            },
            'satisfied_quality': {
                'label': translations['satisfied_quality'],
                'value': int(current_row['Satisfied with Quality %']*100),
                'icon': '✅'
            }
        }
        
        return metrics
    
    def format_satisfaction(self, current_row, translations):
        """Format satisfaction metrics for display"""
        satisfaction = {
            'happy': {
                'label': translations['happy'],
                'value': int(current_row['Overall Happy %']*100),
                'emoji': '😊',
                'class': 'satisfaction-happy'
            },
            'neutral': {
                'label': translations['neutral'],
                'value': int(current_row['Overall Neutral %']*100),
                'emoji': '😐',
                'class': 'satisfaction-neutral'
            },
            'sad': {
                'label': translations['sad'],
                'value': int(current_row['Overall Sad %']*100),
                'emoji': '😔',
                'class': 'satisfaction-sad'
            }
        }
        
        return satisfaction 