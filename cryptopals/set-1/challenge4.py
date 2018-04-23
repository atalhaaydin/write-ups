from binascii import unhexlify
f = open("4.txt").readlines()
n = open("new.txt", "w")
new_f = []
for line in f:
    new_f.append(unhexlify(line.rstrip('\n')))
alnum = list(range(ord('A'), ord('Z')))
alnum.extend(list(range(ord('a'), ord('z'))))
alnum.extend(list(range(ord('0'), ord('9'))))

for i in range(len(alnum)):
    for j in range(len(new_f)):
        for k in range(len(new_f[j])):
            n.write(chr(alnum[i] ^ new_f[j][k]))
        n.write("\n")
n.close()
# $ strings new.txt -n 25
# Now that the party is jumping
