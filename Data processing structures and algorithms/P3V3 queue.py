class CharacterQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def remove_odd_elements(self):
        self.queue = [element for index, element in enumerate(self.queue) if index % 2 == 0]


# Get the input from the user
queue_input = input("Enter the characters in the queue (in line without spaces): ")

# Create the CharacterQueue instance
char_queue = CharacterQueue()

# Enqueue each character from the input
[char_queue.enqueue(char) for char in queue_input]

# Remove odd elements from the queue
char_queue.remove_odd_elements()

# Print the updated queue
print("Updated queue:", "".join(char_queue.queue))

