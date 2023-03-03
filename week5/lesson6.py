import re
file = open("C:/Tulepbergen/pp2/week5/text.txt", "r", encoding = "UTF8")
result = re.sub("[ ,.]", ":", file.read())
print(result)