

# try:
#     x = int(input())

#     if x <= 0 :
#         print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')

#     else:
#         for i in range(x):
#             print(x-i)
# except:
#     print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')


def countdown(x):
    if x <= 0:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
    else:
        for i in range(x):
            print(x-i)

countdown(0)
countdown(10)