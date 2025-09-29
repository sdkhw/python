nums =[int(x) for x in input().strip().split(',') if int(x) % 2 ==1]

# print(nums)

for id, val in enumerate(nums):
    if id == len(nums)-1:
        print(val)
        break
    else: print(val, end=", ")