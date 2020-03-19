#Function

def greet(): 
    print("Hello")
    print("Good Morning")

greet() #calling


def add(x,y):
    c = x+y
    return c

result = add(10,20)
print(result)


def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1,result2=add_sub(10,6)
print(result1,result2)
