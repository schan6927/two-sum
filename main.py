def twoSum(nums, target) :
    length = len(nums) -1
    j = 1
    for i in range(length-1):
        for j in range(length):
            if(nums[i]+nums[j] == target):
                return [i,j]

arr = [2, 7, 11, 15]
num = 9
print(twoSum(arr, num))
