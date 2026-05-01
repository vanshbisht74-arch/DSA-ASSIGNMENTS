# Experiment 15 :
# Insertion Sort

# Aim :
# Understand performance on nearly sorted data.

# What you will implement :
# Insert elements in correct position one by one.

# Input / Output :
# Input: list
# Output: sorted list


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


print(insertion_sort([5, 2, 4, 6, 1, 3]))


# Reason :
# Works faster when array is nearly sorted (less shifting required).


# Viva :
# 1. Worst-case input?
# Reverse sorted array

# 2. Is insertion stable?
# Yes

# 3. Space complexity?
# O(1)