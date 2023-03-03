import re
def f(string):
    parts = re.findall('[A-Z][^A-Z]*', string)
    return ' '.join(parts)

string = str(input())
result = f(string)
print(result)