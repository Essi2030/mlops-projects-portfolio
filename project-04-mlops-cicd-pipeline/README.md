
# 🔁 Project 04 – MLOps CI/CD Pipeline with FastAPI, Docker, and GitHub Actions

This project demonstrates a full CI/CD pipeline for machine learning deployment.  
From training a model to serving it via API, containerizing the app, and automating deployment using GitHub Actions.

## 🎯 Objective
Build a production-ready pipeline for ML deployment with:
- Trained scikit-learn model
- FastAPI inference service
- Docker container for portability
- GitHub Actions workflow for CI/CD

## 🛠 Features
✅ Train and save a classification model  
✅ Serve the model via REST API (FastAPI)  
✅ Containerize with Docker  
✅ GitHub Actions workflow: test + build + deploy  
✅ Optional: push to AWS EC2 or DockerHub

## 🔧 Tech Stack
- Python · scikit-learn · FastAPI · Docker · GitHub Actions · pytest

## 📦 Folder Structure
```
project-04-mlops-cicd-pipeline/
├── 01-train-model.ipynb           # Train and export model (joblib/pkl)
├── api/
│   └── main.py                    # FastAPI app loading model
├── Dockerfile                     # Image build for API service
├── .github/workflows/deploy.yml  # CI/CD automation via GitHub Actions
├── requirements.txt
├── report.md                      # Results, screenshots, logs
└── README.md
```

## 🚀 Example API call
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

Response:
```json
{"prediction": "setosa"}
```

## 📬 Author
Dr. Ehsan Zafari  
Senior ML & MLOps Engineer | CI/CD & Cloud AI Expert  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/dr-ehsan-zafari-ai-ml)

# Triggering CI/CD manually
