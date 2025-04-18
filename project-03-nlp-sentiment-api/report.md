
# 📊 Project Report – Real-Time NLP Sentiment Analyzer

## 🎯 Objective
Build a real-time sentiment classification API using a pre-trained transformer model (DistilBERT). This service enables users to classify text as positive or negative with high accuracy.

## 🧠 Model Overview
- Model: `distilbert-base-uncased`
- Dataset: IMDb Movie Reviews
- Framework: HuggingFace Transformers
- Accuracy on test subset (1,000 samples): ~92%
- Fine-tuned using `Trainer` on 3,000 training samples

## ⚙️ Deployment
The model was integrated with a RESTful API using FastAPI and returns predictions in real-time.

### 🧪 Example request:
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" \
     -d '{"text": "This is absolutely amazing!"}'
```

### ✅ Response:
```json
{"label": "positive", "confidence": 0.985}
```

## 📦 Stack
- HuggingFace Transformers
- FastAPI
- PyTorch
- Docker-ready (optional)
- Python 3.10+

## 🔁 Future Work
- Add model monitoring and logging
- Containerize with Docker
- Deploy to AWS Lambda or SageMaker Inference
- Support more languages and multi-class sentiment

---

👤 Author: Dr. Ehsan Zafari  
Senior Machine Learning & MLOps Engineer | NLP Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/dr-ehsan-zafari-ai-ml)
