
def update(x):
    x=8
    print(x)

update(10)

print("---------------")
def pas(x):
    print(id(x)) #1835321408
    x=8
    print(id(x)) #1835321376
    print("X : ",x) #X :  8

a=10
print(id(a)) #1835321408
pas(a)
print("a : ",a) #a :  10
print("---------------")


def fun(lst):
    print(id(lst)) #58485864
    lst[1]=25
    print(id(lst)) #58485864
    print("List : ", lst) #List :  [10, 25, 30]

lst=[10,20,30]
print(id(lst)) #58485864
fun(lst)
print("lst ", lst) #lst  [10, 25, 30]

