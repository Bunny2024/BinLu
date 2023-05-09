def compute_cube (number): # number: parameter
    """cette fonction calcule la valeu cubique de parameter"""
    cube = number ** 3
    print(cube)

number1 = int(input("Entre a value:"))
cube1 = compute_cube(number1)

number2 = int(input("Entre a value:"))
cube2 = compute_cube(number2)

somme = cube1 + cube2
print(somme)

# somme = compute_cube(number1) + compute_cube(number2)
# print(somme)
