#CLASSES OBJECTS AND INHERITANCE
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname, end = '')

  def welcome(self):
    print("Welcome ", end = '')
    self.printname()
    print(" to the class of 2020")

x = Person("Disha", "Vadecha")
x.welcome()



class Student(Person):
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    self.graduationyear = 2019

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Tejaswini", "Tayade")
x.welcome()



#OVERLOADING AND OVERRIDING
class Rectangle:
  def __init__(self,length,breadth):
    self.length = length
    self.breadth = breadth

  def getArea(self):
    print(self.length*self.breadth," is area of rectangle")



class Square(Rectangle):
  def __init__(self,side):
    self.side = side
    Rectangle.__init__(self,side,side)
  def getArea(self):
    print(self.side*self.side," is area of square")

s=Square(5)
r=Rectangle(3,6)
s.getArea()
r.getArea()
