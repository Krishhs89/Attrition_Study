#!/bin/bash

# Streamlit Dashboard Launcher
# Employee Attrition Prediction System

echo "🚀 Starting Employee Attrition Dashboard..."
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$SCRIPT_DIR/.."

cd "$PROJECT_ROOT/src" || exit 1

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "✅ Python 3 found"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3 first."
    exit 1
fi

echo "✅ pip3 found"

# Check if virtual environment should be used
if [ ! -d "../venv" ]; then
    echo ""
    echo "📦 No virtual environment found. Creating one..."
    python3 -m venv ../venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "🔄 Activating virtual environment..."
source ../venv/bin/activate

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install streamlit pandas plotly

# Check if data exists
if [ ! -f "../data/synthetic_attrition_data.csv" ]; then
    echo ""
    echo "📊 Generating data..."
    python generate_data.py
fi

# Check if model exists
if [ ! -f "../models/model_artifacts.json" ]; then
    echo ""
    echo "🤖 Training model..."
    python train_model.py
fi

# Launch Streamlit
echo ""
echo "✨ Launching dashboard..."
echo ""
echo "📍 The dashboard will open in your browser at http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the server"
echo ""

streamlit run streamlit_app.py
