def reverse(a):
    s = a.split()[::-1]
    slist = []
    for x in s:
        slist.append(x)
    print(" ". join(slist))
a = str(input())
reverse(a)

#Tulepbergen Nurkhan