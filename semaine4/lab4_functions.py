def demande_prenom_nom():
    firstNome = input("Enter your firstname: ") 
    lastNome = input("Enter your lastname: ") 
    answer = firstNome + " "+ lastNome.upper()

    # affiche ensuite (formule) suivi du prénom de l`utilisateur
    print(answer)