class HashTable:
    def __init__(self):
        self.table = {}

    def add_number(self, number):
        if number in self.table:
            self.table[number] += 1
        else:
            self.table[number] = 1

    def search_number(self, number):
        if number in self.table:
            print(f"The number {number} exists in the hash table.")
        else:
            print(f"The number {number} does not exist in the hash table.")

    def print_table(self):
        for number, count in self.table.items():
            print(f"Number: {number}, Occurrences: {count}")


# Read the integers from the text file
file_name = input("Enter the file name (with .txt): ")
numbers = []

try:
    with open(file_name, 'r') as file:
        # Read each line from the file and convert it to an integer
        numbers = [int(line.strip()) for line in file]
except FileNotFoundError:
    print("File not found.")

# Create the hash table
hash_table = HashTable()

# Process the numbers and populate the hash table
for number in numbers:
    hash_table.add_number(number)

# Print the hash table
print("Hash Table:")
hash_table.print_table()

# Prompt the user to search for a number
search_number = int(input("Enter a number to search in the hash table: "))

# Search for the entered number in the hash table
hash_table.search_number(search_number)
