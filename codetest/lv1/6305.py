nums = [12,24,35,24,88,120,155,88,120,155]


def func(nums):
    result = []
    for n in nums:
        if n not in result:
            result.append(n)
    return sorted(result)

print(func(nums))