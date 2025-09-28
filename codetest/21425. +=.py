with open("./1_sample_input.txt", "r") as f :
    lines = f.readlines()

# 첫 줄 (예 데이터 개수)
n = int(lines[0].strip())
# print("n =", n)


# 나머지 줄 처리
data = []

for line in lines[1:]:
    # a , b, c = map(int, line.strip().split(" "))

    nums = list(map(int, line.strip().split(" ")))
    a, b = max(nums[0], nums[1]) , min(nums[0], nums[1])
    c = nums[2]
    i = 0
    while b <= c:
        b += a
        i += 1
    print(i)

    # data.append(nums)
