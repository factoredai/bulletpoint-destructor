import json
from typing import Dict, List

import pandas as pd


def parse_bullet_logs(logs_path: str) -> List[Dict]:

    bullet_points = []

    with open(file=logs_path, mode="r") as f:
        for line in f:
            _, json_data = line.strip().split(",", 1)
            bullet_point = "{" + json_data.split(sep="{")[1]
            bullet_point_as_json = json.loads(bullet_point)
            bullet_points.append(bullet_point_as_json)

    return bullet_points


raw_bullets = parse_bullet_logs(logs_path="data/raw/logs_2.txt")


def clean_bullets(bullets: List[Dict]) -> pd.DataFrame:

    bullet_points = pd.DataFrame(data=bullets)
    bullet_points = bullet_points.fillna(value="")
    bullet_points["skills"] = bullet_points["skills"].apply(lambda x: ", ".join(x))
    return bullet_points
