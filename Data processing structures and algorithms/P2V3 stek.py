class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def transform_stack(stack):
    temp_stack = Stack()

    while not stack.is_empty():
        item = stack.pop()

        if item > 0:
            temp_stack.push(1)
        elif item < 0:
            temp_stack.push(-1)
        else:
            temp_stack.push(item)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack


# Create a stack and populate it with numbers
stack = Stack()
numbers = [4, -7, 2, 0, -9, 5, -3, 8, -6, 1]
for num in numbers:
    stack.push(num)

# Transform the stack
transformed_stack = transform_stack(stack)

# Print the transformed stack
while not transformed_stack.is_empty():
    print(transformed_stack.pop(), end=' ')
