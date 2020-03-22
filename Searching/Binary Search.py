

def search(list,n):
    l = 0
    u = len(list)-1
    

    while l <= u:
        mid = (l+u)//2

        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid +1
            else:
                u = mid-1
    return False
pos=-1
list=[4,7,8,12,45,99,102,106,199,205]
n = 106

if search(list,n):
    print("Found at :", pos)
else:
    print("Not Found at :", pos)
