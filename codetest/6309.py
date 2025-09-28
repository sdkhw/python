

import random

x = random.randint(1,30)

list1= [random.randint(1,30) for _ in range(10)]
list2= [random.randint(1,30) for _ in range(15)]

# answer = []
print(list1)
print(list2)

answer = list(set(filter(lambda x: x in list2, list1)))

print(sorted(answer))

# print(list(set(list2)))

# print(list1)
# print(list2)



num1 = [4, 29, 18, 13, 19, 25, 9, 6, 10, 24]

num2 = [18, 6, 23, 10, 27, 16, 11, 29, 13, 28, 9, 3, 15, 22, 19]


print(num1)
print(num2)
answer = list(set(filter(lambda x: x in num2, num1)))

print(sorted(answer))
