# nums = [int(x) for x in input().strip().split()]

s = input().strip()
answer = 0
for c in s:
    answer += int(c)
print(answer)

# s = 0
# for i in nums:
#     s+= i

# print(s)

for a, b in zip([1,2] , [3,4]):
    print(a,b)