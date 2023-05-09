def soustraction ( a, b ):
    """ma fonction fait la soustraction entre a et b"""
    sous = a - b
    return sous
print( help( soustraction ))

def addition (a, b):
    """ma fonction fait la addition entre a et b"""
    add = a+ b
    return add
print( help( addition ))

def compute_cube (number): # number: parameter
    """cette fonction calcule la valeu cubique de parameter"""
    cube = number ** 3
    return cube
s = compute_cube(5) # number : argument
print(s)

def sayhello():
    print("Hello everyone!")
    return

sub = soustraction ( 10 , 3 )
print(sub)

sub = addition (3, 6)
print(sub)

sayhello()

salut = sayhello()
print(salut)

ali = int(input("Entre a value:"))
cube = compute_cube(ali) # number:argument
print(cube)

def compute_cube (number): # number: parameter
    """cette fonction calcule la valeu cubique de parameter"""
    cube = number ** 3
    print(cube)

