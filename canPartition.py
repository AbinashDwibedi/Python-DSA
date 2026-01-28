
class Solution:
    def canPartition(self, nums):       
        numsSum = sum(nums)
        if numsSum % 2 != 0:
            return False
        
        
        def checkSubsetSum(nums,k):
            n = len(nums)
            prev = [0]*(k+1)
            prev[0] = 1
            for i in range(n):
                curr = [0]*(k+1)
                curr[0] = 1
                for j in range(k+1):
                    notTake = prev[j]
                    take = 0
                    if nums[i] <= j:
                        take = prev[j-nums[i]]
                    curr[j] = notTake + take
                prev = curr
            return curr[k]>0
        return checkSubsetSum(nums,numsSum//2)