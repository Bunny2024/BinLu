#vérifie si un nombre est un nombre parfait ou non.

print("Perfect Number Calculator\n")

# utilisateur donne un number
number = int(input("Enter a number: "))
# for i in range(1, number/2 + 1)
sum = 0
i = 1
while i < number:   
    if number % i == 0 :
        sum += i
    i += 1

if sum == number:
    print("\n",number,"is a prefect number.")
else:
    print("\nSorry,",number,"is not a prefect number.")

print("\nBye!")