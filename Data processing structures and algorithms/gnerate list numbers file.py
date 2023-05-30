import random

# Generate a list of random numbers
numbers = [random.randint(1, 100) for _ in range(10)]

# Write the numbers to a file
file_name = "numbers.txt"

with open(file_name, 'w') as file:
    for number in numbers:
        file.write(str(number) + '\n')

print(f"File '{file_name}' has been generated with random numbers.")
