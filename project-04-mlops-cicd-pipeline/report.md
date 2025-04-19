
# 📊 Project Report – MLOps CI/CD Pipeline with FastAPI, Docker, GitHub Actions

## 🎯 Objective
To build an automated, production-ready CI/CD pipeline for a machine learning API using industry best practices. The goal is to simulate how a real-world ML service would be trained, served, and deployed automatically on push events.

---

## 🧠 Model
- Dataset: Iris flower dataset
- Algorithm: RandomForestClassifier (scikit-learn)
- Accuracy: ~96% on test set
- Output: `iris_model.joblib` and `class_names.txt`

---

## 🌐 API
- Framework: FastAPI
- Input: list of 4 float features
- Output: predicted class label (e.g., "setosa")
- Route: `/predict`
- Example:
```json
POST /predict
Body: { "features": [5.1, 3.5, 1.4, 0.2] }
Response: { "prediction": "setosa" }
```

---

## 📦 Infrastructure
- Containerization: Docker
- CI/CD: GitHub Actions
  - Trigger: Push to main branch
  - Steps: Checkout → Install → Test
- Future scope: Deploy image to DockerHub or AWS EC2

---

## 📌 Folder Structure
```
project-04-mlops-cicd-pipeline/
├── 01-train-model.ipynb           # Model training and export
├── api/main.py                    # FastAPI serving code
├── Dockerfile                     # For containerizing the API
├── requirements.txt               # Python dependencies
├── .github/workflows/deploy.yml  # CI/CD automation script
├── report.md                      # Summary of architecture
└── README.md
```

---

## 🧠 Next Steps
- Add DockerHub auto-push
- Add unit tests via pytest
- Deploy live to EC2 or render

---

👨‍💻 Author: Dr. Ehsan Zafari  
Senior ML/MLOps Engineer | CI/CD + Cloud AI Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/dr-ehsan-zafari-ai-ml)
