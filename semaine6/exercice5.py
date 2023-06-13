# Question 1
def presence_de_A(sequence):

    for nucleotide in sequence :
        if nucleotide == 'A' :
            return True
    return False

# Test
sequence =  "CTTGCT"
print(sequence," presence de A",presence_de_A(sequence))

# Question 2
def presence_de_AT(sequence):

    for i in range(len(sequence) - 1) :
        if sequence[i] == 'A' and sequence[i+1] == 'T' :
            return i 
    return None

# Test
sequence =  "CTTATGCT"
print(sequence," presence de A est",presence_de_AT(sequence))

# Question 3
def position(code, sequence):
    for i in range(len(sequence)):
        if sequence[i:i+len(code)] == code:
            return i + 1
    return None

code = "CCG"
sequence = "CTCCGTT"
print(position(code, sequence))  

# Question 4
