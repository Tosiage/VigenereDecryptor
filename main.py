coincidenceList = []
approxKeyLength = 0
key = []
letterFrequencyEnglish = {
    'A': 8.12,
    'B': 1.49,
    'C': 2.71,
    'D': 4.32,
    'E': 12.02,
    'F': 2.30,
    'G': 2.03,
    'H': 5.92,
    'I': 7.31,
    'J': 0.10,
    'K': 0.69,
    'L': 3.98,
    'M': 2.61,
    'N': 6.95,
    'O': 7.68,
    'P': 1.82,
    'Q': 0.11,
    'R': 6.02,
    'S': 6.28,
    'T': 9.10,
    'U': 2.88,
    'V': 1.11,
    'W': 2.09,
    'X': 0.17,
    'Y': 2.11,
    'Z': 0.07
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
        #print(i,f)
        c1 = ci[:i]
        c2 = ci[f:]
        #print(c1)
        #print(c2)
        #print(compare(c1, c2))
        coincidenceList.append(compare(c1, c2))
        i = i - 1

    #print(coincidenceList)


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
    #print(letterCount)
    letterFrequency = {}
    for k in letterCount:
        letterFrequency[k] = letterCount[k]/len(cipher)
   # print(letterFrequency)
    return letterFrequency




################################################################


file = open('testCipher.txt', 'r')
cipherText = file.read()
file.close()
findCoincidences(cipherText)
approxKeyLength = coincidenceList.index(max(coincidenceList)) + 1
#print(approxKeyLength)
letterFrequency = findLetterFrequency(approxKeyLength, cipherText)
print(letterFrequency)

