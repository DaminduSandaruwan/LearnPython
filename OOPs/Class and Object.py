#Class -Design - Blueprint
#Object - Instance

class Computer:
    #Attributes(Variavles) and Behaviour(Methods)

    def config(self):
        print("i5, 16GB, 1TB")

x=9
print(type(x)) #<class 'int'>

comp1 = Computer()
print(type(comp1)) #<class '__main__.Computer'>

print("------------------------")

Computer.config(comp1) #i5, 16GB, 1TB inside the () give the object


comp2=Computer()
Computer.config(comp2) #i5, 16GB, 1TB


comp1.config() #i5, 16GB, 1TB
comp2.config() #i5, 16GB, 1TB

