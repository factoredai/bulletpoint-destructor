import os

import openai
from dotenv import find_dotenv, load_dotenv

load_dotenv(dotenv_path=find_dotenv(filename=".env"))

openai.api_key = os.environ["OPENAI_API_KEY"]
