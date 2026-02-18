import streamlit as st
from logger import log_inspection
from ultralytics import YOLO
from severity_score import calculate_severity
from report_generator import generate_report
import tempfile
import time
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="RoadGuard AI v2", page_icon="🚀", layout="centered")

st.title("🚀 RoadGuard AI v2")
st.markdown("### Intelligent Road Condition Monitoring System")

st.divider()

# Confidence Slider
confidence = st.slider("Detection Confidence Threshold", 0.1, 1.0, 0.5)

uploaded_file = st.file_uploader("Upload Road Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    st.subheader("📷 Uploaded Image")
    st.image(temp_path)

    model = YOLO("weights/best.pt")

    st.subheader("🔍 Running Detection...")

    start_time = time.time()
    results = model(temp_path, conf=confidence)
    end_time = time.time()

    # DEBUG LINE
    st.write("Raw Boxes:", results[0].boxes)


    annotated_image = results[0].plot()
    boxes = results[0].boxes
    damage_count = len(boxes)

    score, condition = calculate_severity(damage_count)
    log_inspection(damage_count, score, condition, end_time - start_time)
    report = generate_report(score, condition, damage_count)
    
    st.subheader("📊 Detection Result")
    st.image(annotated_image)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Damages Detected", damage_count)

    with col2:
        st.metric("Road Health Score", f"{score}/100")

    st.metric("Inference Time (seconds)", round(end_time - start_time, 3))

    st.subheader("📝 Inspection Report")
    st.success(report)

    # Download Button
    st.download_button(
        label="Download Inspection Report",
        data=report,
        file_name="road_inspection_report.txt",
        mime="text/plain"
    )

    # ------------------ ANALYTICS DASHBOARD ------------------

    st.divider()
    st.subheader("📈 Damage Distribution Analysis")

    if damage_count > 0:
        class_ids = boxes.cls.cpu().numpy()
        class_counts = {}

        for cls_id in class_ids:
            class_name = model.names[int(cls_id)]
            if class_name in class_counts:
                class_counts[class_name] += 1
            else:
                class_counts[class_name] = 1

        labels = list(class_counts.keys())
        values = list(class_counts.values())

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_xlabel("Damage Type")
        ax.set_ylabel("Count")
        ax.set_title("Damage Type Distribution")

        st.pyplot(fig)

    else:
        st.info("No damages detected for analysis.")

st.divider()
st.caption("Developed by Aaryan | YOLOv8 | Deployed on Render")


