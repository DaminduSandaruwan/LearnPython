""" Errors 
        1. Compile time
        2. Run time
        3. Logical 
"""

#syntax error -->Compile time

#everithing ok but answer is wrong ---> Logical error

#Everthing ok but user giving different input(divide bt zero) --->run time error

a = 5
b = 2

print(a/b)
#Statement -->1.Normal 2.Critical

print("Bye")


a = 5
b = 0

try:
    print(a/b) #ZeroDivisionError: division by zero
except Exception:
    print("Hey, You cant divide by zero") #Hey, You cant divide by zero

print("--------------------")
try:
    print(a/b)
except Exception as e:
    print("Error : ", e) #Error :  division by zero

print("--------------------")

try:
    print("Resource Open")
    print(a/b)
    print("Resource Closed")
except Exception as e:
    print("Error : ", e)

#Resource Open
#Error :  division by zero

print("--------------------")

try:
    print("Resource Open")
    print(a/b)

except Exception as e:
    print("Error : ", e)
    print("Resource Closed")

#Resource Open
#Error :  division by zero
#Resource Closed

print("--------------------")

try:
    print("Resource Open")
    print(a/b)

except Exception as e:
    print("Error : ", e)

finally:
    print("Resource Closed")

#Resource Open
#Error :  division by zero
#Resource Closed

print("--------------------")

a = 5
b = 2
try:
    print("Resource Open")
    print(a/b)
    k= int(input("Enter a Number : "))
    print(k)

except Exception as e:
    print("Error : ", e)

finally:
    print("Resource Closed")

#Resource Open
#2.5
#Error :  invalid literal for int() with base 10: 'p'
#Resource Closed

print("--------------------")

a = 5
b = 2
try:
    print("Resource Open")
    print(a/b)
    k= int(input("Enter a Number : "))
    print(k)

except ZeroDivisionError as e:
    print("Error : ", e)

except ValueError as e:
    print("Error : ", e)

except Exception as e:
    print("Error : ", e)

finally:
    print("Resource Closed")