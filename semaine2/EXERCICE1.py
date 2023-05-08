# Exercice1
# On se donne 3 longueurs:a, b et c
#Tu vas déterminer les propriétés de triangle dont

#1.Définis trois variables
# donne 3 longueurs:a, b et c
a = int(input("Enter side 1st:"))
b = int(input("Enter side 2nd:"))
c = int(input("Enter side 3rd:"))

#2.Ordre
if a <= b and b <= c:
    print("Ordre existe,a<=b,b<=c.")
else:
    print("Ordre n'existe pas.")

#3.Existence c <= a + b
somme = a + b 

if c <= somme:
    print("Triangle existe.")
else:
    print("Triangle n'existe pas.")

#4.Triangle rectangle
c_square = c ** 2
b_square = b ** 2
a_square = a ** 2
somme = a_square + b_square 

if c_square == somme :
    print("Triangle rectangle existe.")
else:
    print("Ce n'est pas une Triangle rectangle. ")

#5.Triangle équilatéral
if c == a and b == a:
    print("Triangle équilatéral.")
else:
    print("Ce n'est pas une Triangle équilatéral. ")

#6.Triangle isocèle
if c == a or b == a:
    print("Triangle isocèle.")
else:
    print("Ce n'est pas une Triangle isocèle. ")

#7. Angles aigus
if  c_square > a_square + b_square and b_square > a_square + c_square and a_square > c_square + b_square:
    print("Tous les angles sont aigus.")
else:
    print("Une angle n'est pas angu. ")

