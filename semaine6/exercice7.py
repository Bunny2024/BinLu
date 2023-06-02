def suppimer_rang(liste,rang):
    n = len(liste)
    new_liste = liste[ : rang] + liste[rang + 1:  ]
    return new_liste
print("suppimer rang")
print(suppimer_rang([8,7,6,5,4],2))