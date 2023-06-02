def suppimer_element(liste,element):
    new_liste = []
    for x in liste:
        if x !=element:
            new_liste += [x] # new_liste.append(x)
    return new_liste

print("suppimer element")
print(suppimer_element([8,7,4,6,5,4],4))