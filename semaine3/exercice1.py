#Créez un programme qui commence par lire l'âge de visiteurs  avec un âge saisi sur chaque ligne. 
#L'utilisateur saisira une ligne vide pour indiquer qu'il n'y a plus d'invités dans le groupe. 
#Votre programme doit ensuite afficher le prix d'entrée pour le groupe, 
#accompagné d'un message approprié. 
#Le coût doit être affiché avec deux décimales.

# règles de coût pour chaque groupe d'âge
bebe = 0.00
enfant = 14.00
age = 18.00
adulte = 23.00

# count du visiteur
count_bebe = 0
count_enfant = 0
count_age = 0
count_adulte = 0

# Donne l'âge de chaque visiteur
while True:
    age_str = input("Entrez l'âge du visiteur: ")
    if age_str == "":
        break
    age = int(age_str)
    
    # Count du visiteur au groupe d'âge
    if age <= 2:
        count_bebe += 1
    elif age <= 12:
        count_enfant += 1
    elif age >= 65:
        count_age += 1
    else:
        count_adulte += 1

# Calcul du coût total pour le groupe
total = count_enfant * enfant + count_age * age + count_adulte * adulte

# Affichage du message de coût total
print(f"Le coût total pour votre groupe est: {total:.2f} $.\
      \nParmi eux: {count_bebe} bébé/e/s, gratuite.\
      \n{count_enfant} enfant/e/s, {enfant}$ chacun.\n{count_age} age/e/s, {age}$ chacun.\
      \n{count_adulte} enfant/e/s, {adulte}$ chacun.")
