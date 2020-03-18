#if else
x = int(input("Enter Your Number : "))
r = x%2
if (r==0):
    print("Even")
    if x>5 : # checking another condition
        print("Number is greater than 5")
    else:
        print("Number is lower than 5")
else:
    print("Odd")

#if elif else
y = int(input("Enter your number : "))

if(y==1):
    print("One")
elif(y==2):
    print("two")
elif(y==3):
    print("Three")
else:
    print("Default")