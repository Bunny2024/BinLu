message = input("Enter a string:")

l = list(message)
print(l)

dictionary = {}

for characters in message:
    dictionary[characters] = True
    
print(dictionary)

for characters in message:    
    if characters in dictionary.keys():
        dictionary[characters] = dictionary[characters] + 1
    else:
        dictionary[characters] = 1


print(dictionary)

