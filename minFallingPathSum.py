class Solution:
    def minFallingPathSum(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        dp = [[float("inf")] * (n + 2) for _ in range(m)]
        dp[m-1][1:n+1] = matrix[m-1]
        for i in range(m-2, -1, -1):
            for j in range(n):
                left = dp[i+1][j]
                mid  = dp[i+1][j+1]
                right= dp[i+1][j+2]
                dp[i][j+1] = matrix[i][j] + min(left, mid, right)

        return min(dp[0][1:n+1])
