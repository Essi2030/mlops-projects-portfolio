
# 👁️ Project 05 – Vision-Based Defect Detection with YOLOv8

This project demonstrates a real-time computer vision pipeline using YOLOv8 for detecting surface defects in industrial images. The final model is served via FastAPI for API-based prediction and can be integrated into cloud or edge systems.

---

## 🎯 Objective
- Detect visual defects in images using object detection
- Train a YOLOv8 model on a labeled dataset (bounding boxes)
- Build an inference API using FastAPI for real-time use
- Optionally containerize with Docker

---

## 🧠 Model
- Architecture: YOLOv8 (from Ultralytics)
- Task: Object Detection
- Dataset: Custom images (surface defects or public datasets)
- Output: bounding boxes + class labels

---

## 🧪 Example Output
<img src="https://user-images.githubusercontent.com/placeholder/defect-example.png" width="500"/>

---

## 🛠️ Tools & Libraries
- `ultralytics` (YOLOv8)
- `FastAPI` · `OpenCV` · `Torch`
- `Docker` (for deployment)

---

## 📦 Folder Structure
```
project-05-vision-defect-detection/
├── 01-train-yolo.ipynb         # Training YOLOv8 model
├── 02-api-inference.ipynb      # Building FastAPI inference
├── api/                        # Inference code (main.py)
├── data/                       # Images + labels
├── Dockerfile
├── requirements.txt
├── report.md
└── README.md
```

---

## 📬 Author
Dr. Ehsan Zafari  
Senior ML/MLOps Engineer | Computer Vision Specialist  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/dr-ehsan-zafari-ai-ml)

