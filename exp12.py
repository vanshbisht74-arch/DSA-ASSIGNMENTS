# Experiment 12: Stack using SLL + Parentheses Checker

# Viva Q1: Why stack is ideal?
# Answer: Follows LIFO which matches bracket closing.

# Viva Q2: What fails in "([)]"?
# Answer: Order mismatch.

# Viva Q3: Underflow meaning?
# Answer: Pop from empty stack.


def is_valid(s):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0


print(is_valid("()[]{}"))
print(is_valid("([)]"))