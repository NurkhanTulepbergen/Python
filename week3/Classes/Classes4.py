class Point:
    def move(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(str(self.x) + ' ' + str(self.y))
    def dist(self):
        print(abs(self.y-self.x))
p = Point()
a= int(input())
b= int(input())
p.move(a, b)
p.show()
p.dist()
p.move(a, b)
p.dist()

#Tulepbergen Nurkhan