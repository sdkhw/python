# nums = 2, 3, 4, 5
import math

nums = [int(x) for x in input().strip().split(',')]


# print(nums)

answer = list(map(lambda x: round(x*2*math.pi, 2) , nums))

for idx, val in enumerate(answer):
    
    if idx == len(answer)-1:
        print(val)
    else:
        print(val, end=', ')