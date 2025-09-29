strings = [x.strip() for x in input().strip().split(',')]

# print(strings)
strings.sort()

# print(strings)

for idx, val in enumerate(strings):
    if idx == len(strings)-1: 
        print(val)
    else: 
        print(val, end=', ')