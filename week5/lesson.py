import re
file = open("C:/Tulepbergen/pp2/week5/text.txt", "r", encoding = "UTF8")
result = re.findall(".*(а or a).*(б or b)*", file.read())
print(result)
