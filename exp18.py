# Experiment 18 :
# Heap Sort

# Aim :
# Use heap to sort elements.

# What you will implement :
# Build heap and extract max.

# Input / Output :
# Input: list
# Output: sorted list


def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


print(heap_sort([5, 2, 9, 1, 5, 6]))


# Reason :
# Uses heap structure to sort efficiently.


# Viva :
# 1. Why not stable?
# Swapping changes order of equal elements

# 2. Time complexity?
# O(n log n)

# 3. Use case?
# Priority queue