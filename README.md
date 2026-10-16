# Zootopia With API

Kleines Programm, das eine Tier-Website erzeugt. Du gibst einen Tiernamen ein, das Programm holt passende Tiere von der [API Ninjas Animals API](https://api-ninjas.com/api/animals) und schreibt sie in `animals.html`.

## Dateien

- `animals_web_generator.py` - fragt den Tiernamen ab und erzeugt die Website
- `data_fetcher.py` - holt die Tierdaten von der API
- `animals_template.html` - HTML-Vorlage
- `requirements.txt` - benötigte Python-Pakete

## Installation

1. Repository klonen:

```bash
git clone https://github.com/uwaschbusch-sudo/zootopia-with-api-and-github.git
cd zootopia-with-api-and-github
```

2. Pakete installieren:

```bash
pip install -r requirements.txt
```

3. Kostenlosen API-Key bei [API Ninjas](https://api-ninjas.com) holen.

4. Im Projektordner eine Datei `.env` mit genau dieser Zeile anlegen:

```
API_KEY=dein_api_key
```

Die `.env` steht in der `.gitignore` und wird nicht hochgeladen. Gib deinen Key nie weiter.

## Nutzung

```bash
python animals_web_generator.py
```

Beispiel:

```
Enter a name of an animal: Fox
Website was successfully generated to the file animals.html.
```

Öffne `animals.html` im Browser. Gibt es kein passendes Tier, zeigt die Website eine Meldung.