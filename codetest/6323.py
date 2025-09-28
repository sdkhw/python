# 피보나치 수열


fivo = [1]

num = int(input())

if num == 1:
    print(fivo)

elif num >= 2:
    fivo.append(1)
    if num == 2:
        print(fivo)
    else:
        for i in range(num-2):
            fivo.append(fivo[-1]+fivo[-2])
        print(fivo)

