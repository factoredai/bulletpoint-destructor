import json
from typing import Dict, List

import pandas as pd
from openai import OpenAI
from tqdm import tqdm

from src.modeling.bullet_descriptiors import SYSTEM_MESSAGE

client = OpenAI()


def build_chat_messages(bullet_point: str) -> List[Dict[str, str]]:
    return [
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": bullet_point},
    ]


def extract_entities(bullet_point: str) -> Dict[str, str]:

    messages = build_chat_messages(
        bullet_point=bullet_point,
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=messages,
    )

    return json.loads(s=response.choices[0].message.content)


def compute_ner_for_all_bullets(bullets: List[Dict[str, str]]) -> pd.DataFrame:

    bullet_point_entities = [
        extract_entities(bullet_point=bullet["raw_bullet"]) for bullet in tqdm(bullets)
    ]

    return pd.DataFrame(data=bullet_point_entities)
