from binascii import unhexlify, hexlify
from random import randint
# not completed
def hamming_distance(a, b):
    if len(a) != len(b):
        exit(1)

    dist = 0
    for x, y in zip(a, b):
        z = x ^ y
        while z:
            dist += z & 1
            z >>= 1

    return dist

a = bytearray("this is a test", "utf-8")
b = bytearray("wokka wokka!!!", "utf-8")
print(hamming_distance(a, b))
