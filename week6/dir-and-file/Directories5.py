f = open("C:/Tulepbergen/pp2/week6/dir-and-file/experiment.txt", "a", encoding = "UTF8" )
list1 = []
x = str(input())
list1.append(x)
f.write(str(list1))
f.close()
f = open("C:/Tulepbergen/pp2/week6/dir-and-file/experiment.txt", "r", encoding = "UTF8")
print(f.read())
