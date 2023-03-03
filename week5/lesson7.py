import re
file = open("C:/Tulepbergen/pp2/week5/text.txt", "r")
result = re.sub("_", "", file.read())
print(result)