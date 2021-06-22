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



def build_tree(data):
    fr = get_frequencies(data)
    queue = []
    code = {symbol: '' for symbol in fr}
    for letter, frequency in fr.items():
        heappush(queue, (frequency, letter))
    while len(queue) > 1:
        firstf, firstl = heappop(queue)
        secondf, secondl = heappop(queue)
        for letter in firstl:
            code[letter] = '0' + code[letter]
        for letter in secondl:
            code[letter] = '1' + code[letter]
        heappush(queue, (firstf + secondf, ''.join(sorted(firstl + secondl))))
    return code
    





