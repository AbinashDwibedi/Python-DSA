class Solution:
    def knapSack(self, val, wt, capacity):
        # n = len(wt)
        # dp = [[-1]*(capacity+1) for _ in range(n)]
        # def helper(idx,cap):
        #     if idx < 0:
        #         return 0
        #     if dp[idx][cap] != -1:
        #         return dp[idx][cap]
        #     notPick = helper(idx-1,cap)
        #     pick = float("-inf")
        #     if wt[idx] <= cap:
        #         pick = val[idx] + helper(idx,cap-wt[idx])
        #     dp[idx][cap] =  max(notPick,pick)
        #     return dp[idx][cap]
        
        # return helper(n-1,capacity)
        
        n= len(wt)
        dp = [[0]*(capacity+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(capacity+1):
                notPick = dp[i-1][j]
                pick = float("-inf")
                if wt[i-1] <= j:
                    pick = val[i-1] + dp[i][j-wt[i-1]]
                dp[i][j] = max(notPick,pick)
        return dp[n][capacity]
