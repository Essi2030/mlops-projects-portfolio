# 🧠 Project 03 – Real-Time NLP Sentiment Analyzer + API

This project demonstrates a complete NLP pipeline for text sentiment classification using a pretrained BERT model, served via FastAPI, and containerized using Docker for deployment.

## 🎯 Objective
Build an MLOps-ready sentiment analysis service that:
- Classifies input texts (positive/negative/neutral)
- Responds via a real-time REST API
- Can be deployed locally or on the cloud (AWS, GCP, etc.)

## 🛠 Features
✅ Fine-tuned BERT or DistilBERT on sentiment dataset  
✅ Real-time inference with FastAPI  
✅ Fully containerized using Docker  
✅ Ready for production deployment or integration

## 🔧 Tech Stack
- Python · HuggingFace Transformers · FastAPI · Docker · Scikit-learn · Pandas

## 📦 Folder Structure
```
project-03-nlp-sentiment-api/
├── 01-train-model.ipynb         # Load or fine-tune BERT on sentiment data
├── 02-build-api.ipynb           # Run and test FastAPI app
├── model/                       # Saved transformer model
├── api/                         # FastAPI app code
├── Dockerfile                   # For containerized deployment
├── report.md                    # Summary & performance
└── README.md
```

## 💬 Example API Call
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" \
     -d '{"text": "This product is amazing!"}'
```

Response:
```json
{"label": "positive", "confidence": 0.985}
```

## 📬 Author
Dr. Ehsan Zafari  
Senior Machine Learning & MLOps Engineer  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/dr-ehsan-zafari-ai-ml)

