class Node:
    def __init__(self) -> None:
        self.children = {}
        self.value = None
class PrefixTrie():
    def __init__(self):
        self.Head = Node()
    def find(self, node, key):
        for c in key:
            if c in node.children:
                node = node.children[char]
            else:
                return None
        return node.value

    def insert(self, node, key, value):
        for c in key:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.value = value
