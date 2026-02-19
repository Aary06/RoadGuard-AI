import numpy as np

def calculate_severity(boxes, model_names, img_shape):
    if boxes is None or len(boxes) == 0:
        return 100, "Excellent"

    img_area = img_shape[0] * img_shape[1]

    total_damage_area = 0
    damage_count = len(boxes)

    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        box_area = (x2 - x1) * (y2 - y1)
        total_damage_area += box_area.item()

    damage_ratio = total_damage_area / img_area

    # Score calculation
    score = max(0, 100 - int(damage_ratio * 200))

    if score > 80:
        condition = "Good"
    elif score > 50:
        condition = "Moderate"
    else:
        condition = "Critical"

    return score, condition
