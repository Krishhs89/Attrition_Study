# Implementation Plan - Employee Attrition Prediction

This plan outlines the steps to emulate the study "Predicting employee attrition and explaining its determinants" using a synthetic dataset and Logistic Regression.

## User Review Required

> [!IMPORTANT]
> **Synthetic Data**: Since the original dataset is proprietary (Italian financial corporation), I will generate a **synthetic dataset** with 15,000 samples and 35 features to mimic the study's data structure.

## Proposed Changes

### Data Generation
#### [NEW] [generate_data.py](file:///Users/krishnakumar/.gemini/antigravity/scratch/logistic_regression/generate_data.py)
- Script to generate a synthetic dataset.
- **Samples**: 15,000
- **Features**: 35 (mix of numerical and categorical to simulate employee data like Age, Salary, Department, Tenure, etc.)
- **Target**: 'Attrition' (Binary: 0/1)

### Model Implementation
#### [NEW] [train_model.py](file:///Users/krishnakumar/.gemini/antigravity/scratch/logistic_regression/train_model.py)
- Load the synthetic data.
- Preprocess data (encoding categorical variables, scaling numerical ones).
- Split into Train/Test sets.
- Train a **Logistic Regression** model.
- Calculate metrics: **Accuracy, Precision, Recall, F1-score, AUC**.
- Generate **SHAP** plots to explain feature importance, emulating the study's focus on explainability.

## Verification Plan

### Automated Tests
- Run `python generate_data.py` to ensure data is created correctly.
- Run `python train_model.py` and check for successful execution and output of metrics.

### Manual Verification
- Review the generated SHAP plots to see if they provide intuitive explanations (e.g., lower satisfaction -> higher attrition).
- Check if the model metrics are reasonable for a synthetic dataset.
