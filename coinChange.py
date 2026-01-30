class Solution:
    def coinChange(self, coins, amount) :
        # dp = [float('inf')]*(amount+1)
        # dp [0] = 0
        # for i in range(1,amount+1):
        #     for coin in coins:
        #         if i - coin >= 0:
        #             dp[i] = min(dp[i],dp[i-coin]+1)
        # return dp[amount] if dp[amount]!= float('inf') else -1
        

        # n= len(coins)
        # dp = [[-1]*(amount+1) for _ in range(n)]
        # def helper(idx,amt):
        #     if idx == 0:
        #         if amt%coins[idx] == 0:
        #             return amt//coins[idx]
        #         else:
        #             return float("inf")
        #     if dp[idx][amt] != -1:
        #         return dp[idx][amt]
        #     notPick = helper(idx-1,amt)
        #     pick = float("inf")
        #     if coins[idx] <= amt:
        #         pick = 1+ helper(idx,amt-coins[idx])
        #     dp[idx][amt] = min(notPick,pick)
        #     return dp[idx][amt]
        # result = helper(n-1,amount)
        # return result if result != float("inf") else -1

        n = len(coins)
        dp = [[float("inf")]*(amount+1) for _ in range(n)]
        for amt in range(amount+1):
            if amt%coins[0] == 0:
                dp[0][amt] = amt//coins[0]

        for i in range(1,n):
            for amt in range(amount+1):
                notPick = dp[i-1][amt]
                pick = float("inf")
                if coins[i] <= amt:
                    pick = 1+ dp[i][amt-coins[i]]
                dp[i][amt] = min(pick, notPick)
        
        return dp[n-1][amt] if dp[n-1][amt] != float("inf") else -1