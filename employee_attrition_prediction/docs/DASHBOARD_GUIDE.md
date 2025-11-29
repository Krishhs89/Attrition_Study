# Running the Dashboard Applications

This guide shows you how to run both the Streamlit and R Shiny dashboards.

## Prerequisites

### For Streamlit (Python)
```bash
pip install -r requirements.txt
```

### For R Shiny
```R
install.packages(c("shiny", "shinydashboard", "ggplot2", "plotly", "DT", "jsonlite", "dplyr"))
```

---

## Running Streamlit Dashboard

### Option 1: From src/ directory
```bash
cd employee_attrition_prediction/src
streamlit run streamlit_app.py
```

### Option 2: From project root
```bash
streamlit run src/streamlit_app.py
```

The app will automatically open in your browser at `http://localhost:8501`

### Features:
- 📊 **Overview**: Key metrics and quick statistics
- 🔍 **EDA**: Interactive data exploration with distributions and correlations
- ⚙️ **Feature Engineering**: One-Hot Encoding transformation details
- 🤖 **Model Building**: Training configuration and coefficient analysis
- ✅ **Validation**: Performance metrics and confusion matrix
- 🚀 **CI/CD Status**: Pipeline monitoring and deployment tracking

---

## Running R Shiny Dashboard

### Option 1: From R Console
```R
setwd("employee_attrition_prediction/src")
shiny::runApp("shiny_app.R")
```

### Option 2: From RStudio
1. Open `shiny_app.R` in RStudio
2. Click "Run App" button in the top right

The app will launch at `http://localhost:XXXX` (port varies)

### Features:
Same as Streamlit dashboard, but with R Shiny's reactive framework:
- Real-time updates
- Interactive plots with Plotly
- Data tables with DT package
- Beautiful dashboard layout with shinydashboard

---

## Screenshots

### Overview Page
Shows high-level metrics and attrition distributions by generation and gender.

### EDA Page
Interactive exploration with:
- Dataset preview table
- Distribution histograms by attrition status
- Correlation heatmap

### Feature Engineering Page
Demonstrates the One-Hot Encoding transformation:
- Before/After comparison
- Feature expansion metrics (41 → 167 features)
- Top engineered features by importance

### Model Building Page
Details about the model:
- Algorithm configuration (Logistic Regression, SGD)
- Training process steps
- Coefficient distribution histogram

### Validation Page
Model performance evaluation:
- Accuracy, Precision, Recall, F1 Score
- Confusion matrix visualization
- Improvement recommendations

### CI/CD Status Page
Pipeline monitoring:
- Stage-by-stage status
- Build information
- Recent commits
- Deployment status (Staging/Production)

---

## Troubleshooting

### Streamlit Issues

**Port already in use:**
```bash
streamlit run streamlit_app.py --server.port 8502
```

**Module not found:**
```bash
pip install --upgrade -r requirements.txt
```

### R Shiny Issues

**Package not found:**
```R
install.packages("package_name")
```

**Data not loading:**
Make sure you're running from the correct directory and that `../data/synthetic_attrition_data.csv` exists.

---

## Customization

### Changing the Theme

**Streamlit:**
Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#F63366"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

**R Shiny:**
Modify the `skin` parameter in `dashboardPage()`:
```R
dashboardPage(
  skin = "blue"  # Options: blue, black, purple, green, red, yellow
)
```

---

## Performance Tips

1. **Large Datasets**: Use data sampling for EDA plots
2. **Slow Loading**: Consider caching with `@st.cache_data` (Streamlit) or `reactive()` (Shiny)
3. **Memory**: Close unused browser tabs

---

## Next Steps

1. **Connect Real Data**: Replace synthetic data with actual HR data
2. **Add More Visualizations**: ROC curves, precision-recall curves
3. **Export Reports**: Add PDF/Excel export functionality
4. **User Authentication**: Implement login for production use
5. **Real-time Predictions**: Add prediction input form
