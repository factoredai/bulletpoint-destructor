from typing import Dict, List

import jellyfish
import numpy as np
import pandas as pd
from sacrebleu.metrics.bleu import BLEU
from tqdm import tqdm


def compute_string_similarity(prediction: str, reference: str) -> float:
    return np.round(jellyfish.jaro_similarity(prediction, reference), 2)


def compute_bullet_descriptors_scores(
    predictions: Dict[str, str], references: Dict[str, str]
) -> Dict[str, float]:
    scores = {}
    for bullet_description in ["what", "how", "why", "whom", "skills"]:
        scores[bullet_description] = compute_string_similarity(
            prediction=predictions[bullet_description].lower(),
            reference=references[bullet_description].lower(),
        )
    return scores


def compute_all_bullet_scores(
    predictions: List[Dict[str, str]], references: List[Dict[str, str]]
) -> pd.DataFrame:
    bullet_scores = [
        compute_bullet_descriptors_scores(
            predictions=predictions[i], references=references[i]
        )
        for i in tqdm(range(len(predictions)))
    ]

    return pd.DataFrame(data=bullet_scores)


def compute_blue_score(
    predictions: Dict[str, str], references: Dict[str, str]
) -> Dict[str, float]:
    bleu = BLEU()
    description_scores = {}
    for bullet_description in ["what", "why", "how", "whom", "skills"]:
        if references[bullet_description] == "":
            description_scores[bullet_description] = 0.0

        else:
            description_scores[bullet_description] = bleu.corpus_score(
                hypotheses=predictions[bullet_description],
                references=references[bullet_description],
            ).score
    return description_scores
