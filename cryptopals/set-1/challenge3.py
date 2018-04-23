from binascii import unhexlify
a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
b = unhexlify(a)
alphabet = list(range(ord('A'), ord('Z')))
# alphabet.extend(list(range(ord('a'), ord('z'))))
# alphabet.extend(list(range(ord('0'), ord('9'))))

for i in range(len(alphabet)):
    print("#", chr(alphabet[i]), sep="", end = " ")
    for j in range(len(b)):
        print(chr(alphabet[i] ^ b[j]), end="")
    print()

# X Cooking MC's like a pound of bacon
