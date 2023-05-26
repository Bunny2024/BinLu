# select third in the list

# def select_third(mylist):
#     if len(mylist) >= 3:
#         return mylist[2]
#     else:
#         return None

def select_third(mylist):
    if len(mylist) >= 3:
        return mylist[2]
    return None

list1 = [1,3,5,7,9]
list2 = [1,3]

third = select_third(list1)
print(third)

third = select_third(list2)
print(third)

