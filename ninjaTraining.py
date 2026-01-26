
def ninjaTraining(n, points):
    # Write your code here.
    # dp=[[-1]*(3) for _ in range(n)]
    # def helper(idx,t):
    #     if idx == n:
    #         return 0
    #     if dp[idx][t] != -1:
    #         return dp[idx][t]
    #     maxi = float("-inf")
    #     for i in (0,1,2):
    #         if t == -1 or i != t:
    #             maxi = max(points[idx][i] + helper(idx+1,i),maxi)
    #     dp[idx][t] = maxi
    #     return maxi
    # return helper(0,-1)
    
    dp = [[0]*(4) for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        for l in range(4):
            maxi = float("-inf")
            for j in range(3):
                if j != l:
                    maxi = max(maxi,points[i][j]+dp[i+1][j])
            dp[i][l] = maxi
              
    return dp[0][3]
