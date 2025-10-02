import heapq
T = int(input())  # 테스트 케이스 개수 읽기

for i in range(T):
    x =  int(input())
    y =  list(map(int, input().split(" ")))

    heapq.heapify(y)

    nod_num = len(y) // 2
    sum = 0
    
    while True:
        idx = nod_num - 1 
        sum += y[idx]
        if nod_num == 1:
            break
        nod_num //= 2
    print(f"#{i+1} {sum}")
