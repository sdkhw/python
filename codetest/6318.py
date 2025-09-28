string = 'abcdef'

dic = {}
val = 0
for s in string:
    dic[s] = val
    val += 1

for key, val in dic.items():
    print(f'{key}: {val}')
