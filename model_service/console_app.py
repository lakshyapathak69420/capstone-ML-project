"""
a simple console app to showcase that model can be served if on app if refined.
"""

import sys
import numpy as np
from model_pipeline import prediction_model, standardScaler

# Mapping dictionaries
education_mapping = {
    1: 0,  # None
    2: 1,  # Elementary
    3: 2,  # HighSchool-Dropout
    4: 3,  # HighSchool
    5: 4,  # College
    6: 5   # Graduate
}
different_categories_of_education = {
    1: "None",
    2: "Elementary",
    3: "HighSchool-Dropout",
    4: "HighSchool",
    5: "College",
    6: "Graduate"
}

 
def income_mapping(income):

    if income < 10000:
        return 1
    elif 10000 <= income < 15000:
        return 2
    elif 15000 <= income < 20000:
        return 3
    elif 20000 <= income < 25000:
        return 4
    elif 25000 <= income < 35000:
        return 5
    elif 35000 <= income < 50000:
        return 6
    elif 50000 <= income < 75000:
        return 7
    elif income >= 75000:
        return 8
    else:
        return None  # fallback for invalid values


def age_mapping(age):
    if 18 <= age <= 24:
        return 1
    elif 25 <= age <= 29:
        return 2
    elif 30 <= age <= 34:
        return 3
    elif 35 <= age <= 39:
        return 4
    elif 40 <= age <= 44:
        return 5
    elif 45 <= age <= 49:
        return 6
    elif 50 <= age <= 54:
        return 7
    elif 55 <= age <= 59:
        return 8
    elif 60 <= age <= 64:
        return 9
    elif 65 <= age <= 69:
        return 10
    elif 70 <= age <= 74:
        return 11
    elif 75 <= age <= 79:
        return 12
    elif age >= 80:
        return 13
    else:
        return None  # for invalid ages


def get_input(prompt, val_type=int, allowed=None):
    while True:
        try:
            value = val_type(input(prompt))
            if allowed and value not in allowed:
                print(f"Invalid input. Allowed values: {allowed}")
                continue
            return value
        except ValueError:
            print(f"Please enter a valid {val_type.__name__}.")

def main():
    print("Please provide the following details:")

    # Binary / 0-1 features
    HighBP = get_input("HighBP (0=No, 1=Yes): ", int, [0,1])
    HighChol = get_input("HighChol (0=No, 1=Yes): ", int, [0,1])
    CholCheck = get_input("Have you checked you chol in last 30 days (0=No, 1=Yes): ", int, [0,1])
    Smoker = get_input("Are you a smoker (0=No, 1=Yes): ", int, [0,1])
    Stroke = get_input("Have you suffered from stroke in last 30  days (0=No, 1=Yes): ", int, [0,1])
    HeartDiseaseorAttack = get_input("Do you have any heart disease (0=No, 1=Yes): ", int, [0,1])
    PhysActivity = get_input("Do you take part in physical activity (0=No, 1=Yes): ", int, [0,1])
    Fruits = get_input("Do you eat fruits regularly  (0=No, 1=Yes): ", int, [0,1])
    Veggies = get_input("Do you eat Veggies regularly (0=No, 1=Yes): ", int, [0,1])
    HvyAlcoholConsump = get_input("Are you a heavy alchohol consumer (0=No, 1=Yes): ", int, [0,1])
    AnyHealthcare = get_input("Do you have any health care  (0=No, 1=Yes): ", int, [0,1])
    NoDocbcCost = get_input("Have you not gone to doctor in last 30 days because of the dr cost (0=No, 1=Yes): ", int, [0,1])
    DiffWalk = get_input("do you have difficulty in walking (0=No, 1=Yes): ", int, [0,1])
    Sex = get_input("Sex (0=Female, 1=Male): ", int, [0,1])

    # Numerical features
    BMI_input = get_input("BMI (numeric): ", float)
    BMI = standardScaler(BMI_input)
    GenHlth = get_input("General Health on a scale of 1 to 5: ", int, [1,2,3,4,5])
    MentHlth = get_input("Poor Mental Health Days in last 30 days (0-30): ", int, range(0,31))
    PhysHlth = get_input("Poor Physical Health Days in last 30 days (0-30): ", int, range(0,31))

    
    print("different_categories_of_education")
    for k in different_categories_of_education:
        print(f"{k} : {different_categories_of_education[k]}")
    # Categorical features mapped
    Education_input = get_input("Education (1-6): ", int, range(1,7))
    Education = education_mapping[Education_input]

    Age_input = get_input("enter your age: ", int)
    Age = age_mapping(Age_input)

    Income_input = get_input("enter your income in usd: ", int)
    Income = income_mapping(Income_input)

    # Prepare feature array
    features = np.array([[
        HighBP, HighChol, CholCheck, BMI, Smoker,
        Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies,
        HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth,
        MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income
    ]])

    # Prediction
    prediction = prediction_model.predict_proba(features)
    probab = prediction[1]
    chances = round(probab, 4)
    chances = chances * 100
    print(f"chance of you getting diabetes is {chances}")

if __name__ == "__main__":
    main()
