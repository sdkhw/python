# filter((True or False 진리 함수?) ,순환 가능 객체)
# map 어떤 조건에 대응되는 새로운 수를 뱉음

mylist = [1,2,3,4,5,6,7,8,9,10]

mylist2 = list(filter(lambda x : x % 2 == 0, mylist))
mylist3 = list(map(lambda x : x**2, mylist2))

p1 = list(map(lambda x : x**3 , mylist))

print(mylist2)
print(mylist3)
print(p1)
