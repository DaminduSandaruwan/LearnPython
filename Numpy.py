from numpy import *
# install numpy ---> pip3 install numpy

arr= array([1,2,3,4,5,6],int)
print(arr)
print("-----------------------------")
 #creating numpy Array

myarray=array([1,2,3,4,5])
print(myarray) #[1 2 3 4 5]
print(myarray.dtype) #int32

print("-----------------------------")

myarray=array([1,2,3,4,5.0])
print(myarray) #[1. 2. 3. 4. 5.]
print(myarray.dtype) #float64

print("-----------------------------")

myarray = linspace(0,15,16) #0-15 dividing into 16 parts
print(myarray) #[ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15.]

print("-----------------------------")

myarray = arange(1,15,2)
print(myarray) #[ 1  3  5  7  9 11 13]

print("-----------------------------")

myarray=logspace(1,40,5)
print(myarray)
print('%.2f' %myarray[4]) #10000000000000000303786028427003666890752.00

print("-----------------------------")

myarray= zeros(5)
print(myarray) #[0. 0. 0. 0. 0.]

print("-----------------------------")

myarray=ones(5,int)
print(myarray) #[1 1 1 1 1]

print("-----------------------------")
