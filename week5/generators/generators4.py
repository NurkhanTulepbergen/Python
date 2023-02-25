class  f():
    def __init__(self, n, v):
        self.n = n
        self.v = v
    def __iter__(self):
        self.a = self.n-1
        return self
    def __next__(self):
        if self.a<self.v:
            self.a+=1
            return pow(self.a, 2)
        else:
            raise StopIteration
g, c = map(int,input().split())
myclass = f(g, c)
myit = iter(myclass)
for x in myit:
    print(x)