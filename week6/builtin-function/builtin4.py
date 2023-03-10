import time
def f(n, ms):
    time.sleep(ms/1000)
    x = pow(n, 1/2)  
    return(f"Square root of {n} after {ms} miliseconds is: {x}")
n = int(input())
ms = int(input())
print(f(n, ms))