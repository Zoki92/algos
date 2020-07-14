"""Suffix trie"""

class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.string = self.populate_suffix_tree(string)
    
    # Time complexity: O(n^2) | Space O(n^2)
    def populate_suffix_tree(self, string):
        for i in range(len(string)):
            self._populate_suffix_tree(i, string)
        
    def _populate_suffix_tree(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            if string[j] not in node:
                node[string[j]] = {}
            node = node[string[j]]
        node[self.endSymbol] = True
    
    # Time complexity: O(m) time | O(1) space
    # m is the length of the stree we are searching for
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node

    def __str__(self):
        return f"{self.root}"


trie = SuffixTrie('babc')

print(trie)
print(trie.contains('ab'))