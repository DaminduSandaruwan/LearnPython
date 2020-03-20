#Factorial

def fac(n):
    if(n==0):
        return 1

    else:
        return n * fac(n-1)



result=fac(5)
print("Factorial is : ",result)