# Experiment 26 :
# Hash Table using Separate Chaining

# Aim :
# Handle collisions using separate chaining.

# What you will implement :
# Insert, get, delete using key % table_size.

# Input / Output :
# Input: key-value pairs
# Output: bucket display + get/delete result


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_func(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_func(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_func(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return

    def display(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


ht = HashTable(5)

ht.insert(1, "A")
ht.insert(6, "B")
ht.insert(11, "C")

ht.display()

print("Get 6:", ht.get(6))

ht.delete(6)
print("After delete:")
ht.display()


# Reason :
# Keys 1, 6, 11 collide because key % 5 gives same index.


# Viva :
# 1. Collision meaning?
# When two keys get same index

# 2. Why chaining works?
# It stores multiple values in same bucket using list

# 3. Load factor?
# Number of elements / table size