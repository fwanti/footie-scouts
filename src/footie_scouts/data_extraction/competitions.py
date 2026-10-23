import requests
import os
from pathlib import Path
from dotenv import load_dotenv

root_dir = Path(__file__).resolve().parents[3]
load_dotenv(root_dir / ".env")

token = os.getenv("FOOTBALL_DATA_API_KEY")
base_uri = "https://api.football-data.org/v4"

if not token:
    raise ValueError("FOOTBALL_DATA_API_KEY is not configured")

def get_competitions() -> list[dict]:
    
    response = requests.get(
        f'{base_uri}/competitions/', 
        headers={'X-Auth-Token': token },
        timeout=30)

    response.raise_for_status()

    return response.json()['competitions']