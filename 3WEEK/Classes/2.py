class Shape:
    a = 0
    def area(self):
        print(self.a)
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def show(self):
        print(self.length**2)
length=int(input("Enter the length of the square:\n"))
a=Square(length)
a.show()

