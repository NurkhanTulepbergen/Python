import re
file = open("C:/Tulepbergen/pp2/week5/text.txt", "r",  encoding = "UTF8")
result = re.findall("[A-Z][a-z]+")
print(result)
