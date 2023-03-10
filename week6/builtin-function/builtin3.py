def f(string):
    l = ''.join(reversed(string))
    if string == l:
        return "Palindrom"
    else:
        return "Not Palindrom"
string = str(input())
print(f(string))
