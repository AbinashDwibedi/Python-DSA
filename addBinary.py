class Solution:
    def addBinary(self, a, b):
        result = ""
        i,j= len(a)-1,len(b)-1
        carry =0
        while i >=0 or j>= 0:
            val1 = a[i] if i >= 0 else 0
            val2 = b[j] if j >=0 else 0
            sumi = int(val1) + int(val2) + carry
            result += str(sumi % 2)
            carry = sumi // 2
            i -= 1
            j -= 1
        if carry>0:
            result += str(carry)
        return "".join(reversed(result))