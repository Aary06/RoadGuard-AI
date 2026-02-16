import streamlit as st
from ultralytics import YOLO
from severity_score import calculate_severity
from report_generator import generate_report
import tempfile

st.set_page_config(page_title="RoadGuard AI", page_icon="🚀", layout="centered")

st.title("🚀 RoadGuard AI")
st.markdown("### AI-Powered Road Damage Detection & Severity Analysis")

st.divider()

uploaded_file = st.file_uploader("Upload Road Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    st.subheader("📷 Uploaded Image")
    st.image(temp_path, use_container_width=True)

    st.subheader("🔍 Running Detection...")
    
    model = YOLO("weights/best.pt")
    results = model(temp_path)

    annotated_image = results[0].plot()
    damage_count = len(results[0].boxes)

    score, condition = calculate_severity(damage_count)
    report = generate_report(score, condition, damage_count)

    st.subheader("📊 Detection Result")
    st.image(annotated_image, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Damages Detected", damage_count)

    with col2:
        st.metric("Road Health Score", f"{score}/100")

    st.subheader("📝 Inspection Report")
    st.success(report)

st.divider()
st.caption("Developed by Aaryan | YOLOv8 | RDD2022 Dataset")
