class Solution:
    def repeatedNTimes(self, nums):
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i-1] == nums[i]:
        #         return nums[i]
        # return 0

        #using set 
        seto = set()
        for num in nums:
            if num in seto:
                return num
            seto.add(num)