import random 
listOfNumbers = [random.randint(0, 1000) for i in range(1000)]

def bubbleSortFor(array):
    copyOfArray = array[:]
    lengthOfArray = len(copyOfArray)

    for i in range(lengthOfArray - 1):
        for j in range(lengthOfArray - i - 1):
            if copyOfArray[j] > copyOfArray[j+1]:
                copyOfArray[j], copyOfArray[j+1] = copyOfArray[j+1], copyOfArray[j]

    return copyOfArray


def bubbleSortWhile(array):
    copyOfArray = array[:]
    lengthOfArray = len(copyOfArray)

    i = 0
    while i < lengthOfArray - 1:
        j = 0
        while j < lengthOfArray - i - 1:
            if copyOfArray[j] > copyOfArray[j+1]:
                copyOfArray[j], copyOfArray[j+1] = copyOfArray[j+1], copyOfArray[j]
            j += 1
        i += 1

    return copyOfArray

def bubbleSortMaxIndex(array):
    copyOfArray = array[:]
    lengthOfArray = len(copyOfArray)

    while lengthOfArray != 0:
        maxIndex = 0
        i = 1

        while i < lengthOfArray:
            if copyOfArray[i-1] > copyOfArray[i]:
                copyOfArray[i-1], copyOfArray[i] = copyOfArray[i], copyOfArray[i-1]
                maxIndex = i
            i += 1

        lengthOfArray = maxIndex

    return copyOfArray




print(bubbleSortFor(listOfNumbers), '\n')
print(bubbleSortWhile(listOfNumbers), '\n')
print(bubbleSortMaxIndex(listOfNumbers), '\n')