# 입력 :1 2 3 4 5
# map 함수로 타입 변환

items = input().strip().split()

print(items)
nums = list(map(lambda x: int(x), items))

print(nums)


