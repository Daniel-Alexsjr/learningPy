nums = [3,2,2,3,2,2]
val = 3

for i in nums:
    if i == val:
        nums.append(nums.pop(nums.index(val)))

k = len([x for x in nums if x != val])

print(nums, k)