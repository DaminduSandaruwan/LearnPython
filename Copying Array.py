from numpy import *

arr= array([1,2,3,4,5])

arr=arr+5
print(arr) #[ 6  7  8  9 10]

arr1= array([1,2,3,4,5])
arr2= array([6,7,8,9,10])

arr3 = arr1+arr2
print(arr3) #[ 7  9 11 13 15]

print(sin(arr1)) #[ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427] 
print(cos(arr1)) #[ 0.54030231 -0.41614684 -0.9899925  -0.65364362  0.28366219]
print(log(arr1)) #[0.         0.69314718 1.09861229 1.38629436 1.60943791] 
print(sqrt(arr1)) #[1.         1.41421356 1.73205081 2.         2.23606798]  
print(sum(arr1)) #15
print(min(arr1)) #1
print(max(arr1)) #5

print(concatenate([arr1,arr2])) #[ 1  2  3  4  5  6  7  8  9 10]

#copy
#alising
arr1=array([25,65,85,45,48])
arr2= arr1 #copy
print(arr2) #[25 65 85 45 48]

print(id(arr1)) #194789032 Id same
print(id(arr2)) #194789032 Id same

arr1=arr2.view() # in this case we can get both two ids

print(id(arr1)) #25013208 Id not same
print(id(arr2)) #197148248 

#Shallow Copy

arr1 = array([2,6,8,1,3])
arr2 = arr1.view()
arr1[1]=7

print(arr1) #[2 7 8 1 3]
print(arr2) #[2 7 8 1 3]
# in shallow copy both when we change item of one array, both array items will be changed

#Deep Copy
arr1 = array([2,6,8,1,3])
arr2 = arr1.copy()
arr1[1]=7

print(arr1) #[2 7 8 1 3]
print(arr2) #[2 6 8 1 3]
#in  deep copy when we change item in one array it effect only that array

