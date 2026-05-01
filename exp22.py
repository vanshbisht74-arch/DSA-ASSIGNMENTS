# Experiment 22 :
# Priority Queue using Heap

# Aim :
# Implement priority queue operations.

# What you will implement :
# Insert, peek, extract-min.

# Input / Output :
# Input: elements
# Output: extracted order


import heapq

heap = []

# insert
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

# peek
print("Top:", heap[0])

# extract
while heap:
    print(heapq.heappop(heap), end=" ")


# Reason :
# Heap ensures smallest element always on top.


# Viva :
# 1. Why heap?
# Efficient insert + extract O(log n)

# 2. Complexity?
# Insert/extract = O(log n)

# 3. Use case?
# Scheduling, Dijkstra