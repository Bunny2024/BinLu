# Programme une fonction plus_petit_diviseur(n) qui renvoie, le plus petit diviseur 𝑑 > 2 de 
# l’entier 𝑛 > 2. Par exemple plus_petit_diviseur(91) renvoie 7, car 91 = 7 × 13.

n = int(input("Entrez un nombre : "))

def plus_petit_diviseur(n):
    d = 2
    while n % d != 0:
        d += 1
    return d

resultat = plus_petit_diviseur(n)

print(f"plus_petit_diviseur({n}):{resultat}")

