#in array same type items, fixed size

#import array as arr
from array import *

#type code
    #'i' - signed int, 'I'- unsigned int
    #'f' -float, 'd'- double, 'l' - signed long, 'L' - unsigned Long
vals = array('i',[5,9,8,4,2])
print(vals) #array('i', [5, 9, 8, 4, 2])

print(vals.buffer_info()) #(21948200, 5) it is address,array size
print("-----------------------------")
print(vals.typecode) #i print typecode
print("-----------------------------")
vals.reverse() #reverse the array
print(vals) #array('i', [2, 4, 8, 9, 5])
print("-----------------------------")
print(vals[0]) #2 print 0 index

print("-----------------------------")

for i in range(len(vals)): #use len for get the length of array
    print(vals[i])

print("-----------------------------")

cha = array('u',['a','e','u','d'])
for i in range(len(cha)):
    print(cha[i])
print("-----------------------------")

vals = array('i',[5,9,8,4,2])

newArr = array(vals.typecode,(a for a in vals)) #assign one by one from vals array 
for i in range(len(newArr)):
    print(newArr[i]) #print 5 9 8 4 2

print("-----------------------------")
i=0
while(i<len(newArr)):
    print(newArr[i])
    i+=1

#getting input from user to array

myarr=array('i',[])
n = int(input("How many numbers do you want to add : "))

for i in range(n):
    x = int(input("Enter your Number :"))
    myarr.append(x) #send the value to array

print(myarr)

val = int(input("Enter Value for Search : "))
k=0
for i in myarr:
    if i ==  val:
        print("Found the Number and Index is : ",k)
        break
    k+=1 # for counting index
print(myarr.index(val)) # we can use this method for finding index for val 