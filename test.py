import unittest
from pngreader import *
from prefixtrie import *
from huffman import *
class testPng(unittest.TestCase):
    def test_header(self):
        z = pngReader("RED.png")
        z.get_header_string()
        self.assertEqual(z.header_string, 'IHDR')
        z.end()
    def test_huffman(self):
        s = 'lossless-compression'
        z = HuffmanEncoder()
        t = z.build_tree(s)
        m = z.decode(t)
        self.assertEqual(s,m)


if __name__ == '__main__':
    unittest.main()