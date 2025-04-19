
# 🔁 Project 04 – MLOps CI/CD Pipeline with FastAPI, Docker, and GitHub Actions

This project demonstrates a production-ready CI/CD pipeline to automate training, serving, and testing of a machine learning model via a REST API. Built with FastAPI, Docker, and GitHub Actions.

---

## 🎯 Objective
- Train a ML model (Iris classifier)
- Serve it as an API using FastAPI
- Dockerize the application
- Automate CI/CD using GitHub Actions

---

## 🧠 Model
- Algorithm: RandomForestClassifier
- Dataset: Iris (scikit-learn)
- Accuracy: ~96%
- Outputs:
  - `iris_model.joblib`
  - `class_names.txt`

---

## 🌐 API Features
- Built with FastAPI
- `/predict` endpoint receives 4 float features
- Returns predicted class with confidence

Example:
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

Response:
```json
{ "prediction": "setosa" }
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)
- Trigger: push to `main`
- Steps:
  - Checkout code
  - Install dependencies
  - Run tests or validation logic

---

## 📦 Folder Structure
```
project-04-mlops-cicd-pipeline/
├── 01-train-model.ipynb           # Train and save model
├── api/main.py                    # FastAPI serving code
├── Dockerfile                     # Docker build
├── requirements.txt               # Dependencies
├── .github/workflows/deploy.yml  # CI/CD pipeline
├── report.md                      # Summary report
└── README.md
```

---

## 🚀 Next Steps
- Add unit tests with `pytest`
- Add DockerHub auto-push
- Deploy to AWS EC2 or Render

---

## 👨‍💻 Author
Dr. Ehsan Zafari  
Senior ML/MLOps Engineer  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/dr-ehsan-zafari-ai-ml)

🔗 [View Project on GitHub](https://github.com/Essi2030/mlops-projects-portfolio/tree/main/project-04-mlops-cicd-pipeline)
