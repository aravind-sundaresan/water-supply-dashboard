# Water Supply Dashboard

A comprehensive dashboard for monitoring and analyzing water supply performance across different villages in Assam, India. The dashboard provides real-time metrics, performance analytics, and actionable insights for water supply management.

## Features

- **Multi-language Support**: English and Assamese (অসমীয়া) interface
- **Responsive Design**: Optimized for desktop and mobile devices
- **Interactive Charts**: Visual representation of water supply data
- **Performance Metrics**: Key performance indicators for water supply schemes
- **Dynamic Filtering**: Filter by District, Division, Sub-division, and Village
- **Suggestion Engine**: AI-powered recommendations based on performance metrics
- **Mobile Layout**: Dedicated mobile-optimized interface

## Project Structure

```
water-supply-dashboard/
├── data/                                    # Data files
│   ├── IVR PoC - Scheme Report Sample.xlsx  # Main data source
│   └── CSAT Scheme report Sample - English.png
├── src/                                     # Source code
│   ├── app.py                              # Main application
│   ├── constants.py                        # Configuration and translations
│   ├── styles.py                           # CSS styling components
│   ├── data_processor.py                   # Data loading and processing
│   └── chart_builder.py                    # Chart creation and styling
├── requirements.txt                         # Python dependencies
└── README.md                               # This file
```

## Code Architecture

The project uses a modular architecture for better maintainability:

#### 1. `constants.py`
- File paths and configuration
- Language translations (English/Assamese)
- Chart styling parameters
- Suggestion thresholds

#### 2. `styles.py`
- CSS styling functions
- Responsive design rules
- Mobile layout styles
- Component-specific styling

#### 3. `data_processor.py`
- `DataProcessor` class for data operations
- Filter options generation
- Data formatting and validation
- Suggestion generation logic

#### 4. `chart_builder.py`
- `ChartBuilder` class for chart creation
- Water supply comparison charts
- HTML generation for metrics grids
- Chart styling and layout

#### 5. `app.py`
- Main application with modular structure
- Clean separation of concerns
- Better error handling
- Modular UI components

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd water-supply-dashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify data files**:
   Ensure the following files exist in the `data/` directory:
   - `IVR PoC - Scheme Report Sample.xlsx`

### Running the Application

```bash
streamlit run src/app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Usage Guide

### Language Toggle
- Use the toggle switch in the top-right corner to switch between English and Assamese
- All interface elements, including filter labels and metrics, will be translated

### Filtering Data
1. **District**: Select the district from the dropdown
2. **Division**: Choose the division within the selected district
3. **Sub Division**: Select the sub-division
4. **Village**: Choose the specific village/scheme

### Understanding the Dashboard

#### Performance Metrics
- **Gets Water Daily**: Percentage of households receiving daily water supply
- **Gets Water at Same Time**: Consistency in water supply timing
- **Satisfied with Quantity**: Satisfaction with water quantity
- **Satisfied with Quality**: Satisfaction with water quality

#### Overall Satisfaction
- **Happy**: Percentage of satisfied customers
- **Neutral**: Percentage of neutral responses
- **Sad**: Percentage of dissatisfied customers

#### Water Supply Chart
- **Blue Bars**: Expected water supply
- **Yellow Line**: Actual water supplied
- Shows daily comparison for the last 7 days

#### Next Steps
- Dynamic suggestions based on performance metrics
- Actionable recommendations for improvement
- Contact information for relevant authorities

### Mobile Experience
- Automatically detects mobile devices
- Optimized layout for smaller screens
- Touch-friendly interface
- Simplified navigation

## Key Metrics Explained

### Performance Indicators
- **Daily Water Supply**: Measures reliability of water delivery
- **Consistent Timing**: Evaluates schedule adherence
- **Quantity Satisfaction**: Assesses adequacy of water supply
- **Quality Satisfaction**: Monitors water quality standards

### Satisfaction Levels
- **Happy (😊)**: Positive feedback indicating good service
- **Neutral (😐)**: Moderate satisfaction, room for improvement
- **Sad (😔)**: Negative feedback requiring immediate attention

## Data Sources

The dashboard uses Excel files containing:
- **Scheme Performance Data**: Metrics for each water supply scheme
- **Water Supply Data**: Daily expected vs actual water supply
- **Geographic Hierarchy**: District → Division → Sub-division → Village structure

## Technical Features

### Responsive Design
- CSS Grid layouts for metrics
- Flexbox for mobile optimization
- Media queries for different screen sizes
- Progressive enhancement

### Interactive Components
- Plotly charts for data visualization
- Streamlit widgets for user interaction
- Real-time data filtering
- Dynamic content updates

### Performance Optimization
- Efficient data processing
- Lazy loading of components
- Optimized chart rendering
- Minimal re-renders

## Troubleshooting

### Common Issues

1. **Data not loading**:
   - Check if Excel files exist in `data/` directory
   - Verify file permissions
   - Ensure correct sheet names

2. **Charts not displaying**:
   - Check browser console for JavaScript errors
   - Verify Plotly installation
   - Clear browser cache

3. **Language toggle not working**:
   - Refresh the page
   - Check browser compatibility
   - Verify translation files

### Error Messages
- **"No data found"**: Check filter selections
- **"File not found"**: Verify data file paths
- **"Chart error"**: Check data format and values

## Development

### Adding New Features
1. Update `constants.py` for new translations
2. Modify `data_processor.py` for new data processing
3. Add styling in `styles.py` if needed
4. Update `chart_builder.py` for new visualizations
5. Integrate in `app.py`

### Code Style
- Follow PEP 8 guidelines
- Use descriptive variable names
- Add docstrings for functions
- Maintain modular structure

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is developed for the Jal Jeevan Mission Assam initiative.

## Support

For technical support or questions:
- Check the troubleshooting section
- Review the code documentation
- Contact the development team

---

**Last Updated**: July 2025  
**Version**: 1.0  
**Compatibility**: Python 3.8+, Streamlit 1.0+