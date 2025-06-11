def removeDuplicates(nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                print(nums[j])
                j += 1
        return j

print(removeDuplicates([1,1,2,3,4]))