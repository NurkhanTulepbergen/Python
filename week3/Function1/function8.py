thislist =[int(x) for x in input().split()]
def spy_games(arr):
    return '007' in ''.join(str(i) for i in arr)

print(spy_games(thislist))
#Tulepbergen Nurkhan