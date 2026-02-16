## 🌐 Live Demo

https://roadguard-ai-1.onrender.com

---

# 🚀 RoadGuard AI

RoadGuard AI is a deep learning-based road damage detection system built using YOLOv8 and deployed with Streamlit.

The system detects potholes and cracks from road images, calculates a road health score, and generates automated inspection reports.

---

## 🔍 Problem Statement

Manual road inspection is time-consuming and inefficient. This project automates road damage detection using computer vision.

---

## 💡 Solution

- Custom-trained YOLOv8 model (RDD2022 dataset)
- GPU-accelerated training (RTX 2050)
- Severity scoring algorithm
- Interactive Streamlit dashboard

---

## 🧠 Tech Stack

- Python
- YOLOv8 (Ultralytics)
- PyTorch (CUDA)
- OpenCV
- Streamlit

---

## 📊 Model Performance

- mAP50: 0.542
- Precision: 0.592
- Recall: 0.513

---
## 📷 Demo

### Upload Interface
![Upload](Assets/demo1.png)

### Detection Output
![Detection](Assets/demo2.png)

### Final Inspection Report
![Report](Assets/demo3.png)

---


## 👨‍💻 Developed By

Aaryan Pandey  
Microsoft Elevate AI Intern  
Engineering Student | AI & IoT Enthusiast
📫 Connect with me on LinkedIn:www.linkedin.com/in/aary06

---


## ⚙️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py




