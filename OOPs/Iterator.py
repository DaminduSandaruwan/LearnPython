nums = [7,8,9,5]



it=iter(nums)
print(it)

print(it.__next__()) #7
print(it.__next__()) #8

print(next(it))#9

for i in nums:
    print(i)

print("---------------------------")

class TopTens:
    
    def __init__(self):
        self.num = 1
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1

            return val
        else:
            raise StopIteration

values = TopTens()

print(next(values))
for i in values:
    print(i)

#print onlu 1 to 10 not repeat 1 twice