#Scope

a = 10 #Global

def something():
    a = 15 #Local
    print("Inside : ",a)


something()
print("Outside : ", a)


x = 10 #Global

def something2():    
    print("Inside : ",x) #Gloabal variable can access inside function

something2()
print("Outside : ", x)


#its not good
def something3():
    global c
    c=15
    print("in fun : ",c)

something3()
print(c) #can access c in the fuction when it is declare as global


print("-------------------------------")


z=10
print("ID of z : ",id(z))
def something4():
    z=9
    y=globals()['z']
    print("ID of Y : ",id(y))
    print("Z : ",z)

    globals()['z'] = 15

something4()
print("Now Z is : ",z)