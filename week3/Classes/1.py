class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
    def grow(self):
        self.age += 10
    def cout(self):
        print("my age is" , str({self.age}))
class student(Person):
    def __init__(self,subject):
        super().__init__(self.name,self.surname,self.age)
        self.subject = subject
    def lala(self):
        print(self.subject)
        
x = Person("Sara", "hadskash", 20)
a = student("sara", "kdsahdsak", 20)
a.grow()
a.lala()
x.cout()
x.grow()
x.cout()
