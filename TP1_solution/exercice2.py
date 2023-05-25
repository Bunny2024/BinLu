# écrire une première fonction est_premier_1(n) qui renvoie « vrai » (True) 
# si n est un nombre premier et « faux » (False) sinon. 
# Par exemple est_premier_1(13) renvoie True, est_premier_1(14) renvoie False

n = int(input("Entrez un nombre : "))

def est_premier_1(n):
    if n < 2:
        return False
    if n == 2:
        return True
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

resultat = est_premier_1(n)

print(f"{n}est un nombre premier:{resultat}")