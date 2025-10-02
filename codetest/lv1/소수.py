

def sieve_primes(M, N):
    sieve = [True] * (N + 1)
    sieve[0:2] = [False, False]  # 0, 1은 소수가 아님

    for i in range(2, int(N**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, N+1, i):  # i 배수 제거
                sieve[j] = False

    return [x for x in range(M, N+1) if sieve[x]]

# print(sieve_primes(1, 100))


import math

list1 = sieve_primes(1, 100)

num = 1

def function(n) :
    return n**2 /(n**2 -1)

for i in list1:
    num *= function(i)

print(num)
answer = math.pi**2 / 6

print(answer)
print("error :", num - answer)

list2 = sieve_primes(1,2100)

print(list2[-20:])