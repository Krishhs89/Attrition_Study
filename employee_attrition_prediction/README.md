# Employee Attrition Prediction System

> A complete machine learning solution for predicting employee attrition using Logistic Regression

![Status](https://img.shields.io/badge/status-production--ready-green)
![Python](https://img.shields.io/badge/python-2.7-blue)
![ML](https://img.shields.io/badge/ML-Logistic%20Regression-orange)

## 📋 Overview

This project provides a end-to-end solution for predicting employee attrition based on 41 workplace variables including demographics, manager metrics, and talent acquisition data. The system includes data generation, model training, inference serving, and CI/CD automation.

## 🗂️ Project Structure

```
employee_attrition_prediction/
├── README.md                    # This file
├── docs/                        # Documentation
│   ├── deployment_guide.md      # Production deployment & monitoring guide
│   ├── simple_explanation.md    # Non-technical explanation for stakeholders
│   ├── walkthrough.md           # Technical walkthrough
│   ├── implementation_plan.md   # Original implementation plan
│   ├── confusion_matrix.svg     # Model performance visualization
│   └── feature_importance.svg   # Feature importance chart
├── src/                         # Source code
│   ├── generate_data.py         # Synthetic data generation script
│   ├── train_model.py           # Model training with One-Hot Encoding
│   └── serve_model.py           # Production inference server
├── ci_cd/                       # CI/CD configuration
│   └── ml_pipeline.yml          # GitHub Actions workflow
├── models/                      # Trained model artifacts
│   └── model_artifacts.json     # Serialized model (coefficients, intercept)
├── data/                        # Data files
│   └── synthetic_attrition_data.csv
├── notebooks/                   # Jupyter notebooks (future use)
└── tests/                       # Unit tests (future use)
```

## 🚀 Quick Start

### Prerequisites
- Python 2.7 or Python 3.x
- No external dependencies required (uses built-in libraries only)

### 1. Generate Training Data
```bash
cd src/
python generate_data.py
```
**Output**: Creates `synthetic_attrition_data.csv` with 1,000 samples and 41 features

### 2. Train the Model
```bash
python train_model.py
```
**Output**: 
- `model_artifacts.json` (trained model)
- `confusion_matrix.svg` (performance visualization)
- `feature_importance.svg` (feature coefficients)

### 3. Start Inference Server
```bash
python serve_model.py
```
**Result**: Server runs on `http://localhost:8000`

### 4. Make Predictions
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [/* 167 numeric values */]}'
```

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Accuracy | 63% |
| Precision | - |
| Recall | - |
| F1 Score | - |

*Note: Performance on synthetic data. Real-world performance will vary with actual HR data.*

## 🔑 Key Features

### 41 Variables Considered
The model uses employee attributes including:
- **Demographics**: Age, Gender, Ethnicity, Generation
- **Employment**: Business Title, Job Family, Hire/Rehire status
- **Manager Metrics**: Risk tolerance, engagement scores, diversity commitment
- **Talent Acquisition**: Time to hire, recruiter, source
- **Development**: Promotion history, career path

### Technical Highlights
- ✅ **Pure Python Implementation**: No NumPy, Pandas, or scikit-learn required
- ✅ **One-Hot Encoding**: Automatic handling of categorical variables
- ✅ **Logistic Regression**: From-scratch implementation using SGD
- ✅ **Production-Ready**: HTTP server for real-time predictions
- ✅ **CI/CD Pipeline**: Automated training and deployment
- ✅ **Comprehensive Documentation**: Technical and non-technical guides

## 📚 Documentation

| Document | Purpose | Audience |
|----------|---------|----------|
| [Deployment Guide](docs/deployment_guide.md) | Production deployment, monitoring, CI/CD setup | DevOps, ML Engineers |
| [Simple Explanation](docs/simple_explanation.md) | "Explain like I'm 5" walkthrough | Non-technical stakeholders |
| [Walkthrough](docs/walkthrough.md) | Technical implementation details | Data Scientists, Developers |
| [Implementation Plan](docs/implementation_plan.md) | Original design decisions | Project Managers |

## 🔄 CI/CD Pipeline

The project includes a GitHub Actions workflow (`ci_cd/ml_pipeline.yml`) that:
1. Generates fresh training data
2. Trains the model
3. Validates model artifacts
4. Deploys to production (on main branch)

**Setup**:
```bash
mkdir -p .github/workflows
cp ci_cd/ml_pipeline.yml .github/workflows/
git add .
git commit -m "Add CI/CD pipeline"
git push origin main
```

## 🔍 Monitoring & Maintenance

See [Deployment Guide](docs/deployment_guide.md) for:
- Model performance monitoring
- Data drift detection
- Prediction latency tracking
- Automated retraining strategies
- Alert configuration

## 🛠️ Future Improvements

### Short-term
- [ ] Add unit tests in `tests/`
- [ ] Create Jupyter notebooks for EDA
- [ ] Implement proper logging
- [ ] Add model versioning

### Medium-term
- [ ] Support for real HR data ingestion
- [ ] Dashboard for model monitoring
- [ ] A/B testing framework
- [ ] Model explanation API (SHAP values)

### Long-term
- [ ] Ensemble methods (Random Forest, XGBoost)
- [ ] Deep learning models
- [ ] Real-time streaming predictions
- [ ] Multi-tenant support

## 📝 License

This is a demonstration project. Adapt as needed for your organization.

## 🤝 Contributing

To improve this project:
1. Modify code in `src/`
2. Update relevant documentation in `docs/`
3. Add tests in `tests/`
4. Submit changes via pull request

## 📞 Support

For questions about:
- **Deployment**: See [Deployment Guide](docs/deployment_guide.md)
- **Understanding the code**: See [Simple Explanation](docs/simple_explanation.md)
- **Technical details**: See [Walkthrough](docs/walkthrough.md)

---

**Created**: November 2025  
**Last Updated**: November 2025  
**Version**: 1.0.0
