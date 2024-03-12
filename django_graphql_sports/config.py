import os
from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()


@dataclass
class AppConfig:
    FOOTBALL_URL: str
    FOOTBALL_API_KEY: str
    BASKETBALL_URL: str
    BASKETBALL_API_KEY: str


def get_config():
    return AppConfig(
        FOOTBALL_URL=os.getenv('FOOTBALL_URL'),
        FOOTBALL_API_KEY=os.getenv('FOOTBALL_API_KEY'),
        BASKETBALL_URL=os.getenv('BASKETBALL_URL'),
        BASKETBALL_API_KEY=os.getenv('BASKETBALL_API_KEY')
    )