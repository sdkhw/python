def solution(my_string, is_prefix):
    answer = 0
    if  len(is_prefix) > len(my_string):
        return 0
    else:
        for i in range(len(is_prefix)):
            if is_prefix[i] == my_string[i]:
                answer = 1
            else: 
                return 0
            
    return answer

print(solution("banana","nan"))
# print(chr('a'))

str = "hello"

for c in str:
    if(ord(c) <ord('l')):
        print("더 적음")
    elif ord(c) == ord('l'):
        print("같음")

    else: print("더 큼")

print(ord('l'))
print(ord('h'))
print(ord('e'))
print(ord('l'))
print(ord('l'))
print(ord('o'))

