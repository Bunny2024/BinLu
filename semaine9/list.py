def multi (lst,idx_start,idx_end):

    resultat = 1

    if idx_start > idx_end and idx_end > 0 :
        idx_start , idx_end = idx_end , idx_start

    # if idx_start > idx_end and idx_end < 0 :
    #     idx_start , idx_end = idx_end , idx_start*(-1)

    sub_list = lst[idx_start:idx_end + 1]

    for element in sub_list:
        resultat = resultat * element

    return resultat


myList = [7 ,10 ,9 ,5 ]

resultat = multi(myList , -2, -3)

print(resultat)




