# AI-Powered-Financial-Fraud-Detection-System
- An AI-powered financial fraud detection system using K-Means, Isolation Forest, Random Forest, LightGBM, and SHAP Explainability with an interactive Streamlit dashboard.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 📌 Overview

- Financial fraud has become one of the biggest challenges in the banking and fintech industry. Traditional rule-based systems often fail to detect evolving fraud patterns, resulting in financial losses and reduced customer trust.
This project presents an **AI-Powered Financial Fraud Detection System** that combines **supervised learning**, **unsupervised anomaly detection**, and **Explainable AI (XAI)** to accurately identify fraudulent transactions while providing interpretable predictions through an interactive **Streamlit** web application.
The system performs transaction analysis, fraud classification, anomaly detection, customer segmentation, and risk assessment using multiple machine learning models.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 🎯 Objectives
- Detect fraudulent financial transactions using Machine Learning
- Perform anomaly detection to identify suspicious transaction patterns
- Classify transactions as Genuine or Fraudulent
- Generate fraud probability and transaction risk score
- Segment transactions using clustering techniques
- Provide Explainable AI (XAI) using SHAP
- Visualize fraud analytics through an interactive dashboard
- Support both single transaction and batch transaction prediction
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## ✨ Key Features

- 🔍 Fraud Detection using Machine Learning
- 📊 Interactive Streamlit Dashboard
- 🚨 Real-time Fraud Risk Prediction
- 🤖 Ensemble Machine Learning Models
- 📈 Transaction Risk Scoring
- 🔎 Anomaly Detection using Isolation Forest
- 👥 Customer Segmentation using K-Means Clustering
- 💡 Explainable AI using SHAP
- 📂 Batch CSV Prediction
- 📥 Download Prediction Results
- 📉 Interactive Charts and Visualizations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Machine Learning Models

| Model | Purpose |
|--------|----------|
| Random Forest | Fraud Classification |
| LightGBM | High Accuracy Prediction |
| Isolation Forest | Anomaly Detection |
| K-Means | Customer Segmentation |
| SHAP | Model Explainability |

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Technology Stack

1] Programming Language
- Python

2] Machine Learning
- Scikit-Learn
- LightGBM
- SHAP

3] Data Processing
- NumPy
- Pandas

4] Visualization
- Plotly
- Matplotlib

5] Web Framework
- Streamlit
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 🗂️ Project Structure
- fraud_detection_system/
- app.py → Main Streamlit Dashboard
- fraud_pipeline.py → Data preprocessing, model training and prediction pipeline
- generate_dataset.py → Synthetic transaction dataset generation
- requirements.txt → Required Python libraries
- models/
    random_forest.joblib
    lightgbm.joblib
    isolation_forest.joblib
    kmeans.joblib
    scaler.joblib
- data/
    transactions.csv
    creditcard.csv
- README.md
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## ⚙️ How It Works

- Step 1 — User uploads a transaction dataset or enters transaction details manually
- Step 2 — Transaction data is cleaned and preprocessed
- Step 3 — Features are normalized using StandardScaler
- Step 4 — K-Means groups similar transactions into clusters
- Step 5 — Isolation Forest detects anomalous transactions
- Step 6 — Random Forest predicts whether the transaction is fraudulent
- Step 7 — LightGBM calculates fraud probability and improves prediction accuracy
- Step 8 — SHAP explains which features contributed most to the prediction
- Step 9 — Results are displayed on an interactive Streamlit dashboard
- Step 10 — Users can download fraud prediction results as a CSV file
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 🔍 Key Findings / Output
- Fraud Prediction (Fraud / Genuine)
- Fraud Probability Score
- Transaction Risk Score
- Anomaly Detection Result
- Cluster Assignment
- SHAP Feature Importance
- Fraud Distribution Analysis
- Model Performance Metrics
- Downloadable Prediction Report
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Application Modules

1] Dashboard
- Fraud Statistics
- Risk Distribution
- Fraud Trends
- Model Performance
- Cluster Analysis

2] Fraud Prediction
- Predict Individual Transactions
- Fraud Probability
- Risk Score
- Explainable Predictions

3] Batch Prediction
- Upload CSV File
- Detect Fraud
- Export Results

4] Explainable AI
- SHAP Summary Plot
- Feature Importance
- Local Prediction Explanation
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Performance Highlights
- High fraud detection accuracy
- Ensemble-based prediction
- Explainable AI integration
- Fast real-time inference
- Interactive visualization dashboard
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 🔎 Conclusion
- This AI-Powered Financial Fraud Detection System demonstrates how Machine Learning, Anomaly Detection, Clustering, and Explainable AI can be combined to build an intelligent fraud detection solution. The ensemble of Random Forest, LightGBM, Isolation Forest, and K-Means provides accurate fraud prediction while SHAP offers transparent explanations for every prediction. The interactive Streamlit dashboard enables financial analysts to monitor transactions, assess fraud risks, and make informed decisions efficiently.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 🚀 How to Run

- cd fraud_detection_system
- pip install -r requirements.txt
- streamlit run app.py
