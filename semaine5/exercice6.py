def inverser(liste):
    new_liste = []
    for element in liste:
        new_liste = [element] + new_liste
    return new_liste

myList = [1,2,3,4]
print(inverser(myList))