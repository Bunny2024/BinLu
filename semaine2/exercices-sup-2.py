# Créez un programme qui calcule le coût total d'une commande, y compris les frais d'expédition.

print("=" * 50 + "\nCalculateur d'expédition\n" + "=" * 50)

# donne un cout:
cout = float(input("Coût des articles commandes: "))

if cout <= 0:
    print("Vous devez entre un nombre positif.")
elif cout <30:
    frais = 5.95
    cout = cout + frais
    print(f"Frais d'expédition:\t{frais}")
    print(f"Coût total :\t\t{cout}")
elif cout <50 and cout >=30:
    frais = 7.95
    cout = cout + frais
    print(f"Frais d'expédition:\t{frais}")
    print(f"Coût total :\t\t{cout}")
elif cout <75 and cout >=50:
    frais = 7.95
    cout = cout + frais
    print(f"Frais d'expédition:\t{frais}")
    print(f"Coût total :\t\t{cout}")
elif cout >=75:
    frais = 0
    cout == cout + frais
    print(f"Frais d'expédition:\t{frais}")
    print(f"Coût total :\t\t{cout}")


print("=" * 50 + "\nBye!" )