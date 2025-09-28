# reverse sort 함수

names = ['재석', '명수', '준하','형돈','하하', '홍철', '길']

# 원본은 건드리지 않고 뒤집는 함수
reversed_name = list(reversed(names))
print(reversed_name)
print(names)


# 원본 뒤집기

names.reverse()
print(names)


# sort

list1 = [3, 1, 4, 2, 5]

# list1.sort()
print(list1)

print(sorted(list1, reverse=True))
