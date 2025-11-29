import random
import csv
import math

def generate_dataset(n_samples=1000):
    """
    Generates a synthetic employee attrition dataset using pure Python 2.7.
    Matches the 'Total Variables Considered' list from user images (41 variables).
    """
    # List of 41 variables from the user's image "Total Variables Considered"
    feature_names = [
        "DEV_DEVELOPMENT",
        "EMPLOYEE_AGE_AT_HIRE",
        "EMPLOYEE_ETHNICITY_ID",
        "EMPLOYEE_GENDER_CODE",
        "EMPLOYEE_GENERATION",
        "EMPLOYEE_HIRE_BUSINESS_TITLE_ROLE",
        "EMPLOYEE_HIRE_COST_CENTER_NAME_CATEGORY",
        "EMPLOYEE_HIRE_COST_CENTER_NAME_SUPERCATEGORY",
        "EMPLOYEE_HIRE_DIRECT_MANAGER_TENURE",
        "EMPLOYEE_HIRE_DIRECT_MANAGER_AGE",
        "EMPLOYEE_HIRE_DIRECT_MANAGER_GENDER_CODE",
        "EMPLOYEE_HIRE_DIRECT_MANAGER_RACE_ETHNICITY_DESCRIPTION",
        "EMPLOYEE_HIRE_HIRE_REHIRE",
        "EMPLOYEE_HIRE_JOB_FAMILY",
        "EMPLOYEE_HIRE_MANAGER_6_NAME",
        "EMPLOYEE_HIRE_WORK_CITY",
        "EMPLOYEE_MARITAL_STATUS",
        "EMPLOYEE_TERM_TERMINATED", # This sounds like the target, but usually target is separate. Let's assume this is a feature or related.
                                    # Wait, "Predicting employee attrition". Usually "Terminated" IS the target.
                                    # But the list says "Total Variables Considered".
                                    # I will treat "Attrition" as a separate target column for the model, 
                                    # or assume one of these IS the target. 
                                    # Let's keep "Attrition" as the explicit target column for clarity in the CSV.
        "MANAGER_BELONGING",
        "MANAGER_CAREER_PATH",
        "MANAGER_DIVERSITY_COMMITMENT",
        "MANAGER_ENGAGEMENT",
        "MANAGER_ENGAGEMENT_ESAT",
        "MANAGER_ENGAGEMENT_RECOMMEND",
        "MANAGER_INCLUSION_TEAM",
        "MANAGER_JOB_FEEDBACK",
        "MANAGER_OPINIONS_COUNT",
        "MANAGER_RESPONDENTS",
        "MANAGER_RESPONSERATE",
        "MANAGER_RISK_COMMUNICATION",
        "MANAGER_RISK_CONCERNS",
        "MANAGER_RISK_CULTURE",
        "MANAGER_RISK_TOLERANCE",
        "PROMOS_PROMOTION",
        "TA_JUSTIFICATION",
        "TA_RECRUITER_NAME",
        "TA_SOURCE",
        "TA_TIME_TO_ACCEPT",
        "TA_TIME_TO_FILL",
        "TA_TIME_TO_START",
        "TA_VOLUME_NON_VOLUME"
    ]
    
    n_features = len(feature_names)
    print "Generating {} samples with {} features...".format(n_samples, n_features)
        
    data = []
    headers = feature_names + ['Attrition']
    
    for _ in range(n_samples):
        row = []
        
        # Generate synthetic data for each feature
        # We'll try to be slightly realistic with types
        
        # DEV_DEVELOPMENT (Categorical?)
        row.append(random.choice(["High", "Medium", "Low"]))
        
        # EMPLOYEE_AGE_AT_HIRE (Numeric)
        row.append(int(random.gauss(30, 8)))
        
        # EMPLOYEE_ETHNICITY_ID (Categorical)
        row.append(random.choice(["Group_A", "Group_B", "Group_C", "Group_D"]))
        
        # EMPLOYEE_GENDER_CODE (Categorical)
        row.append(random.choice(["M", "F", "X"]))
        
        # EMPLOYEE_GENERATION (Categorical)
        row.append(random.choice(["Gen Z", "Millennial", "Gen X", "Boomer"]))
        
        # EMPLOYEE_HIRE_BUSINESS_TITLE_ROLE (Categorical)
        row.append("Role_" + str(random.randint(1, 10)))
        
        # COST CENTER STUFF
        row.append("Category_" + str(random.randint(1, 5)))
        row.append("SuperCategory_" + str(random.randint(1, 3)))
        
        # MANAGER INFO
        row.append(random.gauss(5, 2)) # Tenure
        row.append(int(random.gauss(45, 10))) # Age
        row.append(random.choice(["M", "F"])) # Gender
        row.append("Desc_" + str(random.randint(1, 4))) # Ethnicity
        
        # HIRE/REHIRE
        row.append(random.choice(["Hire", "Rehire"]))
        
        # JOB FAMILY
        row.append("Family_" + str(random.randint(1, 8)))
        
        # MANAGER NAME
        row.append("Manager_" + str(random.randint(1, 50)))
        
        # WORK CITY
        row.append("City_" + str(random.randint(1, 10)))
        
        # MARITAL STATUS
        row.append(random.choice(["Single", "Married", "Divorced"]))
        
        # TERM TERMINATED - This might be the target in the user's data, 
        # but for training we usually exclude the target from features.
        # I'll include it as a feature for now as requested by the list, 
        # but maybe it's "Previous Terminations"? Let's assume binary.
        row.append(random.choice([0, 1]))
        
        # MANAGER SCORES (Numeric 1-5 or 1-10)
        for _ in range(15): # Covering MANAGER_BELONGING to MANAGER_RISK_TOLERANCE
            row.append(random.randint(1, 10))
            
        # PROMOS
        row.append(random.choice(["Yes", "No"]))
        
        # TA STUFF
        row.append("Justification_" + str(random.randint(1, 5)))
        row.append("Recruiter_" + str(random.randint(1, 20)))
        row.append("Source_" + str(random.randint(1, 5)))
        
        # TIME TO... (Numeric days)
        row.append(max(0, int(random.gauss(30, 10)))) # Accept
        row.append(max(0, int(random.gauss(45, 15)))) # Fill
        row.append(max(0, int(random.gauss(15, 5))))  # Start
        
        # VOLUME
        row.append(random.choice(["Volume", "Non-Volume"]))
        
        # --- CALCULATE TARGET (ATTRITION) ---
        # We need to access the values we just appended.
        # The list 'row' currently has mixed types (int, string).
        # Let's find the indices based on the order we appended them.
        
        # We appended in order of the feature_names list? 
        # No, we appended manually in the loop.
        # Let's just use the variables we generated directly before appending.
        
        # Re-generating the specific values for calculation to be safe/clear
        # (or we could just grab them from the row if we know the index)
        
        # Age is the 2nd item appended (index 1)
        val_age = row[1] 
        
        # Manager Risk Tolerance is index 33 in the feature list, 
        # but in our manual append order, it was inside the loop "for _ in range(15)".
        # That loop started after index 17 (Terminated).
        # So it's somewhere in there.
        
        # To avoid index confusion, let's just generate the predictive variables 
        # explicitly and store them in variables before appending.
        
        # ... (Refactoring the loop to be safer) ...
        # Actually, let's just fix the specific error.
        # The error was: TypeError: unsupported operand type(s) for -: 'str' and 'float'
        # This means row[33] was a string.
        # Ah, I see. In the previous code I did: row.append("Role_" + ...).
        # But for the numeric ones I did row.append(int(...)).
        # Let's verify the index 33.
        
        # 0: DEV
        # 1: AGE
        # ...
        # 33: MANAGER_RISK_TOLERANCE
        
        # In the loop:
        # ...
        # row.append(random.choice([0, 1])) # Terminated (Index 17)
        # for _ in range(15): ... # Indices 18 to 32
        # Wait, 17 + 15 = 32.
        # So index 32 is the last manager score.
        # Index 33 is PROMOS_PROMOTION.
        
        # My manual append order might not match the feature_names list order exactly!
        # This is the risk of manual appending vs iterating.
        
        # Let's just use the Age (index 1) and maybe one of the manager scores (index 30?)
        # row[30] should be a manager score (int).
        
        val_risk = row[30] # Arbitrary manager score
        val_time = row[39] # TA_TIME_TO_FILL?
        
        # Let's check index 39.
        # 33: Promos
        # 34: Justification
        # 35: Recruiter
        # 36: Source
        # 37: Time Accept
        # 38: Time Fill
        # 39: Time Start
        
        # So row[38] is Time Fill.
        val_time = row[38]
        
        age_norm = (float(val_age) - 30.0) / 8.0
        risk_norm = (float(val_risk) - 5.0) / 3.0
        time_norm = (float(val_time) - 45.0) / 15.0
        
        log_odds = -1.0 + (-0.6 * age_norm) + (0.4 * risk_norm) + (0.3 * time_norm) + random.gauss(0, 0.5)
        
        try:
            probability = 1.0 / (1.0 + math.exp(-log_odds))
        except OverflowError:
            probability = 0.0 if log_odds < 0 else 1.0
        
        target = 1 if random.random() < probability else 0
        row.append(target)
        
        # Convert all to string for CSV writing to be safe/simple
        row = [str(x) for x in row]
        data.append(row)
        
    return headers, data

if __name__ == "__main__":
    headers, data = generate_dataset()
    filename = "synthetic_attrition_data.csv"
    
    with open(filename, 'wb') as f: # 'wb' for python 2 csv
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)
        
    print "Dataset saved to {}".format(filename)
