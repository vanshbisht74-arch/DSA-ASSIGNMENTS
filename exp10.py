# Experiment 10: Singly Linked List

# Viva Q1: Why search is O(n)?
# Answer: We traverse node by node.

# Viva Q2: Why insert-at-head is O(1)?
# Answer: No traversal required.

# Viva Q3: Node structure?
# Answer: Contains data + next pointer.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_begin(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new

    def insert_end(self, val):
        new = Node(val)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete(self, val):
        temp = self.head

        if temp and temp.data == val:
            self.head = temp.next
            return

        while temp.next:
            if temp.next.data == val:
                temp.next = temp.next.next
                return
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()


l = SLL()
l.insert_begin(1)
l.insert_end(2)
l.insert_end(3)
l.delete(2)
l.display()