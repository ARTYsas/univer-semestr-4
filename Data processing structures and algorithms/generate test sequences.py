import random

# Generate a list of 10,000 random integers
sequence = [random.randint(1, 10000) for _ in range(10000)]

# Save the sequence to a file change name of file to sequence1.txt or sequence2.txt or sequence3.txt
with open('sequence3.txt', 'w') as file:
    for number in sequence:
        file.write(str(number) + '\n')
