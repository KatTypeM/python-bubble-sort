
# Python Algorithm

# Bubble sort of list


import random
# random.shuffle(myArray) # changes the array itself
# randomized = random.sample(myArray, len(myArray)) # creates a new list and returns it


myArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]


myArrayRandomized = random.sample(myArray, len(myArray))
myArrayRandomized2 = random.sample(myArray, len(myArray))
print("Unsorted arrays")
print(myArray)
print(myArrayRandomized)
print(myArrayRandomized2)


def bubbleSort(arrayInput):
    n = len(arrayInput)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1 ):
            if arrayInput[j] > arrayInput[j + 1]:
                temp = arrayInput[j]
                arrayInput[j] = arrayInput[j+1]
                arrayInput[j+1] = temp
                # large expression sets two conditions on each side of equal sign. same as above without the temp step
                # arrayInput[j], arrayInput[j + 1] = arrayInput[j + 1], arrayInput[j]
                swapped = True
        if(swapped == False):
            break
    output = arrayInput
    return output

print("Sorted arrrays")
print(bubbleSort(myArrayRandomized))
print(bubbleSort(myArrayRandomized2))






