# Vous devez écrire un programme qui demande à son utilisateur un nombre entier.

# donne un lettre:
nombre = int(input("Entez un nombre entier: "))

# Si ce nombre est négatif, le programme devra afficher le message « nombre refusé »
if nombre < 0:
    print(nombre, "nombre refusé ")
else:
# La parité du nombre (pair ou impaire) ;
    if nombre % 2 == 0:
        print("Le nombre est pair.")
    elif nombre % 2 == 1:
        print("Le nombre est impair.")
        12
# Si le nombre est un multiple de 10 (s’il ne l’est pas, le programme ne l’affiche pas 
if nombre % 10 == 0:
    print("Le nombre est un multiple de 10.")

# Si c’est un nombre à un, deux ou trois chiffres ou plus.
if nombre < 10:
    print("Le nombre a un chiffre.")
elif nombre < 100:
    print("Le nombre a deux chiffre.")
elif nombre >= 100:
    print("Le nombre a trois chiffre ou plus.")
