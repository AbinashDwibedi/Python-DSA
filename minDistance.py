class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[-1]*n for _ in range(m)]

        def helper(i1,i2):
            if i1<0:
                return i2+1
            if i2<0:
                return i1+1
            if dp[i1][i2] != -1:
                return dp[i1][i2]
            if word1[i1] == word2[i2]:
                dp[i1][i2] = helper(i1-1,i2-1)
            else:
                dp[i1][i2] = 1+ min(helper(i1-1,i2),helper(i1,i2-1),helper(i1-1,i2-1))
            return dp[i1][i2]
        
        return helper(m-1,n-1)
#edit distance