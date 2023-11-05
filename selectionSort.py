import random 
listOfNumbers = [random.randint(0, 1000) for i in range(1000)]

def selectionSort(array):
    lengthOfArray = len(array)

    for i in range(lengthOfArray - 1):
        minIndex = i
        for j in range(i + 1, lengthOfArray):
            if array[minIndex] > array[j]:
                minIndex = j

        if minIndex != i:
            array[i], array[minIndex] = array[minIndex], array[i]

selectionSort(listOfNumbers)
print(listOfNumbers)