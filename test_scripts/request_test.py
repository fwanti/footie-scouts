import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv

root_dir = Path(__file__).resolve().parents[1]
load_dotenv(root_dir / ".env")

token = os.getenv("FOOTBALL_DATA_API_KEY")
base_uri = "https://api.football-data.org/v4"

if not token:
    raise ValueError("FOOTBALL_DATA_API_KEY is not configured")

def get_areas() -> list[dict]:

    response = requests.get(
        f'{base_uri}/areas/', 
        headers={'X-Auth-Token': token },
        timeout=30)

    response.raise_for_status()

    return response.json()['areas']                

def get_competitions() -> list[dict]:
    
    response = requests.get(
        f'{base_uri}/competitions/', 
        headers={'X-Auth-Token': token },
        timeout=30)

    response.raise_for_status()

    return response.json()['competitions']

def areas_transformation():
    response = get_areas()
    areas = []
    for area in response:
        item = (
            area['id'],             
            area['name'],
            area['parentArea'],
            area['parentAreaId']
        )

        if item not in areas:
            areas.append(item)
    for i in areas: print(i)

def competitions_transformation():
    response = get_competitions()
    competitions = []
    competitions = []
    for competition in response:
            item = (
                competition['id'],                
                competition['name'],
                competition['area']['name'],
                competition['lastUpdated']

            )   
                 
            if item not in competitions:
                competitions.append(item)

    for i in competitions: print(i)
