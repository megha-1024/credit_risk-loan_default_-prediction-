**Credit Risk & Loan Default Prediction**
________________________________________

**Project Overview**

This project focuses on building a Credit Risk & Loan Default Prediction system using machine learning techniques to help financial institutions evaluate borrower risk and make informed lending decisions.
Using borrower financial and loan-related attributes such as income, credit score, loan amount, loan purpose, and employment details, the model predicts whether a loan applicant is likely to default or not.
The project follows a complete end-to-end data science pipeline, including data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and deployment readiness.

________________________________________

**Objectives**

•	Analyze borrower and loan characteristics influencing loan default

•	Identify high-risk borrower profiles

•	Build and compare binary classification models

•	Evaluate model performance using ROC-AUC and accuracy

•	Create a deployment-ready ML solution for banking & fintech applications

________________________________________

**Dataset**

•	**Source:** Credit risk dataset (CSV format)

•	**Target Variable:** loan_status

     •	0 → Non-default
     
     •	1 → Default

     
•	**Features include:**

     •	Applicant Income
     
     •	Credit Score
     
     •	Loan Amount
     
     •	Loan Purpose
     
     •	Employment Length
     
     •	Interest Rate
     
     •	Debt-to-Income Ratio

________________________________________

**Exploratory Data Analysis (EDA)**

  •	Loan default distribution analysis
  
  •	Credit score vs default trends
  
  •	Income and loan amount impact on default risk
  
  •	Correlation analysis to identify key risk factors
  
  •	Visualization using bar charts, histograms, and heatmaps
  
________________________________________

**Machine Learning Models**

The following binary classification models were trained and evaluated:

  •	Logistic Regression
  
  •	Random Forest Classifier
  
  •	Gradient Boosting / XGBoost (optional)
  
**Model Evaluation Metrics**

  •	Accuracy
  
  •	Precision & Recall
  
  •	F1-Score
  
  •	ROC-AUC Score (primary comparison metric)
  
**Best Model Performance:**

  •	Accuracy: ~93%
  
  •	ROC-AUC: ~0.93
  
________________________________________

**Tech Stack**

  •	Python
  
  •	Pandas, NumPy
  
  • Matplotlib, Seaborn
  
  •	Scikit-learn
  
  •	Jupyter Notebook
  
  •	Streamlit (for deployment)

________________________________________

**Project Structure**

credit-risk-loan-default-prediction/

│

├── data/

│   └── credit_risk_dataset.csv

│

├── notebooks/

│   └── credit_risk_analysis.ipynb

│

├── models/

│   └── trained_model.pkl

│

├── app.py     

├── requirements.txt

└── README.md

________________________________________

**Results & Insights**

  •	Credit score and debt-to-income ratio are the strongest predictors of default
  
  •	Lower income groups show higher default probability
  
  •	Ensemble models outperform simple linear models
  
  •	ROC-AUC provides better risk evaluation than accuracy alone
  
________________________________________

Author

**Megha Shinde**

Aspiring Data Scientist | Machine Learning Enthusiast




