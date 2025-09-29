s= "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

# score = ['A','B','C','D']

answer = 0

list_char = set(s)

dic = dict(map(lambda x : (x, s.count(x)) , list_char))

# print(dic)

for key, val in dic.items():
    if key == 'A':
        answer += val*4
    elif key == 'B':
        answer += val*3
    elif key == 'C':
        answer += val*2
    else:
        answer += val*1

print(answer)



# print(list_char)




'''
answer = 0
score = [0,0,0,0]




s= 'ksdksdksdksdkkksdddsdsdkkksdddsdsdkk'
result = {}

for ch in s:
    result[ch] = result.get(ch, 0) + 1

print(result)
print(result.get('s'))

print(s.count('k'))
# print(set(s))


s = 'ksdksdksdksdkkksdddsdsdkkksdddsdsdkk'
unique_chars = set(s)

count_dict = dict(map(lambda ch: (ch, s.count(ch)), unique_chars))
print(count_dict)


# A 4, B 3, C 2, D 1


'''
