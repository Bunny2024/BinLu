# myList=[1,2,3,4]
# print(myList)

# newList = [myList[-1]] + myList.pop(-1)

# print(newList)

def rotation(liste):
    n = len(liste)
    new_list = [liste[n-1]]+liste[0:n-1]
    return new_list

print("---- Rotation ----")
print(rotation([1,2,3,4]))
