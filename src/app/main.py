from typing import Dict

import uvicorn
from fastapi import FastAPI

from src.modeling.openai_ner import extract_entities

app = FastAPI()


@app.get(path="/bullet_point_descriptors")
def compute_bullet_point_descriptors(bullet_point: str) -> Dict[str, str]:
    return extract_entities(
        bullet_point=bullet_point,
    )


if __name__ == "__main__":
    # For local development:
    uvicorn.run("src.app.main:app", port=3000, reload=True)

    # For Docker deployment:
    #uvicorn.run("main:app", host="0.0.0.0", port=80)
