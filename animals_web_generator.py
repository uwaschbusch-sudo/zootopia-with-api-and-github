import html

import data_fetcher

PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def read_text_file(file_path):
    """Liest eine Textdatei und gibt ihren Inhalt als String zurück."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_text_file(file_path, content):
    """Schreibt den übergebenen String in eine Textdatei."""
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)


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


def build_not_found_output(animal_name):
    """Erzeugt die HTML-Meldung für ein nicht gefundenes Tier."""
    # Eingabe maskieren, damit kein fremdes HTML in die Seite gelangt
    safe_name = html.escape(animal_name, quote=False)
    return f'<h2 style="text-align: center;">The animal "{safe_name}" doesn\'t exist.</h2>\n'


def ask_animal_name():
    """Fragt den Nutzer nach einem Tiernamen und gibt ihn zurück."""
    while True:
        name = input("Enter a name of an animal: ").strip()
        # Leere Eingaben abweisen
        if name:
            return name
        print("Please enter a name.")


def main():
    """Fragt einen Tiernamen ab, holt die Daten von der API und erzeugt animals.html."""
    animal_name = ask_animal_name()
    animals_data = data_fetcher.fetch_data(animal_name)
    template = read_text_file("animals_template.html")

    # Leere Antwort der API bedeutet: Tier existiert nicht
    if animals_data:
        animals_output = build_animals_output(animals_data)
    else:
        animals_output = build_not_found_output(animal_name)
    html_content = template.replace(PLACEHOLDER, animals_output)

    write_text_file("animals.html", html_content)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
