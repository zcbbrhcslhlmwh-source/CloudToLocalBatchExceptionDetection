import os
import json

DATA_DIR = "./data"

def data_loader(start_time=None, end_time=None):
    data_list = []

    for filename in os.listdir(DATA_DIR):
        if not filename.endswith(".json"):
            continue

        file_path = os.path.join(DATA_DIR, filename)

        with open(file_path, "r") as f:
            data = json.load(f)

            # 时间筛选（简单版）
            if start_time and end_time:
                ts = data["timestamp"]
                if not (start_time <= ts <= end_time):
                    continue

            data_list.append(data)

    return data_list