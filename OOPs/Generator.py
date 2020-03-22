#Generator gives iterator

def topten():
    
    yield 1 #make generator
    yield 2
    yield 3
    yield 4
    yield 5

values = topten()
print(values.__next__()) #1
print(values.__next__()) #2
print(values.__next__()) #3

for i in values:
    print(i) #4,5
    
print("------------------------------")
def topfive():
    n = 1
    while n<= 5:
        sq = n*n
        yield sq
        n += 1


values = topfive()


for i in values:
    print(i) #4,5