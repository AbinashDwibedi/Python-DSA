def findMin( nums):
        left = 0
        right = len(nums)-1
        mini = float("inf")

        while left<= right:
            mid = (left+right)//2
            if nums[left] <= nums[mid]:
                mini = min(mini,nums[left])
                left = mid+1
                continue
            else:
                mini = min(mini,nums[mid])
                right = mid-1
        return mini