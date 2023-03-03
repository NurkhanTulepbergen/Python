import re
file = open("C:/Tulepbergen/pp2/week5/text.txt", "r", encoding = "UTF8")
result = re.findall(r".*a+.*b{2,3}", file.read())
print(result)
