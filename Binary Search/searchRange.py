def searchRange(nums, target):
        left = 0
        right = len(nums)-1
        lans = -1
        rans = -1
        while left <= right :
            mid = (left+right) // 2
            if nums[mid] == target:
                rans = mid
                right = mid-1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        left = 0 
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                lans = mid
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return [rans,lans]