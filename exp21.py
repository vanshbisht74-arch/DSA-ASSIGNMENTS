# Experiment 21 :
# BST Delete (All cases)

# Aim :
# Delete node correctly in BST.

# What you will implement :
# Handle leaf, one child, two children cases.

# Input / Output :
# Input: value to delete
# Output: inorder after deletion


def find_min(root):
    while root.left:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete(root.left, key)

    elif key > root.val:
        root.right = delete(root.right, key)

    else:
        # case 1: no child
        if root.left is None and root.right is None:
            return None

        # case 2: one child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # case 3: two children
        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    return root


root = delete(root, 7)

print("After deletion:", end=" ")
inorder(root)


# Reason :
# Replace with inorder successor in case of two children.


# Viva :
# 1. Inorder successor?
# Smallest value in right subtree

# 2. Why delete tricky?
# Multiple cases to handle

# 3. How verify?
# Inorder traversal should remain sorted