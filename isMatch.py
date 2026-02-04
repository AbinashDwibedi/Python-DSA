from functools import lru_cache
# instead of creating a dp array iam using the inbuilt cache function
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        @lru_cache(None)
        def helper(i1,i2):
            if i2<0 and i1<0:
                return True
            if i2<0:
                return False
            if i1<0:
                for k in range(i2+1):
                    if p[k] != "*":
                        return False
                return True
            if s[i1]==p[i2] or p[i2] == "?":
                return helper(i1-1,i2-1)
            if p[i2] == "*":
                return helper(i1-1,i2) or helper(i1,i2-1)
            return False
        return helper(m-1,n-1)