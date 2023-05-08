# EXERCICE 4
# Écrivez un programme qui lit un nombre entier positif, n, de l'utilisateur. 
# Ensuite il affiche la somme de tous les nombres entiers positifs de 1 à n. 
# La somme des n premiers entiers positifs peut être calculée à l'aide de la formule: 
# 𝑆= 𝑛(𝑛+1)/2

# lit un nombre entier positif , n
n = int(input("Enter a positive integer: "))

# calculer la somme de tous les nombres entiers positifs de 1 à n: 1 + 2 + 3+...
somme = n * (n +1)/2 
somme = int (somme)

# affiche la somme
print(f"the sum of the {n} positive integers is {somme}")


