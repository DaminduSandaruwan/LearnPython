num = 5
print(id(num)) #print address of num

name ='Damindu'
print(id(name)) #print address of name

a = 10
b = a

print(id(a)) #1938475072
print(id(b)) #1938475072
# address are same because b = a; in python 

print(id(10)) #1938475072 address is based on box it self

k = 10
print(id(k)) #1938475072

a=9
print(id(a)) #1938475056
print(id(b)) #1938475072

k = a
print(id(k)) #1938475056 same as address of (a)

b = 8
print(id(b)) #1938475040

PI= 3.14
print(type(PI)) #<class 'float'>







