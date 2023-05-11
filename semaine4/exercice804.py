from inspect import formatargvalues


def affiche_salutation(formule):
    """cette fontion demande a l`utilisateur son prenom et affiche ensuit"Bonjour"suivi"""
    # demande a l`utilisateur son prenom
    nom = input("Enter your name: ") # nome.uppe
    answer = formule + " "+ nom

    # affiche ensuite (formule) suivi du prénom de l`utilisateur
    print(answer)

affiche_salutation("Coucou")