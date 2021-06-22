import unittest
from pngreader import *
from prefixtrie import *
class testPng(unittest.TestCase):
    def test_header(self):
        z = pngReader("RED.png")
        z.get_header_string()
        self.assertEqual(z.header_string, 'IHDR')
        z.end()
    def test_prefix(self):
        z = Node()


if __name__ == '__main__':
    unittest.main()