
# 🚀 RoadGuard AI v2

### Intelligent Road Damage Detection & Monitoring System

RoadGuard AI v2 is a deep learning-powered road inspection platform that detects road damages, evaluates infrastructure condition, logs inspection history, and provides real-time analytics through a deployed web interface.

---

## 🌐 Live Deployment

🔗 **Live Demo:**
`https://roadguard-ai-1.onrender.com/`

---

## 🧠 Problem Statement

Manual road inspection is slow, inconsistent, and inefficient.
Infrastructure authorities require scalable, automated systems to monitor road conditions and plan maintenance proactively.

---

## 💡 Solution Overview

RoadGuard AI v2 uses a custom-trained YOLOv8 model to:

* Detect potholes and cracks
* Classify damage types (D00, D10, D20, D40)
* Compute road health score using:

  * Damage type weighting
  * Confidence scores
  * Damage area ratio
  * Damage density
* Generate inspection reports
* Log historical inspections
* Provide analytics dashboard

---

## 🔬 Model Details

* Model: YOLOv8s (Fine-tuned)
* Dataset: RDD2022 (Road Damage Dataset)
* Training GPU: NVIDIA RTX 2050 (4GB)
* Image Size: 640x640
* Epochs: 60
* Deployment: CPU inference (Render)

 ---

## ⚙️ Deployment Optimization

Due to cloud memory constraints (Render free tier – 512MB RAM),
the deployed version uses a lightweight YOLOv8n model for stable
CPU-based inference.

The high-accuracy YOLOv8s (60-epoch) model is retained locally
for performance benchmarking and advanced evaluation.

This demonstrates practical model optimization for real-world
deployment environments.

---

## 📊 Performance Metrics

### 🔹 v1 (Baseline – 15 Epochs, YOLOv8n)
```
mAP50: 0.542
Precision: 0.592
Recall: 0.513
```

### 🔹 v2 (Upgraded – 60 Epochs, YOLOv8s)
```
mAP50: 0.656
mAP50-95: 0.370
Precision: 0.661
Recall: 0.617
```
### 🚀 Improvement Summary

* 📈 +11.4% increase in mAP50
* 📈 Better pothole detection (D40 mAP50: 0.778)
* 📈 Improved recall → fewer missed damages
* ⚡ Faster inference (~0.3s per image)

### 🔍 Key Observations

* Strong performance on pothole detection (D40).
* Moderate improvement in thin crack detection.
* Model optimized for real-world drone-based road imagery.
* Balanced precision-recall tradeoff for infrastructure inspection.

---

## ⚙️ Features

### 🔍 Detection Engine

* Adjustable confidence threshold
* Real-time inference time display
* Damage bounding box visualization

### 🧮 Intelligent Severity Engine

* Type-aware scoring
* Confidence-weighted damage
* Damage area density calculation
* Dynamic condition classification

### 📝 Reporting System

* Automated inspection report generation
* Downloadable report (.txt)

### 📈 Monitoring Dashboard

* Historical inspection logging (CSV)
* Total inspections count
* Average road health score
* Condition distribution chart

---

## 🏗 System Architecture

```
Image Input
   ↓
YOLOv8 Detection
   ↓
Severity Engine
   ↓
Report Generator
   ↓
Logging System (CSV)
   ↓
Analytics Dashboard
   ↓
Cloud Deployment (Render)
```

---

## 📂 Project Structure

```
roadguard-ai/
│
├── app.py
├── severity_score.py
├── report_generator.py
├── logger.py
├── inspection_logs.csv
├── weights/
│   └── best.pt
├── assets/
└── requirements.txt
```

---

## 🚀 How To Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Future Scope

* GPS-based damage tagging
* Drone-based real-time monitoring
* PDF report generation
* Maintenance cost estimation
* Predictive road degradation modeling
* REST API integration

---

## 👨‍💻 Developed By

Aaryan Pandey | Microsoft Elevate Intern | Computer Science Engineering Student | Rajiv Gandhi Proudyogiki Vishwavidyalaya, Bhopal

----




