
class Shape():

    def __init__(self,name):
        self.name=name

    def describe(self):
        print (f"This shape is called {self.name}")

#shape1=Shape(name="")
# shape1=Shape(name="name")
# shape1.describe()

class Rectangle(Shape):
    def __init__(self, length,width):
        super().__init__("Rectangle")
        self.width=width
        self.length=length    

    def area(self):
        a=self.width*self.length
        print(f"For {self.name} area is {a}")
        return a

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius=radius
        

    def area(self):
        a=3.142*self.radius*self.radius
       
        print(f"For {self.name} area is {a}")
        return a

r1=Rectangle(10,3)
r1.describe()
r1.area()

c1=Circle(12)
c1.describe()
c1.area()