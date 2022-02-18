class Shape:
    a = 0
    def area(self):
        print(self.a)
class Rectangle(Shape):
    def _init_(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length*self.width)
l=int(input("Enter the length:\n"))
w=int(input("Enter the width:\n"))
a=Rectangle(l,w)
a.area()