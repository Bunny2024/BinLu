from re import S


def charaterCounts(s):
    counts = {}
    for ch in s:
        if ch in counts.keys():
            counts[ch] = counts[ch] + 1
        else:
            counts[ch] = 1

    return counts

mot1 = input("Enter the first String: ")
mot2 = input("Enter the second String: ")

counts1 = charaterCounts(mot1)
counts2 = charaterCounts(mot2)

if counts1 == counts2:
    print(f"\"{mot1}\" and \"{mot2}\" are anagrams.")
else:
    print(f"\"{mot1}\" and \"{mot2}\" are not anagrams.")
