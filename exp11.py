# Experiment 11: Doubly Linked List

# Viva Q1: DLL advantage over SLL?
# Answer: Allows backward traversal.

# Viva Q2: Browser history mapping?
# Answer: Back and forward navigation.

# Viva Q3: Deletion ease in DLL?
# Answer: No need to track previous node.


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None