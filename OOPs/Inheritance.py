class A: #Super Class
    def feature1(self):
        print("Feature 1 Working")
    
    def feature2(self):
        print("Feature 2 Working")


class B(A): # Child Class inherit all the fetures of A #Sub class
    def feature3(self):
        print("Feature 3 Working")
    
    def feature4(self):
        print("Feature 4 Working")


class C(B): #C(A,B)
    def feature5(self):
        print("Feature 5 Working")

a1 = A()
a1.feature1() #Feature 1 Working
a1.feature2() #Feature 2 Working

b1=B()
b1.feature3() #Feature 3 Working
b1.feature4() #Feature 4 Working

b1.feature1() #Feature 1 Working
b1.feature2() #Feature 2 Working

c1=C() #MultiLevel Inheritance  A <--- B <--- C
c1.feature5() #Feature 5 Working
c1.feature1() #Feature 1 Working
c1.feature3() #Feature 3 Working 