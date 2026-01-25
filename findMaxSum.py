
def findMaxSum(self,arr):
    n = len(arr)
    dp = [-1 for _ in range(n)]
    def helper(idx):
        if idx<0:
            return 0
        if dp[idx] != -1:
            return dp[idx]
        dp[idx] = max(helper(idx-1),arr[idx]+helper(idx-2))
        return dp[idx]
    return helper(n-1)