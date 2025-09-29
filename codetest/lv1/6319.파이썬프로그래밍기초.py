

st = str(input())
print(st)
a = ''

string_list = list(st)
string_list.reverse()

for s in string_list:
    a += s

if a == st:
    print('입력하신 단어는 회문(Palindrome)입니다.')
