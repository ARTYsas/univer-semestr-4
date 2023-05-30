# Define a class to represent a node in the ordered search tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Define a class to represent the ordered search tree
class OrderedSearchTree:
    def __init__(self):
        self.root = None

    # Method to insert a new key into the tree
    def insert(self, key):
        if self.root is None:
            # If tree is empty, create a new node and set it as the root
            self.root = TreeNode(key)
        else:
            # Call the recursive insert method to find the correct position for insertion
            self._insert_recursive(self.root, key)

    # Recursive helper method for insert
    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                # If left child is None, create a new node and set it as the left child
                node.left = TreeNode(key)
            else:
                # Recursively traverse to the left subtree
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                # If right child is None, create a new node and set it as the right child
                node.right = TreeNode(key)
            else:
                # Recursively traverse to the right subtree
                self._insert_recursive(node.right, key)

    # Method to search for a key in the tree
    def search(self, key):
        return self._search_recursive(self.root, key)

    # Recursive helper method for search
    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            # If node is None or key is found, return the node
            return node
        elif key < node.key:
            # Recursively traverse to the left subtree
            return self._search_recursive(node.left, key)
        else:
            # Recursively traverse to the right subtree
            return self._search_recursive(node.right, key)

    # Method to remove a key from the tree
    def remove(self, key):
        self.root = self._remove_recursive(self.root, key)

    # Recursive helper method for remove
    def _remove_recursive(self, node, key):
        if node is None:
            # Base case: key not found, return None
            return node
        elif key < node.key:
            # Recursively traverse to the left subtree
            node.left = self._remove_recursive(node.left, key)
        elif key > node.key:
            # Recursively traverse to the right subtree
            node.right = self._remove_recursive(node.right, key)
        else:
            # Key found, perform removal
            if node.left is None:
                # If node has no left child, replace it with its right child
                return node.right
            elif node.right is None:
                # If node has no right child, replace it with its left child
                return node.left
            else:
                # If node has both left and right children, find the in-order successor
                successor = self._find_successor(node.right)
                # Replace the key of the current node with the successor key
                node.key = successor.key
                # Remove the successor from the right subtree
                node.right = self._remove_recursive(node.right, successor.key)
        return node

    # Helper method to find the in-order successor of a node
    def _find_successor(self, node):
        while node.left is not None:
            node = node.left
        return node

# Example usage
# Create an instance of the OrderedSearchTree
tree = OrderedSearchTree()

# Insert a list of elements into the tree
elements = [5, 3, 7, 2, 4, 6, 8]
for element in elements:
    tree.insert(element)

# Search for a key in the tree
print("search key: ", end=" ")
search_key = int(input())
result = tree.search(search_key)
if result is not None:
    print(f"Key {search_key} found in the tree.")
else:
    print(f"Key {search_key} not found in the tree.")

# Remove a key from the tree
print("which key you want to remove: ", end=" ")
remove_key = int(input())
tree.remove(remove_key)

# Search for the removed key again
print("Searching for previous removed key...")
result = tree.search(remove_key)
if result is not None:
    print(f"Key {remove_key} found in the tree. Something went wrong 0_0")
else:
    print(f"Key {remove_key} not found in the tree. You removed it!")
