#check prime number or not
num = int(input("Enter your Number : "))

for i in range(2,num):
    if num % i == 0:
        print("Not Prime Number")
        break
else:
    print("Prime Number")