class Solution:
    def checkSubarraySum(nums, k):
        remainder = {0:-1}
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            rem = prefix % k
            if rem in remainder:
                if i- remainder[rem] >= 2:
                    return True
            else:
                remainder[rem] = i
        return False
