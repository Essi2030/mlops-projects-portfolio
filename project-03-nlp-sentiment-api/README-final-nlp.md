
# 🧠 Project 03 – Real-Time NLP Sentiment Analyzer + API

A real-time sentiment analysis API powered by DistilBERT using HuggingFace Transformers and FastAPI. This project demonstrates how to build, serve, and test a modern NLP model for production.

## 🎯 Objective
- Classify user-submitted text as **positive** or **negative**
- Provide real-time inference via a REST API
- MLOps-friendly design with Docker & cloud deploy potential

## 🛠 Features
- ✅ Pretrained BERT (DistilBERT) fine-tuned on IMDb reviews
- ✅ Tokenization and batching with HuggingFace
- ✅ REST API using FastAPI
- ✅ JSON input/output with confidence scores
- ✅ Backed by PyTorch, ready for cloud deployment

## 📦 Folder Structure
```
project-03-nlp-sentiment-api/
├── 01-train-model.ipynb         # Training BERT model on IMDB
├── 02-build-api.ipynb           # FastAPI REST service
├── model/                       # Saved model and tokenizer
├── api/                         # Optional production API code
├── report.md                    # Performance summary
└── README.md
```

## 🔧 Tech Stack
`Transformers · FastAPI · PyTorch · Scikit-learn · Pandas · Docker`

---

## 💬 Example API Call

### 🔁 Request:
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" \
     -d '{"text": "This product is amazing!"}'
```

### ✅ Response:
```json
{
  "label": "positive",
  "confidence": 0.985
}
```

---

## 📊 Model Accuracy
- Accuracy on test set: **~92%**
- Dataset: `IMDb movie reviews`
- Class Labels: `"positive"` / `"negative"`

---

## 📬 Author
Dr. Ehsan Zafari  
Senior Machine Learning & MLOps Engineer  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/dr-ehsan-zafari-ai-ml)

## 🔗 Project Repository
👉 [View on GitHub](https://github.com/Essi2030/mlops-projects-portfolio/tree/main/project-03-nlp-sentiment-api)
