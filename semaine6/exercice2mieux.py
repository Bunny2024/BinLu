def met_au_pluriel(mot):

    derniere_lettre = mot [len(mot) - 1 ]
    avant_derniere_lettre = mot [len(mot) - 2 ]

    if derniere_lettre == "s":
        pluriel = mot 
    elif avant_derniere_lettre == "a" and derniere_lettre == "l":
        debut_mot = mot [ 0 : len(mot) - 2]
        pluriel = debut_mot + "aux"
    else:
        pluriel = mot + "s"
    return pluriel

mot = input("Dis moi un mot : ")
pluriel =met_au_pluriel(mot)

print("Mon mot :", mot)
print("Au pluriel :", pluriel)
