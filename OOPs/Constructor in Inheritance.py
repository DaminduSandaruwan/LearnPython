class A: #Super Class
    def __init__(self):
        print("in A Init")
        

    def feature1(self):
        print("Feature 1 Working")
    
    def feature2(self):
        print("Feature 2 Working")


class B(A): # Child Class inherit all the fetures of A #Sub class
    def __init__(self):
        print("in B Init")

    def feature3(self):
        print("Feature 3 Working")
    
    def feature4(self):
        print("Feature 4 Working")

class C(A): # Child Class inherit all the fetures of A #Sub class
    def __init__(self):
        super().__init__() # can access super class
        print("in B Init")

a1 = A() #in A Init

b1= B() #in B Init --> because i create a Consructor in B
# If you create object of sub class it will first try to find init of sub class , 
# if it is not found then it will call init of super class

c1=C() #if you have call super then it will first call init of super class then call init of sub class
#in A Init
#in B Init

print("---------------------")
class D():
    def __init__(self): 
        print("in D init")

class E(A,D):
     def __init__(self):
        super().__init__()
        print("in D init")
    
     def feat(self):
        super().feature2()


e1=E()
#in A Init
#in D init
 #Method Resolution Order Left to Right A--->B
e1.feature1() #Feature 1 Working
e1.feat() #Feature 2 Working