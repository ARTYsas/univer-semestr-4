import time

def direct_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] % 2 == 1:
            min_idx = i
            for j in range(i+1, n):
                if arr[j] % 2 == 1 and arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Test sequence 1 - Read from file
with open('sequence1.txt', 'r') as file:
    arr1 = [int(line.strip()) for line in file]

start_time = time.time()
sorted_arr1 = direct_selection_sort(arr1)
end_time = time.time()
execution_time1 = end_time - start_time

# Test sequence 2 - Read from file
with open('sequence2.txt', 'r') as file:
    arr2 = [int(line.strip()) for line in file]

start_time = time.time()
sorted_arr2 = direct_selection_sort(arr2)
end_time = time.time()
execution_time2 = end_time - start_time

# Test sequence 3 - Read from file
with open('sequence3.txt', 'r') as file:
    arr3 = [int(line.strip()) for line in file]

start_time = time.time()
sorted_arr3 = direct_selection_sort(arr3)
end_time = time.time()
execution_time3 = end_time - start_time

print("Direct Selection Sort:")
print("Sequence 1 - Sorted array:", sorted_arr1)
print("Execution time:", execution_time1, "seconds")
print("Sequence 2 - Sorted array:", sorted_arr2)
print("Execution time:", execution_time2, "seconds")
print("Sequence 3 - Sorted array:", sorted_arr3)
print("Execution time:", execution_time3, "seconds")
