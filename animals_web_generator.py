# Bonus - Python Filtering

import json

PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """Lädt eine JSON-Datei und gibt deren Inhalt zurück."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_text_file(file_path):
    """Liest eine Textdatei und gibt ihren Inhalt als String zurück."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_text_file(file_path, content):
    """Schreibt den übergebenen String in eine Textdatei."""
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)


def get_available_skin_types(animals_data):
    """Ermittelt alle im Datensatz vorkommenden skin_type-Werte."""
    skin_types = set()
    for animal in animals_data:
        skin_type = animal.get("characteristics", {}).get("skin_type")
        if skin_type:
            skin_types.add(skin_type)
    return sorted(skin_types)


def ask_user_for_skin_type(available_skin_types):
    """Zeigt die verfügbaren skin_type-Werte an und fragt den Nutzer."""
    print("Verfügbare Skin Types:")
    for skin_type in available_skin_types:
        print(f"- {skin_type}")

    while True:
        chosen_skin_type = input("Bitte einen Skin Type eingeben: ").strip()
        if chosen_skin_type in available_skin_types:
            return chosen_skin_type
        print("Ungültige Eingabe, bitte einen Wert aus der Liste wählen.")


def filter_animals_by_skin_type(animals_data, skin_type):
    """Gibt nur die Tiere zurück, deren skin_type exakt übereinstimmt."""
    return [
        animal
        for animal in animals_data
        if animal.get("characteristics", {}).get("skin_type") == skin_type
    ]


def serialize_animal(animal):
    """Erzeugt für ein Tier eine HTML-Karte mit Titel und Detailliste."""
    characteristics = animal.get("characteristics", {})
    locations = animal.get("locations", [])

    output = '<li class="cards__item">\n'

    if "name" in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    output += '  <div class="card__text">\n'
    output += '    <ul class="card__list">\n'
    if "diet" in characteristics:
        output += f"      <li class=\"card__list-item\"><strong>Diet:</strong> {characteristics['diet']}</li>\n"
    if locations:
        output += f"      <li class=\"card__list-item\"><strong>Location:</strong> {locations[0]}</li>\n"
    if "type" in characteristics:
        output += f"      <li class=\"card__list-item\"><strong>Type:</strong> {characteristics['type']}</li>\n"
    if "lifespan" in characteristics:
        output += f"      <li class=\"card__list-item\"><strong>Lifespan:</strong> {characteristics['lifespan']}</li>\n"
    if "color" in characteristics:
        output += f"      <li class=\"card__list-item\"><strong>Color:</strong> {characteristics['color']}</li>\n"
    if "skin_type" in characteristics:
        output += f"      <li class=\"card__list-item\"><strong>Skin Type:</strong> {characteristics['skin_type']}</li>\n"
    output += "    </ul>\n"
    output += "  </div>\n"

    output += "</li>\n"
    return output


def build_animals_output(animals_data):
    """Erzeugt einen HTML-String mit einer Karte pro Tier."""
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def main():
    """Fragt einen Skin Type ab und erzeugt animals.html nur dafür."""
    animals_data = load_data("animals_data.json")
    template = read_text_file("animals_template.html")

    available_skin_types = get_available_skin_types(animals_data)
    chosen_skin_type = ask_user_for_skin_type(available_skin_types)
    filtered_animals = filter_animals_by_skin_type(animals_data, chosen_skin_type)

    animals_output = build_animals_output(filtered_animals)
    html_content = template.replace(PLACEHOLDER, animals_output)

    write_text_file("animals.html", html_content)


if __name__ == "__main__":
    main()
