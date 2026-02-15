class Solution:
    def maxFrequencyElements(self, nums):
        hm = {}
        maxi = 0
        for num in nums:
            hm[num] = hm.get(num,0)+1
            maxi = max(maxi,hm[num])

        sumi = 0
        for key,value in hm.items():
            if value == maxi:
                sumi += value
        return sumi