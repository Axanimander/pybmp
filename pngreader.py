import math

def getLong(x, offset):
    return int.from_bytes(x[offset:offset+3], byteorder='big', signed=False)

class chunk:
    def __init__(self):
        self.length = 0
        self.type = 0
        self.data = []
        self.CRC = 0

class pngReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'rb')
        self.byte_array = self.file.read()
        self.first_byte = self.byte_array[0]
        self.signature = self.byte_array[1:4]
        self.header_string = ''
        self.chunk_array = []
        self.chunks = {
            "IHDR" : self.read_IHDR,
            "PLTE" : self.read_PLTE,
            "sRGB" : self.read_sRGB,
            "IDAT" : self.read_IDAT,
            "IEND" : self.read_IEND,
            "gAMA" : self.read_gAMA,
        }
    def readChunk(self, chunk_type, offset):
        self.chunks.get(chunk_type, lambda a:f'Unsupported Chunk Type: {a}')(offset)
    # Read the Header chunk   
    def read_IHDR(self): 
        return 0
    # Read the pallette chunk
    def read_PLTE(self):
        return 0
    # Read the color mode chunk
    def read_sRGB(self):
        return 0
    # Read the image data chunk
    def read_IDAT(self):
        return 0
    # Read the end chunk
    def read_IEND(self):
        return 0
    # Read the gamma chunk
    def read_gAMA(self):
        return 0
    def get_header_string(self):
        self.header_string = ''.join(list(map(chr, self.byte_array[12:16])))
    def end(self):
        self.file.close()


def runtest():
    z = pngReader("RED.png")
    z.get_header_string()
    print(z.header_string)
    



