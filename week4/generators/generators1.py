import math 
def f(n):
    a = 1
    while a <= n:
        yield pow(a, 2)
        a += 1
h = int(input())
for i in f(h):
    print(i)
        
# or 
""""

class f():
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a < self.n:
            self.a += 1 
            return pow(self.a, 2)
        else:
            raise StopIteration
a = int(input())
myclass = f(a)
myit = iter(myclass)
for x in myit:
    print(x)
"""