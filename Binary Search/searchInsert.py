def searchInsert(nums, target) :
        left = 0
        right = len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left+ right) //2

            if nums[mid] >= target:
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return len(nums) if ans == -1 else ans
# same logic as lower bound