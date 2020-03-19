from numpy import *

arr1= array([
                [1,2,3],
                [4,5,6]
            ])
print(arr1.ndim) #2 dimention
print(arr1.shape) #(2, 3) give row and coloumn 
print(arr1.size) #6 Size

arr2 = arr1.flatten() #cover 2d array to 1d array
print(arr2) #[1 2 3 4 5 6]

print("----------------------")

arr1= array([
                [1,2,3,6,2,9],
                [4,5,6,7,5,3]
            ])

arr3=arr1.reshape(3,4) #(3,4) 1D array convert to 2D array
print(arr3)
#[[1 2 3 6]
# [2 9 4 5]
# [6 7 5 3]]
print("----------------------")
arr3=arr1.reshape(2,2,3) #1D array convert to 3D array ---> 
#big 3d array has 2d array each 2d array has 1d array and each have 3 items
print(arr3)
#[[[1 2 3]
# [6 2 9]]

# [[4 5 6]
#  [7 5 3]]]
print("----------------------")

arr1= array([
                [1,2,3,6],
                [4,5,6,7]
            ])
m= matrix(arr1)
print(m)

m= matrix('1 2 3 6 ; 4 5 6 7')
print(m)
#[[1 2 3 6]
# [4 5 6 7]]

print("----------------------")

m= matrix('1 2 3; 6 4 5;1 6 7')
print(m)
#[[1 2 3]
# [6 4 5]
# [1 6 7]]

print("----------------------")


print(diagonal(m)) #[1 4 7]
print(m.max()) #7
print(m.min()) #1

m1 = matrix('1 2 3; 6 4 5;1 6 7')
m2= matrix('2 3 4; 7 2 9; 5 3 4')

m3 = m1*m2
print(m3)
#[[31 16 34]
# [65 41 80]
# [79 36 86]]

