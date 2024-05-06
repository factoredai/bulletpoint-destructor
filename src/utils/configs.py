import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(dotenv_path=find_dotenv(filename=".env"))

OPENAI_API_KEY = os.getenv(key="OPENAI_API_KEY")
