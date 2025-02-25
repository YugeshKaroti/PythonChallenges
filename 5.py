# Given an array of integers nums, return the number of good pairs.A pair (i, j) is called good if nums[i] == nums[j] and i < j.
def numIdenticalPairs(nums):
    c = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j:
                if nums[i] == nums[j]:
                    c+=1
    return c