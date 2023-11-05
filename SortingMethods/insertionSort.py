import random 
listOfNumbers = [random.randint(0, 1000) for i in range(1000)]

def insertionSort(array):
    copyOfArray = array[:]
    lengthOfArray = len(copyOfArray)

    for i in range(lengthOfArray):
        sorted = i - 1
        
        while sorted > -1 and copyOfArray[sorted] > copyOfArray[sorted+1]:
            copyOfArray[sorted], copyOfArray[sorted+1] = copyOfArray[sorted+1], copyOfArray[sorted]
            sorted -= 1
            
    return copyOfArray
            
print(insertionSort(listOfNumbers))