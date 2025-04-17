
# 🔍 Project 01 – AutoML with SageMaker

This project demonstrates a full ML pipeline using **Amazon SageMaker Autopilot** for predicting customer churn. It includes dataset upload to S3, Autopilot configuration and run, deployment of the best model, and testing the endpoint with sample inputs.

## 🧠 Objective
Use SageMaker Autopilot to train a binary classifier to predict customer churn from a dataset, then deploy and test it in production.

## 📦 Dataset
A simplified telecom churn dataset with features such as service usage, account history, and customer demographics.

## 🚀 Pipeline Steps
1. Upload dataset to Amazon S3 ✅
2. Run SageMaker Autopilot experiment ✅
3. Retrieve best candidate model ✅
4. Deploy model to real-time endpoint ✅
5. Run predictions with sample inputs ✅
6. Monitor and log results (CloudWatch/optional)

## 🔧 Technologies
- AWS SageMaker (Autopilot, Deployments)
- S3
- Python (boto3, sagemaker SDK)
- Jupyter / Google Colab

## 📁 Files
- `01-upload-data.ipynb`: Upload dataset to S3
- `02-run-autopilot.ipynb`: Start Autopilot job and track progress
- `03-deploy-and-test.ipynb`: Deploy and query the model endpoint
- `report.md`: Results and analysis

## ✅ Results
- Endpoint deployed successfully
- Predictions returned for real sample data
- Job monitored via SageMaker console

## 📬 Author
Dr. Ehsan Zafari – Senior ML/MLOps Engineer | AWS Certified
