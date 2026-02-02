class Solution:
    def minInsertions(self, s: str) -> int:
        sRev = s[::-1]
        lcsR = self.lcs(s,sRev)
        return len(s)-lcsR
    
    def lcs(self,str1:str,str2:str):
        m = len(str1)
        n = len(str2)
        prev = [0]*(n+1)
        for i in range(1,m+1):
            curr = [0]*(n+1)
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j],curr[j-1])
            prev = curr[:]
        return prev[n]
    
