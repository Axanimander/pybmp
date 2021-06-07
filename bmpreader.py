import math

def getLong(a, n):
	return (a[n+3] * (2**24)) + (a[n+2] * (2**16)) + (a[n+1] * (2**8)) + (a[n])
def getInt(a, n):
	return ((a[n+1] * (2**8)) + (a[n]))
class bmpReader():
    def __init__(self, filename):
        #for now assume BITMAPINFOHEADER
        #https://en.wikipedia.org/wiki/BMP_file_format
        self.filename = filename
        f = open(filename, 'rb')
        self.byteArray = f.read()
        self.format = self.byteArray[:2]
        self.size = getLong(self.byteArray, 2)   
        self.arrOffset = getLong(self.byteArray, 10)
        self.pixelWidth = getLong(self.byteArray, 18)
        self.pixelHeight = getLong(self.byteArray, 22)
        self.colorPlanes = getInt(self.byteArray, 26) # Just for completion sake, should be 1
        self.bitDepth = getInt(self.byteArray, 28)
        self.compressionMethod = getLong(self.byteArray, 30) # value of 0 is none, most common
        self.dataSize = getLong(self.byteArray, 34)
        self.horizontalRes = getLong(self.byteArray, 38) # horizontal and vertical res in PPM (pixels per meter)
        self.verticalRes = getLong(self.byteArray, 42)
        self.palletteColors = getLong(self.byteArray, 46)
        self.importantColors = getLong(self.byteArray, 50) # generally ignored, here for completeness
        self.byteWidth = int(math.ceil(float(self.pixelWidth * self.bitDepth)/8.0))
        self.paddedWidth = int(math.ceil(float(self.byteWidth)/4.0)*4.0)
        self.byteSize = 2 if self.pixelWidth > 255 or self.pixelHeight > 255 else 1
        self.hexData = ""
        self.pixelArray = []
    def outputHexPixelData(self):
        for i in range(self.pixelHeight):
            for j in range(self.byteWidth):
                n = self.arrOffset + ((self.pixelHeight - 1 - i) * self.paddedWidth) + j
                v = self.byteArray[n]
                self.hexData += "{0:#04x}".format(v) + ", "
    def outputRawPixelData(self):
        for i in range(self.pixelHeight):
            for j in range(self.byteWidth):
                n = self.arrOffset + ((self.pixelHeight - 1 - i) * self.paddedWidth) + j
                v = self.byteArray[n]
                self.pixelArray.append(v)

                
                




                



    
