# Question a 
def transforme_en_verlan(mot):

    verlan = ""
    for carac in mot :
        verlan = carac + verlan
    
    return verlan

mot = "BONJOUR"
verlan = transforme_en_verlan(mot)
print("Le mot",mot,"devient",verlan,"!")

# Question b
def est_un_palindrome(mot):

    verlan = transforme_en_verlan(mot)
    if mot == verlan:
        return True
    else:
        return False
    
    # return mot == transforme_en_verlan(mot)

mot = "kayak"
print("Le mot",mot,"est un palindrome :",est_un_palindrome(mot),"!")