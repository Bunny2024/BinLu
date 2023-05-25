#Trouve le plus petit entier 𝐹𝑛 qui n’est pas nombre premier . 𝐹𝑛 = 2 **(2 ** n) + 1

# from math import sqrt
# def est_premier_1(n):
#     if n == 1:
#         return False
#     for i in range(2, int(sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

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


def trouve_Fn_non_premier():
    n = 0
    while True:
        Fn = 2 ** (2 ** n) + 1
        if not est_premier_1(Fn):
            return Fn
        n += 1

resultat = trouve_Fn_non_premier()
print("Le plus petit entier Fn qui n'est pas nombre premier:", resultat)
