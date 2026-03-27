
# Experiment 4 :
    #   Fibonacci (Naive vs Memoized) + Call Counter
# Aim :
    #   Understand inefficiency of naive recursion and benefit of memoization.
# What you will implement (in lab) :
    #   Implement fib naive(n) and fib memo(n) with call counters. Compare call counts for
    #n=10,20,30 to show performance difference clearly.
# Input / Output expectation :
    #Input: n values. Output: fib(n) + calls naive + calls memo + short explanation (3–4
    #lines).
# Lab checkpoints (faculty verifies) :
    #• Memoized version drastically reduces calls
    #• Student can explain repeated subproblems
# Viva :
    #1. Why naive Fibonacci is slow?
    #2. Memoization relates to DP ?
    #3. Space impact of memoization?

def naive_fib(n):
    if n<= 1:
        return n
    else : 
        return naive_fib(n-1) + naive_fib(n-2)
    
# Time complexity = O(2ⁿ)

memo = {}
def fib_memo(num):
    if num in memo:
        return memo[num]
    if num <= 1:
        return num
    memo[num] = fib_memo(num-1) + fib_memo(num-2)
    return memo[num]

    # Time complexity = O(n) Space complexity = O(n)
    
# Reason for Improvement :
    # Memoization stores previously computed results and avoids repeated calculations.
