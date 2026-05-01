# Experiment 17 :
# Quick Sort

# Aim :
# Understand partition and pivot impact.

# What you will implement :
# Partition array and sort recursively.

# Input / Output :
# Input: list
# Output: sorted list


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
        


arr = [5, 2, 9, 1, 5, 6]
quick_sort(arr, 0, len(arr) - 1)
print(arr)


# Reason :
# Efficient sorting using partition → average O(n log n)


# Viva :
# 1. Worst-case?
# Already sorted + bad pivot → O(n^2)

# 2. Stable?
# No

# 3. Average time?
# O(n log n)