# Créez un programme qui convertit les notes en chiffres vers des notes en lettres.

print("Letter Grade Converter\n")

while True:
    
    # donne un note:
    note = int(input("Entrez numerical grade: "))
    if note > 100 or note <0:
        print("Erreur d'entrée.")
    elif note > 87:
        print("Note en lettre :A")
    elif note > 79:
        print("Note en lettre :B")
    elif note > 66:
        print("Note en lettre :C")
    elif note > 60:
        print("Note en lettre :D")
    else:
        print("Note en lettre :F")

    continu = input("\nContinue(y/n)?: ")
    if continu == "n":
        break

print("\nBye!")