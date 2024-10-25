""" """

import os

from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)


@dataclass
class Settings:
    API_KEY: str
    REDIS_HOST: str
    REDIS_PORT: int


settings = Settings(
    API_KEY=os.getenv("API_KEY"),
    REDIS_HOST=os.getenv("REDIS_HOST"),
    REDIS_PORT=os.getenv("REDIS_PORT")
)
