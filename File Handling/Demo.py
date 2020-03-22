
f = open('File Handling/MyData','r') #reading
print(f)
#<_io.TextIOWrapper name='File Handling/MyData' mode='r' encoding='cp1252'>

print(f.read())
"""
My name is Damindu Sandaruwan
Undergraduate in USJ
Phython Programming
Information and Comminucation Technology
Sri Lanka
"""
print("-----------------------")


g = open('File Handling/MyData','r') #reading

print(g.readline())
print(g.readline())

"""
My name is Damindu Sandaruwan

Undergraduate in USJ
"""
print("-----------------------")

print(g.readline(),end="")
print(g.readline())

"""
Phython Programming
Information and Comminucation Technology
"""
#WRITE DATA

w1= open('File Handling/NewFile','w') #write

w1.write("Damindu Sandaruwan") #but loss other data and wtithe this
#so we have to append

w2= open('File Handling/NewFile','a') #append
w2.write(" Kalugalagedara")

print("-----------------------")
#Copying from other file

f2 = open('File Handling/MyData','r') #reading
w3= open('File Handling/NewFile','a') #append
for data in f2:
    print(data)
    w3.write(data)

print("-----------------------")

f3 = open('File Handling/MyPhoto.jpg','rb') #read binary

for i in f3:
   print(i)


f4 = open('File Handling/MyPhoto.jpg','rb') #read binary
f5 = open('File Handling/MyNewPic.jpg','wb') #write binary

for i in f4:
    f5.write(i) #create anothe my pic