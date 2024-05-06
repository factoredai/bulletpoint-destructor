import json
from typing import Dict, List

import pandas as pd
from openai import OpenAI
from tqdm import tqdm

from src.modeling.prompt_templates import SYSTEM_MESSAGE
from src.utils.configs import OPENAI_API_KEY

class BulletExtractor:
    def __init__(self, model_name: str = "gpt-3.5-turbo-0125") -> None:
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model_name = model_name

    @staticmethod
    def build_chat_messages(bullet_point: str) -> List[Dict[str, str]]:
        return [
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": bullet_point},
        ]

    def extract_entities(self, bullet_point: str) -> Dict[str, str]:
        messages = self.build_chat_messages(
            bullet_point=bullet_point,
        )

        response = self.client.chat.completions.create(
            messages=messages,
            model=self.model_name,
            response_format={"type": "json_object"},
        )

        return json.loads(s=response.choices[0].message.content)

    def extract_entities_for_all_bullets(
        self, bullets: List[Dict[str, str]]
    ) -> pd.DataFrame:
        bullet_point_entities = [
            self.extract_entities(bullet_point=bullet["raw_bullet"])
            for bullet in tqdm(iterable=bullets)
        ]

        return pd.DataFrame(data=bullet_point_entities)
