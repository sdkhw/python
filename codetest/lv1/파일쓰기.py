nums = [1, 2, 3, 4, 5]

with open("output.txt", "w", encoding="utf-8") as f:
    # for num in nums:
    for i in range(5):
        f.write( " "* (4-i) +"*"* (i+1)+ "\n")


# for i in range(5):
#     print( " "* (4-i) +"*"* (i+1)+ "\n")    

nums = []

nums1 = []

print(nums)