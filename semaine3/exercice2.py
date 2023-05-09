# Créez un programme qui convertit les notes en chiffres vers des notes en lettres.

print("Letter Grade Converter\n")
             # continu ="y"
while True:  # continu =="y":
    
    # donne un note:
    note = int(input("Entrez numerical grade: ")) #letter = F,pas besoin le else
    if note > 100 or note <0:
        print("Erreur d'entrée.") 
    elif note > 87:
        print("Note en lettre :A") # letter = A
    elif note > 79:
        print("Note en lettre :B") # letter = B
    elif note > 66:
        print("Note en lettre :C") # letter = C
    elif note > 60:
        print("Note en lettre :D") # letter = D
    else:
        print("Note en lettre :F") # letter = E
    # print("Note en lettre :",letter)
    continu = input("\nContinue(y/n)?: ")
    if continu == "n":
        break

print("\nBye!")