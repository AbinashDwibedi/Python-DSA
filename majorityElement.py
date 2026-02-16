class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num,0) + 1
        for key,value in hashMap.items():
            if value > n//2:
                return key

        candidate = 0
        count = 0
        for num in nums:
            if count == 0 :
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate 