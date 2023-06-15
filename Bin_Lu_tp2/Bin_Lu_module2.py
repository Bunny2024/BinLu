def planing(d):

    result =[]  # créer une liste vide，pour stocker l'ordre de final
    d_mirror = {}   # créer un dictionnaire vide
# La clé est la tâche et la valeur est une liste d'autres tâches qui dépendent de cette tâche.
    for k , v in d.items():
        # print(f"k ={k} and v ={v}")
# Itérer sur les paires clé-valeur (tâches et dépendances) dans le dictionnaire d
        for element in v :
# element :value de dépendances 
            if element in d_mirror.keys():
                d_mirror[element] .append(k)
# Si la valeur existe déjà, ajoutez la clé
            else:
                d_mirror[element] = []
                d_mirror[element] .append(k)
# Si la valeur n'existe pas,créer une nouvelle liste ,ajoutez la clé
    # calculer le point de depart : first task to do
    to_do =[]
# Créez une liste vide 'to_do' pour stocker les tâches à exécuter.
    for k , v  in d.items():
        if len(v) == 0:
# Si la liste de dépendances v est vide, ajoutez la tâche k à la liste to_do.
            to_do.append(k)
# ADD :Exemple 3:On suppose qu’il existe qu’une seule tâche de départ.
    if len(to_do) > 1:
        return None

    while len(to_do) > 0:
        start = to_do.pop()
# Affichez la dernière tâche de la liste de tâches comme démarrage initial de la tâche.
        result.append(start)
# Ajoutez start à la liste des résultats, indiquant que la tâche est terminée.
        # print(f"start = {start}")
        # l = d_mirror[start]
        # for element in l :
        #     d[element].remove(start)
        # print(f"d intial devient {d}")
        l = d_mirror.get(start)
# Obtenez la liste des tâches dépendantes l de start dans d_mirror.
        if l != None:
            for element in l:
                d[element].remove(start)
# Supprimez start de la liste de dépendances d[element] de l'élément task.
                if len(d[element]) == 0 :
                    to_do.append(element)
# Si d[element] est vide, ajouter l'élément task à la liste to_do, indiquant qu'il peut être exécuté.
        # for element in l :
        #     d[element].remove(start)
        #     if len(d[element]) == 0 :
        #         to_do.append(element)

        # print(f"d initial devient {d}")
        # print(result)

    return result 

# result = planing(tasks)