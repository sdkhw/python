nums = [int(n.strip()) for n in input().strip().split(',')]

# print(nums)


for n in nums:
    print(f'square({n}) => {n**2}')