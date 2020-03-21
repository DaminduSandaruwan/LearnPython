#Polymorphism
    #1.Duck Typing
    #2.Operator Overloading
    #3.Merhod Overloading
    #4.Method Overiding

a = 5
b = 6
print(a+b) #11
print(int.__add__(a,b)) #11


a = '5'
b = '6'
print(a+b) #56
print(str.__add__(a,b)) #56

print("-----------------------")

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other): #overload the + operator
        m1=self.m1 + other.m1
        m2=self.m2 + other.m2
        s3=Student(m1,m2)
        return s3
    
    def __gt__(self,other): #greater than
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False
            
    def __str__(self):
        return '{} {} '.format(self.m1, self.m2)        


s1=Student(75,80) 
s2=Student(25,65)

s3=s1+s2
print(s3.m1) #100

if s1>s2:
    print("s1 Win") #s1 Win
else:
    print("s2 Win")

print("---------------------")

#print(s1) #<__main__.Student object at 0x0307E640>
#print(s1.__str__()) #<__main__.Student object at 0x0307E640>

print(s1) #75 80 Operator Overloading