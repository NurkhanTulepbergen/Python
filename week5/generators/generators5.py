class f():
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        self.a = self.n
        return self
    def __next__(self):
        if self.a>0:
            self.a -= 1
            return self.a
        else:
            raise StopIteration
a = int(input())
myclass = f(a)
myit = iter(myclass)
for x in myit:
    print(x)