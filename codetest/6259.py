s = list(input().strip())

# print(s)

answer = {
    'LETTERS' : 0,
    'DIGITS' : 0
}


for i in s:
    if  (ord(i)>= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) >= 90):
        answer['LETTERS'] += 1
    elif ord(i)>= 48 and ord(i) <=57:
        answer['DIGITS'] += 1

# print(answer)

for k, v in zip(answer.keys(), answer.values()):
    print(f'{k} {v}')


# print(ord('a')) # 97
# print(ord('z')) # 122
# print(ord('A')) # 65
# print(ord('Z')) # 90

# print(chr(91))

# print(ord('0')) # 48
# print(ord('1')) # 49
# print(ord('9')) # 57