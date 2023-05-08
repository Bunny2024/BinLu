# EXERCICE 3
# Créer un programme qui lit la longueur et la largeur en pieds carrés 
# d’un champ d'agriculteur de l'utilisateur. 
# Votre programme doit afficher la superficie du champ en hectares. 
# Aide : Chaque hectare vaut 43 560 pieds carrés.

# lire la large
Largeur = float(input("Enter the width of the field in feet: "))
# Largeur = input("Enter the width of the room: ")
# largeur = float(Largeur)

# lire la longueur
Longeur = float(input("Enter the longth of the field in feet: "))

SQFT = 43560

# calculer la surface
area = Largeur * Longeur # en pieds carrés
area = area / SQFT
area = round(area, 2)

# area = round(Largeur * Longeur/43500, 2)

# affichage
print(f"The area of the room is {area} in sqft")
