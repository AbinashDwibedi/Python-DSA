class Solution:
    def subarraysWithSumDivByK(self, nums, k):
        prefix = 0
        mp = {0:[-1]}
        result = []
        for i,num in enumerate(nums):
            prefix += num
            rem = prefix % k
            if rem in mp:
                for j in mp[rem]:
                    result.append(nums[j+1:i+1])
            if rem not in mp:
                mp[rem] = []
            mp[rem].append(i)
        return len(result)