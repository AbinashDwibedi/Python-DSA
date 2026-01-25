class Solution:
    def rob(self, nums):

        n = len(nums)
        if n == 1:
            return nums[0]

        arr1 = nums[:n-1]
        arr2 = nums[1:n]

        return max(self.findMaxSum(arr1), self.findMaxSum(arr2))

    def findMaxSum(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        dp = [0] * n
        dp[0] = max(0, arr[0])

        for i in range(1, n):
            take = arr[i] + (dp[i-2] if i > 1 else 0)
            notTake = dp[i-1]
            dp[i] = max(take, notTake)

        return dp[n-1]
