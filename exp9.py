# Experiment 9: Dynamic Array Simulation

# Viva Q1: What is amortized complexity?
# Answer: Average cost per operation over many operations.

# Viva Q2: Why doubling helps?
# Answer: Reduces number of resizes.

# Viva Q3: Why pop is O(1)?
# Answer: Just decreases size (no shifting).


class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.arr = [0]*self.capacity

    def append(self, val):
        if self.size == self.capacity:
            self.capacity *= 2
            new = [0]*self.capacity
            for i in range(self.size):
                new[i] = self.arr[i]
            self.arr = new

        self.arr[self.size] = val
        self.size += 1
        print(self.arr[:self.size], "Size:", self.size, "Cap:", self.capacity)

    def pop(self):
        if self.size == 0:
            return "Underflow"
        self.size -= 1


d = DynamicArray()
d.append(1)
d.append(2)
d.append(3)
d.pop()