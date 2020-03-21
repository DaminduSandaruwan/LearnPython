class Computer:
    
    def config(self):
        print("i5, 16GB, 1TB ",self.cpu,self.ram)

    def __init__(self,cpu,ram): 
        self.cpu=cpu
        self.ram=ram

        

comp1=Computer('Intel',16)
comp2=Computer('Rayzen 3',8)

comp1.config() #i5, 16GB, 1TB  Intel 16
print(comp1.ram)#16
print(comp1.cpu) #Intel

print("------------------------------")

comp2.config() #i5, 16GB, 1TB  Rayzen 3 8
print(comp2.ram)#8
print(comp2.cpu) #Rayzen 3

