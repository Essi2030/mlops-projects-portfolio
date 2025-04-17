
# 📊 Project Report – SageMaker Autopilot: Customer Churn Prediction

## 🔍 Goal
Train and deploy a binary classification model to predict whether a customer will churn using SageMaker Autopilot.

## ✅ Summary
- Dataset uploaded to S3 bucket
- Autopilot ran 250+ candidates using various algorithms and preprocessing methods
- Best candidate deployed to real-time endpoint
- Endpoint tested with real data, achieving 87% accuracy
- Logs monitored with CloudWatch

## 🔍 Evaluation Metrics
- Accuracy: 87%
- F1 Score: 0.84
- AUC: 0.91

## 🔧 Tools Used
- SageMaker Autopilot
- S3
- CloudWatch
- boto3 / Python

## 📝 Notes
Further work can include endpoint monitoring via Model Monitor, advanced data balancing, or model explainability using SageMaker Clarify.
