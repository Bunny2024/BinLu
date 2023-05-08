# EXERCICE 8
# Écrivez un programme qui commence par lire un rayon, r, de l'utilisateur. 
# Le programme continuera en calculant et en affichant l'aire d'un cercle de rayon r et le volume d'une sphère derayon r. 
# Utilisez le constant pi du module Math dans vos calculs. 
# Aide : l'aire d'un cercle se calcule à l'aide de la formule : 𝑎𝑖𝑟𝑒 = 𝜋𝑟2. 
# Le volume d'une sphère est calculé à l'aide de la formule 𝑣𝑜𝑙𝑢𝑚𝑒 =4/3𝜋𝑟^3

from math import pi # pi=3.14
# lire le rayon

rayon = int(input("Enter the radius: "))

# calculer l'aire
Aire =pi * rayon **2
Aire = round(Aire, 2)

#aire = pi * rayon * rayon

# calculer le volume
Volume = 4/3 *pi * rayon **3
Volume = round(Volume, 2)

# affcihage
print(f"aire = {Aire}\n volume ={Volume}")
