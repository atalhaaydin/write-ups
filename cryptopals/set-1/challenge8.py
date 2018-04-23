def detect_ecb(line, BLOCK_SIZE = 16):
    d = {}
    score = 0
    for i in range(0, len(line), BLOCK_SIZE):
        if line[i : i + BLOCK_SIZE] in d:
            d[line[i : i + BLOCK_SIZE]] += 1
            score += 1
        else:
            d[line[i : i + BLOCK_SIZE]] = 0
    if score >= 1:
        print(line)
        return line
    return None


f = open("8.txt").readlines()
for line in f:
    detect_ecb(line.rstrip("\n"))
