# Experiment 8: 2D Array Operations

# Viva Q1: Complexity of scanning a matrix?
# Answer: O(n*m) because we visit every element.

# Viva Q2: Real-world use of 2D arrays?
# Answer: Images, spreadsheets, game boards.

# Viva Q3: Memory layout?
# Answer: Row-wise (row-major order).


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Row Sum
print("Row sums:")
for row in matrix:
    print(sum(row))

# Column Sum
print("Column sums:")
for col in range(len(matrix[0])):
    s = 0
    for row in range(len(matrix)):
        s += matrix[row][col]
    print(s)

# Search
target = 5
found = False
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == target:
            found = True

print("Found:", found)

# Transpose
transpose = []
for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    transpose.append(row)

print("Transpose:", transpose)