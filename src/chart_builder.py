# Chart building components for the Water Supply Dashboard

import plotly.graph_objects as go
from constants import CHART_COLORS, CHART_STYLING

class ChartBuilder:
    """Handles all chart creation and styling operations"""
    
    def __init__(self):
        self.colors = CHART_COLORS
        self.styling = CHART_STYLING
    
    def create_water_supply_chart(self, ws_village, translations):
        """Create the water supply comparison chart"""
        fig = go.Figure()
        
        # Bar for expected supply (show value on top of bar)
        fig.add_trace(go.Bar(
            x=ws_village['Date (Prev 7 days)'],
            y=ws_village['Expected water delivery'],
            name=translations['expected_water'],
            marker_color=self.colors['bar_color'],
            text=ws_village['Expected water delivery'],
            textposition='outside',
            textfont=dict(size=self.styling['text_font_size'], color=self.colors['text_color']),
            hovertemplate=f"{translations['expected_water']}: %{{y}}<extra></extra>",
            opacity=self.styling['bar_opacity'],
            cliponaxis=False
        ))
        
        # Line for actual supply (show value above marker)
        fig.add_trace(go.Scatter(
            x=ws_village['Date (Prev 7 days)'],
            y=ws_village['Water Supplied (in kl)'],
            mode='lines+markers+text',
            name=translations['supplied_water'],
            line=dict(color=self.colors['line_color']),
            marker=dict(size=self.styling['marker_size'], color=self.colors['line_color']),
            text=["<br>" + f"{v:.2f}" for v in ws_village['Water Supplied (in kl)']],
            textposition='top center',
            textfont=dict(size=self.styling['line_text_font_size'], color=self.colors['line_text_color']),
            texttemplate='%{text}',
            hovertemplate=f"{translations['supplied_water']}: %{{y}}<extra></extra>"
        ))
        
        # Calculate dynamic margins and y-axis range
        max_expected = ws_village['Expected water delivery'].max()
        max_actual = ws_village['Water Supplied (in kl)'].max()
        
        # Adjust top margin based on data values
        if max_expected > 80 or max_actual > 80:
            top_margin = 140
        elif max_expected > 60 or max_actual > 60:
            top_margin = 120
        else:
            top_margin = 110
        
        # Calculate y-axis range
        max_y = max(max_expected, max_actual)
        yaxis_max = max_y * 1.2 if max_y > 0 else 10
        
        # Update layout
        fig.update_layout(
            barmode='group',
            title=translations['water_supply_chart'],
            xaxis_title=translations['date'],
            yaxis_title=translations['volume_kl'],
            legend_title='',
            legend=dict(
                orientation='v',
                yanchor='top',
                y=1.15,
                xanchor='left',
                x=0
            ),
            template='simple_white',
            margin=dict(
                l=self.styling['margin']['l'],
                r=self.styling['margin']['r'],
                t=top_margin,
                b=self.styling['margin']['b']
            ),
            width=self.styling['chart_width'],
            height=self.styling['chart_height'],
            yaxis=dict(range=[0, yaxis_max])
        )
        
        return fig
    
    def create_metrics_grid_html(self, metrics, translations):
        """Create HTML for metrics grid"""
        html_template = '''
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-icon">{icon1}</div>
                <div class="metric-label">{label1}</div>
                <div class="metric-value">{value1}%</div>
            </div>
            <div class="metric-card">
                <div class="metric-icon">{icon2}</div>
                <div class="metric-label">{label2}</div>
                <div class="metric-value">{value2}%</div>
            </div>
            <div class="metric-card">
                <div class="metric-icon">{icon3}</div>
                <div class="metric-label">{label3}</div>
                <div class="metric-value">{value3}%</div>
            </div>
            <div class="metric-card">
                <div class="metric-icon">{icon4}</div>
                <div class="metric-label">{label4}</div>
                <div class="metric-value">{value4}%</div>
            </div>
        </div>
        '''
        
        return html_template.format(
            icon1=metrics['gets_water_daily']['icon'],
            label1=metrics['gets_water_daily']['label'],
            value1=metrics['gets_water_daily']['value'],
            icon2=metrics['same_time']['icon'],
            label2=metrics['same_time']['label'],
            value2=metrics['same_time']['value'],
            icon3=metrics['satisfied_quantity']['icon'],
            label3=metrics['satisfied_quantity']['label'],
            value3=metrics['satisfied_quantity']['value'],
            icon4=metrics['satisfied_quality']['icon'],
            label4=metrics['satisfied_quality']['label'],
            value4=metrics['satisfied_quality']['value']
        )
    
    def create_satisfaction_grid_html(self, satisfaction, translations):
        """Create HTML for satisfaction grid"""
        html_template = '''
        <div class="satisfaction-grid">
            <div class="satisfaction-card {class1}">
                <div class="satisfaction-emoji">{emoji1}</div>
                <div class="satisfaction-label">{label1}</div>
                <div class="satisfaction-value">{value1}%</div>
            </div>
            <div class="satisfaction-card {class2}">
                <div class="satisfaction-emoji">{emoji2}</div>
                <div class="satisfaction-label">{label2}</div>
                <div class="satisfaction-value">{value2}%</div>
            </div>
            <div class="satisfaction-card {class3}">
                <div class="satisfaction-emoji">{emoji3}</div>
                <div class="satisfaction-label">{label3}</div>
                <div class="satisfaction-value">{value3}%</div>
            </div>
        </div>
        '''
        
        return html_template.format(
            emoji1=satisfaction['happy']['emoji'],
            label1=satisfaction['happy']['label'],
            value1=satisfaction['happy']['value'],
            class1=satisfaction['happy']['class'],
            emoji2=satisfaction['neutral']['emoji'],
            label2=satisfaction['neutral']['label'],
            value2=satisfaction['neutral']['value'],
            class2=satisfaction['neutral']['class'],
            emoji3=satisfaction['sad']['emoji'],
            label3=satisfaction['sad']['label'],
            value3=satisfaction['sad']['value'],
            class3=satisfaction['sad']['class']
        ) 