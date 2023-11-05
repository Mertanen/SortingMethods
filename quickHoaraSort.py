import random 
import sys

listOfNumbers = [random.randint(0, 1000) for i in range(1000)]

def quickHoaraSort(array, left, right):
    if left >= right:
        return 
    else:
        pivot = array[(left + right) // 2]
        i = left
        j = right
        while i <= j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i <= j: 
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1 
                quickHoaraSort(array, left, j)
                quickHoaraSort(array, i, right)

quickHoaraSort(listOfNumbers, 0, len(listOfNumbers) - 1) 

print(listOfNumbers)