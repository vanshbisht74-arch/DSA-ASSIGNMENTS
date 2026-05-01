# Experiment 16 :
# Merge Sort

# Aim :
# Learn divide and conquer approach.

# What you will implement :
# Split array and merge sorted halves.

# Input / Output :
# Input: list
# Output: sorted list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


print(merge_sort([5, 2, 9, 1, 5, 6]))


# Reason :
# Divides problem into smaller parts → efficient O(n log n).


# Viva :
# 1. Why stable?
# Because equal elements maintain order

# 2. Why extra memory?
# Uses extra array during merging

# 3. Use case?
# External sorting (large data)