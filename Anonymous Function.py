#Anonymous Function - Lambda's

def squre(a): #Normal Function
    return a*a

result = squre(5)
print(result)

f = lambda a : a*a #Lambda Function
result = f(5)
print(result)

x = lambda a,b : a+b
result = x(5,6)
print(result)