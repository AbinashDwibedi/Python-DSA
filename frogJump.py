class Solution:
    def canCross(stones):
        stoneSet = set(stones)
        lastStone = stones[-1]
        memo = set()

        def dfs(pos,k):
            if (pos,k) in memo:
                return False
            if pos == lastStone:
                return True
            for i in (k-1,k,k+1):
                if i>0 and i+pos in stoneSet:
                    if dfs(i+pos,i):
                        return True
            memo.add((pos,k))
            return False
        return dfs(0,0)
