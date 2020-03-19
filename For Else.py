nums = [12,16,18,21,20,25]

for num in nums:
    if num % 5 == 0:
        print(num)
        break # for get only one answer (one iteration)
else:
    print("Not Found")
