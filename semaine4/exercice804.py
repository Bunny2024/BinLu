from inspect import formatargvalues


def affiche_salutation(formule):
    """cette fontion demande a l"""
    nom = input("Enter your name: ")
    answer = formule + " "+ nom
    print(answer)

affiche_salutation("Coucou")