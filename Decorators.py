#Decorators

def div(a,b):
    if a<b:
        a,b = b,a #swap
    print(a/b)

div(2,4) # but user want do 4/2

print("---------------")

#without tochinf function ,, we can use decorators

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div1 = smart_div(div) #change the behavior of that function
div1(2,4) #2.0


