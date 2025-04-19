
# 📊 Project Report – Vision-Based Defect Detection with YOLOv8

## 🎯 Objective
To build a real-time object detection system using YOLOv8 that can identify visual defects in industrial or manufacturing settings.

---

## 🧠 Model
- Architecture: YOLOv8n (Ultralytics)
- Dataset: Custom dataset with bounding boxes for defects
- Image Size: 640x640
- Epochs: 30
- Format: Exported in ONNX and PyTorch

---

## 🔍 Inference API
- Framework: FastAPI
- Endpoint: `/predict`
- Input: image file
- Output: list of detections with class, confidence, and bounding box

### 📥 Sample Response:
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

## 🧪 Evaluation
- mAP50: ~0.84
- Precision: ~0.88
- Inference time: ~11ms per image (CPU)

---

## 📦 Stack
- `ultralytics`, `PyTorch`, `FastAPI`, `OpenCV`, `Docker` (optional)
- Optimized for real-time industrial applications

---

## 🚀 Future Improvements
- Deploy to edge device or cloud instance
- Add streamlit interface for demo
- Test on real production image feeds

---

👨‍💻 Author: Dr. Ehsan Zafari  
Senior ML/MLOps Engineer | Vision AI Specialist  
🔗 [LinkedIn](https://www.linkedin.com/in/dr-ehsan-zafari-ai-ml)
