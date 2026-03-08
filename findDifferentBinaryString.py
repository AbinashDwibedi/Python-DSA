class Solution:
    def findDifferentBinaryString(self, nums):
        # n = len(nums)
        # size = 2**n
        # arr = [0]*size
        # for num in nums:
        #     tmp = int(num,2)
        #     arr[tmp]+=1
        # for i in range(size):
        #     if arr[i] == 0:
        #         ans = bin(i)[2:]
        #         return "0"*(n-len(ans)) + ans
        # return "0"*n

        n = len(nums)
        l = []
        for i in range(len(nums)):
            if nums[i][i] == "0":
                l.append("1")
            else:
                l.append("0")
        return "".join(l)