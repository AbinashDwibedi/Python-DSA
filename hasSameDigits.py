class Solution:
    def hasSameDigits(self, s: str) -> bool:
        currS = s
        while len(currS) > 2:
            newS = ""
            for i in range(1,len(currS)):
                val1 = int(currS[i-1])
                val2 = int(currS[i])
                sumi = (val1 + val2) % 10
                newS += str(sumi)
            currS = newS
        return True if currS[0] == currS[1] else False