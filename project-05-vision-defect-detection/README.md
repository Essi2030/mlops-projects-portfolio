
# 👁️ Project 05 – Vision-Based Defect Detection with YOLOv8

This project demonstrates an end-to-end object detection pipeline using YOLOv8 to identify visual defects in images. It includes training on a custom dataset, exporting the model, and serving it through a FastAPI REST API.

---

## 🎯 Objective
Build an AI system that detects surface defects using deep learning and serves predictions via a REST API.

---

## 🧠 Model
- Architecture: YOLOv8n (Ultralytics)
- Dataset: Custom defect dataset (bounding boxes)
- Export format: ONNX + PyTorch
- Trained for 30 epochs @ 640x640 resolution

---

## 🌐 FastAPI Inference
- Endpoint: `/predict`
- Input: uploaded image file (JPG/PNG)
- Output: list of detected defects with class, confidence, and bounding box

### 🧪 Example API Call:
```bash
curl -X POST http://localhost:8000/predict -F "file=@defect.jpg"
```

### ✅ Example Response:
```json
{
  "detections": [
    {
      "class": "crack",
      "confidence": 0.978,
      "bbox": [55.2, 34.8, 200.1, 120.7]
    }
  ]
}
```

---

## 🧰 Tech Stack
- `ultralytics`, `PyTorch`, `FastAPI`, `OpenCV`
- Optionally Dockerized for deployment

---

## 📦 Folder Structure
```
project-05-vision-defect-detection/
├── 01-train-yolo.ipynb         # YOLOv8 training notebook
├── 02-api-inference.ipynb      # API building notebook
├── api/                        # FastAPI code
├── data/                       # Dataset & labels
├── Dockerfile                  # (optional)
├── requirements.txt            # Python packages
├── report.md                   # Final project report
└── README.md
```

---

## 👨‍💻 Author
Dr. Ehsan Zafari  
Senior ML/MLOps Engineer | Vision AI Specialist  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/dr-ehsan-zafari-ai-ml)

🔗 [View Project on GitHub](https://github.com/Essi2030/mlops-projects-portfolio/tree/main/project-05-vision-defect-detection)
