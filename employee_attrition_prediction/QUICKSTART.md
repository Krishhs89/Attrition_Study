# Quick Start Guide - Streamlit Dashboard

## 🚀 Launch the Dashboard (Easiest Method)

### Option 1: One-Click Launch (Recommended)
```bash
cd /Users/krishnakumar/Documents/Professional/Carriers/Ally/Work/Attrition
./employee_attrition_prediction/scripts/launch_dashboard.sh
```

This script will automatically:
- ✅ Check Python 3 installation
- ✅ Create a virtual environment
- ✅ Install all dependencies (Streamlit, Pandas, Plotly)
- ✅ Generate data if missing
- ✅ Train model if missing
- ✅ Launch the dashboard

---

## 🔧 Manual Setup (If You Prefer)

### Step 1: Install Dependencies
```bash
cd /Users/krishnakumar/Documents/Professional/Carriers/Ally/Work/Attrition/employee_attrition_prediction

# Option A: Using pip
pip3 install streamlit pandas plotly

# Option B: Using the requirements file
pip3 install -r requirements.txt
```

### Step 2: Generate Data & Train Model
```bash
cd src
python3 generate_data.py
python3 train_model.py
```

### Step 3: Launch Dashboard
```bash
streamlit run streamlit_app.py
```

---

## 📊 What You'll See

Once the dashboard launches, your browser will automatically open to `http://localhost:8501` showing:

### 🏠 Overview Tab
- Total Employees: 1,000
- Attrition Rate: ~16%
- Feature count (41 → 167 after encoding)
- Quick statistics

### 🔍 EDA Tab
- Interactive dataset preview (scrollable table)
- Select any variable to see its distribution
- Attrition comparison charts
- Correlation heatmap

### ⚙️ Feature Engineering Tab
- Before/After encoding examples
- Feature expansion metrics
- Top 15 most important features (interactive bar chart)

### 🤖 Model Building Tab
- Training configuration
- Coefficient distribution
- Model parameter summary

### ✅ Validation Tab
- Performance metrics (Accuracy, Precision, Recall, F1)
- Interactive confusion matrix
- Improvement recommendations

### 🚀 CI/CD Status Tab
- Pipeline stage tracking
- Build history
- Deployment status

---

## 🎮 Interactive Features

Try these interactions once the app is running:

1. **EDA Tab**: Select different variables from the dropdown to explore distributions
2. **Hover over charts** to see detailed values
3. **Click and drag** on plots to zoom
4. **Double-click** to reset zoom
5. **Use sidebar** for additional filters (if you extend the app)

---

## 🛑 Stopping the Dashboard

Press `Ctrl + C` in the terminal to stop the server.

---

## 🔧 Troubleshooting

### Port Already in Use
```bash
streamlit run streamlit_app.py --server.port 8502
```

### Module Not Found
```bash
pip3 install --upgrade streamlit pandas plotly
```

### Data/Model Not Found
```bash
cd src
python3 generate_data.py
python3 train_model.py
```

### Browser Doesn't Auto-Open
Manually navigate to: `http://localhost:8501`

---

## 🎨 Customization

### Change Theme
Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

### Add Authentication
Install `streamlit-authenticator`:
```bash
pip3 install streamlit-authenticator
```

---

## 📸 Screenshots

After launching, you can take screenshots by:
1. Viewing each tab
2. Using your browser's screenshot tool
3. Or pressing `Ctrl+Shift+S` (on most browsers)

---

## 🎯 Next Steps

1. ✅ Run the dashboard
2. 📸 Take screenshots for your presentation
3. 🔄 Replace synthetic data with real HR data
4. 🚀 Deploy to Streamlit Cloud (free) for sharing

---

## 💡 Tips

- The app automatically reloads when you edit `streamlit_app.py`
- Use `st.cache_data` decorators to speed up data loading
- All charts are generated with Plotly for maximum interactivity
- Data is loaded from `../data/synthetic_attrition_data.csv`
- Model is loaded from `../models/model_artifacts.json`

---

**Have fun exploring! 🎉**
