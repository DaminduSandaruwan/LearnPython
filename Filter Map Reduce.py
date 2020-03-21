#filter() map() reduce()

#filter()
nums = [3,2,6,5,8,9,6,4,8,5,8]

def is_even(n):
    return n%2==0

evens = list(filter(is_even,nums))
print(evens) #[2, 6, 8, 6, 4, 8, 8]

print("------------------------------")

evens = list(filter(lambda x : x%2==0,nums))
print(evens) #[2, 6, 8, 6, 4, 8, 8]

print("------------------------------")

def update(n):
    return n*2

doubles = list(map(update,evens))
print(doubles) #[4, 12, 16, 12, 8, 16, 16]

print("------------------------------")

doubles = list(map(lambda x :x*2 ,evens))
print(doubles) #[4, 12, 16, 12, 8, 16, 16]

print("------------------------------")

from functools import reduce 

def add_all(a,b):
    return a+b

sum = reduce(add_all,doubles)
print(sum) #84

print("------------------------------")

sum = reduce(lambda x,y : x+y,doubles)
print(sum) #84