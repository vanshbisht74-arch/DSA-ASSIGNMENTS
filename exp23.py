# Experiment 23 :
# Graph Representation (Adjacency List)

# Aim :
# Represent graph using adjacency list.

# What you will implement :
# Store nodes and edges.

# Input / Output :
# Input: edges
# Output: adjacency list


graph = {}

edges = [(1, 2), (1, 3), (2, 4), (3, 5)]

for u, v in edges:
    if u not in graph:
        graph[u] = []
    graph[u].append(v)

print(graph)


# Reason :
# Adjacency list is space efficient.


# Viva :
# 1. List vs matrix?
# List uses less space

# 2. Directed vs undirected?
# Directed has one-way edges

# 3. Weighted graph?
# Stores weight with edge