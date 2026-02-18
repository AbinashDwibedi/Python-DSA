class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binData = bin(n)
        curr = binData[2]
        for i in range(3,len(binData)):
            if curr == binData[i]:
                return False
            else:
                curr = binData[i]
        return True