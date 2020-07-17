coincidenceList = []
approxKeyLength = 0
key = []
letterFrequencyEnglish = {
    'A': 8.12/100,
    'B': 1.49/100,
    'C': 2.71/100,
    'D': 4.32/100,
    'E': 12.02/100,
    'F': 2.30/100,
    'G': 2.03/100,
    'H': 5.92/100,
    'I': 7.31/100,
    'J': 0.10/100,
    'K': 0.69/100,
    'L': 3.98/100,
    'M': 2.61/100,
    'N': 6.95/100,
    'O': 7.68/100,
    'P': 1.82/100,
    'Q': 0.11/100,
    'R': 6.02/100,
    'S': 6.28/100,
    'T': 9.10/100,
    'U': 2.88/100,
    'V': 1.11/100,
    'W': 2.09/100,
    'X': 0.17/100,
    'Y': 2.11/100,
    'Z': 0.07/100
}


def compare(a, b):
    coincidences = 0
    for x, y in zip(a, b):
        if x == y:
            coincidences = coincidences + 1
    return coincidences


def findCoincidences(cipher):
    clength = len(cipher)
    ci = cipher
    i = clength - 1
    while i > 0:
        f = clength - i
        c1 = ci[:i]
        c2 = ci[f:]
        coincidenceList.append(compare(c1, c2))
        i = i - 1


def countLetters(string):
    dict = {}
    for letter in string:
        if letter in dict:
            dict[letter] = dict[letter] + 1
        else:
            dict[letter] = 1
    return dict


def rotList(list):
    list.append(list[0])
    list.pop(0)


def findLetterFrequency(keyLength, cipher):
    #print(cipher[0::keyLength])
    letterCount = countLetters(cipher[0::keyLength])
    print(letterCount)
    totalCountedLetters = 0
    for key in letterCount:
        totalCountedLetters = totalCountedLetters + letterCount[key]
    print(totalCountedLetters)
    letterFrequency = {}
    for k in letterCount:
        letterFrequency[k] = letterCount[k]/totalCountedLetters
    return letterFrequency


################################################################


file = open('testCipher.txt', 'r')
cipherText = file.read()
file.close()
findCoincidences(cipherText)
approxKeyLength = coincidenceList.index(max(coincidenceList)) + 1
print(approxKeyLength)
letterFrequency = findLetterFrequency(approxKeyLength, cipherText)
print(letterFrequency)

