#Instance methods, Class methods, Static methods

class Student:
    
    school = "Kandy"  #Class Variable

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


#Instance Methods ---> 1.Accessor Methods   2. Mutator Methods
    def avg(self): #Instance method
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1
    
    def set_m1(self,value):
        self.m1=value

    @classmethod   #set as a class method
    def getSchool(cls):
        return cls.school

    @staticmethod   #set as a static method
    def info():
        print("This is Student Class.. in abc module")



s1=Student(45,65,89)
s2=Student(89,35,69)

print("Average : ",s1.avg())
print("Average : ",s2.avg())

print(s1.m1) #45
s1.set_m1(80)
print(s1.get_m1()) #80

print(s1.getSchool()) #Kandy

print(Student.getSchool()) #Kandy

Student.info() #This is Student Class.. in abc module