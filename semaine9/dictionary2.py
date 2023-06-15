def d_moyenne_neg(d) :

    result = []
    moyenne = None 
    counter = 0
    for  v in d.values():   
        if v < 0 :   # if v % 2 == 0 
            result.append(v)
            counter += 1
    if result:
        summe = sum (result)
        moyenne = summe / counter 
    return moyenne


d = { "a": -1, "b":-10 , "c" : -1 }

result = d_moyenne_neg(d)
print(result)
