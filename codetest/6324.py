nums = [1,2,3,4,3,2,1]

# 유일한 값들만 남기는 작업

answer = []
for i in range(len(nums)):
    if i ==0:
        answer.append(nums[i])
    if nums[i] not in answer:
        answer.append(nums[i])


print(nums)
print(answer)