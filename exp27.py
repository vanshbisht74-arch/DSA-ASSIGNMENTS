# Experiment 27 :
# Trie / Prefix Tree

# Aim :
# Support fast prefix searching.

# What you will implement :
# Insert, search, startsWith.

# Input / Output :
# Input: words + prefix
# Output: True / False


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.end = True

    def search(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.end

    def startsWith(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True


trie = Trie()

trie.insert("cat")
trie.insert("car")
trie.insert("dog")

print(trie.search("cat"))
print(trie.search("ca"))
print(trie.startsWith("ca"))


# Reason :
# Trie stores characters level by level, so prefix search becomes fast.


# Viva :
# 1. Trie vs hash map for prefix?
# Trie is better for prefix search

# 2. Space trade-off?
# Uses more memory because every character creates nodes

# 3. Autocomplete use?
# Search suggestions