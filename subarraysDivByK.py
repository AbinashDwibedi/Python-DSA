class Solution:
    def subarraysDivByK(self, nums, k):
        prefix = 0
        mp = {0:1}
        count = 0
        for i,num in enumerate(nums):
            prefix += num
            rem = prefix % k
            if rem in mp:
                count += mp[rem]
            mp[rem] = mp.get(rem,0)+1
        return count