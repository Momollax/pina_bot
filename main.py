import random

def get_raretée():
    print("Bot pour roll les items D&D de pina")
    rarity_input = input("entrez la raretee de l'item:\n1) Commun\n2) Commun a lien\n3) peu commun\n4) peu commun lien\n5) rare\n6) rare lien\n7) tres rare\n8) tres rare lien\nreponse: ")

    try:
        rarity = int(rarity_input)
    except ValueError:
        print("Erreur : vous devez entrer un nombre entier entre 1 et 8")
        return None

    if rarity < 1 or rarity > 8:
        print("Erreur : vous devez entrer un nombre entier entre 1 et 8")
        return None

    quantity_input = input("entrez le nombre d'items a generer: ")
    try:
        quantity = int(quantity_input)
    except ValueError:
        print("Erreur : vous devez entrer un nombre entier")
        return None

    if quantity < 1:
        print("Erreur : le nombre d'items doit etre superieur a 0")
        return None

    return rarity, quantity

def handle_rarity(file_name, quantity):
    number_item = count_lines_in_file(file_name)
    items = get_items(quantity, number_item)
    lines = extract_lines_from_file(file_name, items)
    if lines:
        write_to_file(items, lines + '\n')
        

def handle_common(quantity):
    handle_rarity("common.txt", quantity)

def handle_common_link(quantity):
    handle_rarity("common_link.txt", quantity)

def handle_uncommon(quantity):
    handle_rarity("uncommon.txt", quantity)

def handle_uncommon_link(quantity):
    handle_rarity("uncommon_link.txt", quantity)

def handle_rare(quantity):
    handle_rarity("rare.txt", quantity)

def handle_rare_link(quantity):
    handle_rarity("rare_link.txt", quantity)

def handle_very_rare(quantity):
    handle_rarity("very_rare.txt", quantity)

def handle_very_rare_link(quantity):
    handle_rarity("very_rare_link.txt", quantity)

def handle_error():
    print("Rareté invalide")

def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as f:
            return len(f.readlines())
            
    except FileNotFoundError:
        print(f"Le fichier {filename} est introuvable")
        return None

def get_items(quantity, number_item):
    items = []
    for i in range(quantity):
        items.append(random.randint(1, number_item))
    print("roll des dé: ", items)
    items_sorted = sorted(items)
    print("items triés: ", items_sorted)
    return items_sorted

def extract_lines_from_file(filename, items):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            extracted_lines = []
            for item in items:
                if item <= len(lines):
                    extracted_lines.append(lines[item-1].strip().replace('[','').replace(']',''))
                else:
                    extracted_lines.append(f"L'item {item} n'existe pas dans le fichier {filename}")
            f.close()
            return '\n'.join(extracted_lines)
    except FileNotFoundError:
        print(f"Le fichier {filename} est introuvable")
        return None


def write_to_file(items, text):
    lignes = text.split('\n')
    with open('response.txt', 'w') as f:
        f.writelines("roll des de: ")
        f.writelines([str(i) + ' ' for i in items])
        f.writelines('\n\n')
        f.writelines('\n\n'.join(lignes))

def main():
    rarity_and_quantity = get_raretée()

    if rarity_and_quantity is None:
        return

    rarity, quantity = rarity_and_quantity

    switcher = {
        1: lambda: handle_rarity("data/common.txt", quantity),
        2: lambda: handle_rarity("data/common_link.txt", quantity),
        3: lambda: handle_rarity("data/uncommon.txt", quantity),
        4: lambda: handle_rarity("data/uncommon_link.txt", quantity),
        5: lambda: handle_rarity("data/rare.txt", quantity),
        6: lambda: handle_rarity("data/rare_link.txt", quantity),
        7: lambda: handle_rarity("data/very_rare.txt", quantity),
        8: lambda: handle_rarity("data/very_rare_link.txt", quantity),
    }

    func = switcher.get(rarity, handle_error)
    func()


if __name__ == "__main__":
    main()
