import time

import sys
sys.setrecursionlimit(10**6)  # Set the recursion limit to a larger value

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] % 2 == 1:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Test sequence 1 - Read from file
with open('sequence1.txt', 'r') as file:
    arr1 = [int(line.strip()) for line in file]

start_time = time.time()
quicksort(arr1, 0, len(arr1) - 1)
end_time = time.time()
execution_time1 = end_time - start_time

# Test sequence 2 - Read from file
with open('sequence2.txt', 'r') as file:
    arr2 = [int(line.strip()) for line in file]

start_time = time.time()
quicksort(arr2, 0, len(arr2) - 1)
end_time = time.time()
execution_time2 = end_time - start_time

# Test sequence 3 - Read from file
with open('sequence3.txt', 'r') as file:
    arr3 = [int(line.strip()) for line in file]

start_time = time.time()
quicksort(arr3, 0, len(arr3) - 1)
end_time = time.time()
execution_time3 = end_time - start_time

print("Quicksort:")
print("Sequence 1 - Sorted array:", arr1)
print("Execution time:", execution_time1, "seconds")
print("Sequence 2 - Sorted array:", arr2)
print("Execution time:", execution_time2, "seconds")
print("Sequence 3 - Sorted array:", arr3)
print("Execution time:", execution_time3, "seconds")
