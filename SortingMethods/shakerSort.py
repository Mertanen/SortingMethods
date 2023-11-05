import random 
listOfNumbers = [random.randint(0, 1000) for i in range(1000)]

def shakerSort(array):
    copyOfArray = array[:]
    swapped = True
    start = 0
    end = len(copyOfArray) - 1
    
    while swapped == True:
        swapped = False
        
        for i in range(start, end):
            if copyOfArray[i] > copyOfArray[i+1]:
                copyOfArray[i], copyOfArray[i+1] = copyOfArray[i+1], copyOfArray[i]
                swapped = True    
                
        if not swapped:
            break
        
        swapped = False
        end -= 1
        
        for i in range(end - 1, start - 1, -1):
            if copyOfArray[i] > copyOfArray[i+1]:
                copyOfArray[i], copyOfArray[i+1] = copyOfArray[i+1], copyOfArray[i]
                swapped = True
        
        start += 1
    
    return copyOfArray

print(shakerSort(listOfNumbers))