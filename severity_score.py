def calculate_severity(detections, model_names):
    total_weight = 0

    # Weight by damage type severity
    severity_weights = {
        "D00": 5,   # minor crack
        "D10": 10,  # moderate crack
        "D20": 20,  # severe crack
        "D40": 30   # pothole / extreme
    }

    for box in detections:
        class_id = int(box.cls)
        class_name = model_names[class_id]
        confidence = float(box.conf)

        weight = severity_weights.get(class_name, 5)

        total_weight += weight * confidence

    # Convert weight to score
    score = max(0, 100 - int(total_weight))

    if score >= 75:
        condition = "Good"
    elif score >= 50:
        condition = "Moderate"
    elif score >= 25:
        condition = "Poor"
    else:
        condition = "Critical"

    return score, condition


