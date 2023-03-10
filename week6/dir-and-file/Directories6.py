cnt = 0
while cnt < 26:
    for x in range(26):
        a = chr(x+65)
        f = open(f"{a}.txt", "x")
        cnt += 1