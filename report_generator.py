def generate_report(score, condition, damage_count):
    report = f"""
Road Inspection Report

Total Damages Detected: {damage_count}
Road Health Score: {score}/100
Condition: {condition}

Recommendation:
"""

    if condition == "Good":
        report += "Routine monitoring recommended."
    elif condition == "Moderate":
        report += "Preventive maintenance within 6 months."
    elif condition == "Poor":
        report += "Repair required soon."
    else:
        report += "Immediate maintenance required."

    return report
