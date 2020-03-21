class Student: #Outer Class
    def __init__(self,name,rollno):
        self.name=name
        self.rollno = rollno
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop: #Inner Class
        def __init__(self):
                self.brand='HP'
                self.cpu='id'
                self.ram=8
        
        def show(self):
            print(self.brand,self.cpu,self.ram)
    

s1=Student("Damindu",2)
s2=Student("Sandaruwan",3)

print(s1.name,s1.rollno)

s1.show()
#Damindu 2
#HP id 8


lap1=s1.lap 
lap2=s2.lap

print(id(lap1))
print(id(lap2))

#You can create object of inner class inside the outer class or
#you can create object of inner class outside the outer class provided you use outer class name to call it

lap3 =Student.Laptop()
