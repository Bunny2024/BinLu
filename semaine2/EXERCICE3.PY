# Lit une lettre de l'alphabet de l'utilisateur. 
# Si l'utilisateur saisit a, e, i, o ou u, votre programme doit afficher un message：
# indiquant que la lettre saisie est une voyelle. 
# Si l'utilisateur saisit y, votre programme doit afficher un message ：
# indiquant que y est parfois une voyelle et parfois une consonne. 
# Sinon, votre programme doit afficher un message indiquant que la lettre est une consonne.

# donne un alphabet
alphabet = str(input("Entrez un un alphabet: "))

if alphabet in ['a', 'e', 'i', 'o', 'u'] :
    print(alphabet, "est une voyelle.")

elif alphabet == 'y':
    print(alphabet, "est parfois une voyelle et parfois une consonne.")

else:
    print(alphabet, "est une consonne.")