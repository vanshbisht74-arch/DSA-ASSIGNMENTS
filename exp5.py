
# Experiment 5:
    #Tower of Hanoi (N=3 Trace + Complexity)
# Aim :
    #Use recursion to generate step-by-step solution and observe exponential growth.
# What you will implement (in lab) :
    #Implement Hanoi(n, src, aux, dst) and print exact move sequence for n=3. Show move
    #count for n=4 and infer complexity.
# Input / Output expectation :
    #Input: n. Output: move sequence for n=3 + move count for n=4 + complexity statement.
# Lab checkpoints (faculty verifies) :
    #• Correct move order for n=3
    #• Complexity stated: O(2n)
# Viva :
    # 1. Why moves are 2n-1?
    # 2. What is recursion tree idea?
    # 3. Practical risk of exponential algorithms?
    
# SOLUTION :
def hanoi(n, source, aux, dest):
    if n == 1:
        print(f"Move disk 1 from {source} to {dest}")
        return
    hanoi(n-1, source, dest, aux)
    print(f"Move disk {n} from {source} to {dest}")
    hanoi(n-1, aux, source, dest)

hanoi(3, 'A', 'B', 'C')

# Number of Moves :
    # 2ⁿ − 1
    # For n = 3 → 7 moves

# Complexity :
    # Time complexity = O(2ⁿ)
