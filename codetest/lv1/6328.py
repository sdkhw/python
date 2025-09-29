st = input().strip().split(',')

print(st)

if len(st[0].strip()) > len(st[1].strip()):
    print(st[0].strip())
else:
    print(st[1].strip())



# 리스트 컴프리헨션

st = [s.strip() for s in input().split(',')]
# ,로 구분하고 각 요소 공백 제거