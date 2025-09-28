import random



nums = [2, 4, 6, 8, 10]
print(nums)

# x = random.randint(0,10)
# y = random.randint(0,10)

x = 5
y = 10
if x in nums:
    print(f'{x} => True')
else:
    print(f'{x} => False')

if y in nums:
    print(f'{y} => True')
else:
    print(f'{y} => False')