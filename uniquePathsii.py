class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) :

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        dp = [[-1]*(n) for _ in range(m)]
        def helper(idx1,idx2):
            if idx1 >= m or idx2 >= n:
                return 0
            if dp[idx1][idx2] != -1:
                return dp[idx1][idx2]
            if obstacleGrid[idx1][idx2] == 1:
                return 0
            if idx1 == m-1 and idx2 == n-1:
                return 1
            
            dp[idx1][idx2] = helper(idx1,idx2+1)+helper(idx1+1,idx2)
            return dp[idx1][idx2]

        return helper(0,0)