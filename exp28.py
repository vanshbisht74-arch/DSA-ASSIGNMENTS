# Experiment 28 :
# Bloom Filter Toy Demo

# Aim :
# Understand probabilistic membership test.

# What you will implement :
# Bit array + multiple hash functions.

# Input / Output :
# Input: insert items + query items
# Output: possibly present / definitely not present


size = 10
bit_array = [0] * size


def hash1(item):
    return len(item) % size


def hash2(item):
    return sum(ord(ch) for ch in item) % size


def add(item):
    bit_array[hash1(item)] = 1
    bit_array[hash2(item)] = 1


def check(item):
    if bit_array[hash1(item)] == 1 and bit_array[hash2(item)] == 1:
        return "Possibly present"
    else:
        return "Definitely not present"


add("apple")
add("banana")

print("Bit array:", bit_array)

print("apple:", check("apple"))
print("grape:", check("grape"))


# Reason :
# Bloom filter can say possibly present or definitely not present.
# It may give false positives but never false negatives.


# Viva :
# 1. Can bloom filter have false negatives?
# No

# 2. Why memory efficient?
# Uses bit array instead of storing full data

# 3. Industry use?
# Databases, cache, security systems