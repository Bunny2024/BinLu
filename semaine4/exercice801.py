def affiche_table_de_7():
    for i in range(1,11):
        multiplication = i * 7
        print(f"{i} * 7 = {multiplication}")

affiche_table_de_7()

def affiche_table(n):
    for i in range(11,0,-1):
        multiplication = i * n
        print(f"{i} * {n} = {multiplication}")
n = int(input("Entre n: "))
affiche_table(n)

def affiche_table_smart():
    n = int(input("Entre n: "))
    for i in range(11,0,-1):
        multiplication = i * n
        print(f"{i} * {n} = {multiplication}")
affiche_table_smart()