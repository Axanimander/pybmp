import unittest
from pngreader import *

from huffman import *
class testPng(unittest.TestCase):
    def test_header(self):
        z = pngReader("RED.png")
        z.get_header_string()
        self.assertEqual(z.header_string, b'IHDR')
        z.end()
    def test_huffman(self):
        s = 'lossless-compression'
        z = HuffmanEncoder()
        z.build_tree(s)
        t = z.encode(s)
        m = z.decode(t)
        self.assertEqual(s, m)
    def test_huffman_bits(self):
        s = s = 'lossless-compression'
        z = HuffmanEncoder()
        z.build_tree(s)
        t = z.encode(s)
        m = z.decode_bits(t)
        self.assertEqual(s, m)


if __name__ == '__main__':
    unittest.main()