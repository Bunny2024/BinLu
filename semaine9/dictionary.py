
# def d_keys(d, value) :

#     result = []
#     for k , v in d.items():
#         if v == value :
#             result.append(k)
#     return result 
# d = { "a": -1, "b":- 8 , "c" : 1 ,"d" :10 , "e" :-1 }


# result = d_keys(d, -1)
# print(result)

def d_moyenne_neg(d) :

    result = []
   # b2 moyenne = None 
   # a1 for k , v in d.items():
    for  v in d.values():    #a2
        if v < 0 :
            result.append(v)
    if result:
        summe = sum (result)
        moyenne = summe / len (result)
        return moyenne
    else:     # b1
        return None

d = { "a": -1, "b":-10 , "c" : -1 }

result = d_moyenne_neg(d)
print(result)
