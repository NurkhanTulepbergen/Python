import re
def f(m0bject):
    return m0bject.group("g1").upper()+ m0bject.group("g3") + m0bject.group("g2").upper() + m0bject.group("g4")
text = str(input())#snakecase hdja_dhkas_dshajk
pattern = "(?P<g1>\w)(?P<g3>\w)_(?P<g2>\w)(?P<g4>\w)"
print(re.sub(pattern, f, text))