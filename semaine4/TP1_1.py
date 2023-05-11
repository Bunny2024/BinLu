# number = int(input("Entre un number: "))

def diviseur(n,d):
    d = 2
    # if n % d == 0:
    while n % d != 0 :
        d = d + 1
    return d

def diviseur(n,d):
    d=2
    while d <=n:
        if n % d != 0:
            d = d + 1
        else : return d
    return d
