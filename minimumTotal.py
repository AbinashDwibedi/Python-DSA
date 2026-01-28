class Solution:
    def minimumTotal(self, triangle):
        # m = len(triangle)
        # dp = [[-1]*(i+1) for i in range(m)]
        # def helper(idx1,idx2):
        #     if idx1 == m-1:
        #         return triangle[idx1][idx2]
        #     if dp[idx1][idx2] != -1:
        #         return dp[idx1][idx2]
        #     dp[idx1][idx2] = triangle[idx1][idx2] + min(helper(idx1+1,idx2),helper(idx1+1,idx2+1))
        #     return dp[idx1][idx2] 
        # return helper(0,0)

        dp = triangle[-1][:]
        n = len(triangle)
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j],dp[j+1])
        return dp[0]










