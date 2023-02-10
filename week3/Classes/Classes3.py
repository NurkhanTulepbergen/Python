class rec():
    def __init__(self,l,w):
       self.l=l
       self.w=w
    def area(self):
        return self.w*self.l
        
a=int(input())
b=int(input())       
rec=rec(a,b)
print(rec.area())

#Tulepbergen Nurkhan