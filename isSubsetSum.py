class Solution:
    def isSubsetSum (self, arr, sum):
        # n = len(arr)
        # dp = [[-1]*(sum+1) for _ in range(n)]
        # def helper(idx,k):
        #     if idx < 0:
        #         if k == 0:
        #             return 1
        #         else:
        #             return 0
        #     if dp[idx][k] != -1:
        #         return dp[idx][k]
        #     notTake = helper(idx-1,k)
        #     take = 0
        #     if arr[idx] <= k:
        #         take = helper(idx-1,k-arr[idx])
        #     dp[idx][k] = take + notTake
        #     return dp[idx][k]
        
        # ans = helper(n-1,sum)
        # return True if ans>0 else False

        n = len(arr)
        dp = [[0]*(sum+1) for _ in range(n+1)]
        dp[0][0] = 1
        
        for i in range(n):
            for j in range(sum+1):
                notTake = dp[i][j]
                take = 0
                if arr[i]<= j:
                    take = dp[i][j-arr[i]]
                dp[i+1][j] = take + notTake
        if dp[n][sum]>0:
            return True
        else:
            return False
        
        