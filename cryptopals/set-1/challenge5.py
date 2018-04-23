from binascii import unhexlify, hexlify


def xor(a, key):
    a = bytearray(a, 'utf-8')
    key = bytearray(key, 'utf-8')
    new = ""
    for i in range(len(a)):
        new += chr(a[i] ^ (key[i % len(key)]))
    return hexlify(bytearray(new, "utf-8"))

a = "Burning 'em, if you ain't quick and nimbleBurning 'em,\
 if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

print(xor(a, key))
