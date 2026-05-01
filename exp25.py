# Experiment 25 :
# DFS Traversal

# Aim :
# Traverse graph deeply.

# What you will implement :
# DFS using recursion.

# Input / Output :
# Input: start node
# Output: DFS order


def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for n in graph.get(node, []):
            dfs(graph, n, visited)


dfs(graph, 1, set())


# Reason :
# DFS explores depth first.


# Viva :
# 1. DFS vs BFS?
# DFS = depth, BFS = level

# 2. Recursion issue?
# Stack overflow possible

# 3. Use case?
# Cycle detection, path finding