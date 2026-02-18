import csv
import os
from datetime import datetime

LOG_FILE = "inspection_logs.csv"

def log_inspection(damage_count, score, condition, inference_time):
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "Damage Count",
                "Road Health Score",
                "Condition",
                "Inference Time (s)"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            damage_count,
            score,
            condition,
            round(inference_time, 3)
        ])
