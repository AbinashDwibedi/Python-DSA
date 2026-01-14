class Solution:
    def findPages(arr, k):
        n = len(arr)
        if k > n:
            return -1
        
        left = max(arr)
        right = sum(arr)
        
        def possible(mid):
            summ = 0
            count = 1
            for num in arr:
                if (summ+num) <= mid:
                    summ += num
                else:
                    summ = num
                    count += 1
                    if count > k:
                        return False
            return True
        ans = -1
        while left <= right :
            mid = (left+right)//2
            if possible(mid):
                right = mid-1
                ans = mid
            else:
                left = mid+1
        return ans
                
        