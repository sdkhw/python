# import sys

# input = sys.stdin.readline  # 빠른 입력


T = int(input())  # 테스트 케이스 개수 읽기

for _ in range(T):
    x, y, n = map(int, input().split(" "))
    # 각 테스트 케이스 처리
    cnt = 0
    while True:
        if x > n: break
        x,y = min(x,y), max(x,y)
        x += y
        cnt += 1 
    print(cnt)
        # max_num = max(x,y)
        # min_num = min(x,y)


        # 무조건 작은놈에서 큰놈을 더해 업데이트 해야함.

    # print("max", max_num)
    # print("min", min_num)

    # print(x)  # 여기서 원하는 로직을 넣으면 됨



