# un programme qui lit le nom d'un mois de l'utilisateur sous la forme d'une chaîne de caractères. 
# Ensuite, votre programme doit afficher le nombre de jours de ce mois. 
#Affichez "28 ou 29 jours" pour le mois de février afin de tenir compte des années bissextiles.

# donne un mois
mois = input("Entrez un mois: ")

if mois in ['janvier', 'mars', 'mai', 'juillet', 'août', 'octobre', 'décembre']:
    print(f"Le mois de {mois} a 31 jours.")
elif mois in ['avril', 'juin', 'septembre', 'novembre']:
    print(f"Le mois de {mois} a 30 jours.")
elif mois == 'février':
    print(f"Le mois de {mois} a 28 ou 29 jours.")
else:
    print("Erreur d'entrée.")