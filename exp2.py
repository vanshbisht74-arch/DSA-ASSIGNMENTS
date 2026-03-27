

# Experiment 2:
    #Complexity Drill (Operation Counting)
# Aim:
    #Develop intuition for time/space complexity using simple loop structures and case analysis.
# What you will implement (in lab):
    #Create 4 snippets: single loop, nested loop, triangular loop, and halving loop. Count operations roughly and map to Big-O. Add best/avg/worst reasoning for linear search and
    #binary search.
# Input / Output expectation:
    #Input: n. Output: for each snippet print estimated operation count + complexity label+ 2-line justification.
# Lab checkpoints (faculty verifies):
    #• Correct mapping for O(1), O(n), O(n2), O(logn)
    #• Clear best/avg/worst definitions with examples
# Viva:
    #1. Big-O vs Big-Theta difference?
    #2. What does worst-case represent?
    #3. Why complexity matters in real systems?

# SOLUION :

# Loop Analysis

# Single Loop
    # Operations proportional to n
    # Time complexity = O(n)

# Nested Loop
    # Operations = n × n
    # Time complexity = O(n²)

# Triangular Loop

    # Operations = n(n+1)/2
    # Time complexity = O(n²)

# Halving Loop

    # Input reduces by half each step
    # Time complexity = O(log n)
    
# Linear Search Complexity

    # Best case → O(1)
    # Average case → O(n)
    # Worst case → O(n)

# Binary Search Complexity

    # Best case → O(1)
    # Average case → O(log n)
    # Worst case → O(log n)
    
def single_loop(n):
    count = 0 
for i in range(n):
    count += 1
print("Single Loop Operations:", count)
print("Complexity: O(n)")
print("Reason: Loop runs n times\n")



# 2. Nested Loop -> O(n^2)
def nested_loop(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    print("Nested Loop Operations:", count)
    print("Complexity: O(n^2)")
    print("Reason: n * n operations\n")



# 3. Triangular Loop -> O(n^2)

def triangular_loop(n):
    count = 0
    for i in range(n):
        for j in range(i + 1):
            count += 1
    print("Triangular Loop Operations:", count)
    print("Complexity: O(n^2)")
    print("Reason: n(n+1)/2 ≈ n^2/2 → O(n^2)\n")



# 4. Halving Loop -> O(log n)

def halving_loop(n):
    count = 0
    while n > 0:
        n = n // 2
        count += 1
    print("Halving Loop Operations:", count)
    print("Complexity: O(log n)")
    print("Reason: Value reduces by half each time\n")



# Linear Search

def linear_search(arr, key):
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == key:
            print("Linear Search Found at index:", i)
            print("Operations:", count)
            return
    print("Linear Search Not Found")
    print("Operations:", count)



# Binary Search

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high:
        count += 1
        mid = (low + high) // 2

        if arr[mid] == key:
            print("Binary Search Found at index:", mid)
            print("Operations:", count)
            return
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    print("Binary Search Not Found")
    print("Operations:", count)



# Main Execution

n = int(input("Enter value of n: "))
print(f"--- Complexity Snippets ---")

single_loop(n)
nested_loop(n)
triangular_loop(n)
halving_loop(n)

print(f"--- Search Comparisons ---")

arr = list(range(1, n+1))  # Sorted array

key = int(input("Enter key to search: "))

print(f"Linear Search:")
linear_search(arr, key)

print(f"Binary Search:")
binary_search(arr, key) 
