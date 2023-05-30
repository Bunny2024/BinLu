def reverseLookup(data,value_to_check):
    # construct a list of the key that map to value
    keys = []

    for key, value in data.items():
        if value == value_to_check : 
            keys.append(key)
    return keys

frEn = {
    "le": "the",
    "la": "the",
    "livre": "book",
    "pomme": "apple"
}

print(f"The french words'the'are {reverseLookup(frEn,'the')}")
# The french words'the'are["le","la"].

print(f"The french words'apple'are {reverseLookup(frEn,'apple')}")
# The french words'apple'are ["pomme"]

print(f"The french words'apple'are {reverseLookup(frEn,'pomme')}")
# The french words'apple'are []