
# Aim
# Implement binary search recursively and explain why it is O(log n).
# What you will implement (in lab)
# Implement binarySearch(arr, key, low, high) returning index or -1. Explain recurrence
# intuition: T(n)=T(n/2)+O(1).
# Input / Output expectation
# Input: sorted list + key. Output: index or -1, including empty list and missing key cases.
# Lab checkpoints (faculty verifies)
# • Correct mid logic and termination
# • Handles empty list and not-found properly
# Viva (answer any 3)
# 1. Why sorted data is required?
# 2. Best/avg/worst case?
# 3. Divide & Conquer meaning?

# SOLUTION : 
def bin_search( arr , low , high , key ):
    if low > high:
        return -1 
    mid = (low + high)//2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return bin_search( arr , low , high , mid -1 )
    else :
        return bin_search( arr , key , mid + 1 , high)
    
arr = [ 1 , 5 , 6 , 8 , 3 , 7 , 9 ]
print(bin_search(arr, 7, 0, len(arr)-1))

# Recurrence Relation :
    # T(n) = T(n/2) + O(1)

# Complexity :
    # Time complexity = O(log n) Space complexity = O(log n)

