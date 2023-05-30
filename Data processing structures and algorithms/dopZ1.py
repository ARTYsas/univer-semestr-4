class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Reference to the previous node
        self.next = None  # Reference to the next node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Reference to the first node in the list
        self.tail = None  # Reference to the last node in the list
        self.size = 0     # Number of elements in the list

    def append(self, data):
        """
        Adds a new node with the given data to the end of the list.
        """
        new_node = Node(data)

        if not self.head:
            # If the list is empty, set the new node as both the head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # Append the new node to the end of the list
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def remove_between(self):
        """
        Removes the elements between the index of the minimum and maximum values in the list.
        """
        if not self.head or not self.head.next:
            return

        current = self.head
        min_value = float('inf')
        max_value = float('-inf')

        # Find the minimum and maximum values in the list
        while current:
            min_value = min(min_value, current.data)
            max_value = max(max_value, current.data)
            current = current.next

        current = self.head
        min_index = float('inf')
        max_index = float('-inf')
        index = 0

        # Find the indices of the minimum and maximum values
        while current:
            if current.data == min_value:
                min_index = index
            if current.data == max_value:
                max_index = index
            current = current.next
            index += 1

        # Determine the correct order of min_index and max_index
        if min_index > max_index:
            min_index, max_index = max_index, min_index

        current = self.head
        index = 0

        # Remove the elements between the minimum and maximum indices
        while current:
            if min_index <= index <= max_index:
                next_node = current.next
                self._remove_node(current)
                current = next_node
            else:
                current = current.next

            index += 1

    def _remove_node(self, node):
        """
        Removes the given node from the list.
        """
        # Remove the node by adjusting the prev and next references
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        self.size -= 1

    def print_list(self):
        """
        Prints the elements of the list.
        """
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Modified list:", elements)


# Create a doubly-linked list and add elements
linked_list = DoublyLinkedList()
linked_list.append(5)
linked_list.append(2)
linked_list.append(8)
linked_list.append(3)
linked_list.append(1)
linked_list.append(9)
linked_list.append(4)
linked_list.append(6)
linked_list.append(7)

# Print the initial list
linked_list.print_list()

# Remove elements between the index of the minimum and maximum values
linked_list.remove_between()

# Print the modified list
linked_list.print_list()
