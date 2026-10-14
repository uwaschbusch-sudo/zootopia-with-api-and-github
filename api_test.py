import os

import requests
from dotenv import load_dotenv

API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_response(name):
    """Sendet die Anfrage an die API und gibt die Antwort zurück."""
    # Key aus der .env-Datei laden
    load_dotenv()
    api_key = os.getenv("API_KEY")
    # Abbruch, wenn kein Key vorhanden ist
    if not api_key:
        raise SystemExit("API_KEY fehlt in der .env-Datei.")
    # Anfrage mit Tiername und Key senden
    return requests.get(
        API_URL,
        params={"name": name},
        headers={"X-Api-Key": api_key},
        timeout=10,
    )


def main():
    """Fragt einen Tiernamen ab und zeigt die Antwort an."""
    # Tiername einlesen
    name = input("Tiername: ").strip()
    response = fetch_response(name)
    # Statuscode und Anfang der Antwort ausgeben
    print("Statuscode:", response.status_code)
    print("Antwort:", response.text[:500])


if __name__ == "__main__":
    main()
