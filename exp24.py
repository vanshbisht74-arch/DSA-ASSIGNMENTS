# Experiment 24 :
# BFS Traversal

# Aim :
# Traverse graph level-wise.

# What you will implement :
# BFS using queue.

# Input / Output :
# Input: start node
# Output: BFS order


from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph.get(node, []))


graph = {1: [2, 3], 2: [4], 3: [5], 4: [], 5: []}

bfs(graph, 1)


# Reason :
# BFS explores level by level.


# Viva :
# 1. Why queue?
# FIFO ensures level traversal

# 2. Shortest path?
# Yes (unweighted graph)

# 3. Complexity?
# O(V+E)