def calculate_severity(damage_count):
    if damage_count <= 2:
        return 85, "Good"
    elif damage_count <= 5:
        return 60, "Moderate"
    elif damage_count <= 10:
        return 40, "Poor"
    else:
        return 20, "Critical"
