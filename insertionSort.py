import random 
listOfNumbers = [random.randint(0, 1000) for i in range(1000)]

def insertionSort(array):
    lengthOfArray = len(array)

    for i in range(lengthOfArray):
        sorted = i - 1

        while sorted > -1 and array[sorted] > array[sorted+1]:
            array[sorted], array[sorted+1] = array[sorted+1], array[sorted]
            sorted -= 1

insertionSort(listOfNumbers)
print(listOfNumbers)