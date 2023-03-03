import re
def f(m0bect):
    return m0bect.group("g1") + " " + m0bect.group("g2") 
text = str(input())
pattern = r"(?P<g1>\w)(?P<g2>[A-Z]+)"
print(re.sub(pattern, f, text))