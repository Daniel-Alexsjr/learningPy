def removeDuplicates(nums):
    newarray =[]
    for i in nums:
        if i not in newarray:
            newarray.append(i)
    return newarray

print(removeDuplicates([1,1,2,3,4,4,4]))