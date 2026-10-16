import os

import requests
from dotenv import load_dotenv

# Key aus der .env-Datei laden
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """Holt die Tierdaten zum Namen von der API und gibt eine Liste von Dictionaries zurück."""
    # Abbruch, wenn kein Key vorhanden ist
    if not API_KEY:
        raise SystemExit("API_KEY fehlt in der .env-Datei.")
    response = requests.get(
        API_URL,
        params={"name": animal_name},
        headers={"X-Api-Key": API_KEY},
        timeout=10,
    )
    # Bei HTTP-Fehlern eine Ausnahme auslösen
    response.raise_for_status()
    return response.json()
