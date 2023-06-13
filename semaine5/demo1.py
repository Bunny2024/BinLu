list_1= [ 1,2,3 ]

list_2 = list_1
# list_2.append (4)
list_2.insert(1,9)
print(list_1)
print(list_2)
list_3 = list_1.copy()
list_3.append ( 4 )
list_4 = list_1[:] + list_3
print(list_3)

print(list_4)
# print(id(list_1),id(list_2),id(list_3),id(list_4))
# longueur = len(list_4)
# print(longueur)