
letters = ['a', 'b', 'c' , 'd', 'e' , 'i', 'h']

def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False


filtered_vowels = filter(filter_vowels,letters)

answer = list(filtered_vowels)
print(answer)


# filter((True or False 진리 함수?) ,순환 가능 객체)
mylist = [1,2,3,4,5,6,7,8,9,10]

mylist2 = list(filter(lambda x : x % 2 == 0, mylist))
mylist3 = list(map(lambda x : x**2, mylist2))

print('mylist2 :',mylist2)
print('mylist3 :',mylist3)

i= 1
for i in range(10):
    print(i)

print(i) # 이게왜?