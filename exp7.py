# Experiment 7: Arrays 1D (Insert/Delete + Shift Count)

# Viva Q1: Why index access is O(1)?
# Answer: Because arrays use continuous memory and direct indexing.

# Viva Q2: Why insertion at start is O(n)?
# Answer: All elements need to shift right.

# Viva Q3: Static vs Dynamic arrays?
# Answer: Static = fixed size, Dynamic = resizable (like Python list)


def insert(arr, pos, val):
    shifts = len(arr) - pos
    arr.insert(pos, val)
    return arr, shifts

def delete(arr, pos):
    shifts = len(arr) - pos - 1
    arr.pop(pos)
    return arr, shifts


arr = [1, 2, 3, 4]

arr, s = insert(arr, 1, 10)
print("After Insert:", arr, "Shifts:", s)

arr, s = delete(arr, 2)
print("After Delete:", arr, "Shifts:", s)