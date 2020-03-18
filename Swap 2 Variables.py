#Normal Swaping
a = 5
b = 6

temp =a
a=b
b=temp

print(a)
print(b)

#in python
a = 5
b = 6

a = a + b
b = a - b
a = a - b

print(a) #6
print(b) #5

# in this case dont need extra memory
a = 5
b = 6

a= a ^ b
b = a ^ b
a = a ^ b

print(a) #6
print(b) #5

#another way
a = 5
b = 6

a,b=b,a

print(a) #6
print(b) #5