def maxAdjacentDistance(nums):
    adjacent_max = max(abs(nums[i] - nums[i+1]) for i in range(len(nums)-1))
    circular = abs(nums[0] - nums[-1])
    return max(circular, adjacent_max)

print(maxAdjacentDistance(nums = [3,2,-5,-3]))
