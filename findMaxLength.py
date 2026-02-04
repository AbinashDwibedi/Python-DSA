class Solution:
    def findMaxLength(self, nums) :
        hm = {0:-1}
        max_len = 0
        curr_sum = 0
        for i,num in enumerate(nums):
            if num == 0:
                curr_sum -= 1
            else:
                curr_sum += 1
            
            if curr_sum in hm:
                length = i - hm[curr_sum]
                max_len = max(max_len,length)
            else:
                hm[curr_sum] = i
        return max_len