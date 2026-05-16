from collections import Counter

def createStrings(word, k):
    if (k == 1):
        return [[char] for char in word]
    
    strings = []
    substrings = createStrings(word, k - 1)

    for char in word:
        for string in substrings:
            newString = string + [char]
            strings.append(newString)
    
    return strings

word = input("Enter the word: ")

n = len(word)

k = int(input("Enter the number of letters: "))

while (k <= 0 or k > n):
    if k <= 0:
        print("The number must be positive.")
    elif k > n:
        print("You cannot use more letters than in the word")
    k = input("Enter the number of letters: ")


# The idea is to recursively create substrings
stringsList = createStrings(word, k)

strings = list()

for list in stringsList:
    strings.append("".join(list))

wordsSet = set()

for answer in strings:
    wordsSet.add(answer)

toRemove = set()

for answer in wordsSet:
    if not Counter(word) >= Counter(answer):
        toRemove.add(answer)

for answer in toRemove:
    wordsSet.remove(answer)

print(str(len(wordsSet)) + " possible combinations.")




