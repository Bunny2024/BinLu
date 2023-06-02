# from unittest import result


# def Gostco(d):
#     result = []
#     todo = []

# return result

# if len(task.keys) == len(result)
    # return result
    # else

task = {'T3':['T1','T2'],'T2':['T1'],'T1':[]}
d = {}

for k, v in task.items():
    print(f"k = {k}, v = {v}")
    for val in v:
        if val in d.keys():
            d[val].append(k)
        else:
            d[val] = []
            d[val].append(k)
        
print(task)
print(d)
 
# construire un nov did
# "T1" : ["T2","T3"]
# "T2" : ["T3"]
