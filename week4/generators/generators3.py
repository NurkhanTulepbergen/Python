def divs(n):
    for i in range(n+1):
        if i % 12 == 0:
            yield i
n = int(input())
for x in divs(n):
    print(x)