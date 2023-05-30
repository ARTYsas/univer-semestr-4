import random

def linear_search(arr, key):
    matches = []
    for i in range(len(arr)):
        if arr[i] == key:
            matches.append(i)
    return matches

# Step 1: Ask the user for the size of the array and the search key
size = int(input("Enter the size of the array (it will randomly generatd with numbers from 1 to 100): "))
key = int(input("Enter the search key: "))

# Step 2: Generate an array of random numbers
arr = [random.randint(1, 100) for _ in range(size)]
print("Generated Array:", arr)

# Step 3: Perform linear search and return the number of matches and their positions
matches = linear_search(arr, key)
num_matches = len(matches)

# Print the results
print("Number of Matches:", num_matches)
print("Positions of Matches:", matches)
