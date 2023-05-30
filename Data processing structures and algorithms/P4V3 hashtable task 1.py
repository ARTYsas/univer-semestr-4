class HashTable:
    def __init__(self):
        self.table = {}

    def add_letter(self, letter):
        if letter in self.table:
            self.table[letter] += 1
        else:
            self.table[letter] = 1

    def search_letter(self, letter):
        if letter in self.table:
            print(f"The letter '{letter}' exists in the hash table.")
        else:
            print(f"The letter '{letter}' does not exist in the hash table.")

    def print_table(self):
        for letter, count in self.table.items():
            print(f"Letter: {letter}, Occurrences: {count}")


# Get the input string from the user
input_string = input("Enter a string: ")

# Create the hash table
hash_table = HashTable()

# Process the input string and populate the hash table
for letter in input_string:
    hash_table.add_letter(letter)

# Print the hash table
print("Hash Table:")
hash_table.print_table()

# Prompt the user to search for a letter
search_letter = input("Enter a letter to search in the hash table: ")

# Search for the entered letter in the hash table
hash_table.search_letter(search_letter)
