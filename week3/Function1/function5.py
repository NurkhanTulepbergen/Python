from itertools import permutations
def random(string):
    a = list(permutations(string))
    for x in a:
        print(str().join(x), end=" ")
string = input()
print(random(string))

#Tulepbergen Nurkhan
