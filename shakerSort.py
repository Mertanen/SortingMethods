import random 
listOfNumbers = [random.randint(0, 1000) for i in range(1000)]

def shakerSort(array):
    swapped = True
    start = 0
    end = len(array) - 1

    while swapped == True:
        swapped = False

        for i in range(start, end):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True    

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True

        start += 1


shakerSort(listOfNumbers)
print(listOfNumbers)