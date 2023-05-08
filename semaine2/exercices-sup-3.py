# Vous devez écrire un petit programme qui demande la saisie d’une lettre correspondant à un menu. 

print("=" * 50 + "\nMenu\n" + "=" * 50)

# donne un lettre:
lettre = input("Entez un caractere: ")

if lettre in ['A', 'B', 'Q']:
    print(f"Vous avez choisi le menu {lettre} ")
else:
    print("Votre choix est invalide.")

print("=" * 50 + "\nFin!" )