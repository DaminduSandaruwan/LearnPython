# DATA TYPES - None,Numeric,List,Tuple,Set,String,Range,Dictionary

#Numeric - int,float,complex,bool

num = 2.5
print(type(num)) #<class 'float'>

num=5
print(type(num)) #<class 'int'>

num = 6 + 9j
print(type(num)) #<class 'complex'>

a = 5.6
b = int(a)
print(type(b)) #<class 'int'>

k = float(b)
print(k) #5.0
print(type(k)) #<class 'float'>

k = 6
c = complex(b,k)
print(c) #(5+6j)

print(b<k) #True
bool=b<k
print(bool) #True

print(int(True)) #1

#List
lst = [25,52,65,89,78,45]
print(type(lst)) #<class 'list'>

#Set
set1={36,45,65,85,45}
print(type(set1)) #<class 'set'>

#Tuple
tup=(45,65,98,45,26,45,78,36)
print(type(tup)) #<class 'tuple'>

#String
str = "Damindu"
print(type(str)) #<class 'str'>
st = 'A'
print(type(st)) #<class 'str'>

#Range
a = range(0,10)
print(type(a)) #<class 'range'>
print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(2,10,2))) #[2, 4, 6, 8]


#Dictionary
dic = {'Damindu':'Huawei','Sandaruwan':'Samsung','Bandara':'Apple'}
print(dic) #{'Damindu': 'Huawei', 'Sandaruwan': 'Samsung', 'Bandara': 'Apple'}
print(type(dic)) #<class 'dict'>
print(dic.values()) #dict_values(['Huawei', 'Samsung', 'Apple'])
print(dic['Sandaruwan']) #Samsung
print(dic.get('Damindu')) #Huawei



