import json
from urllib.parse import quote

base_url = "https://5e.tools/items.html#"
# Charger le contenu du fichier JSON
with open('toto.json', 'r') as fichier_json:
    data = json.load(fichier_json)

files="very_rare.txt"

# Ouvrir le fichier en mode lecture
with open(files, 'r') as fichier_txt:
    lignes = fichier_txt.readlines()

# Comparer les noms avec les noms des objets dans le fichier JSON
for i, ligne in enumerate(lignes):
    nom_objet = ligne.strip().split(',')[0]
    for item in data.get('item', []):
        if item.get('name') == nom_objet:
            source = item.get('source')
            if source:
                url_partie = quote(nom_objet.lower()).replace(' ', '%20') + "_" + source
                url_complet = base_url + url_partie
                # Mettre à jour la ligne avec la virgule et l'URL
                ligne_mise_a_jour = ligne.strip() + f", {url_complet}\n"
                lignes[i] = ligne_mise_a_jour

# Écrire les lignes mises à jour dans le fichier .txt
with open(files, 'w') as fichier_txt:
    fichier_txt.writelines(lignes)