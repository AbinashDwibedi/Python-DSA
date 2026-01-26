class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*(n) for _ in range(m)]
        def helper(idx1,idx2):
            if idx1>=m or idx2>=n:
                return 0
            if dp[idx1][idx2] != -1:
                return dp[idx1][idx2]
            if idx1 == m-1 or idx2 == n-1:
                return 1
            
            dp[idx1][idx2]= helper(idx1,idx2+1) + helper(idx1+1,idx2)
            return dp[idx1][idx2]
        return helper(0,0)