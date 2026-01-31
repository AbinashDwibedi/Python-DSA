class Solution:
    def change(self, amount, coins) :
        n = len(coins)
        dp = [[-1]*(amount+1)for _ in range(n)]
        def helper(idx,amt):
            if idx < 0:
                if amt == 0:
                    return 1
                else:
                    return 0
            if dp[idx][amt]!=-1:
                return dp[idx][amt]
            notPick = helper(idx-1,amt)
            pick = 0
            if coins[idx] <= amt:
                pick = helper(idx,amt-coins[idx])
            dp[idx][amt] = notPick + pick
            return dp[idx][amt]
        return helper(n-1,amount)