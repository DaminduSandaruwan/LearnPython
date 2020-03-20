import sys

print(sys.getrecursionlimit()) #1000

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit()) #2000

i=0
def greet():
    global i
    i+=1
    print("Hello : ", i)
    greet()

greet()