# EXERCICE 2
# Écrivez un programme qui demande à l'utilisateur de saisir la largeur et la longueur d'une salle.
# Une fois les valeurs lues, votre programme doit calculer et afficher la surface de cette salle. 
# La longueur et la largeur seront saisies sous forme de nombres à virgule flottante.

# lire la large
Largeur = float(input("Enter the width of the room: "))
# Largeur = input("Enter the width of the room: ")
# largeur = float(Largeur)

# lire la longueur
Longeur = float(input("Enter the longth of the room: "))

# calculer la surface
area = Largeur * Longeur

# afficher le resultat
# print("The area of the room is ", area)
# print("The area of the room is "+ str( area))
print(f"The area of the room is {area}")

