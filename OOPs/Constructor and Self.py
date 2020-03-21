class Computer:
    def __init__(self):
        self.name="Damindu"
        self.age=23

    def update(self):
        self.age=30

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

#self is a pointer to directing object

c1=Computer() #in the Heap Memory hold objects
print(id(c1)) #11855664 address of that memory

#Size of an object depends on the no of variables

c2=Computer()
print(id(c2)) #50128688 



print(c1.name) #Damindu
print(c2.name) #Damindu

c1.name="Sandaruwan"
print(c1.name) #Sandaruwan

c1.update()
print(c1.age)#30


c3=Computer()

if c2.compare(c3): #comparing c2 and c3
    print("They are same")
else:
    print("They are different")