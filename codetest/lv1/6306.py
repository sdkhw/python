a, b = input(), input()

while True:
    if a.isdigit() and b.isdigit():
        print(f'x * y =  {int(a)*int(b)}')
        break
    else:
        print('숫자가 아닙니다. 재입력하세요.')
        a, b = input(), input()