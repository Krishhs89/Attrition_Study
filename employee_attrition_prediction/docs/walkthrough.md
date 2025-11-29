# Walkthrough - Employee Attrition Prediction

I have updated the solution to match your specific **ML Process** and **Variable List** from the images you provided.

## 1. Workflow Alignment
The code now follows the workflow shown in your "ML Process" slide:

1.  **Data Collection**: Simulated by `generate_data.py`, creating the exact **41 variables** you listed (e.g., `EMPLOYEE_AGE_AT_HIRE`, `MANAGER_RISK_TOLERANCE`).
2.  **Data Pre-Processing**: `train_model.py` now includes a **One-Hot Encoding** step to handle the categorical variables (like `EMPLOYEE_GENDER_CODE`, `DEV_DEVELOPMENT`) shown in your data dictionary.
3.  **Modelling**: Uses **Logistic Regression** as specified in your "Diagnostic Model" slide.
4.  **Important Features**: Generates a feature importance plot to emulate the "SHAP Analysis" mentioned in your slides.

## 2. Updated Dataset
The synthetic dataset now contains **1,000 samples** with the **41 specific variables** from your "Total Variables Considered" image.
- **File**: [synthetic_attrition_data.csv](file:///Users/krishnakumar/.gemini/antigravity/scratch/logistic_regression/synthetic_attrition_data.csv)

## 3. Results & Presentation Assets
I generated updated visualization assets based on this new dataset.

### Feature Importance
Shows which of the 41 variables (and their categories) most strongly influence attrition.
![Feature Importance Plot](/Users/krishnakumar/.gemini/antigravity/brain/3f0d21c6-837e-43e7-a64a-6ef14d47b85a/feature_importance.svg)

### Confusion Matrix
Visualizes the model's prediction accuracy.
![Confusion Matrix](/Users/krishnakumar/.gemini/antigravity/brain/3f0d21c6-837e-43e7-a64a-6ef14d47b85a/confusion_matrix.svg)

## 4. Your Work & Photos
You can add your own photos (e.g., screenshots of your process, whiteboard sketches) here by placing the image files in the folder and using the following syntax:
`![Description of photo](/path/to/your/photo.png)`

## How to Run
1. **Generate Data**:
   ```bash
   python generate_data.py
   ```
   *This script now generates the 41 specific variables from your images.*

2. **Train Model**:
   ```bash
   python train_model.py
   ```
   *This script now handles categorical variables automatically.*
