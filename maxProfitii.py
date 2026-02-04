class Solution:
    def maxProfit(self, prices):
        # n = len(prices)
        # dp = [[-1]*(2) for _ in range(n)]
        # def helper(idx,buy):
        #     if idx == n:
        #         return 0
        #     if dp[idx][buy] != -1:
        #         return dp[idx][buy]
        #     if(buy):
        #         dp[idx][buy]= max(-prices[idx] + helper(idx+1,0),helper(idx+1,1))
        #         return dp[idx][buy]
        #     else:
        #         dp[idx][buy]= max(prices[idx]+helper(idx+1,1),helper(idx+1,0))
        #         return dp[idx][buy]

        # return helper(0,1)

        # n = len(prices)
        # dp = [[0]*(2) for _ in range(n+1)]
        # for i in range(n-1,-1,-1):
        #     dp[i][1] = max(-prices[i] + dp[i+1][0],dp[i+1][1])
        #     dp[i][0] = max(prices[i] + dp[i+1][1],dp[i+1][0])
        # return dp[0][1]
        profit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
        
