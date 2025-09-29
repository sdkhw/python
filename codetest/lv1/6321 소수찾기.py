# 소수 판별

num = int(input())

for i in range(num):
    if (i+1) == 1:
        continue
    elif i+1 == num:
        print('소수입니다.')
        break
    else:
        if num %(i+1) == 0:
            print('소수가 아닙니다.')
            break
    