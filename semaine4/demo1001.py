# def addtition( a , b ):   
#     somme = a + b  # somme :variable local
#     return somme

# a = [1, 2, 3] # variable global
# print(a)
# print(id(a))
# print("========")

# a . append(4)
# print(a)
# print(id(a))
# print("========")

# def add( a ):
#     print(f"a = {a} and its id = {id(a)}")
#     a .append (18)
#     print(f"a = {a} and its id = {id(a)}")

# number = [1, 2, 3]
# print(f"nomber = {number} and its id = {id(number)} ")
# add(number)

# print(f"nomber = {number} and its id = {id(number)} ")


def add( number ):
    print(f"number = {number} and its id = {id(number)}")
    number = number+ 1
    print(f"number = {number} and its id = {id(number)}")

number = 1
print(f"nomber = {number} and its id = {id(number)} ")

add(number)
print(f"nomber = {number} and its id = {id(number)} ")