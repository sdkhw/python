nums =  [12, 24, 35, 70, 88, 120, 155]

# print(list(filter(lambda x: x % 2 == 1, nums)))


# for idx,val in enumerate(nums):
    # print(idx, val)
answer = [val for idx,val in enumerate(nums) if (idx+1) % 2 == 0 ]
print(answer)