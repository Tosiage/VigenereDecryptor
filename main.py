coincidenceList = []
approxKeyLength = 0

def compare(a, b):
    coincidences = 0
    for x, y in zip(a, b):
        if x == y:
            coincidences = coincidences + 1
    return coincidences


def findCoincidences(filePath):
    file = open(filePath, 'r')
    cipher = file.read()
    file.close()
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


    print(coincidenceList)



findCoincidences('testCipher.txt')
approxKeyLength = coincidenceList.index(max(coincidenceList)) + 1
print(approxKeyLength)