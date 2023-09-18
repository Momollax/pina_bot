# Ouvrir le fichier en mode lecture
files="very_rare.txt"
with open(files, "r") as f:
    lines = f.readlines()

# Ouvrir le fichier en mode écriture
with open(files, "w") as f:
    for line in lines:
        elements = line.strip().split(",")  # Diviser la ligne en éléments
        if len(elements) >= 2:
            first_element = elements[0].strip()
            second_element = elements[1].strip()
            f.write(f"{first_element},{second_element}\n")  # Réécrire les deux premiers éléments