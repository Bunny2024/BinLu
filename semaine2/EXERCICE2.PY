# Lit un nombre entier de l'utilisateur. 
# Afficher un message indiquant si l'entier est pair ou impair.

# donne un nombre
nombre = int(input("Entrez un nombre entier: "))

if nombre % 2 == 0:
    print(nombre, "est pair.")
else:
    print(nombre, "est impair.")
