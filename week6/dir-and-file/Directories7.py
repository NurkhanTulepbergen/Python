f1 = open("C:/Tulepbergen/pp2/week6/dir-and-file/experiment.txt", "r", encoding="UTF8")
x = f1.read()
f2 = open("secondex.txt", "w")
f2.write(x)
f2.close()
f2 = open("secondex.txt", "r", encoding="UTF8")
print(f2.read())

