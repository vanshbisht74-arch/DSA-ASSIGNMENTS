# Experiment 20 :
# Binary Search Tree (Insert, Search, Inorder)

# Aim :
# Build BST and verify sorted order using inorder traversal.

# What you will implement :
# Insert nodes, search element, and print inorder traversal.

# Input / Output :
# Input: values to insert + search key
# Output: inorder traversal + search result


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return Node(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def search(root, key):
    if root is None or root.val == key:
        return root

    if key < root.val:
        return search(root.left, key)

    return search(root.right, key)


root = None
for val in [5, 3, 7, 2, 4, 6, 8]:
    root = insert(root, val)

print("Inorder:", end=" ")
inorder(root)

print("\nSearch 4:", "Found" if search(root, 4) else "Not Found")


# Reason :
# In BST, left < root < right → inorder gives sorted output.


# Viva :
# 1. Why inorder gives sorted?
# Because BST follows left < root < right property

# 2. Worst-case height?
# O(n) (skewed tree)

# 3. Average complexity?
# O(log n)