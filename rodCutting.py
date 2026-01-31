class Solution:
    def cutRod(self, price):
        # n = len(price)
        # dp = [[-1]*(n+1) for _ in range(n)]
        # def helper(idx,sz):
        #     if idx == 0:
        #         return sz * price[idx]
        #     if dp[idx][sz] != -1:
        #         return dp[idx][sz]
        #     notTake = helper(idx-1,sz)
        #     take = float("-inf")
        #     if idx+1 <= sz:
        #         take = price[idx] + helper(idx,sz-(idx+1))
        #     dp[idx][sz] = max(notTake,take)
        #     return dp[idx][sz]
        # return helper(n-1,n)
        
        n = len(price)
        dp = [0] * (n + 1)

        for sz in range(n + 1):
            dp[sz] = sz * price[0]

        for idx in range(1, n):
            for sz in range(idx + 1, n + 1):
                dp[sz] = max(
                    dp[sz],
                    price[idx] + dp[sz - (idx + 1)]
                )

        return dp[n]