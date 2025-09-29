# import sys

# for line in sys.stdin:
#     print(">>" , line.strip().upper())



# 런타임 에러
while True:
    s = input()
    if s=="":
        break
    print(f">> {s.upper()}")


# 런타임 에러X
while True:
    try:
        s = input()
    except:
        break
    if s=="":
        break
    print(f">> {s.upper()}")
          