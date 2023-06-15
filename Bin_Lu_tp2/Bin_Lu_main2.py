from Bin_Lu_module2  import planing 

# Exemple1
tasks = {"T3":["T1","T2"],"T2":["T1"],"T1":[]}
result = planing(tasks)

print(f"Exemple 1 :",(result))

# Exemple2
tasks = {"T3":["T2"],"T2":["T3","T1"],"T1":[]}
result = planing(tasks)
if len(result) < len(tasks):
    result = None

print(f"Exemple 2 :",(result))

# Exemple3
tasks = {"T3":["T2"],"T2":["T1"],"T1":[],"T0":[]}
result = planing(tasks)

print(f"Exemple 3 :",(result))

# Exemple4
tasks = {"T4":["T3"],"T3":["T2","T1"],"T2":["T1"],"T1":[]}
result = planing(tasks)

print(f"Exemple 4 :",(result))