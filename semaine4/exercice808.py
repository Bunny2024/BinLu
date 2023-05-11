#Le volume d’un cube en fonction de la longueur d’un côté,
from cmath import pi


def volume_cube(a):   
    volume = a ** 3 
    return volume

volume = volume_cube(float(input("Entre la longueur d’un côté: ")))
print(volume)

# Le volume d’une boule en fonction de son rayon
def volume_boule(r):   
    volume = (4 / 3) * pi * r ** 3
    return volume

volume = volume_boule(float(input("Entre le rayon d’une boule: ")))
print(volume)

# Le volume d’un cylindre en fonction du rayon de sa base et de sa hauteur
def volume_cylindre(r , h):   
    volume = h* pi * r ** 2
    return volume

volume = volume_cylindre(float(input("Entre le rayon d’une cylindre: ")),\
    float(input("Entre la hauteur d’une cylindre: ")))
print(volume)

# Le volume d’une boîte parallélépipède rectangle en fonction de ses trois dimensions.
def volume_boite(x , y, z):   
    volume = x* y * z
    return volume

volume = volume_boite(float(input("Entre le x: ")),float(input("Entre le y: "))\
    ,float(input("Entre le z: ")))
print(volume)