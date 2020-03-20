def add(a,b): #Formal Argument
    c = a + b 
    print(c)

add(5,6)

#Actual Argument--> 1.Position 2.Keyword 3.Default 4.Variable Length

def person(name,age):
    print(name)
    print(age)

person('Damindu',23) #position 

print("------------------------")

person(23,'Damindu') #in this case name=23 and age = 'Damindu'

print("------------------------")

person(age=23,name='Damindu') #use keyword

print("------------------------")

def person(name,age=18): #Default
    print(name)
    print(age)
person('Damindu') # in this case use default age
print("------------------------")

def Sum(a, *b):
    c =a
    for i in b:
        c = c+i
    print(c)

Sum(5,6,7,8) # in this case use variable length parameters

print("------------------------")

def person(name, **data):
    print(name) #Damindu
    print(data) #{'age': 23, 'city': 'Kandy', 'Tel': 761234567}

    for i,j in data.items():
        print(i,j)
        #age 23
        #city Kandy
        #Tel 761234567


person('Damindu',age = 23,city = 'Kandy',Tel = 761234567)# Keyworded variable Length Argument