#Method Overloading --> same method different argument

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        return s


s1=Student(45,86)


print(s1.sum(5,9)) #14

print(s1.sum(5,9,7)) #21

print("-----------------------------")
#Method Overriding

class A:
    def show(self):
        print("In A Show")

class B(A):
    def show(self):
        print("In B Show")

a1 =A()
a1.show() #In A Show

b1= B()
b1.show() #In B Show