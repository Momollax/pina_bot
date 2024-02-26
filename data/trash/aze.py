import json
import urllib.parse

# Charger le fichier JSON d'origine
with open("toto.json", "r") as f:
    data = json.load(f)

# Initialiser une liste pour stocker les objets avec leur rareté, leur URL et leur valeur (le cas échéant)
objets_rarete_url_value = []

# Parcourir chaque objet dans les données
for objet in data["item"]:
    # Vérifier si l'objet a une clé "rarity"
    if "rarity" in objet:
        # Extraire le nom de l'objet, sa rareté et sa source
        nom_objet = objet["name"]
        rarete_objet = objet["rarity"]
        source_objet = objet["source"]
        # Créer l'URL en formatant le nom de l'objet
        url_objet = "https://5e.tools/items.html#" + urllib.parse.quote_plus(nom_objet.replace(" ", "%20")) + "_" + source_objet
        # Vérifier si l'objet a une clé "value"
        if "value" in objet:
            valeur_objet = objet["value"]
        else:
            valeur_objet = None
        # Ajouter le nom de l'objet, sa rareté, sa source, son URL et sa valeur à la liste
        objets_rarete_url_value.append({"name": nom_objet, "rarity": rarete_objet, "source": source_objet, "url": url_objet, "value": valeur_objet})

# Trier les objets par rareté
objets_rarete_url_value_tries = sorted(objets_rarete_url_value, key=lambda x: x["rarity"])

# Écrire la liste d'objets avec leur rareté triés, leur URL et leur valeur (le cas échéant) dans un nouveau fichier JSON
with open("objets_rarete_url_value_tries.json", "w") as f:
    json.dump(objets_rarete_url_value_tries, f, indent=4)
