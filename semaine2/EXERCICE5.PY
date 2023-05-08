# La valeur de classement (rating) attribuée à un employé est soit 0.0, soit 0.4, soit 0.6 ou plus.
# Ces valeurs comprises entre 0.0 et 0.4 et entre 0.4 et0.6 ne sont jamais utilisées. 
# Le montant de l'augmentation d'un employé est égal à 2400,00$ multiplié par sa valeur de classement.
# 0.0 Unacceptable performance 0.4 Acceptable performance 0.6 ou plus Meritorious performance
# Écrivez un programme qui lit le rating de l'utilisateur.
# Et indique si la performance était inacceptable,acceptable ou méritoire.
# Le montant de l'augmentation de l'employé doit également être indiqué.
# programme doit afficher un message d'erreur approprié en cas de saisie d'un rating non valide.


# donne un rating:
rating = float(input("Entrez le rating de l'employé : "))

if rating == 0.0:
    print("La performance est inacceptable.")
    print("Aucune augmentation salariale ne sera accordée.")
elif rating == 0.4:
    # calculer l'augmentation
    augmentation = 0.4 * 2400
    print("La performance de l'employé est acceptable.")
    print(f"L'augmentation salariale de l'employé est de {augmentation}$.")
elif rating >= 0.6:
    # calculer l'augmentation
    augmentation = rating * 2400
    print("La performance de l'employé est méritoire.")
    print(f"L'augmentation salariale de l'employé est de {augmentation}$.")
else:
    print("Erreur d'entrée.")
