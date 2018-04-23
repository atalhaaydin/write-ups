from binascii import unhexlify, hexlify


def xor(a, b):
    new = []
    if(len(a) != len(b)):
        exit(1)
    a, b = unhexlify(a), unhexlify(b)
    for i in range(len(a)):
        new.append(a[i] ^ b[i])
    return hexlify(bytearray(new))

x = "1c0111001f010100061a024b53535009181c"
y = "686974207468652062756c6c277320657965"
print(xor(x, y))
# 746865206b696420646f6e277420706c6179
