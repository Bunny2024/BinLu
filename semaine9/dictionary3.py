def planing(d):
    result =[]
    d_mirror = {}


    for k , v in d.items():
        print(f"k ={k} and v ={v}")
        for element in v :
            if element in d_mirror.keys():
                d_mirror[element] .append(k)
            else:
                d_mirror[element] = []
                d_mirror[element] .append(k)
    # calculer le point de depart : first task to do
    to_do =[]
    for k , v  in d.items():
        if len(v) == 0:
            to_do.append(k)

    while len(to_do) > 0:
        start = to_do.pop()
        result.append(start)

        # print(f"start = {start}")
        # l = d_mirror[start]
        # for element in l :
        #     d[element].remove(start)
        # print(f"d intial devient {d}")
        l = d_mirror.get(start)
        if l != None:
            for element in l:
                d[element].remove(start)
                if len(d[element]) == 0 :
                    to_do.append(element)
        # for element in l :
        #     d[element].remove(start)
        #     if len(d[element]) == 0 :
        #         to_do.append(element)

        print(f"d initial devient {d}")
        print(result)

    return result 

tasks = {"T5":["T3","T4"],"T4":["T1","T2"],"T3":["T4"],"T1":["T2"],"T2":[]}

result = planing(tasks)