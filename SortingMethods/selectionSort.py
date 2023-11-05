import random 
listOfNumbers = [random.randint(0, 1000) for i in range(1000)]

def selectionSort(array):
    copyOfArray = array[:]
    lengthOfArray = len(copyOfArray)
    
    for i in range(lengthOfArray - 1):
        minIndex = i
        for j in range(i + 1, lengthOfArray):
            if copyOfArray[minIndex] > copyOfArray[j]:
                minIndex = j
                
        if minIndex != i:
            copyOfArray[i], copyOfArray[minIndex] = copyOfArray[minIndex], copyOfArray[i]
    
    return copyOfArray

print(selectionSort(listOfNumbers))