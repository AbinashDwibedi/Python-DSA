class Solution:
    def isIsomorphic(self, s, t):
        m = len(s)
        n = len(t)
        hs1 = {}
        hs2 = {}
        if m != n:
            return False
        
        for i in range(m):
            if s[i] not in hs1:
                hs1[s[i]] = i
            if t[i] not in hs2:
                hs2[t[i]] = i
            if hs1[s[i]] != hs2[t[i]]:
                return False
        return True