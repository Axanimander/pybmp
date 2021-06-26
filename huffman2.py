from queue import PriorityQueue

class Node:
    def __init__(self, char_list, freq=0, left=None, right=None):
        self.char_list = char_list
        self.freq = freq
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.freq < other.freq
    def __le__(self, other):
        return self.freq <= other.freq
    def __gt__(self, other):
        return self.freq > other.freq
    def __ge__(self, other):
        return self.freq >= other.freq
    