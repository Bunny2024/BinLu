# EXERCICE 7
# De nombreuses personnes mesurent leur taille en pied (i.e. en anglais inch) et en pouces.
# Écrivez un programme qui lit le nombre des pieds de l'utilisateur, et le nombre des pouces. 
# Une fois ces valeurs lues, votre programme doit calculer et afficher le nombre équivalent en centimètres.
# Aide : Un pied correspond à 12 pouces. Un pouce correspond à 2,54 centimètres.
# Un pouce = 2.54 cm = 0.083333 pied
# Un pied = 30.48 cm = 12 pouces

# lire le pied
Pied = float(input("Enter the pied: "))

#calculer le longuer
Longuer = Pied * 30.48

# affcihage
print(f"The Longuer = {Longuer} cm")

# lire le pouce
pouce = float(input("Enter the pouce: "))

#calculer le longuer
Longuer2 = pouce * 2.54

# affcihage
print(f"The Longuer = {Longuer2} cm")
