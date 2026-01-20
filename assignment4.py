# Name: Igiebor Oluwafemi Emmanuel
# Course: Data Structure
# cousre : CSC 301
# Matric Number: 230502027
# Level: 300L

# Define a Node class for the binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to perform in-order traversal (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Function to perform pre-order traversal (Root, Left, Right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Function to perform post-order traversal (Left, Right, Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# Function to calculate the height of the tree
def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1

# Example usage
if __name__ == "__main__":
    # Creating the binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("In-order traversal:")
    inorder(root)
    print("\nPre-order traversal:")
    preorder(root)
    print("\nPost-order traversal:")
    postorder(root)
    print("\nHeight of the tree:", height(root))
