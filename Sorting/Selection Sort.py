
def sort(nums):
    
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if nums[j]< nums[minpos]:
                minpos=j

        temp = nums[i]
        nums[i]= nums[minpos]
        nums[minpos]=temp

        print(nums)




nums = [5,3,8,6,7,2]
sort(nums)

print("Finally :",nums) #[2, 3, 5, 6, 7, 8]