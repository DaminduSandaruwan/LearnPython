for i in range(4): #(0,4)
    for j in range(0,4):
        print("# " ,end="") # end is use for being i the same line. not to go next line
    print()

print("----------------------")

for i in range(4):
    for j in range(i+1):
        print("# ", end="")
    print()

print("---------------------")

for i in range(4):
    for j in range(4-i):
        print("# ", end="")
    print()

