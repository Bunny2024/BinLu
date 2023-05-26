# une liste de canidats,mettez le premier candidat à la 
# dernière place et vice versa.

myList=["Vézina"," Albert"," George"," Amos"]
print(myList)

# def reverse_canidate(myList):
#     temp = myList[-1]
#     myList[-1] = myList[0]
#     myList[0] = temp

def reverse_canidate(myList):
    myList[0], myList[-1] = myList[-1] , myList[0]

reverse_canidate(myList)
print(myList)