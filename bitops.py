def append_zero_bit(data):
    """appends 0 to the end of a series of bits"""
    return (data << 1) | 0

def append_one_bit(data):
    """Appends 1 to the end of a series of bits"""
    return (data << 1) | 1

def copylastbit(src, dst):
    """Appends final bit from one series of bits to another"""
    return (dst << 1) | (src & 1)

def pop_last_bit(bits):
    bits >> 1

def destructive_copy_last_bit(src, dst):
    t = copylastbit(src, dst)
    src = src >> 1
    return t
    


