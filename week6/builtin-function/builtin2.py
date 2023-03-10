def f(s):
    cnt = 0
    cnt1 = 0
    for x in range(len(s)):
        if s[x].upper()==s[x]:
            cnt += 1
        elif s[x].lower()==s[x]:
            cnt1 += 1
    yield r'The numbers of upper case: ', cnt
    yield r'The numbers of lower case: ', cnt1
s = str(input())
x = f(s)
for i in f(s):
    print(i)
