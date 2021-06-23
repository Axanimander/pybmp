from huffman import *
def compressfile(filename, fileout):
    z = HuffmanEncoder()
    compressed_data = None
    with open(filename, 'rb') as binfile:
        buff = binfile.read()
        z.build_tree(str(buff))
        compressed_data = z.encode(str(buff))
    with open(fileout, 'x') as outfile:
        outfile.write(compressed_data)
 

    
    

