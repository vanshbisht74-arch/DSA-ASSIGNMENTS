
# Experiment 3:
    #Recursive Factorial + Call Stack Trace
# Aim :
    #Learn recursion basics: base case, recursive case, and stack growth.
# What you will implement (in lab):
    #Implement factorial(n) recursively for n≥0 and reject invalid input. Draw call stack for
    #factorial(4) showing return values.
# Input / Output expectation :
    #Input: n. Output: factorial(n) + manual call stack trace (in notebook) + time/space
    #complexity statement.
# Lab checkpoints (faculty verifies) :
    #• Base case correct, recursion correct
    #• Complexity stated correctly: time O(n), space O(n)
# Viva :
    #1. What is recursion depth?
    #2. Why recursion uses stack memory?
    #3. When iteration is better than recursion?

# SOLUTION :

# Mathematical Definition :
#   n! = n × (n−1)!
#   0! = 1
def fact(n):
    if n<0:
        return "Invalid Input"
    elif n == 0 or n == 1 :
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))

# fact(4) 
# = 4 × fact(3) -->here, we breakdown into it's constituents as n * factorial of n-1 
# = 4 × 3 × fact(2) --> here, fact of 3 is again broke down into it's constituent steps as n as 3 and then fact of n-1 being factorial of 2
# = 4 × 3 × 2 × fact(1) --> here our base case comes into play and provides that end point from where we'll get some value as fact of 1
# = 24 --> this is the final value and in recursive approach it follows the same structure while unfolding and folding of code


# Complexity

# Time complexity = O(n)
# Space complexity = O(n)
