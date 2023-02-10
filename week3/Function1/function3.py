def solve(numheads, numlegs):
    rh = (numlegs - 2*numheads)//2
    ch = (4*numheads - numlegs)//2
    print(ch, rh)

numheads = int(input(" "))
numlegs = int(input(" "))

solve(numheads, numlegs)

#Tulepbergen Nurkhan