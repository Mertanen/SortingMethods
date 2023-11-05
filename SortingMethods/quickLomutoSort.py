import random 
listOfNumbers = [random.randint(0, 1000) for i in range(1000)]

def quickLomutoSort(array, start, end):
    left = start
    current = left 
    if start >= end: return
    
    while current < end:
        if array[current] <= array[end]:
            array[left], array[current] = array[current], array[left]
            left += 1
        current += 1
    
    array[left], array[end] = array[end], array[left]
    
    quickLomutoSort(array, start, left - 1)
    quickLomutoSort(array, left + 1, end)
    
quickLomutoSort(listOfNumbers, 0, len(listOfNumbers) - 1)
print(listOfNumbers)