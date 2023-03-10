filename = open("C:/Tulepbergen/pp2/week6/dir-and-file/experiment.txt", "r", encoding="UTF8")
x = filename
count = 0
for line in x:
    count += 1
print(f'This file has {count} lines.')