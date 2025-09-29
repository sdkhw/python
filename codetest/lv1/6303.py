nums1 = [1,3,6,78,35,55]
nums2 = [12,24,35,24,88,120,155]

nums3 = list(filter(lambda x : x in nums2, nums1))
print(nums3)