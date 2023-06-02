# Dictionnaire des points Scrabble par lettre 

points_scrabble = {     
'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, \
'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,\
'D': 2, 'G': 2,\
'B': 3, 'C': 3, 'M': 3, 'P': 3,\
'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,\
'K': 5,\
'J': 8, 'X': 8,\
'Q': 10, 'Z': 10 } 

    ## read a word from a user
# mot = input("Enter a word: ") )
    ## Compute the score for this word
# upperCase = mot.upper()
# score = 0
# for ch in upperCase:
#     score = score + points_scrabble[ch]

mot = input("Enter a word: ")
mot = mot.upper()
def calculer_score_scrabble(mot):
    score = 0
    for lettre in mot:
        score += points_scrabble.get(lettre)  

    return score 
score = calculer_score_scrabble(mot) 

print( f"\"{mot}\" has the score = {score} .")