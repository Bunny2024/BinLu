# EXERCICE 9
# Une machine découpe dans une plaque, des disques circulaires de rayon rExt, 
# percés d’un trou circulaire de rayon rInt avec rInt < rExt et ne débordant pas du disque. 
#Quelle est la surface d’un disque découpé ?

# lire le rayon rExt
rExt = float(input("Enter the rayon rExt: "))

# lire le rayon rInt
rInt = float(input("Enter the rayon rInt: "))

#calculer la surface
from math import pi # pi=3.14

surface1 = pi * rExt **2
surface2 = pi * rInt **2
surface = surface1 -surface2
surface = round(surface, 2)

# affcihage
print(f"La surface d'un disque découpé = {surface} ")