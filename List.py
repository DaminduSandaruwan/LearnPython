nums = [25,26,59,48,65,45,25,45,63]
print(nums) #[25, 26, 59, 48, 65, 45, 25, 45, 63]
print(nums[0]) #25
print(nums[2:]) #[59, 48, 65, 45, 25, 45, 63]

names=['Daminu','Sandaruwan','Bandara']
print(names) #['Daminu', 'Sandaruwan', 'Bandara']

values=[9.5,'Damindu',45]
print(values) #[9.5, 'Damindu', 45]

mil=[nums,names]
print(mil) #[[25, 26, 59, 48, 65, 45, 25, 45, 63], ['Daminu', 'Sandaruwan', 'Bandara']]

nums.append(45) #adding new item
print(nums) #[25, 26, 59, 48, 65, 45, 25, 45, 63, 45]

nums.insert(2,88) #insert number between list (index 2)
print(nums) #[25, 26, 88, 59, 48, 65, 45, 25, 45, 63, 45]

nums.remove(26)
print(nums) #[25, 88, 59, 48, 65, 45, 25, 45, 63, 45]

nums.pop(1) # remove index 1
print(nums) #[25, 59, 48, 65, 45, 25, 45, 63, 45]

print(nums.pop())  #pop last element 45

del nums[2:] # delete numbers startind index 2
print(nums) #[25, 59]

nums.extend([29,12,14,36])
print(nums) #[25, 59, 29, 12, 14, 36]

print(min(nums)) #12 minimum
print(max(nums)) #59 maximum

nums.sort() #sorting
print(nums) #[12, 14, 25, 29, 36, 59]

 

