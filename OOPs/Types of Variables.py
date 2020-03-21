class Car:

    wheels = 4 #class namespace

    def __init__(self):
        self.mil=10     #Instance Variable
        self.com="BMW"  #Instance Variable


c1=Car()
c2=Car()

print(c1.com,c1.mil,c1.wheels) #BMW 10 4
print(c2.com,c2.mil,c2.wheels) #BMW 10 4

c1.mil=8
print(c1.com,c1.mil) #BMW 8

#namespace => 1.Class Namespace   2. Object/instance Namespace

Car.wheels=5
print(c1.com,c1.mil,c1.wheels) #BMW 8 5