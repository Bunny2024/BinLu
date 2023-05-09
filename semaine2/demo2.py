#age = 16

# if  age >=18:
#    print("Tu peux voter.")  
# if  age < 18:
#else:
#    print("Go sleep.")


# age = int(input("Enter your age:"))
# name = input("Enter your name:")
# gender = input("Enter your gender:")
# print(gender.upper())
# print(f"Bonjour,{name}") 

# if  age >=18 and gender =="M": 
#     print("Tu peux voter.")  
# else: #   print("Sorry.\nGo sleep.")  
# print("end")

age = int(input("Quel est votre age?"))
montant = 50

if age < 12:
    print("L'entrée est gratuite.")
    discount = 1
elif age < 25:
    print("Vous bénéficiez d'une réduction de 25%.")
    discount = 0.25
# if age >=25:
else:
    print("Vous ne bénéficiez pas de réduction.")
    discount = 0

#calculateur
pay =montant * (1-discount)

# affiche
print(f"Your ticket = {pay}$")


