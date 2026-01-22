class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.prefix = [nums[0]]
        for i in range(1,len(nums)):
            self.prefix.append(nums[i]+self.prefix[i-1])

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]