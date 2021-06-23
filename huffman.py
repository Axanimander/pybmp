from heapq import heappush, heappop
from collections import Counter

def get_weights(data):
    """Returns a dictionary containing symbols with their frequencies"""
    return Counter(data)

def get_weights_reverse(data):
    return sorted(get_weights(data).items(), reverse=True)

def get_frequencies(data):
    weights = get_weights_reverse(data)
    f = {}
    for item in weights:
        f[item[0]] = float(item[1]) / len(data)
    return f
s = 'lossless-compression'

def sortByWeight(node):    
  return (node.weight * 1000000 + ord(node.symbol[0]))

class Node(object):
    left = None
    right = None
    item = None
    weight = 0
    decodedict = {}
    def __init__(self, symbol, weight, l=None, r=None):
        self.symbol = symbol
        self.weight = weight
        self.left = l
        self.right = r
    def __repr__(self):
        return '("%s", %s, %s, %s)' % (self.symbol, self.weight, self.left, self.right)
class HuffmanEncoder:
    def __init__(self):
        self.symbols = {}
        self.code = {}
        self.queue = []
        self.data = ""
    def get_frequency(self):
        self.symbols = {}
        for symbol in self.data:
            self.symbols[symbol] = self.symbols.get(symbol, 0) + 1
    def preorder_traversal(self, node, path=""):
        if node.left == None:
            self.code[node.symbol] = path
        else:
            self.preorder_traversal(node.left, path + "0")
            self.preorder_traversal(node.right, path + "1")

    def build_tree(self, data):
        self.data = data
        self.get_frequency()
        
        self.queue = []
        for symbol in self.symbols.keys():
            self.queue.append((Node(symbol, self.symbols[symbol], None, None)))
        self.queue.sort(key=sortByWeight)
            
        while len(self.queue) > 1:
            leftNode = self.queue.pop(0)
            rightNode = self.queue.pop(0)
            newNode = Node(leftNode.symbol + rightNode.symbol, leftNode.weight + rightNode.weight, leftNode, rightNode)
            self.queue.append(newNode)
            self.queue.sort(key=sortByWeight)
        self.code = {}
        self.preorder_traversal(self.queue[0])
        self.decodedict = dict((value, key) for key, value in self.code.items())

        encoded = ""
        for symbol in data:
            encoded = encoded + self.code[symbol]
        return encoded
    def view_codes(self):
        li = []
        for symbol in self.code.keys():
            code = self.code[symbol]
            li.append([len(code), symbol, code])
        li.sort()
        for c in li:
            print(c[1] + " : " + c[2])
    def decode(self, encodedbits):
        bits = ''
        decoded = ''
        for b in encodedbits:
            bits = bits + b
            #print(bits)
            if(bits in self.decodedict):
                decoded = decoded + self.decodedict[bits]
                bits = ''
        return decoded



    





