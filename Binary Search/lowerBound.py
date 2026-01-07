def lowerBound( arr, target):
        left = 0
        right = len(arr)-1
        ans = -1
        while left <= right:
            mid = (left+right) // 2
            
            if arr[mid] >= target:
                ans = mid
                right = mid -1
            else:
                left = mid+1
        return len(arr) if ans == -1 else ans