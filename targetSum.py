from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums, target):
        @lru_cache(None)
        def helper(idx, tar):
            if idx < 0:
                return 1 if tar == 0 else 0
            
            return helper(idx - 1, tar - nums[idx]) + helper(idx - 1, tar + nums[idx])

        return helper(len(nums) - 1, target)