def twoSum(nums, target) :
    length = len(nums) -1
    j = 1
    for i in range(length-1):
        for j in range(length):
            if(nums[i]+nums[j] == target):
                return [i,j]
)
