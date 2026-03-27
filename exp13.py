# Experiment 13: Queue using Linked List

# Viva Q1: BFS uses queue?
# Answer: It processes nodes level by level.

# Viva Q2: FIFO meaning?
# Answer: First In First Out.

# Viva Q3: Scheduling example?
# Answer: CPU task scheduling.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, val):
        new = Node(val)
        if not self.rear:
            self.front = self.rear = new
            return
        self.rear.next = new
        self.rear = new

    def dequeue(self):
        if not self.front:
            return "Underflow"
        temp = self.front
        self.front = self.front.next

        if not self.front:
            self.rear = None

        return temp.data


q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())