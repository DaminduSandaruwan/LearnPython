#Polymorphism
    #1.Duck Typing
    #2.Operator Overloading
    #3.Merhod Overloading
    #4.Method Overiding

#Duck Typing

x = 5
x = 'Damindu'

class VSCode:
    def execute(self):
        print("Compiling")
        print("Running")

class Laptop:
    def Code(self,ide):
        ide.execute()

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Conversion Check")
        print("Compiling")
        print("Running")

ide=VSCode()

lap1 = Laptop()
lap1.Code(ide)
#Compiling
#Running

print("------------------------------")

ide=MyEditor()
lap1.Code(ide)
#Spell Check
#Conversion Check
#Compiling
#Running