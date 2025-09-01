# Diabetes Prediction using Machine Learning  

This project focuses on predicting whether a patient is diabetic or not using the **Pima Indians Diabetes Dataset** from the UCI Machine Learning Repository. Alongside building predictive models, the project also compares multiple algorithms to understand which performs best for this classification task.  

---

## 📌 Problem Statement  
Diabetes is one of the most common health challenges globally, and early prediction can help in taking preventive measures. The goal of this project is:  
- To predict whether a patient is diabetic or not based on diagnostic measurements.  
- To compare the performance of different machine learning models.  

---

## 📂 Dataset  
- **Source:** [UCI Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)  
- **Features:** 21 diagnostic measurements (e.g., glucose, BMI, age, education level, etc.)  
- **Target:** Binary classification (Diabetic / Not Diabetic)  
- **Size:** 500,000+ rows, 21 features, 1 Label  

---

## 🤖 Models Used  
The following models were trained and evaluated:  
- Logistic Regression  
- K-Nearest Neighbors (KNN)  
- Random Forest Classifier  
- XGBoost Classifier  

---

## 📊 Results  

### Training Performance

| Model                 |  Accuracy  | Recall  | Precision | ROC-AUC |  
|-----------------------|------------|---------|-----------|---------|  
| Logistic Regression   | 0.73       | 0.75    | 0.72      | 0.81    |  
| KNN Classifier        | 0.89       | 0.88    | 0.82      | 0.92    |  
| Random Forest         | 0.95       | 0.96    | 0.95      | 0.99    |  
| XGBoost Classifier    | 0.80       | 0.82    | 0.74      | 0.85    |  

### Testing Performance  

| Model                  | Accuracy | Recall | Precision | ROC Score |
|------------------------|----------|--------|-----------|-----------|
| Logistic Regression    | 0.72     | 0.75   | 0.38      | 0.81      |
| K-Nearest Neighbors    | 0.75     | 0.83   | 0.43      | 0.84      |
| Random Forest          | 0.82     | 0.92   | 0.52      | 0.94      |
| XGBoost Classifier     | 0.73     | 0.82   | 0.40      | 0.85      |

➡️ *For detailed analysis and discussions, please refer to the full project/research report included in this repository.*

---

## ⚡ Limitations  
These results were achieved on a personal laptop, which limited the extent of hyperparameter tuning and large-scale experimentation. With more computational resources and time, the performance of models like XGBoost could likely be improved further.  

---

## 🚀 How to Run  
1. Clone the repository.  
2. Open the notebooks in order:  
   - `1_EDA.ipynb`  
   - `2_Data_Preparation.ipynb`  
   - `3_Model_Training.ipynb`  
   - `4_Testing_and_Evaluation.ipynb`  
3. Run each step to reproduce results.  https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

---

## ✨ Conclusion  
This project demonstrates how different machine learning models can be applied to diabetes prediction. Random Forest performed the best overall, while Logistic Regression provided a simple baseline. Despite computational limitations, the project establishes a strong baseline and offers room for further improvements with deeper tuning and advanced resources.  
