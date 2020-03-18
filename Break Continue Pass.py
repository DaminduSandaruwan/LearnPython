#Break Continue Pass

#Break
av = 10 # availble candy
x = int(input("How many Candies you want ? "))
i=1
while i<=x :
    if(x>av):
        print("Out of stock")
        break
    print("Candy")
    i+=1

print("Bye...")
print("------------------------------------")
#Continue
for i in range(1,20):
    if(i%3==0):
        continue
    print(i) #print withour 3s multipications


print("------------------------------------")
#Pass
for i in range(1,20):
    if(i%2==0):
        pass
    else:
        print(i) # print all odd numbers in range 1-20

print("------------------------------------")

if i==4:
    pass #when we want to pass block

def fun():
    pass




